"""Exercise the lightweight route without initializing any campaign harness."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_lean_authoring import png

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/blog-writer/scripts/build_release.py"


@unittest.skipUnless(importlib.util.find_spec("markdown_it"), "Markdown dependency required")
class LightweightMatrixTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.plan_path = self.workspace / "task-plan.json"
        self.plan = {
            "shared": {
                "focus_keyword": "example workflow",
                "cta": {"product_name": "Example Product", "anchor_text": "Try Example Product",
                    "product_destination_url": "https://example.com/product",
                    "relationship_disclosure": "Disclosure: I am the founder."},
            },
            "articles": [{"article_id": "A01", "platform": "owner-supplied-platform",
                "language": "en", "reader_task": "Prepare and inspect an example."}],
        }
        self.write_plan()
        self.receipt = self.workspace / "owner-confirmation.txt"
        self.receipt.write_text("Confirm the displayed one-article test plan.", encoding="utf-8")
        self.article = self.workspace / "articles/A01"
        (self.article / "canonical").mkdir(parents=True)
        (self.article / "images").mkdir()
        images = []
        for index, zone in enumerate(("lead", "middle", "closing"), 1):
            file = self.article / f"images/{index:02d}-{zone}-example.png"
            png(file, (index * 40, 10, 50))
            images.append({"file": str(file.relative_to(self.article)),
                "alt": "Example " + zone, "caption": "Editorial explanation."})
        png(self.article / "images/00-cover-example.png", (10, 100, 120))
        self.front = {
            "seo_title": "Example workflow: prepare and inspect", "tags": ["example"],
            "description": "Prepare and inspect one example.",
            "excerpt": "A practical introduction to preparing inputs and inspecting the result.",
            "images": images,
            "cover": {"file": "images/00-cover-example.png", "alt": "Example cover"},
            "research": {"keyword_basis": "CURRENT_BRAND_SITE", "keyword_refs": ["PRODUCT"],
                "sources": [{"id": "PRODUCT", "url": "https://example.com/product",
                    "notes": "Fixture, not a verified product."}], "claims": []},
        }
        self.body = (
            "# Example workflow: prepare and inspect\n\n"
            "Start with one example.\n\n<!-- BLOG_3P_IMAGE:01 -->\n\n"
            "## Prepare the input\n\nKeep the input clear.\n\n<!-- BLOG_3P_IMAGE:02 -->\n\n"
            "## Inspect the result\n\nCheck the result.\n\n<!-- BLOG_3P_IMAGE:03 -->\n\n"
            "[Try Example Product](https://example.com/product).\n\nDisclosure: I am the founder.\n"
        )
        self.write_draft()

    def write_plan(self):
        self.plan_path.write_text(json.dumps(self.plan), encoding="utf-8")

    def write_draft(self):
        (self.article / "canonical/article.md").write_text(
            "---json\n" + json.dumps(self.front) + "\n---\n" + self.body, encoding="utf-8")

    def run_script(self, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), "--plan", str(self.plan_path), *extra],
            text=True, capture_output=True)

    def freeze(self):
        result = self.run_script("--freeze", "--receipt-file", str(self.receipt),
            "--source", "test-owner-message")
        self.assertEqual(result.returncode, 0, result.stderr)

    def build(self, *extra):
        return self.run_script("--article-id", "A01", *extra)

    def test_build_and_check_without_campaign_or_review_state(self):
        self.freeze()
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("BUILT_NOT_QUALITY_APPROVED", result.stdout)
        self.assertEqual(self.build("--check").returncode, 0)
        self.assertFalse((self.workspace / "campaign.json").exists())
        self.assertFalse((self.workspace / "state.json").exists())
        self.assertFalse((self.article / "reviews").exists())
        self.assertFalse((self.article / "article-package.json").exists())
        html = (self.article / "handoff/visual-payload.html").read_text()
        markdown = (self.article / "handoff/visual-payload.md").read_text()
        self.assertIn('lang="en"', html)
        self.assertIn("【图片 02", html)
        self.assertIn("【图片 02", markdown)
        self.assertIn("Alt：Example middle", html)
        self.assertLess(html.index("Keep the input clear."), html.index("【图片 02"))
        self.assertNotIn("<script", html)
        files = {str(p.relative_to(self.article)): p.read_bytes()
            for p in self.article.rglob("*") if p.is_file()}
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(files, {str(p.relative_to(self.article)): p.read_bytes()
            for p in self.article.rglob("*") if p.is_file()})

    def test_no_binding_or_changed_owner_plan_rejects_build(self):
        self.assertNotEqual(self.build().returncode, 0)
        self.freeze()
        self.plan["articles"][0]["platform"] = "unconfirmed-replacement"
        self.write_plan()
        self.assertNotEqual(self.build().returncode, 0)
        self.assertFalse((self.article / "handoff").exists())

    def test_scope_duplicates_and_unknown_article_are_rejected(self):
        duplicate = copy.deepcopy(self.plan["articles"][0])
        duplicate["article_id"] = "A02"
        self.plan["articles"].append(duplicate)
        self.write_plan()
        result = self.run_script("--freeze", "--receipt-file", str(self.receipt), "--source", "test")
        self.assertNotEqual(result.returncode, 0)
        self.plan["articles"].pop()
        self.write_plan()
        self.freeze()
        self.assertNotEqual(self.run_script("--article-id", "../A01").returncode, 0)

    def test_original_cta_disclosure_and_confirmed_link_counts(self):
        self.plan["shared"]["link_policy"] = {"target_link_count": 1}
        self.write_plan()
        self.freeze()
        self.assertEqual(self.build().returncode, 0)
        self.body += "\n[Source](https://example.com/product)\n"
        self.write_draft()
        self.assertNotEqual(self.build().returncode, 0)
        self.body = self.body.replace("[Source](https://example.com/product)", "Source")
        self.body = self.body.replace("Disclosure: I am the founder.", "")
        self.write_draft()
        self.assertNotEqual(self.build().returncode, 0)

    def test_cover_and_markers_not_replaced_by_file_presence(self):
        self.freeze()
        self.front.pop("cover")
        self.write_draft()
        self.assertNotEqual(self.build().returncode, 0)
        self.front["cover"] = {"file": "images/00-cover-example.png", "alt": "Example cover"}
        self.body = self.body.replace("<!-- BLOG_3P_IMAGE:02 -->", "")
        self.write_draft()
        self.assertNotEqual(self.build().returncode, 0)

    def test_current_pair_and_image_change_requires_rebuild(self):
        self.freeze()
        self.assertEqual(self.build().returncode, 0)
        markdown = self.article / "handoff/visual-payload.md"
        markdown.write_text(markdown.read_text().replace("Try Example Product", "Changed CTA"))
        self.assertNotEqual(self.build("--check").returncode, 0)
        self.assertEqual(self.build().returncode, 0)
        png(self.article / "images/02-middle-example.png", (120, 80, 30))
        self.assertNotEqual(self.build("--check").returncode, 0)
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(self.build("--check").returncode, 0)

    def test_explicit_wr_preserved_and_legacy_workspace_not_migrated(self):
        self.plan["articles"][0]["review_route"] = "WR"
        self.write_plan()
        self.freeze()
        self.assertEqual(self.build().returncode, 0)
        manifest = json.loads((self.article / "handoff/.build.json").read_text())
        self.assertEqual(manifest["review_route"], "WR")
        self.assertNotIn("approved", manifest)
        (self.article / "article-package.json").write_text("{}")
        self.assertNotEqual(self.build().returncode, 0)

    def test_excerpt_is_separate_visible_and_identical_in_both_payloads(self):
        self.front["excerpt"] = 'A reader "summary" & a useful next step.'
        self.write_draft()
        self.freeze()
        self.assertEqual(self.build().returncode, 0)
        html = (self.article / "handoff/visual-payload.html").read_text()
        markdown = (self.article / "handoff/visual-payload.md").read_text()
        self.assertIn('id="article-excerpt"', html)
        self.assertIn('A reader &quot;summary&quot; &amp; a useful next step.', html)
        self.assertIn('- Excerpt（文章摘要）：' + self.front["excerpt"], markdown)
        self.assertIn('- Description：' + self.front["description"], markdown)
        self.assertLess(html.index('id="seo-description"'), html.index('id="article-excerpt"'))
        self.assertNotIn(self.front["excerpt"], html.split('</article>', 1)[0])
        self.assertEqual(self.build("--check").returncode, 0)

    def test_new_payload_requires_own_nonempty_excerpt(self):
        self.freeze()
        for value in (None, "", "   ", 42):
            with self.subTest(value=value):
                if value is None:
                    self.front.pop("excerpt", None)
                else:
                    self.front["excerpt"] = value
                self.write_draft()
                result = self.build()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("excerpt", result.stderr)
        self.assertFalse((self.article / "handoff").exists())

    def test_excerpt_change_or_independent_edit_invalidates_current_build(self):
        self.freeze()
        self.assertEqual(self.build().returncode, 0)
        self.front["excerpt"] = "Updated reader summary."
        self.write_draft()
        self.assertNotEqual(self.build("--check").returncode, 0)
        self.assertEqual(self.build().returncode, 0)
        markdown = self.article / "handoff/visual-payload.md"
        markdown.write_text(markdown.read_text().replace("Updated reader summary.", "Other summary."))
        self.assertNotEqual(self.build("--check").returncode, 0)


if __name__ == "__main__":
    unittest.main()
