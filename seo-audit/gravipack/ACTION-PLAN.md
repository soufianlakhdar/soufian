# Gravipack — SEO Action Plan

Date: 2026-10-12 · Source: [FULL-AUDIT-REPORT.md](FULL-AUDIT-REPORT.md) (numbers `#n` refer to findings there)

## Phase 0: Unblock the on-site crawl — Day 1

*Goal:* Allow gravipack.fr/.com hosts in the audit environment and run the pending claude-seo on-site commands (ONSITE-AUDIT-PENDING.md) to score Schema, Performance, Images and finalise Technical SEO.

| # | Action | Severity | Impact | Effort | Owner | Do after |
|---|---|---|---|---|---|---|

## Phase 1: Critical fixes (index consolidation, claim compliance, reputation triage) — Week 1

*Goal:* One canonical host, no junk URLs in the index, compliant health wording, and every negative review answered.

| # | Action | Severity | Impact | Effort | Owner | Do after |
|---|---|---|---|---|---|---|
| #5 | gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com | 🟡 Medium | 6 | Low | dev | — |
| #4 | Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation | 🟡 Medium | 7 | Medium | content + legal | #1 |
| #7 | The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles | 🟡 Medium | 6 | Medium | dev | #5 |
| #29 | Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=) | 🟡 Medium | 4 | Low | dev | #5 |
| #16 | The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages | 🟡 Medium | 5 | Medium | dev | #5, #7 |
| #28 | Other brand storefronts and hosts (gravipack.ma, gravipacker.com, a probable agency staging host) show different catalogues, model names and prices | 🟡 Medium | 4 | Medium | dev | #5 |
| #3 | Review and 'arnaque' searches surface critical content the brand has not answered (Trustpilot 3.1/5 with unanswered 2026 complaints, the Outzer review, sceptical forum threads) | 🟠 High | 7 | Medium | management + customer service | #23 |
| #23 | Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards) | 🟡 Medium | 4 | Low | management + customer service | — |
| #27 | On-site social-proof figures ('4,7 sur Google' from 1,121-1,175 reviews, '500 000 clients satisfaits') are not independently verified | 🟡 Medium | 4 | Low | management + customer service | #30 |
| #41 | Pre-order dates that have already passed may still be live on product pages, and news posts show no dates in search snippets (verify on-site) | 🔵 Low | 3 | Low | content + legal | #7 |

## Phase 2: High-impact on-page & commerce fixes — Weeks 2-3

*Goal:* Rewrite titles/slugs, de-cannibalise, win back model and brand SERPs, publish the evidence page, align prices/specs across channels, add schema.

| # | Action | Severity | Impact | Effort | Owner | Do after |
|---|---|---|---|---|---|---|
| #11 | Title tags are over-long, carry a bloated site-wide suffix and stacked claim keywords, and sometimes omit the model name or contain typos | 🟡 Medium | 6 | Medium | content + dev | #4, #9 |
| #9 | Dozens of pages target the same 'anti mal de dos' and 'exosquelette' terms, so the home page, category hub and product pages compete | 🟡 Medium | 6 | Medium | content + dev | #7, #4 |
| #2 | Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model names (Sherpa, Hiking 33, Feather, Business Talk) | 🟠 High | 7 | Medium | management + e-commerce | #7, #21 |
| #6 | Segment categories rank mainly for 'anti mal de dos' wordings and miss the market's generic head terms (sac à dos ergonomique, cartable ergonomique, sac randonnée léger…) | 🟡 Medium | 6 | Medium | content + dev | #9, #4 |
| #1 | The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank | 🟠 High | 8 | High | content + legal | #16 |
| #20 | Prices differ across channels and on gravipack.com itself, with struck 'reference' prices almost everywhere | 🟡 Medium | 5 | Medium | management + e-commerce | #7 |
| #21 | Model names, capacities, weights and warranty terms conflict across channels, and some specs are publicly disputed | 🟡 Medium | 5 | Medium | management + e-commerce | — |
| #17 | Who sells, makes and services Gravipack products is not explained, and partner listings are partly outside the brand's control | 🟡 Medium | 5 | Medium | management + e-commerce | #23 |
| #13 | For 'gravipack', an obsolete 2020 crowdfunding page comes first and the home page ranked only #6-#9 in the results we sampled | 🟡 Medium | 5 | Medium | management + customer service | #29, #3, #23 |
| #36 | Low-value archives and duplicate CMS pages are indexed (attribute/tag archives, a /category/ base, a /test/ copy, duplicate contact pages) | 🔵 Low | 3 | Low | dev | #5 |
| #44 | Product slugs are very long and keyword-stuffed, and some contain typos or '-copie' leftovers | 🔵 Low | 2 | Low | content + dev | #7, #4 |
| #30 | Product, Offer and review markup and the Merchant Center setup cannot be verified, and the Content API for Shopping has been sunset (verify on-site) | 🔵 Low | 5 | Medium | dev | #7, #16 |
| #37 | Organization markup should carry the verified legal identity and sameAs links (verify on-site) | 🔵 Low | 3 | Low | dev | #23 |
| #24 | The likely Google Business Profile and local citations still show the old Vincennes address, while the registered seat is now in Paris | 🟡 Medium | 4 | Medium | marketing | — |
| #45 | Some snippets show mini-cart text ('0 items - 0,00 €'), so meta descriptions need checking (verify on-site) | ⚪ Info | 2 | Low | content + dev | #11 |

## Phase 3: Content & authority — Month 2

