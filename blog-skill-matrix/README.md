# Blog Skill Matrix

[简体中文](README.zh-CN.md) · Version 0.14.0 · [MIT license](LICENSE)

A compact workflow for useful, evidence-bounded SEO articles and human-native publishing. This revision reduces entrypoints and duplicate bookkeeping. It does not merge G with R, change model settings, or grant publication permission.

## Components

| Component | Responsibility |
| --- | --- |
| `blog-gate` | Consolidate research and the complete pre-write proposal, obtain owner confirmation, dispatch writers, verify requirement fidelity, and inspect public pages |
| `blog-writer` | Continuously research, localize keywords, write, create images, build payloads, and perform one integrated quality check |
| `blog-review` (optional) | Independent review only when explicitly selected by the owner |
| Internal resources | Matching guidance belongs to G; editorial references, templates, and deterministic building/checking belong to W |

Start with `$blog-gate`. WQ remains same-context author self-review. WR remains an owner-explicit independent R. Material risks do not automatically create a reviewer.

## End-to-end flow

Research and proposal → owner confirmation → W writes, prepares images, and builds/checks the final HTML and Markdown payloads → WQ author QA or an explicitly selected independent R reviews the final visual payload → G verifies original requirements and hands off the approved version → human publication → the same G checks public-page transport.

Sending payloads to R is internal review, not approval for human release. R inspects the rendered final page and actual final images, not only the draft or source code. Subsequent changes require affected-content and dependency verification; an earlier verdict does not silently approve a new build. This does not add another review round or version report.

Use a small pool of visible reusable writers for disjoint article paths. G owns shared requirements and progress. Do not create a new role for every stage or a worktree merely to fill capacity.

## Minimal authoring and delivery

Keep one `task-plan.json` for shared requirements and per-article differences, plus the actual owner confirmation. The plan template is `templates/task-plan.json`. Proposed outlines and stylistic preferences do not become requirements automatically.

Each author maintains `articles/<ID>/canonical/article.md` and image files. The Markdown includes SEO information, image placement/alt/captions, and necessary source notes. A deterministic tool generates paired `handoff/visual-payload.html` and `handoff/visual-payload.md`, with a small hidden consistency record; authors do not duplicate metadata or manually construct page shells.

The payload shows title, body with exact-position Chinese insertion notes and visible localized alt, then SEO title/tags/description and a separate Excerpt (article summary). New drafts provide the excerpt independently of the search description. There are no copy buttons. Images are numbered PNG/JPG/JPEG files. A separate cover is provided by default and does not replace a body image.

One quality check covers the final article and actual final images. Fix real defects and inspect affected dependencies rather than routinely rereading everything. Passing output is short; record actual issues, not all-green reports. G verifies the owner requirements against delivery without repeating semantic review.

After context compression, first reread the [short workflow](docs/workflow-core.md). Use the [authoring guide](skills/blog-writer/references/markdown-authoring.md) for formats and commands and the [editorial standard](skills/blog-writer/references/editorial-standard.md) when relevant.

## Requirements and evidence

Platforms must come from the owner's supplied and confirmed scope, with distinct per-article mappings. Establish the predominant language from actual homepage/trending/popular/featured articles; UI language, past accounts, and text transport are not audience evidence. Report conflicts rather than silently replacing platforms or forcing a mismatched language.

Preserve all owner-required keyword meanings per article. Prefer applicable localized brand wording, then regional natural variants, then documented translation fallback when checks find no consensus. Titles foreground distinct reader problems instead of repeating a long prefix. Literal matching applies only to explicitly locked wording; there are no density quotas. Optional English-only Google Trends is relative global context, not search volume or proof of local demand.

Articles must be independently useful. The required CTA remains a secondary, specific, transparent recommendation with its exact required anchor, URL and disclosure. Count target-site introduction, recommendation and source links together by occurrence; impose only owner-confirmed quantities. Multiple specified anchors are not prohibited categorically, but useful content and local checks cannot guarantee retention or search-policy acceptance. Inspect images for actual method accuracy and brand fit.

## Runtime and compatibility

Python 3.9+. The Markdown route requires `markdown-it-py==3.0.0`; the dependency file remains at `skills/blog-human-handoff/scripts/requirements.txt`. New projects do not need the legacy harness initializer, dispatch gates, review indexes, or package acceptance chain.

The four retired directories retain internal code or legacy material, not discoverable skill entrypoints. Existing `campaign.json`/package/index projects retain their confirmed historical semantics and are not silently migrated. [README.legacy.md](README.legacy.md) contains conditional legacy commands, not requirements for new tasks.

Publication remains human-only. Registration/login and minimal setup need [separate account authorization](docs/account-preparation.md); they never permit article input, media upload, drafts, publication, deletion or fingerprint changes. Mechanical success is not a quality verdict or proof of owner identity. After human acceptance, the same G performs bounded public transport QA without reopening W/R; completion requires both acceptance and public verification.

There is no promised saving percentage. Evaluate ordinary-article runs and actual publisher rework.
