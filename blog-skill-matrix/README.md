# Blog Skill Matrix

[简体中文](README.zh-CN.md) · Version 0.14.0 · [MIT license](LICENSE)

**Start with a reader's question. Deliver a useful article, relevant images, and copy-ready publishing pages.**

A connected workflow for brand content, multilingual SEO, and third-party blog platforms. It covers topics, research, writing, images, quality checks, and human publishing handoff while reducing repeated research, reviews, and file maintenance. Content quality, owner requirements, and task cost matter together. Publication remains human-operated.

[Core capabilities](#why-use-this-matrix) · [Deliverables](#what-you-get) · [Workflow](#workflow) · [Task cost](#how-task-cost-is-controlled) · [Getting started](#getting-started)

## Why use this matrix?

- **Write for a specific reader problem.** Shape the topic around who needs what answer, then deliver useful explanations, steps, or choices. Connect product recommendations to the actual task.
- **Localize SEO with evidence.** Preserve required keyword meanings, prefer applicable brand wording, and check regional natural variants. Titles foreground distinct questions rather than sharing a repeated long prefix.
- **Match both brand and platform.** Align voice and illustration style with brand references. Assess audience language and content fit from actual platform articles, strictly within the owner's supplied scope.
- **Use images to explain.** Place body images next to the methods they clarify and provide a separate cover. Inspect actual final images, not merely file presence.
- **Review the finished article.** An optional independent R examines the visual payload, real images, and material sources. Fix real issues without routinely turning a local change into a new full review.
- **Make human publishing easier.** Prepare matching HTML/Markdown, Chinese insertion notes, visible localized alt, SEO fields, and an excerpt in a consistent order.
- **Reduce workflow overhead.** Reuse shared evidence and a small agent pool; let code organize and count. Keep more work focused on the article instead of repeated handoffs.

## What you get

A page you can open, select, and copy into a rich-text editor—not a publishing handoff that requires reading HTML source.

| Deliverable | Purpose |
| --- | --- |
| Visual HTML publishing page | Copy title and body separately, with exact-position Chinese insertion notes and visible localized alt |
| Matching Markdown page | Use in a Markdown editor or as a readable fallback |
| Numbered PNG/JPG/JPEG body images | Match adjacent sections and the confirmed quantity/coverage |
| Separate cover image | Reflect the article and brand without replacing a body image |
| SEO title, tags, and description | Retrieve individual fields at the bottom |
| Excerpt | A separate reader-facing summary for platform cards or excerpt fields |

The layout stays simple and consistent: **title → body and image notes → SEO fields → excerpt**. There are no copy buttons.

One draft and one asset set support the delivery. Authors do not manually retell the same body, metadata, and image list in multiple files. Necessary source notes stay with the draft; passing review is brief and problems are recorded when they exist.

## Workflow

```text
G: research and writing proposal
        ↓
Owner confirms the complete scope
        ↓
W: article, images, cover, and built/checked HTML + Markdown payloads
        ↓
Follow one confirmed quality route:
  ├─ Default self-review: W checks the complete delivery in the same context
  └─ Independent review: R checks the final payload, images, and sources
        ↓ Quality passed
G: verify original requirements and hand off to the publisher
        ↓
Human publishes and returns URL + accepted / needs-fix verdict
        ↓ After human acceptance
Same G: read-only public-page check
        ↓ Check passed
Complete: human acceptance + public verification

Platform issue → Human repair → Accepted again → Same G checks affected items
```

Choose one quality route. Independent R replaces W's formal full self-review. Platform repairs do not restart the writing/review cycle.

| Role | Responsibility |
| --- | --- |
| G: `blog-gate` | Research coordination, requirement confirmation, writer dispatch, fidelity acceptance, and public QA |
| W: `blog-writer` | Continuous research, keyword localization, writing, images, and payload production |
| R: `blog-review` (optional) | Owner-selected independent review of the rendered final payload, images, cover, and material sources |

R receives built and mechanically checked HTML/Markdown payloads, not a draft waiting to be formatted. It checks reader value, facts, SEO and language, image accuracy, recommendations and links, and delivery usability. G accepts the reviewed version before it is handed to the publisher.

### When a real issue is found

```text
Real issue
   → Original W fixes and rebuilds the payload
   → Same W or R checks changes and their direct dependencies
   → Once resolved, return to G acceptance
```

Unresolved material issues or scope changes require an owner decision, not approval. Article changes return to the original writer; platform transport repairs remain human-operated. An earlier verdict does not automatically cover a new build.

## How task cost is controlled

Cost is one design priority, not the sole objective. Article count, research/localization difficulty, model choice, context, repairs, and image requirements determine actual usage. There is no promised fixed article price or unmeasured saving percentage.

| Route | Main model work per article | Trade-off |
| --- | --- | --- |
| Default: author self-review | W continuously prepares the article, images, and payloads, then checks them in the same context | Less independent handoff and repeated background loading |
| Optional: independent review | W continuously produces the article; a reusable R reviews the final payload once | Additional independent reading and image inspection, with a non-author perspective |

Both routes share G's batch coordination and requirement acceptance. Public QA follows actual URL-return batches. Independent R replaces the author's formal full self-review rather than being added on top; these arrangements are not fixed API-call counts or token bills.

Reuse applicable evidence, build two payloads from one Markdown draft, and use code for counting and consistency. Verify real changes, omit all-green reports, and stop repeated work while waiting for human input. Ordinary articles retain one full quality check; lower overhead does not mean dropped requirements.

Research, writing, actual image inspection, and necessary repairs still consume model usage. Image generation may carry a separate charge; body images and the extra cover follow confirmed specifications. Tool calls, result reading, and human publishing also have costs. Parallelism reduces waiting but does not guarantee fewer tokens.

## Getting started

Once the matrix is connected to your local skill-capable tool, start with `$blog-gate`. Adapt this request to your task:

```text
$blog-gate

Brand and target page: <product-page URL>
Candidate platforms: <my supplied list or file>
Article count: 3, each on a different platform
Keywords: <required meanings and supporting angles>
CTA: <exact anchor, URL, and founder disclosure>
Images: <body-image quantity, ratio, and style; plus a cover>

First report each article's research, language/platform fit, and writing plan.
Wait for my confirmation before writing.
Use independent review: a reusable R reviews the finished visual payload
and actual images. Fix real issues; do not routinely rereview the whole article.
Deliver HTML, Markdown, images, SEO fields, and an excerpt for human publication.
```

Independent review is an explicit choice in this example, not an automatic extra stage. To use the default route, ask for author self-review without independent R.

For initial setup, retain the complete `blog-skill-matrix` directory, including internal helpers, templates, and references, and register only the three skill entrypoints. Copying three `SKILL.md` files alone is insufficient. Follow your tool's local skill installation mechanism.

## Content quality and task boundaries

- **Evidence-based platform and language fit.** Research only owner-supplied candidates and obtain confirmation. Use actual homepage/trending/popular/featured articles to establish audience language—not UI language, old accounts, or text-display capability. Never silently add or replace platforms.
- **SEO for a specific reader problem.** Preserve all required keyword meanings per article, foreground distinct questions in titles, and avoid a repeated long prefix. Use descriptive H2/H3 headings, not density quotas. Prefer applicable localized brand wording, then regional variants, then documented translation fallback. Optional Trends is not proof of search volume or local demand.
- **Independent reader value.** Provide useful answers and supported facts. Keep product recommendations secondary while preserving the specified CTA, anchors, URLs, and disclosure. Respect owner-specified multiple links without inventing caps or promising ranking, indexing, or retention.
- **Images that explain the method.** Inspect every final image and cover for adjacency, accurate method, example continuity, and brand fit. File existence and dimensions do not establish visual quality.
- **Local delivery is not publication.** The matrix does not enter article editors, upload images, save drafts, or publish automatically. Account preparation needs [separate authorization](docs/account-preparation.md). Completion requires human acceptance and public verification.

## Runtime and further reading

Use an environment with local skills and file tools, plus Python 3.9+. Markdown building requires `markdown-it-py==3.0.0`; install it in an isolated environment where appropriate:

```sh
python -m pip install -r skills/blog-human-handoff/scripts/requirements.txt
```

Internal directory names remain for code compatibility, not as extra skill entrypoints. Existing `campaign.json`/package/index workspaces keep their historical contracts and are not automatically migrated.

- [Short workflow](docs/workflow-core.md): task order and boundaries; reread after context compression.
- [Authoring and tools](skills/blog-writer/references/markdown-authoring.md): draft format and build/check commands.
- [Editorial standard](skills/blog-writer/references/editorial-standard.md): reader value, keywords, images, and recommendations.
- [Platform matching](skills/blog-gate/references/platform-matching.md): audience and delivery fit within the supplied candidates.
- [Historical compatibility](README.legacy.md): conditional legacy guidance, not a new-task prerequisite.

[MIT license](LICENSE). Improvements grounded in actual articles, publisher rework, and reproducible issues are welcome. Unmeasured savings or ranking gains are not capability guarantees.