*Goal:* Guides, comparison and B2B hubs, entity building (Wikidata), digital PR and link reclamation.

| # | Action | Severity | Impact | Effort | Owner | Do after |
|---|---|---|---|---|---|---|
| #8 | Few guide pages target informational carrying and back-pain queries, and Gravipack is absent from those results | 🟡 Medium | 6 | High | content + legal | #4, #1 |
| #14 | No comparison or alternatives content answers 'Gravipack vs …' and comparison intent | 🟡 Medium | 5 | Medium | content + legal | #1, #4 |
| #12 | B2B and occupational (TMS/QVT) demand has no indexable hub; the offers sit inside product pages and service 'products' | 🟡 Medium | 5 | Medium | content + dev | #4, #22 |
| #15 | There is no single, consistent explainer for 'sac à dos exosquelette', and the brand describes its product several different ways | 🟡 Medium | 5 | Medium | marketing | #4, #16 |
| #10 | Gravipack is missing from the third-party comparison and 'meilleur …' articles that rank for generic ergonomic, hiking and school-bag queries | 🟡 Medium | 6 | High | marketing / PR | #14 |
| #22 | RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links | 🟡 Medium | 5 | Low | marketing / PR | — |
| #19 | Independent press coverage is thin at the top end, and none dated 2025 or 2026 was found | 🟡 Medium | 5 | Medium | marketing / PR | #22 |
| #18 | Press and partner mentions of Gravipack have unknown link status and should be checked and reclaimed as links | 🟡 Medium | 5 | Low | marketing / PR | #33 |
| #25 | No Wikidata or Wikipedia entity exists for Gravipack; searches return only lookalike brands | 🟡 Medium | 4 | Low | marketing | #23, #32 |
| #26 | Marketplace ratings are weak and split across legacy model names (Decathlon brand page 3.88/5, Feather noir 1.5/5, Fnac Road Adventure about 3/5) | 🟡 Medium | 4 | Medium | management + e-commerce | #2, #17 |
| #40 | No public size/fit table maps height and weight to strap settings, although bags are adjusted to each buyer | 🔵 Low | 3 | Low | content + legal | — |
| #35 | The inventor-founder's expertise is spread across several posts rather than one authoritative bio | 🔵 Low | 3 | Low | content + legal | #38 |
| #38 | Patent and trademark claims are not backed by publication or registration numbers | 🔵 Low | 3 | Low | content + legal | — |
| #32 | Awards are real but under-sourced, and the army and special-forces claims rest on founder statements and undated owned posts | 🔵 Low | 3 | Low | management + customer service | #23 |
| #43 | No 'Où acheter' page lists authorised sellers, and some channels (Amazon.fr, Cdiscount, ManoMano, pharmacies) were not found | 🔵 Low | 3 | Low | management + e-commerce | #17 |
| #39 | A reseller's Gravipack brand page and Decathlon lead several generic 'anti mal de dos' results | 🔵 Low | 3 | Low | management + e-commerce | #21 |

## Phase 4: Monitoring & iteration — Ongoing

*Goal:* Track KPIs monthly, drift-monitor key pages, keep content and reviews fresh.

| # | Action | Severity | Impact | Effort | Owner | Do after |
|---|---|---|---|---|---|---|
| #42 | The YouTube channel is named 'zero gravity backpack' and uses medical wording; the social and community footprint is small or stale | 🔵 Low | 3 | Medium | marketing | #15, #4 |
| #31 | AI and search crawler access, server rendering, Bing coverage and llms.txt need an on-site check | 🔵 Low | 3 | Low | marketing | #29 |
| #34 | FAQ and category intros may not be written as self-contained answers (verify on-site) | 🔵 Low | 3 | Low | marketing | #4, #15, #31 |
| #33 | The backlink profile cannot be measured with the current tooling; no toxic patterns were seen in the sample | 🔵 Low | 3 | Low | marketing / PR | — |

## KPIs to track

| KPI | Baseline (evidence) | Target | Tool |
|---|---|---|---|
| Indexed gravipack.fr pages / redirects | 0 indexed; redirect status unknown | .fr 301 → gravipack.com page-to-page | curl -I, GSC |
| Hosts with indexed store URLs | 3+ (apex ≈40, www ≈58, presta ≈16 sampled) | 1 canonical host | GSC Page indexing, site: queries |
| Home page position for "gravipack" | #6-#9 in sampled results | #1 with sitelinks | GSC Performance (query = gravipack), rank tracker FR mobile |
| gravipack.com position for model queries (Sherpa, Hiking 33, Feather, Oslo) | first owned URL #6-#9 or absent for 4/5 models | Top 3 for all models | Rank tracker FR |
| Titles > 60 characters | 76/98 sampled (max 204) | < 10 % | /seo technical crawl, Screaming Frog |
| Trustpilot score / review count / reply rate | 3.1/5 · 9 reviews · 0 % replies to negatives | ≥ 4.2 · 100+ reviews · 100 % replies within 48 h | Trustpilot Business |
| Independent editorial mentions per quarter | 0 since Feb 2024 | ≥ 3 per quarter (incl. 1 health/prevention outlet) | Google Alerts, mention monitoring |
| Non-brand organic clicks to guides & category hubs | near zero (no informational coverage) | + month-over-month growth after launch | GSC Performance (exclude brand) |
| SEO Health Score (claude-seo) | 33/100 provisional (75 % of weight) | ≥ 70 after Phases 1-3 | /seo audit re-run |
