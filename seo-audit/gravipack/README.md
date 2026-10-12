# Gravipack SEO audit (claude-seo)

Audit of `http://gravipack.fr/` → live brand store `gravipack.com`, run with the [claude-seo](https://github.com/AgriciDaniel/claude-seo) toolkit (v2.4.2) on 2026-10-12.

| File | What it is |
|---|---|
| [FULL-AUDIT-REPORT.md](FULL-AUDIT-REPORT.md) | Executive summary, scores, and all 45 findings. Each finding has its severity, impact (1-10), effort, evidence, why it matters, effect on SEO, a step-by-step fix, and checks for monitoring and falsifiability. |
| [ACTION-PLAN.md](ACTION-PLAN.md) | The findings sequenced into phases (Day 1 → Week 1 → Weeks 2-3 → Month 2 → Ongoing), with owners, dependencies and KPIs. |
| [ONSITE-AUDIT-PENDING.md](ONSITE-AUDIT-PENDING.md) | The checks that need the live site (blocked in the audit sandbox), with the exact `/seo` commands to run. |
| `FULL-AUDIT-REPORT.pdf` | A PDF of the report, made by claude-seo's `google_report.py` (if present). |
| [audit-data.json](audit-data.json) | Data file in claude-seo's format, used to generate the PDF/HTML/XLSX reports. |
| [findings.json](findings.json) | The 45 final findings, the scores and the merge map back to the 142 raw findings. |
| [findings/](findings/) | Raw output from each specialist (phase 1 and phase 2), with the fact-checker's verdict on each finding. |
| [appendix/](appendix/) | Data tables: URL inventory (114 URLs), SERP analysis (32 keywords), keyword clusters, site architecture, 3 content briefs, mention inventory, registry and entity facts, marketplace price comparison. |

**Scores:**

- **Provisional SEO Health Score: 33/100.** This covers only the 75 % of claude-seo's weighting that can be measured from search evidence.
- **Off-site visibility score: 35/100.**

**Findings:** 3 High, 26 Medium, 15 Low and 1 Info. None is Critical, because nothing in the evidence proves an indexing block or a penalty.

**Limitation:** the audit sandbox could not reach the site. Everything here comes from search-engine evidence: about 360 searches of indexed URLs, titles as shown in results, third-party sites and public registries. Schema, Core Web Vitals and images are not yet scored. Robots.txt, sitemaps and redirects are unchecked, so Technical SEO is only partly scored. See `ONSITE-AUDIT-PENDING.md` for the checks still to run.
