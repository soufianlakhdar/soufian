# Gravipack — Full SEO Audit (claude-seo)

**Audit target:** `http://gravipack.fr/` (as requested) → brand store indexed at `gravipack.com`  
**Date:** 2026-10-12  
**Toolkit:** [claude-seo v2.4.2](https://github.com/AgriciDaniel/claude-seo) — `/seo audit` orchestration with `seo-technical`, `seo-sitemap`, `seo-hreflang`, `seo-page`, `seo-cluster`, `seo-sxo`, `seo-plan`, `seo-content-brief`, `seo-competitor-pages`, `seo-backlinks`, `seo-content` (E-E-A-T), `seo-geo`, `seo-agentic`, `seo-ecommerce`, `seo-local`, `seo-maps` methodologies  
**Business type detected:** E-commerce (D2C WooCommerce store + marketplaces + B2B quotes)

> ⚠️ **Scope limitation, read first.** The audit sandbox's network policy blocked `gravipack.fr`, `www.gravipack.fr`, `gravipack.com` and `www.gravipack.com`, so **no page of the site could be crawled or rendered**. Following claude-seo's rule *“URL unreachable → report clearly, do not guess site content”*, this report covers everything that can be proven from **search-engine evidence** (≈360 web searches: indexed URLs, titles as shown in results, third-party sites, public registries). Checks that need the live HTML (robots.txt, sitemaps, canonicals, redirects, schema, Core Web Vitals, images, accessibility) are listed in [`ONSITE-AUDIT-PENDING.md`](ONSITE-AUDIT-PENDING.md) with the exact claude-seo commands to run once the domains are allowed. Positions quoted are from the search results we sampled (a US-located, non-Google index), not Google.fr rankings.

## 1. Executive summary

Gravipack has a genuinely distinctive product (a patented-claimed "exosquelette" strap system), real recognition (Concours Lépine silver 2018, INPI Trophées 2022 finalist, RATP deployment) and broad retail distribution. Search engines, however, see a fragmented, over-optimised and weakly trusted brand. The provisional **SEO Health Score is 33/100** (75 % of claude-seo's weight measurable without crawling the site) and the **off-site visibility score is 35/100**.

**1. The audited domain is not the live site.** `gravipack.fr` has zero indexed pages; the store lives on `gravipack.com`, but search engines index it on two hosts (apex and `www`), plus a legacy PrestaShop store (`presta.gravipack.com`) and other brand storefronts. Duplicate product URLs, cart/sort/filter parameters and thin archives dilute crawl budget and ranking signals. Consolidating to one canonical host with 301 redirects is the first, cheapest win.

**2. Titles and categories fight each other.** About 76 % of sampled titles exceed 60 characters and over half repeat "anti mal de dos", so the home page, categories and ~30 products cannibalise one keyword while the market's real head terms ("sac à dos ergonomique", "cartable ergonomique", "sac à dos ordinateur ergonomique") go unclaimed.

**3. Health claims are the biggest trust and ranking risk.** "-92 %", "anti-douleur", "dispositif médical" and "remboursé par la Sécurité sociale" have no public primary evidence (no published study, no CE/EUDAMED or LPP record found; the reimbursement source actually describes employer funding). For a YMYL-adjacent product, Google's quality systems and Merchant Center reward substantiated, carefully worded claims.

**4. Gravipack doesn't own its own name.** For "gravipack" the home page ranked only #6-#9 in the results we sampled; "gravipack avis/arnaque" is led by Trustpilot (3.1/5, 9 reviews, negatives unanswered), a critical Outzer test and sceptical forums; marketplaces outrank the store for 4 of 5 model names, with no price parity.

**5. Little content for discovery.** There are almost no guides, comparison pages, size guides or a B2B/TMS-prevention hub, no Wikidata entity, and no independent press since February 2024, so AI answer engines and "meilleur…" comparatifs don't cite Gravipack.

Fix order: consolidate hosts and clean the index (week 1), rewrite claims, titles and categories and answer every review (weeks 2-3), then build evidence, guides, comparison and B2B content plus digital PR (month 2). The on-site half of the audit (schema, Core Web Vitals, images, robots/sitemaps) is ready to run as soon as the domains are allowed in the audit environment.

### Scores

| Score | Value | Notes |
|---|---|---|
| **SEO Health Score (provisional)** | **33/100** | PROVISIONAL weighted mean of the pillars measurable from search evidence (Technical 22 [partial], Content 23 [partial], On-Page 20, AI Search Readiness 10), renormalised; Schema, Performance and Images need the on-site crawl (assessed weight: 75%) |
| **Off-site & search-visibility score** | **35/100** | Simple mean of AI Search Readiness, Off-Page & Authority, Brand & Reputation, E-commerce & Marketplaces and Local SEO scores |
| Findings | 45 | 🟠 High: 3, 🟡 Medium: 26, 🔵 Low: 15, ⚪ Info: 1 |

### Category scorecard

| Pillar | In claude-seo Health Score | Weight | Score | Status | Rationale |
|---|---|---|---|---|---|
| Technical SEO | yes | 22% | **35/100** *(partial)* | partially-assessed | Index hygiene and host consolidation scored 30/100 by the indexation specialist: 4 owned hosts, apex+www both indexed, legacy presta store, duplicate product URLs, cart/sort/filter parameters and thin archives in the index (canonical-host-fr, duplicate-product-urls, legacy-presta-subdomain, parameter-urls-indexed). HTTPS-only URLs seen (+). robots.txt, sitemaps, redirects and CWV not observable. |
| On-Page SEO | yes | 20% | **35/100** | assessed | 76/98 sampled titles exceed 60 chars (up to 204), 53/98 stack "anti mal de dos", model names often missing, heavy cannibalisation, categories target brand vocabulary instead of market head terms, very long slugs (title-tags, keyword-cannibalisation, category-head-terms, url-slugs). Scored from titles as shown in search results. |
| Content Quality | yes | 23% | **30/100** *(partial)* | partially-assessed | Strong first-hand inventor story and real awards, but YMYL health claims (-92 %, "anti-douleur", "remboursé par la Sécurité sociale", "dispositif médical") have no public primary evidence (study-92-evidence, health-claims-wording); informational guide coverage near zero (informational-guides-gap); no comparison, size-guide or authoritative founder bio pages. |
| AI Search Readiness | yes | 10% | **33/100** *(partial)* | partially-assessed | Gravipack appears for niche "exosquelette / anti mal de dos" prompts (proxy 65) but is absent from broad informational and "meilleur…" prompts (proxy 12); no Wikidata/Wikipedia entity, inconsistent descriptors and entity facts (knowledge-graph-entity, exosquelette-definition-descriptor, entity-facts-consistency). Crawler access/llms.txt not observable. |
| Schema / Structured Data | yes | 10% | n/a — not assessed | not-assessed | Requires the live HTML. Recommendations prepared (organization-schema, product-schema-merchant-center). |
| Performance (CWV) | yes | 10% | n/a — not assessed | not-assessed | Requires PageSpeed/CrUX or a local Lighthouse run against the live site. |
| Images | yes | 5% | n/a — not assessed | not-assessed | Requires the live HTML (alt text, formats, sizes, lazy-loading). |
| Off-Page & Authority | supplementary | — | **45/100** *(partial)* | partially-assessed | ~25 mentioning domains incl. 5 high-authority French editorial (Journal du Geek, Maddyness, Europe 1, France Bleu, franceinfo), but no national daily/health media, no coverage since Feb 2024, absent from comparatifs; link status unmeasured (press-coverage-freshness, listicle-comparatif-gap, mention-link-reclamation, backlink-measurement). |
| Brand & Reputation | supplementary | — | **30/100** | assessed | Home page only #6-#9 for "gravipack" in sampled results; "avis/arnaque" SERPs led by Trustpilot 3.1/5 (9 reviews, negatives unanswered incl. 2026), critical Outzer test and sceptical forums; on-site social-proof figures not corroborated (review-serps-unanswered, brand-serp, onsite-social-proof-claims). |
| E-commerce & Marketplaces | supplementary | — | **30/100** | assessed | Marketplaces/resellers outrank gravipack.com for 4 of 5 model queries; no price parity (up to ~2.8x spread incl. struck reference prices); inconsistent specs and legacy model names across channels; marketplace ratings weak (model-serps-ceded, price-parity-reference-prices, product-data-consistency, marketplace-reviews). |
| Local SEO | supplementary | — | **35/100** *(partial)* | partially-assessed | Likely GBP and PagesJaunes/Mappy citations still show the old Vincennes "Maroquinerie" listing while the legal seat moved to Paris 2e; no store locator (gbp-local-citations, where-to-buy-channels). |

### Top 5 critical issues

1. 🟠 [#1 The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank](#1-the--92--claim-rests-on-a-2019-lyon-study-with-no-public-primary-document-and-no-citable-evidence-page-on-the-main-site-while-forum-doubts-about-it-rank) — impact 8/10, effort High
1. 🟠 [#3 Review and 'arnaque' searches surface critical content the brand has not answered (Trustpilot 3.1/5 with unanswered 2026 complaints, the Outzer review, sceptical forum threads)](#3-review-and-arnaque-searches-surface-critical-content-the-brand-has-not-answered-trustpilot-315-with-unanswered-2026-complaints-the-outzer-review-sceptical-forum-threads) — impact 7/10, effort Medium
1. 🟠 [#2 Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model names (Sherpa, Hiking 33, Feather, Business Talk)](#2-marketplaces-resellers-and-old-crowdfunding-pages-outrank-gravipackcom-for-its-own-model-names-sherpa-hiking-33-feather-business-talk) — impact 7/10, effort Medium
1. 🟡 [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation) — impact 7/10, effort Medium
1. 🟡 [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom) — impact 6/10, effort Low

### Top quick wins

- [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom) — Low effort, impact 6/10
- [#22 RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links](#22-ratps-own-pages-document-its-use-of-gravipack-but-this-has-not-been-turned-into-a-case-study-or-links) — Low effort, impact 5/10
- [#18 Press and partner mentions of Gravipack have unknown link status and should be checked and reclaimed as links](#18-press-and-partner-mentions-of-gravipack-have-unknown-link-status-and-should-be-checked-and-reclaimed-as-links) — Low effort, impact 5/10
- [#29 Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=)](#29-cart-sort-and-filter-parameter-urls-appear-in-the-index-add-to-cart-order-filter_product_cat) — Low effort, impact 4/10
- [#25 No Wikidata or Wikipedia entity exists for Gravipack; searches return only lookalike brands](#25-no-wikidata-or-wikipedia-entity-exists-for-gravipack-searches-return-only-lookalike-brands) — Low effort, impact 4/10
- [#27 On-site social-proof figures ('4,7 sur Google' from 1,121-1,175 reviews, '500 000 clients satisfaits') are not independently verified](#27-on-site-social-proof-figures-47-sur-google-from-1121-1175-reviews-500-000-clients-satisfaits-are-not-independently-verified) — Low effort, impact 4/10

## 2. Domain & entity snapshot (what search evidence shows)

| Item | Finding |
|---|---|
| `gravipack.fr` / `www.gravipack.fr` | **0 indexed pages** in every query tried; no third-party page links to or names the .fr domain. |
| `gravipack.com` vs `www.gravipack.com` | Both hosts indexed (≈40 apex + ≈58 www URLs sampled) — no single canonical host. |
| `presta.gravipack.com` | Legacy PrestaShop store still indexed (≈16 URLs) with old models/prices. |
| Other brand hosts seen | `gravipack.ma`, `gravipacker.com`, possible staging copy `gravipack.archemia.fr` (verify). |
| CMS | WordPress + WooCommerce (URL patterns `/produit/`, `/categorie-produit/`, `?add-to-cart=`). |
| Legal entity | EXOSQUELETTE LIGHT SAS, SIREN 840 543 383 (formerly GRAVIBAG → GRAVIPACK, renamed 2025); seat Paris 2e since May 2026; president Mohammed Errafi. Kid'abord is a separate company acting as licensee and marketplace seller. |
| Recognition | Concours Lépine silver medal 2018 (press), INPI Trophées 2022 finalist (inpi.fr), Europe 1 Trophées de l'Avenir 2023 candidate, RATP equipped ~50 maintenance workers (VivaTech 2023). |
| Reputation snapshot | Trustpilot 3.1/5 from 9 reviews, negative reviews unanswered (incl. 2026); Decathlon brand page ≈3.9/5 (16); critical Outzer test and sceptical forum threads rank for brand queries. |

## 3. Findings by pillar

Each finding has: severity (claude-seo priority: Critical = blocks indexing/penalty · High = significant ranking impact, fix within 1 week · Medium = optimisation opportunity, within 1 month · Low = backlog), impact score (1-10), effort, confidence, the evidence, why it matters, how it affects SEO, a step-by-step fix, and claude-seo's synthesis checks (dependencies, falsifiability, leading indicator).

| # | Finding | Pillar | Severity | Impact | Effort |
|---|---|---|---|---|---|
| 1 | [The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank](#1-the--92--claim-rests-on-a-2019-lyon-study-with-no-public-primary-document-and-no-citable-evidence-page-on-the-main-site-while-forum-doubts-about-it-rank) | Content Quality | 🟠 High | 8 | High |
| 2 | [Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model names (Sherpa, Hiking 33, Feather, Business Talk)](#2-marketplaces-resellers-and-old-crowdfunding-pages-outrank-gravipackcom-for-its-own-model-names-sherpa-hiking-33-feather-business-talk) | E-commerce & Marketplaces | 🟠 High | 7 | Medium |
| 3 | [Review and 'arnaque' searches surface critical content the brand has not answered (Trustpilot 3.1/5 with unanswered 2026 complaints, the Outzer review, sceptical forum threads)](#3-review-and-arnaque-searches-surface-critical-content-the-brand-has-not-answered-trustpilot-315-with-unanswered-2026-complaints-the-outzer-review-sceptical-forum-threads) | Brand & Reputation | 🟠 High | 7 | Medium |
| 4 | [Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation) | Content Quality | 🟡 Medium | 7 | Medium |
| 5 | [gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom) | Technical SEO | 🟡 Medium | 6 | Low |
| 6 | [Segment categories rank mainly for 'anti mal de dos' wordings and miss the market's generic head terms (sac à dos ergonomique, cartable ergonomique, sac randonnée léger…)](#6-segment-categories-rank-mainly-for-anti-mal-de-dos-wordings-and-miss-the-markets-generic-head-terms-sac-à-dos-ergonomique-cartable-ergonomique-sac-randonnée-léger) | On-Page SEO | 🟡 Medium | 6 | Medium |
| 7 | [The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles) | Technical SEO | 🟡 Medium | 6 | Medium |
| 8 | [Few guide pages target informational carrying and back-pain queries, and Gravipack is absent from those results](#8-few-guide-pages-target-informational-carrying-and-back-pain-queries-and-gravipack-is-absent-from-those-results) | Content Quality | 🟡 Medium | 6 | High |
| 9 | [Dozens of pages target the same 'anti mal de dos' and 'exosquelette' terms, so the home page, category hub and product pages compete](#9-dozens-of-pages-target-the-same-anti-mal-de-dos-and-exosquelette-terms-so-the-home-page-category-hub-and-product-pages-compete) | On-Page SEO | 🟡 Medium | 6 | Medium |
| 10 | [Gravipack is missing from the third-party comparison and 'meilleur …' articles that rank for generic ergonomic, hiking and school-bag queries](#10-gravipack-is-missing-from-the-third-party-comparison-and-meilleur--articles-that-rank-for-generic-ergonomic-hiking-and-school-bag-queries) | Off-Page & Authority | 🟡 Medium | 6 | High |
| 11 | [Title tags are over-long, carry a bloated site-wide suffix and stacked claim keywords, and sometimes omit the model name or contain typos](#11-title-tags-are-over-long-carry-a-bloated-site-wide-suffix-and-stacked-claim-keywords-and-sometimes-omit-the-model-name-or-contain-typos) | On-Page SEO | 🟡 Medium | 6 | Medium |
| 12 | [B2B and occupational (TMS/QVT) demand has no indexable hub; the offers sit inside product pages and service 'products'](#12-b2b-and-occupational-tmsqvt-demand-has-no-indexable-hub-the-offers-sit-inside-product-pages-and-service-products) | On-Page SEO | 🟡 Medium | 5 | Medium |
| 13 | [For 'gravipack', an obsolete 2020 crowdfunding page comes first and the home page ranked only #6-#9 in the results we sampled](#13-for-gravipack-an-obsolete-2020-crowdfunding-page-comes-first-and-the-home-page-ranked-only-6-9-in-the-results-we-sampled) | Brand & Reputation | 🟡 Medium | 5 | Medium |
| 14 | [No comparison or alternatives content answers 'Gravipack vs …' and comparison intent](#14-no-comparison-or-alternatives-content-answers-gravipack-vs--and-comparison-intent) | Content Quality | 🟡 Medium | 5 | Medium |
| 15 | [There is no single, consistent explainer for 'sac à dos exosquelette', and the brand describes its product several different ways](#15-there-is-no-single-consistent-explainer-for-sac-à-dos-exosquelette-and-the-brand-describes-its-product-several-different-ways) | AI Search Readiness | 🟡 Medium | 5 | Medium |
| 16 | [The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages](#16-the-legacy-prestashop-store-prestagravipackcom-still-appears-in-search-results-with-old-product-study-and-award-pages) | Technical SEO | 🟡 Medium | 5 | Medium |
| 17 | [Who sells, makes and services Gravipack products is not explained, and partner listings are partly outside the brand's control](#17-who-sells-makes-and-services-gravipack-products-is-not-explained-and-partner-listings-are-partly-outside-the-brands-control) | E-commerce & Marketplaces | 🟡 Medium | 5 | Medium |
| 18 | [Press and partner mentions of Gravipack have unknown link status and should be checked and reclaimed as links](#18-press-and-partner-mentions-of-gravipack-have-unknown-link-status-and-should-be-checked-and-reclaimed-as-links) | Off-Page & Authority | 🟡 Medium | 5 | Low |
| 19 | [Independent press coverage is thin at the top end, and none dated 2025 or 2026 was found](#19-independent-press-coverage-is-thin-at-the-top-end-and-none-dated-2025-or-2026-was-found) | Off-Page & Authority | 🟡 Medium | 5 | Medium |
| 20 | [Prices differ across channels and on gravipack.com itself, with struck 'reference' prices almost everywhere](#20-prices-differ-across-channels-and-on-gravipackcom-itself-with-struck-reference-prices-almost-everywhere) | E-commerce & Marketplaces | 🟡 Medium | 5 | Medium |
| 21 | [Model names, capacities, weights and warranty terms conflict across channels, and some specs are publicly disputed](#21-model-names-capacities-weights-and-warranty-terms-conflict-across-channels-and-some-specs-are-publicly-disputed) | E-commerce & Marketplaces | 🟡 Medium | 5 | Medium |
| 22 | [RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links](#22-ratps-own-pages-document-its-use-of-gravipack-but-this-has-not-been-turned-into-a-case-study-or-links) | Off-Page & Authority | 🟡 Medium | 5 | Low |
| 23 | [Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards) | Brand & Reputation | 🟡 Medium | 4 | Low |
| 24 | [The likely Google Business Profile and local citations still show the old Vincennes address, while the registered seat is now in Paris](#24-the-likely-google-business-profile-and-local-citations-still-show-the-old-vincennes-address-while-the-registered-seat-is-now-in-paris) | Local SEO | 🟡 Medium | 4 | Medium |
| 25 | [No Wikidata or Wikipedia entity exists for Gravipack; searches return only lookalike brands](#25-no-wikidata-or-wikipedia-entity-exists-for-gravipack-searches-return-only-lookalike-brands) | AI Search Readiness | 🟡 Medium | 4 | Low |
| 26 | [Marketplace ratings are weak and split across legacy model names (Decathlon brand page 3.88/5, Feather noir 1.5/5, Fnac Road Adventure about 3/5)](#26-marketplace-ratings-are-weak-and-split-across-legacy-model-names-decathlon-brand-page-3885-feather-noir-155-fnac-road-adventure-about-35) | E-commerce & Marketplaces | 🟡 Medium | 4 | Medium |
| 27 | [On-site social-proof figures ('4,7 sur Google' from 1,121-1,175 reviews, '500 000 clients satisfaits') are not independently verified](#27-on-site-social-proof-figures-47-sur-google-from-1121-1175-reviews-500-000-clients-satisfaits-are-not-independently-verified) | Brand & Reputation | 🟡 Medium | 4 | Low |
| 28 | [Other brand storefronts and hosts (gravipack.ma, gravipacker.com, a probable agency staging host) show different catalogues, model names and prices](#28-other-brand-storefronts-and-hosts-gravipackma-gravipackercom-a-probable-agency-staging-host-show-different-catalogues-model-names-and-prices) | Technical SEO | 🟡 Medium | 4 | Medium |
| 29 | [Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=)](#29-cart-sort-and-filter-parameter-urls-appear-in-the-index-add-to-cart-order-filter_product_cat) | Technical SEO | 🟡 Medium | 4 | Low |
| 30 | [Product, Offer and review markup and the Merchant Center setup cannot be verified, and the Content API for Shopping has been sunset (verify on-site)](#30-product-offer-and-review-markup-and-the-merchant-center-setup-cannot-be-verified-and-the-content-api-for-shopping-has-been-sunset-verify-on-site) | Schema / Structured Data | 🔵 Low | 5 | Medium |
| 31 | [AI and search crawler access, server rendering, Bing coverage and llms.txt need an on-site check](#31-ai-and-search-crawler-access-server-rendering-bing-coverage-and-llmstxt-need-an-on-site-check) | AI Search Readiness | 🔵 Low | 3 | Low |
| 32 | [Awards are real but under-sourced, and the army and special-forces claims rest on founder statements and undated owned posts](#32-awards-are-real-but-under-sourced-and-the-army-and-special-forces-claims-rest-on-founder-statements-and-undated-owned-posts) | Brand & Reputation | 🔵 Low | 3 | Low |
| 33 | [The backlink profile cannot be measured with the current tooling; no toxic patterns were seen in the sample](#33-the-backlink-profile-cannot-be-measured-with-the-current-tooling-no-toxic-patterns-were-seen-in-the-sample) | Off-Page & Authority | 🔵 Low | 3 | Low |
| 34 | [FAQ and category intros may not be written as self-contained answers (verify on-site)](#34-faq-and-category-intros-may-not-be-written-as-self-contained-answers-verify-on-site) | AI Search Readiness | 🔵 Low | 3 | Low |
| 35 | [The inventor-founder's expertise is spread across several posts rather than one authoritative bio](#35-the-inventor-founders-expertise-is-spread-across-several-posts-rather-than-one-authoritative-bio) | Content Quality | 🔵 Low | 3 | Low |
| 36 | [Low-value archives and duplicate CMS pages are indexed (attribute/tag archives, a /category/ base, a /test/ copy, duplicate contact pages)](#36-low-value-archives-and-duplicate-cms-pages-are-indexed-attributetag-archives-a-category-base-a-test-copy-duplicate-contact-pages) | Technical SEO | 🔵 Low | 3 | Low |
| 37 | [Organization markup should carry the verified legal identity and sameAs links (verify on-site)](#37-organization-markup-should-carry-the-verified-legal-identity-and-sameas-links-verify-on-site) | Schema / Structured Data | 🔵 Low | 3 | Low |
| 38 | [Patent and trademark claims are not backed by publication or registration numbers](#38-patent-and-trademark-claims-are-not-backed-by-publication-or-registration-numbers) | Content Quality | 🔵 Low | 3 | Low |
| 39 | [A reseller's Gravipack brand page and Decathlon lead several generic 'anti mal de dos' results](#39-a-resellers-gravipack-brand-page-and-decathlon-lead-several-generic-anti-mal-de-dos-results) | E-commerce & Marketplaces | 🔵 Low | 3 | Low |
| 40 | [No public size/fit table maps height and weight to strap settings, although bags are adjusted to each buyer](#40-no-public-sizefit-table-maps-height-and-weight-to-strap-settings-although-bags-are-adjusted-to-each-buyer) | Content Quality | 🔵 Low | 3 | Low |
| 41 | [Pre-order dates that have already passed may still be live on product pages, and news posts show no dates in search snippets (verify on-site)](#41-pre-order-dates-that-have-already-passed-may-still-be-live-on-product-pages-and-news-posts-show-no-dates-in-search-snippets-verify-on-site) | Content Quality | 🔵 Low | 3 | Low |
| 42 | [The YouTube channel is named 'zero gravity backpack' and uses medical wording; the social and community footprint is small or stale](#42-the-youtube-channel-is-named-zero-gravity-backpack-and-uses-medical-wording-the-social-and-community-footprint-is-small-or-stale) | AI Search Readiness | 🔵 Low | 3 | Medium |
| 43 | [No 'Où acheter' page lists authorised sellers, and some channels (Amazon.fr, Cdiscount, ManoMano, pharmacies) were not found](#43-no-où-acheter-page-lists-authorised-sellers-and-some-channels-amazonfr-cdiscount-manomano-pharmacies-were-not-found) | E-commerce & Marketplaces | 🔵 Low | 3 | Low |
| 44 | [Product slugs are very long and keyword-stuffed, and some contain typos or '-copie' leftovers](#44-product-slugs-are-very-long-and-keyword-stuffed-and-some-contain-typos-or--copie-leftovers) | On-Page SEO | 🔵 Low | 2 | Low |
| 45 | [Some snippets show mini-cart text ('0 items - 0,00 €'), so meta descriptions need checking (verify on-site)](#45-some-snippets-show-mini-cart-text-0-items---000--so-meta-descriptions-need-checking-verify-on-site) | On-Page SEO | ⚪ Info | 2 | Low |

## Technical SEO

**Score:** **35/100** *(partial)* — Index hygiene and host consolidation scored 30/100 by the indexation specialist: 4 owned hosts, apex+www both indexed, legacy presta store, duplicate product URLs, cart/sort/filter parameters and thin archives in the index (canonical-host-fr, duplicate-product-urls, legacy-presta-subdomain, parameter-urls-indexed). HTTPS-only URLs seen (+). robots.txt, sitemaps, redirects and CWV not observable.

**What works:**
- Only HTTPS URLs surfaced in search results
- No toxic or spam link patterns in the sampled mentions
- Clear WooCommerce URL taxonomy (/produit/, /categorie-produit/) that can be cleaned up with standard plugins

### 5. gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | Low | needs-on-site-check | Technical SEO |

**Issue.** Context first: gravipack.fr, the domain submitted for this audit, is not where the brand's indexed store lives. We sampled search results from a US-located, non-Google index (about 60 phase-1 queries plus phase-2 checks). In them, site:gravipack.fr, "gravipack.fr", "www.gravipack.fr" and "gravipack.fr" sac à dos returned no URL on gravipack.fr or www.gravipack.fr. Every official result was on gravipack.com.

Every third-party page that names a domain also names gravipack.com: the Trustpilot profile (/review/gravipack.com), the LinkedIn company page, Les Pépites Tech and Motherbase. The legal notice at gravipack.com/mentions-legales/ (publisher EXOSQUELETTE LIGHT, host Gandi) describes gravipack.com, and no link or mention profile was found for gravipack.fr.

We could not fetch the live sites from the audit sandbox, and a PageSpeed request for gravipack.fr failed with a quota error (HTTP 429). So it is unknown whether .fr redirects, is parked or has lapsed. Zero indexed pages is exactly what a correct 301 from .fr to .com produces, so the .fr part is Low unless the on-site check shows .fr is parked, lapsed, not resolving or serving duplicate 200 pages. In those cases it becomes Medium, and higher if gravipack.fr is printed on packaging, in press kits or on old campaign material.

Second, the gravipack.com store appears on both hosts in the results we sampled. Of the 114 owned URLs observed, 58 were on www.gravipack.com, 40 on gravipack.com (apex) and 16 on the legacy presta.gravipack.com, which has its own finding. These counts describe the URLs we saw, not the size of the index.
- Apex: the home page, /boutique-gravipack/, /mentions-legales/, /conditions-generales-de-vente/, /contacts/, /nos-engagements/ and most product categories: /categorie-produit/tous-les-sacs-a-dos-exosquelette/ and its randonnée, scolaire, business, voyage, urbain, militaire, outillage and claie-de-portage children.
- www: /faq/, /contact-gravipack/, /articles/, /actualites-gravipack-2/, the /categorie/* blog archives, /a-propos-de-nous-gravipack-au-service-de-votre-dos/, /gravipackers/, the attribute and tag archives, and 28 of the 46 product URLs (18 were on apex).
- Pages from the same listing sit on different hosts. The shop root is on apex, while /boutique-gravipack/page/2/ and /boutique-gravipack/?order=price are on www. /categorie-produit/tous-les-sacs-a-dos-exosquelette/ is on apex and its /page/2/ on www.
- For the brand query 'gravipack', the owned results alternated between hosts: www /gravipackers/, apex /, a www product, then apex /nos-engagements/. For 'gravipack prix', apex /boutique-gravipack/ (#4) was followed by www /boutique-gravipack/?order=price (#5).

No product or category path was recorded on both hosts; only the home page was reported on both. This is mixed-host indexing, not proven duplication. It fits either of two explanations:
- Both hosts answer 200 without consistent canonicals.
- A redirect already exists and this non-Google index still holds stale entries. This is plausible, because WordPress's redirect_canonical() and Yoast/Rank Math normally enforce one host.

Some examples first reported as host duplicates (Light Promax, G-Pack) are really different slugs and are handled in the duplicate-product-URL finding.

**Evidence.** <http://gravipack.fr/> · <https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/> · <https://www.gravipack.com/boutique-gravipack/page/2/> · <https://www.gravipack.com/boutique-gravipack/?order=price> · <https://www.gravipack.com/faq/> · <https://www.gravipack.com/gravipackers/> · <https://gravipack.com/nos-engagements/> · <https://gravipack.com/mentions-legales/> · <https://fr.trustpilot.com/review/gravipack.com> · <https://fr.linkedin.com/company/gravipack> · <https://lespepitestech.com/startup-de-la-french-tech/gravipack> · *(+1 more in findings/)*

**Why it matters.** A brand should have one 'entity home': a single host that Google, Merchant Center and AI answer engines all treat as official.

If both hosts answer 200, Google treats them as separate URLs. It has to cluster them and may pick a canonical you did not choose. Search Console data is split if only a URL-prefix property is verified, and Merchant Center expects feed landing pages on the claimed website.

For gravipack.fr, the stakes are brand protection and type-in traffic, because French customers and journalists naturally guess '.fr'. A parked, lapsed or duplicate .fr wastes those visits and blurs the brand entity. A lapsed registration could also be taken by a third party.

**Effect on SEO.** If both .com hosts serve 200, internal links and external equity are split between them. Crawl is spent on duplicate fetches, updates are re-clustered more slowly, and results can show a non-preferred URL with an older title. A clean single-hop 301 consolidates everything on one host and gives knowledge-graph and AI systems one official URL.

For .fr, a correct path-preserving 301 already delivers the full benefit. No link profile was found for .fr, so the 'wasted link equity' effect is small, and the main gains are type-in traffic and brand consistency. If .fr instead serves duplicate 200 pages, it becomes a cross-domain duplicate that competes with .com.

**How to fix.**

0. **Measure before choosing. Do not pick a host from this report.** Find which host is canonical today and keep it unless there is a strong reason to switch:
   - WordPress: Réglages → Général → 'Adresse web de WordPress (URL)' and 'Adresse web du site (URL)', or `wp option get home` and `wp option get siteurl`.
   - View the source of the home page and one product page on both hosts. Note which host `rel=canonical` and `og:url` use.
   - Open the Yoast or Rank Math sitemap (`/sitemap_index.xml`) and note the host in the `<loc>` entries.
   - In Search Console, run URL Inspection on about 10 URLs from each host and compare 'Canonical déclarée par l'utilisateur' with 'Canonical sélectionnée par Google'.
   www may well be the current canonical, since most products, the FAQ and most posts were observed there. Forcing apex would then be a second migration. Trustpilot's 'review/gravipack.com' is not evidence for apex, because Trustpilot always strips 'www'.
1. **Run the redirect matrix** (see onsite_check). If every non-canonical variant already returns a single 301 to the same path on the canonical host, add no rules. The mixed index is stale, so go to step 5.
2. **If both .com hosts return 200, find the layer responsible before adding rules.** WordPress's redirect_canonical() normally redirects any host that does not match 'home'. If it does not, check:
   - a page cache serving copies per host (WP Rocket, LiteSpeed Cache, Varnish);
   - a CDN or proxy (e.g. Cloudflare) rewriting the Host header or carrying its own redirect rules;
   - the vhost configuration.
   Stacking an .htaccess rule on top of an existing CDN or plugin redirect is the usual cause of redirect loops and chains.
3. **Take a full backup (files and database) and work in a maintenance window** before touching 'home' or 'siteurl'. A mismatch between the database and the server rules can lock you out of wp-admin; you can recover by defining `WP_HOME` and `WP_SITEURL` in wp-config.php.
   Then add one server-level rule **above** `# BEGIN WordPress` that sends every variant to the canonical host in one hop. The example below assumes www is canonical. If apex wins, match `^www\.gravipack\.com$` instead and target https://gravipack.com/.
```apache
RewriteEngine On
# gravipack.fr, www.gravipack.fr and the non-canonical .com host -> one hop
RewriteCond %{HTTP_HOST} ^(www\.)?gravipack\.fr$ [NC,OR]
RewriteCond %{HTTP_HOST} ^gravipack\.com$ [NC]
RewriteRule ^(.*)$ https://www.gravipack.com/$1 [R=301,L]
# http -> https on the canonical host (behind a proxy/CDN test X-Forwarded-Proto instead of %{HTTPS})
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.gravipack.com/$1 [R=301,L]
```
   Nginx equivalent:
```nginx
server {
  listen 80; listen 443 ssl;
  server_name gravipack.fr www.gravipack.fr gravipack.com;  # certificate must cover all names
  return 301 https://www.gravipack.com$request_uri;
}
server { listen 80; server_name www.gravipack.com; return 301 https://www.gravipack.com$request_uri; }
```
4. **Clean internal references once the redirect works:**
   - Run Better Search Replace as a dry run, then live, replacing the non-canonical host with the canonical one in `wp_posts` and `wp_postmeta`. Skip the `guid` column, and never edit home or siteurl this way.
   - If the site uses Elementor, run Elementor → Outils → Remplacer l'URL.
   - Fix menu links, then purge the page cache and the CDN.
5. **Align every signal on the canonical host:**
   - Yoast or Rank Math outputs an absolute, self-referencing canonical.
   - The XML sitemap lists canonical-host URLs only.
   - robots.txt contains `Sitemap: https://<hôte-canonique>/sitemap_index.xml`.
   - The `url` in the Organization and WebSite JSON-LD uses the canonical host.
   - Merchant Center feed `link` values match the claimed website.
6. **Search Console and Bing:**
   - Create a **Domain property** for gravipack.com (DNS TXT record). It covers www, apex, presta, http and https.
   - Create a separate Domain property for gravipack.fr.
   - Resubmit the sitemap.
   - In Bing Webmaster Tools, import from Search Console or verify by DNS.
   - Allow 2-4 weeks for Google to re-cluster before judging the result.
7. **gravipack.fr:**
   - Confirm ownership at the registrar and switch on multi-year auto-renewal.
   - Make sure https://gravipack.fr and https://www.gravipack.fr carry a valid TLS certificate. A redirect behind a certificate error never reaches users.
   - Make both return a path-preserving 301 to the canonical .com host in **one hop**. The rule in step 3 covers this if .fr points to the same server. Registrar 'web forwarding' is acceptable only if it issues a 301, keeps the path and serves HTTPS.
   - Do **not** add hreflang between .fr and .com. Both are French for France, and hreflang is only for distinct language or region versions.
   - Use the Change of Address tool only if .fr ever hosted the site.
   - Do not move the store to .fr: all observed equity is on .com.
8. **Off-site:** use the exact canonical URL everywhere you control it:
   - LinkedIn, the YouTube 'À propos' tab, and the Instagram and Facebook bios;
   - the claimed Trustpilot business profile;
   - the GRAVIPACK seller profile on Decathlon;
   - a final news update on each of the 4 KissKissBankBank campaigns (KKBB support now redirects to Ulule, so post these updates yourself);
   - the press kit, email signatures and packaging.

- **First principle:** A site should answer on exactly one host. Every other host or domain should return a single 301 to the same path on that host, so that Google, Merchant Center and AI engines consolidate signals on one entity home. A domain that redirects correctly is supposed to have zero indexed pages, so that is not a defect in itself.
- **Do first:** —
- **How we'll know the fix failed:** Check 4 weeks after deployment. The fix has failed if any of these is true:
- any URL in the curl matrix returns 200, 302 or more than one hop on a non-canonical host or on gravipack.fr;
- URL Inspection still shows 'Canonical sélectionnée par Google' on the non-canonical host for most of the sampled URLs;
- Search Console Performance, filtered on the non-canonical host, still records clicks.

Conversely, if the matrix already shows correct single 301s before any change, the duplication hypothesis is false and the mixed index was stale. The remaining work is then only the Domain properties, the sitemap and internal-link alignment.
- **Leading indicator to monitor:** - Share of Search Console clicks and impressions on non-canonical-host URLs (Performance → Pages, 'URL contient' the non-canonical host). Target: close to 0 within 8 weeks.
- Number of non-canonical URLs listed as 'Page avec redirection' in the Page indexing report.
- A weekly redirect monitor on the 8 host variants, expecting status 301 and the right Location header.
- **To verify on-site:** For http and https on each of gravipack.fr, www.gravipack.fr, gravipack.com and www.gravipack.com, run `curl -sIL -o /dev/null -w '%{http_code} %{num_redirects} %{url_effective}\n' <url>/faq/?x=1` and expect a single 301 hop to the same path on the canonical host. Also check:
- the .fr TLS certificate;
- the WordPress home and siteurl values;
- the rel=canonical and og:url host on the home page and one product page, on both hosts;
- the host used in the sitemap <loc> entries and in the robots.txt Sitemap line;
- the Google-selected canonical for about 10 URLs in Search Console;
- whether gravipack.fr is printed on packaging, in the press kit or on old campaign material.

### 7. The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | Medium | needs-on-site-check | Technical SEO |

**Issue.** In the search results we sampled, several product families appear under more than one URL. Some of these URLs use a second product base, /produit-gravipack/, alongside WooCommerce's /produit/.
- **Sherpa Kaki ×3**, all with the same 90-character title ('Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur'): www /produit/sac-a-dos-sherpa-kaki-avec-exosquelette-…-legerete-en-haute-montagne/, apex /produit-gravipack/sac-a-dos-sherpa-kaki and apex /produit-gravipack/sac-a-dos-sherpa.
- **Hiking Terracotta ×2**, with the same title: www /produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-…/ and apex /produit-gravipack/sac-a-dos-revolutionnaire.
- **Light Promax ×3**, all surfacing for a single query:
  - apex /produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/ and www /produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/, both titled 'Sac à dos outillage anti-douleur exosquelette Gravipack®';
  - www /produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/ ('… Light Promax de Gravipack').
- **Cargo Max ×2**, with the identical title 'Claie de portage aluminium exosquelette Gravipack pour charges lourdes'.
- **Business Talk V4 ×3**, surfacing for one query: a 20 L page plus two 25 L pages (…-25l-…-pour-deux-ordinateurs-…-revolutionnaire/ and …-ordinateur-25l-…-ergonomie-eva-memoire-de-forme/). The 20 L page may be a distinct SKU; the two 25 L pages are the likely duplicate pair.
- **Kingston ×2**: /produit/sac-a-dos-teletravail-kingston-…/ and /produit/vive-la-rentree-scolaire-…-kingston-avec-exosquelette/. Both ranked together (#1 and #3) for 'sac à dos scolaire anti mal de dos' in the extended sample.
- **Solar battery ×2**, one slug ending in '-copie' (a leftover from WooCommerce's 'Dupliquer' action).
- **Pearl**: /produit/…pearl-29l-gris…/ and /produit-gravipack/sac-a-dos-exosquelette-gravipack-pearl/ carry **different** titles; the second says 'Pearl femme'. This may be a separate listing or an old version.

Corrections:
- The two G-Pack URLs (collège/lycée on apex, 'pour la journée … professionnels et vélo' on www) share the title 'Sac à dos exosquelette révolutionnaire et unique G-Pack Gravipack', but may be two real products. In that case the problem is a duplicate title, not a duplicate URL.
- The Compostelle 65 L '-copie' slug is a different capacity and belongs to the slug finding.
- One URL per colour (Sherpa bleu, Sherpa 45L orange and Sherpa kaki; Hiking 30L gris and Hiking terracotta; Oslo rouge; Pearl 29L gris) is a pattern Google supports with ProductGroup markup, so it is not a defect in itself.
- The short /produit-gravipack/ URLs may already be 301s or shortlinks that a stale, non-Google index still lists.
- Real ranking cannibalisation can only be confirmed in Search Console (query → pages).

The earlier High rating rested on an 'unverifiable' verdict, which does not meet the evidence rule, so this is Medium until the status check is done.

**Evidence.** <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa-kaki> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa> · <https://www.gravipack.com/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/> · <https://gravipack.com/produit-gravipack/sac-a-dos-revolutionnaire> · <https://www.gravipack.com/produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-avec-exosquelette-gravipack-pour-toutes-vos-aventures/> · <https://gravipack.com/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/> · <https://www.gravipack.com/produit/claie-de-portage-exosquelette-cargo-max-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/claie-de-portage-aluminium-exosquelette-anti-mal-de-dos-cargo-max-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/> · *(+10 more in findings/)*

**Why it matters.** Each live duplicate of a product splits its links, reviews, internal links and engagement. Google then chooses for itself which URL to show, and may pick the weaker copy or one with an old title.

Duplicate titles across products also make the catalogue look careless. They make it harder for the official product page to win model queries, where in the sampled results marketplaces already rank above it.

**Effect on SEO.** Model queries ('gravipack sherpa', 'light promax', 'business talk') are spread over sibling URLs, so no single page builds full strength. Search Console is likely to show 'Doublon : Google n'a pas choisi la même URL canonique que l'utilisateur' or 'Autre page avec balise canonique correcte' at scale (to verify). Review stars and merchant listings may attach to inconsistent URLs or prices.

Consolidating with 301s, or grouping real variants with ProductGroup markup, concentrates the signals on one URL per product.

**How to fix.**

1. **Audit status first.**
   - Crawl every URL in the groups with Screaming Frog in list mode, or run `curl -sI` on each. Record the status, final URL, rel=canonical and `<title>`.
   - Export the products (Produits → Exporter, CSV with ID, SKU, slug, status and GTIN) to separate distinct SKUs from copies.
   - Check each URL with Search Console URL Inspection.
   Only URLs answering 200 count as duplicates; a URL that already 301s is not one.
2. **Find what produces /produit-gravipack/.** Possible sources:
   - an old 'Base des produits' under Réglages → Permaliens;
   - a custom rewrite (`wp rewrite list | grep produit-gravipack`);
   - a shortlink or redirect plugin (Pretty Links, Redirection, Rank Math Redirections);
   - an .htaccess rule.
   If these URLs answer 200, add explicit 301s to the surviving /produit/ URLs one by one, because the slugs differ (e.g. /produit-gravipack/sac-a-dos-sherpa-kaki → /produit/sac-a-dos-sherpa-kaki-avec-…/). Then remove the source.
3. **True copies (same SKU):**
   - Keep the URL with the most links, sales and reviews (Search Console Links and Performance).
   - 301 the others to it with Redirection or Rank Math → Redirections (type 301).
   - Move the reviews by reassigning them to the survivor's product ID (WooCommerce reviews are comments).
   - Update menus and internal links.
   - Only then move the copy to the Corbeille and empty it.
   Likely candidates: Sherpa Kaki ×3, Hiking Terracotta ×2, Light Promax ×3, Cargo Max ×2, the two Business Talk V4 25 L pages and the '-copie' battery.
4. **Distinct SKUs that share a title** (G-Pack ×2, Business Talk V4 20 L vs 25 L, and the two Pearl pages if both are real): give each one a title and H1 that state the difference, and keep a self-referencing canonical. For example:
   - « Business Talk V4 20 L – sac à dos ordinateur à exosquelette | Gravipack »
   - « Business Talk V4 25 L – sac à dos 2 ordinateurs à exosquelette | Gravipack »
   - « G-Pack collège-lycée – sac à dos scolaire à exosquelette »
   - « G-Pack pro & vélo – sac à dos de journée à exosquelette »
   For Kingston, decide whether 'Vive la rentrée scolaire' is a real separate school offer; if not, 301 it to the Kingston product.
5. **Colour variants: choose ONE model and apply it to every family.**
   - **(A) Single page:** make it a WooCommerce variable product (Type de produit : Produit variable; attribute Couleur used for variations). Colour selection then uses `?attribute_pa_couleur=kaki` on the parent URL. 301 the old colour URLs to the parent.
   - **(B) Multi-page:** keep one self-canonical URL per colour and group the URLs with ProductGroup markup, using the same `item_group_id` in the Merchant Center feed. Do **not** canonicalise colour pages to the parent while also submitting them as landing pages; that sends conflicting signals. Example for (B); check that Rich Results Test reports valid merchant listings:
```json
{"@context":"https://schema.org","@type":"ProductGroup","name":"Gravipack Sherpa 45 L","productGroupID":"SHERPA45","variesBy":["https://schema.org/color"],"brand":{"@type":"Brand","name":"Gravipack"},
 "hasVariant":[
  {"@type":"Product","sku":"SHERPA45-KAKI","name":"Gravipack Sherpa 45 L kaki","color":"kaki","url":"https://<hôte>/produit/<slug-kaki>/","image":"https://<hôte>/…/sherpa-kaki.jpg","offers":{"@type":"Offer","price":"<prix>","priceCurrency":"EUR","availability":"https://schema.org/InStock"}},
  {"@type":"Product","sku":"SHERPA45-BLEU","name":"Gravipack Sherpa 45 L bleu","color":"bleu","url":"https://<hôte>/produit/<slug-bleu>/"}
 ]}
```
   With either option, the /produit-gravipack/ URLs and the true copies need 301s, not just canonicals.
6. **One migration map, one release.** Combine these 301s with the presta map and any slug changes (such as the Compostelle 65 L '-copie' slug, handled in the slug finding) so that no redirect chains form. Regenerate the Yoast or Rank Math sitemap so it lists only the surviving URLs, then re-crawl to confirm there are no duplicate product titles.

- **First principle:** Each product should have one indexable URL, or one URL per real variant with the variants explicitly grouped. When several live URLs carry the same product and title, Google chooses the canonical itself, and links, reviews and internal signals are split across the copies.
- **Do first:** [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom)
- **How we'll know the fix failed:** Check 4-6 weeks after the merge. The fix has failed if any of these is true:
- Search Console Page indexing still lists the merged URLs as indexed, or shows 'Doublon : Google n'a pas choisi la même URL canonique que l'utilisateur' for product URLs;
- Performance for a model query ('gravipack sherpa', 'light promax', 'cargo max') still spreads impressions over 2 or more URLs of the same SKU;
- a crawl still finds duplicate product titles.

If step 1 shows that the /produit-gravipack/ URLs and old slugs already return 301, the duplicate hypothesis is false for them. The finding then shrinks to title differentiation and variant markup, at Low.
- **Leading indicator to monitor:** - Number of distinct product URLs with impressions per model in Search Console. Target: 1 per model, or 1 per real variant.
- Duplicate-title count in the monthly crawl. Target: 0.
- Valid items in the Search Console merchant listings report.
- **To verify on-site:** - `curl -sI` on every URL in the groups, on both hosts;
- rel=canonical and `<title>` on each, in the page source;
- Search Console URL Inspection (Google-selected canonical);
- the WooCommerce product permalink base, and the source of /produit-gravipack/;
- the product CSV export (SKU and GTIN per URL), to tell copies from distinct SKUs;
- review counts on each duplicate.

### 16. The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | needs-on-site-check | Technical SEO |

**Issue.** The old PrestaShop store at presta.gravipack.com still appears in the search results we sampled (a US-located, non-Google index). We recorded 16 URLs on it:
- **Home page**, titled 'Gravipack, le sac a dos scolaire, business et randonnée, ce sac à dos allègent le poids…' (126 characters).
- **Categories:** /2-accueil, /22-produit, /24-sac-a-dos-sport, /72-sac-a-dos-scolaire and /73-gravipack ('Gravipack, le sac à dos en apesanteur qui ne fait pas mal au dos et aux épaules').
- **/40-etude-scientifique-soulage-le-dos-gravipack** ('L'étude scientifique du sac à dos en apesanteur Gravipack.'). This is the only indexed page about the 2019 LBMC / Faculté de Médecine Lyon-Sud study that we found.
- **Other pages:** /59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack, /plan-du-site-gravipack, and /content/1-livraison-sac-a-dos-gravipack ('… Gravipack le meilleur sac a dos au monde - livraison client').
- **Six product pages:**
  - Safar Vibe (/accueil/13-…)
  - Business Talk (/accueil/15-…)
  - Hiking33 (/accueil/16-sac-a-dos-gravipack-hikking33.html, 'Le seul sac à dos au monde qui allège le poids Hiking 33 Gravipack.')
  - Road Adventure (/accueil/17-…)
  - Sherpa 45 (/accueil/19-…, '… Le meilleur sac à dos de montagne.')
  - Feather (/accueil/21-…)

The legacy pages still compete for the brand's own model queries in the results we sampled:
- **'gravipack hiking 33':** presta was #8 in one run. In a re-run it was #9, and the main store was absent from the top 10.
- **'gravipack feather cartable':** presta was #10 and the only owned result.
- **'gravipack business talk':** presta was #9.
- **'gravipack prix':** the presta home page was #9.
- **site:gravipack.com searches** (categorie-produit, sac business ordinateur, CGV livraison, presse Lépine) also returned presta URLs. A gravipack.com-restricted 'Feather … prix' search returned 8 presta URLs out of 12.

The pages carry crowdfunding-era model names. Feather, Road Adventure and Safar Vibe exist only there among the owned sites, and 'Hiking 33' and 'Business Talk' differ from today's 'Hiking 30L / Terracotta' and 'Business Talk V4'. They also carry superlatives ('le seul sac à dos au monde', 'le meilleur sac à dos de montagne', 'en apesanteur') that the claims findings ask to retire.

On prices:
- One phase-2 snippet showed the Feather page at 149,00 € TTC 'en stock', although Feather was not found on the main store. That page may be presenting an offer that no longer exists.
- The other legacy prices, the 'commandes de réservation 2-3 mois' wording and the delivery terms came from search summaries that were not saved, so they are not asserted here.
- 249 € was still the regular Sherpa price in 2026. Decathlon's 149,90 € promotion ran 18/06-30/08/2026 and has ended, so the legacy Sherpa price is not stale.

Whether these URLs still return 200, already redirect or return 404 could not be checked, and indexes lag behind redirects. Hence Medium; raise to High if curl shows presta still serving 200 pages.

**Evidence.** <https://presta.gravipack.com/> · <https://presta.gravipack.com/73-gravipack> · <https://presta.gravipack.com/72-sac-a-dos-scolaire> · <https://presta.gravipack.com/24-sac-a-dos-sport> · <https://presta.gravipack.com/22-produit> · <https://presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack> · <https://presta.gravipack.com/59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack> · <https://presta.gravipack.com/plan-du-site-gravipack> · <https://presta.gravipack.com/content/1-livraison-sac-a-dos-gravipack> · <https://presta.gravipack.com/accueil/13-sac-a-dos-gravipack-safar-vibe.html> · <https://presta.gravipack.com/accueil/15-sac-a-dos-gravipack-business-talk.html> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · *(+5 more in findings/)*

**Why it matters.** A second storefront for the same brand competes with the live store for brand and model queries, and for some of them it is the first owned result. Buyers researching a model therefore meet stale content: retired model names, superlatives the brand is moving away from, and possibly lapsed offers.

The old store also holds two assets the main site needs: the study summary and the Concours Lépine page. AI answer engines can quote the legacy pages as current facts.

**Effect on SEO.** Links and relevance earned during the crowdfunding years (2019-2021 press, KissKissBankBank) stay on the legacy host and do not reach gravipack.com. Model queries ('gravipack hiking 33', 'gravipack feather') show a legacy page instead of the live product. Crawl budget is spent on a retired store. Prices or availability that differ across the brand's own URLs add risk for merchant listings.

Clean one-to-one 301s pass these signals to the live equivalents and remove the stale results.

**How to fix.**

1. **Check the live state.** Run `curl -sI` on the 16 URLs and the presta root (see onsite_check). Find out whether PrestaShop still takes orders. If it does, set a shutdown date and export orders and customers according to your retention obligations.
2. **Prioritise by equity.** In the gravipack.com Search Console Domain property (see the host finding), filter Links and Performance on 'presta.' to see which legacy URLs have links or impressions. Use Bing Webmaster Tools as a second source.
3. **Move the unique content first. Do not return 410 for it.**
   - Publish the study summary on gravipack.com, as described in the evidence-page finding: protocol, authors, sample and exactly what the 92 % measures, after legal review. Redirect /40-etude-scientifique-soulage-le-dos-gravipack only once that page is live, and send it straight there.
   - Merge the useful facts from /59-concours-lepine-… (medal, year, category) into the existing /gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/ post.
4. **Map URL by URL to pages that exist today on the canonical host.** Do not map to planned URLs such as /cartable-ergonomique/, which would create 404s or later chains. Take the final product URLs from the duplicate-product finding. Suggested map:
   - `/` → home page
   - `/2-accueil` → /boutique-gravipack/
   - `/22-produit` and `/73-gravipack` → /categorie-produit/tous-les-sacs-a-dos-exosquelette/
   - `/72-sac-a-dos-scolaire` → …/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/
   - `/24-sac-a-dos-sport` → …/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/
   - Sherpa 45 → the surviving Sherpa product URL
   - Hikking33 → the Hiking 30L / Terracotta product
   - Business Talk → Business Talk V4 (a current product)
   - Feather → the Feather page if it is re-listed on gravipack.com, otherwise the scolaire category
   - `/content/1-livraison-…` → /conditions-generales-de-vente/, or a dedicated delivery page if one exists
   - `/59-concours-lepine-…` → the Lépine post
   - `/40-etude-scientifique-…` → the new evidence page (step 3)
   - Safar Vibe, Road Adventure and `/plan-du-site-gravipack` → the closest category if they have links or impressions, otherwise **410 Gone**
   - Never send unmapped URLs to the home page. Google treats mass redirects to the home page as soft 404s.
5. **Implement the map at server level on the presta vhost, not inside PrestaShop.** Replace PrestaShop's .htaccess with explicit rules. The host below is an example; use the canonical host from the host finding.
```apache
RewriteEngine On
RewriteRule ^$ https://www.gravipack.com/ [R=301,L]
RewriteRule ^2-accueil/?$ https://www.gravipack.com/boutique-gravipack/ [R=301,L]
RewriteRule ^(22-produit|73-gravipack)/?$ https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/ [R=301,L]
RewriteRule ^72-sac-a-dos-scolaire/?$ https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/ [R=301,L]
RewriteRule ^59-concours-lepine- https://www.gravipack.com/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/ [R=301,L]
RewriteRule ^accueil/16-sac-a-dos-gravipack-hikking33\.html$ https://www.gravipack.com/produit/<slug-hiking>/ [R=301,L]
# ... one line per mapped URL ...
RewriteRule ^accueil/13-sac-a-dos-gravipack-safar-vibe\.html$ - [G,L]
# anything left: 410, never the home page
RewriteCond %{REQUEST_URI} !^/robots\.txt$
RewriteRule ^ - [G,L]
```
   On Nginx, use a `map $uri $presta_target { … }` with `if ($presta_target) { return 301 $presta_target; } return 410;`.
6. **Keep the redirects reachable:**
   - Keep presta.gravipack.com in DNS, keep its vhost and keep a valid TLS certificate for at least 12 months, ideally permanently.
   - Switch off the PrestaShop application, not the host. If the back office must stay online, put it behind HTTP authentication on a separate path.
   - Do not Disallow presta in robots.txt and do not noindex it. Google has to recrawl the URLs to see the 301s.
   - Use the Removals tool only as a temporary cover if a stale price or claim is causing harm; it hides URLs for about 6 months only.
   - Optionally, submit a temporary sitemap listing the 16 legacy URLs to speed up recrawl. Remove it once they show 'Page avec redirection'.
7. **Update the links you control** to their gravipack.com equivalents: post a final news update on each of the 4 KissKissBankBank campaigns, and update old press releases and social bios. Keep this presta map in the single URL-migration sheet shared with the slug and product-merge work. That way a later slug change updates these targets directly and does not create chains.

- **First principle:** Every retired URL that has earned links or rankings should resolve in one hop to its closest live equivalent, or return 410 if there is none. A retired store that still answers or stays indexed competes with the live store using stale facts.
- **Do first:** [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom), [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), `citable-evidence-page`
- **How we'll know the fix failed:** Check 6-8 weeks after deployment. The fix has failed if any of these is true:
- any of the 16 URLs returns 200, 302 or a redirect chain;
- Page indexing in the Search Console Domain property, filtered on presta, reports the legacy URLs as 'Soft 404' or still indexed instead of 'Page avec redirection';
- site:presta.gravipack.com in Google or Bing still lists pages;
- 'gravipack hiking 33' and 'gravipack feather' still show a presta URL and no gravipack.com product.
- **Leading indicator to monitor:** - Number of presta URLs reported as 'Page avec redirection' in Search Console. Target: all mapped URLs, with the rest returning 410.
- Number of presta URLs still indexed. Target: 0.
- Search Console impressions on gravipack.com product pages for 'gravipack hiking', 'gravipack feather', 'gravipack sherpa 45' and 'gravipack business talk'.
- **To verify on-site:** - `curl -sI` on each of the 16 legacy URLs and on https://presta.gravipack.com/, to see the current status (200, 301 or 404);
- robots.txt on the presta host;
- whether the PrestaShop checkout still works;
- Search Console Domain property → Links, for links to presta URLs;
- whether Feather is still sold on gravipack.com;
- the final slugs of the surviving Sherpa, Hiking and Business Talk V4 products.

### 28. Other brand storefronts and hosts (gravipack.ma, gravipacker.com, a probable agency staging host) show different catalogues, model names and prices

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Medium | likely | Technical SEO |

**Issue.** Besides gravipack.com and the legacy presta host, the search results we sampled surfaced three more hosts carrying the brand. None of them has a visible relationship to the main store.

1. **gravipack.ma is a second 'Gravipack®' storefront.**
   - It ranked #1, and its /categories-de-produits/sac-a-dos-bureautique/ page #7, for 'Gravipack sac à dos revendeur boutique'. That query was run with gravipack.com and the big retailers excluded.
   - Searches restricted to .ma returned the home page, /categories-de-produits/sac-a-dos-bureautique/, /product-category/sac-a-dos-gravipack/gravipack-edition-outdoor/ and /product-category/gravipack-accessoire/accessoires-high-tech-bureautique/.
   - Prices are in **euros**: Rome 119.90, Dublin 249.90, Trek Air 25L 129, Sherpa Peak 50L 189 (range about 119-249.90 €).
   - It promises 'livraison rapide partout dans le monde', which overlaps the French market.
   - Some model names do not exist on gravipack.com (Trek Air 25L, Summit Air 35L, Sherpa Peak 50L, against Sherpa 45 and Hiking 30L). Others are shared (Rome, Dublin).
   - Its bureautique page shows a 1-year warranty.
   - It uses two category URL bases (/categories-de-produits/ and /product-category/), and one page says 'boutique en préparation'.
   - We do not know who operates it or whether it is meant as a Moroccan regional store. The brand does have Moroccan press coverage (lematin.ma, challenge.ma, fnh.ma).
2. **gravipacker.com is a third brand domain** (#5 in the same sample). It shows the old Vincennes (94300) address with contact@gravipack.com and pages about test events. The registered seat has been 10 rue de la Paix, 75002 Paris since 19/05/2026.
3. **gravipack.archemia.fr is probably a development or staging host.**
   - It appeared only as the subject of a ScamAdviser report (scamadviser.com/fr/verifier-site/gravipack.archemia.fr, rated 'probably legitimate'). That report ranked #9 for 'gravipack arnaque' in one run.
   - A direct search for the host returned no page from it.
   - Archemia is a communication and web-development agency in Nanterre (Sortlist profile, about 5 people, founded 2023).
   - The duplicate-content risk is speculative, so this is a Low sub-item. The only effect we observed is a scam-checker page carrying the brand name in an 'arnaque' result.

International note (Info): we found no English or other-language Gravipack-owned URL, although demand signals exist: the English KissKissBankBank campaign page, a 2021 English translation on gearxnews (weak), and the Moroccan press. The phase-1 conclusion 'no regional version, hreflang not applicable' is therefore partly contradicted by gravipack.ma. hreflang only becomes relevant if .ma is meant to be the Moroccan version of the same catalogue.

**Evidence.** <https://gravipack.ma/> · <https://gravipack.ma/categories-de-produits/sac-a-dos-bureautique/> · <https://gravipack.ma/product-category/sac-a-dos-gravipack/gravipack-edition-outdoor/> · <https://gravipack.ma/product-category/gravipack-accessoire/accessoires-high-tech-bureautique/> · <https://www.gravipacker.com/> · <https://www.scamadviser.com/fr/verifier-site/gravipack.archemia.fr> · <https://www.sortlist.co.uk/agency/archemia> · <https://www.kisskissbankbank.com/en/projects/gravipack> · <https://lematin.ma/journal/2020/gravipack-permet-gra-bretelles-munies-dinserts-innovants-placer-sac-dos-apesanteur-epaules/329564/amp>

**Why it matters.** Every domain carrying the brand needs one declared role. Two stores selling the same brand in the same language and currency to overlapping markets compete as duplicates, unless they are clearly regional and cross-annotated.

Buyers and AI engines also cannot tell which shop, model names, prices and warranty are official. That adds to the trust doubts already visible in the 'avis' and 'arnaque' results.

Merchant Center ties offers to one claimed website per account and country. A crawlable staging copy duplicates content and leaks unfinished pages.

**Effect on SEO.** Brand and model signals split across domains. gravipack.ma pages can appear in French results next to the official store with different names and prices, and entity facts (address, warranty, model names) conflict across the brand's own sites.

The fix has three parts:
- either hreflang fr-FR / fr-MA backed by real regional differences, or consolidation by 301;
- one list of official domains;
- the staging host behind authentication.
Together they concentrate equity on gravipack.com and remove the conflicting shopping entities.

**How to fix.**

1. **Inventory and ownership.**
   - Check WHOIS and the legal notices of gravipack.ma and gravipacker.com to confirm who runs them: EXOSQUELETTE LIGHT, a licensee or a distributor.
   - Ask Archemia whether gravipack.archemia.fr is theirs and what it hosts.
   - Keep a domain register with these columns: domain, operator, purpose, relationship to gravipack.com, renewal date.
2. **gravipack.ma: decide its role and follow it through.**
   - **(a) If it is the Moroccan store,** make it genuinely regional:
     - prices in MAD, and Moroccan delivery, returns and warranty terms, with a Moroccan legal notice;
     - aligned model names, or a visible French equivalent (e.g. « Sherpa Peak 50L – équivalent France : Sherpa 45 »);
     - a shipping promise limited to the markets it actually serves.
     Then add reciprocal hreflang **only between true equivalent pages**, either in the `<head>` of both sites or in their XML sitemaps:
```html
<link rel="alternate" hreflang="fr-FR" href="https://www.gravipack.com/produit/<rome>/" />
<link rel="alternate" hreflang="fr-MA" href="https://gravipack.ma/<rome>/" />
<link rel="alternate" hreflang="x-default" href="https://www.gravipack.com/produit/<rome>/" />
```
     Yoast and Rank Math do not output cross-domain hreflang, so use a small `wp_head` snippet or the sitemap method. Validate with a crawler's hreflang report (no missing return tags). Also pick one category base on .ma and 301 the other.
   - **(b) If it is not a separate market operation,** 301 it to gravipack.com, path by path where equivalents exist and otherwise to the closest category. Keep the domain registered.
3. **gravipacker.com:**
   - If it is a community or event site, keep it non-commercial, correct the address to the current seat, and link once, clearly, to the official store.
   - If it is redundant, 301 it to the existing /gravipackers/ testimonials page on gravipack.com.
4. **gravipack.archemia.fr (staging):**
   - Run `curl -sI https://gravipack.archemia.fr/`.
   - If it serves a copy of the site, put it behind HTTP Basic Auth. This is the most robust option, because it blocks both crawlers and people:
```apache
AuthType Basic
AuthName Staging
AuthUserFile /chemin/.htpasswd
Require valid-user
```
   - If authentication is impossible, send `Header set X-Robots-Tag "noindex, nofollow"` for the whole host.
   - Do not rely on WordPress's 'Demander aux moteurs de recherche de ne pas indexer ce site'. It is a weak control and is often copied to production by mistake. Add a go-live checklist item that makes sure neither that setting nor the authentication reaches the live site.
   - Search the production database (Better Search Replace, dry run, 'archemia') to confirm that no canonical, hreflang, image or sitemap URL points to the staging host.
   - If staging pages are ever indexed, verify the host in Search Console and use Removals while the authentication takes effect.
5. **Declare the official domains.** List them in the footer and the mentions légales (« Sites officiels : gravipack.com (France) ; gravipack.ma (Maroc) », if .ma is kept). Keep the Organization JSON-LD `url` on the canonical gravipack.com host. Use `sameAs` for profiles (LinkedIn, YouTube, Instagram), not for sister stores.
6. **International (Info).** If English or Spanish sales are ever planned, use subfolders on the canonical host (/en/, /es/) with WPML or Polylang, and self-referencing, reciprocal hreflang that includes x-default. Do not publish machine-translated product pages without review. Until then, no action is needed.

The presta redirect plan has its own finding and is not repeated here.

- **First principle:** Each domain carrying the brand must have one declared role: the canonical store, a genuinely regional store cross-annotated with hreflang, a redirect, or private staging. Undeclared parallel stores and publicly reachable staging hosts split the brand entity and make it look inconsistent.
- **Do first:** [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom)
- **How we'll know the fix failed:** Check after 8 weeks. The fix has failed if any of these is true:
- gravipack.ma pages still appear for French brand or model queries next to the gravipack.com equivalents, either in the gravipack.com Search Console property (Performance by country) or in a French rank tracker;
- a hreflang crawl reports missing return tags;
- `curl` on gravipack.archemia.fr returns 200 without authentication;
- site:gravipack.archemia.fr or site:gravipacker.com shows pages that contradict the official facts.

If the operator check shows that .ma is a separate, legitimate Moroccan licensee planning Moroccan pricing, the overlap risk drops to Low.
- **Leading indicator to monitor:** - Number of brand domains other than gravipack.com in a monthly French brand-SERP check. Target: only the official store plus any declared regional site.
- hreflang errors in the monthly crawl. Target: 0.
- Search Console impressions by country for each domain.
- **To verify on-site:** - WHOIS and the legal notice on gravipack.ma and gravipacker.com, to identify the operator;
- the .ma checkout currency, and whether it ships to France;
- any existing hreflang or canonical tags on gravipack.ma and gravipack.com;
- `curl -sI https://gravipack.archemia.fr/` (expect 401 or a noindex X-Robots-Tag);
- site:gravipack.archemia.fr, site:gravipack.ma and site:gravipacker.com, in both Google and Bing.

### 29. Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Low | needs-on-site-check | Technical SEO |

**Issue.** Four parameter URLs were among the roughly 114 owned URLs observed in the search results we sampled:
- https://gravipack.com/?add-to-cart=6527, titled 'Accueil - Le sac à dos exosquelette GRAVIPACK anti mal au dos'. The current home title we observed is 'Gravipack : le sac révolutionnaire anti mal de dos exosquelette'.
- https://www.gravipack.com/boutique-gravipack/?add-to-cart=2678 ('Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos.').
- https://www.gravipack.com/boutique-gravipack/?order=price ('Boutique Gravipack').
- https://www.gravipack.com/boutique-gravipack/?order=price&filter_product_cat=nouveau-sac-a-dos (107-character title 'Boutique - Sac a dos anti mal de dos GRAVIPACK avec exosquelette allège le poids…').

In the 'gravipack prix' sample, the sort duplicate ?order=price ranked #5, right after the clean /boutique-gravipack/ at #4, and took a brand-query slot.

The titles use old suffixes, which points to old crawl snapshots, so the live site may already handle these URLs. `?order=` and `filter_product_cat=` are not WooCommerce core parameters (core sorting uses `?orderby=`), which suggests a theme or filter widget generates them.

A correction to the earlier version: bot hits on add-to-cart links do **not** affect stock. WooCommerce reserves or reduces stock only at checkout or order, so the only real side effects are analytics and session pollution.

Rated Medium. Downgrade to Low if the live site already noindexes or blocks these states.

**Evidence.** <https://gravipack.com/?add-to-cart=6527> · <https://www.gravipack.com/boutique-gravipack/?add-to-cart=2678> · <https://www.gravipack.com/boutique-gravipack/?order=price> · <https://www.gravipack.com/boutique-gravipack/?order=price&filter_product_cat=nouveau-sac-a-dos> · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** An add-to-cart URL is an action, not a page, and a sort or filter state duplicates the listing it modifies. Once indexed, these copies compete with the real home and shop pages and can be picked as the shop's canonical. They also multiply as more filters are added.

**Effect on SEO.** These URLs waste crawl, create duplicates of the home and shop pages (one of them with an outdated title), and take brand-SERP slots. Bot add-to-cart hits create sessions and carts that distort analytics; they do not affect stock.

Applying noindex in the right order removes these URLs without losing link signals.

**How to fix.**

1. **Check the live behaviour** of the four URLs (see onsite_check). If they already send `noindex` (meta robots or X-Robots-Tag), only monitoring is needed.
2. **Add-to-cart links.**
   - Enable WooCommerce → Réglages → Produits → 'Activer les boutons Ajout au panier en AJAX sur les archives'.
   - Check that the theme keeps WooCommerce's default `rel="nofollow"` on loop add-to-cart buttons. This is a hint to crawlers, not a block.
3. **Noindex the parameter states with one filter.** Do not also add a canonical pointing to another URL on the same page; choose one signal. Yoast omits the canonical on noindexed URLs; check what Rank Math outputs.
```php
// Yoast SEO (code-snippets plugin or child theme)
add_filter( 'wpseo_robots', function ( $robots ) {
  foreach ( array( 'add-to-cart', 'order', 'orderby', 'filter_product_cat', 'min_price', 'max_price' ) as $p ) {
    if ( isset( $_GET[ $p ] ) ) { return 'noindex, follow'; }
  }
  return $robots;
} );
// Rank Math equivalent
add_filter( 'rank_math/frontend/robots', function ( $robots ) {
  foreach ( array( 'add-to-cart', 'order', 'orderby', 'filter_product_cat', 'min_price', 'max_price' ) as $p ) {
    if ( isset( $_GET[ $p ] ) ) { $robots['index'] = 'noindex'; $robots['follow'] = 'follow'; }
  }
  return $robots;
} );
```
4. **Find the widget that creates `?order=` and `filter_product_cat=`.** It may be a theme shop grid, a page-builder product widget, or a filter plugin such as WOOF or YITH.
   - Enable its 'noindex filtered URLs' option, or render the filters as buttons instead of crawlable links.
   - For category navigation, link to the clean /categorie-produit/… URLs instead of `?filter_product_cat=`.
5. **Sequencing.** Wait until Search Console shows these URLs as 'Exclue par la balise noindex' and they have left the index. Only then add this to robots.txt:
```
User-agent: *
Disallow: /*?add-to-cart=
Disallow: /*&add-to-cart=
```
   Blocking earlier would stop Google from seeing the noindex. Keep sort and filter URLs crawlable with noindex, unless Crawl stats show heavy waste.
6. **Check** that the XML sitemap and internal links never include parameter URLs, and that parameter URLs on the non-canonical host are covered by the host redirect (see the host finding).

- **First principle:** Only URLs that represent a distinct, useful page should be indexable. Action URLs (add-to-cart) and sort or filter states of the same listing are duplicates of their clean URL.
- **Do first:** [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom)
- **How we'll know the fix failed:** Check six weeks after the change. The fix has failed if any of these is true:
- Search Console still reports ?add-to-cart=, ?order= or filter_product_cat= URLs as indexed;
- URL Inspection on them shows 'Indexation autorisée ? Oui';
- a brand query still shows /boutique-gravipack/?order=price.

If step 1 shows the live site already noindexes these URLs, the original observation came from stale snapshots and the finding should be closed.
- **Leading indicator to monitor:** - Number of indexed URLs containing '?' in Search Console Page indexing. Target: 0, apart from deliberate exceptions.
- Number of parameter URLs listed as 'Exclue par la balise noindex'.
- Share of Googlebot requests to parameter URLs in Crawl stats.
- **To verify on-site:** On both hosts:
- run `curl -sI 'https://<host>/?add-to-cart=6527'`;
- run `curl -s 'https://<host>/boutique-gravipack/?orderby=price' | grep -i -E 'robots|canonical'`, and the same for the ?order=price&filter_product_cat=nouveau-sac-a-dos variant;
- check for an X-Robots-Tag header or meta robots, and for the canonical.

Also check:
- robots.txt;
- the Yoast or Rank Math robots settings, and any existing wpseo_robots filter;
- the WooCommerce AJAX add-to-cart setting;
- which plugin or widget outputs ?order= and filter_product_cat=.

### 36. Low-value archives and duplicate CMS pages are indexed (attribute/tag archives, a /category/ base, a /test/ copy, duplicate contact pages)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | Technical SEO |

**Issue.** About 8 low-value or duplicate URLs were indexed among the roughly 100 gravipack.com URLs observed in the search results we sampled:
- **WooCommerce attribute archives:** www /attribut-produit/accessoires/exosquelette-gravipack/ ('Archives des Exosquelette Gravipack - Gravipack, le sac à dos …', 109 characters) and /attribut-produit/accessoires/poches-frontales/ (103 characters).
- **Product tag archive:** /etiquette-produit/precommande/ ('Précommande - Sac a dos exosquelette anti-mal de dos Gravipack …', 109 characters).
- **A second blog-category base:** www /category/gravipack-engage-dans-le-handicap-et-l-inclusion/ ('Actualité Handicap - …', 116 characters). It carries the old suffix and may be a stale entry. The main base is /categorie/ (/categorie/innovation/, /categorie/technologie/, /categorie/militaire/, /categorie/outillage/), and those archives use the default title 'X Archives - …' (up to 94 characters).
- **/test/** (www) is indexed with the same title as /gravipack-soulage-les-forces-speciales-au-sofins/ plus the old suffix (122 characters). It looks like a draft copy of the SOFINS post.
- **Two contact URLs:** www /contact-gravipack/ ('Contactez Gravipack') and apex /contacts/ ('Contacts - Le sac à dos exosquelette GRAVIPACK anti mal au dos'). /contacts/ carries the old suffix and may be stale.
- **Two blog listing pages:** /articles/ and /actualites-gravipack-2/. The '-2' only shows that the slug collided with another when the page was created; it does not prove that a sibling page still exists.

Corrections to the earlier version:
- Paginated /page/2/ URLs are **not** a problem; they should stay indexable with a self-referencing canonical.
- 'Thin' would require word and product counts we do not have, so these pages are described as low-value.
- The claim that the Innovation and Militaire archives list the same posts is unsupported and has been dropped.
- The two RATP posts, and /nos-engagements/ versus /a-propos-de-nous-gravipack-au-service-de-votre-dos/, can be legitimately distinct and are not counted as duplicates.
- /devis/ versus /devis-gravipack/ is covered in the B2B finding.

About 8 URLs on a site of about 100 is Low.

**Evidence.** <https://www.gravipack.com/attribut-produit/accessoires/exosquelette-gravipack/> · <https://www.gravipack.com/attribut-produit/accessoires/poches-frontales/> · <https://www.gravipack.com/etiquette-produit/precommande/> · <https://www.gravipack.com/category/gravipack-engage-dans-le-handicap-et-l-inclusion/> · <https://www.gravipack.com/categorie/innovation/> · <https://www.gravipack.com/categorie/militaire/> · <https://www.gravipack.com/test/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/contact-gravipack/> · <https://gravipack.com/contacts/> · <https://www.gravipack.com/actualites-gravipack-2/> · <https://www.gravipack.com/articles/>

**Why it matters.** Archive pages that only re-list a handful of products, and leftover test or duplicate pages, give searchers nothing new. They dilute site-quality signals, use crawl budget, and can appear in place of the real page: /test/ could be shown instead of the SOFINS post, or a stale /contacts/ could show old details. Duplicate contact URLs also split the 'who you are and how to reach you' signals that Google looks for on a merchant site.

**Effect on SEO.** The effects are minor index bloat, a possible wrong-URL choice for the SOFINS post and the contact page, and long templated 'Archives' titles in the results. Cleaning these up concentrates signals on the real category, post and contact pages. The ranking impact is small.

**How to fix.**

1. **Check status first** (see onsite_check). URLs that already return 301 or 404 are stale index entries and need nothing.
2. **/test/:** if it returns 200, 301 it to /gravipack-soulage-les-forces-speciales-au-sofins/ (Redirection, or Rank Math → Redirections). Then delete the test post and empty the Corbeille. If you want to keep it as a working draft, set it to Brouillon or Privé so it stops resolving publicly.
3. **Contact pages:** keep the one used in the menu on the canonical host (likely /contact-gravipack/), and 301 /contacts/ to it, plus /contact/ if that exists. Do not create a new contact URL. The contact details themselves (legal entity, current seat) are handled in the entity-facts finding.
4. **Product attribute and tag archives.** Set them to noindex with one of these:
   - Yoast (v20+): Paramètres → Catégories et étiquettes → 'Étiquettes produits' and each 'Attribut produit (pa_…)' → turn off 'Afficher … dans les résultats de recherche' (labels vary by version).
   - Rank Math: Titres et métas → Étiquettes produits / attributs → Robots meta = No Index.
   - Or remove the archives entirely: Produits → Attributs → edit → untick 'Activer les archives ?'. Then 301 any archive URL that has links to the matching category.
5. **Blog categories:** keep /categorie/innovation/, /technologie/, /militaire/ and /outillage/ indexable only if each gets a short, unique intro and lists enough posts; otherwise set them to noindex,follow. Replace the default 'Archives' title template with `%%term_title%% %%sep%% %%sitename%%` (Yoast) or `%term% %sep% %sitename%` (Rank Math). This is shared with the title-template finding.
6. **/category/ base:**
   - Confirm that Réglages → Permaliens → 'Préfixe des catégories' is set to 'categorie'.
   - If /category/… still answers 200, 301 it to the matching /categorie/… archive with a Redirection regex (`^/category/(.*)` → `/categorie/$1`), but only where the slugs match.
   - Map the handicap archive to its existing /categorie/ equivalent, or to the post it lists.
7. **Blog index:**
   - Check which page is set as the 'Page des articles' under Réglages → Lecture. Keep that one, and 301 the other listing only if it is a true duplicate.
   - Before renaming /actualites-gravipack-2/, look in Pages → Corbeille for an 'actualites-gravipack' item that blocks the clean slug.
   - Any rename gets a 301 and goes into the single migration map.
8. **Leave pagination alone** (/boutique-gravipack/page/2/, /categorie-produit/…/page/2/): self-canonical, indexable, with plain `<a href>` links. Confirm that the Yoast or Rank Math sitemap drops the noindexed taxonomies; both plugins do this automatically.

- **First principle:** Index only pages that serve a distinct purpose for searchers. Archives that merely re-list products, and leftover test or duplicate CMS pages, add crawl and quality noise without ranking for anything useful.
- **Do first:** [#5 gravipack.fr, the audited domain, has no indexed pages, and the store's indexed URLs are split between gravipack.com and www.gravipack.com](#5-gravipackfr-the-audited-domain-has-no-indexed-pages-and-the-stores-indexed-urls-are-split-between-gravipackcom-and-wwwgravipackcom)
- **How we'll know the fix failed:** Check after 6 weeks. The fix has failed if /test/ or /contacts/ still return 200, or if Search Console still reports /attribut-produit/ and /etiquette-produit/ URLs as indexed.

Before applying noindex, also check Search Console Performance: if any of these archives earned clicks in the last 3 months, the 'low-value' hypothesis is wrong for that URL. Give it content instead of noindexing it.
- **Leading indicator to monitor:** - Indexed URL counts in Search Console Page indexing under /attribut-produit/, /etiquette-produit/, /category/, /test/ and /contacts/. Target: 0 for each.
- Duplicate-title count in the monthly crawl.
- **To verify on-site:** - HTTP status on both hosts of /test/, /contacts/, /contact/, /contact-gravipack/, /category/gravipack-engage-dans-le-handicap-et-l-inclusion/ and /actualites-gravipack/;
- the Yoast or Rank Math search-appearance settings for product tags, product attributes and categories;
- whether 'Activer les archives' is enabled on product attributes;
- the posts page set under Réglages → Lecture;
- Search Console clicks for each archive over the last 3 months.

## On-Page SEO

**Score:** **35/100** — 76/98 sampled titles exceed 60 chars (up to 204), 53/98 stack "anti mal de dos", model names often missing, heavy cannibalisation, categories target brand vocabulary instead of market head terms, very long slugs (title-tags, keyword-cannibalisation, category-head-terms, url-slugs). Scored from titles as shown in search results.

**What works:**
- Every product and category page carries a descriptive, French, intent-bearing title
- Use-case categories already exist (randonnée, scolaire, business, militaire, médical, outillage) — the outillage hub already ranks for a generic head term

### 6. Segment categories rank mainly for 'anti mal de dos' wordings and miss the market's generic head terms (sac à dos ergonomique, cartable ergonomique, sac randonnée léger…)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | Medium | likely | On-Page SEO |

**Issue.** The structure is already in place: 10 segment sub-categories exist under /categorie-produit/tous-les-sacs-a-dos-exosquelette/ (randonnée, scolaire, business/télétravail, voyage, urbain, médical, militaire/tactique, outillage, claie de portage, nouveaux). The problem is what they are named after: the brand's technology and benefit ('exosquelette', 'anti mal de dos'), not the generic words the market searches with.

Category titles as indexed:
- Randonnée: 'Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS'
- Scolaire: 'Sac à dos exosquelette scolaire Gravipack allège le poids de 92%'
- Business: 'Sac à dos exosquelette anti-mal de dos business voyage d'affaires'
- Urbain: 'Sac à dos exosquelette urbain Gravipack allege le poids sur le dos'
- Médical: 'Sac à dos médical Gravipack allégez vos missions sauvez des vies'
- Militaire: 'Sac à dos exosquelette militaire d'assault allège le poids Gravipack'
- Claie: 'Claie de portage Gravipack anti-TMS pour charges très lourdes'
- Parent hub: 'Achetez un sac à dos révolutionnaire avec exosquelette Gravipack'
Category slugs run 90-151 characters.

Where they rank. These are extended-mode results from the search results we sampled (a US-located, non-Google index); positions are directional.
- With the 'anti mal de dos' feature modifier, gravipack.com does rank:
  - 'sac à dos scolaire anti mal de dos': #1-#3 (two Kingston product pages and the scolaire category)
  - 'sac à dos ergonomique mal de dos': #2 and #4 (Hiking 30 L Gris, home page)
  - 'sac à dos anti mal de dos': #4-#6
  - 'sac à dos randonnée anti mal de dos': #5-#6 (randonnée category, home page)
  - 'sac à dos ordinateur ergonomique anti mal de dos': #3-#5 (Business Talk V4 25 L, business category, home page)
- The exception that proves the model: the outillage hub ranks #9 for the generic 'sac à dos porte-outils', behind ManoMano, Leboncoin, DeWalt, Leroy Merlin, Hellopro, Rubix, OPPBTP and Fischer Darex. A second run reproduced this identically. Its title now reads 'Sac à dos exosquelette pour l'outillage professionnel Gravipack', which uses the market's words and has no 'anti mal de dos'.
- Absent for the generic wordings:
  - 'sac à dos ergonomique': sacados.fr, mon-sac-a-dos.fr, karkoa, sacroche, la-sacoche-officielle, accergo, le-repaire-du-sac-a-dos, arsayo, ma-boutique-ergonomique. Six of the nine are collection or product pages named after the query. Standard mode (osprey, manor, ergobag, deuter) showed no Gravipack either.
  - 'cartable ergonomique': lespetitsbaroudeurs (ergobag + a category), mon-sac-a-dos, mahilana, ma-boutique-ergonomique ×4, univers-cartable. It shares 0 URLs with 'sac à dos scolaire anti mal de dos', so it is a separate set of results.
  - 'sac à dos ordinateur ergonomique': mon-sac-a-dos, Eastpak, Darty, Ergonovie.
  - 'sac à dos médical secouriste': Girodmedical, SMSP, Praxisdienst.
  - 'sac à dos militaire tactique léger': Projet13, Mode-Tactique, V8.
- Likely absent (standard mode or single runs only):
  - 'sac à dos randonnée léger ergonomique' (deuter ×4, alpinstore ×3, glisshop)
  - 'sac à dos randonnée 60+10' (deuter, alpinstore, tonton-outdoor, alltricks), although Helsinki and Oslo are 60+10 L
  - 'sac à dos voyage ergonomique' (deuter Voyager ×7, osprey, thule)
  - 'claie de portage ergonomique' (alpinstore, tonton-outdoor)
  - 'sac à dos Compostelle mal de dos' (conseilsport.decathlon.fr, pilgrim sites), although Compostelle products exist and 'compostelle' is in the randonnée slug
  - 'sac à dos vélotaf ergonomique' (tonton-outdoor, culturevelo)
- 'Sac à dos ergonomique' appears in the titles of the Centurion, Kingston and Dublin product pages and of /mentions-legales/, but in no category title.

School nuance: the 'cartable ergonomique' results are led by primary-school cartables (ergobag Prime 'cartable CP primaire', univers-cartable). Gravipack's scolaire category targets collège, lycée and étudiants (per its slug), and its school products (Kingston, G-Pack 'collège-lycée') are backpacks. 'Cartable' is an adjacent segment and should be used only where it describes the product accurately.

Realistic upside: head-term results are dominated by Deuter, Osprey, military.eu and large retailers. The likely gain is in the mid-tail and in moving from page 2 to page 1, as the outillage hub shows, rather than a top-3 position for 'sac à dos ergonomique'.

**Evidence.** <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-ordinateur-anti-mal-de-dos-business-tele-travail-professionnel/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/> · <https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-medical/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-militaire-tactique-assault-anti-mal-de-dos/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-voyage-gravipack-anti-mal-de-dos/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-urbain/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/claie-de-portage/> · <https://sacados.fr/collections/sac-a-dos-ergonomique/> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/> · *(+7 more in findings/)*

**Why it matters.** For commercial category queries, the page type that wins is a category or collection page whose title and H1 name the category the way searchers do. Buyers search by activity plus feature ('sac à dos randonnée ergonomique', 'sac à dos ordinateur ergonomique', 'sac à dos porte-outils', 'sac à dos médical') and compare specifications.

Hubs written only around the brand's own vocabulary catch the 'anti mal de dos' long tail and miss most of each segment's demand, even though the products fit those queries.

**Effect on SEO.** Adding the market head term to each category's title, H1 and intro, while keeping 'anti mal de dos' as a secondary term, should extend category visibility beyond the modifier long tail. It should reach mid-tail and some head queries in randonnée, business, scolaire, médical and militaire, as already happened for outillage.

Spec-rich buying-guide copy (volume, empty weight, laptop size, strap sizes) also matches the comparison vocabulary that competitors and AI answers use.

**How to fix.**

1. Size the opportunity first.
   - Pull French volumes and difficulty (Google Keyword Planner or DataForSEO, location France) for: 'sac à dos ergonomique', 'cartable ergonomique', 'sac à dos scolaire ergonomique', 'sac à dos ordinateur ergonomique', 'sac à dos randonnée ergonomique', 'sac à dos porte-outils', 'sac à dos médical', 'sac à dos tactique', 'claie de portage', 'sac à dos vélotaf'.
   - Add GSC impressions per category.
   - Prioritise the 2-3 segments with the best combination of volume and product fit.
2. Do not rename the parent slug 'tous-les-sacs-a-dos-exosquelette'. WooCommerce category URLs are hierarchical, so a rename changes about 12 child URLs, as well as the URL that currently ranks for 'sac à dos exosquelette'.
   - For 'sac à dos ergonomique', start by giving the existing hub a title and H1 that carry both terms. Use the same wording as the cannibalisation fix: title 'Sac à dos ergonomique à exosquelette, anti mal de dos | Gravipack', H1 'Sacs à dos ergonomiques à exosquelette, anti mal de dos'.
   - Only if the hub still gets no impressions for 'sac à dos ergonomique' after 8-12 weeks, create a separate landing page or top-level category 'Sacs à dos ergonomiques'. Give it a distinct angle (comparison by use) so it does not duplicate the hub.
3. Retitle each segment category as market term + differentiator + brand. Add the generic term and keep 'anti mal de dos' where the category already ranks with it. Change the category Name in Produits → Catégories and the SEO title; keep the slug. Character counts in brackets:
   - Randonnée: 'Sac à dos randonnée ergonomique anti mal de dos | Gravipack' (59)
   - Business: 'Sac à dos ordinateur ergonomique anti mal de dos | Gravipack' (60)
   - Scolaire: 'Sac à dos scolaire ergonomique à exosquelette | Gravipack' (57). Add 'cartable' to the copy only for models suited to primary school, if there are any.
   - Outillage (already ranks #9): light touch only, e.g. 'Sac à dos porte-outils pro à exosquelette | Gravipack' (53). Test this change on its own, and do not change the URL.
   - Médical: 'Sac à dos médical et secouriste ergonomique | Gravipack' (55)
   - Militaire: 'Sac à dos tactique militaire ergonomique | Gravipack' (52). This also fixes the 'assault' typo.
   - Voyage: 'Sac à dos de voyage ergonomique à exosquelette | Gravipack' (58)
   - Urbain: 'Sac à dos urbain et vélotaf ergonomique | Gravipack' (51), but only if the bike-suited models (Tokyo, Rome) are in this category.
   - Claie: 'Claie de portage ergonomique, charges lourdes | Gravipack' (57). Drop 'anti-TMS' until the claims review decides.
   Make each H1 the category name, carrying the same head term.
4. Copy for each category. claude-seo's category gate is 400+ words; Google sets no word count.
   - Above the grid, 50-120 words: what the category is, who it is for, and the differentiator.
   - Below the grid, 400-600 words: a spec comparison table across the models (volume, empty weight, max load, laptop size, rain cover, strap sizes M-XXL), sizing advice, real use cases, and links to guides.
   - Add a 'Compostelle' H2 to the randonnée category.
   - Example intro for randonnée: « Nos sacs à dos de randonnée ergonomiques intègrent un exosquelette breveté qui répartit la charge entre le dos et les épaules. Du sac à la journée au sac de trek 60+10 L, choisissez selon la durée de vos sorties, le volume et la taille de vos bretelles. »
5. If attribute filters are added (usage, volume, ordinateur), keep filter combinations out of the index with one method only: either noindex,follow or a canonical to the base category, not both.
6. Slugs: change category slugs only for hubs that do not rank, and only inside the single URL migration release, with 1:1 301s. Do not toggle Rank Math's 'Remove product category base' (Rank Math → General Settings → WooCommerce) outside that release: it changes every category URL.
7. Structured data: CollectionPage + ItemList + BreadcrumbList on each category (see the cannibalisation finding).
8. Track these terms in a France/Google.fr rank tracker (mobile): 'sac à dos porte-outils', 'sac à dos ergonomique', 'sac à dos ordinateur ergonomique', 'sac à dos scolaire ergonomique', 'sac à dos médical secouriste', 'sac à dos randonnée ergonomique'.

- **First principle:** Commercial category queries are answered by pages whose title, H1 and copy name the category in the searcher's words. Gravipack's categories use the brand's own language ('exosquelette', 'anti mal de dos'). That wins the brand's long tail but not the generic vocabulary. The one hub whose title uses a market term ('outillage professionnel') is also the one that ranks for a generic head term.
- **Do first:** [#9 Dozens of pages target the same 'anti mal de dos' and 'exosquelette' terms, so the home page, category hub and product pages compete](#9-dozens-of-pages-target-the-same-anti-mal-de-dos-and-exosquelette-terms-so-the-home-page-category-hub-and-product-pages-compete), [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation)
- **How we'll know the fix failed:** Eight to twelve weeks after retitling, one of these is true:
- GSC shows no new impressions on the retitled categories for queries without 'mal de dos' (the generic head terms).
- Impressions for the 'anti mal de dos' queries on those categories have dropped by more than 20 %.
In either case, revert the wording on that category.
- **Leading indicator to monitor:** Monthly in GSC: for each category URL, open Pages → that URL → Queries, and exclude queries containing 'mal de dos' or 'gravipack'. Track the number of generic queries with impressions and their average position. Also track rank-tracker positions for the 6 benchmark terms.
- **To verify on-site:** Check on the live site:
- The live title, H1, meta description, intro copy and word count of the parent hub and the 10 sub-categories.
- The product count in each category.
- Whether the scolaire range includes products suited to primary-school children.
- Whether a filter plugin creates indexable parameter URLs.
- The Rank Math/Yoast category-base settings.
- GSC impressions per category before the change.

### 9. Dozens of pages target the same 'anti mal de dos' and 'exosquelette' terms, so the home page, category hub and product pages compete

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | Medium | likely | On-Page SEO |

**Issue.** The repetition is real. These counts come from titles and URLs as indexed in the search results we sampled (a US-located, non-Google index):
- 53 of 98 gravipack.com titles contain 'anti mal de dos', 'anti-mal de dos' or 'anti mal au dos'.
- 28 of 39 product titles contain it, and 37 slugs contain 'anti-mal-de-dos'.
- 66 of 98 titles contain 'exosquelette'.
- The site-wide title suffix adds both terms to 13 more pages.
- At least 11 URLs target 'sac (à dos) randonnée anti mal de dos' by title or slug: the randonnée category, Sherpa bleu ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa'), Pearl ('Sac randonner léger…'), Easy Travel and Helsinki (slug 'sac-randonner-leger-anti-mal-de-dos'), Compostelle 80 L ('…randonnée 80L révolutionnaire anti mal de dos pas cher'), Oslo Rouge, Hiking Terracotta, Hiking Gris, Sherpa Kaki, and presta /24-sac-a-dos-sport.
- The same models also exist under several URLs: G-Pack ×2, Light Promax ×3, Business Talk V4 ×3, Cargo Max ×2, Kingston ×2, and Sherpa Kaki on both /produit/ and /produit-gravipack/. This is the clearest source of competing URLs and is handled in the duplicate-product finding.

What the sampled results show. These are extended-mode results; positions are directional and come from single runs, and standard mode disagreed.
- 'sac à dos anti mal de dos': gravipack.com held 3 of 9 results (Pearl product page, home page, Tokyo product page). ergo-corner.com, a reseller of Gravipack, held 3 more, and an ici.fr piece about Gravipack 1, so 7 of the 9 results relate to Gravipack. In standard mode no gravipack.com URL appeared; decathlon.fr/vc/gravipack did.
- 'sac à dos randonnée anti mal de dos': the randonnée category ranked about #5 and the home page about #6, so the intended category does rank.
- 'sac à dos porte-outils anti mal de dos': 5 Gravipack URLs in the top 10 (ExoTool, Light Promax ×2, ToolMaster, outillage category). That is domination of the results, not proof of harm.
- 'sac à dos scolaire anti mal de dos': two Kingston URLs and the scolaire category hold #1-#3.
- 'sac à dos exosquelette': the main category and the home page both appear, at about #6-#7.
- The existing hub, /categorie-produit/tous-les-sacs-a-dos-exosquelette/, is not the URL that ranks for 'sac à dos anti mal de dos'; the home page and single product pages are. The hub is titled 'Achetez un sac à dos révolutionnaire avec exosquelette Gravipack' (page 2: 'Tous les sacs à dos anti-mal de dos exosquelette Gravipack') and has 10 segment sub-categories.
- The three 'anti mal de dos' query variants share 4 URLs pairwise. But those are the most ubiquitous URLs in the whole data set (ergo-corner/55, ergo-corner/13, arsayo, the home page). Without ergo-corner the overlap drops to 2, which calls for interlinking the pages, not for one page serving all three queries.

What is not shown: that rankings are diluted or rotating. Several URLs from one site in a results page is extra visibility. Real cannibalisation, meaning URLs alternating for one query and splitting its impressions, can only be confirmed in Search Console.

**Evidence.** <https://gravipack.com/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/> · <https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/page/2/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-easy-travel-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · <https://gravipack.com/produit/vive-la-rentree-scolaire-sac-anti-mal-de-dos-college-gravipack-kingston-avec-exosquelette/> · *(+5 more in findings/)*

**Why it matters.** When dozens of pages present the same primary term, the engine, not the site, decides which URL answers each query.

For broad category intent ('sac à dos anti mal de dos', 'sac à dos exosquelette'), the page type that usually wins is a category page with buying-guide content. A product page covers one model, and the home page is navigational.

If the hub is not clearly signposted as the answer, links and engagement stay spread across the home page and individual products. Then the page best suited to the brand's main phrase cannot build up its strength.

**Effect on SEO.** Concentrating the head terms on the existing hub (title, H1, copy, internal anchors), while product pages lead with use + model, should make one URL the stable answer for each head query. Product pages then capture the long tail.

If GSC shows URLs alternating, consolidation reduces position swings and recovers clicks lost to the wrong landing page, for example a 60 L trekking bag shown for a commuter query. If GSC shows no alternation, the gain is smaller and comes mostly from the hub's better relevance.

**How to fix.**

1. Confirm in Search Console first. That is Google.fr data; this audit's positions come from a different engine.
   - Go to Performance → Search results, add a Query filter (contains) for 'anti mal de dos', and open the Pages tab.
   - Repeat for 'sac à dos exosquelette', 'randonnée anti mal de dos', 'scolaire anti mal de dos' and 'porte outils'.
   - Cannibalisation means two or more URLs each take a meaningful share of impressions for the same query, with positions alternating week to week. To see this, compare date ranges, or use Looker Studio with the GSC connector (query + page by week).
   - If one URL already takes more than about 80 % of a query's impressions, leave that query alone.
2. Build a keyword-to-URL map in one sheet with columns: query | intent | target URL | allowed secondary URLs | internal anchor.
   - Existing hub /categorie-produit/tous-les-sacs-a-dos-exosquelette/ → 'sac à dos anti mal de dos' + 'sac à dos exosquelette' (+ 'sac à dos ergonomique'; see the category head-terms finding)
   - Home page → brand terms ('Gravipack', 'sac à dos Gravipack') + 'sac à dos exosquelette'. Keep 'anti mal de dos' in the home title until the hub ranks.
   - Randonnée category → 'sac à dos randonnée anti mal de dos / ergonomique'
   - Scolaire category → 'sac à dos scolaire anti mal de dos'
   - Business category → 'sac à dos ordinateur ergonomique anti mal de dos'
   - Outillage → 'sac à dos porte-outils'; Claie → 'claie de portage'
   - Product pages → use + model + capacity, with 'anti mal de dos' as a secondary modifier.
3. Retarget the existing hub. Do not create a new /sac-a-dos-anti-mal-de-dos/ URL; that would add yet another competing page.
   - Title: 'Sac à dos ergonomique à exosquelette, anti mal de dos | Gravipack' (65 characters; only the brand falls in the cut-off zone).
   - H1: 'Sacs à dos ergonomiques à exosquelette, anti mal de dos'.
   - Both are subject to the health-claims wording decision.
   - Add an 80-150-word intro above the product grid: what the exoskeleton does and who each segment is for.
   - Put the longer buying guide below the grid: how to choose by use, volume and strap size (M-XXL), with links to each segment category.
   - To print bottom-of-category text from a term meta field, add to the child theme:
   add_action( 'woocommerce_after_shop_loop', function () {
       if ( ! is_product_category() ) { return; }
       $term = get_queried_object();
       $html = get_term_meta( $term->term_id, 'seo_bottom_text', true );
       if ( $html ) { echo '<section class="cat-guide">' . wp_kses_post( wpautop( $html ) ) . '</section>'; }
   }, 20 );
4. Stage the change in this order:
   a. Publish the hub copy and the internal links.
   b. Wait 4-6 weeks and re-check GSC.
   c. Only then make the home title brand-led and move product titles to use + model.
   Never strip 'anti mal de dos' from all product titles at once: the audit found those titles currently earn long-tail visibility.
5. Internal links. These are the strongest signal the site controls.
   - Add a main menu item 'Sacs à dos anti mal de dos' pointing to the hub. Link the home hero and category tiles to the hub and the segment categories with descriptive anchors.
   - On every product page, enable breadcrumbs (Yoast, Rank Math or WooCommerce) and add one contextual link to its segment category, e.g. 'Voir tous nos sacs de randonnée à exosquelette'.
   - Blog posts should link to categories, not to random products.
   - The exact anchor 'sac à dos anti mal de dos' points only to the hub.
6. Consolidate same-model duplicates (G-Pack, Light Promax, Business Talk V4, Cargo Max, Kingston) as described in the duplicate-product finding. If the 'Vive la rentrée scolaire' Kingston URL is the same product as the main Kingston URL, 301 it there.
7. Structured data on the hub: CollectionPage + ItemList + BreadcrumbList, not Article.
   - Yoast and Rank Math already output CollectionPage and BreadcrumbList for product categories in their @graph. Add only the ItemList, via the wpseo_schema_graph or rank_math/json_ld filter, so the page keeps a single graph. For example:
   {"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":1,"url":"https://gravipack.com/produit/<sherpa-45>/"},{"@type":"ListItem","position":2,"url":"https://gravipack.com/produit/<oslo-60-10>/"}]}
   - Use the canonical host decided in the host fix.
8. Repeat step 1 eight weeks after each stage.

- **First principle:** An engine normally shows only one or two URLs per site for a query. When many pages carry the same primary term, internal links, anchors and titles are the site's main way to tell the engine which URL is the intended answer. Without them the engine chooses, and its choice can change from week to week.
- **Do first:** [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation)
- **How we'll know the fix failed:** Eight to twelve weeks after the hub is retargeted and linked, one of these is true:
- GSC still shows the home page and product pages taking most of the impressions for 'sac à dos anti mal de dos' (hub share under about 20 %), with alternating URLs.
- Total clicks for the query group have fallen below the baseline.
In that case, revert the product title changes and review the hub copy and links.
- **Leading indicator to monitor:** In GSC, weekly:
- the number of distinct gravipack.com URLs with impressions for each head query;
- the hub's impressions and average position for 'sac à dos anti mal de dos' and 'sac à dos exosquelette';
- the share of the query group's clicks that land on the mapped URL.
- **To verify on-site:** Check on the live site and in the client's tools:
- GSC Performance, query → pages, for the five head queries (not available to this audit).
- Screaming Frog inlinks and anchor-text report for the hub and the segment categories.
- The hub's live title, H1, intro and word count.
- Breadcrumb output on product pages.
- Whether the two Kingston URLs and the two G-Pack URLs are the same product.

### 11. Title tags are over-long, carry a bloated site-wide suffix and stacked claim keywords, and sometimes omit the model name or contain typos

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | Medium | likely | On-Page SEO |

**Issue.** Source: the titles of 114 URLs (98 on gravipack.com / www.gravipack.com and 16 on the legacy presta.gravipack.com) as they were displayed in the search results we sampled. These came from a US-located, non-Google index. Displayed titles can differ from the raw <title>, so every number below needs an on-site check.

1. Length. 76 of the 98 gravipack.com titles exceed 60 characters (median 65; 29 exceed 80). Including presta, the figure is 87 of 114. One counted title (the RATP post) ends in '...', so its length is a lower bound. The extremes:
- Compostelle 65 L: 204 characters. Compostelle 25 L and 35 L: 182.
- The post /cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/: 154.
- Helsinki: 136 ('Sac à dos GRAVIPACK exosquelette 60+10 L : soulage le dos et les épaules, répartit la charge. Recommandé pour randonnée et port prolongé'). This is a description pasted into the title field.
- /test/ 122, Kingston 118, /category/gravipack-engage-dans-le-handicap-et-l-inclusion/ 116, Dublin 101, Tokyo 95, Sherpa Kaki 90, Hiking Terracotta 90, Austerlitz 85.
- The home page title is 63 characters ('Gravipack : le sac révolutionnaire anti mal de dos exosquelette') in the main snapshot. It is not a product title.

2. Bloated site-wide suffix. 13 URLs end in ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant' (73 characters): Compostelle 25/35/65 L, /gravipackers/, /articles/, /test/, the 'révolution' post, /categorie/innovation/, /categorie/technologie/, /categorie/militaire/, /categorie-produit/accessoires-sac-a-dos/ and two /attribut-produit/ archives. Search engines shorten titles; they do not lengthen them. So this is almost certainly the live title template (the site name or tagline fed into the site-name variable). At least two templates were observed. Other URLs end in ' - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos.' (/etiquette-produit/precommande/, the /category/…handicap archive) or in ' - Le sac à dos exosquelette GRAVIPACK anti mal au dos' (/contacts/, /devis/). These may come from older crawl snapshots.

3. Default archive wording is still in use: 'Innovation Archives', 'Technologie Archives', 'Militaire Archives', 'Outillage Archives', 'Accessoires sac à dos Archives', 'Archives des Exosquelette Gravipack', 'Archives des Poches frontales'. These are the English and French defaults of the SEO plugin's taxonomy template.

4. Model names are missing, or sit at characters 46-68, where the title is cut off.
- No model name: Oslo Rouge ('Sac ergonomique de randonnée anti-mal de dos avec exosquelette', which also has no brand), Centurion ('Sac à dos ergonomique anti-mal de dos avec exosquelette Gravipack'), ToolMaster ('Sac outillage anti-mal de dos exosquelette'), both Business Talk V4 25 L URLs ('Sac à dos exosquelette 25L anti-mal de dos pour deux ordinateurs' and 'Sac à dos ordinateur 25L anti-mal de dos révolutionnaire'), and Gravitech/Barracuda ('Claie de portage révolutionnaire exosquelette anti-mal de dos').
- No brand: Sherpa bleu ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa') and Oslo.
- Identical titles on different URLs: G-Pack ×2, Light Promax ×2 ('Sac à dos outillage anti-douleur exosquelette Gravipack®'), Cargo Max ×2, Sherpa Kaki ×3. The duplicate URLs themselves are covered in the duplicate-product finding.

5. Typos. These were verbatim at crawl time. Search engines do not introduce typos, but some may have been fixed since.
- 'Sac randonner léger … Pearl': 'randonner' is the verb; it should be 'randonnée'.
- 'militaire d'assault' (militaire category): should be 'd'assaut'.
- 'allege' (urbain category): should be 'allège'.
- 'Sac a dos' (Dublin, a shop filter URL, the Précommande tag, presta): should be 'Sac à dos'.
- 'ce sac à dos allègent' (presta home): should be 'allège'.
- Lowercase starts: 'fabrication professionnelle…' and 'gravipack' (Rome: 'Sac anti mal de dos business ROME ergonomique gravipack').
- Brand casing varies: Gravipack / GRAVIPACK / GraviPack® / Gravipack®.

6. Thin or off-target titles:
- 'Boutique Gravipack' (18 characters; on the shop, its /page/2/ and ?order=price), 'Contactez Gravipack' (19), 'Nos engagements' (15).
- /mentions-legales/: 'Le sac à dos ergonomique - Mentions légales, tout ce que vous devez savoir sur Gravipack.' (89).
- A seasonal 'Vive la rentrée scolaire…' title on an evergreen Kingston product page.

7. Stacked claim tokens:
- 'révolutionnaire' in about 10 titles (home, main category, G-Pack ×2, City, Business Talk V4 ×2, Compostelle 80 L, Gravitech…)
- 'anti douleur' / 'anti-douleur' (Sherpa Kaki, Light Promax ×2)
- 'anti-TMS' (randonnée and claie categories)
- '92%' (scolaire category, one post)
- 'apesanteur' (6, mostly presta)
- 'meilleur' and 'Le seul sac à dos au monde' (presta)
The health-claims finding decides what wording is allowed. This finding covers length, template and format.

Not claimed: that Google is rewriting these titles (the index sampled is not Google), or that the home page has two titles (one of them belonged to a ?add-to-cart= parameter URL).

What already works: several category titles are close to the target length. Outillage is 63 characters ('Sac à dos exosquelette pour l'outillage professionnel Gravipack'), claie de portage 61, 'Tous les sacs à dos anti-mal de dos exosquelette Gravipack' 58, and /faq/ 58.

**Evidence.** <https://gravipack.com/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-de-survie-65-litres-ergonomique-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme-copie/> · <https://www.gravipack.com/produit/sac-a-dos-de-survie-35-litres-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme/> · <https://www.gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-helsinki-gravipack-60l-10l-70l/> · <https://www.gravipack.com/cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/> · <https://www.gravipack.com/categorie/innovation/> · <https://www.gravipack.com/categorie/militaire/> · <https://www.gravipack.com/attribut-produit/accessoires/poches-frontales/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-toolmaster-orange-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · *(+6 more in findings/)*

**Why it matters.** The title is the headline of every organic result and the strongest on-page hint of what a page is about. claude-seo's quality gate asks for 30-60 characters, the primary keyword near the start, the brand last, and a unique title per page.

Google cuts titles by pixel width (about 580-600 px, roughly 55-65 characters). On most Gravipack product pages, that cut falls before the model name and capacity, which are what a buyer who already knows the range types ('gravipack sherpa', 'gravipack oslo 60+10'). As a result, every result reads like its siblings: 'Sac … anti mal de dos … exosquelette …'.

The 73-character tagline repeats 'exosquelette anti-mal de dos' on every templated page. This adds to the site-wide keyword repetition and makes legal, archive and test pages present themselves on the same words as products.

Typos and stacked superlatives ('révolutionnaire', 'anti douleur') sit in the most visible line of the snippet. That hurts trust with a French audience that is already sceptical in the forum and review results.

**Effect on SEO.** The effect is mainly on CTR and relevance, not on indexing.
- Shorter titles with the model near the start show the model, capacity and use in full. This helps model queries, where marketplaces and resellers currently outrank gravipack.com, and click-through on long-tail queries.
- Removing the suffix cuts site-wide keyword repetition, and stops archive and utility pages from presenting themselves as product pages.
- Over-long or boilerplate titles invite engines to rewrite them, which reduces control over the message.

Under claude-seo, title length is a CTR issue rather than an eligibility issue, hence Medium.

**How to fix.**

Stage 0 – Baseline (before any change)
1. Export the current titles from Screaming Frog (Page Titles tab → Export) or from the Yoast/Rank Math bulk editor.
2. Export GSC Performance → Pages for the last 3 months (clicks, impressions, CTR, position) for all product, category and post URLs. Keep both files as the baseline.

Stage 1 – Remove the suffix at template level (day 1, low risk)
3. Find where the tagline comes from. It is usually the WordPress Site Title (Réglages → Général) or the SEO plugin's site name. Menu labels vary by plugin version.
   - Yoast v20+: Yoast SEO → Settings → Site basics. Set Website name = 'Gravipack' and choose '|' or '–' as the separator.
   - Rank Math: set the separator in Titles & Meta → Global Meta and the website name in Titles & Meta → Local SEO.
   - Setting the site name to 'Gravipack' also gives Google a clean WebSite name.
   - The slogan can stay as the WordPress tagline, but it must not appear in any title template (%%sitedesc%% / %sitedesc%).
4. Set the templates (Yoast → Settings → Content types / Categories & tags; Rank Math → Titles & Meta):
   - Products: %%title%% %%sep%% %%sitename%% (Rank Math: %title% %sep% %sitename%)
   - Product categories: %%term_title%% %%page%% %%sep%% %%sitename%% (Rank Math: %term% %page% %sep% %sitename%)
   - Posts: %%title%% %%sep%% %%sitename%%
   - Post categories: %%term_title%% – Actualités %%page%% %%sep%% %%sitename%%
   - Product tags and attribute archives: %%term_title%% %%sep%% %%sitename%% (whether they stay indexed is handled in the thin-archive finding).
   Remove 'Archives' and 'Archives des' everywhere. Do not use %%primary_category%% in the product template: the category names are long and would bring back titles of 80+ characters.
5. Check that no page has the tagline hard-coded in its own SEO title field. Take a backup, then run in phpMyAdmin or WP-CLI:
   SELECT post_id, meta_value FROM wp_postmeta WHERE meta_key IN ('_yoast_wpseo_title','rank_math_title') AND meta_value LIKE '%homme femme enfant%';
   Also confirm that the theme declares add_theme_support('title-tag') and does not print its own <title>, and that only one SEO plugin is active.

Stage 2 – Typos and thin titles (week 1)
6. Fix the typos: 'randonnée' (not 'randonner'), 'd'assaut', 'allège', 'Sac à dos', 'allègent' → 'allège', and capitalise the first letter of each title. Use one brand spelling in titles, 'Gravipack'; keep ® for body copy only.
7. Rewrite the thin or off-target titles (character counts in brackets):
   - Shop: 'Boutique sacs à dos à exosquelette | Gravipack' (46)
   - Contact: 'Contact et devis entreprise | Gravipack' (39)
   - Engagements: 'Nos engagements : dos, santé, inclusion | Gravipack' (51)
   - Legal: 'Mentions légales | Gravipack' (28)
   - CGV: 'Conditions générales de vente | Gravipack' (41)
   - Kingston: remove 'Vive la rentrée scolaire' from the evergreen title and use a seasonal banner instead.

Stage 3 – Product titles (after the keyword map in the cannibalisation finding and the health-claims wording decision)
8. Format: [use term] + [model + capacity/colour] + [differentiator] | Gravipack.
   - Keep it to 60 characters or fewer.
   - Put the model within the first ~35 characters so it is never cut off.
   - The use term stays first because model names have little search demand of their own (claude-seo: primary keyword near the start).
   - Keep 'anti mal de dos' as a secondary modifier where the claims decision allows it. Do not strip it from every product title before the category hub ranks for it.
   Examples:
   - 'Sac de randonnée Sherpa 45 L à exosquelette | Gravipack' (55)
   - 'Sac de trek Oslo 60+10 L rouge, anti mal de dos | Gravipack' (59)
   - 'Sac à dos ordinateur Business Talk V4 25 L | Gravipack' (54)
   - 'Sac porte-outils ToolMaster à exosquelette | Gravipack' (54)
   - 'Sac à dos ergonomique Centurion à exosquelette | Gravipack' (58)
   - 'Sac de voyage Pearl 29 L anti mal de dos | Gravipack' (52)
   - 'Sac à dos urbain Austerlitz à exosquelette | Gravipack' (54)
   - 'Sac de trek Compostelle 65 L ergonomique | Gravipack' (52)
   - 'Sac à dos de trek Helsinki 60+10 L | Gravipack' (46)
   For the claie, confirm the current model name first: the URL says Gravitech, the copy says Barracuda.
9. The product name is the H1 and also feeds the Merchant Center feed. It can stay model-first and descriptive, e.g. 'Gravipack Sherpa 45 L – Sac de randonnée à exosquelette'. Set the SEO title separately in the Yoast/Rank Math box.
10. Roll out in two batches. Do 10 products first and compare their CTR and impressions with the baseline after 4 weeks, then do the rest. Tools: Yoast SEO → Tools → Bulk editor, the SEO title column on Rank Math's Products list, or a CSV import (WP All Import).

Stage 4 – Posts
11. Editorial H1s can stay expressive. Give each post its own SEO title of 60 characters or fewer, starting with the 154-character 'révolution' post and /test/ (which should be removed; see the duplicate-pages finding).

Stage 5 – QA
12. Re-crawl with Screaming Frog and check Page Titles → Over 60 characters / Over 561 pixels / Duplicate / Below 30 characters. Targets:
   - zero duplicates;
   - zero titles containing 'homme femme enfant' or 'Archives';
   - fewer than 10 % of indexable URLs over 60 characters.

- **First principle:** A title is a page's label in the results list. It must say what is unique about the page (model, capacity, use) within the first ~55 characters. A template suffix is identical on every page, so it adds length without telling one page from another.
- **Do first:** [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), [#9 Dozens of pages target the same 'anti mal de dos' and 'exosquelette' terms, so the home page, category hub and product pages compete](#9-dozens-of-pages-target-the-same-anti-mal-de-dos-and-exosquelette-terms-so-the-home-page-category-hub-and-product-pages-compete)
- **How we'll know the fix failed:** 1) A re-crawl 48 h after the template change still finds titles containing 'homme femme enfant' or 'Archives'. That means the tagline is hard-coded somewhere: the theme, a per-page SEO title field, or a second SEO plugin.
2) Six to eight weeks after each product batch, GSC CTR for the rewritten URLs is not higher than the baseline at comparable average positions, or impressions for 'anti mal de dos' queries on those product pages fall by more than 20 %. In that case, revert those titles or restore the modifier.
- **Leading indicator to monitor:** Three things to watch:
- GSC → Performance → Pages: CTR and impressions of the 13 suffix URLs and the ~39 product URLs against the baseline.
- GSC queries containing model names ('gravipack sherpa', 'gravipack oslo', 'business talk') that land on gravipack.com.
- Screaming Frog counts of titles over 60 characters and of duplicate titles.
- **To verify on-site:** Check on the live site:
- View-source <title> on the home page, three product pages (Compostelle 65 L, Oslo Rouge, Sherpa Kaki), one category (militaire) and one post (/cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/).
- In Yoast/Rank Math: the site name, the separator, and the title templates for products, product categories, posts, post categories, tags and attributes.
- The WordPress Site Title and Tagline.
- The wp_postmeta query for hard-coded taglines.
- Whether the listed typos are still live.
- Whether the theme or a second SEO plugin outputs its own <title>.

### 12. B2B and occupational (TMS/QVT) demand has no indexable hub; the offers sit inside product pages and service 'products'

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | On-Page SEO |

**Issue.** Three site-restricted searches in the search results we sampled found no /entreprises/, /professionnels/, CSE, QVT, collectivités, pompiers/secours or prévention-TMS page on gravipack.com. Here is what exists instead.

Quote pages
- /devis/: titled 'Devis - Le sac à dos exosquelette GRAVIPACK anti mal au dos'. B2B team, reply within 24 h, free mock-up; the form asks for the company name and SIRET.
- /devis-gravipack/: titled 'Demandez votre devis Gravipack…', with custom solutions per industry.
- That these two pages serve the same intent is inferred from their titles only.

B2B services published as WooCommerce products
- /produit/fabrication-professionnelle-gravipack/, titled 'fabrication professionnelle, cadeaux d'entreprise et objets publicitaires haut de gamme.' (88 characters, starting in lowercase).
- A key ring carrying the SNCF logo: /produit/porte-cle-flamme-personnalise-avec-logo-sncf-broderie-premium-gravipack/.
- A payment-link product, /produit/lien-de-paiement-unique-pour-votre-commande-personnalisee-gravipack/, which surfaced for CGV and refund queries.
- The waist-belt buckle is a real spare part and is fine as a product.

B2B selling points that exist only inside product sheets
- 'adopté par plus de 120 clients B2B et B2G'
- 'déployé dans entreprises et administrations pour prévenir les TMS et améliorer la QVT'
- prescription by doctors or the médecin du travail
- funding via AGEFIPH / FIPHFP / MDPH / Escavie (ExoTool and others)
- 'tarifs dégressifs pour entreprises & administrations' (Austerlitz)
- prices for collectivités (Centurion)
- SAMU and military doctors
- The home page lists the Armée de Terre, the Légion étrangère, the Préfecture de police, the gendarmerie, fire services and regional councils as users (self-reported).

B2B proof written as news, not as landing pages
- /le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/, the VivaTech/Le Parisien post, /gravipack-soulage-les-forces-speciales-au-sofins/ (plus a /test/ copy) and the Techterre post.
- RATP Group's own pages name Gravipack. Its CSR page describes an exoskeleton backpack for staff who inspect tracks on foot, and its VivaTech 2023 pages say about 50 roaming maintenance workers were equipped. An owned post says 250 agents, so the figure must be reconciled before it is reused.

Facts that conflict
- The custom-logo key ring shows a minimum order of 20 units on one sheet and 30 on the other.
- Capacity is '20 à 100 litres' on the Techterre post and '20 à 60 litres' on the SOFINS post. These may describe different product families (one post presents the Barracuda claie), so verify.
- The AGEFIPH/FIPHFP wording is imprecise rather than fabricated: both bodies fund workplace-adaptation equipment for workers with a recognised disability, case by case.

Occupational search results
- Generic TMS queries ('sac à dos TMS travail', 'exosquelette passif prévention TMS') return only institutional sources: INRS, OSHA, DREETS, CRAMIF, FFB, INSPQ. A brand page will rarely rank there, so a vendor guide is an opportunity, not a defect.
- A zero result for a query combining 'Gravipack' with TMS terms is an artefact of the search tool, since the product pages do contain that wording.
- OPPBTP's preventionbtp.fr 'solutions' sheet ranks #7 for 'sac à dos porte-outils', near the Gravipack outillage hub at #9.

B2B search demand has not been quantified (no volume data), hence Medium.

**Evidence.** <https://gravipack.com/devis/> · <https://gravipack.com/devis-gravipack/> · <https://gravipack.com/produit/fabrication-professionnelle-gravipack/> · <https://gravipack.com/produit/porte-cle-flamme-personnalise-avec-logo-sncf-broderie-premium-gravipack/> · <https://www.gravipack.com/produit/porte-cle-flamme-personnalise-sur-mesure-avec-votre-logo-broderie-premium-gravipack/> · <https://www.gravipack.com/produit/lien-de-paiement-unique-pour-votre-commande-personnalisee-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-porte-outils-exotool-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/> · <https://gravipack.com/le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/> · <https://gravipack.com/gravipack-au-salon-vivatech-cet-outil-de-pointe-au-service-des-voyageurs-et-des-agents-du-metro-le-parisien/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · *(+6 more in findings/)*

**Why it matters.** B2B buyers (HSE managers, médecins du travail, CSE members, buyers in collectivités, maintenance managers) search for a job to be done: équiper des agents terrain, prévenir les TMS liés au port de charge, cadeaux CSE personnalisés, achats publics. They expect a page that presents the offer, the proof, the process and a way to request a quote.

Today that information is scattered across consumer product sheets, news posts and 'products' that are really services. As a result, no URL can rank for those queries, collect B2B links (RATP, OPPBTP, trade media) or convert visitors through a clear path.

The claims that would be reused for B2B (TMS prevention, prescription, funding) are YMYL-adjacent. They must be accurate before they are concentrated on a hub.

**Effect on SEO.** A hub-and-spoke /entreprises/ section would:
- create indexable landing pages for B2B intent;
- consolidate the quote-page signals onto one URL;
- give PR and case studies a link target;
- remove thin service and payment 'products' from the product index and the Merchant Center feed.

Consistent, sourced facts on one page also give buyers and AI answers a single version to cite.

**How to fix.**

1. Verify before publishing anything. This is a gate:
   - the '120 clients B2B/B2G' figure;
   - named clients and institutions, with written permission to cite them (this includes the SNCF logo on the key-ring product);
   - the prescription wording and the funding wording;
   - the RATP numbers (the owned '250 agents' vs RATP's ~50 at VivaTech 2023).
   Remove or reword anything that cannot be documented.
2. Build /entreprises/ as a parent WordPress page, with spokes only where there is a real offer and proof. Start with the hub and two spokes, then add more:
   - /entreprises/maintenance-outillage/ (ToolMaster, Light Promax, ExoTool; the RATP case)
   - /entreprises/sacs-personnalises/ (the 'fabrication professionnelle' offer, CSE gifts and logo key rings, with MOQ, lead times, mock-up and quote)
   - later: /entreprises/secours-sante/, /entreprises/defense-securite/, /entreprises/collectivites/ (Centurion, the public-procurement process) and a prévention-TMS guide.
   Suggested titles: 'Sacs à dos à exosquelette pour les entreprises | Gravipack' (58) and 'Sacs à dos personnalisés pour entreprises | Gravipack' (53). H1 example: « Équiper vos équipes terrain de sacs à dos à exosquelette ».
   Content for the hub and spokes:
   - use cases;
   - proof: case studies with numbers and the client's permission;
   - the process: prêt d'essai, devis, déploiement, formation au réglage;
   - the pricing model ('tarifs dégressifs à partir de [X] unités');
   - a downloadable spec sheet and the quote form.
3. Funding wording: reword it and add sources; do not delete it. Suggested wording: « Selon votre situation, l'équipement peut être éligible à une aide de l'AGEFIPH (secteur privé) ou du FIPHFP (fonction publique) dans le cadre d'un aménagement de poste pour un salarié reconnu travailleur handicapé, après étude du dossier par l'organisme. » Link to each agency's aid page, and use the same wording on the product sheets.
4. Keep one quote URL.
   - Compare the two forms and keep one (/devis/ or /entreprises/devis/).
   - 301 the other, with the Redirection plugin or in .htaccess: RewriteRule ^devis-gravipack/?$ https://gravipack.com/devis/ [R=301,L]
   - Update menus and CTAs.
   - Track submissions as a GA4 key event (generate_lead).
5. Take the services out of the product catalogue.
   - Rebuild 'fabrication professionnelle' as the /entreprises/sacs-personnalises/ page, and 301 /produit/fabrication-professionnelle-gravipack/ to it.
   - Payment-link product: set Catalogue visibility to 'Caché' (Publish box) and set it to noindex. In Yoast: Advanced → 'Allow search engines to show this Product in search results?' = No. In Rank Math: Advanced → Robots Meta → No Index. This also removes it from the plugin sitemap. Exclude it from the Merchant Center feed.
   - SNCF key ring: if it is client-specific, hide and noindex it, or 301 it to the personalisation page. Keep one generic custom-logo key ring with a single MOQ.
6. Structured data.
   - BreadcrumbList on the hub and the spokes.
   - Service on the personalisation spoke. This is entity markup only; it produces no rich result.
   {"@context":"https://schema.org","@type":"Service","name":"Sacs à dos à exosquelette personnalisés pour entreprises","serviceType":"Personnalisation de sacs à dos et accessoires (logo, couleurs)","provider":{"@id":"https://gravipack.com/#organization"},"areaServed":{"@type":"Country","name":"France"},"audience":{"@type":"BusinessAudience","audienceType":"Entreprises, CSE, collectivités"},"url":"https://gravipack.com/entreprises/sacs-personnalises/"}
   - Use the canonical host chosen in the host fix, and make the @id match the Organization node that the SEO plugin outputs.
7. Internal links.
   - Add 'Entreprises' to the main menu and the footer.
   - Add a block « Équiper vos équipes ? Demandez un devis » on the outillage, médical, militaire and claie categories.
   - Link the RATP, VivaTech and SOFINS posts to the matching spoke.
8. Prévention-TMS guide (/entreprises/prevention-tms-port-de-charge/).
   - Follow the INRS framing: collective prevention comes first and the backpack is a complement; cover risk assessment, field trial, training and limits.
   - Use the RATP deployment as the real case.
   - Have an ergonomist or a médecin du travail review the guide, and name the reviewer.
   - Avoid 'anti-douleur' and other medical claims.
   Expect little ranking against INRS and OSHA; the value lies in sales enablement, links and AI citations. FAQ content on these pages serves readers only; there is no FAQ rich result.
9. OPPBTP: submit a documented field case, with the client's agreement, to the preventionbtp.fr 'Solutions' database. That database publishes company field cases, so this works better than pitching vendor guides.
10. Fix the conflicting facts: one MOQ per product, and one capacity range per model family once the Techterre and SOFINS context has been checked.

- **First principle:** B2B buyers search for the problem and the buying process, not for a product name, and a query can only be answered by a page that exists for it. When the offer, the proof and the process are scattered across consumer product sheets and service 'products', there is no URL to rank, to link to, or to convert on.
- **Do first:** [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), [#22 RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links](#22-ratps-own-pages-document-its-use-of-gravipack-but-this-has-not-been-turned-into-a-case-study-or-links), `host-canonicalisation`
- **How we'll know the fix failed:** Three months after launch, any of these is true:
- The hub and spokes are indexed (URL Inspection) but get fewer than about 50 impressions a month in GSC for non-brand B2B queries.
- Organic quote submissions (the GA4 key event) have not risen from the baseline.
- The old service-product URLs are still indexed.
- **Leading indicator to monitor:** Three things to watch:
- GSC impressions on /entreprises/ URLs for queries containing 'entreprise', 'professionnel', 'personnalisé', 'devis', 'collectivité' or 'TMS'.
- GA4 generate_lead key events from organic sessions that land on /entreprises/.
- New referring domains to the hub (RATP, OPPBTP, trade media).
- **To verify on-site:** Check on the live site:
- A crawl and a sitemap check for any existing B2B page.
- /devis/ vs /devis-gravipack/: content, form and CTA links.
- The catalogue visibility and robots status of the payment-link, 'fabrication professionnelle' and SNCF key-ring products, and whether they are in the Merchant Center feed.
- The MOQ on both key-ring sheets.
- The capacity context on the Techterre and SOFINS posts.
- Documents supporting the '120 clients', prescription and funding wording.

### 44. Product slugs are very long and keyword-stuffed, and some contain typos or '-copie' leftovers

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **2** | Low | confirmed | On-Page SEO |

**Issue.** Confirmed from the URLs themselves, as they were indexed in the search results we sampled.

Length
- 30 of 39 product URLs exceed 100 characters (median 110).
- Longest: City, 205 characters: /produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/ ('anti-mal-de-dos' twice, plus a superlative).
- Compostelle 80 L, 196 characters: /produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/.
- Hiking Terracotta: 161 characters (…revolutionnaire…).
- Category slugs run 90-151 characters (the randonnée hub is 151).

Repetition
- 37 slugs contain 'anti-mal-de-dos'.
- Sherpa orange repeats a word: '…-sherpa-45l-orange-anti-mal-de-dos-orange-…'.

Typos
- 'sac-randonner-leger' (Easy Travel, Helsinki).
- 'oganizer' (/produit/porte-outils-elastique-amovible-velcro-oganizer-gravipack/).
- 'hikking33' (presta).
- 'assault' (militaire category slug).
- The post /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/, whose title is 'Un sac à dos pas comme les autres… les épaules de vos enfants vont adorer'. The title was edited after the slug was generated.

Leftovers from duplicated products
- '-copie' on Compostelle 65 L (…memoire-de-forme-copie/) and on the solar battery (…boussole-infinity-gravipack-copie/).

Claim words in URLs
- 'pas-cher' and 'revolutionnaire' (Compostelle 80 L).
- 'certainement-le-meilleur-sac-au-monde' (City).
- 'la-seule-au-monde' (Tokyo: /produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/). This slug also lacks the model name.
- Light Promax ('…outillage-parcours-gravipack/') also lacks the model name.
- A news index sits at /actualites-gravipack-2/.

Needs a live check (seen in snippets only)
- /sac-a-dos-hiking-30l-gris-…/ is used for a bag described as 33 L.
- /fourreau-de-portage-exosquelette-gravitech-…/ is used for a product titled 'Claie de portage…' and named Barracuda.

Why Low: words in the URL are a minor ranking signal, and every slug change needs a 301, so a mass rename would cost more than it brings. Tokyo, for example, already ranks for two of the queries we tested despite its slug.

**Evidence.** <https://www.gravipack.com/produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/> · <https://www.gravipack.com/produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-de-survie-65-litres-ergonomique-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme-copie/> · <https://www.gravipack.com/produit/batterie-solaire-externe-multi-port-avec-lampe-torche-et-boussole-infinity-gravipack-copie/> · <https://gravipack.com/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/> · <https://www.gravipack.com/produit/porte-outils-elastique-amovible-velcro-oganizer-gravipack/> · <https://gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-easy-travel-gravipack/> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://gravipack.com/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/> · <https://gravipack.com/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/> · *(+1 more in findings/)*

**Why it matters.** Short, descriptive slugs are easier to read, share and cite. Very long slugs get cut off in breadcrumb and URL displays and in shared links, and the repeated 'anti-mal-de-dos' adds to the site-wide keyword repetition.

Superlatives in the URL ('le meilleur sac au monde', 'la seule au monde') put unsubstantiated claims in a field that is copied everywhere and cannot be edited later without a redirect.

'-copie' slugs show products that were duplicated in the back office and may still be live as duplicates.

**Effect on SEO.** The direct effect on relevance and CTR is small. The real risk lies in the fix: renaming indexed URLs without exact 301s causes 404s and loses link equity, and stacking renames on top of the presta redirects creates redirect chains.

If slugs are changed only where a merge or a claim fix is needed anyway, the result is cleaner URLs and fewer claim words in the address bar, with negligible risk.

**How to fix.**

1. No mass rename. Add slug changes to the single URL migration map shared with the duplicate-product, presta-redirect, host and category fixes, and ship them in one release. The map is a spreadsheet with these columns: old URL → new URL → reason → has backlinks? → date.
2. Change a slug only in one of these cases:
   a. Two URLs are being merged. This includes the '-copie' products: check whether the '-copie' Compostelle 65 L and battery duplicate an original product, and if so keep one product and 301 the other.
   b. The slug contains a typo.
   c. The slug contains a claim that the claims review removes: City 'certainement-le-meilleur-sac-au-monde', Tokyo 'la-seule-au-monde', Compostelle 80 L 'pas-cher' / 'revolutionnaire'. Accept a few weeks of fluctuation on City and Tokyo if the claims review requires the change.
3. Pattern for new and changed slugs: /produit/<modele>-<contenance>[-<couleur>]/, about 5 words at most, no 'anti-mal-de-dos', no superlatives. Examples: /produit/sherpa-45l-orange/, /produit/compostelle-80l/, /produit/compostelle-65l/, /produit/tokyo/, /produit/city/, /produit/porte-outils-elastique-organizer/, /produit/sac-randonnee-easy-travel/, /produit/helsinki-60-10l/. Set the slug by hand when creating a product (product edit screen → Permalien → Modifier).
4. Redirects. WordPress stores the old slug, and wp_old_slug_redirect() normally 301s renamed posts and products. Add explicit rules anyway as a safeguard, because they survive later edits.
   - Easiest: the Redirection plugin or Rank Math → Redirections (301, exact match).
   - Or in .htaccess, above the WordPress block:
     RewriteEngine On
     RewriteRule ^produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/?$ https://gravipack.com/produit/city/ [R=301,L]
   - Or in Nginx: location = /produit/<ancien-slug>/ { return 301 https://gravipack.com/produit/<nouveau-slug>/; }
   - Point every target at the canonical host chosen in the host-consolidation fix (apex or www).
5. No chains. Legacy presta URLs must redirect straight to the final URL (presta → new slug), never presta → old slug → new slug. Check with Screaming Frog (Reports → Redirects → Redirect Chains) or curl -sIL.
6. Update everything that links to the old URLs:
   - internal links in menus, category descriptions and posts (Better Search Replace on wp_posts.post_content, after a full backup);
   - the XML sitemap (Yoast and Rank Math regenerate it automatically);
   - the Merchant Center feed;
   - partner and press links: ask ergo-corner and the press to update links to renamed URLs.
7. Do not touch the slugs of URLs that rank or earn links unless the 301 is live at the same moment.
   - Leave the parent category slug 'tous-les-sacs-a-dos-exosquelette' unchanged. WooCommerce category URLs are hierarchical, so renaming the parent changes about 12 child URLs.
   - Leave the outillage category slug unchanged; it ranks.
8. Backlog only:
   - The 'autresvos' post slug: negligible gain. If it is touched, use /sac-a-dos-enfant-pas-comme-les-autres/ with a 301.
   - The 'assault' category slug: fix the title now, and change the slug only in the migration release.
9. Confirm the content mismatches on the live pages (Hiking '30l' vs 33 L; Gravitech/fourreau vs Barracuda/claie), and correct the product name and copy first. Change the slug only if the page is being merged or renamed anyway.

- **First principle:** A URL is an address first and a keyword carrier a distant second. Once a URL is indexed and linked, keeping it stable is worth more than the small relevance gain from a cleaner slug. So slug changes should ride on changes that are needed anyway: merges, typo fixes and claim removal.
- **Do first:** [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), `legacy-presta-redirects`, `host-canonicalisation`, [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation)
- **How we'll know the fix failed:** Any of these means the change went wrong:
- In the post-release crawl, an old URL returns 404 or takes more than one redirect hop.
- GSC Page indexing shows 'Not found (404)' rising.
- Renamed URLs have not recovered their baseline clicks 6-8 weeks after the change.
- **Leading indicator to monitor:** Screaming Frog: redirect chains = 0 and internal links to redirected URLs = 0. GSC Page indexing: the 'Not found (404)' and 'Page with redirect' counts. Clicks of renamed URLs against the baseline.
- **To verify on-site:** Check on the live site:
- curl -sIL on the City, Compostelle 80 L, Compostelle 65 L '-copie' and battery '-copie' URLs (status code and final URL).
- Whether each '-copie' product is a published duplicate of another product.
- The Hiking 30 L capacity and the Gravitech/Barracuda naming on the live pages.
- Existing Redirection or Rank Math rules and _wp_old_slug entries.
- Backlinks to the URLs to be renamed (GSC → Links).

### 45. Some snippets show mini-cart text ('0 items - 0,00 €'), so meta descriptions need checking (verify on-site)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| ⚪ **Info** | **2** | Low | needs-on-site-check | On-Page SEO |

**Issue.** A search summary recorded during the audit noted that snippets for gravipack.com product, legal and CGV results (e.g. Oslo Rouge, /mentions-legales/, /conditions-generales-de-vente/) often showed the empty mini-cart text '0 items - 0,00 €'. Presta pages showed similar cart-widget text. The snippet text itself was not saved, so the observation cannot be re-checked.

These snippets were produced by a non-Google engine. Google writes its own snippet from page content in most cases, even when a meta description exists, so cart text in a snippet does not prove that meta descriptions are missing. It does suggest that the mini-cart markup sits early in the page text, where any search engine or AI crawler may pick it up.

The meta description tags could not be inspected, because the site could not be fetched. Status: verify on-site.

**Evidence.** <https://gravipack.com/mentions-legales/> · <https://gravipack.com/conditions-generales-de-vente/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://presta.gravipack.com/accueil/15-sac-a-dos-gravipack-business-talk.html>

**Why it matters.** The snippet under the title is the second line of the 'ad' that every organic result shows. A page with a useful meta description gives the engine a better candidate than '0 items - 0,00 €', especially if boilerplate is also kept out of the snippet. The claude-seo gate is 120-160 characters, unique, and written for that page.

**Effect on SEO.** CTR only, and uncertain; there is no ranking effect. If descriptions are missing and boilerplate is being used, fixing both should improve snippet quality on product and category results. If descriptions already exist, the fix is limited to the mini-cart.

**How to fix.**

1. Check first.
   - View-source <meta name="description"> on the home page, three product pages and two categories.
   - Check the plugin templates. Yoast: Settings → Content types → Products / Categories & tags → Meta description. Rank Math: Titles & Meta → Products / Product categories → Description.
2. If descriptions are missing or generic, write unique ones (120-160 characters) for the home page, the hub, the 10 segment categories and the top 20 products by impressions.
   - Elsewhere, use the product short description as a fallback (Rank Math variable %wc_shortdesc%; Yoast %%excerpt%%).
   - Keep unverified facts in brackets and avoid health claims. Example (140 characters): « Sherpa 45 L : sac de randonnée Gravipack à exosquelette breveté qui répartit la charge sur le dos. Bretelles [M à XXL], livraison en France. »
3. Keep the mini-cart out of snippets.
   - Add data-nosnippet to its wrapper in the child-theme header, e.g. <div class="header-mini-cart" data-nosnippet>…</div>. Google honours data-nosnippet on div, span and section elements.
   - Make sure the cart widget is not the first text inside <main>.
4. Four weeks later, re-check the snippets on google.fr for 10 URLs. Google may still rewrite them, so judge by CTR rather than by exact wording.

- **First principle:** A search engine builds the snippet from the meta description, or from the page text it judges most relevant to the query. Boilerplate that appears early in the page text is a poor candidate, but it can still be chosen when nothing better is offered.
- **Do first:** [#11 Title tags are over-long, carry a bloated site-wide suffix and stacked claim keywords, and sometimes omit the model name or contain typos](#11-title-tags-are-over-long-carry-a-bloated-site-wide-suffix-and-stacked-claim-keywords-and-sometimes-omit-the-model-name-or-contain-typos)
- **How we'll know the fix failed:** Either google.fr snippets still show '0 items - 0,00 €' after the change (the cart text is inside the main content, or the page has not been re-crawled), or GSC CTR on the updated URLs does not move after 6-8 weeks at comparable positions.
- **Leading indicator to monitor:** GSC CTR by page for the top 20 products and for the categories, plus a monthly spot check of 10 snippets on google.fr.
- **To verify on-site:** Check on the live site:
- View-source <meta name="description"> on the home page, Oslo Rouge and two other product pages, the hub, one segment category, /mentions-legales/ and /conditions-generales-de-vente/.
- The Yoast/Rank Math description templates for products and categories.
- Where the mini-cart markup sits in the DOM, and whether it is inside <main>.
- Whether data-nosnippet is already used.

## Content Quality

**Score:** **30/100** *(partial)* — Strong first-hand inventor story and real awards, but YMYL health claims (-92 %, "anti-douleur", "remboursé par la Sécurité sociale", "dispositif médical") have no public primary evidence (study-92-evidence, health-claims-wording); informational guide coverage near zero (informational-guides-gap); no comparison, size-guide or authoritative founder bio pages.

**What works:**
- Genuine inventor-founder with a documented invention story (Concours Lépine silver 2018, INPI Trophées 2022 finalist)
- An FAQ and blog/press section already exist
- Real institutional use case (RATP, ~50 maintenance workers, VivaTech 2023)

### 1. The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟠 **High** | **8** | High | likely | Content Quality |

**Issue.** - No public primary document:
  - Press relays 'une étude de la faculté de médecine de Lyon réalisée en 2019' (Journal du Geek 2021, Maddyness 2024). The founder cites a 2019 study at the Lyon-Sud faculty of medicine (fnh.ma).
  - Targeted searches found no paper, report, protocol, sample size or author list.
  - A 2019 Lyon 1 physiotherapy thesis on bibnum.univ-lyon1.fr showed no visible link to Gravipack, and none should be assumed.
  - Forum users report finding nothing on PubMed, the EU trial registers or the lab's site.
- The only study page found is on the legacy subdomain: presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack ('L'étude scientifique du sac à dos en apesanteur Gravipack.'). It refers to the LBMC / Faculté de Médecine Lyon-Sud. None surfaced on the main domain in site: queries.
- The 92 % is described as a cut in weight, in load or in pressure, depending on the page:
  - /faq/: 'évacue jusqu'à 92 % de la charge';
  - school category title: 'allège le poids de 92%';
  - the post /inventeur-dun-sac-a-dos-en-apesanteur/, titled 'Le sac à dos en apesanteur anti-mal de dos allège le poids de 92%';
  - Decathlon titles: 'Allège la charge de 92%';
  - the KissKissBankBank campaign 'le sac à dos révolutionnaire qui allège la charge de 92';
  - INPI's profile: 'alléger de 92 % la charge sur les épaules';
  - a reseller: 'réduction de pression estimée à 92%';
  - Maddyness: '92% le poids … ressenti sur les épaules'.
  A bag cannot reduce the weight of its load, so 'allège le poids de 92 %' is easy to challenge.
- Doubts rank on brand searches, unanswered. In the results we sampled (a US-located, non-Google index; brand positions are volatile):
  - 'gravipack étude Lyon' returned 6 randonner-leger threads, a moodle univ-lyon1 page, Maddyness and Europe 1, and no gravipack.com page;
  - 'gravipack arnaque efficace 92%' returned 8 randonner-leger threads plus KissKissBankBank, and no owned URL;
  - randonner-leger threads also appeared for 'gravipack avis' and 'gravipack arnaque'.
- Reported neutrally:
  - Those threads contain unverified third-party statements: that the work was a preliminary pre-study by a master's intern from which no conclusion about Gravipack can be drawn, and that the lab would not share it without a formal request.
  - One earlier search summary paraphrased a post as saying the lab asked that the study not be used for promotion. That is an unverified allegation.
  - A forum member estimates the effect at about 30 % (subjective) and argues the load moves to the lower back. An Australian bushwalk.com thread is also sceptical.
  - The SEO issue is that these pages rank unanswered, not whether they are true.
- The official YouTube channel description still presents a 2019 'scientific and medical study'.
- Same-name lab: an LBMC at ENS Lyon (cell biology) also appears in results. The biomechanics LBMC is a joint unit of Université Gustave Eiffel and Université Claude Bernard Lyon 1. The evidence page must name the unit precisely.
- No third-party source shows a named independent health professional backing the claims. That is absence only; whether site pages show a reviewer is unverified.
- Related signals exist:
  - RATP's own pages name the exoskeleton backpack developed by Gravipack (about 50 roaming maintenance agents equipped as of VivaTech 2023);
  - a possible Lyon 1 link;
  - finalist in the 2022 Trophées INPI;
  - silver medal at the 2018 Concours Lépine.
- Third-party sources frequently question the figure.

**Evidence.** <https://presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack> · <https://www.gravipack.com/faq/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://gravipack.com/inventeur-dun-sac-a-dos-en-apesanteur/> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.kisskissbankbank.com/en/projects/le-sac-a-dos-revolutionnaire-qui-allege-la-charge-de-92> · <https://www.inpi.fr/trophees/gravipack-les-bretelles-qui-allegent-le-poids-sur-les-epaules-et-le-dos> · <https://vauguillettes.fr/gravipack/> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://www.randonner-leger.org/forum/viewtopic.php?id=37663&p=2> · *(+9 more in findings/)*

**Why it matters.** The 92 % is the brand's headline promise on its own pages and on partner listings, in a topic close to health (YMYL). Without a public method, raters, journalists, ergonomists and answer engines have nothing to check. The most visible 'evidence' then becomes sceptical forum threads on brand queries.

Under French consumer law, a quantified claim must be substantiable at the time it is made (L121-1/L121-2 C. conso). A protocol stating what was measured is the only way to keep the figure. Read literally, 'allège le poids' is the easiest version to disprove.

**Effect on SEO.** An indexed evidence page on the main domain becomes:
- the link target for press, ergonomists and resellers;
- the page that can rank for 'gravipack étude', 'gravipack 92 %' and 'gravipack avis';
- the passage answer engines quote.
The 301 from presta consolidates the legacy page's signals. One precisely worded claim removes the inconsistency that sceptics use.

**How to fix.**

1. Go back to the source.
   - Retrieve the 2019 document.
   - Ask the biomechanics LBMC (Université Gustave Eiffel / Lyon 1) for written permission to name it and to publish it or a summary.
   - Establish exactly what was measured (for example, peak pressure under the strap at the trapezius), on how many subjects, with what load and in what conditions.
2. Decide:
   - If it can be published, create the evidence page on the canonical host, e.g. /etude-biomecanique-gravipack/ (a WordPress Page).
   - If not, stop using the figure, or limit it to what can be shown, and commission a new test (step 7).
3. Evidence page content:
   - H1: « Étude biomécanique Gravipack : ce que mesure le chiffre de 92 % ».
   - Answer-first paragraph, filled in only from the document: « Le sac ne devient pas plus léger : la charge totale reste la même. Le chiffre de 92 % correspond à [la baisse de la pression mesurée sous les bretelles, au niveau des trapèzes], mesurée en [2019] par [unité, laboratoire] sur [n] participants portant [x] kg [à l'arrêt / en marche]. Il s'agit d'une étude [exploratoire], non publiée dans une revue à comité de lecture. »
   - A methodology table: laboratory and unit, authors and roles, date, sample size, load, protocol, sensors, measured variable, result with spread, limitations, funding and conflicts of interest. Add the PDF if permitted.
   - A section « Ce que l'étude ne montre pas » (no clinical outcome on back pain).
   - A 'Statut réglementaire' paragraph, based on the route chosen in health-claims-wording.
   - A 'Relu par [Nom, titre]' box, disclosing any payment, and 'Mis à jour le'.
4. Migrate and redirect the legacy page.
   - Review the presta page and move any useful content.
   - Then 301 it to the new URL as part of the presta migration map, never to the home page. On the presta vhost:
```
RewriteEngine On
RewriteCond %{HTTP_HOST} ^presta\.gravipack\.com$ [NC]
RewriteRule ^40-etude-scientifique-soulage-le-dos-gravipack/?$ https://[hote-canonique]/etude-biomecanique-gravipack/ [R=301,L]
```
5. Use one harmonised claim, and only if the study measured strap pressure:
   - Claim: « Jusqu'à 92 % de pression en moins mesurée sous les bretelles* ».
   - Footnote: « *Étude [laboratoire], [année], [n] sujets, charge de [x] kg, [conditions] — voir l'étude. La charge totale n'est pas réduite : elle est répartie différemment. »
   - Titles cannot carry a footnote, so take 92 % out of titles (school category, /inventeur-dun-sac-a-dos-en-apesanteur/) and keep it in body copy with the footnote.
   - Store the footnote as a WordPress synced pattern so every page uses the same text.
   - Rewrite the FAQ answer, e.g.: « Non, le sac ne devient pas plus léger. L'exosquelette répartit la charge différemment : lors d'un test en laboratoire, la pression mesurée sous les bretelles a baissé jusqu'à 92 % (voir l'étude). »
6. Align the other surfaces:
   - Decathlon (Kid'abord's listings and the brand's own seller account), Nature & Découvertes, Fnac, Kiabi, Au Vieux Campeur, Ergo-Corner and the other reseller pages;
   - INPI's Trophées profile (request an update);
   - news updates on the 4 KissKissBankBank campaigns;
   - the YouTube channel description: remove 'scientific and medical study' until the document is public.
7. Commission an independent test from a biomechanics or sports-science (STAPS) lab, with a pre-registered protocol: pressure mapping at the shoulders and lumbar load, n ≥ 20, against a conventional bag with a hip belt. Publish the result whatever it shows.
8. Name a reviewer. A masseur-kinésithérapeute DE or an ergonomist reviews the evidence page and the guides as a disclosed reviewer, not as a product endorser (CSP R.4127-20; the Transparence Santé rules apply if the medical-device route is taken).
9. Respond once on the brand results. When the page is live, post one disclosed reply as the brand in the randonner-leger and bushwalk threads, stating what was measured and linking to the page. Do not argue about the allegations.
10. Add markup as entity context only; it earns no rich result. Add Dataset markup only if real data can be downloaded.
```json
{"@context":"https://schema.org","@type":"WebPage","@id":"https://[hote-canonique]/etude-biomecanique-gravipack/#webpage","name":"Étude biomécanique Gravipack : ce que mesure le chiffre de 92 %","lastReviewed":"[AAAA-MM-JJ]","reviewedBy":{"@type":"Person","name":"[Nom]","jobTitle":"[Ergonome]"},"citation":{"@type":"Report","name":"[Titre du rapport]","author":{"@type":"Organization","name":"[Unité, laboratoire]"},"datePublished":"2019"}}
```
11. Link the page from /faq/, the home page, the school category, every product page (« Ce que mesure le chiffre de 92 % ») and the about page. Send it to Journal du Geek, Maddyness, Europe 1 and INPI as the source to cite.

- **First principle:** A quantified, health-adjacent claim is only as strong as the public document behind it. When the brand does not publish the method, the only indexed evidence is the sceptics' threads, and they become the answer to every brand-plus-proof query.
- **Do first:** [#16 The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages](#16-the-legacy-prestashop-store-prestagravipackcom-still-appears-in-search-results-with-old-product-study-and-award-pages), `host-canonical-split`
- **How we'll know the fix failed:** - If the lab declines and no replication is commissioned within 3 months, the fix becomes dropping the figure. Keeping it in that case means this finding has failed.
- After launch, the page is not doing its job if:
  - it is not indexed within 4 weeks;
  - 3 months later it does not appear for 'gravipack étude' or 'gravipack 92' on Google.fr;
  - new press and forum posts still say no study has been published.
- **Leading indicator to monitor:** - Search Console impressions and clicks on the evidence URL for 'gravipack étude', 'gravipack 92', 'gravipack avis' and 'gravipack arnaque'.
- Referring domains to the evidence page.
- Number of owned and partner surfaces still using a bare '92 %'.
- **To verify on-site:** - Read the presta study page: what it says about the lab, authors, protocol and sample.
- Check whether /faq/ or a product tab already summarises or links to the study.
- Search WordPress for every mention of '92'.
- Confirm whether the presta host still returns 200, and how its redirects are planned.
- Read the current YouTube channel description.
- Check whether any page shows a named health reviewer.

### 4. Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **7** | Medium | likely | Content Quality |

**Issue.** The evidence is page titles and URL slugs as shown in the search results we sampled. Current page text could not be fetched.
- 'Anti-douleur':
  - The Sherpa Kaki title 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur' appears on 3 URLs: /produit/sac-a-dos-sherpa-kaki-avec-exosquelette-…, /produit-gravipack/sac-a-dos-sherpa-kaki and /produit-gravipack/sac-a-dos-sherpa.
  - The Light Promax title 'Sac à dos outillage anti-douleur exosquelette Gravipack®' appears on 2 URLs, one with the slug /produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/.
- 'Anti-TMS': the randonnée category ('Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS') and 'Claie de portage Gravipack anti-TMS pour charges très lourdes'.
- '92 %' in titles: the school category ('Sac à dos exosquelette scolaire Gravipack allège le poids de 92%'), and Decathlon partner titles ending '… Allège la charge de 92%' on the Hiking 33, Sherpa 45, Pearl and Feather listings. The study behind the figure is covered in study-92-evidence.
- Superlatives:
  - Tokyo slug '…la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos';
  - City slug 'anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-…';
  - G-Pack 'révolutionnaire et unique';
  - presta titles 'Le seul sac à dos au monde qui allège le poids Hiking 33', 'Le meilleur sac à dos de montagne' and '…le meilleur sac a dos au monde';
  - 'révolutionnaire' in 10 recorded titles.
  These fall under the French rules on misleading advertising (Code de la consommation L121-1/L121-2), not under medical-device rules. A search snippet for one product page also showed 'recommandé par kinés, ergonomes et médecins du travail' (verify on-site).
- 'Dispositif médical (préventif)':
  - Used by the press: Journal du Geek 2021 ('qualifié de dispositif médical de prévention contre le mal de dos') and Maddyness 2024 ('reconnu dispositif médical préventif contre les troubles musculosquelettiques et correcteur de posture').
  - Used by company representatives: the founder in a fnh.ma interview, and a co-director of a licensee on France Bleu ('avant tout un dispositif médical').
  - A site: search found no owned page using it.
  - Three searches found no CE marking, EU declaration of conformity, EUDAMED or ANSM record. EUDAMED is not indexed by web search, so this is weak evidence either way.
- Reimbursement:
  - The only source is one undated founder interview on challenge.ma, a Moroccan outlet (about 2022-23): 'le premier sac à dos bénéficiant d'un remboursement par la sécurité sociale en hexagone'.
  - The same article says the occupational doctor (médecin du travail) may prescribe the bag and the cost is 'pris en charge par l'employeur'. That is employer funding, so the article contradicts its own claim.
  - No LPP or ameli listing was found. A lespepitestech review says the bag 'devrait être remboursé' (should be reimbursed). The claim was not found on gravipack.com.
  - challenge.ma is the only Gravipack result for 'sac à dos remboursé sécurité sociale mal de dos', and no Gravipack page answers the question.
- Children's line: health wording reaches parents through the school category title above, the G-Pack collège/lycée product, the Kingston bag promoted as 'Vive la rentrée scolaire', Decathlon's Feather titles ('Allège la charge de 92%') and the presta Feather page ('Sac à dos scolaire Feather Gravipack contre le mal de dos').
- Not a claim issue: 'Sac à dos médical Gravipack allégez vos missions sauvez des vies' describes a bag for first responders and their work. It is not a therapeutic claim.
- Ranking trade-off: in the extended sample, gravipack.com ranks for the 'anti mal de dos' head terms:
  - 'sac à dos anti mal de dos' #4-#6;
  - 'sac à dos ergonomique mal de dos' #2;
  - 'sac à dos scolaire anti mal de dos' #1-#3, with the school category at #2;
  - 'sac à dos randonnée anti mal de dos', with the randonnée category at #5.
  'Anti mal de dos' is the brand's main demand term, so removing it everywhere without testing has a cost.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa-kaki> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/claie-de-portage/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/> · <https://gravipack.com/produit/sac-a-dos-college-lycee-anti-mal-de-dos-avec-exosquelette-g-pack-gravipack/> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html> · *(+8 more in findings/)*

**Why it matters.** - Back pain, musculoskeletal disorders and children's backs are close to YMYL ('Your Money or Your Life') topics. Google's rater guidelines put Trust first there and discount unsupported health claims.
- Under the EU Medical Device Regulation (MDR 2017/745, Art. 2(1)), a product's intended purpose is read from its labelling, advertising and promotional material. Wording such as 'anti-douleur', 'anti-TMS' or 'dispositif médical préventif' can bring a backpack into medical-device scope. That means conformity assessment, CE marking and regulated advertising (CSP L5213-1 and following).
- Unqualified superlatives and a reimbursement claim contradicted by its own source risk being treated as misleading commercial practices (L121-1/L121-2 C. conso).
- If Gravipack uses Google Merchant Center (account status unknown), the relevant policy is Misrepresentation. The risk stays hypothetical until the account is checked.

**Effect on SEO.** - Titles and slugs are the most visible and most quoted text in search results and AI answers.
- Claims in them feed the sceptical 'arnaque / étude / 92 %' results, lower how health-adjacent pages are judged, and make answer engines less willing to repeat brand statements.
- Concrete, checkable wording (use, volume, weight, patent number) usually reads as more credible in a result.
- Rated Medium, not High: the evidence is search-result titles only and the fix is a wording change. The underlying evidence problem is handled in study-92-evidence.

**How to fix.**

1. Build a claims register (Google Sheet) with these columns: Claim | Exact wording | Where (URL; title, H1, slug, meta, alt, body, feed, partner, YouTube, press kit) | Evidence | Decision (keep / qualify / remove) | Owner | Review date.
   Pull every occurrence from WordPress with WP-CLI (adjust the table prefix):
```
wp db query "SELECT ID, post_type, post_name, post_title FROM wp_posts WHERE post_status='publish' AND CONCAT_WS(' ', post_title, post_name, post_excerpt, post_content) REGEXP 'anti[- ]?douleur|anti[- ]?tms|92 ?%|seule? au monde|meilleur sac|unique|dispositif m|rembours|prescrit|recommand'"
wp db query "SELECT post_id, meta_key, meta_value FROM wp_postmeta WHERE meta_key IN ('_yoast_wpseo_title','_yoast_wpseo_metadesc','rank_math_title','rank_math_description','_wp_attachment_image_alt') AND meta_value REGEXP 'anti[- ]?douleur|anti[- ]?tms|92 ?%|seule? au monde|meilleur sac'"
wp term list product_cat --fields=term_id,name,slug,description
```
   Also include non-health figures seen in snippets, such as '500 000 clients satisfaits'.
2. Choose the regulatory route with a regulatory consultant and counsel, and brief every spokesperson (founder, licensees, agency).
   a. Medical device:
      - identify the legal manufacturer (brand owner or licensee);
      - build the technical documentation and clinical evaluation;
      - sign the EU declaration of conformity (class I non-sterile, non-measuring devices are self-declared);
      - register in EUDAMED (SRN, UDI-DI) and affix CE;
      - then state the intended purpose on product pages.
   b. Consumer product (faster):
      - remove 'dispositif médical', 'correcteur de posture', 'anti-TMS' and 'anti-douleur' everywhere;
      - add to the evidence page and the FAQ: « Gravipack est un sac à dos ergonomique. Ce n'est pas un dispositif médical et il ne remplace pas un avis médical. »;
      - ask Journal du Geek and Maddyness to update their sentences.
3. In week 1, remove treatment and absolute wording. Examples (check specs before publishing):
   - Sherpa Kaki: « Sac de montagne Sherpa 45 L kaki à exosquelette | Gravipack »
   - Light Promax: « Sac à dos porte-outils Light Promax à exosquelette | Gravipack »
   - Claie: « Claie de portage à exosquelette pour charges lourdes | Gravipack »
   - Randonnée category: keep the ranking phrase and drop 'anti-TMS'. Use « Sac de randonnée anti mal de dos à exosquelette | Gravipack » if counsel accepts the phrase, otherwise « Sac de randonnée à exosquelette : charge mieux répartie | Gravipack ».
   - School category: « Sac à dos scolaire à exosquelette, collège et lycée | Gravipack ». The 92 % moves to body copy with a footnote, or is dropped.
   - City: « Sac à dos ordinateur City à exosquelette | Gravipack »
   - Professional products: « pensé pour les professionnels qui portent des charges au quotidien » instead of 'anti-TMS'.
   - Superlatives: replace them with checkable facts, each linked to its source, such as « Médaille d'argent au Concours Lépine 2018 » or « Finaliste des Trophées INPI 2022 ». Use « technologie brevetée (brevet n° …) » once the numbers are confirmed (see patents-trademark).
4. Decide on 'anti mal de dos' separately, with counsel.
   - If it stays, use it only as a descriptive modifier, with a qualifier in the body: « conçu pour mieux répartir la charge et soulager les épaules ; ne remplace pas un avis médical ». Or use an H2 such as « Sac à dos et mal de dos : ce que fait (et ne fait pas) l'exosquelette ».
   - Test any title change on about 5 URLs for 4 weeks in Search Console before rolling it out.
5. Change only the misleading slugs (porte-outil-anti-douleur, la-seule-au-monde, certainement-le-meilleur-sac-au-monde).
   - Do it inside the single URL migration map, together with the presta and /produit-gravipack/ consolidation, so you do not create redirect chains.
   - Use Rank Math > Redirections, Yoast Premium's automatic redirect, or .htaccess above # BEGIN WordPress:
```
RewriteRule ^produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/?$ https://[hote-canonique]/produit/sac-a-dos-porte-outils-light-promax-exosquelette/ [R=301,L]
```
   - Keep the 301s permanently, and update internal links and the sitemap.
6. Reimbursement:
   - Never repeat 'remboursé par la Sécurité sociale'.
   - If employer funding is real and documented, publish /prise-en-charge-employeur/ with: « Sur proposition du médecin du travail (mesures individuelles d'aménagement du poste, art. L4624-3 du Code du travail), l'employeur peut financer un sac Gravipack ; les mesures de santé et de sécurité ne doivent entraîner aucune charge financière pour le salarié (art. L4122-2). Gravipack fournit devis, fiche technique et attestation. Gravipack n'est pas inscrit sur la LPP et n'est pas remboursé par l'Assurance Maladie. »
   - Have counsel check the reading of Cass. soc. 5 juillet 2017 n° 15-29.424 before citing it.
   - Ask challenge.ma for a correction.
   - A FAQ answer « Le sac Gravipack est-il remboursé ? » helps users and answer engines. FAQPage markup brings no rich result.
7. Children's pages:
   - Have a paediatric physiotherapist review the school category, G-Pack, Kingston and Feather pages, with a dated 'Relu par' box.
   - Replace absolute promises such as « protège le dos de votre enfant » with « aide à mieux répartir le poids du cartable ».
   - Health professionals act as reviewers of educational content, not as product endorsers (CSP R.4127-20 for doctors; kiné ethics rules are similar).
8. Push the same wording to every channel:
   - the product feed (the feed-plugin API migration is covered in the Merchant Center finding);
   - Decathlon: both the brand's own seller account and Kid'abord, a separate company acting as licensee and marketplace seller;
   - Nature & Découvertes, Fnac, Kiabi, Au Vieux Campeur, Ergo-Corner and Équilibre France Ergonomie;
   - gravipack.ma;
   - the 4 KissKissBankBank campaign pages, as a creator news update;
   - YouTube descriptions, LinkedIn and the press kit.
9. If a Merchant Center account exists, check Diagnostics for Misrepresentation flags after the feed update. Request re-crawling of the main changed URLs through URL Inspection, and save a before/after title baseline.

- **First principle:** In YMYL-adjacent commerce, a claim is an asset only if it can be substantiated. Titles and slugs are the text most often quoted in results and answers, and under MDR the intended purpose is read from exactly that text.
- **Do first:** [#1 The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank](#1-the--92--claim-rests-on-a-2019-lyon-study-with-no-public-primary-document-and-no-citable-evidence-page-on-the-main-site-while-forum-doubts-about-it-rank), `url-migration-map`, `partner-listing-consistency`
- **How we'll know the fix failed:** - If, 4 weeks after the test rewrite, clicks on the rewritten URLs for the 'anti mal de dos' queries fall more than about 20 % compared with similar unchanged URLs, revise the modifier before rolling out.
- If, 60 days after the brief, partner listings still show 'anti-douleur' or a bare '92 %', or a Merchant Center Misrepresentation flag persists, the propagation step has failed.
- **Leading indicator to monitor:** - Share of claims-register rows resolved across the site, the feed and partners.
- Search Console clicks and CTR for rewritten URLs compared with a control group.
- Number of partner listings still titled 'Allège la charge de 92%'.
- **To verify on-site:** - Crawl the site with a Screaming Frog custom search using the regex above, across titles, H1s, meta descriptions, body text, alt text and Yoast/Rank Math SEO titles.
- Read /faq/.
- Check whether 'prescrit par les médecins du travail', 'recommandé par kinés, ergonomes et médecins du travail', 'dispositif médical' or 'remboursé' appear anywhere.
- Export the product feed and check titles and descriptions.
- Check Merchant Center status if an account exists.

### 8. Few guide pages target informational carrying and back-pain queries, and Gravipack is absent from those results

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | High | likely | Content Quality |

**Issue.** Gravipack does publish some informational content, so 'the blog is press/PR only' is wrong. Indexed examples: the brand-specific how-to /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/, /evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/, /le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/, /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/ and /faq/ (which, according to search snippets, covers sizing and custom fitting by height and weight). Most other indexed posts are news and PR: SOFINS, RATP/VivaTech (2 posts), Concours Lépine and Bacary Sagna. What is missing is generic, non-brand guides that answer the carrying, load-weight and fit questions people search before they know the brand.

Evidence from the search results we sampled (a US-located, non-Google index):
- The 12 saved informational result sets (K13-K24) contain 0 gravipack.com URLs:
  - 'comment bien porter son sac à dos': pourquoidocteur, 24matins, consoglobe, a CISSS PDF, allodocteurs, a cssphares PDF, courrierlaval.
  - 'quel sac à dos quand on a mal au dos': allodocteurs x2, protegez-vous, MAIF, randonner-leger.
  - 'poids cartable 10%': dhnet, six Assemblée nationale PDFs, pourquoidocteur.
  - 'mal au dos sac à dos randonnée': globe-trotting, rtbf, Deuter x2, Osprey, Salomon x2.
  - 'régler bretelles sac à dos': Salomon x4, Deuter, Rab, blog.snowleader, tonton-outdoor x2.
  - 'poids max sac rando %': Deuter x2, glisshop, rtbf, cimalp, FFRandonnée x2.
  - In 'sac à dos qui soulage le dos et les épaules', 'sac à dos mal aux épaules solution' and 'bretelles ergonomiques sac à dos', Gravipack appears only through third parties: KissKissBankBank, Journal du Geek, randonner-leger threads and i-trekkings.
- Across 13 informational or health prompts, no Gravipack page appeared. Examples: cartable ergonomique mal de dos enfant, poids max sac rando, sac à dos TMS travail, sac à dos recommandé par les ostéopathes, exosquelette passif TMS. Three groups led these results: health institutions (CISSS/CSS PDFs, Assemblée nationale, INSPQ, INRS, OSHA), health media (allodocteurs, pourquoidocteur, Vidal) and brand guides (Deuter, Osprey, Salomon).
- Gravipack effectively created the term 'sac à dos exosquelette', but a kentfaith.fr blog post ('Sac A Dos Exosquelette ?') leads that query. In the extended sample, gravipack.com's category and home page sit at #6-#7.

Caveats:
- Many results came from Quebec, Belgium or Switzerland (cisss-lanaudiere, cssdgs.gouv.qc.ca, dhnet.be, rtbf, inspq). Treat the pattern as a direction, not a Google.fr ranking.
- Most informational queries ran in standard mode, which also under-represented gravipack.com for its own core terms.
- Some queries have mixed intent. For 'sac à dos randonnée anti mal de dos', the Gravipack randonnée category (#5) and home page (#6) rank alongside a zeoutdoor comparison and a norveya blog post. gravipack.com also ranks for the commercial 'anti mal de dos' head terms.
- The gap is therefore the pure how-to and load-weight layer, not the commercial layer.

**Evidence.** <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/> · <https://www.gravipack.com/evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/> · <https://www.gravipack.com/le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/> · <https://www.gravipack.com/et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/> · <https://www.gravipack.com/faq/> · <https://www.gravipack.com/articles/> · <https://www.kentfaith.fr/blog/article_sac-a-dos-exosquelette_6410> · <https://www.salomon.com/fr-ch/sg/a/how-to-properly-adjust-your-backpack> · <https://www.ffrandonnee.fr/randonner/conseils/preparer-son-sac-a-dos> · <https://www.allodocteurs.fr/actualite-sante-mal-de-dos-des-enfants-a-cause-d-un-sac-trop-lourd-_4170.html> · <https://www.pass-education.fr/actualites/cartable-trop-lourd-dos-enfant/>

**Why it matters.** These are the early-stage questions of Gravipack's audience: parents worried about the cartable, hikers with sore shoulders, workers who carry tools. Search engines answer them with guides, so product and category pages cannot take those places.

Outdoor brands and shops (Salomon, Deuter, Osprey, Snowleader, tonton-outdoor, glisshop) win these queries with guides. That shows an e-commerce site can rank here if it stays on carrying and fit topics where it has real expertise.

Gravipack has first-hand material no competitor can copy: strap-adjustment know-how, fitting personalised to height and weight, field use by RATP agents, and a 7-month independent hiking test. Question-style queries are also where AI answers draw their sources, although this audit did not measure presence in AI answers.

**Effect on SEO.** - New top-of-funnel entry points, with internal links into the randonnée, scolaire, business and outillage categories.
- More depth on carrying, adjusting and spreading the load. That supports the commercial 'anti mal de dos' pages that already rank.
- Short, sourced answer passages that answer engines can quote.
- Staying out of medical-condition queries avoids publishing YMYL content the site cannot credibly support.

**How to fix.**

1. Set the scope before writing.
   - Target carrying, fit and load-weight questions only.
   - Do not target hard-YMYL condition queries ('sac à dos scoliose enfant', 'sac à dos hernie discale') as primary keywords. At most, add one reviewed paragraph to the child guide telling readers to see a doctor.
   - Make no therapeutic claims (soigne, guérit, anti-douleur, anti-TMS).
   - Link every mention of the 92 % figure to the evidence page (see study-92-evidence).
2. Build the structure in WordPress without touching existing URLs.
   - Create a Page 'Conseils' at /conseils/ as the hub.
   - Publish each guide as a child Page (Page attributes > Parent: Conseils), e.g. /conseils/regler-son-sac-a-dos/.
   - Do not change Settings > Permalinks; that would move every existing post.
   - Keep news and PR in the existing /articles/ blog.
3. Publish in this order, 1-2 guides per month. Size each guide to its intent: ranking guides run roughly 1,200-1,800 words, but treat that as a guideline, not a target.
   - Hub: « Comment bien porter son sac à dos sans avoir mal au dos » (query: comment bien porter son sac à dos).
   - « Comment régler les bretelles de son sac à dos : la méthode en 5 étapes » (query: comment régler les bretelles d'un sac à dos). Use a generic method, and link Gravipack owners to the existing brand guide /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/. Keep both pages; do not merge or redirect the brand guide.
   - « Poids du cartable : quel poids maximum selon l'âge ? » with a calculator (queries: poids du cartable, poids cartable 10 %). Go live by May-June 2027, before the rentrée.
   - « Poids maximum d'un sac de randonnée : combien porter selon son poids ? » with a calculator (query: poids maximum sac à dos randonnée).
   - « Mal aux épaules avec un sac à dos : causes fréquentes et bons réglages » (query: sac à dos mal aux épaules solution).
   - « Sac à dos exosquelette : définition et fonctionnement » (query: sac à dos exosquelette), to win back the definition query from the kentfaith post. If /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/ overlaps, fold it in with a 301.
   - Later: « Porter des charges au travail : bien choisir et régler son sac » for tradespeople, citing INRS, with no 'anti-TMS' promise.
4. Use this template for every guide:
   - an answer-first paragraph of 40-60 words under the H1;
   - H2s phrased as questions;
   - numbered steps;
   - original photos or diagrams of strap settings;
   - the existing YouTube adjustment videos, embedded;
   - a 'Sources' list (INRS, FFRandonnée, ameli.fr, Éducation nationale);
   - 'Mis à jour le [date]';
   - a box 'Relu par [Nom], masseur-kinésithérapeute DE / ergonome, le [date]';
   - a short, factual closing section « Ce que fait l'exosquelette Gravipack, et ce qu'il ne fait pas », linking to one category and to the evidence page.
   Example answer box for the cartable guide (check every reference before publishing): « Le repère couramment cité en France est un cartable ne dépassant pas 10 % du poids de l'enfant, soit 3 kg pour 30 kg. Les études ne montrent pas de lien clair entre le poids du cartable et le mal de dos (revue systématique BJSM 2018), mais un cartable allégé et bien réglé reste plus confortable. »
   Quote the BJSM 2018 review (Yamato et al.) honestly. Check any FCPE or FFRandonnée percentage against its source before quoting it.
5. Recruit a named kinésithérapeute or ergonomist to review the educational content, and disclose any payment. Do not use doctors or physiotherapists as product endorsers on commercial pages: CSP R.4127-20 forbids it for doctors, and kinés have similar rules.
6. Add markup for entity context only; it earns no rich result.
   - Use Article with a named author, plus reviewedBy and lastReviewed on the WebPage.
   - Do not add HowTo (that rich result was removed), and do not add FAQPage expecting a rich result.
   - In Rank Math or Yoast, set the schema type to Article, then add the reviewer with a snippet like this:
```json
{"@context":"https://schema.org","@type":"WebPage","@id":"https://[hote-canonique]/conseils/regler-son-sac-a-dos/#webpage","lastReviewed":"2027-01-10","reviewedBy":{"@type":"Person","name":"[Nom]","jobTitle":"Masseur-kinésithérapeute DE"},"mainEntity":{"@type":"Article","headline":"Comment régler les bretelles de son sac à dos","author":{"@type":"Person","name":"[Auteur]"},"publisher":{"@id":"https://[hote-canonique]/#organization"},"datePublished":"2027-01-15"}}
```
7. Build each calculator as a small HTML/JS block, or with the Calculated Fields Form plugin. Also print the rule as plain text, so the page reads correctly without JavaScript.
8. Internal links:
   - each guide links to one matching category and back to the hub;
   - each category links to 2-3 guides;
   - the brand adjustment guide links to the generic one;
   - product pages link to the adjustment and fit guides.
9. Publish on the canonical host only (see host-canonical-split). Add the hub to the XML sitemap and request indexing through URL Inspection.

- **First principle:** Search engines match the type of page to the intent of the query. On how-to, load-weight and fit questions, the results are guides from health bodies, media and outdoor brands. A shop can enter those results only with guides, and only credibly on the carrying and fit topics where it has first-hand expertise.
- **Do first:** [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), [#1 The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank](#1-the--92--claim-rests-on-a-2019-lyon-study-with-no-public-primary-document-and-no-citable-evidence-page-on-the-main-site-while-forum-doubts-about-it-rank), `host-canonical-split`, `category-hub-architecture`
- **How we'll know the fix failed:** Check 6 months after the first 4 guides go live. The page-type or topic choice is wrong for this domain if any of these is true:
- Search Console shows none of the guides in the top 20 on Google.fr for its primary query;
- the guides have fewer than about 500 impressions a month combined;
- GA4 shows almost no clicks from the guides to categories.
In that case, rework or merge the guides before writing more.
- **Leading indicator to monitor:** - Search Console Performance, filtered to pages containing /conseils/: impressions and average position for 'comment régler les bretelles d'un sac à dos', 'poids cartable', 'poids maximum sac à dos randonnée' and 'sac à dos exosquelette'.
- GA4 clicks from guides to category pages.
- **To verify on-site:** - In WP admin, list all posts and pages to confirm which informational pages exist beyond the 5 found.
- Read /faq/ and /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/: check content, host, indexability and self-referencing canonical.
- Check Search Console for informational queries that already earn impressions.
- Confirm the category URLs the guides will link to, after any planned category renames.

### 14. No comparison or alternatives content answers 'Gravipack vs …' and comparison intent

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | Content Quality |

**Issue.** No comparison, 'vs' or alternatives page from Gravipack was found, yet comparison intent is clear in the search results we sampled (a US-located, non-Google index).
- On three commercial head-term result pages, listicles or comparisons took about 20-35 % of results:
  - 'sac à dos ergonomique': 2/9 (accergo, le-repaire);
  - 'meilleur sac à dos anti mal de dos': 3/9 (norveya, accergo, techradar);
  - 'sac à dos randonnée anti mal de dos': 3/9 (zeoutdoor comparatif, norveya, accergo).
- On explicit best-of queries, they dominate:
  - 'sac à dos randonnée ergonomique': 4/9 (Glisshop, Ridepark, Toporando, Hardloop), naming Osprey Talon/Exos/Aether, Deuter Aircontact Core 40+10, Gregory, Millet and Mammut;
  - 'meilleur cartable ergonomique 2026': 8/9 (Futura-Sciences, Avis-Parents, meilleurs.fr), naming ergobag Prime, Satch, Baagl and Tann's;
  - 'meilleur sac à dos ergonomique comparatif 2026': Snowleader, Toporando, Clubic, TechRadar;
  - 'sac à dos scolaire anti mal de dos' also carries comparison posts from bodypack, sac-a-dos-france and laboutiquedestoons.
- Gravipack is not named in any comparison or best-of article we saw.
- Two searches found no 'Gravipack vs X' or 'alternatives à Gravipack' page. 'gravipack vs osprey OR deuter OR alternative sac exosquelette' returned only Deuter-vs-Osprey content (outforia, mountainsforeverybody, bushwalk, expertworldtravel).
- None of the gravipack.com URLs recorded in this audit is a comparison page. That record is a sample of search results, so absence on the site is likely rather than certain.
- People do evaluate the brand: the i-trekkings test of the Oslo 70 L ('Idée de génie ou arnaque ?') and a Gomet article rank. Outzer's critical Sherpa 45 review ('Un sac à dos terrifiant', which measured about 30 L of usable volume) ranks for 'gravipack avis'.
- Competing carrying technologies appear in the results:
  - Osprey's AG 'Anti-Gravity' back system (Aura AG on mec.ca and i-run) for 'sac à dos anti gravité', where gravipack.com is absent;
  - Deuter Aircontact;
  - Tucano Marte Gravity 'AGS' (3 pearl.fr results for 'sac à dos ordinateur anti mal de dos');
  - Kensington Contour, ergobag, Bon Chic Bon Dos and the LEX exoskeleton.
- Osprey also has an official French sizing guide, and Deuter publishes advice pages on back pain and maximum load.
- gravipack.com's home page already ranks #5 for 'meilleur sac à dos anti mal de dos' in the extended sample. A separate brand 'meilleur…' page would compete with it.

**Evidence.** <https://outforia.com/deuter-vs-osprey> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · <https://gomet.net/innovation-gravipack-le-sac-a-dos-qui-defie-la-pesanteur/> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html> · <https://zeoutdoor.com/randonnee/comparatif-sac-a-dos-de-randonnee> · <https://norveya.com/blogs/organisation/les-meilleurs-sacs-a-dos-ergonomiques-contre-le-mal-de-dos> · <https://www.accergo.fr/meilleurs-sacs-a-dos-ergonomiques/> · <https://toporando.fr/meilleurs-sacs-a-dos-randonnee-trekking/> · <https://www.futura-sciences.com/conso/comparatifs/meilleur-cartable-comparatif/> · <https://www.avis-parents.com/tests-avis/meilleur-cartable-primaire/> · <https://www.mec.ca/fr/product/6016-968/sac-a-dos-aura-ag-60-de-osprey-femmes> · <https://www.pearl.fr/article/TG3837/sac-a-dos-pour-pc-portable-15-6-16-marte-gravity-avec-redresse-dos-noir> · *(+1 more in findings/)*

**Why it matters.** Gravipack bags cost roughly €90-€289. Buyers compare them with hip-belt and ventilated-back designs from brands they already know, and the exoskeleton only makes sense next to those alternatives. When the brand publishes no fair comparison, sceptical third-party reviews frame the choice instead.

A brand-written 'meilleur…' listicle that puts its own product first rarely ranks, because review-type results favour independent hands-on testing. The realistic routes are honest mechanism explainers and 'X vs Y' pages from the brand, plus getting into the independent listicles that already rank.

**Effect on SEO.** - Pages that can rank for 'X vs Y', 'quel modèle choisir', 'sac à dos anti gravité' and 'exosquelette ou sac classique' queries.
- Internal links to model pages.
- A sourced comparison that answer engines can quote instead of forum threads.
- Outreach can get Gravipack into existing 'meilleur…' listicles that the brand cannot rank for itself.

**How to fix.**

1. Prepare the data first. Keep one master spec sheet per model: volume as measured, empty weight as weighed, strap fitting range, warranty and current price. Use it on the site and send it to every reseller. Resolve the conflicts this audit found: Hiking listed as 30 L and 33 L; Sherpa weight listed as 1,200 g and 1,250 g; Sherpa volume, which Outzer measured at about 30 L.
2. Build the pages in this order. Size each one to its intent, with no fixed word count.
   a. « Quel Gravipack choisir ? Sherpa, Hiking, Oslo, Tokyo, Business Talk, Kingston… » at /quel-gravipack-choisir/. One comparison table (use, volume, weight, fitting, warranty, 'prix au [date]'), built with a WooCommerce product table or TablePress, linking every product.
   b. « Sac à dos à exosquelette ou sac à dos classique : quelles différences ? » at /comparatif/sac-a-dos-exosquelette-vs-sac-classique/.
   c. « Exosquelette Gravipack ou dos Anti-Gravity d'Osprey : deux façons de porter » at /comparatif/exosquelette-vs-anti-gravity/, targeting 'sac à dos anti gravité'. Describe Osprey AG from Osprey's own pages, with links.
   d. « Exosquelette ou ceinture ventrale : que fait chaque système de la charge ? ». Say honestly that a hip belt moves load to the pelvis and may suit heavy treks better.
   e. « Gravipack Sherpa 45 vs Osprey Talon 44 vs Deuter Aircontact Core 40+10 », only after weighing and measuring all three bags.
   f. « Cartable ergonomique collège : Feather vs ergobag vs Satch », only once Feather is sold on gravipack.com and its height threshold is the same everywhere (today 1m50 in some places, 1m55 in others). Have a paediatric physiotherapist review it.
   g. A laptop-bag comparison table inside the business category (Business Talk V4 and Kingston vs Tucano Marte Gravity and Kensington Contour), not a separate page.
   Do not create a standalone 'meilleur sac à dos anti mal de dos' page. Put a comparison table in the hub or category that already ranks.
3. Apply these fairness rules on every page.
   - Show a visible disclosure such as: « Gravipack est notre marque. Ce comparatif est rédigé par l'équipe Gravipack. Les caractéristiques des autres sacs proviennent des sites de leurs fabricants (liens ci-dessous), relevées le [date]. Nous indiquons aussi les points sur lesquels ils font mieux que nous. »
   - Link every competitor fact to the maker's page.
   - Write 'Non communiqué' for missing data.
   - Name competitor strengths: hip-belt load transfer, ventilated backs, lower weight or price.
   - Make no medical claims.
   - Present the 92 % only as « chiffre annoncé par le fabricant », linked to the evidence page.
   - Add a 'Méthodologie' section and 'Mis à jour le', and review each page every quarter.
4. Titles follow the pattern « Gravipack Sherpa 45 vs Osprey Talon 44 : poids, volume et portage comparés (2026) ». Breadcrumb: Accueil > Comparatifs > page.
5. Markup: ItemList for the chooser and roundups, Article for explainers, and Product only for Gravipack's own products. Never add Product, Review or AggregateRating markup for competitors. Example:
```json
{"@context":"https://schema.org","@type":"ItemList","name":"Quel Gravipack choisir ?","itemListElement":[{"@type":"ListItem","position":1,"url":"https://[hote-canonique]/produit/[sherpa-45]/"},{"@type":"ListItem","position":2,"url":"https://[hote-canonique]/produit/[hiking-30]/"}]}
```
6. Win the listicle places through outreach. Offer loan samples, with disclosure, to authors who already rank: zeoutdoor, Toporando, guide-velo, tonton-outdoor, meilleurtest, accergo, norveya, Avis-Parents. Affiliate links must carry rel="sponsored". Never trade samples for links.

- **First principle:** When comparisons dominate the results for a query, a product page cannot satisfy that query, and whoever publishes the comparison shapes the buying decision. A brand can credibly own comparisons of mechanisms and of its own range, but not 'best of' verdicts about itself.
- **Do first:** [#1 The '-92 %' claim rests on a 2019 Lyon study with no public primary document and no citable evidence page on the main site, while forum doubts about it rank](#1-the--92--claim-rests-on-a-2019-lyon-study-with-no-public-primary-document-and-no-citable-evidence-page-on-the-main-site-while-forum-doubts-about-it-rank), [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), `cross-channel-spec-consistency`, `category-hub-architecture`
- **How we'll know the fix failed:** The format or the data is wrong if, 6 months after launch:
- Search Console shows no impressions for 'vs', 'ou', 'anti gravité' or 'quel gravipack' queries on the new pages;
- the pages draw impressions but no clicks to product pages;
- a competitor disputes a fact on a page.
For outreach: if 10 disclosed pitches lead to no inclusion in an independent comparison, change the angle (for example, offer the measured spec sheet) instead of sending more pitches.
- **Leading indicator to monitor:** - Search Console impressions and clicks for queries containing 'vs', 'ou', 'comparatif', 'anti gravité' or 'quel gravipack'.
- A monthly count of independent comparisons that name Gravipack.
- **To verify on-site:** - Confirm in WP admin and site search that no comparison or model-chooser page exists.
- Check the product attribute fields (volume, weight, warranty) for each model, and whether they match reseller listings.
- Check whether Feather is sold on gravipack.com.
- Check in Search Console which page currently ranks for 'meilleur sac à dos anti mal de dos'.

### 35. The inventor-founder's expertise is spread across several posts rather than one authoritative bio

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | Content Quality |

**Issue.** The founder is visible online, so 'no visible entity footprint' is wrong. The issue is that his expertise is scattered.
- Owned founder content exists:
  - /inventeur-dun-sac-a-dos-en-apesanteur/, whose title leads with a claim: 'Le sac à dos en apesanteur anti-mal de dos allège le poids de 92%';
  - /et-si-tout-commencait-par-un-sac-trop-lourd-et-un-reve-de-le-rendre-leger-pour-tous/;
  - the about page /a-propos-de-nous-gravipack-au-service-de-votre-dos/, titled like a product page ('Le sac anti mal de dos léger Gravipack au service de votre dos et de vos épaules');
  - /gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/.
- Third parties name Mohammed Errafi as inventor, founder and president: lespepitestech, Journal du Geek, Neozone, Europe 1's Trophées de l'Avenir 2023 profile, INPI's 2022 Trophées profile, forumeco, a fnh.ma interview, a founder interview on YouTube, and his LinkedIn profile (linkedin.com/in/errafi/, posts from 2021 to 2023).
- Name ambiguity: the search 'Mohammed Errafi Gravipack LinkedIn' returned the unrelated packaging company 'Gravis'. That suggests search engines link the person and the brand only weakly.
- Unknown without a crawl: whether these pages carry a proper bio, photo, dates, author attribution and Person markup, and whether the Organization markup declares a founder.

**Evidence.** <https://gravipack.com/inventeur-dun-sac-a-dos-en-apesanteur/> · <https://www.gravipack.com/et-si-tout-commencait-par-un-sac-trop-lourd-et-un-reve-de-le-rendre-leger-pour-tous/> · <https://www.gravipack.com/a-propos-de-nous-gravipack-au-service-de-votre-dos/> · <https://www.gravipack.com/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/> · <https://lespepitestech.com/startup-de-la-french-tech/gravipack> · <https://www.europe1.fr/node/58664> · <https://www.inpi.fr/trophees/gravipack-les-bretelles-qui-allegent-le-poids-sur-les-epaules-et-le-dos> · <https://forumeco.fr/gravipack-revolutionne-le-sac-a-dos/> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://www.linkedin.com/in/errafi/> · <https://www.youtube.com/watch?v=V0CuNW4N9Q8> · <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383>

**Why it matters.** An inventor's first-hand account (why he designed the exoskeleton, the prototypes, tests and awards) is experience that generic competitor content cannot copy. It also answers the rater guidelines' question of who is behind the site. Journalists and answer engines need one stable page describing the person and his role.

**Effect on SEO.** A single bio page, linked from the Organization markup:
- helps search engines connect the person, the brand and the legal entity;
- can rank for founder and 'inventeur gravipack' queries;
- gives the press one page to link to.

**How to fix.**

1. Create one authoritative bio.
   - Preferably make it a section of the existing about page, with its own anchor, to avoid a second about page. Otherwise publish it at /mohammed-errafi-inventeur-gravipack/.
   - Role: président d'EXOSQUELETTE LIGHT SAS, inventeur de l'exosquelette Gravipack.
   - The invention story with dated milestones, each linked to a source: first patent filing 2016, company created 2018, Concours Lépine silver medal 2018, Trophées INPI 2022 finalist, Europe 1 Trophées de l'Avenir 2023 nominee, RATP deployment shown at VivaTech 2023.
   - Patents, linked to the IP page (patents-trademark).
   - A list of press interviews with links, a photo and a press contact.
   - Only press sources were found for the Lépine year, so confirm it from the official prize list before publishing.
   - Include no personal data beyond name and role.
2. Retitle the about page to describe the company, e.g. « À propos de Gravipack : l'inventeur, l'entreprise et l'exosquelette ».
   - Retitle /inventeur-dun-sac-a-dos-en-apesanteur/ without the 92 % claim, e.g. « Mohammed Errafi, inventeur du sac à dos à exosquelette Gravipack ».
   - Keep the slugs, and link both posts to the bio.
3. In WordPress, create or complete his user profile (biographical info, photo) and set him as author of the posts he wrote. Keep his author archive indexable only if it has real content.
4. Add Person and Organization JSON-LD with linked @ids, using the registry facts: legal name EXOSQUELETTE LIGHT SAS, current registered seat 10 rue de la Paix, 75002 Paris.
   - With Yoast, extend the Organization piece with a filter:
```php
add_filter('wpseo_schema_organization', function ($data) {
  $data['legalName'] = 'EXOSQUELETTE LIGHT SAS';
  $data['founder'] = ['@id' => home_url('/a-propos-de-nous-gravipack-au-service-de-votre-dos/#mohammed-errafi')];
  return $data;
});
```
   - Output the Person node (in Rank Math: Schema Generator > custom JSON-LD):
```json
{"@context":"https://schema.org","@type":"Person","@id":"https://[hote-canonique]/a-propos-de-nous-gravipack-au-service-de-votre-dos/#mohammed-errafi","name":"Mohammed Errafi","jobTitle":"Fondateur, président et inventeur de l'exosquelette Gravipack","worksFor":{"@id":"https://[hote-canonique]/#organization"},"sameAs":["https://www.linkedin.com/in/errafi/"]}
```
5. Use the bio in the press kit and as the author box on posts he writes. He is the inventor, not a health professional, so the guides and the evidence page still need an independent health reviewer.

- **First principle:** Search engines and journalists attribute expertise to a named person who is described the same way everywhere. When an inventor's story is split across posts titled as product claims, there is no single entity page to attach that expertise to.
- **Do first:** [#38 Patent and trademark claims are not backed by publication or registration numbers](#38-patent-and-trademark-claims-are-not-backed-by-publication-or-registration-numbers), `entity-facts-organization-schema`
- **How we'll know the fix failed:** The consolidation has not worked if, 3 months after launch:
- the Rich Results Test or Schema Markup Validator does not show the Person linked as founder;
- the bio page does not appear for 'Mohammed Errafi Gravipack' or 'inventeur gravipack' on Google.fr;
- new press coverage still links to scattered posts.
- **Leading indicator to monitor:** - Search Console impressions on the bio page for queries containing 'errafi' or 'inventeur gravipack'.
- Number of new press links pointing to the bio.
- **To verify on-site:** - Read the about page and the two founder posts: bio, photo, dates, byline.
- Inspect the existing JSON-LD (Organization founder, Person) with the Rich Results Test.
- Check whether author archives exist and whether they are noindexed.

### 38. Patent and trademark claims are not backed by publication or registration numbers

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | Content Quality |

**Issue.** Patents:
- Patent counts in public sources rise over time, which fits a growing portfolio rather than a contradiction:
  - about 3 international patents around 2018-19 (Neozone; forumeco, which also says the first filing was in 2016);
  - 4 in 2020 (lematin.ma);
  - 'Brevets : 1 France, 9 internationaux et 3 en cours de dépôts' on INPI's 2022 Trophées profile;
  - then 9 (fnh.ma).
- A search snippet for a product page showed 'protégé par 13 brevets' (verify on-site). 13 equals 1 + 9 + 3, so it would count pending applications as patents.
- No publication number surfaced in 6 searches across Google Patents, Espacenet, Patentscope, EPO, INPI and Justia (by inventor Mohammed Errafi, by Gravibag/Gravipack and by technical terms). Only unrelated backpack patents came back. The search tool indexes patent databases poorly, so this is not evidence that the patents do not exist.
- The first filing (2016) predates the company (2018), so the holder may be the inventor personally, licensing the patents to the company. Confirm this.
- The post /le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/ may already list the numbers (verify on-site).
- 'Breveté' is used without a number: in gravipack.ma's tagline 'premier sac à dos exosquelette anti mal de dos breveté' and in the YouTube video 'Exosquelette breveté Gravipack sac a dos - Vidéo 3D'.

Trademark:
- A GRAVIPACK filing dated 27/05/2019 (in force to 27/05/2029) rests on a societe.com summary. INPI's profile mentions 2 marks and an international filing.
- No INPI, EUIPO or WIPO register entry was seen in 2 searches. The INPI index instead surfaces FR3275099 'GRAVIPACK', an unrelated mark filed in 2004 and expired in 2014, covering classes 1, 17 and 19.
- '®' appears in titles such as 'Gravipack®' (Light Promax) and 'GraviPack®' (/nos-engagements/).

**Evidence.** <https://www.inpi.fr/trophees/gravipack-les-bretelles-qui-allegent-le-poids-sur-les-epaules-et-le-dos> · <https://forumeco.fr/gravipack-revolutionne-le-sac-a-dos/> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://www.neozone.org/innovation/gravipack-le-sac-a-dos-qui-reste-leger-comme-une-plume-meme-quand-il-est-plein-a-craquer> · <https://www.gravipack.com/le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/> · <https://www.societe.com/societe/gravipack-840543383.html> · <https://data.inpi.fr/marques/FR3275099> · <https://gravipack.ma/> · <https://www.youtube.com/watch?v=homKGDpmhOA> · <https://gravipack.com/nos-engagements/> · <https://www.gravipack.com/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/>

**Why it matters.** For an inventor-led brand, verifiable patents are among the few expertise signals anyone can check. Without numbers, 'breveté' reads as marketing. Calling pending applications patents, or using ® where a mark is not registered, is itself a misleading-practice risk.

Register numbers also separate the brand from homonyms: the expired 2004 GRAVIPACK mark, and the 'Gravis' packaging company that appears in searches for the founder.

**Effect on SEO.** Minor but cheap:
- a checkable fact that press, Wikidata and answer engines can state without hedging;
- links to authoritative register pages;
- the basis for replacing superlatives with 'technologie brevetée (brevet n° …)' in health-claims-wording.

**How to fix.**

1. Get from the IP counsel, for each patent family: publication numbers (FR, EP, WO, national), title, applicant or holder (the inventor or EXOSQUELETTE LIGHT SAS, and any licence), inventor, filing and grant dates, status and territories. Cross-check on data.inpi.fr and Espacenet (inventor 'Errafi').
2. Publish one reference page, either by updating /le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/ or as /brevets-et-marques/. Link it from the footer and from product pages. Example table:
```
| Titre | N° de publication | Titulaire | Inventeur | Dépôt | Statut | Territoires | Registre |
|---|---|---|---|---|---|---|---|
| [Bretelle à exosquelette …] | FR [n°] | [titulaire] | Mohammed Errafi | [date] | Délivré | FR | Espacenet |
| [..] | WO [n°] | [..] | Mohammed Errafi | [date] | Demande en cours | [pays] | Patentscope |
```
   Add 'Dernière vérification le [date]'.
3. Wording rules:
   - 'technologie brevetée (brevet FR n° …)' only for granted patents;
   - 'demande de brevet déposée (n° …)' for pending ones;
   - one dated count, e.g. « Au [date] : 1 brevet français délivré, 9 titres internationaux, 3 demandes en cours », and only if counsel confirms it;
   - replace 'protégé par 13 brevets' if it includes pending applications.
4. Trademark:
   - Get the registration numbers, owner and classes (backpacks fall in class 18).
   - Add to the mentions légales: « Gravipack® est une marque déposée de [titulaire] (INPI n° [..] ; [UE/OMPI n° ..]). »
   - Use ® only where the mark is registered. This matters for gravipack.ma unless the registration covers Morocco.
5. Use the same count and wording on the INPI profile, LinkedIn, the KissKissBankBank pages, gravipack.ma, YouTube and the press kit.
6. Markup: declare the brand on Product (brand: {"@type":"Brand","name":"Gravipack"}) and keep patent numbers as visible text. There is no rich result for patents.

- **First principle:** An IP claim builds trust only when anyone can check it in a public register. Without numbers, 'breveté' reads as marketing, and a register search shows an unrelated expired GRAVIPACK mark instead.
- **Do first:** —
- **How we'll know the fix failed:** - If counsel cannot give publication numbers for granted patents, 'breveté' must go. Keeping it means this fix failed.
- After publication: if press and resellers still use different counts 3 months later, or the page gets no impressions for 'gravipack brevet', the reference page is not being found or used.
- **Leading indicator to monitor:** - Number of owned and partner surfaces using the agreed, dated IP statement.
- Search Console impressions for 'gravipack brevet'.
- **To verify on-site:** - Read the propriété industrielle post, the mentions légales and the CGV for patent and trademark numbers.
- Crawl for '®', 'breveté', 'brevet' and '13 brevets'.
- Check how the product page that showed 'protégé par 13 brevets' words it.

### 40. No public size/fit table maps height and weight to strap settings, although bags are adjusted to each buyer

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | likely | Content Quality |

**Issue.** Fit content exists, but no public rule tells a buyer which setting or size they will get.

What exists (from search snippets; verify on-site):
- The Business Talk V4, Hiking and Tokyo product pages say each bag is personalised free of charge to the buyer's height and weight, within ±10 cm and ±8 kg.
- The Austerlitz page asks for height and weight at order and adjusts the bag in the workshop.
- The Tokyo page mentions an exchange if the wearer's build changes.
- /faq/ covers sizing and custom fitting.
- An official adjustment guide exists at /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/.

What is missing: a public table mapping height and weight to a strap setting or size, and 'comment se mesurer' (how to measure yourself) content. Neither surfaced.

Sales channels describe fit differently:
- Ergo-Corner titles every Gravipack product 'Personnalisation de l'exosquelette M/L/XL/XXL' or '3 tailles', with 'sur-mesure' for very small or tall people.
- The Feather vs Feather Plus threshold is '<1m55' on most channels but '<1m50 et 30 kg' on Kiabi.

Competitors own the size-guide results:
- Osprey's official French sizing guide measures torso length from C7 to the iliac crest (S/M 43-52 cm, WXS/S 34-43 cm). Snowleader and Alpinstore republish it.
- Arsayo sizes its bags by shoulder width (S/M/L).

Fit comes up in some reviews, alongside other complaints such as refunds:
- Decathlon reviewers of the Hiking 33 mention hard adjustment and straps rubbing the neck when the bag is lightly loaded.
- One Decathlon reviewer obtained custom straps only after contacting the brand.
- Trustpilot reviews mention straps coming loose.

**Evidence.** <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/> · <https://gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://www.gravipack.com/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/faq/> · <https://www.ergo-corner.com/gravipack/676-sherpa-45l-kaki-avec-exosquelette-gravipack-.html> · <https://www.ergo-corner.com/gravipack/737-sac-a-dos-city-avec-exosquelette-gravipack.html> · <https://www.kiabi.com/sac-a-dos-gravipack-feather-noir-noir_P1459532C1459533> · <https://www.osprey.com/fr/expert-advice/sizing> · <https://www.snowleader.com/guide-des-tailles-osprey> · <https://www.alpinstore.com/fr/content/2744-guide-taille-osprey> · <https://www.decathlon.fr/r/mp/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/093a557b-159a-4282-95a8-76495a70d99e/c5>

**Why it matters.** Personalised fitting is a selling point, but before ordering a buyer cannot tell what 'adjusted to your height and weight' means or what to enter. A public table answers that. It also reduces fit-related returns and reviews, and gives resellers one consistent wording instead of their own M/L/XL labels.

**Effect on SEO.** Modest:
- a page that can rank for long-tail queries such as 'taille sac à dos' and 'comment choisir la taille de son sac à dos', alongside Osprey's guide;
- consistent fit data for product pages, feeds and resellers, which can link back to the guide.

**How to fix.**

1. Publish « Guide des tailles et du réglage Gravipack » at /guide-des-tailles-gravipack/. It should include:
   - How personalisation works: « Indiquez votre taille et votre poids à la commande : nous préréglons l'exosquelette en atelier (tolérance ±10 cm et ±8 kg). Si votre morphologie change, contactez-nous pour un échange. » Match the exact terms of the CGV.
   - One table per model family, mapping height range and weight range to the workshop setting or strap size actually used (for example: Taille 150-165 cm / Poids 45-60 kg → réglage [A]). Use the internal settings. Do not invent an M/L/XL/XXL scale if the workshop does not use one.
   - « Comment se mesurer »: height without shoes and current weight; for models with a hip belt, torso length from C7 to the iliac crest.
   - One Feather vs Feather Plus threshold, stated the same way everywhere.
   - Links to the existing adjustment guide and the YouTube adjustment video.
2. In WooCommerce, make height and weight required fields on products that are pre-adjusted (WooCommerce Product Add-Ons or a similar plugin), and show the guide link next to them:
```php
add_action('woocommerce_before_add_to_cart_button', function () {
  echo '<p class="gp-fit"><a href="/guide-des-tailles-gravipack/">Guide des tailles : quelle taille et quel poids indiquer ?</a></p>';
});
```
3. Link the guide from every product page, from /faq/ and from the adjustment guide.
4. Send the table to resellers (Ergo-Corner, the Decathlon sellers, Nature & Découvertes, Au Vieux Campeur, Kiabi) with a link back, and ask them to replace their own size labels with it.
5. Only if sizes are sold as separate WooCommerce variations, expose them as the size attribute in Product/Offer markup and in the product feed. Otherwise leave size out of the markup.

- **First principle:** Buyers of a fitted product need to know before ordering whether it will fit. When a brand personalises fit but does not publish the rule, competitors' size guides and post-purchase reviews answer that question instead.
- **Do first:** `cross-channel-spec-consistency`
- **How we'll know the fix failed:** Track return reasons in WooCommerce. The table is unclear or badly placed if, within 6 months of publication, fit-related return reasons and 'quelle taille' contact requests do not fall, or the guide gets no clicks from product pages.
- **Leading indicator to monitor:** - Share of orders with height and weight filled in.
- Fit-related return reasons per month.
- Clicks from product pages to the guide.
- **To verify on-site:** - Read the /faq/ sizing answer and the fitting text on product pages.
- Ask the workshop whether it uses separate strap sizes or settings.
- Check whether WooCommerce already captures height and weight at order.
- Check the Feather / Feather Plus threshold stated on the site.

### 41. Pre-order dates that have already passed may still be live on product pages, and news posts show no dates in search snippets (verify on-site)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | Content Quality |

**Issue.** This evidence comes from search snippets only. The live site could not be fetched, and a snippet can be cached from before a date passed. Audit date: 12 Oct 2026.

**Pre-order dates in snippets that have now passed**
- **Tokyo PDP** (apex, /produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/): 'premières expéditions à partir de mi-septembre 2026'.
  - This is one of the strongest owned product pages in the search results we sampled (a US-located, non-Google index). It appears for 'sac à dos anti mal de dos' and 'sac à dos vélo travail anti mal de dos', and it was the first owned URL for 'gravipack avis'. A stale date here is seen by the most searchers.
- **Business Talk V4 20L** (www): 'précommande … disponibilité prévue en juin 2026', described as a limited series.
- **Business Talk V4 25L 'deux ordinateurs'** (www): 'Prévente – Offre Early Bird : livraison garantie en août', with 129,90 € struck through to 59,90 €. The snippet gives no year, but any August before today has passed. If the Early Bird price is still active, it is a −54 % promotion with no end date.

**Pre-order date that will pass in about 5 weeks**
- **Claie Barracuda / fourreau Gravitech** (apex, /produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/; SERP title 'Claie de portage révolutionnaire exosquelette anti-mal de dos'): 'livraison à partir de mi-novembre 2026'.

**Signals that make the problem worse**
- The product-tag archive www /etiquette-produit/precommande/ is indexed. Its title is 'Précommande - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos.' (109 characters). Products that have shipped may still be listed there as pre-orders.
- A legacy presta.gravipack.com CMS page still describes 'commandes de réservation' with 2-3 months' delivery. The main store's product pages and CGV promise 1-2 days in France, so the index carries conflicting delivery promises.
- The gravipack.com Trustpilot profile (3.1/5 from 9 reviews in our sample) includes a review of an order delivered about three months late. Some positive reviews also mention a late but tracked delivery. That profile led the 'gravipack avis' results we sampled, so missed dates already reach the review results.
- The only 2026-dated owned content we found is this pre-order copy. Dated blog posts in the sample run from 2022 to 2025.

**News and event posts with no date in snippets**
- A site-restricted 2025/2026 query surfaced these pages with no publication date or event date in the result summaries:
  - /actualites-gravipack-2/
  - the SOFINS post /gravipack-soulage-les-forces-speciales-au-sofins/ (plus a /test/ duplicate)
  - /gravipack-presentees-au-salon-militaire-techterre-combat-futur/
  - /gravipack-bientot-en-magasin-linnovation-en-apesanteur-prend-son-envol/ (names no store)
- Correction to the original claim: the /articles/ blog is dated (posts from 2022 to 2025 in the phase-1 sample). The gap is that snippets and these event or news posts show no date, not that the site has no dates at all. Whether each post shows a date on the page needs an on-site check.

**Moved to other findings**
- Price spreads across snippets (for example Business Talk V4 at 149 € vs 129 €, Pearl, Oslo, Sherpa) are mostly crawl timing and promotions, such as the Decathlon promotion from 18/06 to 30/08/2026. They are covered in the price-parity finding.
- Spec conflicts (Hiking Gris URL says '30l' but the page says 33 L; Rome 1,6 kg vs 1,9 kg; Oslo '60+10L' vs '70L') are covered in the product-data consistency finding.
- Utility pages indexed as products are covered in the B2B finding.
- A mismatch between the schema price and the visible price only matters on the live page. It is listed under onsite_check.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/> · <https://gravipack.com/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/> · <https://www.gravipack.com/etiquette-produit/precommande/> · <https://www.gravipack.com/actualites-gravipack-2/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/gravipack-presentees-au-salon-militaire-techterre-combat-futur/> · <https://gravipack.com/gravipack-bientot-en-magasin-linnovation-en-apesanteur-prend-son-envol/> · <https://www.gravipack.com/articles/> · <https://fr.trustpilot.com/review/gravipack.com> · <https://es.trustpilot.com/review/gravipack.com> · *(+1 more in findings/)*

**Why it matters.** A visible delivery date is a promise. When 'juin 2026' or 'mi-septembre 2026' is still shown in October 2026, the shopper reads it as a late product or an unmaintained shop. That hurts most on the Tokyo page, one of the brand's best-ranking product pages, and for a brand whose review results already include delivery-delay and refund complaints. A pre-order that is past its date or never expires also invites disputes under French consumer law: the seller must state a delivery date or deadline before the order is placed. Undated event posts stop readers, journalists and AI answer engines from judging how recent the SOFINS or Techterre activity is, which weakens the only fresh owned news the brand has.

**Effect on SEO.** The effect is indirect and works through click-through rate, conversion and trust, not through a ranking penalty. Past-due dates in snippets lower CTR on product pages that already rank. If the stock status, Product JSON-LD availability (PreOrder, BackOrder or InStock) and the Merchant Center feed disagree, Google can drop availability and price from product snippets and flag free merchant listings. The indexed 'Précommande' tag archive can keep showing shipped products as pre-orders. Visible dates and datePublished/dateModified on posts help Google and AI answer engines judge recency and cite the right event. The freshness gain is small but real.

**How to fix.**

1. **List every dated promise (about 1 hour).** In WP-CLI, run one search per term:
   ```bash
   for t in "précommande" "prévente" "Early Bird" "disponibilité prévue" "premières expéditions" "livraison garantie" "livraison à partir" "bientôt"; do
     wp post list --post_type=product,post,page --post_status=publish --s="$t" --fields=ID,post_title,post_type; done
   # If pages are built with Elementor, the text is also stored in post meta:
   wp db query "SELECT post_id FROM $(wp db prefix)postmeta WHERE meta_key='_elementor_data' AND meta_value LIKE '%précommande%'"
   ```
   Also open Produits → Étiquettes → 'Précommande' and list its products. Check the short description, the long description and any custom 'disponibilité' field.
2. **Fix each product's stock status today, starting with Tokyo, both Business Talk V4 pages and Barracuda/Gravitech.** For Business Talk V4, edit only the URL that will remain after the duplicate-product consolidation.
   - **Shipped and available:** Produit → Inventaire → État du stock = 'En stock' and tick 'Gérer le stock ?'. Remove the 'Précommande' tag. Replace the copy with « En stock – expédié sous 1 à 2 jours ouvrés » so it matches the CGV.
   - **Still not shipped:** État du stock = 'En réapprovisionnement' and Autoriser les commandes en réapprovisionnement = 'Autoriser, mais avec notification client'. Write a new honest, dated message such as « Précommande – premières expéditions prévues à partir du [jj mois 2026]. Nous vous prévenons par e-mail en cas de changement. »
   - **Limited series sold out (Business Talk V4 20L 'série limitée'):** set 'En rupture de stock'. Keep the page live (status 200) with a link to the nearest current model, and do not hide out-of-stock items from the catalogue if the page ranks. Use a 301 to the successor only when the product is permanently discontinued.
   - **Expired Early Bird:** end the sale. For any future promotion, use Prix promo → 'Planifier' with Du/Au dates so it ends automatically. Price markup (StrikethroughPrice priceSpecification plus validFrom/validThrough, not priceValidUntil) is covered in the price finding.
3. **Make pre-order messages expire on their own** so this cannot recur. Option A is the official WooCommerce Pre-Orders extension, which takes a release date and switches the product to purchasable when that date arrives. Option B is a custom field `_gp_date_expedition` (format AAAA-MM-JJ) plus this snippet in the Code Snippets plugin:
   ```php
   // Visible text: shows the date only while it is still in the future
   add_filter( 'woocommerce_get_availability_text', function ( $text, $product ) {
     $d = get_post_meta( $product->get_id(), '_gp_date_expedition', true );
     if ( $product->is_on_backorder() && $d ) {
       $ts = strtotime( $d );
       return $ts > time()
         ? sprintf( 'Précommande – premières expéditions à partir du %s', date_i18n( 'j F Y', $ts ) )
         : 'Réassort en cours – contactez-nous pour connaître le délai exact';
     }
     return $text;
   }, 10, 2 );
   // Structured data: PreOrder + availabilityStarts only while the date is in the future
   add_filter( 'woocommerce_structured_data_product_offer', function ( $offer, $product ) {
     $d = get_post_meta( $product->get_id(), '_gp_date_expedition', true );
     if ( $product->is_on_backorder() && $d && strtotime( $d ) > time() ) {
       $offer['availability'] = 'https://schema.org/PreOrder';
       $offer['availabilityStarts'] = date( 'c', strtotime( $d ) );
     }
     return $offer;
   }, 10, 2 );
   ```
   If Rank Math generates the Product schema instead of WooCommerce, make the same change through the `rank_math/snippet/rich_snippet_product_entity` filter. Yoast WooCommerce SEO builds on the WooCommerce data, so the filter above applies.
4. **Keep the feed in line with the page.** In Google for WooCommerce or your feed plugin, map 'En réapprovisionnement' to `preorder` or `backorder` with an `availability_date`, which Merchant Center requires for pre-orders. Turn on automatic item updates for availability and price. Then check every edited product page in the Rich Results Test: visible text, Offer.availability and price must agree.
5. **Handle the 'Précommande' tag archive.**
   - Remove the tag from products that have shipped.
   - Set product tags to noindex. In Yoast: Réglages → Taxonomies → Étiquettes produits → 'Afficher dans les résultats de recherche' = Non. In Rank Math: Titres & Méta → Étiquettes produits → Robots Meta = No Index.
   - If the tag is retired, 301 /etiquette-produit/precommande/ to the 'Nouveaux sacs à dos Gravipack' category with the Redirection plugin or Rank Math → Redirections.
6. **Dates on news and event posts.** Check first: posts under /articles/ already show dates.
   - Where a template hides the date (single posts, /actualites-gravipack-2/ listing), turn it on. In Astra: Personnaliser → Blog → Article unique → Méta 'Date'. In Elementor Theme Builder: 'Infos de la publication' widget, Date + 'Dernière mise à jour'. The rendered line should read « Publié le 12 mars 2025 · Mis à jour le 10 octobre 2026 ».
   - Make sure the SEO plugin outputs BlogPosting or Article (not NewsArticle) with datePublished and dateModified. In Yoast: Réglages → Types de contenu → Articles → Type d'article = 'Article de blog'. In Rank Math: Schema → Articles → 'Blog Post'.
   - Change dateModified only when the content changes materially.
   - Keep the /actualites-gravipack-2/ URL. Renaming it is low-value URL churn.
7. **Date the events in the copy.**
   - In the first sentence of the SOFINS and Techterre posts, give the event date and place, e.g. « Les [jj–jj mois aaaa], Gravipack a présenté la claie Barracuda au salon SOFINS… », using the real dates.
   - Update 'Gravipack bientôt en magasin' with the store names and a dated « Mise à jour du [date] » box. Otherwise link it to the where-to-buy page.
8. **Remove the conflicting legacy promise.** Change the presta.gravipack.com 'commandes de réservation / 2-3 mois' page, or 301 it, as part of retiring the presta subdomain.
9. **Recrawl and make it routine.**
   - Request indexing for the edited product pages and posts in Search Console with URL Inspection → 'Demander une indexation'. The Indexing API does not apply to products.
   - For Bing, ping the URLs through IndexNow (Rank Math Instant Indexing or Microsoft's IndexNow plugin).
   - On the 1st of each month, list overdue pre-orders with `wp post list --post_type=product --meta_key=_gp_date_expedition --meta_compare='<' --meta_value=$(date +%F) --fields=ID,post_title`. The target is an empty list.

- **First principle:** A date in a page or snippet is a promise with an expiry date. Once it passes, unchanged text tells searchers the product is late or the shop is not maintained. Search engines and Merchant Center also compare the availability stated in the copy, the structured data and the feed. Freshness has to be managed by a process, not by one-off edits.
- **Do first:** [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles)
- **How we'll know the fix failed:** 1. If the on-site check shows the Tokyo and Business Talk V4 pages already show current stock text and matching schema, the snippets were only cached. In that case close the stale-date part and keep only the auto-expiry process (steps 3 and 9).
2. Two to four weeks after the fixes, re-run 'site:gravipack.com précommande' and 'site:gravipack.com 2026'. If snippets still show 'juin 2026', 'mi-septembre 2026' or 'Early Bird … août', or the Rich Results Test still shows PreOrder or BackOrder on shipped products, the fix did not propagate.
3. If CTR in Search Console for the Tokyo and Business Talk V4 pages is flat over 28 days against the previous 28 days, stale text was not what held CTR down. That would confirm the low impact score, so do not escalate it.
- **Leading indicator to monitor:** Track these:
- Live products whose pre-order or shipping date is in the past: target 0, checked monthly with the WP-CLI command.
- Search Console clicks and CTR for the Tokyo and Business Talk V4 pages, comparing 28-day periods.
- Availability issues in Merchant Center and in the Search Console Merchant listings and Product snippets reports: target 0.
- New Trustpilot reviews mentioning 'retard' or 'livraison'.
- **To verify on-site:** For the Tokyo, Business Talk V4 20L, both Business Talk V4 25L, and Gravitech/Barracuda product pages, record:
- the visible availability or pre-order text and the WooCommerce stock status;
- Offer.availability, availabilityStarts and price in the Product JSON-LD, against the visible price, using the Rich Results Test and view-source;
- whether the 59,90 € Early Bird price is still active.

Also check:
- whether /etiquette-produit/precommande/ is indexable (meta robots) and which products it lists;
- whether single posts and the /actualites-gravipack-2/ listing show a visible date, and whether the Article or BlogPosting schema has matching datePublished/dateModified (SOFINS, Techterre and 'bientôt en magasin' posts);
- whether the presta 'commandes de réservation 2-3 mois' page is still live and indexed;
- Merchant Center diagnostics and the Search Console Merchant listings and Product snippets reports for availability or price mismatch warnings.

## AI Search Readiness

**Score:** **33/100** *(partial)* — Gravipack appears for niche "exosquelette / anti mal de dos" prompts (proxy 65) but is absent from broad informational and "meilleur…" prompts (proxy 12); no Wikidata/Wikipedia entity, inconsistent descriptors and entity facts (knowledge-graph-entity, exosquelette-definition-descriptor, entity-facts-consistency). Crawler access/llms.txt not observable.

**What works:**
- Distinctive, ownable category term ("sac à dos exosquelette")
- Official YouTube channel and LinkedIn page exist and rank for the brand

### 15. There is no single, consistent explainer for 'sac à dos exosquelette', and the brand describes its product several different ways

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | AI Search Readiness |

**Issue.** **1. The term is mostly about Gravipack already, but no Gravipack page defines it.**

We ran 'sac à dos exosquelette' twice in our search tool, which uses a US-located, non-Google index, so these are not Google.fr positions.

In the extended run, Gravipack holds 2 of the 9 results:
- #6, the catalogue category /categorie-produit/tous-les-sacs-a-dos-exosquelette/
- #7, the home page

Five more results are about Gravipack:
- #2, an i-trekkings test of the Oslo 70 L
- #4, an ergo-corner reseller brand page
- #5, compostelle-autrement ('Gravipack, le sac à dos en apesanteur')
- #8, the Decathlon marketplace Hiking 33 listing, titled '… Allège la charge de 92%'
- #9, a Google Patents result

Only two results are generic third parties:
- #1, kentfaith.fr 'Sac A Dos Exosquelette ?'. The search summary attributes sensors, automatic adjustment and army use to it.
- #3, alloprod.com

The standard run returned no gravipack.com URL. It showed the ffrandonnee.fr news item 'Une innovation : un exosquelette pour alléger le poids du sac à dos', Journal du Geek (2021), i-trekkings, Neozone (LEX) and three EPO patents.

The gap is narrower than 'third parties define the category'. Gravipack has no page that gives a quotable 'Un sac à dos exosquelette est…' definition. Search summaries also describe the mechanism in conflicting ways:
- 'inserts en carbone relevant les bretelles comme des pouces'
- 'armature métallique'
- transfer 'vers le centre de gravité'
- critics saying the load just moves to the lower back

The query 'sac à dos exosquelette c'est quoi' was never run.

Gravipack is the brand most associated with this category term. It did not invent the concept, because load-transferring pack exoskeletons predate it.

**2. Explainer-like content already exists, split across three posts:**
- www /evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/ ('L'évolution du portage de sac à dos jusqu'à la révolution Gravipack')
- www /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/ ('Et si votre sac à dos ne pesait presque plus rien ?')
- apex /inventeur-dun-sac-a-dos-en-apesanteur/ ('Le sac à dos en apesanteur anti-mal de dos allège le poids de 92%')

The last title says the bag's weight is reduced. That contradicts how the product works: the weight is unchanged and the load is transferred to the hips. Sceptics use exactly this point; forum.bushwalk.com (2024) notes that the 'weightless' bag weighs 890 g.

**3. The descriptors vary.**
- 'exosquelette': in 66 of the 98 sampled main-site titles.
- 'sac à dos en apesanteur': in 5 of the 16 legacy presta.gravipack.com titles (e.g. /73-gravipack 'Gravipack, le sac à dos en apesanteur qui ne fait pas mal au dos et aux épaules', /59-concours-lepine…, /plan-du-site-gravipack, the Road Adventure product). Also in the apex post above, the Facebook bio ('Sac a Dos en Apesanteur - Innovation Française') and the 2022 KissKissBankBank campaign slug.
- 'EVA ergonomique mémoire de forme': in the Compostelle survie 25 / 35 / 65 L titles and the 80 L slug.
- 'zero gravity backpack': on the YouTube channel.
- Efficacy wording also varies: 'allège le poids', 'allège la charge', 'réduire efficacement le poids'.

Correction to the phase-1 claim: the Compostelle 25 / 35 / 65 L titles do contain 'exosquelette', but only through the site-wide title suffix ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant'. That suffix appears on 13 of the 98 sampled titles. On 12 of them it is the only occurrence of 'exosquelette', including the three EVA bags. So the suffix suggests an exoskeleton on EVA products that may not have one (verify on-site).

No sampled Gravipack title uses 'anti-gravité'. 'Apesanteur' is a generic French word, not a competitor trademark. It only points towards a results page that others own: 'sac à dos anti gravité' is held by Osprey AG, Pearl Luna Gravity and similar products.

**4. Unrelated products are indexed.** They blur the entity only mildly:
- external solar battery (slug ends '-copie')
- paracord bracelet
- dragonne
- porte-clé flamme
- /produit/fabrication-professionnelle-gravipack/ ('fabrication professionnelle, cadeaux d'entreprise et objets publicitaires haut de gamme')

Selling accessories is normal. They just should not sit in the core exoskeleton categories.

**Evidence.** <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/> · <https://gravipack.com/> · <https://www.kentfaith.fr/blog/article_sac-a-dos-exosquelette_6410> · <https://www.alloprod.com/sac-a-dos-exosquelette/> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · <https://www.compostelle-autrement.com/post/gravipack-le-sac-a-dos-en-apesanteur> · <https://www.ffrandonnee.fr/s-informer/actualites/une-innovation-un-exosquelette-pour-alleger-le-poids-du-sac-a-dos> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · <https://www.gravipack.com/evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/> · <https://www.gravipack.com/et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/> · <https://gravipack.com/inventeur-dun-sac-a-dos-en-apesanteur/> · *(+8 more in findings/)*

**Why it matters.** When someone asks 'c'est quoi un sac à dos exosquelette ?' or 'comment ça marche ?', answer engines and featured snippets lift the clearest self-contained 'X est…' passage from a page that ranks. The source today is kentfaith, whose summarised claims about sensors and automatic adjustment do not describe Gravipack, or scattered press wording.

Using one stable descriptor everywhere ('Gravipack = sacs à dos à exosquelette') is what lets engines tie the brand to the term and say correctly which models have the exoskeleton. A clear statement that the bag's weight does not change also defuses the most common sceptical argument ('it weighs 890 g, it isn't weightless').

**Effect on SEO.** The page would capture the informational variants ('c'est quoi', 'comment ça marche', 'fonctionnement'), which currently return no Gravipack URL. It would also give AI Overviews, ChatGPT and Perplexity a quotable Gravipack definition and give product pages a strong supporting page to link to.

Consolidating three overlapping posts with 301 redirects merges their signals instead of splitting them. Aligning the descriptor and the title suffix removes mixed signals about which products have the exoskeleton.

Keep the catalogue category as the commercial target for the head term, and point the explainer at definitional intent, so the two pages do not compete.

**How to fix.**

1. **Assign roles to the URLs.**
   - Keep /categorie-produit/tous-les-sacs-a-dos-exosquelette/ as the commercial target for 'sac à dos exosquelette'. It already ranks.
   - Create one explainer page for definitional and how-it-works intent.
   - Each page links to the other: the category intro says « Comment fonctionne l'exosquelette ? », and the explainer says « Voir tous les sacs à dos exosquelette ».

2. **Consolidate the existing posts. Do not add a fourth.**
   - In Search Console (Performance and Links), note clicks, queries and backlinks for /evolution-du-portage…/, /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/ and /inventeur-dun-sac-a-dos-en-apesanteur/.
   - Build a WordPress Page, e.g. /sac-a-dos-exosquelette-fonctionnement/, on the host the host-consolidation fix keeps as canonical. Merge any unique sections into it, for example the carrying-history part.
   - 301 the posts whose main topic is 'how it works' to it, using Rank Math → Redirections, Yoast Premium → Redirects or the Redirection plugin (exact match, 301). Server-level alternatives:
   ```apache
   # .htaccess, avant le bloc WordPress
   RewriteEngine On
   RewriteRule ^inventeur-dun-sac-a-dos-en-apesanteur/?$ https://gravipack.com/sac-a-dos-exosquelette-fonctionnement/ [R=301,L]
   RewriteRule ^et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/?$ https://gravipack.com/sac-a-dos-exosquelette-fonctionnement/ [R=301,L]
   ```
   ```nginx
   location = /inventeur-dun-sac-a-dos-en-apesanteur/ { return 301 https://gravipack.com/sac-a-dos-exosquelette-fonctionnement/; }
   ```
   - If the 'évolution du portage' post earns links on its own, keep it as a history article that links to the explainer.
   - Update internal links with Better Search Replace so that none goes through a redirect.

3. **Write the page answer-first.**
   - Title tag: « Sac à dos exosquelette : comment ça marche ? | Gravipack » (about 55 characters).
   - H1: « Sac à dos exosquelette : définition et fonctionnement ».
   - Definition box in the first 60 words:
     > « Un sac à dos exosquelette est un sac dont les bretelles intègrent une structure rigide passive, sans moteur ni capteur. Chez Gravipack, des inserts rigides intégrés aux bretelles reportent une partie de la charge des épaules vers les hanches, par l'intermédiaire de la ceinture. Le poids du sac ne change pas : c'est la répartition de la pression qui change. »
   - Add « brevetés » and the publication number once the patents fix confirms them.
   - Then add these H2 sections, written as questions:
     - « Comment fonctionne l'exosquelette ? », with a force-path diagram: shoulders → inserts → hip belt.
     - « Le sac est-il plus léger ? ». Answer no, and give the empty weight of each model in grams, plus the weight the inserts add.
     - « Ce que l'exosquelette ne fait pas »: no motor, no sensors, no automatic adjustment, no weight removed. Say where the load goes; this answers the lower-back critique.
     - « Quels modèles Gravipack sont équipés ? »
     - « Sac classique, dos tendu en filet (type Osprey Anti-Gravity) ou exosquelette : quelles différences ? ». Use a factual table: where the load passes, empty weight, adjustment, ventilation. Naming Osprey here is acceptable nominative use.
     - « Brevets et distinctions ». Use only facts the patents and awards fixes have sourced. Verify the Concours Lépine silver medal year; the legacy page gives none and the press says 2018.
   - Quote measured results only by linking to the evidence page (study fix). Do not repeat '-92 %' here.
   - Embed the existing 'Exosquelette breveté Gravipack sac a dos - Vidéo 3D' (homKGDpmhOA) and link the bretelles adjustment guide.
   - Meta description: « Qu'est-ce qu'un sac à dos exosquelette ? Définition, fonctionnement des inserts dans les bretelles, ce que l'exosquelette fait (et ne fait pas) et modèles équipés. »
   - Schema: the Article (or WebPage) and BreadcrumbList that Yoast or Rank Math generates, with author, datePublished and a visible dateModified.

4. **Link it from every product page that has the exoskeleton.**
   - Use a global product tab (`woocommerce_product_tabs` filter or a custom-tabs plugin) or a line in the short description: « Comment fonctionne l'exosquelette Gravipack → ».
   - Also link it from the use-case category intros and /faq/.

5. **Adopt one canonical descriptor** and use it verbatim in the About page, Organization `description`, category intros, marketplace brand text, the press kit and the YouTube, Facebook, Instagram and LinkedIn bios:
   > « Gravipack est une marque française de sacs à dos dont les bretelles intègrent un exosquelette qui reporte une partie de la charge des épaules vers les hanches. »
   - Stop using « apesanteur » as a product descriptor on owned pages. The presta pages are handled by the legacy-subdomain 301s. Update the Facebook bio.
   - Ask the Decathlon seller to drop « Allège la charge de 92% » from listing titles; that goes through the licensee and health-claims fixes.

6. **Fix the misleading title suffix** in the titles fix. It looks like the WordPress or Yoast 'Site name' is set to « Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant ». Set it to « Gravipack » (Yoast → Réglages → Paramètres du site, or Rank Math → Titres & méta) and use `%%title%% %%sep%% %%sitename%%` (Rank Math: `%title% %sep% %sitename%`).

7. **Make exoskeleton status explicit per product.**
   - Add a WooCommerce attribute (Produits → Attributs) « Technologie de portage » with the terms « Exosquelette » and « Sans exosquelette (bretelles EVA à mémoire de forme) ».
   - Tick 'Visible on product page' and leave 'Enable archives' off, to avoid creating another thin attribute archive.
   - Products without inserts come out of the 'tous-les-sacs-a-dos-exosquelette' tree.

8. **Move off-entity items into the existing accessories category.**
   - Battery, paracord bracelet, dragonne and porte-clé go to /categorie-produit/accessoires-sac-a-dos/ or a sub-category « Équipement outdoor ». Fix their '-copie' slugs in the duplicate-products fix.
   - Turn 'fabrication professionnelle / cadeaux d'entreprise' into a B2B page (B2B fix) and 301 the product URL to it.

- **First principle:** Answer engines quote the most self-contained definition passage among the pages that rank. An entity is only as clear as the one sentence that is repeated about it across sources. Gravipack ranks for the term, but no page's job is to define it, and its own pages use several descriptors.
- **Do first:** `titles-template-suffix`, `canonical-host-consolidation`, `study-evidence-page`, [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), `patents-trademark-citation`, [#16 The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages](#16-the-legacy-prestashop-store-prestagravipackcom-still-appears-in-search-results-with-old-product-study-and-award-pages)
- **How we'll know the fix failed:** The fix has failed if any of these holds:
- 8–12 weeks after publication, the new page has no Search Console impressions for queries that combine 'exosquelette' with 'c'est quoi', 'comment', 'fonctionne' or 'définition'.
- AI answers to « c'est quoi un sac à dos exosquelette ? » still describe sensors or automatic adjustment, or still do not cite Gravipack.
- The category's average position for 'sac à dos exosquelette' drops after launch. That means the two pages are cannibalising each other, and the explainer should be re-targeted to purely informational wording.
- **Leading indicator to monitor:** - In Search Console, filter Performance to the new URL and to queries containing 'exosquelette': track impressions and average position, and check that the old post URLs fall to zero.
- Run a monthly prompt panel of 5 definitional prompts in ChatGPT search, Perplexity, Google AI Mode and Copilot. Log whether Gravipack is cited and whether the answer says the weight is unchanged.
- **To verify on-site:** - Read the three posts: word count, unique sections and inbound links (Search Console Links report).
- Check whether the 'tous les sacs à dos exosquelette' category has intro text above the product grid.
- Confirm which Compostelle / EVA models actually contain the inserts.
- Check the current Yoast or Rank Math site name and title templates, and whether any products override them.
- After launch, run curl -sI on each old URL to confirm a single-hop 301 to the canonical host.

### 25. No Wikidata or Wikipedia entity exists for Gravipack; searches return only lookalike brands

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Low | likely | AI Search Readiness |

**Issue.** **No entry on Wikidata, Wikipedia or Crunchbase.** A search for 'Gravipack' restricted to wikipedia.org, wikidata.org and crunchbase.com returned only lookalikes:
- Crunchbase: gravitas-packaging, grinpack, gravic, gpack
- Wikipedia: Greif, Gravity Payments, Gravit, Graphic Packaging, Grav (software), Gravitar

None of the 33 phase-2 result sets, and none of about 60 phase-1 sets, contained a Gravipack page on those domains. This is absence evidence from a non-Google search tool, so confidence is 'likely'. Whether a Google knowledge panel exists could not be observed.

**Name collisions make disambiguation harder:**
- 'Mohammed Errafi Gravipack LinkedIn' returned the packaging firm Gravis (cbinsights, dealroom, preqin) and gracepack.
- A phase-1 query returned unrelated Wikipedia namesakes (Mohammed Al-Rufrafi, Mohammed Errafai).
- A YouTube search showed an unrelated 'Zero Gravity™' channel (UC-yPO91aYTm4g886iApv-vw) next to the official channel, whose display name is 'Gravipack zero gravity backpack'.
- An unrelated Instagram account, @granipack (26K), sits next to @gravipack.

**Entity sources that do exist:**
- the LinkedIn company page fr.linkedin.com/company/gravipack. It ranked #2 for 'gravipack' in one sampled run and dropped out in a re-run, because brand results were volatile across runs.
- the founder's profile linkedin.com/in/errafi/
- the YouTube channel @Gravipack, plus Instagram and Facebook
- registry pages: annuaire-entreprises.data.gouv.fr, societe.com, Pappers, rubypayeur
- Les Pépites Tech, and the directory motherbase.ai (my.motherbase.ai/startup/107826-gravipack, which shows Vincennes and 'created 2018')

Phase 1 described motherbase.ai as 'AI-generated'; that is unverified and is dropped here. Phase 1 also said 'no LinkedIn'; that is wrong and dropped.

These profiles disagree with each other:
- LinkedIn shows a '201-500 employees' band, while its structured data says 5 employees.
- LinkedIn gives the HQ as Vincennes, Facebook says Sens, and the mentions légales say Paris.

So there is no neutral, referenced record for engines to settle on.

**Registry facts available for a referenced record:**
- Legal entity: EXOSQUELETTE LIGHT SAS, SIREN 840 543 383, NAF 77.40Z.
- Created 12/06/2018 in Sens (89) as GRAVIBAG.
- Renamed GRAVIPACK on 01/07/2022, and EXOSQUELETTE LIGHT by an AGE of 02/01/2025 (BODACC of 28/02/2025).
- Seats: Sens 2018–2022; 46 rue de la Bienfaisance, 94300 Vincennes, 2022–2026; 10 rue de la Paix, 75002 Paris, since 19/05/2026.
- President and founder: Mohammed Errafi.
- Independent coverage: franceinfo, France Bleu (ici), Europe 1, Journal du Geek (2021), Maddyness (Feb 2024), and the INPI Trophées 2022 finalist page.

The patent part of the phase-1 finding moves to the patents finding.

A missing Wikipedia article is normal for a company of this size and is not a ranking factor in itself.

**Evidence.** <https://www.crunchbase.com/organization/gravitas-packaging> · <https://www.crunchbase.com/organization/gpack> · <https://en.wikipedia.org/wiki/Gravit> · <https://en.wikipedia.org/wiki/Mohammed_Errafai> · <https://www.youtube.com/channel/UC-yPO91aYTm4g886iApv-vw> · <https://www.youtube.com/@Gravipack> · <https://fr.linkedin.com/company/gravipack> · <https://www.linkedin.com/in/errafi/> · <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383> · <https://rubypayeur.com/societe/gravipack-840543383> · <https://my.motherbase.ai/startup/107826-gravipack> · <https://lespepitestech.com/startup-de-la-french-tech/gravipack>

**Why it matters.** Wikidata is a structured, referenced source that knowledge graphs and LLM retrieval use to resolve a name to one entity. claude-seo's seo-geo lists Wikipedia and Wikidata presence among the strongest AI-citation signals; Profound (2025) reports that Wikipedia is 47.9 % of ChatGPT's top-10 cited sources.

Without such a record, engines describe Gravipack from directories and its own profiles, which conflict on HQ, company name and headcount. The 'Grav*' lookalikes and the 'Zero Gravity' channel also add noise.

It is an AI-visibility and brand-SERP opportunity, not a ranking fix, hence Medium.

**Effect on SEO.** A referenced Wikidata item with consistent identifiers gives Organization `sameAs` an authoritative anchor. It improves the odds of a knowledge panel for 'gravipack' and of correct facts in AI answers: legal name, HQ, founding year, official site.

It also helps AI answers separate Gravipack from Gravis, Gravitas Packaging and the 'Zero Gravity' channel.

**How to fix.**

1. **Settle the facts first.** Use the master fact sheet from the entity-facts fix: legal name, current seat and canonical domain. Never present Vincennes as the current seat.

2. **Check for existing items.** Search Wikidata for « Gravipack », « Gravibag » and « Exosquelette Light » to avoid creating a duplicate.

3. **Edit transparently.** Use a named account. On its user page, disclose the conflict of interest (« Je représente Gravipack / EXOSQUELETTE LIGHT SAS »), following Wikidata's COI guidance. Keep wording neutral, and add no claims such as 'anti mal de dos', '92 %' or a patent count.

4. **Create the item.**
   - Label fr/en « Gravipack ».
   - Description fr « marque française de sacs à dos à exosquelette », en « French backpack brand with a load-transferring exoskeleton in the shoulder straps ».
   - Aliases « EXOSQUELETTE LIGHT », « GRAVIBAG ».
   - Statements. Check every property and Q-id in the Wikidata interface before saving.
     - P31 instance of = business (Q4830453). A separate brand item (Q431289) linked to the company is optional later.
     - P17 country = France (Q142).
     - P571 inception = 12 June 2018.
     - P1448 official name, with P580 start / P582 end qualifiers: « GRAVIBAG » (2018-06-12 → 2022-07-01), « GRAVIPACK » (2022-07-01 → 2025-01-02), « EXOSQUELETTE LIGHT » (from 2025-01-02).
     - P159 headquarters location:
       - Sens: start 2018, end 2022.
       - Vincennes: start 2022, end 2026-05-19.
       - Paris (Q90): start 2026-05-19, preferred rank, with P6375 street address « 10 rue de la Paix, 75002 Paris ».
     - P112 founded by = Mohammed Errafi. Link a person item only if one exists or can be created with independent references (inventor coverage). Otherwise leave it out rather than create a thin item.
     - P856 official website = the canonical URL.
     - P1616 SIREN = 840543383.
     - P2003 Instagram username = gravipack.
     - P2013 Facebook username = gravipack.
     - P4264 LinkedIn company ID = gravipack.
     - P2397 YouTube channel ID = the official channel's UC… ID, taken from YouTube Studio → Paramètres → Chaîne → Paramètres avancés. Not UC-yPO91aYTm4g886iApv-vw, which is the unrelated 'Zero Gravity™' channel.
     - P166 award received: only for awards the awards fix confirms with an independent source.
   - References: add a P854 reference URL and P813 retrieval date to every statement, citing independent sources. Use annuaire-entreprises.data.gouv.fr or BODACC for registry facts, and INPI, Journal du Geek, Maddyness, France Bleu and Europe 1 for the rest. Never cite gravipack.com alone.

5. **Align the other profiles.**
   - Create or claim a Crunchbase organisation profile with the same facts: legal name, founded 2018, HQ Paris, canonical website, LinkedIn.
   - Correct the LinkedIn page: HQ Paris 75002, a real employee band instead of 201-500, the canonical website.

6. **Add the Wikidata URL to Organization `sameAs`.** The Organization finding owns the full markup. In Yoast: Réglages → Représentation du site → Autres profils. Or use a filter:
   ```php
   add_filter( 'wpseo_schema_organization', function ( $data ) {
       $data['sameAs'][] = 'https://www.wikidata.org/wiki/Q_____'; // ID de l'élément créé
       return $data;
   } );
   ```
   Rank Math: Titres & méta → Référencement local → profils sociaux, or the `rank_math/json_ld` filter. Use only profiles that represent the entity: Wikidata, LinkedIn, YouTube, Instagram, Facebook. Do not list Trustpilot, the Decathlon brand page or KKBB.

7. **Leave Wikipedia for later.** Do not write a French Wikipedia article now. Notability for companies requires at least two independent, centred, national secondary sources published at least two years apart. The 2021 and 2024 coverage may get there, but an article should come from independent editors, or carry the mandatory COI disclosure.

8. **Claim the knowledge panel** if one appears for 'Gravipack', using Google's verification flow with an account tied to the official site or YouTube channel. Create a Google Business Profile only for a staffed, customer-facing address (local fix).

- **First principle:** Knowledge graphs and LLMs resolve a name by matching it to a structured, referenced record. Where no record exists, 'Gravipack' gets resolved by resemblance to better-documented lookalikes and by whichever directory profile happens to rank.
- **Do first:** [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards), `canonical-host-consolidation`, `organization-schema-legal-identity`, [#32 Awards are real but under-sourced, and the army and special-forces claims rest on founder statements and undated owned posts](#32-awards-are-real-but-under-sourced-and-the-army-and-special-forces-claims-rest-on-founder-statements-and-undated-owned-posts)
- **How we'll know the fix failed:** The fix has failed if any of these holds:
- The Wikidata item gets a deletion request or is merged within the first month. That means the references were not independent enough.
- Three months after creation, the Google Knowledge Graph Search API (kgsearch.googleapis.com, query 'Gravipack') still returns no Gravipack entity.
- AI answers to « Qui a fondé Gravipack et où est basée l'entreprise ? » still give Sens or Vincennes as current, or confuse Gravipack with Gravis or Gravitas Packaging.
- **Leading indicator to monitor:** - The Wikidata item stays live with no deletion request, and other editors add statements to it.
- A Knowledge Graph Search API result for 'Gravipack' appears, with its resultScore tracked monthly.
- In a monthly AI prompt panel, the share of answers that give the correct legal name, HQ and founding year goes up.
- A knowledge panel appears on 'gravipack' brand searches.
- **To verify on-site:** - Check whether the site already outputs Organization JSON-LD and what its `sameAs`, `legalName` and address contain (view-source plus Rich Results Test).
- Check that the mentions légales name EXOSQUELETTE LIGHT SAS at 10 rue de la Paix, 75002 Paris.
- Copy the exact YouTube channel ID from YouTube Studio.
- Before creating the item, confirm that no Wikidata item exists under any former name.

### 31. AI and search crawler access, server rendering, Bing coverage and llms.txt need an on-site check

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | AI Search Readiness |

**Issue.** Nothing in this finding could be checked. The sandbox network policy blocked:
- robots.txt on every host (gravipack.com, www.gravipack.com, presta.gravipack.com, gravipack.fr)
- response headers and WAF / CDN behaviour
- the rendered versus raw HTML
- /llms.txt

The PageSpeed Insights / Lighthouse run also failed, with HTTP 429 (quota), recorded in scratchpad data/psi_fr_mobile.json. No Bing Webmaster Tools data was available.

What is known:
- The site is WordPress + WooCommerce: /produit/, /categorie-produit/ and ?add-to-cart= URLs are indexed. WooCommerce is usually server-rendered, but page builders, AJAX-loaded tabs and JS sliders can keep product text out of the initial HTML.
- The mentions légales name Gandi as the host. Whether a CDN or WAF sits in front is unknown.
- Search results show no sign either way about llms.txt.

The severity is a placeholder. Escalate it to **Critical** if robots.txt or the WAF blocks Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot or PerplexityBot on the canonical host. Escalate it to **High** if product descriptions, prices or FAQ answers appear only after JavaScript runs.

**Evidence.** <https://gravipack.com/> · <https://www.gravipack.com/> · <https://presta.gravipack.com/73-gravipack> · `/tmp/claude-0/-home-user-soufian/f48d95be-0ad3-5e07-bab2-7b53bc671068/scratchpad/data/psi_fr_mobile.json`

**Why it matters.** An engine can only cite pages its search crawler is allowed to fetch and can read in the HTML. Each crawler controls a different engine:
- **Search and answer crawlers (must be allowed):** OAI-SearchBot (ChatGPT search), Claude-SearchBot (Claude search), PerplexityBot (Perplexity), Googlebot (Search, AI Overviews and AI Mode) and Bingbot (Bing and Copilot).
- **Training-only tokens (a business choice; they do not affect citation):** GPTBot, ClaudeBot, Google-Extended, CCBot and Applebot-Extended.

llms.txt is optional:
- It carries zero weight in claude-seo's GEO score.
- Google's AI optimisation guide says Google Search ignores it, and no major AI search provider has confirmed using it.
- Lighthouse has an llms-txt audit, but a missing file is reported as informational only.

**Effect on SEO.** If a search crawler is blocked, or the content is injected by JavaScript, that engine cannot cite the site at all. If access is open and the HTML is server-rendered, nothing here limits visibility.

Bing coverage matters because Copilot draws on the Bing index. llms.txt has no expected effect on Google; at most it might help a little with non-Google agents.

**How to fix.**

1. **Read robots.txt on every host.**
   ```bash
   for h in gravipack.com www.gravipack.com presta.gravipack.com gravipack.fr; do echo "== $h"; curl -s https://$h/robots.txt; done
   ```
   - List each user-agent group separately.
   - Remember that a named group replaces `User-agent: *` entirely for that bot (RFC 9309), so rules in `*` do not reach a bot that has its own group.
   - A 5xx on robots.txt makes compliant crawlers treat the whole site as disallowed.

2. **Edit robots.txt** in Yoast (Outils → Éditeur de fichiers), in Rank Math (Réglages généraux → Modifier robots.txt) or as a physical file.
   - Do not disallow the search crawlers.
   - Blocking training crawlers is optional and is the owner's decision. Example:
   ```
   User-agent: *
   Disallow: /wp-admin/
   Allow: /wp-admin/admin-ajax.php

   # Facultatif : refuser l'entraînement des modèles (choix commercial)
   User-agent: GPTBot
   User-agent: ClaudeBot
   User-agent: Google-Extended
   User-agent: CCBot
   User-agent: Applebot-Extended
   Disallow: /

   Sitemap: https://gravipack.com/sitemap_index.xml
   ```
   - Parameter rules for ?add-to-cart= and ?order= follow the parameter-URL fix's order: noindex first, Disallow only later.
   - Optionally add a `Content-Signal: search=yes, ai-input=yes, ai-train=<choix>` line inside each group. This is a Cloudflare policy with no confirmed effect on Google.

3. **Test the WAF by user agent.**
   ```bash
   for ua in Googlebot bingbot OAI-SearchBot Claude-SearchBot PerplexityBot; do printf '%-18s' $ua; curl -s -o /dev/null -w '%{http_code}\n' -A "Mozilla/5.0 (compatible; $ua)" https://gravipack.com/produit/<slug>/; done
   ```
   - Each should return 200, with no challenge page.
   - Spoofing the user agent only tests rules based on user agents. Also check the server or WAF logs for real, verified crawler IPs (openai.com/searchbot.json, claude.com/crawling/bots.json, perplexity.com/perplexitybot.json, Google and Bing reverse DNS). Do not IP-block Anthropic's or OpenAI's crawlers, and keep CAPTCHAs off content pages.
   - The response headers (`server`, `cf-ray`, etc.) show whether a CDN or WAF is in front of the site.

4. **Confirm that content is in the server HTML.**
   - Run `curl -s https://gravipack.com/produit/<slug>/ | grep -c 'exosquelette'` and check that the product description, price and FAQ answers are present without JavaScript.
   - In Search Console, use URL Inspection → Tester l'URL en direct → Afficher la page explorée.
   - Or run claude-seo `render_page.py --mode auto` and `agentic_check.py`.

5. **Search Console:** check that the 'Search generative AI' property setting, available to all sites since 31/08/2026, is left on 'include', the default. Do not use the Indexing API; it only covers JobPosting and BroadcastEvent pages.

6. **Bing Webmaster Tools.**
   - Import the property from Search Console, or verify by DNS (there is no 'Domain property' type).
   - Submit the canonical sitemap and check coverage of the canonical host.
   - Enable IndexNow through Rank Math → Instant Indexing or Microsoft's IndexNow plugin.

7. **Optionally, and last**, publish /llms.txt at the root of the canonical host. Present it as a convenience for non-Google agents, never as a ranking lever.
   ```
   # Gravipack
   > Marque française de sacs à dos dont les bretelles intègrent un exosquelette qui reporte une partie de la charge des épaules vers les hanches. Société : EXOSQUELETTE LIGHT SAS, Paris.

   ## Comprendre
   - [Sac à dos exosquelette : comment ça marche ?](https://gravipack.com/sac-a-dos-exosquelette-fonctionnement/)
   - [FAQ](https://gravipack.com/faq/)
   - [Régler les bretelles exosquelette](https://gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/)

   ## Produits
   - [Tous les sacs à dos exosquelette](https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/)

   ## Entreprise
   - [À propos](https://gravipack.com/a-propos-de-nous-gravipack-au-service-de-votre-dos/)
   ```
   - Make sure unknown URLs return a real 404, not a soft-404 200. A catch-all 200 also fails Lighthouse's llms-txt audit.

8. **Once quota allows,** run Lighthouse's Agentic Browsing category and report the result as X/N passed audits.

- **First principle:** Citation requires the engine's own search crawler to be allowed to fetch the page and to find the text in the HTML. Training-crawler rules do not affect citation. Google Search does not read llms.txt.
- **Do first:** `canonical-host-consolidation`, [#29 Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=)](#29-cart-sort-and-filter-parameter-urls-appear-in-the-index-add-to-cart-order-filter_product_cat)
- **How we'll know the fix failed:** The fix has failed if any of these holds:
- 30 days after the check, access logs or CDN analytics show no hits, or 403 and challenge responses, from verified OAI-SearchBot, Claude-SearchBot, PerplexityBot or Bingbot.
- Bing Webmaster Tools shows that most canonical sitemap URLs are not indexed.
- Search Console's 'Afficher la page explorée' HTML for a product page lacks the description or price.
- **Leading indicator to monitor:** - Monthly count of verified search-crawler requests by status code in the server logs.
- Search Console crawl stats by response code.
- Bing Webmaster Tools indexed-page count.
- GA4 sessions referred by chatgpt.com, perplexity.ai, copilot.microsoft.com and claude.ai.
- **To verify on-site:** - robots.txt on all four hosts.
- curl status codes per bot user agent, plus WAF or CDN firewall events for verified bots.
- Response headers, to identify the CDN or WAF.
- Raw versus rendered HTML of one product page, one category page and /faq/.
- The Search Console 'Search generative AI' setting.
- Bing Webmaster Tools coverage and IndexNow status.
- Whether /llms.txt exists, and whether a random URL returns 404.

### 34. FAQ and category intros may not be written as self-contained answers (verify on-site)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | AI Search Readiness |

**Issue.** This is a hypothesis to verify, not a confirmed defect.

**What is indexed:**
- /faq/ on the www host, titled 'Foire Aux Questions des sacs à dos exosquelettes Gravipack' (58 characters). Search summaries say it covers sizing and custom fitting by height and weight, and cabin baggage. One summary quotes it as saying the bag « évacue jusqu'à 92 % de la charge ». That figure comes from an unpublished study and is stated inconsistently as weight, load or pressure; the study and health-claims findings deal with it.
- The how-to /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/, which ranked #1 for a site-restricted sizing and adjustment query.
- Product pages, which say each bag is personalised free of charge to the buyer's height and weight (±10 cm / ±8 kg). That is citable fit information that could be stated once, clearly.

**What we could not see:**
- the heading levels, answer lengths and order of the FAQ
- whether answers load in the HTML or through JavaScript accordions
- whether the use-case category pages have intro text

In the sampled results, 0 of 25+ informational queries returned a gravipack.com URL, so these pages are not yet being picked up for question-type searches.

**Evidence.** <https://www.gravipack.com/faq/> · <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/>

**Why it matters.** In claude-seo's seo-geo scoring, citability counts for 25 % and structural readability for 20 %, so 45 % of the GEO score. Both reward:
- question-style H2/H3 headings
- a direct answer in the first 40–60 words
- passages that make sense on their own
- key answers near the top (SE Ranking finds about 44 % of AI citations come from the first 30 % of a page)

Google says content does not need to be chunked for AI. Clear Q&A simply serves readers and answer engines alike.

FAQ rich results are not available to Gravipack. Google restricted them to authoritative government and health sites in August 2023, and claude-seo's schema reference records them as retired for all sites from 7 May 2026. So the value of this work is users and AI citability, not a SERP feature.

**Effect on SEO.** Well-structured answers raise the chance that Gravipack's own wording is quoted in AI Overviews, ChatGPT, Perplexity and Copilot for 'gravipack' + question searches (weight, adjustment, sizing, where to buy) and for category questions. Without them, these answers come from forums and marketplace reviews.

It also stops the FAQ from being the quoted source of a figure that is not yet substantiated.

**How to fix.**

1. **Restructure /faq/ into themed sections:** Fonctionnement, Choisir et régler, Commande et garantie.
   - One H2 per theme and one H3 per question, written the way users ask.
   - Answer in 40–60 words that make sense on their own, then add detail.
   - Put the most-asked questions in the top third of the page, and add a jump-link table of contents.

2. **Keep answers in the initial HTML.**
   - Native `<details><summary>` or Gutenberg heading + paragraph blocks are fine.
   - Avoid accordions that load answers by AJAX on click (check with curl or Search Console URL Inspection).

3. **Example answers** (fill in the bracketed facts):
   - **« Le sac Gravipack est-il plus léger qu'un sac classique ? »**
     > « Non. L'exosquelette ne réduit pas le poids du sac : un Gravipack pèse [X g] à vide. Les inserts rigides intégrés aux bretelles reportent une partie de la charge des épaules vers les hanches, par la ceinture. Le poids total reste le même ; c'est la répartition de la pression qui change. »
   - **« Comment choisir et régler mon Gravipack ? »**
     > « Chaque sac est personnalisé gratuitement selon votre taille et votre poids (tolérance ±10 cm / ±8 kg) [vérifier]. À réception, réglez la ceinture sur les hanches, puis les bretelles et le rappel de charge : suivez notre guide pas à pas et sa vidéo. »
     Link the bretelles guide here.
   - **« Comment fonctionne l'exosquelette ? »**: a two-sentence summary linking to the 'sac à dos exosquelette' explainer.
   - **« Où acheter Gravipack ? »**: list the official channels, as in the where-to-buy finding.
   - **« Quelle garantie ? »**: state the current CGV terms. Do not reuse the crowdfunding-era '10 ans' unless it still applies.

4. **Claim-sensitive questions.**
   - « Que signifie le chiffre de 92 % ? »: publish only after the evidence page exists. Say what was measured (pressure or load), by whom, when and on how many people, and link the source. Until then, remove « évacue jusqu'à 92 % de la charge » (study and health-claims findings).
   - « Le sac Gravipack est-il remboursé ? »: include only if reimbursement is real and documented. Phase 2 found no LPP listing, and the source behind the claim describes employer funding. If there is no documentation, leave the question out.

5. **Category intros.** Open each use-case category with a 40–60-word answer-first paragraph above the product grid. For the hiking category:
   > « Les sacs à dos de randonnée Gravipack intègrent un exosquelette dans les bretelles qui reporte une partie de la charge vers les hanches. Ils existent en [volumes] et se règlent selon votre taille. »
   Add 3–5 short Q&As below the grid. Edit the category description in WooCommerce → Produits → Catégories; if the theme shows descriptions only below the grid, use the theme's category-header option or a hook.

6. **Markup.**
   - The Yoast or Rank Math FAQ blocks output FAQPage markup automatically. Existing FAQPage markup can stay; it is harmless and worth only an Info note. Do not add it expecting a rich result.
   - Keep the BreadcrumbList and WebPage markup the plugins generate.
   - Show a visible 'Mis à jour le' date.

- **First principle:** Answer engines lift passages that answer a question without needing their surroundings. FAQ answers that depend on context, are hidden behind JavaScript, or repeat an unsupported figure either cannot be quoted or end up as the quoted source of that figure.
- **Do first:** `study-evidence-page`, [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), [#15 There is no single, consistent explainer for 'sac à dos exosquelette', and the brand describes its product several different ways](#15-there-is-no-single-consistent-explainer-for-sac-à-dos-exosquelette-and-the-brand-describes-its-product-several-different-ways), [#31 AI and search crawler access, server rendering, Bing coverage and llms.txt need an on-site check](#31-ai-and-search-crawler-access-server-rendering-bing-coverage-and-llmstxt-need-an-on-site-check)
- **How we'll know the fix failed:** The fix has failed if either of these holds:
- 8–12 weeks after the rewrite, Search Console shows no rise in question-form queries ('gravipack' plus comment, est-ce que, combien, régler, taille) landing on /faq/ and the category pages.
- The monthly AI prompt panel ('Le sac Gravipack est-il plus léger ?', 'Comment régler un sac Gravipack ?') still quotes forum or marketplace text rather than the FAQ wording.
- **Leading indicator to monitor:** - Search Console impressions and clicks on /faq/ and the category URLs for question-type queries.
- GA4 landing-page sessions on /faq/ from AI referrers (chatgpt.com, perplexity.ai, copilot.microsoft.com).
- How often the monthly AI prompt panel cites the FAQ.
- **To verify on-site:** - View the raw HTML of /faq/: H2/H3 levels, whether the answers are present without JavaScript, answer word counts, and where '92 %', 'remboursé' and 'Sécurité sociale' appear.
- Check whether category pages have intro text above the product grid.
- Check whether FAQPage markup is already emitted (Rich Results Test).
- Confirm the current warranty and personalisation terms in the CGV and on product pages.

### 42. The YouTube channel is named 'zero gravity backpack' and uses medical wording; the social and community footprint is small or stale

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Medium | likely | AI Search Readiness |

**Issue.** **YouTube: the channel exists and ranks. Its name and description are the problem, not its size.**

In the 'gravipack' results we sampled, youtube.com/@Gravipack and /c/Gravipack ranked #3–#4 in one run and #2–#3 in a re-run; positions were volatile. Phase-1 claims of 'no YouTube presence' and a 'missing video list' are withdrawn.

The channel already has playlists: 'Contenants des sacs à dos Gravipack', 'Gravipackers : militaires, randonneurs, jacquets, enfants' and 'Les Exosquelettes Gravipack'.

It also has per-model and B2B videos:
- Tokyo (stVloflCKp8)
- Rome (XWKZ-PsU-VE)
- Light Promax (5rGu1ntLvRw)
- MedMax for pompiers and urgentistes (5RNn93sinxo)
- RATPLovesStartUp (1Xq8EKyINTw)
- a 3D exoskeleton video (homKGDpmhOA)
- a founder interview (V0CuNW4N9Q8)
- a school-bag video (aqvti5NwaE0)
- a user testimonial (O_9o6-6tw4s)

TV and third-party videos also rank:
- C8 'William à midi', June 2024 (rhduWNbpPko)
- Samuel Etienne (5DELA6ARIIc)
- 'JE TESTE UN SAC À DOS AVEC DES EXOSQUELETTES - GRAVIPACK' (7AsOwX_9R2w, owner unknown)
- 'Ce Sac est à Avoir !' (Z0eU4T6bNHE)

The newest indexed upload dates from about mid-June 2025, so nothing has been indexed for roughly 16 months. The channel's structured data shows an unlabelled count of 766; it is unclear what it measures, so we do not call the channel small.

What still needs fixing:
- The display name 'Gravipack zero gravity backpack' clashes with the 'exosquelette' descriptor. It also sits next to an unrelated 'Zero Gravity™' channel in results.
- The channel description cites a 2019 'étude scientifique et médicale' and frames the bag as a preventive health device. How to substantiate that belongs to the study and health-claims findings.

Decathlon Hiking 33 reviewers say adjustment is difficult. The site has /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/, which ranked #1 for a site-restricted sizing and adjustment query. Search summaries mention a settings PDF and an adjustment video linked from product pages, but whether that video exists and is embedded is unconfirmed.

**Other social profiles:**
- **Facebook:** about 2,440 followers and 2,161 likes (two captures). The bio reads 'Sac a Dos en Apesanteur - Innovation Française' and the page places the brand in Sens. Older posts use the 'Atlas 33' model name. It hosts BFM TV and 'testé et approuvé par la FNAC' videos and has a /reviews/ tab.
- **Instagram @gravipack:** about 23K followers and 196 posts, but that is a snapshot from around March 2023, not a current figure. An unrelated lookalike, @granipack (26K), exists.
- **LinkedIn company page:** 1,850–1,884 followers. The latest indexed company post is from 27/09/2023 and the founder's from 14/10/2023. Social posts are only partly indexed, so this does not prove inactivity.
- **TikTok and Pinterest:** no account found in generic or domain-filtered searches. Both are poorly indexed, so absence does not prove the brand has no account.

**Community:**
- Two open-web queries returned no reddit.com URL: 'gravipack reddit' and 'Gravipack backpack exoskeleton straps review reddit'. The tool cannot search reddit.com directly, so this is absence evidence only.
- The community discussion that does surface is randonner-leger.org (e.g. pid 626046 and 626048, thread id=37663) and forum.bushwalk.com (2024, sceptical: the 'weightless' bag weighs 890 g, the waist belt does the work, 'just another con').
- For a French niche brand, a Reddit gap is normal.

**Evidence.** <https://www.youtube.com/@Gravipack> · <https://www.youtube.com/c/Gravipack/videos> · <https://www.youtube.com/channel/UC-yPO91aYTm4g886iApv-vw> · <https://www.youtube.com/watch?v=stVloflCKp8> · <https://www.youtube.com/watch?v=XWKZ-PsU-VE> · <https://www.youtube.com/watch?v=5rGu1ntLvRw> · <https://www.youtube.com/watch?v=5RNn93sinxo> · <https://www.youtube.com/watch?v=1Xq8EKyINTw> · <https://www.youtube.com/watch?v=homKGDpmhOA> · <https://m.youtube.com/watch?v=rhduWNbpPko> · <https://www.youtube.com/watch?v=5DELA6ARIIc> · <https://www.youtube.com/watch?v=7AsOwX_9R2w> · *(+9 more in findings/)*

**Why it matters.** The YouTube channel and social profiles are among the first things people see when they search the brand, and engines use their names and bios to describe the entity. A channel called 'zero gravity backpack', with a medical-sounding description, spreads the wrong descriptor and an unsupported claim.

claude-seo's seo-geo cites an Ahrefs 75k-brand study in which YouTube mentions had the strongest correlation with AI visibility (~0.737). That is a correlation and depends on methodology, so treat it as directional.

With uploads paused since mid-2025, recent practical questions about adjustment and sizing are answered by forums and marketplace reviews.

Follower counts are not a ranking factor. Hence Low.

**Effect on SEO.** The effect is indirect:
- The brand-SERP profiles would match the site's descriptor.
- Video results become possible for how-to queries, mainly where the video is the page's main content.
- AI engines get more corroborating sources, consistent `sameAs` targets and fresher, dated mentions.
- Disclosed answers on forums give engines a brand-side view to set against the sceptical threads they surface by default.

**How to fix.**

1. **Rename the channel and clean the description.**
   - Name: « Gravipack » (YouTube Studio → Personnalisation → Informations de base). Keep the @Gravipack handle.
   - New description:
     > « Gravipack conçoit des sacs à dos dont les bretelles intègrent un exosquelette qui reporte une partie de la charge des épaules vers les hanches. Tutoriels de réglage, présentation des modèles, tests terrain. Site officiel : https://gravipack.com »
   - Remove the 'étude scientifique et médicale' wording. Once the evidence page exists (study finding), link it neutrally instead.
   - Add links to the site, LinkedIn and Instagram.

2. **Make the next videos answer the questions people actually ask.** The per-model series already exists.
   - (a) « Comment régler les bretelles exosquelette de votre Gravipack », 3–5 min with chapters. Embed it as the main content of /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/. This answers the Decathlon complaints about adjustment.
   - (b) Measured empty weight and volume per model, shown on a scale and with a measuring method.
   - (c) The 3D video, re-cut as the explainer for the 'sac à dos exosquelette' page.
   - (d) Shorts cut from the C8 and BFM segments, if you hold the rights.
   - Then keep a dated cadence, for example one upload a month.

3. **Make every video description useful.**
   - First line: a link to the matching product or guide URL on the canonical host (optionally `?utm_source=youtube&utm_medium=video`).
   - French chapters.
   - Uploaded, checked French captions (.srt) rather than auto-captions only. LLMs read the transcript.

4. **Embed videos on the site.**
   - Use the WordPress YouTube embed block.
   - Add VideoObject markup with Yoast Video SEO or Rank Math (Schema → Vidéo): name, description, thumbnailUrl, uploadDate, duration, embedUrl.
   - Video rich results appear mainly when the video is the page's main content, so expect them on the guide page, not on product pages. On product pages, the embed still helps users and gives AI engines context.

5. **Ask third-party creators** (e.g. the owner of 7AsOwX_9R2w) and the TV channels, where possible, to add a gravipack.com link to their video descriptions.

6. **Align every bio** with the canonical descriptor and the current facts.
   - Facebook: replace « Sac a Dos en Apesanteur » and update the location from Sens.
   - Instagram: bio and link.
   - LinkedIn: HQ Paris 75002, a real employee band.
   - Post dated updates regularly. LinkedIn suits B2B proof points, such as RATP's VivaTech 2023 deployment (about 50 roaming maintenance workers equipped, per RATP's own pages).

7. **Treat TikTok and Pinterest as optional.** Open them only if the team can sustain them, e.g. Pinterest boards for back-to-school and hiking that link product pages. Do not expect ranking gains from follower counts.

8. **Join community discussions openly. Never astroturf.**
   - Answer substantive randonner-leger.org and bushwalk.com threads from a disclosed brand or founder account, with data: empty weight, how the load is transferred, a link to the explainer and evidence pages.
   - Lend bags to independent long-distance hikers for honest, disclosed trip reports.
   - On Reddit, take part only where the topic comes up, with disclosure. Never buy upvotes or post as a 'customer'.

9. **List the renamed YouTube channel, Instagram, Facebook and LinkedIn** in Organization `sameAs` and in Wikidata (P2397, P2003, P2013, P4264).

- **First principle:** Engines describe a brand partly from the profiles that rank for its name. If those profiles use a different descriptor ('zero gravity'), make claims the site cannot back, or go quiet for 16 months, then forums and marketplaces supply the current narrative.
- **Do first:** [#15 There is no single, consistent explainer for 'sac à dos exosquelette', and the brand describes its product several different ways](#15-there-is-no-single-consistent-explainer-for-sac-à-dos-exosquelette-and-the-brand-describes-its-product-several-different-ways), `study-evidence-page`, [#4 Therapeutic, medical-device and reimbursement wording ('anti-douleur', 'anti-TMS', 'dispositif médical', 'remboursé par la Sécurité sociale') and absolute superlatives are used without substantiation](#4-therapeutic-medical-device-and-reimbursement-wording-anti-douleur-anti-tms-dispositif-médical-remboursé-par-la-sécurité-sociale-and-absolute-superlatives-are-used-without-substantiation), `organization-schema-legal-identity`
- **How we'll know the fix failed:** The fix has failed if any of these holds:
- Three months after the rename, brand results and YouTube search for 'gravipack' still show 'zero gravity backpack'.
- No new video has been indexed since the cadence started.
- The adjustment video gets negligible views from YouTube search or from the guide page, and new Decathlon or Trustpilot reviews keep citing adjustment difficulty.
- AI answers to « comment régler un sac Gravipack ? » cite neither the guide nor the video.
- **Leading indicator to monitor:** - YouTube Studio: views from YouTube search for 'gravipack réglage' and 'gravipack' queries, and uploads per month.
- GA4 sessions with utm_source=youtube.
- The Search Console video indexing report for the guide page.
- Each month, count new reviews that mention adjustment difficulty.
- **To verify on-site:** - Check whether product pages and the bretelles guide already embed an adjustment video and the settings PDF.
- Check whether VideoObject is output (Rich Results Test).
- Check which social profiles Organization `sameAs` lists.
- In YouTube Studio, read the real subscriber count, the exact channel ID and the date of the last upload.
- Identify who owns video 7AsOwX_9R2w.

## Schema / Structured Data

**Score:** n/a — not assessed — Requires the live HTML. Recommendations prepared (organization-schema, product-schema-merchant-center).

### 30. Product, Offer and review markup and the Merchant Center setup cannot be verified, and the Content API for Shopping has been sunset (verify on-site)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **5** | Medium | needs-on-site-check | Schema / Structured Data |

**Issue.** **We could not check the markup or Merchant Center.** The sandbox network policy blocked gravipack.com, and the search tool shows no Shopping units. So the current Product and Offer markup and any Merchant Center account status are unknown. WooCommerce outputs Product and Offer JSON-LD by default (an AggregateOffer for variable products). The task is to check completeness and accuracy, not to assume the markup is absent.

**Evidence that would block or weaken merchant listings if markup or a feed repeats it:**

1. **Several prices for one model on gravipack.com itself.** Search snippets, 12/10/2026, capture dates unknown:
   - Sherpa: bleu 119 € (struck price 249 €), orange and kaki 149,90 €, orange 99 € in a promo list.
   - Tokyo: 189 € on one page, 129 € (was 249 €) on another.
   - Pearl: 89 € (was 99,90 €) on one page, 119 € in a list.

   Google disapproves offers when the feed price, the structured-data price and the visible price differ.
2. **Variant structure.**
   - Each colour has its own URL: Sherpa bleu, 45L orange and kaki; Hiking 30L gris and terracotta; Oslo rouge; Pearl 29L gris.
   - A second base path, /produit-gravipack/, holds exact duplicates. The Sherpa Kaki title appears on 3 URLs. Light Promax has 3 URLs; Cargo Max, Business Talk V4 25L and G-Pack have 2 each; two slugs end in '-copie'.
   - Without ProductGroup and variesBy markup, or a single variable product, Google sees near-duplicate, unrelated products.
3. **Review display.**
   - Search snippets of product pages (Rome, Kingston, Hiking Terracotta, Tokyo, Hiking Gris, Sherpa Kaki…) show an 'Avis Google 4,7' badge with hard-coded counts that do not match: 'plus de 1121 avis', 'plus de 1126 avis', and 'plus de 1175 avis' on an 'Avis Google des clients Gravipack' page.
   - **Correction to the earlier hypothesis:** the rating is not uncorroborated. A directory page (groupe-ranque.fr) reports 4,7/5 from 998 Google reviews for Gravipack Vincennes. A blog (compostelle-autrement.com) reports 4,8/5 from 900+. Both are weak sources, but they fit a real Google Business Profile that keeps gaining reviews.
   - The real problems are the inconsistent hard-coded counts, and the risk that this business-level rating is marked up as a Product aggregateRating.
   - Third-party ratings are lower: Trustpilot 3,1/5 (9 reviews; profile claimed since Dec 2020; negative reviews from June 2026 still unanswered), Decathlon brand page 3,88/5 (16), Decathlon collection 4,1/5 (26), Fnac Road Adventure about 3/5 (8).
   - No evidence of on-site product reviews was found. /gravipackers/ is a testimonials page, not product reviews.
4. **Identifiers.** No GTIN or EAN appeared in any official listing snippet, although the same models are sold on Decathlon, Fnac and Nature & Découvertes, which normally require EANs.
5. **Channel context.**
   - No Gravipack offer was found on Amazon.fr.
   - Cdiscount's /r-gravipack.html is an internal search page that returns lookalike products.
   - In the model queries we sampled, marketplace and reseller listings (Decathlon, Nature & Découvertes, Au Vieux Campeur, Ergo-Corner) often rank above the official product page.
   - Google free listings are the main comparison surface where the official offer could appear beside them.
6. **Feed API.** The Content API for Shopping was sunset on 18/08/2026. It has returned intermittent HTTP 410 errors since 01/09/2026 and shuts down completely in early 2027. A WooCommerce feed plugin still on that API silently stops updating prices and stock. Scheduled-fetch, manual and Google Sheets feeds are not affected.
7. **Legacy store.** presta.gravipack.com still shows the Feather at 149 € 'in stock', although the model is no longer in the main store.

**When to raise the severity:**
- **Medium** if product pages have missing or invalid Product markup, or Merchant Center shows disapprovals.
- **High** if the 'Avis Google 4,7' badge is output as a Product aggregateRating.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa-kaki> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · <https://gravipack.com/boutique-gravipack/> · <https://groupe-ranque.fr/gravipack/> · <https://www.compostelle-autrement.com/post/gravipack-le-sac-a-dos-en-apesanteur> · <https://fr.trustpilot.com/review/gravipack.com> · <https://www.decathlon.fr/vc/gravipack> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html> · *(+3 more in findings/)*

**Why it matters.** - **Required data.** Merchant listings need a name, an image and an Offer with a price above zero and a priceCurrency. GTIN, shippingDetails and hasMerchantReturnPolicy add annotations and improve product matching.
- **Price mismatches.** Google compares the visible price, the structured-data price and the feed price, and disapproves offers that differ. gravipack.com already shows 2 to 3 prices for the same model.
- **Review rules.** Google's review-snippet guidelines exclude ratings collected on other sites, so the 'Avis Google 4,7' badge is a policy risk if it is marked up. Misusing review markup can lead to a structured-data manual action that removes product rich results across the site.
- **Feed API.** Since the Content API sunset, a feed plugin that has not migrated stops updating prices and stock. That creates mismatches on its own.

**Effect on SEO.** - Valid Offer and ProductGroup markup plus an approved Merchant Center feed make the official store eligible for merchant-listing displays in Search (price, availability, strikethrough price, shipping and return annotations) and for free listings in the Shopping tab and Images.
- In model queries where Decathlon, Nature & Découvertes, Au Vieux Campeur and Ergo-Corner currently appear, the official offer could then show next to them.
- Product snippets (stars) are possible only from on-site product reviews.
- Price mismatches cause item disapprovals. Ratings borrowed from Google or Trustpilot risk a manual action.
- No direct effect on organic rankings.

**How to fix.**

1. **Baseline first (verify on-site, no changes yet).**
   - Run the Rich Results Test on Sherpa bleu, Sherpa kaki, Pearl 29L gris, Tokyo, Kingston and /boutique-gravipack/.
   - For each, record:
     - which tool outputs the markup (WooCommerce core, Yoast WooCommerce SEO, Rank Math, a review widget) and how many Product nodes there are;
     - Offer or AggregateOffer (merchant listings need an Offer per variant);
     - price compared with the visible price, priceCurrency and availability;
     - brand and gtin;
     - aggregateRating and its source;
     - shippingDetails and hasMerchantReturnPolicy.
   - In Search Console, open the Shopping reports: Fiches de marchand and Extraits de produits.
   - In Merchant Center, check whether an account exists, whether the canonical host is verified and claimed, what the product source is, and what Diagnostics shows.
   - If everything is complete, valid and approved, close this item.
2. **One price per variant, everywhere** (do this with the price-parity fix).
   - The visible price, Offer.price and the feed price must be identical.
   - For promotions, keep the selling price in `price` and put the reference price in a price specification of type StrikethroughPrice. Give the sale window with validFrom and validThrough. Do not rely on priceValidUntil: it does not apply to price specifications.
   - Under French law the struck price must be the lowest price charged in the 30 days before the reduction (Code de la consommation L112-1-1). The 249 € reference prices need checking.
```json
"offers": {
  "@type": "Offer",
  "url": "https://gravipack.com/produit/<sherpa-45>/?attribute_pa_couleur=bleu",
  "price": "119.00",
  "priceCurrency": "EUR",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "priceType": "https://schema.org/StrikethroughPrice",
    "price": "149.90",
    "priceCurrency": "EUR"
  },
  "validFrom": "2026-11-01T00:00:00+01:00",
  "validThrough": "2026-11-30T23:59:59+01:00",
  "availability": "https://schema.org/InStock",
  "itemCondition": "https://schema.org/NewCondition",
  "seller": { "@id": "https://gravipack.com/#organization" }
}
```
   The prices above are illustrative; use the real live prices.
3. **Variants** (do this with the duplicate-URL fix). Choose one model:
   - **(A)** One WooCommerce variable product per model (attribute « Couleur »). 301-redirect the old colour URLs, every /produit-gravipack/ duplicate and the '-copie' URLs to it.
   - **(B)** Keep self-canonical colour pages, each marked up as a variant of one ProductGroup with isVariantOf.

   Either way, output ProductGroup with variesBy and productGroupID, and use the same ID as item_group_id in the feed. Never canonicalise colour pages to a parent while submitting them as separate feed items. WooCommerce core does not output ProductGroup: use your SEO plugin's variant support if it has it, or extend `woocommerce_structured_data_product`. Example for model (A):
```json
{
  "@context": "https://schema.org",
  "@type": "ProductGroup",
  "@id": "https://gravipack.com/produit/<sherpa-45>/#productgroup",
  "name": "Sac à dos de randonnée Sherpa 45 L Gravipack",
  "url": "https://gravipack.com/produit/<sherpa-45>/",
  "productGroupID": "SHERPA45",
  "brand": { "@type": "Brand", "name": "Gravipack" },
  "variesBy": ["https://schema.org/color"],
  "hasVariant": [{
    "@type": "Product",
    "sku": "SHERPA45-KAKI",
    "gtin13": "<EAN-13>",
    "name": "Sac à dos Sherpa 45 L Gravipack – kaki",
    "color": "Kaki",
    "image": ["https://gravipack.com/wp-content/uploads/<sherpa-kaki>.jpg"],
    "offers": { "@type": "Offer", "url": "https://gravipack.com/produit/<sherpa-45>/?attribute_pa_couleur=kaki", "price": "149.90", "priceCurrency": "EUR", "availability": "https://schema.org/InStock" }
  }]
}
```
   Repeat the hasVariant entry for each colour.
4. **Identifiers and brand.**
   - Fill the native WooCommerce field « GTIN, UPC, EAN ou ISBN » (Inventaire tab, set per variation; WooCommerce 9.2+) with the EAN-13 codes already used on the Decathlon, Fnac and Nature & Découvertes listings.
   - Keep the SKU as the MPN.
   - If the active markup generator does not output these fields, add them:
```php
add_filter( 'woocommerce_structured_data_product', function ( $markup, $product ) {
    $markup['brand'] = [ '@type' => 'Brand', 'name' => 'Gravipack' ];
    if ( method_exists( $product, 'get_global_unique_id' ) && $product->get_global_unique_id() ) {
        $markup['gtin13'] = $product->get_global_unique_id();
    }
    return $markup;
}, 10, 2 );
```
   This filter only works if WooCommerce core outputs the markup. If Yoast or Rank Math replaces it, set the fields in that plugin instead.
5. **Reviews: mark up only on-site, product-specific ratings.**
   - In WooCommerce > Réglages > Produits > Avis produits, turn on:
     - product reviews;
     - « Afficher le badge “propriétaire vérifié” »;
     - « Les avis ne peuvent être laissés que par des “propriétaires vérifiés” »;
     - mandatory star ratings.
   - WooCommerce core then outputs aggregateRating and review from these reviews only, which follows Google's rules.
   - Ask every buyer for a review about 3 weeks after delivery. Do not filter out unhappy customers.
   - Never output the Google 4,7 badge, Trustpilot (3,1/5, 9 avis), Decathlon or Fnac ratings as a Product aggregateRating. Google's guidelines require ratings collected on your own site, and a business rating is not a product rating. If the badge plugin has a 'rich snippet' or schema option, turn it off.
   - Keep the Google rating, since third parties corroborate about 4,7 from 998 reviews and 4,8 from 900+. Replace the inconsistent hard-coded counts with either:
     - one dated figure linked to the profile, after checking the live number in the Business Profile, e.g. « Note Google : 4,7/5 – [nombre] avis au [date] (voir les avis) »; or
     - a live widget that follows Google's attribution rules.
   - Near the reviews, add the notice required by Code de la consommation L111-7-2 / D111-17, e.g. « Les avis sont déposés par des clients ayant acheté le produit sur gravipack.com (badge “propriétaire vérifié”). Ils sont publiés sans modification, qu’ils soient positifs ou négatifs, par ordre chronologique. »
   - Disclose any incentive given for a review (loi n° 2023-451).
6. **Shipping and returns.** Declare them once, with values identical to the CGV, in one of these places:
   - Merchant Center: Paramètres > Expédition et retours;
   - Search Console's shopping settings, if there is no Merchant Center account;
   - markup: shippingDetails on the Offer, and hasMerchantReturnPolicy on the Offer or once at Organization level.
```json
"shippingDetails": {
  "@type": "OfferShippingDetails",
  "shippingRate": { "@type": "MonetaryAmount", "value": "0.00", "currency": "EUR" },
  "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "FR" },
  "deliveryTime": {
    "@type": "ShippingDeliveryTime",
    "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 2, "unitCode": "DAY" },
    "transitTime": { "@type": "QuantitativeValue", "minValue": 2, "maxValue": 5, "unitCode": "DAY" }
  }
},
"hasMerchantReturnPolicy": {
  "@type": "MerchantReturnPolicy",
  "applicableCountry": "FR",
  "returnPolicyCountry": "FR",
  "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
  "merchantReturnDays": 14,
  "returnMethod": "https://schema.org/ReturnByMail",
  "returnFees": "https://schema.org/ReturnFeesCustomerResponsibility"
}
```
   Use the real shipping rates, delivery times, return window (14 days minimum) and return fees.
7. **Merchant Center and the feed.**
   - **Account:** if none exists, create one, verify and claim the canonical host (through Search Console or Site Kit), and enable free listings for France.
   - **Product source:** check that the feed plugin (Google for WooCommerce, CTX Feed, Product Feed PRO…) is on a release that uses the Merchant API. The changelog and the plugin's sync log will show 410 errors otherwise. Alternatively, switch to a scheduled-fetch XML feed, which is not affected by the sunset.
   - **Feed titles:** model + capacity + colour + brand, without unproven health claims while the claims review is pending (Merchant Center Misrepresentation policy, unreliable claims). Example: « Sac à dos de randonnée Sherpa 45 L kaki – bretelles exosquelette – Gravipack ».
   - **Legacy store:** once presta.gravipack.com is redirected, make sure it no longer exposes in-stock offers.
8. **Validate, then monitor.**
   - Run the Rich Results Test (merchant listings and product snippets) on the 5 URLs.
   - Check the Search Console Shopping reports and Merchant Center Diagnostics.
   - Add a schema check on three URLs to the release checklist for every price or promotion change.

- **First principle:** Google shows an official store's price, stock, shipping and returns in shopping displays only when it can read one consistent offer per variant that follows its policies, across the page, the structured data and the feed. A mismatch or a borrowed rating gets the offer disapproved or the markup ignored rather than displayed.
- **Do first:** `price-parity`, [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), `canonical-host`, `google-rating-claims`, `health-claims-compliance`, [#16 The legacy PrestaShop store presta.gravipack.com still appears in search results with old product, study and award pages](#16-the-legacy-prestashop-store-prestagravipackcom-still-appears-in-search-results-with-old-product-study-and-award-pages)
- **How we'll know the fix failed:** - **Implementation failed** if, 6 to 8 weeks after deployment, the Search Console 'Fiches de marchand' report shows fewer valid items than live variants, or any critical issue (missing price, invalid priceSpecification, review issues). It also failed if Merchant Center shows disapprovals for a price mismatch or for Misrepresentation.
- **The bottleneck is elsewhere** if items are valid and approved but free-listing impressions for model queries ('gravipack sherpa 45', 'sac à dos tokyo gravipack') stay near zero after 8 weeks. The limit is then titles, images or price competitiveness against Decathlon and Nature & Découvertes, not markup. Do not add more markup.
- **No change was needed** if the baseline in step 1 already shows complete, valid Product markup and an active Merchant Center account with no disapprovals. Close the finding as no_change_needed.
- **Leading indicator to monitor:** - Weekly in Search Console (Shopping > Fiches de marchand): valid item count and number of issues.
- In Merchant Center, Performances > Fiches gratuites: impressions and clicks per model.
- Number of disapproved or limited items.
- Weekly 10-URL spot check: share of product URLs where the visible price, the schema price and the feed price match.
- **To verify on-site:** 1. Run the Rich Results Test on the Sherpa bleu, Sherpa kaki, Pearl 29L gris, Tokyo and Kingston product URLs and on /boutique-gravipack/. Record:
   - Product or ProductGroup, Offer or AggregateOffer;
   - price compared with the visible price, priceCurrency, availability;
   - gtin and brand;
   - shippingDetails and hasMerchantReturnPolicy;
   - number of Product nodes;
   - whether aggregateRating exists and its numbers. If it equals 4,7 / 1121–1175, the Google badge is marked up: escalate to High.
2. Identify the plugin behind the Google review badge and its schema or rich-snippet setting.
3. Check the WooCommerce > Réglages > Produits > Avis produits settings and count on-site reviews per model.
4. In Merchant Center: does an account exist, is the canonical host claimed, what are the product source and its API version, and are there disapprovals or Misrepresentation warnings?
5. Check the Search Console Shopping reports.
6. Check the Product markup on the legacy presta.gravipack.com pages.

### 37. Organization markup should carry the verified legal identity and sameAs links (verify on-site)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | needs-on-site-check | Schema / Structured Data |

**Issue.** **We could not inspect the current markup.** The sandbox network policy blocked gravipack.com, so we could not read its JSON-LD. WordPress SEO plugins (Yoast, Rank Math) normally output an Organization node already (name, URL, logo, sometimes social profiles). The likely gap is missing or outdated properties, not a missing block. Verify on-site before changing anything.

**What the off-site evidence shows, and why the properties matter here:**
- **Legal identity is now verified in the registries.** The operator and brand owner is EXOSQUELETTE LIGHT SAS, SIREN 840 543 383 (siège SIRET 840 543 383 00045), share capital 16 960 €, president Mohammed Errafi since June 2018.
  - Created on 12/06/2018 in Sens as GRAVIBAG.
  - Renamed GRAVIPACK from 01/07/2022.
  - Renamed EXOSQUELETTE LIGHT by the AGE of 02/01/2025 (BODACC 28/02/2025).
  - Seat history: Sens, then 46 rue de la Bienfaisance, 94300 Vincennes (late 2022), then **10 rue de la Paix, 75002 Paris since 19/05/2026**.
  - The GRAVIPACK trademark was filed on 27/05/2019 and is valid to 2029, per societe.com.
  - The /mentions-legales/ search snippet already names EXOSQUELETTE LIGHT, Paris. That is good, and the markup should repeat it.
- **Old facts still circulate on third-party pages.** They show Vincennes: rubypayeur ('EXOSQUELETTE LIGHT à VINCENNES'), PagesJaunes ('Gravipack à Vincennes – Maroquinerie', 0 reviews), Mappy (46 r Bienfaisance), gravipacker.com, the groupe-ranque.fr directory ('Gravipack – Vincennes') and the AI-generated directory motherbase.ai. Other directories still list the former name GRAVIBAG.
- **No knowledge-graph entity exists.** Searches filtered to Wikidata, Wikipedia and Crunchbase found only lookalikes: Gravis, Gravitas Packaging, Gpack, a 'Zero Gravity' YouTube channel and the Instagram handle @granipack.
- **Owned profiles exist and can go in sameAs:**
  - LinkedIn company page fr.linkedin.com/company/gravipack
  - YouTube @Gravipack (also reachable as /c/Gravipack)
  - Instagram @gravipack (about 23K followers in a snapshot from around March 2023)
  - Facebook /gravipack
  - Trustpilot gravipack.com (claimed since December 2020; 3.1/5 from 9 reviews)
  - Founder profile: linkedin.com/in/errafi/
- **Documented awards:**
  - Concours Lépine 2018 silver medal, reported consistently by Europe 1 and Neozone. No official palmarès was found.
  - Trophées INPI 2022 finalist, Start-up category, on inpi.fr.
  - A separate 'military innovation' silver medal is claimed by the founder but not documented.
- **Brand results are volatile.** For 'gravipack', in the search results we sampled (a US-located, non-Google index), the home page ranked #7 in one run and #9 in another. The first owned URL ranked #4 to #6. The 2020 KissKissBankBank campaign ranked #1 in both runs.
- **Kid'abord is a separate company.** It acts as licensee and marketplace seller (Decathlon, Nature & Découvertes) and must not be merged into the Gravipack Organization node.

**Evidence.** <https://gravipack.com/mentions-legales/> · <https://gravipack.com/> · <https://www.gravipack.com/a-propos-de-nous-gravipack-au-service-de-votre-dos/> · <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383> · <https://www.verif.com/en/company/GRAVIPACK-68d9c0de12992303386f741e/> · <https://www.inpi.fr/trophees/gravipack-les-bretelles-qui-allegent-le-poids-sur-les-epaules-et-le-dos> · <https://fr.linkedin.com/company/gravipack> · <https://www.youtube.com/@Gravipack> · <https://www.instagram.com/gravipack/> · <https://www.facebook.com/gravipack/> · <https://fr.trustpilot.com/review/gravipack.com> · <https://www.linkedin.com/in/errafi/> · *(+2 more in findings/)*

**Why it matters.** Organization markup is the site's machine-readable statement of who it is. Google uses it, alongside other sources, to choose the logo and to match the brand to the right legal entity. legalName, iso6523Code (the SIREN) and sameAs give an unambiguous key for that matching.

The ambiguity is real here: three legal names in eight years, three seats (Sens, Vincennes, Paris), lookalike brands, and no Wikidata item. LLMs and Google can repeat the stale Vincennes or GRAVIBAG facts, or confuse Gravipack with Gravis or Gravitas.

Keep the effort proportionate. Google says Organization markup is optional and gives no rich result beyond logo eligibility, and Google's AI guidance does not treat it as an AI-specific lever. One accurate block is enough, hence Low.

**Effect on SEO.** Clearer entity matching in the Knowledge Graph and AI answers: the brand (Gravipack), the company (EXOSQUELETTE LIGHT), the founder and the official profiles are tied to one ID. The logo becomes eligible to show in results. Brand descriptions become more consistent, which indirectly helps control the brand results. No direct ranking effect.

**How to fix.**

1. **Measure before changing anything (verify on-site).**
   - Run the Rich Results Test and validator.schema.org on the home page, /a-propos-de-nous-gravipack-au-service-de-votre-dos/ and /mentions-legales/.
   - Note which plugin outputs the markup (Yoast, Rank Math, the theme, WooCommerce or a review widget).
   - Check whether more than one Organization node exists.
   - Check which host (www or apex) the `@id` and `url` use, compared with the canonical host.
   - List which of the properties below are missing.
   - Extend the existing node. Never paste a second Organization block.
2. **Fix the visible facts first.** The markup must repeat what the pages say. The mentions légales (LCEN art. 1-1 since loi SREN 2024) and the About page should carry the same identity block, for example:
   « Gravipack® est une marque de la société EXOSQUELETTE LIGHT SAS (SIREN 840 543 383), dont le siège est situé 10 rue de la Paix, 75002 Paris. La société a été fondée en 2018 par Mohammed Errafi, inventeur des bretelles à exosquelette Gravipack. Médaille d’argent au Concours Lépine 2018 ; finaliste des Trophées INPI 2022 (catégorie Start-up). »
   List only awards you can link to a source.
3. **Plugin settings.**
   - **Yoast:** SEO > Réglages > Représentation du site. Choose « Organisation », name « Gravipack », an alternate name, and a logo (square, at least 112×112 px, crawlable URL). Put the profile URLs under « Autres profils ». Recent Yoast versions also have extra organisation fields on this screen (legal name, founding date, VAT ID, ISO 6523 code…). Fill them where available.
   - **Rank Math:** Titres & Méta > Local SEO. Set type Organization, name, logo, URL and address.
   - Add anything the interface lacks with a filter (step 4).
4. **Add the missing properties with a filter.** Use the child theme's functions.php or a small mu-plugin:
```php
// Yoast SEO
add_filter( 'wpseo_schema_organization', function ( $data ) {
    $data['legalName']     = 'EXOSQUELETTE LIGHT';
    $data['alternateName'] = [ 'GRAVIPACK', 'GRAVIBAG' ];
    $data['iso6523Code']   = '0002:840543383'; // ICD 0002 = SIRENE
    $data['foundingDate']  = '2018-06-12';
    $data['address'] = [
        '@type' => 'PostalAddress', 'streetAddress' => '10 rue de la Paix',
        'postalCode' => '75002', 'addressLocality' => 'Paris', 'addressCountry' => 'FR',
    ];
    $data['founder'] = [ '@id' => home_url( '/#fondateur' ) ];
    $data['award']   = [ 'Médaille d’argent, Concours Lépine 2018', 'Finaliste des Trophées INPI 2022, catégorie Start-up' ];
    return $data;
} );
// Rank Math: add the same keys to the Organization entity with add_filter( 'rank_math/json_ld', ... ).
```
5. **Target result.** This is what the validator should show. Replace the placeholders and use the canonical host:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://gravipack.com/#organization",
  "name": "Gravipack",
  "alternateName": ["GRAVIPACK", "GRAVIBAG"],
  "legalName": "EXOSQUELETTE LIGHT",
  "url": "https://gravipack.com/",
  "logo": "https://gravipack.com/wp-content/uploads/<logo-gravipack>.png",
  "description": "Marque française de sacs à dos équipés de bretelles à exosquelette (inserts carbone) conçues pour répartir la charge portée.",
  "foundingDate": "2018-06-12",
  "iso6523Code": "0002:840543383",
  "vatID": "<n° de TVA intracommunautaire figurant sur vos factures>",
  "address": {"@type": "PostalAddress", "streetAddress": "10 rue de la Paix", "postalCode": "75002", "addressLocality": "Paris", "addressCountry": "FR"},
  "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "email": "<adresse de contact vérifiée>", "availableLanguage": ["fr"]},
  "founder": {"@type": "Person", "@id": "https://gravipack.com/#fondateur", "name": "Mohammed Errafi", "jobTitle": "Président et inventeur", "sameAs": ["https://www.linkedin.com/in/errafi/"]},
  "brand": {"@type": "Brand", "name": "Gravipack"},
  "award": ["Médaille d’argent, Concours Lépine 2018", "Finaliste des Trophées INPI 2022, catégorie Start-up"],
  "sameAs": [
    "https://www.linkedin.com/company/gravipack/",
    "https://www.youtube.com/@Gravipack",
    "https://www.instagram.com/gravipack/",
    "https://www.facebook.com/gravipack/",
    "https://www.trustpilot.com/review/gravipack.com",
    "https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383"
  ]
}
```
   Give the customer-service or returns address on the contact page and in the CGV if it differs from the registered seat. Do not put it in Organization.address.
6. **Link the rest of the markup to this node.**
   - Define the founder `Person` once, with name, role and LinkedIn sameAs only, and reuse its `@id` on the About page and on author bylines.
   - Every Product carries `"brand": {"@type": "Brand", "name": "Gravipack"}`. Each Offer's `seller` and the WebSite `publisher` point to `{"@id": "https://gravipack.com/#organization"}`.
   - Kid'abord is a separate company acting as licensee and marketplace seller. Do not declare it as parentOrganization. Use `manufacturer` only where it is true for a given product.
7. **Keep sameAs clean.**
   - List only profiles that represent the brand, using their canonical URLs (www.linkedin.com/company/gravipack/, www.trustpilot.com/review/gravipack.com).
   - Leave out the Decathlon brand page, the KissKissBankBank campaigns and reseller pages.
   - Add the Wikidata item once it exists. It must be created transparently, with independent references (see the knowledge-graph finding).
   - Update those profiles to the same legal name and Paris seat: the LinkedIn siège, the Facebook « À propos » section and the Trustpilot company information.
8. **Validate, then stop.**
   - Re-run the Rich Results Test (logo detected, 0 errors).
   - Check the rendered HTML in Search Console URL Inspection.
   - Do not invest further. More markup will not create a knowledge panel; off-site sources (registry citations, Wikidata, PagesJaunes) do that.

- **First principle:** Search engines and LLMs build one entity from many sources. When the site states its legal identity, seat and official profiles in machine-readable form, and those facts match the public registry, the conflicting third-party facts (Vincennes, GRAVIBAG, lookalike brands) lose weight in the merged entity.
- **Do first:** [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards), `canonical-host`
- **How we'll know the fix failed:** **Implementation failed** if, after deployment and a recrawl (4 to 8 weeks), the Rich Results Test or Schema validator on the home page still shows errors, a duplicate Organization node, or values that differ from the mentions légales.

**The strategy failed** if the markup validates but, after 3 months, a fixed prompt panel still names Vincennes or Sens as the current seat, gives a legal name other than EXOSQUELETTE LIGHT, or confuses Gravipack with Gravis or Gravitas. The panel is ChatGPT, Perplexity, Gemini and Google AI Mode, asked: « Qui est derrière la marque Gravipack ? », « Où est le siège de Gravipack ? », « Qui a fondé Gravipack ? ». In that case the bottleneck is off-site sources (registry citations, PagesJaunes, Wikidata), not markup. Stop adding properties and fix those sources.
- **Leading indicator to monitor:** - Organization detected with 0 errors in the Rich Results Test on the home page (check once after release, then after each plugin update).
- Monthly share of correct answers (legal name, seat, founder, founding year) in the 5-prompt AI panel.
- Whether the Gravipack logo or a brand knowledge panel appears in a manual google.fr check for 'gravipack' (private window, French location).
- **To verify on-site:** - Run the Rich Results Test and validator.schema.org on https://gravipack.com/ and https://www.gravipack.com/, /a-propos-de-nous-gravipack-au-service-de-votre-dos/ and /mentions-legales/.
- List every Organization, WebSite and Person node and the plugin that outputs it. Check whether two Organization nodes exist (SEO plugin plus theme or review widget).
- Compare name, legalName, address, logo and sameAs with the mentions légales.
- Confirm the logo URL returns 200 and is not blocked by robots.txt.
- Check whether the @id and url use the canonical host.
- In wp-admin, record which Yoast or Rank Math organisation fields are already filled.

## Performance (CWV)

**Score:** n/a — not assessed — Requires PageSpeed/CrUX or a local Lighthouse run against the live site.

*No search-evidence findings — this pillar needs the on-site crawl (see ONSITE-AUDIT-PENDING.md).*

## Images

**Score:** n/a — not assessed — Requires the live HTML (alt text, formats, sizes, lazy-loading).

*No search-evidence findings — this pillar needs the on-site crawl (see ONSITE-AUDIT-PENDING.md).*

## Off-Page & Authority

**Score:** **45/100** *(partial)* — ~25 mentioning domains incl. 5 high-authority French editorial (Journal du Geek, Maddyness, Europe 1, France Bleu, franceinfo), but no national daily/health media, no coverage since Feb 2024, absent from comparatifs; link status unmeasured (press-coverage-freshness, listicle-comparatif-gap, mention-link-reclamation, backlink-measurement).

**What works:**
- Real editorial coverage on high-authority French media
- INPI and RATP institutional pages name the brand
- No toxic link patterns seen

### 10. Gravipack is missing from the third-party comparison and 'meilleur …' articles that rank for generic ergonomic, hiking and school-bag queries

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **6** | High | likely | Off-Page & Authority |

**Issue.** In the search results we sampled (a US-located, non-Google index), no comparison or 'meilleur …' article naming Gravipack appeared for generic ergonomic, hiking, laptop or school-bag queries:
- 'meilleur cartable ergonomique comparatif 2026': avis-parents x4, meilleurtest x3, futura-sciences x2.
- 'meilleur cartable ergonomique 2026': 8 of 9 results are comparisons (futura-sciences, avis-parents x2, meilleurs.fr, lemeilleuravis, coin-pratique, mafamillezen, zoneled). They list ergobag Prime, Satch, Baagl, Eastpak and Tann's.
- 'sac à dos randonnée ergonomique': Glisshop x2, Cdiscount, Rayonrando, Ridepark, Toporando ('11 modèles comparés'), Hardloop ('15 meilleurs'), mon-sac-a-dos and Millet. The lists name Osprey, Deuter, Gregory, Millet and Mammut.
- 'sac à dos ordinateur ergonomique': mon-sac-a-dos x2, sac-a-dos-france, Eastpak, Darty, Karkoa, Accergo ('5 meilleurs'), ma-boutique-ergonomique and Ergonovie.
- 'meilleur sac à dos ergonomique comparatif 2026': Snowleader top 10, Toporando x2, Clubic, TechRadar FR, Globe-Trotting and Athleteside. None of the top 9 is a comparison focused on ergonomics, which is itself a content gap.
- 'sac à dos ergonomique' and 'cartable ergonomique' (extended mode): no Gravipack URL at all. Phase-1 standard sets #22, #26 (tonton-outdoor best-of), #39 (TechRadar, meilleurtest) and #47 (fflose best-of) show the same pattern.

Two more checks found nothing either:
- A search that excluded Gravipack's own sites, resellers and marketplaces returned only single-product tests (i-trekkings Oslo 70 L), press (Gomet, PresseSanté, INPI) and reseller pages, never a list.
- A search limited to accergo, karkoa, mon-sac-a-dos, ma-boutique-ergonomique, techradar, norveya and le-repaire showed no Gravipack mention in the snippets.

Scope correction: Gravipack is not absent from its own niche. Extended-mode data show gravipack.com ranking for the 'anti mal de dos' head terms:
- scolaire: #1-#3
- 'ergonomique mal de dos': #2 and #4
- 'sac à dos anti mal de dos': #4-#6
- randonnée: #5-#6
- ordinateur: #3-#5
For 'meilleur sac à dos anti mal de dos', ergo-corner's Gravipack brand page is #1 and the gravipack.com home page is #5. The gap is the generic 'ergonomique / randonnée / cartable' wording and the third-party lists.

Gravipack sells a product for each segment:
- hiking: Sherpa, Hiking, Oslo;
- laptop: Business Talk V4, Kingston, Rome;
- collège and lycée: G-Pack, Kingston.
Primary-school cartables (ergobag, Satch) are a neighbouring segment rather than a direct match.

Caveats:
- The evidence is snippet-level only.
- The full text of the extended-mode lists (accergo, norveya, karkoa, le-repaire, zeoutdoor comparatif) was not checked, and some may already mention Gravipack.
- Several of the lists that rank are published by competing shops or brands (karkoa, norveya, mon-sac-a-dos, ma-boutique-ergonomique, sacados.fr). They will not feature a rival.

**Evidence.** <https://www.avis-parents.com/tests-avis/meilleur-cartable/> · <https://www.avis-parents.com/tests-avis/meilleur-cartable-primaire/> · <https://www.futura-sciences.com/conso/comparatifs/meilleur-cartable-comparatif/> · <https://www.futura-sciences.com/tech/comparatifs/meilleur-sac-a-dos-ordinateur-portable-comparatif/> · <https://meilleurtest.fr/comparatif/sac-a-dos-ordinateur/> · <https://meilleurtest.fr/comparatif-sac-a-dos-de-randonnee-journee/> · <https://meilleurtest.fr/comparatif-sac-a-dos-20l/> · <https://toporando.fr/meilleurs-sacs-a-dos-randonnee-trekking/> · <https://toporando.fr/meilleurs-sacs-a-dos-randonnee-journee/> · <https://blog.snowleader.com/top-10-sac-a-dos-randonnee/> · <https://www.glisshop.com/conseils/les-meilleurs-sacs-a-dos-de-randonnee.html> · <https://ridepark.com/matos/meilleurs-sacs-a-dos-randonnee/> · *(+9 more in findings/)*

**Why it matters.** For research-before-buying queries ('meilleur …', 'comparatif', 'sac à dos ergonomique'), search engines mostly rank comparison articles and retailer category pages. ChatGPT, Perplexity and Google's AI features build their 'which bag should I buy' shortlists largely from those same articles. A brand missing from them is invisible to buyers at the shortlist stage, however good its own pages are.

**Effect on SEO.** Each inclusion brings:
- referral traffic;
- a brand mention next to category terms (sac à dos ergonomique, cartable ergonomique, sac randonnée), which helps search and AI systems associate the brand with the category and makes AI citations more likely;
- sometimes an editorial link.
Truly independent editorial links can be followed. Affiliate links, and links given in return for a free or loaned product, must be marked rel="sponsored" (or nofollow) and pass no ranking credit. Their value is visibility, sales and places in AI shortlists, not PageRank.

**How to fix.**

1. **Verify before outreach (1-2 days).** Open the full text of each ranking list. In a sheet, record: whether it names Gravipack (yes/no), any link and its rel value, last-updated date, how it makes money (affiliate, Amazon), and the author's contact. Start with:
   - accergo.fr/meilleurs-sacs-a-dos-ergonomiques/, the norveya and karkoa guides, le-repaire, zeoutdoor comparatif;
   - TechRadar FR, meilleurtest.fr, avis-parents, futura-sciences (cartable), Clubic (laptop);
   - the Snowleader top 10, Toporando (journée and trekking), Ridepark, Hardloop, Glisshop conseils, tonton-outdoor, fflose.
2. **Sort the targets into three groups.**
   - (a) Independent editors and testers (meilleurtest, avis-parents, futura-sciences, Clubic, TechRadar FR, Toporando, Ridepark, tonton-outdoor, fflose, i-trekkings): pitch them.
   - (b) Retailer buying guides (Snowleader, Glisshop, Hardloop, Au Vieux Campeur, Nature & Découvertes, ergo-corner, Équilibre France Ergonomie): these guides list what the shop stocks. Ask current resellers to add Gravipack to their own 'meilleurs sacs' and 'bien choisir' guides, and approach the others through wholesale.
   - (c) Competing shops and brands (karkoa, norveya, mon-sac-a-dos, ma-boutique-ergonomique, sacados.fr): skip.
3. **Fix the facts writers will check.** Prepare a one-page fiche technique per model: poids à vide, volume mesuré, dimensions, plage de réglage taille/poids, prix public conseillé, garantie. For the Sherpa 45, publish a measured volume, because its capacity is publicly disputed (Outzer measured about 30 L). Put the same table on each product page in the HTML. Present any efficacy figure ('92 %') only as the brand's own figure, linked to the evidence page once it exists. Align prices across channels first, because lists print prices.
4. **Match the model to the list.**
   - hiking: Sherpa 45 / Hiking 33 / Oslo 60+10;
   - laptop: Business Talk V4 / Kingston;
   - collège/lycée: G-Pack / Kingston;
   - vélotaf: Tokyo / Rome;
   - artisans and porte-outils: Light Promax / ExoTool.
5. **Pitch honestly: offer a loan or test unit, and never pay for placement.** Example:
   > Objet : Proposition de test – sac à dos à exosquelette Gravipack pour votre comparatif « [titre] »
   > Bonjour [Prénom], nous suivons votre comparatif « [titre] ». Gravipack conçoit des sacs à dos dont les bretelles intègrent un exosquelette destiné à soulager les épaules. Nous pouvons vous prêter un [modèle] pour un test en conditions réelles : vous restez entièrement libre de votre avis. Fiche technique : [lien]. Visuels HD et informations société : https://gravipack.com/dossier-de-presse/. Bien cordialement, [Nom], [fonction], Gravipack
   If the product is gifted or any payment is involved, the publisher must disclose it ('collaboration commerciale' / 'produit offert') under the French influencer law (loi n° 2023-451). The links should carry rel="sponsored" or nofollow. If you run an affiliate programme (e.g. Awin, Effiliation, or a WooCommerce plugin such as AffiliateWP), its links must be rel="sponsored".
6. **Time the pitches.**
   - Now (Oct-Dec 2026): the 2027 editions of 'meilleur … 2026' lists, since titles are re-dated around the new year.
   - April-June 2027: back-to-school lists (cartable, sac collège).
   - February-April 2027: hiking lists.
7. **Extra angle.** Neozone covered the competing LEX exoskeleton backpack. Pitch them a piece comparing exoskeleton approaches for backpacks that includes Gravipack.
8. **Own the comparison too.** Publish a fair comparison page ('sac à dos à exosquelette vs sac à dos ergonomique classique', with a table and stated limits). On the existing hubs, add 'ergonomique' as a secondary term without removing 'anti mal de dos'. Both tasks belong to the on-page clusters.
9. **Domain-level gap (later).** Once Moz or DataForSEO is set up, run `/seo backlinks gap gravipack.com ergobag.fr` (or the French Deuter or Osprey sites) to get a referring-domain gap list. Bing's comparison only works for sites you own.

- **First principle:** For 'best X' queries, search engines and AI answers hand the choice to curated lists. A brand makes the shortlist only if independent editors have tested it and can check its specs. Inclusion is earned with accurate data and samples; it cannot be bought.
- **Do first:** `citable-evidence-page`, `spec-price-consistency`, [#14 No comparison or alternatives content answers 'Gravipack vs …' and comparison intent](#14-no-comparison-or-alternatives-content-answers-gravipack-vs--and-comparison-intent), `segment-hubs-ergonomique`
- **How we'll know the fix failed:** Recheck the target sheet after the 2027 back-to-school and hiking update cycles (September 2027). If none of the roughly 15 independent lists names Gravipack, the pitch or the product positioning is not landing. Ask two or three editors why, then shift effort to reseller guides and the brand's own comparison page. The work has also failed if Gravipack gets listed but referral sessions from those domains stay near zero, or AI answers to the fixed prompts still leave it out.
- **Leading indicator to monitor:** Number of target lists that name Gravipack (checked monthly in the sheet); GA4 referral sessions and revenue from those domains; a monthly manual check of 5 fixed prompts in ChatGPT, Perplexity and Google AI Mode for Gravipack mentions: 'meilleur sac à dos ergonomique', 'meilleur cartable ergonomique collège', 'sac à dos randonnée ergonomique', 'sac à dos ordinateur ergonomique' and 'sac à dos anti mal de dos'.
- **To verify on-site:** Check that each product page shows a comparable spec table (poids à vide, volume mesuré, dimensions, prix) in the server-rendered HTML. Check that /dossier-de-presse/ offers a downloadable fact sheet and HD visuals, and that prices match across product pages. Off-site: open the full text of the lists named above in a browser, because the audit saw snippets only.

### 18. Press and partner mentions of Gravipack have unknown link status and should be checked and reclaimed as links

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Low | needs-on-site-check | Off-Page & Authority |

**Issue.** These pages mention Gravipack by name (confirmed in the saved search logs):
- **Editorial:** Maddyness (2024-02-08), Journal du Geek (2021-09-04), ICI/France Bleu (2021-09-02 and 2020-09-03), the ICI 'Les nouveaux inventeurs du concours Lépine' page (first for 'sac à dos anti mal de dos' in the search results we sampled), franceinfo / France 3 BFC (about 2018), Europe 1 (Trophées de l'Avenir 2023), Neozone, Le Matin (2020), Challenge.ma, the FNH.ma founder interview, Gomet, PresseSanté and Maginfrance.
- **Tests and blogs:** the i-trekkings Oslo 70 L test and compostelle-autrement.
- **Institutional:** the INPI Trophées page (2022 finalist).
- **Directories and profiles you can edit or ask to edit:** Les Pépites Tech, MyFrenchStartup, Motherbase (an AI-generated directory, on two subdomains) and four KissKissBankBank campaigns (2020, 2022, 2023 SmartBag, 2024 children's bag).
- **Resellers and partners with brand content:** ergo-corner (/55-gravipack, /content/13-le-sac-a-dos-gravipack and blog b14, which rank in 8 extended-mode 'anti mal de dos' result sets), Équilibre France Ergonomie (/les-nouveaux-sacs-gravipack/ and product pages), Au Vieux Campeur and Nature & Découvertes.
- **Licensees:** the founder interview names Kid'abord, Packcraft and BSGroupe as licensees (unverified for the last two). Kid'abord is a separate company that acts as licensee and as the marketplace seller on Decathlon and Nature & Découvertes; it posts about Gravipack on LinkedIn.

Search data cannot show whether each page links, the rel value, the anchor text, or which host it points to (apex, www, presta. or .fr). Link status is therefore unknown, not 'missing'.

Corrections:
- The francebleu.fr URLs have probably moved to ici.fr after the 2025 rebrand; check the live URL first.
- Decathlon and Fnac seller and brand pages generally do not allow outbound links to brand sites, and nofollow or UGC links pass little or no equity, so they are not realistic targets.
- KKBB support now redirects to Ulule; only the creator can still post updates on the campaign pages.
- Old regional articles (franceinfo 2018) are rarely edited, so expect few successes there.
- RATP-owned pages are covered in the ratp-proof-point finding.

**Evidence.** <https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://www.francebleu.fr/infos/economie-social/le-sac-a-dos-innovant-invente-par-un-icaunais-pour-soulager-les-dos-des-enfants-est-en-vente-1630589500> · <https://www.ici.fr/infos/economie-social/la-nouvelle-eco-le-cartable-revolutionnaire-de-la-societe-gravipack-a-sens-fait-un-carton-1599115911> · <https://www.ici.fr/emissions/les-nouveaux-inventeurs-du-concours-lepine/gravipack-le-sac-anti-mal-de-dos-8017902> · <https://www.franceinfo.fr/france/bourgogne-franche-comte/yonne/innovation-le-sac-a-dos-qui-ne-fait-pas-mal-au-dos-en-voie-de-commercialisation_2822579.html> · <https://www.europe1.fr/node/58664> · <https://www.neozone.org/innovation/gravipack-le-sac-a-dos-qui-reste-leger-comme-une-plume-meme-quand-il-est-plein-a-craquer> · <https://lematin.ma/journal/2020/gravipack-permet-gra-bretelles-munies-dinserts-innovants-placer-sac-dos-apesanteur-epaules/329564.html> · <https://www.challenge.ma/?p=271181> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://gomet.net/innovation-gravipack-le-sac-a-dos-qui-defie-la-pesanteur/> · *(+16 more in findings/)*

**Why it matters.** A page that already names the brand is the cheapest link available. The editor has already judged the brand newsworthy, and the request is a small correction for readers. Links that point at retired hosts (presta.gravipack.com, gravipack.fr) or dead URLs waste equity the brand has already earned.

**Effect on SEO.** Turning even a few of the high-value mentions (Maddyness, Journal du Geek, ICI, Europe 1, INPI) into followed links to the canonical gravipack.com URL would add relevant, authoritative referring domains. How much this helps is unknown without link data. Correcting reseller and directory profiles gives search engines and AI systems consistent entity signals (name, URL, description) that tie mentions to the official site, and it brings referral traffic.

**How to fix.**

1. **Settle the target first.** Agree the canonical host (apex or www). Make sure presta.gravipack.com and gravipack.fr redirect page-to-page with 301s to it. Reclaimed links should point to final URLs, never to a redirect chain.
2. **Check link status (1-2 hours).** Build `links.json` from the URLs above, e.g. `[{"source_url": "https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/"}, {"source_url": "https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/"}]`. Replace francebleu.fr URLs with their live ici.fr versions. From a machine with network access, run:
```bash
"$HOME/.claude/skills/seo/scripts/claude-seo" run verify_backlinks.py --target https://gravipack.com/ --links links.json --json > gravipack-com.json
"$HOME/.claude/skills/seo/scripts/claude-seo" run verify_backlinks.py --target https://gravipack.fr/ --links links.json --json > gravipack-fr.json
```
   The gravipack.com run also catches www. and presta. links (match_type domain_match or subdomain_match); open each match to see the exact target URL. Pages reported as `unverifiable_js` (social and JavaScript-rendered pages) count as unknown, not missing.
3. **Sort the results.**
   - Followed link to a live canonical URL: nothing to do.
   - Link to presta., .fr or a 404: make that URL 301 to the closest matching live page (Redirection plugin or a server rule). Ask the site to update the link only if it is high-value.
   - nofollow link: accept it.
   - No link: request one (step 4).
4. **Request the link.** Start with Maddyness, Journal du Geek, ICI, Europe 1, INPI and i-trekkings. Template (verified facts only):
   > Objet : Votre article sur Gravipack – lien vers le site officiel
   > Bonjour [Prénom], merci encore pour votre article « [titre] » du [date]. Pour vos lecteurs qui souhaitent en savoir plus, serait-il possible d'ajouter un lien vers notre site officiel, https://gravipack.com/ (ou [page la plus pertinente]) ? Visuels HD et informations à jour : https://gravipack.com/dossier-de-presse/. Bien cordialement, [Nom], [fonction], Gravipack
   Do not add unverified claims such as sales volumes ('plus de 20 000 sacs vendus') or efficacy percentages. Send one follow-up after 10 days, then stop.
5. **Edit what you control.**
   - Update the website field and description on Les Pépites Tech, MyFrenchStartup, LinkedIn, YouTube, Facebook, Instagram and the claimed Trustpilot profile.
   - Ask Motherbase to correct its facts.
   - On each of the 4 KKBB campaigns, post a final news update as the creator with the official-store link (KKBB support now redirects to Ulule).
6. **Work with partners.**
   - Send ergo-corner, Équilibre France Ergonomie, Au Vieux Campeur and Nature & Découvertes a brand kit: a short, unique description (not copied from gravipack.com), the logo, the official URL and verified claims only. Ask for a « Site officiel de la marque » link on their brand pages.
   - Ask the licensees (Kid'abord, plus Packcraft and BSGroupe if confirmed) to add a « Technologie Gravipack® » block linking to https://gravipack.com/.
   - Do not ask Decathlon or Fnac for links.
7. **Log and re-check every quarter.** Use the same sheet as new press wins: URL, date, rel, anchor, target, status.

- **First principle:** When a page already names the brand, the editorial judgement has been made. All that is missing is the link, or the right target for it. That makes reclamation the cheapest way to earn relevant links, but only after checking that the links really are missing.
- **Do first:** `canonical-host-consolidation`, `presta-legacy-redirects`, [#33 The backlink profile cannot be measured with the current tooling; no toxic patterns were seen in the sample](#33-the-backlink-profile-cannot-be-measured-with-the-current-tooling-no-toxic-patterns-were-seen-in-the-sample)
- **How we'll know the fix failed:** If the first check shows most high-value mentions already link to gravipack.com, the premise is wrong: close the task and put the effort into new coverage. After outreach, if fewer than 2 of the roughly 10 priority requests produce a link or a corrected target within 3 months, editors are not responding. Stop chasing them and focus on the profiles and partners you control.
- **Leading indicator to monitor:** Number of verified followed links from the mention list (re-run verify_backlinks.py every quarter); new referring domains in GSC Liens > Principaux sites d'origine; GA4 referral sessions from ergo-corner, Équilibre France Ergonomie and KKBB.
- **To verify on-site:** Check that /dossier-de-presse/ exists and lists coverage. Confirm which host is canonical, and that presta.gravipack.com and gravipack.fr URLs return a single 301 to the matching live pages (curl -sI). In GSC, use 'Pages les plus liées' to find linked URLs that return 404.

### 19. Independent press coverage is thin at the top end, and none dated 2025 or 2026 was found

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | Off-Page & Authority |

**Issue.** No independent editorial piece dated 2025 or 2026 was found. Phase 2 ran 25 freshness searches, and verification added three more angles (English-language news, awards, VivaTech/Le Parisien).

Dated coverage that was found, oldest first:
- franceinfo / France 3 Bourgogne-Franche-Comté: about 2018 ('en voie de commercialisation')
- Neozone: about 2018-2019
- ICI (France Bleu) Auxerre: 2020-09-03 ('le cartable révolutionnaire de la société Gravipack à Sens fait un carton')
- Le Matin (Morocco): 2020
- ICI (France Bleu): 2021-09-02
- Journal du Geek: 2021-09-04
- Objets du Futur: 2022-02-14
- Europe 1, Trophées de l'Avenir: 2023 candidate profile
- Maddyness: 2024-02-08
- ICI, 'La RATP innove avec les exosquelettes': about early 2024 (fits RATP's release of 29/02/2024)
- C8 'William à midi' segment on the Hiking bag: YouTube copy from June 2024

Undated:
- ICI's 'Les nouveaux inventeurs du concours Lépine' page on Gravipack, which ranked first for 'sac à dos anti mal de dos' in the extended sample. Its date is unknown and it could be recent; check it.
- A BFM TV segment hosted on the brand's Facebook page.
- The 'Samuel Etienne découvre…' video (owner unknown).
- Gomet, PresseSanté, Maginfrance, Challenge.ma and an FNH.ma interview with the founder.

Institutional mentions:
- the INPI Trophées 2022 finalist page;
- RATP pages, including VivaTech 2023 and a 2024 annual-report page that was probably published in 2025 (unverified).

The owned post slug '/gravipack-au-salon-vivatech-…-le-parisien/' suggests a Le Parisien article about VivaTech 2023 exists. So the accurate statement is 'few high-authority national titles found', not 'no national press or TV'.

The topic gap is clearer than the national one. No health, consumer, parenting or occupational-safety coverage appeared. A search on CPAM / Assurance Maladie / médecine du travail found nothing about Gravipack.

This is absence of evidence, not proof:
- The tool could not search eight major French press domains: Le Parisien, actu.fr, L'Yonne Républicaine, Ouest-France, francetvinfo, 20 Minutes, BFM and TF1info.
- Link velocity cannot be measured without DataForSEO, so this is not a finding about link velocity.

The brand itself is not inactive:
- a Decathlon marketplace promotion ran from 18/06 to 30/08/2026;
- YouTube uploads continued until about mid-June 2025;
- 2026 models are on pre-order: Business Talk V4 20 L (June 2026), Tokyo (mid-September 2026), Barracuda claie (mid-November 2026);
- there have been four KissKissBankBank campaigns (2020, 2022, 2023 SmartBag, 2024 children's bag);
- owned posts cover SOFINS, RATP and the Concours Lépine.
Meanwhile, the freshest third-party content about the brand is user-generated and partly negative. Trustpilot has 2026 reviews, including an unanswered June 2026 complaint about a refund.

**Evidence.** <https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://www.ici.fr/infos/transports/la-ratp-innove-avec-les-exosquelettes-5885238> · <https://www.ici.fr/emissions/les-nouveaux-inventeurs-du-concours-lepine/gravipack-le-sac-anti-mal-de-dos-8017902> · <https://www.ici.fr/infos/economie-social/la-nouvelle-eco-le-cartable-revolutionnaire-de-la-societe-gravipack-a-sens-fait-un-carton-1599115911> · <https://www.francebleu.fr/infos/economie-social/le-sac-a-dos-innovant-invente-par-un-icaunais-pour-soulager-les-dos-des-enfants-est-en-vente-1630589500> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://www.franceinfo.fr/france/bourgogne-franche-comte/yonne/innovation-le-sac-a-dos-qui-ne-fait-pas-mal-au-dos-en-voie-de-commercialisation_2822579.html> · <https://www.neozone.org/innovation/gravipack-le-sac-a-dos-qui-reste-leger-comme-une-plume-meme-quand-il-est-plein-a-craquer> · <https://www.europe1.fr/node/58664> · <https://lematin.ma/journal/2020/gravipack-permet-gra-bretelles-munies-dinserts-innovants-placer-sac-dos-apesanteur-epaules/329564.html> · <https://m.youtube.com/watch?v=rhduWNbpPko> · <https://www.facebook.com/gravipack/videos/le-sac-a-dos-gravipack-sur-bfm-tv/316225463587803/> · *(+8 more in findings/)*

**Why it matters.** Journalists, buyers and AI engines describe a brand from its most visible recent independent sources. With nothing new since 2024, they keep repeating 2018-2021 facts ('en apesanteur', 'en voie de commercialisation', patent counts, the 2019 pre-study), while sceptical forum and review content is fresher. claude-seo's GEO guidance treats brand mentions as more strongly correlated with AI visibility than backlinks. The product sits close to health topics (YMYL), so the most important gap is authority from health, consumer and parenting media.

**Effect on SEO.** New independent, dated coverage adds referring domains and brand mentions. It gives AI engines recent sources that describe the current range and the B2B use, and it helps push sceptical third-party results down the brand results page. In our samples the official home page sat only at #7 to #9 for 'gravipack', and the order changed between runs. The effects build over months; there is no quick ranking switch.

**How to fix.**

1. **Close the evidence gap first (half a day).** Check the 8 domains the tool could not search, the date of the ICI 'concours Lépine' page and the Le Parisien VivaTech 2023 article. Use Google News with `site:` filters, Europresse (through a library or BnF access) or a DataForSEO SERP call. Add every confirmed article to the coverage list.
2. **Make /dossier-de-presse/ the press hub.** It already exists, so do not create a new /presse/ URL. Add:
   - a dated list ('Ils parlent de nous', newest first) giving the medium, date, title and an outbound link for each article;
   - a downloadable kit with HD visuals and the logo;
   - a verified fact sheet: EXOSQUELETTE LIGHT SAS, 10 rue de la Paix 75002 Paris; founder Mohammed Errafi, président; founded 2018; awards with proof (INPI Trophées 2022 finalist, confirmed on inpi.fr; Concours Lépine 2018 silver medal as reported by Europe 1 and Neozone, with the official certificate if you have it);
   - a press contact.
   Remove unverified figures such as sales volumes and client counts.
3. **Publish every real event first as a dated owned post** in /actualites-gravipack-2/, so coverage has a source to link to. Show the publication date on the page. Use BlogPosting, not NewsArticle: NewsArticle gives a brand blog no Top Stories benefit. In Rank Math, set Titres & Méta > Articles > Type de schéma = Article (BlogPosting); Yoast outputs it by default. Expected output:
```json
{"@context":"https://schema.org","@type":"BlogPosting","headline":"Gravipack lance la claie de portage Barracuda","datePublished":"2026-11-16T09:00:00+01:00","dateModified":"2026-11-16T09:00:00+01:00","author":{"@type":"Organization","name":"Gravipack","url":"https://gravipack.com/"},"publisher":{"@type":"Organization","name":"Gravipack","logo":{"@type":"ImageObject","url":"https://gravipack.com/wp-content/uploads/[logo].png"}}}
```
   Update dateModified only when the content really changes; faking freshness goes against Google's guidance.
4. **Plan news hooks for the next 12 months.**
   - Late Oct-Nov 2026: Christmas gift guides.
   - Nov 2026: Barracuda claie deliveries and the 2026 range (Tokyo, Business Talk V4), for outdoor and tech media and as a Maddyness follow-up.
   - Q1 2027: the RATP story, if RATP validates updated figures (transport and HSE trade press, ICI Paris, Le Parisien).
   - Spring 2027: Concours Lépine / Foire de Paris, with a former-prizewinner angle.
   - June 2027: Semaine QVCT, with an occupational musculoskeletal (TMS) angle.
   - June-July 2027: back-to-school pitches for August-September publication.
   - 2027: SOFINS (held every two years) and Préventica, if exhibiting; ask to be listed in their exhibitor directories, which are indexed.
   - World Spine Day (16 October): too close for press in 2026, so use an owned post this year and pitch for 2027.
5. **Run data-led PR only once the evidence page exists.** Example: weigh pupils' bags with a partner collège, publish the method and data on gravipack.com, then pitch « Rentrée 2027 : combien pèse vraiment le sac de nos collégiens ? Nos mesures sur [n] élèves », with real numbers only. Pitch health, parenting and consumer titles (Santé Magazine, Top Santé, Magicmaman, Parents.fr) only after the evidence page and the health-claim clean-up are done. Brand searches already surface unanswered, unverified third-party forum allegations about the 2019 pre-study, and journalists will find them.
6. **Pitch in layers.**
   - Regional: ICI Yonne, ICI Paris, L'Yonne Républicaine, Le Parisien.
   - Business: Maddyness, Le Journal des Entreprises, Les Echos Entrepreneurs, L'Usine Nouvelle (the licensing model and French manufacturing, after checking the facts are current).
   - Trade: occupational safety, transport, defence.
   - Outdoor: Trekmag, Montagnes Magazine, an i-trekkings follow-up.
7. **Follow the rules.** Label any paid advertorial ('publi-rédactionnel') and give its links rel="sponsored". Never buy articles for links. Log every win in a sheet: URL, date, follow/nofollow, anchor, target URL.

- **First principle:** Authority and AI visibility follow independent, recent, citable mentions. Old coverage keeps its value, but when nothing new is published, journalists and AI systems recycle dated or unverified facts, and fresher sceptical content ends up defining the brand.
- **Do first:** `citable-evidence-page`, [#22 RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links](#22-ratps-own-pages-document-its-use-of-gravipack-but-this-has-not-been-turned-into-a-case-study-or-links), `owned-news-dating`, `ymyl-health-claims`
- **How we'll know the fix failed:** By 30 June 2027, Google Alerts and Talkwalker Alerts should show at least 3 new independent editorial articles dated 2026-2027. If not, the hooks are not newsworthy enough: rethink them (data, RATP, product) before spending more on outreach. The work has also failed if coverage appears but GSC Links shows no new referring domains, which means the articles do not link; apply the reclamation process. Finally, if AI answers to 'Gravipack, c'est quoi ?' still cite only 2021 sources after 6 months, the new coverage is not being picked up.
- **Leading indicator to monitor:** New independent articles per quarter (Google Alerts / Talkwalker Alerts for « Gravipack »); new referring domains in GSC Liens; GSC impressions for brand queries; share of sources from 2025 or later cited in ChatGPT and Perplexity answers to 3 fixed brand prompts.
- **To verify on-site:** Check /dossier-de-presse/: what it lists, whether entries are dated and linked, and whether a downloadable kit exists. Check that posts in /actualites-gravipack-2/ show visible dates and output BlogPosting/Article JSON-LD with datePublished and dateModified (view-source or the Rich Results Test). Check whether the owned SOFINS, RATP and Concours Lépine posts carry dates.

### 22. RATP's own pages document its use of Gravipack, but this has not been turned into a case study or links

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Low | likely | Off-Page & Authority |

**Issue.** RATP's own websites describe its use of Gravipack in more places than phase 1 found. A search restricted to ratpgroup.com and ratp.fr returned at least six RATP-owned pages and documents (eight URLs) that name Gravipack:
- the CSR page in French and English. The English page cites 'the exoskeleton backpack, developed by Gravipack, to alleviate the weight carried by staff in charge of infrastructure monitoring who walk along tracks';
- the VivaTech 2023 newsroom article and the VivaTech 2023 event page. They say close to 50 roaming maintenance workers were already using the backpack and that RATP planned to equip all track teams;
- the 'Cahiers d'expertise' innovation PDFs (FR and GB);
- an undated reportage in Askip', RATP's internal magazine;
- the 2024 annual-report (ASDR) 'development' page. The search returned it for 'Gravipack', but the passage itself was not seen. It was probably published in 2025, so verify the wording and the date.
RATP also repeats the brand's '92 %' figure. That is Gravipack's own number, not an RATP measurement.

Independent press backs this up. ICI's 'La RATP innove avec les exosquelettes' dates from about early 2024, which fits RATP's press release of 29/02/2024 on its arm exoskeletons. It mentions Gravipack backpacks for 'parcoureurs de voie' as a project under way.

On gravipack.com the same story is split across two undated news posts:
- /gravipack-au-salon-vivatech-cet-outil-de-pointe-au-service-des-voyageurs-et-des-agents-du-metro-le-parisien/ ('Sac à dos porte-outils exosquelette Gravipack des agents RATP');
- /le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/ ('Gravipack : le porte-outils anti-mal de dos utilisé par la RATP').
There is also an RATP video on the brand's YouTube channel (1Xq8EKyINTw). The VivaTech year behind the 'Le Parisien' post is 2023, when RATP had a stand. The Le Parisien article itself could not be searched because the tool cannot reach that domain.

Phase-1 notes record the owned post quoting '250 agents équipés', attributed to Le Parisien. RATP's own dated figure is about 50 (2023). The two numbers conflict.

No case-study or references URL (/cas-clients/, /references/) appeared in site: searches. An indexed /nos-clients/ page exists, but its content is unknown. It is also unknown whether any RATP page links to gravipack.com. RATP describes its own use and trials; nothing in the evidence amounts to an endorsement or recommendation, and the wording must stay at that level.

**Evidence.** <https://ratpgroup.com/en/heart-of-ratp-groups-csr-commitments/improve-quality-working-life-ratp-group-staff/> · <https://ratpgroup.com/fr/engagements-responsabilite-sociale-environnementale/exosquelettes/> · <https://www.ratp.fr/groupe-ratp/newsroom/innovation/le-groupe-ratp-vous-donne-rendez-vous-au-salon-vivatech-2023-pour> · <https://www.ratp.fr/en/groupe-ratp/vivatech2023> · <https://ratpgroup.com/api/media/ce_innovation_fr_dp-1.pdf> · <https://ratpgroup.com/api/media/ce_innovation_gb.pdf> · <https://askip.ratpgroup.com/reportage-gigp-garantir-la-continuite-preparer-lavenir/> · <https://ratpgroup.com/en/2024-asdr/development/> · <https://www.ratp.fr/en/discover/coulisses/daily-life/exoskeletons-ratp> · <https://www.ici.fr/infos/transports/la-ratp-innove-avec-les-exosquelettes-5885238> · <https://gravipack.com/gravipack-au-salon-vivatech-cet-outil-de-pointe-au-service-des-voyageurs-et-des-agents-du-metro-le-parisien/> · <https://gravipack.com/le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/> · *(+1 more in findings/)*

**Why it matters.** B2B and public-sector buyers (HSE managers, occupational doctors, procurement) look for proof that an organisation like theirs uses the product. A large transport operator describing, on its own sites, how its track staff use Gravipack is the strongest independent proof the brand has. It is dated, verifiable and separate from the brand's own health claims, which are disputed in brand search results. Today that proof is scattered across RATP's sites and two undated owned posts, one of which uses a figure that contradicts RATP's own. There is no structured reference page for 'Gravipack RATP', and no single clean source for sales teams or AI engines to point to.

**Effect on SEO.** Merging the two posts into one dated case-study URL ends the duplication between them. It gives the B2B hub, the outillage category and the porte-outils product pages a proof asset to link to. It gives AI answer engines a fact they can attribute and check against RATP's pages. Any link granted from ratpgroup.com or ratp.fr would be a high-authority, topically relevant referring domain, and even an unlinked RATP mention reinforces the brand entity. The most likely first gain is conversion: more trust on quote (devis) journeys.

**How to fix.**

1. **Inventory and check link status.** Save the RATP URLs above as `links.json` (`[{"source_url": "https://ratpgroup.com/fr/engagements-responsabilite-sociale-environnementale/exosquelettes/"}, ...]`). From a machine with network access, run `"$HOME/.claude/skills/seo/scripts/claude-seo" run verify_backlinks.py --target https://gravipack.com/ --links links.json --json`, then repeat with `--target https://gravipack.fr/`. Check the PDFs and the ratp.fr 'coulisses' story by hand. For each URL, log: does it link, the rel value, the anchor, and the date and figures it states.
2. **Get RATP's agreement before publishing.** Contact the RATP innovation/CSR team behind the VivaTech 2023 stand and the CSR page. Ask for:
   - permission to publish a case study naming RATP (use the logo only with written permission, as it is a registered trademark);
   - the current, citable figure (number of agents equipped, with a date);
   - a short quote from an operational sponsor;
   - a link from the FR and EN CSR pages to the case study or the home page.
   Do not count on links from archived newsroom pages or PDFs, which are rarely edited.
3. **Keep one URL, not two.** Check GSC (Performance and Links) for impressions or links on either post. If one has them, rewrite that post in place as the case study. If neither does, publish at `/nos-clients/ratp-agents-de-voie/`, a child of the existing /nos-clients/ page. Redirect the other post (or both) to it with the Redirection plugin (Outils > Redirection > Ajouter : URL source = old slug, URL cible = case study, type 301) on the canonical host. On Apache the equivalent is `Redirect 301 /le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/ https://gravipack.com/nos-clients/ratp-agents-de-voie/`. Do not leave the old posts live next to the new page.
4. **Write a dated, factual case study.** Suggested H1: « Cas client : le sac porte-outils Gravipack chez les agents de voie de la RATP ». Sections:
   - Le besoin: agents who walk along the tracks carrying their tools.
   - La solution: the model used, confirmed with RATP (probably the porte-outils 'outillage parcours').
   - Chronologie: prototype trials, then VivaTech 2023, then the current status as confirmed by RATP.
   - Ce que dit la RATP: the exact quote, with an outbound link.
   - Limites: label '92 %' as a Gravipack figure and link to the evidence page.
   Example copy: « En juin 2023, à l'occasion de VivaTech, le Groupe RATP indiquait que près de 50 agents de maintenance itinérants utilisaient déjà le sac porte-outils à exosquelette Gravipack, avec l'objectif d'en équiper l'ensemble des équipes de voie (source : ratp.fr). »
   Replace '250 agents' with RATP's dated figure unless RATP confirms 250 in writing. Never write « approuvé » or « recommandé par la RATP ». Embed the existing RATP YouTube video. Show « Publié le / Mis à jour le ».
5. **Add markup.** It helps entity clarity only; there is no rich result. In Rank Math or Yoast, set the schema type to Article, or add:
```json
{"@context":"https://schema.org","@type":"Article","headline":"Cas client : le sac porte-outils Gravipack chez les agents de voie de la RATP","datePublished":"2026-11-02","dateModified":"2026-11-02","author":{"@type":"Organization","name":"Gravipack","url":"https://gravipack.com/"},"mentions":{"@type":"Organization","name":"Groupe RATP","url":"https://ratpgroup.com/"},"citation":["https://ratpgroup.com/fr/engagements-responsabilite-sociale-environnementale/exosquelettes/","https://www.ratp.fr/en/groupe-ratp/vivatech2023"]}
```
   Use the real dates, and change dateModified only when the content changes.
6. **Link to it internally.** Use the anchor « cas client RATP » or « agents de voie de la RATP » from the B2B/entreprises hub, the outillage category, the porte-outils product pages, /devis/ and /dossier-de-presse/. Add a 'trust strip' on the home or B2B page only if RATP approves.
7. **Reuse it.** If RATP validates updated figures, a joint communication is a fresh news hook for transport, HSE and regional press (see press-coverage-freshness). Include the case-study link when you request links from the CSR pages and Askip'.

- **First principle:** Corroboration by a named, authoritative third party is worth more than any first-party claim. But search engines, AI systems and buyers can only use it once it is tied to the brand's own site through a dated, linkable page that states only what the third party said.
- **Do first:** `b2b-no-landing-hub`, `duplicate-cms-test-pages`, `citable-evidence-page`
- **How we'll know the fix failed:** If RATP refuses permission, drop the case-study framing. Publish only a short 'Références publiques' paragraph that quotes and links RATP's public pages, with no logo. Three months after publication, the page has failed as a search asset if GSC shows no impressions for queries containing 'ratp' or B2B terms and no quote request includes it in the session path. Six months after outreach, the link goal has failed if GSC Links shows no ratpgroup.com or ratp.fr linking site. In that case keep the page for conversion and stop chasing the link.
- **Leading indicator to monitor:** GSC impressions and clicks for queries containing 'ratp' and for B2B terms landing on the case-study URL; ratpgroup.com or ratp.fr appearing under GSC Liens > Principaux sites d'origine; GA4 key event 'devis' with the case study in the session path.
- **To verify on-site:** 1) Open both RATP posts. Confirm their content, any publication date, the '250 agents' wording and its stated source, and whether they cite RATP's pages. 2) Check /nos-clients/, /dossier-de-presse/ and the home page for RATP mentions or logo use. 3) Confirm which product RATP uses. 4) After the fix, check that the case study returns 200 on the canonical host, each old post returns a single-hop 301 to it, the page is in the XML sitemap, and the Article JSON-LD passes the Schema Markup Validator.

### 33. The backlink profile cannot be measured with the current tooling; no toxic patterns were seen in the sample

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | confirmed | Off-Page & Authority |

**Issue.** This audit ran at claude-seo backlink Tier 0. `backlinks_auth.py --check --json` returned tier 0 ('Basic (Common Crawl + Verify only)'):
- Moz, Bing Webmaster and Keywords Everywhere were unavailable (no API keys, no ~/.config/claude-seo/ directory);
- there was no DataForSEO connection;
- Common Crawl was excluded under this audit's constraints;
- the verification crawler could not reach the network.
The Backlink Health Score is therefore INSUFFICIENT DATA: 0 of 7 factors had data and the score is null.

This is a limit of the audit's tooling, not a defect on the site. It means referring domains, anchor text, lost links, broken link targets and competitor gaps were not measured. Whether Gravipack already uses Google Search Console or Bing Webmaster Tools is unknown.

What the sample does show: about 25 domains were found through search and checked against the 30 toxic-link patterns. None matched: no PBNs, link farms, hacked, casino or pharma pages, spun content, mass directories or site-wide footer links. The low-value items are harmless duplicates that Google most likely ignores:
- Motherbase on two subdomains (my. and beta.) with paginated variants;
- KKBB /en/ and /nl/ language copies;
- Fnac URLs with tracking parameters;
- ipad.auvieuxcampeur.fr;
- lespepitestech /node/17204;
- Leboncoin resale ads.
The French-language Moroccan press (lematin.ma, challenge.ma, fnh.ma) is relevant, not a language mismatch. presta.gravipack.com is Gravipack's own legacy store host, not a third-party link source.

**Evidence.** <https://moz.com/products/api> · <https://www.bing.com/webmasters> · <https://ahrefs.com/webmaster-tools> · <https://my.motherbase.ai/startup/107826-gravipack> · <https://beta.motherbase.ai/startup/107826-gravipack/> · <https://www.kisskissbankbank.com/nl/projects/gravipack-lesacadosenapesanteur/tabs/backers> · <https://ipad.auvieuxcampeur.fr/sac-a-dos-de-randonnee-sherpa-45.html> · <https://lespepitestech.com/node/17204> · <https://www.leboncoin.fr/ad/accessoires_bagagerie/3006309303> · <https://presta.gravipack.com/59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack>

**Why it matters.** Without link data, the business cannot see whether PR and reclamation work. It cannot spot lost links, or press links pointing at URLs that return 404 after the move from PrestaShop to WooCommerce. It cannot prioritise competitor gaps. And disavowing links without evidence would only throw away useful equity.

**Effect on SEO.** Indirect. Measurement does not change rankings by itself. It reveals wasted equity (links to 404s or legacy hosts that need 301s) and gives every off-page finding in this report a baseline. No penalty risk was detected, so a disavow file would bring no benefit.

**How to fix.**

1. **Google Search Console.** Verify gravipack.com and gravipack.fr as Domain properties (DNS TXT record at the registrar). In Liens, export 'Principaux sites d'origine', 'Pages les plus liées' and 'Texte d'ancrage principal'. This export is the baseline.
2. **Bing Webmaster Tools (free).** Import the sites from GSC or verify them by DNS (Bing has no 'Domain property'). Use the Backlinks report, which shows inbound links with anchors. Bing's index also feeds Microsoft Copilot.
3. **Ahrefs Webmaster Tools** (free for verified sites): referring domains, broken backlinks and anchors.
4. **Optional, for a scored claude-seo report.** Create `~/.config/claude-seo/backlinks-api.json` containing:
```json
{"moz_api_key": "…", "bing_api_key": "…"}
```
   Alternatively, set the environment variables MOZ_API_KEY and BING_WEBMASTER_API_KEY, or connect DataForSEO for link velocity and gap analysis. Then run `/seo backlinks gravipack.com`. A Tier 0 run with Common Crawl from an unrestricted machine is a free first pass.
5. **Recover wasted equity.** From 'Pages les plus liées', list linked URLs that return 404 or redirect to the home page. Redirect each one with a 301 to the closest live page:
   - on gravipack.com, with the Redirection plugin (one rule per URL, type 301);
   - on presta.gravipack.com, with server-level or Cloudflare rules on the presta host, kept for at least a year. Example:
```apache
# vhost presta.gravipack.com
RewriteEngine On
RewriteRule ^accueil/19-sac-a-dos-gravipack-sherpa-45\.html$ https://gravipack.com/produit/[slug-actuel-sherpa]/ [R=301,L]
```
   Do not send everything to the home page; Google treats that as a soft 404.
6. **Do not create a disavow file.** Re-run the toxic check (`/seo backlinks toxic gravipack.com`) once real data exists. Disavow only if a clear manipulative pattern or a negative-SEO spike appears (claude-seo flags a toxic share above 10 %). Never disavow presta.gravipack.com; redirect it.
7. **Monitor monthly.** Track new and lost referring domains and broken targets against the baseline.

- **First principle:** Off-page work cannot be managed if it cannot be measured. Missing link data does not mean there are no link problems, and finding no evidence of toxic links is not a reason to disavow.
- **Do first:** —
- **How we'll know the fix failed:** The measurement step has failed if, 30 days after setup, GSC Liens or Bing Backlinks still show no data for gravipack.com, or no baseline export exists; check the property type and verification. If the first real data shows a toxic share above 10 % or a sudden spike of spammy domains, the 'no disavow needed' conclusion was wrong; review it with /seo backlinks toxic.
- **Leading indicator to monitor:** Referring-domain count (GSC, Bing, Ahrefs Webmaster Tools) month over month; number of linked URLs returning 404; new versus lost referring domains.
- **To verify on-site:** Confirm whether GSC and Bing Webmaster properties already exist and who has access. Run curl -sI on the most-linked legacy URLs (presta.gravipack.com/*, gravipack.fr/*) to check for a single 301 to the matching page. Confirm whether Rank Math or Yoast and the Redirection plugin are installed.

## Brand & Reputation

**Score:** **30/100** — Home page only #6-#9 for "gravipack" in sampled results; "avis/arnaque" SERPs led by Trustpilot 3.1/5 (9 reviews, negatives unanswered incl. 2026), critical Outzer test and sceptical forums; on-site social-proof figures not corroborated (review-serps-unanswered, brand-serp, onsite-social-proof-claims).

**What works:**
- Owned LinkedIn and YouTube profiles rank on page 1 for the brand
- Positive independent reviews exist alongside the negative ones

### 3. Review and 'arnaque' searches surface critical content the brand has not answered (Trustpilot 3.1/5 with unanswered 2026 complaints, the Outzer review, sceptical forum threads)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟠 **High** | **7** | Medium | confirmed | Brand & Reputation |

**Issue.** Searches that combine the brand with 'avis', 'test' or 'arnaque' return mostly third-party pages. The tone is mixed: sceptical forum threads are prominent, and no brand reply is visible anywhere. These positions come from the search results we sampled, a US-located, non-Google index in extended mode, and are not Google.fr rankings.

**'gravipack avis'**
- #1 fr.trustpilot.com/review/gravipack.com
- #2 Fnac Hiking 33 Gris reviews
- #3 Outzer Sherpa 45 review
- #4 Fnac Road Adventure (8 reviews, about 3/5)
- #5 lespepitestech
- #6 ergo-corner
- #7 Tokyo product page, the first owned URL
- #8 i-trekkings test
- #9 randonner-leger thread 37663, page 2

**'gravipack arnaque'** (a query we built, so its search demand is not validated)
- #1 Trustpilot
- #2 i-trekkings ('Idée de génie ou arnaque ?', a favourable test)
- #3 Outzer, titled 'Gravipack Sherpa 45 : Un sac a dos terrifiant'
- #4 and #7 randonner-leger
- #5 the Outzer brand hub
- #6 rubypayeur (a stale Vincennes company listing)
- #8 franceverif ('site fiable')
- #9 a ScamAdviser page for gravipack.archemia.fr
- No owned URL appears.

**Standard-mode runs** (this mode under-represents gravipack.com, so treat 'no owned URL' with caution)
- 'gravipack sherpa avis test': Outzer, 4 randonner-leger threads and Trustpilot.
- 'gravipack arnaque efficace 92%': 8 randonner-leger posts and the KissKissBankBank FAQ. The FAQ is brand-written, not user content.
- 'gravipack étude Lyon' (also a query we built): 6 randonner-leger posts plus moodle.univ-lyon1, Maddyness and Europe 1.
- The same Gravipack threads (570298, 570316, 570392) also rank for generic queries: 'sac à dos qui soulage le dos et les épaules' and 'bretelles ergonomiques sac à dos soulager épaules'.

**Trustpilot**
- The profile has been claimed ('revendiqué') since December 2020, so the brand already has access.
- TrustScore 3 (3.1/5) from only 9 reviews. Ratings are polarised: 56 % 5-star and 33 % 1-star.
- No review has a reply, and no invitations have been sent 'for a long time'.
- A June 2026 review reports pain, a returned bag, no refund and two months without an answer. Another 2026 review calls the company dishonest for the same reason.
- Older complaints: straps coming loose from the fabric, a 3-month pre-order delay, a long wait for a custom order, and about a week of collarbone, shoulder-blade and hip pain after the GR20.
- Positive reviews praise durability, comfort and quick strap replacements under warranty.

**Outzer**
- One Sherpa 45 review (bought for about €240) reports a heavy bag, weak materials and neck pressure.
- The reviewer estimates the capacity at about 30 L rather than 45 L. That is an estimate, not a measurement.
- The reviewer also says the bag was 'conçu en Chine', contrary to the advertising.

**Forums**
- randonner-leger thread '[Sac à dos] gravipack: une vraie révolution?' (2020-2021, about 13 indexed URLs). Posts include '10 kg dans le sac, on en ressent 11' and 'rien sur PubMed', and argue the load moves to the lumbar area. Some posters call it 'publicité déguisée'; others call it 'un projet en développement'. The allegation about the study is covered in the study finding.
- forum.bushwalk.com (Australia, 2024): the 'weightless' bag weighs 890 g; one poster calls it 'just another con'.

**Positive signals the brand does not use**
- The i-trekkings 7-month test (Oslo 70 L on the GR5/GR51: no neck, back or hip pain; 2.4 kg).
- Decathlon: collection 4.1/5 (26 reviews); Hiking 33 4.13/5 (8 reviews).
- Positive Fnac and Trustpilot reviews.

**Owned pages that address these searches but do not rank for them:** /gravipackers/ (testimonials), /inventeur-dun-sac-a-dos-en-apesanteur/, the Concours Lépine post and the legacy presta.gravipack.com study page.

**Reassurance (Info):** more than 10 checks found no DGCCRF, ARPP, Que Choisir or signal-arnaques record about Gravipack. A signal-arnaques hit (#947856) cannot be tied to the brand; it most likely matched the keyword 'Trustpilot'. ScamDoc rates gravipack.com 86 % (first analysis 31/07/2020), and franceverif rates it 'site fiable'. The issue is unanswered criticism, not a fraud record.

**Evidence.** <https://fr.trustpilot.com/review/gravipack.com> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html> · <https://www.outzer.fr/avis/accessoires/gravipack/> · <https://www.randonner-leger.org/forum/viewtopic.php?id=37663> · <https://www.randonner-leger.org/forum/viewtopic.php?id=37663&p=2> · <https://www.randonner-leger.org/forum/viewtopic.php?id=37663&p=3> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=570392> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626080> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=627454> · <https://forum.bushwalk.com/forum/viewtopic.php?p=454212> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Gris/a16809921/avis> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · *(+9 more in findings/)*

**Why it matters.** People search for 'avis', 'arnaque', 'fiable' or 'test' just before they buy. Gravipack sells bags at roughly €90-€290 on health-adjacent claims. For that kind of product, Trust is the most important part of E-E-A-T, and Google's Quality Rater Guidelines tell raters to judge reputation from independent reviews. An unanswered June 2026 refund complaint in the #1 result tells a buyer that ordering is risky and that nobody will answer. A public, factual reply is also what every later reader sees, so one reply works for months. The positive material (i-trekkings, Decathlon 4.1/5, 5-star Trustpilot reviews) exists but is not linked from any owned page. AI answer engines that draw on these same pages may summarise the brand the same way. That is a hypothesis to test with an AI-visibility check, not established evidence.

**Effect on SEO.** The main effect is on click-through and conversion for brand + 'avis'/'arnaque' searches, and on the reputation signals behind Trust. It is not a direct ranking penalty. Replies turn the #1 Trustpilot result from a liability into proof of service. A substantial owned 'avis' page, built by upgrading an already-indexed URL, can earn a top-10 place for 'gravipack avis'. Product reviews collected from verified buyers on the site make product pages eligible for review snippets (Product aggregateRating). Third-party ratings never are.

**How to fix.**

1. **This week: settle the open cases before replying.** Find the June 2026 order and any other unrefunded return in WooCommerce > Commandes and issue the refund (Commande > Rembourser, through the payment gateway). The legal deadline is 14 days after the customer withdraws, and the refund can wait until the goods come back (art. L221-24 C. conso). If the buyer ordered from a marketplace seller (Kid'abord on Decathlon or Nature & Découvertes), arrange the refund with that seller.
2. **Within 7 days, reply publicly to all 9 reviews from the existing claimed account** (business.trustpilot.com > Avis > Répondre), starting with the 2026 refund complaints. Sign with a first name. Make no health promises. Never ask a reviewer to change a rating; Trustpilot lets them update the review once the case is resolved. Do not flag genuine negative reviews. French templates (fill the brackets; post the refund reply only once the refund has gone through):
   - Refund: « Bonjour [Prénom], merci d'avoir pris le temps d'écrire, et pardon : deux mois sans réponse après un retour, ce n'est pas acceptable. Nous avons retrouvé votre commande n° [xxxx]. Le remboursement de [montant] € a été effectué le [date] sur votre moyen de paiement d'origine. Si vous ne le voyez pas sous 5 jours ouvrés, écrivez-nous à [adresse SAV] avec ce numéro : je m'en occupe personnellement. [Prénom], service client Gravipack »
   - Pain or comfort: « Bonjour [Prénom], merci pour ce retour détaillé. Les bretelles se règlent selon votre taille et la charge, et un réglage inadapté peut créer des points de pression. Nous vous proposons un appel de 15 minutes pour vérifier le réglage ensemble [ou un échange de bretelles d'une autre taille]. Nos sacs ne sont pas un traitement médical : si la douleur persiste, parlez-en à un professionnel de santé. [Prénom], Gravipack »
   - Strap or quality defect: « Bonjour [Prénom], désolés que la sangle se soit détachée : c'est couvert par la garantie. Envoyez une photo et votre n° de commande à [adresse SAV], nous expédions la pièce de remplacement sous [x] jours. »
   - Delay: « Vous avez raison, [x] mois d'attente sur une précommande, c'est trop long et nous aurions dû vous prévenir. Les délais de livraison sont désormais datés sur chaque précommande : [lien]. » (only if true)
   - Positive: « Merci [Prénom] ! Ravis que le remplacement sous garantie ait été rapide. Bonnes randonnées avec votre [modèle] ! »
3. **Set a 48-hour reply standard.** Send Trustpilot alerts to the customer-service inbox and reply to every new review, positive or negative.
4. **Invite every buyer, with no filtering.** Install the official Trustpilot WooCommerce plugin and turn on automatic invitations (AFS), triggered when an order reaches 'Terminée', about 7-10 days after delivery. Alternatively, BCC the AFS address in the 'Commande terminée' email. Use one review platform; Trustpilot is the one that ranks first. Choosing which customers to invite breaks Trustpilot's rules. Art. L111-7-2 and D111-16 to D111-19 C. conso also require a public notice. Example: « Comment nous collectons les avis : tous nos clients reçoivent une invitation après livraison ; les avis sont publiés sans sélection, positifs comme négatifs, par Trustpilot, qui indique s'ils sont vérifiés. »
5. **Collect product reviews on the site.** In WooCommerce > Réglages > Produits, enable reviews, star ratings, the 'Propriétaire vérifié' label and 'avis uniquement par des propriétaires vérifiés'. Send a review-request email to every completed order (e.g. CusRev or a similar plugin). Use only these reviews for Product aggregateRating. Never mark up Trustpilot, Google or Fnac ratings, and never put a rating on the Organization or the home page; Google treats that as self-serving.
6. **Turn the existing /gravipackers/ page into the owned answer page** rather than creating a new URL; it already appears in brand searches.
   - New title and H1: « Avis Gravipack : avis clients et tests indépendants ».
   - Show each platform's rating as dated text with a link, low scores included: Trustpilot 3,1/5 (9 avis), Decathlon 4,1/5 (26), Google [x/y], Fnac.
   - Summarise the i-trekkings and Outzer tests fairly, with the brand's response: measured volume and measurement method, country of manufacture.
   - Add a section « Gravipack est-il fiable ? »: legal entity and SIREN, registered office, warranty, returns and refund process and deadlines, real delivery times, after-sales contact, links to the CGV and mentions légales.
   - Link to the evidence page about the 92 % claim and the study.
   - Add a footer link « Avis & preuves » and a link from every product page near the add-to-cart button.
   - FAQ content helps users and AI answers but earns no FAQ rich result for a commercial site. These were restricted in August 2023, and claude-seo records them as retired on 7 May 2026.
7. **Outzer:** post one courteous public response, using the comment or right-of-reply feature if Outzer offers one. Give the measured litre volume with its method and the countries of manufacture of the bag and the inserts, and offer the reviewer an exchange. Do not dispute the reviewer's experience.
8. **randonner-leger** (after the evidence page is live, and within the forum's rules on commercial posts): one post from a named account that discloses its affiliation. Example: « Bonjour, je suis [Prénom Nom], [fonction] chez Gravipack, je le précise d'emblée. Plusieurs questions de ce fil sont légitimes : ce que mesure exactement le chiffre de 92 %, le statut de l'étude de 2019 et le report de charge vers les lombaires. Nous avons publié les réponses, le protocole et ses limites ici : [URL]. Je réponds volontiers aux questions techniques. » Optionally, post an English version on bushwalk. Never use anonymous or fake accounts.
9. **Optional: lend units to independent testers** (i-trekkings, Outzer, outdoor YouTubers). Require clear disclosure under loi n° 2023-451, and never mark up incentivised reviews.
10. **Monitoring:** set up Google Alerts or Talkwalker Alerts for 'Gravipack' + avis/arnaque/escroquerie, and watch signal-arnaques, ScamDoc and Que Choisir. Check 'gravipack avis', 'gravipack arnaque' and 'gravipack fiable' monthly in a French rank tracker.

- **First principle:** Someone who adds 'avis' or 'arnaque' to a brand name already wants to buy and is looking for a reason not to. The results page answers with whatever exists. When a complaint sits unanswered at #1, the silence reads as the brand's answer. A public reply, steady fresh reviews and an owned page that links to independent tests change what that searcher finds.
- **Do first:** `study-evidence-page`, [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards), `measured-volume-origin-specs`
- **How we'll know the fix failed:** Check after 90 days. The fix has failed if: (a) any negative Trustpilot review still has no reply, or fewer than about 20 new reviews have come in although invitations are live; or (b) the upgraded /gravipackers/ page has no Search Console impressions for 'avis' queries and is not in the top 10 for 'gravipack avis' in a French rank check. If invitations are running non-selectively and the TrustScore stays at or below 3.5 on a larger sample, the problem is product or service quality, not visibility. Take it to operations and after-sales; more SEO work will not fix it.
- **Leading indicator to monitor:** Trustpilot share of reviews with a reply and median reply time, plus new reviews per month. In Search Console, impressions, CTR and position for queries matching the regex gravipack.*(avis|arnaque|fiable|test), and the position of /gravipackers/ for them.
- **To verify on-site:** - Read the live /gravipackers/ page: content, title, H1, and which host is canonical.
- Check the CGV clauses on returns, refunds and warranty, and the after-sales contact.
- Check whether a Trustpilot or review plugin is installed, and the review settings under WooCommerce > Réglages > Produits.
- Run the Rich Results Test on 3 product pages and confirm no aggregateRating is built from Trustpilot, Google or Fnac data.
- In Search Console > Performance, filter queries with gravipack.*(avis|arnaque|fiable) to see real Google.fr demand and the landing pages.

### 13. For 'gravipack', an obsolete 2020 crowdfunding page comes first and the home page ranked only #6-#9 in the results we sampled

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | Brand & Reputation |

**Issue.** All positions below come from the search results we sampled: a US-located, non-Google index in extended mode. They varied between runs and are not Google.fr rankings.

**Query 'gravipack', two runs**
- **Run 1:**
  - #1 KissKissBankBank /en/projects/gravipack (the 2020 campaign, in the English interface)
  - #2 LinkedIn company page
  - #3 YouTube @Gravipack
  - #4 YouTube /c/Gravipack
  - #5 equilibre-france-ergonomie (reseller blog)
  - #6 www /gravipackers/
  - #7 apex home page
  - #8 www Austerlitz product
  - #9 apex /nos-engagements/
- **Re-run:**
  - #1 KissKissBankBank
  - #2-#3 YouTube
  - #4 www /gravipackers/
  - #5 apex boutique
  - #6 www Austerlitz
  - #7 /nos-engagements/
  - #8 Hiking 30 L Gris
  - #9 apex home page
  - Owned URLs (site plus YouTube) took 8 of 9 slots.
- **What held in both runs:** the 2020 crowdfunding page was #1; the home page sat between #6 and #9 and was never the top owned result; apex and www URLs were mixed in the results.
- Earlier standard-mode runs that showed no gravipack.com URL at all are an artefact of that mode, which also missed gravipack.com on generic searches where extended mode ranked it. They are discarded.

**Other brand-modifier searches**
- **'gravipack prix':**
  - #1 Decathlon brand collection
  - #2 Fnac brand page (most listings out of stock)
  - #3 the 2023 KissKissBankBank SmartBag campaign 'à 89 €'
  - #4 /boutique-gravipack/
  - #5 www /boutique-gravipack/?order=price (a sorting-parameter duplicate)
  - #6-#8 Rome, Helsinki, G-Pack
  - #9 legacy presta.gravipack.com
- **'gravipack sac à dos':** #1 i-trekkings, #2 ergo-corner, #3 /nos-engagements/ (title 'GraviPack®' or 'Nos engagements'), #4 compostelle-autrement, #5 boutique, #6 home page.
- **'gravipack exosquelette':** works well, with 8 of 9 results owned and the home page at #3.
- 'gravipack avis' and 'gravipack arnaque' are covered in the review-SERP finding.

**The 4 KissKissBankBank campaigns**
- /projects/gravipack (ended 10/10/2020; 745 contributions; 1,437 % of goal, not 1,437 pre-orders; Sherpa 45 limited edition at 89 € instead of 149 €)
- gravipack-lesacadosenapesanteur (2022; 294 contributions; 962 %)
- the SmartBag campaign (2023; 618 contributions; 2,544 %; 89 € offer)
- the children's schoolbag campaign (2024; 100 contributions)

The 2020 and 2023 pages still advertise 89 € prices, while current store prices are higher (e.g. Sherpa 45 at €119-€149.90). KissKissBankBank support now redirects to Ulule, so asking the platform for edits is unlikely to work, but the project owner can still post news updates.

**Evidence.** <https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.kisskissbankbank.com/en/projects/gravipack-lesacadosenapesanteur/tabs/news> · <https://www.kisskissbankbank.com/en/projects/le-sac-a-dos-revolutionnaire-qui-allege-la-charge-de-92> · <https://www.kisskissbankbank.com/en/projects/gravipack-le-sac-a-dos-enfant-muni-d-exosquelette/tabs/backers> · <https://www.youtube.com/@Gravipack> · <https://www.youtube.com/c/Gravipack> · <https://fr.linkedin.com/company/gravipack> · <https://equilibre-france-ergonomie.fr/les-nouveaux-sacs-gravipack/> · <https://www.gravipack.com/gravipackers/> · <https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/> · <https://www.gravipack.com/boutique-gravipack/?order=price> · *(+6 more in findings/)*

**Why it matters.** People who type the brand name are the brand's highest-intent visitors. If a 2020 campaign page with an 89 € price is the first thing they see, some leave the official funnel or arrive with a wrong price in mind. When the home page sits at #6-#9 and is never the first owned result, search engines are not getting a clear signal about which URL is the brand's home. Duplicate apex and www URLs, an indexed legacy subdomain and a parameter duplicate all add to that noise. AI search tools that ground answers in non-Google indexes (Copilot through Bing, ChatGPT search) build their 'what is Gravipack' answer from the same top results.

**Effect on SEO.** Brand clicks leak to KissKissBankBank, retailers and reviews. Sitelinks and a knowledge panel become less likely, and AI answers are anchored on outdated third-party pages. On Google.fr the official home page may already rank first, which only Search Console can confirm. If it does, the problem is mostly about Bing and AI-index visibility, and severity should drop to Low.

**How to fix.**

0. **Measure before changing anything.**
   - In Search Console > Performance, filter the query to exactly 'gravipack', then to the regex ^gravipack. Note the average position, CTR and landing pages (home page vs /gravipackers/ vs others), split by host (apex vs www).
   - Run a manual google.fr check in a private window with &gl=fr&hl=fr, or use a French rank tracker.
   - In Bing Webmaster Tools (import the site from Search Console), check the same query, since Bing feeds Copilot.
   - If the home page is #1 on Google.fr with sitelinks, treat this finding as Low and do only steps 3-5.
1. **Consolidate the hosts** (host-consolidation finding). Keep whichever host Google already selects as canonical. Match WordPress Address and Site Address to it, then redirect the other host in one hop, path preserved:
```apache
# Only once the canonical host is confirmed (www shown as an example)
RewriteEngine On
RewriteCond %{HTTP_HOST} ^gravipack\.com$ [NC]
RewriteRule ^ https://www.gravipack.com%{REQUEST_URI} [R=301,L]
```
   - Let the SEO plugin's canonical tags send ?order= and other parameter URLs to the clean URL, and stop linking to sorted URLs.
   - Retire presta.gravipack.com with 1:1 301 redirects to the matching new URLs (legacy-presta finding).
2. **Home page title and site name.** Confirm the live title starts with the brand: one snapshot showed 'Gravipack : le sac révolutionnaire…', another 'Le sac bureautique ou randonnée révolutionnaire…'. Set it in Yoast or Rank Math (the static home page's SEO box) to « Gravipack® – Sac à dos à exosquelette | Site officiel » (53 characters). Output WebSite JSON-LD with name 'Gravipack' through the plugin's site-name setting (Yoast: Représentation du site; Rank Math: Titres & métas > SEO local) so Google can show the right site name.
3. **KissKissBankBank, all 4 campaigns.** As project owner, post a final news update on each, and add the store link to the creator profile wherever the dashboard still allows it. Example: « Cette campagne est terminée – merci à nos 745 contributeurs ! Les modèles et les prix actuels sont sur notre boutique officielle : https://[hôte canonique]/boutique-gravipack/. Garantie et SAV : [lien contact]. » Adjust the contributor count for each campaign.
4. **Make the owned URLs that already rank explicit.**
   - Give /nos-engagements/ a descriptive title, e.g. « Nos engagements : fabrication, garantie et SAV | Gravipack », and a meta description.
   - Turn /gravipackers/ into the reviews and independent-tests page (review-SERP finding).
   - Keep /boutique-gravipack/ consistent on price with the marketplaces.
5. **Point owned profiles to the canonical home page.** Rename the YouTube channel from 'Gravipack zero gravity backpack' to « Gravipack – sac à dos à exosquelette », and set its About links, the LinkedIn website field and the Instagram and Facebook bio links to the canonical home page. These profiles already hold #2-#4 on the brand query.
6. **Track monthly.** Do a brand results-page snapshot ('gravipack', 'gravipack prix', 'gravipack sac à dos') in a French rank tracker, plus the Search Console brand-query report.

- **First principle:** For a brand-name search, Google ranks the company's official home page first when it can clearly tell which URL that is. Splitting signals across apex and www, a legacy subdomain and parameter duplicates makes that harder. Meanwhile, old third-party pages with the brand name in their title match the query exactly and keep collecting clicks.
- **Do first:** `host-consolidation`, `legacy-presta-redirects`, [#29 Cart, sort and filter parameter URLs appear in the index (?add-to-cart=, ?order=, filter_product_cat=)](#29-cart-sort-and-filter-parameter-urls-appear-in-the-index-add-to-cart-order-filter_product_cat), [#3 Review and 'arnaque' searches surface critical content the brand has not answered (Trustpilot 3.1/5 with unanswered 2026 complaints, the Outzer review, sceptical forum threads)](#3-review-and-arnaque-searches-surface-critical-content-the-brand-has-not-answered-trustpilot-315-with-unanswered-2026-complaints-the-outzer-review-sceptical-forum-threads), [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards)
- **How we'll know the fix failed:** If step 0 already shows the home page at #1 on Google.fr, this finding is limited to Bing and AI indexes; retest it in Bing Webmaster Tools rather than keep changing the site. Otherwise, 8-12 weeks after host consolidation, the fix has failed if Search Console still shows the home page's average position above 2 for 'gravipack' with clicks split across apex and www, or if a French check still shows the KissKissBankBank page above the home page. That would point to an authority gap rather than a consolidation gap, and the next step is the PR and link plan.
- **Leading indicator to monitor:** In Search Console, the home page's average position and CTR for the query 'gravipack', and the share of brand-query clicks landing on owned URLs on one host. From a monthly French rank-tracker snapshot, the number of owned URLs in the top 5 for 'gravipack'.
- **To verify on-site:** - In Search Console, pull the brand-query data: position, CTR and landing pages per host.
- Check that a knowledge panel and sitelinks appear on a google.fr results page.
- Read the live home page title and its WebSite/Organization JSON-LD.
- Run `curl -sI` on / for both hosts to see which one returns 301 and which returns 200.
- Confirm that ?order= URLs carry a canonical to the clean URL.
- Check whether presta.gravipack.com still returns 200.
- Read the current titles of /nos-engagements/ and /gravipackers/.
- Check what the KissKissBankBank creator dashboard still lets you edit.

### 23. Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Low | confirmed | Brand & Reputation |

**Issue.** **What the registries say** (annuaire-entreprises.data.gouv.fr, societe.com, verif.com, Pappers): there is one company, EXOSQUELETTE LIGHT SAS, SIREN 840 543 383.
- Name history: created on 12/06/2018 in Sens as GRAVIBAG, renamed GRAVIPACK on 1 July 2022, then EXOSQUELETTE LIGHT (shareholders' meeting of 02/01/2025).
- Registered office: Sens (2018), then 46 rue de la Bienfaisance, 94300 Vincennes (end of 2022), then 10 rue de la Paix, 75002 Paris since 19/05/2026 (siège SIRET 840 543 383 00045).
- Share capital 16 960 €. President Mohammed Errafi since 2018. Active, with no employees declared.
- These are successive states of one company, so the address history is a timeline, not a contradiction. The mentions légales (indexed snippet: EXOSQUELETTE LIGHT, Paris, hosted by Gandi) already match.

**Still stale or inconsistent:**
- **Owned site:** two contact URLs, /contacts/ (apex) and /contact-gravipack/ (www), showing the Vincennes address in the phase-1 snapshot. The seller identity in the CGV has not been checked.
- **LinkedIn company page:** headquarters Vincennes and a size band of '201-500 employees', while the page's own structured data says 5 and the registry declares none. It has 1,850-1,884 followers.
- **Facebook:** places the brand in Sens, with the bio 'Sac a Dos en Apesanteur - Innovation Française'.
- **Four descriptors for one product:** the YouTube channel is named 'Gravipack zero gravity backpack', the 2023 KissKissBankBank campaign says 'SmartBag', Facebook says 'apesanteur' and the site says 'exosquelette'.
- **Model names:** Atlas 33 (Facebook), Hiking 33 (Decathlon, Fnac), Hiking 30 L (site).
- **Sales:** '500 000 clients satisfaits' on the site against '>20 000' sold in Maddyness (2024); see the social-proof finding.
- **Patents:** 13 (site, LinkedIn) against 9 (older founder posts, fnh.ma). The two counts are compatible: INPI's 2022 profile lists 1 French, 9 international and 3 pending. But no owned page shows the breakdown or any publication numbers.
- **Third-party listings** (not owned, but they can be claimed or corrected):
  - PagesJaunes pros/60790927 ('Gravipack à Vincennes - Maroquinerie', 0 reviews) and a duplicate, pros/62263007
  - Mappy entry at 46 r Bienfaisance
  - rubypayeur ('EXOSQUELETTE LIGHT à VINCENNES'), which ranks #6 for 'gravipack arnaque' in our sample
  - motherbase.ai (Vincennes), an AI-generated directory that appears in brand results
  - myfrenchstartup (company name GRAVIBAG)
  - lespepitestech (Sens, plus a 'French Tech Aix-Marseille Région Sud' tag with no registry basis)
- **Press attribution:** Journal du Geek (2021) calls it 'un sac conçu par Kid'abord'. Kid'abord is a separate company acting as licensee and marketplace seller ('vendu et expédié par KID'ABORD' on Decathlon and Nature & Découvertes). SODILOG in Colmar is the returns address for those listings. These are distribution roles, not competing identities, but no owned page explains them.

**Not real conflicts (no action needed):** the head-office moves; the Concours Lépine 2018 silver and the Ministry of Defence innovation silver, which are two separate claimed awards; the INPI Trophées 2022 profile saying 'Sens', which was correct at the time; forumeco's 'Gravibag, la SAS détentrice de la marque Gravipack', which is historically correct.

**Unknown:** /faq/ and /nos-engagements/ are indexed but we could not see their content, so we cannot say the site has no facts page. The existing about page (/a-propos-de-nous-gravipack-au-service-de-votre-dos/) is the right place for the facts; a new URL is not needed.

**Evidence.** <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383> · <https://www.societe.com/societe/exosquelette-light-840543383.html> · <https://www.verif.com/en/company/GRAVIPACK-68d9c0de12992303386f741e/> · <https://www.pappers.fr/entreprise/gravibag-840543383> · <https://gravipack.com/mentions-legales/> · <https://gravipack.com/contacts/> · <https://www.gravipack.com/contact-gravipack/> · <https://www.gravipack.com/a-propos-de-nous-gravipack-au-service-de-votre-dos/> · <https://www.gravipack.com/faq/> · <https://gravipack.com/nos-engagements/> · <https://fr.linkedin.com/company/gravipack> · <https://www.facebook.com/gravipack/> · *(+12 more in findings/)*

**Why it matters.** Google's Quality Rater Guidelines begin the Trust assessment with 'who is responsible for this website'. French law requires the site to identify its publisher (LCEN art. 1-1, since the loi SREN of 2024). Search engines and AI assistants reconcile company facts across sources. When LinkedIn says 201-500 staff in Vincennes, Facebook says Sens and the registry says Paris with no employees, answers either hedge or repeat the stale value. Forum sceptics also treat such inconsistencies as red flags. Gravipack is an e-commerce brand, not a local shop, so the gain is a clearer company identity rather than local ranking, and any knowledge-panel benefit is indirect.

**Effect on SEO.** Google's Knowledge Graph and AI assistants can resolve the company more cleanly ('Qui est derrière Gravipack ?', 'où est basée l'entreprise ?'), and fewer stale facts get quoted. It also produces the reliable references a future Wikidata item would need. Expect no direct ranking effect; the gain is in Trust and in how the brand is described.

**How to fix.**

1. **Write one internal master fact sheet** with an owner and a review date. It should cover:
   - legal name and former names with dates; SIREN and the registered-office SIRET
   - registered office and, if one exists, an operating or after-sales address, labelled as such. Whether 10 rue de la Paix is a domiciliation address is unverified, so don't present it as a shop.
   - founding date and place, and the president
   - the GRAVIPACK trademark (filed 27/05/2019 according to societe.com; add the registration number)
   - patents as a dated breakdown with publication numbers
   - awards (see the awards finding) and a sales figure with its date and source
   - distribution roles: Kid'abord as licensee and marketplace seller, SODILOG Colmar as returns logistics, other licensees only if confirmed
   - headcount, stated honestly
2. **Publish a dated « Gravipack en bref » block on the existing about page** /a-propos-de-nous-gravipack-au-service-de-votre-dos/. Check /faq/ and /nos-engagements/ first so nothing is duplicated. Example: « Gravipack® est une marque d'EXOSQUELETTE LIGHT SAS (anciennement GRAVIBAG puis GRAVIPACK SAS), SIREN 840 543 383, fondée le 12 juin 2018 à Sens (Yonne) par Mohammed Errafi, inventeur de l'exosquelette de bretelles. Siège social : 10 rue de la Paix, 75002 Paris (depuis mai 2026). Brevets : 1 français, 9 internationaux, 3 demandes en cours (au [date] ; n° …). Nos sacs sont vendus sur gravipack.com et, sous licence, par Kid'abord sur Decathlon.fr et Nature & Découvertes. Mise à jour : [date]. »
3. **Bring the mentions légales in line with LCEN art. 1-1.** Article 6-III no longer exists since 23/05/2024. Text: « Le site gravipack.com est édité par EXOSQUELETTE LIGHT, SAS au capital de 16 960 €, RCS Paris 840 543 383, siège social : 10 rue de la Paix, 75002 Paris. TVA intracommunautaire : FR[clé]840543383. Contact : [e-mail] – [téléphone]. Directeur de la publication : Mohammed Errafi, Président. Hébergeur : Gandi SAS, [adresse, téléphone]. Gravipack® est une marque d'EXOSQUELETTE LIGHT. » Use the same identity for the seller in the CGV and in WooCommerce > Réglages > Général > Adresse de la boutique, which appears on invoices and emails.
4. **Merge the contact pages.** Keep whichever of /contacts/ or /contact-gravipack/ has more links and traffic, and 301 the other to it (Rank Math > Redirections or the Redirection plugin). Show « Siège social : 10 rue de la Paix, 75002 Paris » and, if relevant, « Adresse SAV / d'exploitation : … ».
5. **Update the owned profiles within 2 weeks:**
   - LinkedIn: headquarters Paris 75002, the real size band (e.g. 2-10), website = the canonical home page
   - Facebook About: location and descriptor
   - Instagram bio
   - YouTube channel name and About, e.g. « Gravipack – sac à dos à exosquelette »
   - the KissKissBankBank creator profile
   - the Decathlon brand text, through the licensee
   - Pick one descriptor (« sac à dos à exosquelette ») and map the old names openly, e.g. « Atlas 33, aujourd'hui Hiking 33 » and « SmartBag (campagne 2023) ».
6. **Third-party listings:**
   - Claim the PagesJaunes listing with a free Solocal account, merge pros/62263007 into pros/60790927, change the category from 'Maroquinerie' to a backpack-manufacturing category, and update the address in step with the local SEO finding.
   - Ask for corrections at myfrenchstartup (company name), lespepitestech (remove the Aix-Marseille tag unless it is real) and motherbase.ai (address).
   - Registry-fed sites (rubypayeur, societe.com) update themselves.
   - Leave INPI's 2022 page as it is.
7. **Ask Journal du Geek for a one-line attribution fix**, only if it is accurate: « inventé par Mohammed Errafi (Gravipack), fabriqué et distribué sous licence par Kid'abord ».
8. **Use the same sheet for the Organization JSON-LD** on the home and about pages only, on the canonical host (this links to the schema finding). In recent Yoast versions: Réglages > Représentation du site > Organisation, including the extra organisation fields (legal name, founding date, VAT, ISO 6523). In Rank Math: Titres & métas > SEO local, plus the `rank_math/json_ld` filter for missing properties. Example:
```json
{"@context":"https://schema.org","@type":"Organization","@id":"https://www.gravipack.com/#organization","name":"Gravipack","legalName":"EXOSQUELETTE LIGHT","alternateName":["GRAVIPACK SAS","GRAVIBAG"],"url":"https://www.gravipack.com/","logo":"https://www.gravipack.com/wp-content/uploads/[logo].png","foundingDate":"2018-06-12","founder":{"@type":"Person","name":"Mohammed Errafi","jobTitle":"Président"},"iso6523Code":"0002:840543383","vatID":"FR[clé]840543383","address":{"@type":"PostalAddress","streetAddress":"10 rue de la Paix","postalCode":"75002","addressLocality":"Paris","addressCountry":"FR"},"sameAs":["https://fr.linkedin.com/company/gravipack","https://www.youtube.com/@Gravipack","https://www.instagram.com/gravipack/","https://www.facebook.com/gravipack/"]}
```
   Use whichever host the host-consolidation fix selects; www is only an example. Trustpilot, Decathlon and KissKissBankBank pages are weak sameAs targets.
9. **Optional: a Wikidata item**, only with independent references and a declared conflict of interest. Record past head offices with start and end dates rather than overwriting them.

- **First principle:** Search engines and AI systems resolve a company by checking the same facts across several sources. The newest fact wins only when the authoritative source states it and the other sources repeat it. Otherwise the most-repeated value wins, and here that is stale.
- **Do first:** `host-consolidation`
- **How we'll know the fix failed:** 60 days after the updates, ask ChatGPT (with search), Perplexity, Copilot and Gemini: « Où est basée l'entreprise Gravipack et combien de salariés compte-t-elle ? » and « Qui édite gravipack.com ? ». The fix has failed if answers still give Vincennes or Sens, 201-500 employees, or Kid'abord as the inventor. In that case, check which source each answer cites and correct it. Also re-check the tracked listings, since some directories re-import old data.
- **Leading indicator to monitor:** Share of tracked surfaces showing the current legal name, registered office and descriptor: the site's legal, contact and about pages plus about 12 profiles and listings. Target 100 %. Add a monthly spot check of 5 AI prompts.
- **To verify on-site:** - Read /mentions-legales/, /contacts/, /contact-gravipack/, the CGV, the about page, /faq/, /nos-engagements/ and the footer, and note every company fact they state.
- Ask the owner whether Vincennes is still an operating address and whether 10 rue de la Paix is a domiciliation address.
- Check the existing Organization JSON-LD (view-source or Rich Results Test) and which plugin outputs it.
- Before the 301, check which contact URL has backlinks and traffic (Search Console Links and Performance).

### 27. On-site social-proof figures ('4,7 sur Google' from 1,121-1,175 reviews, '500 000 clients satisfaits') are not independently verified

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Low | likely | Brand & Reputation |

**Issue.** Search snippets of gravipack.com pages, on both the apex and www hosts, show a '4,7' Google rating. Each page gives a different review count:
- 'plus de 1121 avis' (Hiking model)
- 'plus de 1126 avis' (Kingston)
- 'plus de 1175 avis' on a page titled 'Avis Google des clients Gravipack'

Pages seen with the rating: Rome, Hiking Terracotta, Kingston, Tokyo, Hiking Gris, Sherpa Kaki (on the /produit-gravipack/ path) and accessories (strap buckle, shoulder pads). The same pages claim '500 000 clients satisfaits'.

**Outside support for the rating is weak, but it exists.**
- An aggregator page reports 4.7/5 from 998 Google reviews for 'Gravipack - Vincennes' (groupe-ranque.fr/gravipack/). That page is titled 'Gravipack - Vincennes - Sécurité et Stockage Blindé', and phase 1 flagged it as a possible unrelated business with the same name.
- compostelle-autrement writes '4,8/5 sur Google avec déjà plus de 900 avis'. It may be repeating the brand's own figure.
- Counts of 900, then 998, then 1,121-1,175 fit a real Google Business Profile that keeps gaining reviews. But no Google Maps or Business Profile URL surfaced in our searches, and PagesJaunes shows 0 reviews.
- The accurate status is therefore 'not independently verified', not 'false' or 'first-party only'.

**Other platforms are lower, not contradictory:** Decathlon collection 4.1/5 (26 reviews), Decathlon brand page 3.88/5 (16), Trustpilot 3.1/5 (9), Fnac Road Adventure about 3/5 (8).

**'500 000 clients satisfaits' has no source** and is far out of scale with every other sales figure. Maddyness (February 2024) reports more than 20 000 bags sold, and other brand and press material says '20 000 sacs vendus'. 'Satisfaits' also implies a satisfaction measure that is never shown.

The site could not be fetched, so we could not check whether any of these figures feeds Product aggregateRating markup.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-exosquelette-professionnel-et-velo-rome-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · <https://www.gravipack.com/produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-avec-exosquelette-gravipack-pour-toutes-vos-aventures/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://groupe-ranque.fr/gravipack/> · <https://www.compostelle-autrement.com/post/gravipack-le-sac-a-dos-en-apesanteur> · <https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://fr.trustpilot.com/review/gravipack.com> · <https://www.decathlon.fr/vc/gravipack> · <https://www.pagesjaunes.fr/pros/60790927>

**Why it matters.** 1. **Credibility.** Three different counts typed into page text look made up to careful buyers, to forum sceptics who already question the brand's figures, and to AI systems that cross-check numbers. A '500 000' figure that is 25 times the documented '20 000' undermines every other claim on the page.
2. **French law.** Art. L111-7-2 and D111-17 C. conso require anyone who displays reviews to say whether and how they are checked. Unsupported figures can count as a misleading commercial practice (art. L121-2 C. conso).
3. **Structured data (conditional).** Google's review-snippet rules require product ratings to be about the specific product and collected on the page. Google reviews of the business are not product reviews, and Google ignores self-serving ratings on Organization or LocalBusiness markup. If a widget injects this 4.7 into Product aggregateRating, the site risks losing review rich results or a structured-data manual action.

**Effect on SEO.** These figures bring no ranking gain; the risk only runs the other way. Possible consequences: lost review snippets or a manual action if business reviews are marked up as product ratings; weaker Trust signals and 'conflicting ratings' in AI shopping answers; and a hook for a consumer complaint that would then rank for brand searches. A single dated figure with a source link removes all three risks.

**How to fix.**

1. **Trace the source.** In Google Business Profile Manager, confirm that the 'Gravipack' profile with about 1,100 reviews belongs to EXOSQUELETTE LIGHT, and note its current rating, count and address. If it is not yours (for example, if the Vincennes aggregator listing is a different business), remove every '4,7 sur Google' mention. The profile's eligibility (an online-only seller whose Vincennes address became outdated after the May 2026 move to Paris) is covered in the local SEO finding. Fix that first, because a suspended profile would make the figure vanish.
2. **Show one figure from one place.** Replace the per-product text with a single reusable block: a Gutenberg synced pattern, or a shortcode in the WooCommerce single-product template. Example: « ★ 4,7/5 sur Google – 1 175 avis au 1er octobre 2026 · Voir tous nos avis Google » linking to the profile's reviews. Update it monthly. Alternatively, use a widget that fetches the rating live with Google attribution and does not store review content beyond what Google Maps Platform terms allow.
3. **Check the markup.** Run the Rich Results Test on 3 product pages.
   - aggregateRating must come only from product reviews collected on that page (native WooCommerce reviews from verified owners).
   - If a Google-reviews widget plugin, or custom schema in Rank Math or Yoast, outputs aggregateRating or Review from Google reviews, turn that schema output off.
   - Never add a rating to the Organization or home-page markup.
4. **'500 000 clients satisfaits'.** Find every occurrence, for example with `wp db search "clients satisfaits" --all-tables` (the '500 000' may contain a non-breaking space).
   - Either source it with a dated count of orders across the store and its licensees, or replace it with a documented figure, e.g. « plus de 20 000 sacs vendus (chiffre 2024) ».
   - Drop 'satisfaits' unless a satisfaction survey with a stated method and date backs it.
5. **Add the review notice required by L111-7-2 / D111-17** next to every rating, or as a linked « Comment nous collectons les avis » page: « Les notes Google affichées proviennent de notre fiche Google [lien] au [date] ; Gravipack ne contrôle pas ces avis. Les avis produits publiés sur ce site sont réservés aux clients ayant acheté le produit (libellé « Propriétaire vérifié ») ; ils sont publiés sans sélection, positifs comme négatifs, et classés du plus récent au plus ancien. »
6. **Don't cherry-pick.** On the reviews page (see the review-SERP finding), show every platform's rating with its date, including Trustpilot 3,1/5, so the Google figure is seen in context.

- **First principle:** A rating typed into page text goes stale and drifts from its source. Once the same figure shows three counts and cannot be traced to a public profile, users, AI systems and regulators all treat it as unverified, and putting it in structured data breaks Google's review-snippet rules.
- **Do first:** `local-gbp-eligibility`, [#30 Product, Offer and review markup and the Merchant Center setup cannot be verified, and the Content API for Shopping has been sunset (verify on-site)](#30-product-offer-and-review-markup-and-the-merchant-center-setup-cannot-be-verified-and-the-content-api-for-shopping-has-been-sunset-verify-on-site)
- **How we'll know the fix failed:** The fix has failed if any rating shown on the site does not link to a source profile showing the same number (within a few reviews), or if the site still shows more than one count. It has also failed if the Rich Results Test still finds aggregateRating or Review markup built from Google reviews. If step 1 shows the Google profile is not Gravipack's, the only correct outcome is that the 4,7 claim is removed everywhere.
- **Leading indicator to monitor:** Number of distinct rating or count strings found by a site crawl (target: 1, dated and linked). Zero warnings in Search Console's Review snippets and Merchant listings reports.
- **To verify on-site:** - On each product page, find the '4,7 / plus de 11xx avis' element: is it a widget (which plugin?) or text typed into the product description or template?
- Check view-source and the Rich Results Test for aggregateRating or Review in the Product JSON-LD, and where it comes from.
- Find the page titled 'Avis Google des clients Gravipack'.
- Find every occurrence of '500 000 clients satisfaits'.
- In Business Profile Manager, confirm who owns the Google profile and its current count and address.

### 32. Awards are real but under-sourced, and the army and special-forces claims rest on founder statements and undated owned posts

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | likely | Brand & Reputation |

**Issue.** **Confirmed**
- **Trophées INPI 2022:** finalist in the 'Start-up' category, stated on inpi.fr's Gravipack profile and in INPI's list of 15 finalists for 2022.
- **Concours Lépine:** a 2018 silver medal is stated consistently by Europe 1 (Trophées de l'Avenir 2023 profile: 'médaille d'argent au concours Lépine 2018') and Neozone. No source gives 2017. The brand adds 'parmi 523 participants internationaux'. The legacy presta.gravipack.com page ('Médaille d'argent concours Lépine international') gives no year, and no official results list from the organiser was found.
- **Europe 1 Trophées de l'Avenir 2023:** nominee.

**Founder-sourced only**
- 'Testé par l'armée française' (Neozone) and 'l'armée de terre teste, en conditions réelles' (forumeco) are the inventor's statements relayed by the press.
- Only challenge.ma names the Légion étrangère (a 6-month test in 2017).
- A 2018 'médaille d'argent de l'innovation militaire' (Ministry of Defence silver) is relayed by Neozone, fnh.ma and challenge.ma without an event name.
- No Ministère des Armées or DGA document was found.

**Owned surfaces**
- The home page lists Armée de Terre, Légion étrangère, Préfecture de police, gendarmerie, pompiers and régions/départements as users.
- The YouTube channel has a playlist presenting an Army/Légion test.
- The founder's LinkedIn mentions 'invité d'honneur de deux salons militaires', 57 delegations, and 'intégré au sein de l'Armée française et des FS'.
- Blog posts:
  - /gravipack-soulage-les-forces-speciales-au-sofins/: exhibiting at SOFINS, an industry seminar, is not an endorsement, and 'soulage les forces spéciales' implies more than attendance. No third-party SOFINS page was found. Its /test/ duplicate is covered in the duplicate-pages finding.
  - /gravipack-presentees-au-salon-militaire-techterre-combat-futur/: our searches found no trace of a 'Techterre Combat Futur' show.
  - The two posts give different capacity ranges (20-100 L and 20-60 L), possibly for different products (needs a page check).
- The blog has dates (/articles/, 2022-2025), so 'undated' applies only to how these posts appear in search snippets.

**For contrast, a documented institutional reference:** RATP documents its own use on ratpgroup.com. Its CSR page names 'the exoskeleton backpack, developed by Gravipack', and its VivaTech 2023 pages report about 50 roaming maintenance workers equipped. So institutional-user claims are not all owned-only. The owned figure of '250 agents' still has to be reconciled with RATP's figure (RATP finding).

**Evidence.** <https://www.inpi.fr/trophees/gravipack-les-bretelles-qui-allegent-le-poids-sur-les-epaules-et-le-dos> · <https://www.inpi.fr/trophees/trophees-inpi-decouvrez-les-15-finalistes-du-millesime-2022> · <https://www.europe1.fr/node/58664> · <https://www.neozone.org/innovation/gravipack-le-sac-a-dos-qui-reste-leger-comme-une-plume-meme-quand-il-est-plein-a-craquer> · <https://forumeco.fr/gravipack-revolutionne-le-sac-a-dos/> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://www.challenge.ma/?p=271181> · <https://presta.gravipack.com/59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack> · <https://www.gravipack.com/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/> · <https://gravipack.com/gravipack-recompense-et-pret-a-conquerir-le-monde-du-portage/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/gravipack-presentees-au-salon-militaire-techterre-combat-futur/> · *(+4 more in findings/)*

**Why it matters.** Awards and institutional references are standard authority signals, but only when a reader can check them at the source. The INPI finalist status is the strongest third-party trust asset the brand has, and it is barely used. Vague military endorsements imply institutional backing. Under art. L121-4 C. conso, claiming that a public body approved a product when it did not is treated as misleading. On the brand's forum threads, sceptics already test claims like these, and an unverifiable one turns into evidence against the brand. Defence and public buyers also check references.

**Effect on SEO.** The SEO effect is small. A dated, sourced awards page gives journalists and AI engines quotable facts, supports Organization award markup and can earn links from inpi.fr or event organisers. Rewording the military claims removes a trust liability that sceptics could cite. Expect no direct ranking change.

**How to fix.**

1. **Create one « Distinctions & preuves » page**, or a section of the existing about page. For each item give the date, organiser, category, result and a source link:
   - « Trophées INPI 2022 – finaliste, catégorie Start-up » → link to the inpi.fr profile
   - « Concours Lépine International (Paris), 2018 – médaille d'argent [catégorie] » → a photo of the diploma or an attestation from the organiser (AIFF); link the Europe 1 profile until an official results list is found
   - « Trophées de l'Avenir Europe 1, 2023 – nommé » → europe1.fr
   - « Médaille d'argent [nom exact du concours d'innovation de défense], 2018 » → only with the exact event name and a document; otherwise leave it out
   - « Salon SOFINS [année] – exposant » → the organiser's exhibitor list
   - RATP → link RATP's own pages
2. **Reword the military claims to what is documented:**
   - « Présenté au salon SOFINS [année] » instead of « soulage les forces spéciales ».
   - « Prototype évalué en 2017 par des militaires de l'Armée de terre (retours d'essai internes, non publiés) » only with a written attestation. Otherwise remove the army test wording.
   - Remove « Légion étrangère », army insignia and institutional logos from the home page's user list and from the YouTube playlist title unless you hold written permission.
3. **Techterre 'Combat Futur' post:** add the organiser, date, place, a link and stand photos. If the event cannot be documented, unpublish the post and 301 it to the blog's military category. Use one capacity range in both posts, or name the product each range refers to.
4. **Dates and markup on news posts:** make sure every post shows a visible publication date and outputs BlogPosting or Article with datePublished and dateModified. Yoast and Rank Math do this for posts by default; check that the theme doesn't hide the date. Do not use NewsArticle, which brings no Top Stories eligibility for a brand blog.
5. **Organization markup:** add the award property, e.g. `"award": ["Finaliste des Trophées INPI 2022 (catégorie Start-up)", "Médaille d'argent, Concours Lépine International 2018"]`.
6. **Consolidate the award pages.** Move the presta Lépine page into the new page and 301 it there (part of the presta redirect plan). Link the two existing award posts (the Concours Lépine post and 'récompensé et prêt à conquérir…') to the new page.
7. **Ask for listings with a website link:** the SOFINS organiser's exhibitor directory, and the Concours Lépine organiser's winners list.

- **First principle:** An award or endorsement adds authority only when a reader or a crawler can verify it at the source. An institutional claim that cannot be checked becomes a liability as soon as a sceptic looks for proof.
- **Do first:** [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards), `legacy-presta-redirects`, `archives-test-duplicates`
- **How we'll know the fix failed:** The fix has failed if, 30 days after the page goes live, any award or institutional claim on the site still has no linked source, or if the Ministry of Defence silver medal or the 2017 army test is still stated without a named event or a document. It has also failed if AI answers to « Gravipack récompenses » still say 'testé par la Légion étrangère' or give 2017 for the Lépine medal, while omitting the INPI finalist status.
- **Leading indicator to monitor:** Share of award and endorsement claims on the site that link to a source (target 100 %). New referring links from inpi.fr, event organisers or exhibitor directories.
- **To verify on-site:** - List every page that mentions the army, Légion, special forces, Ministry of Defence, Lépine or INPI: home page, blog posts, product pages, the military category.
- Check the visible dates on the SOFINS and Techterre posts.
- Check which products the 20-100 L and 20-60 L ranges refer to.
- Check whether an Organization award property already exists in the JSON-LD.
- Ask the owner for the Lépine diploma, the exact defence-innovation award name and any written attestation of the 2017 tests.

## E-commerce & Marketplaces

**Score:** **30/100** — Marketplaces/resellers outrank gravipack.com for 4 of 5 model queries; no price parity (up to ~2.8x spread incl. struck reference prices); inconsistent specs and legacy model names across channels; marketplace ratings weak (model-serps-ceded, price-parity-reference-prices, product-data-consistency, marketplace-reviews).

**What works:**
- Broad distribution (Decathlon, Nature & Découvertes, Au Vieux Campeur, Fnac) gives demand-side visibility
- 83-product catalogue with clear use-case ranges

### 2. Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model names (Sherpa, Hiking 33, Feather, Business Talk)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟠 **High** | **7** | Medium | likely | E-commerce & Marketplaces |

**Issue.** **What we saw.** In the search results we sampled, third-party pages outrank gravipack.com for the brand's own model names, and for some models the official store does not appear at all. These positions come from a US-located, non-Google index in extended mode, which is closer to a real top 10. Brand results change between runs, so treat positions as indicative.
- **'gravipack sherpa' (run twice).** Positions #1-#6 are KissKissBankBank (2020 campaign), Trustpilot, KissKissBankBank (2022 campaign), the Decathlon Sherpa 45 listing, the Nature & Découvertes Sherpa bleu and the Au Vieux Campeur Sherpa 45. The first gravipack.com URL (Sherpa orange) is #7; it was #6 in the first run.
- **'gravipack hiking 33' (run twice).** decathlon.fr/vc/gravipack is #1 and KissKissBankBank #2. Three Fnac Hiking 33 listings with tracking parameters hold #3, #5 and #6, the Decathlon Hiking 33 listing #4, Équilibre France Ergonomie #7 and the Nature & Découvertes Hiking Terracota #8. The legacy presta.gravipack.com Hiking33 page is #9. The main store is absent from the top 10; it was #9 in the first run.
- **'gravipack feather cartable'.** The main store is absent. KissKissBankBank, Au Vieux Campeur, Nature & Découvertes (4 URLs), Fnac and Kiabi (2) rank, and only the legacy presta Feather page appears, at #10.
- **'gravipack business talk'.** The first owned URL (Business Talk V4 20 L) is #7, behind KissKissBankBank (2), Au Vieux Campeur, two YouTube videos (one from BFMTV) and Équilibre. The presta Business Talk page is #9.
- **'gravipack oslo 60+10' is the exception.** Owned pages hold #2-#4 behind the i-trekkings test. The Oslo has the same name everywhere and is rarely sold elsewhere.

**Three visible causes:**
1. **Names do not match.** Retailers and the legacy store say 'Hiking 33' and 'Sherpa 45'. gravipack.com says 'Hiking 30L gris', 'Hiking Terracotta', 'Sherpa bleu', 'Sherpa orange 45L' and 'Sherpa Kaki'. Its titles put the model last and often leave out the capacity, e.g. 'Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa' and 'Sac à dos exosquelette anti-mal de dos de montagne Hiking Gris Gravipack'. No official page contains the query term '33'.
2. **Some models are sold elsewhere but not on the official store.** Feather and Feather Plus are missing from the main store; only presta lists Feather, at 149 € 'en stock'. They are still sold by Decathlon (including Gravipack's own seller account, at 149 €), Nature & Découvertes, Au Vieux Campeur, Kiabi and Fnac. Road Adventure and Safar Vibe are still listed by Fnac, Decathlon or Nature & Découvertes, with no successor shown on gravipack.com.
3. **Legacy and crowdfunding pages keep ranking.** The four KissKissBankBank campaigns are the brand's own pages: /projects/gravipack (2020), gravipack-lesacadosenapesanteur (2022), the 2023 SmartBag campaign and the 2024 children's bag. All four end on a closed campaign instead of a current product. presta.gravipack.com still serves Hiking33, Sherpa 45, Feather, Business Talk, Road Adventure and Safar Vibe pages; the redirect plan for them is in the presta finding.

**Most models do have a successor, but no page says so:**
- Business Talk continues as Business Talk V4 (20 L, 25 L, 25 L EVA).
- Hiking 33 continues as Hiking 30 L gris and Terracotta.
- Sherpa 45 continues as Sherpa 45 L (bleu, orange, kaki).
- City Connect continues as City.
Only Feather, Road Adventure and Safar Vibe have no visible successor.

**Not every one of these clicks is lost.** Part of the Decathlon offer is sold by Gravipack's own account, and the KissKissBankBank pages are the brand's own.

**Evidence.** <https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.kisskissbankbank.com/en/projects/gravipack-lesacadosenapesanteur> · <https://www.kisskissbankbank.com/en/projects/le-sac-a-dos-revolutionnaire-qui-allege-la-charge-de-92> · <https://www.kisskissbankbank.com/en/projects/gravipack-le-sac-a-dos-enfant-muni-d-exosquelette> · <https://fr.trustpilot.com/review/gravipack.com> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-sherpa-bleu-gravipack-97687010> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-sherpa-45.html> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://www.decathlon.fr/vc/gravipack> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Cooper/a16809926/w-4?m=a750bda958&h=gig&bo=48737913&piddl=836768> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · *(+9 more in findings/)*

**Why it matters.** People who search 'gravipack + modèle' have already chosen the brand. These are the brand's highest-intent, highest-margin queries. When they land on a marketplace or a closed crowdfunding page:
- Gravipack loses the direct sale, or the licensee makes it;
- Gravipack loses the customer relationship;
- Gravipack loses control of the price, claims and specs the buyer sees.
Out-of-stock Fnac pages and legacy presta pages with old prices also make a poor first impression.

**Effect on SEO.** Model pages can win back #1 for 'gravipack <modèle>' queries when they:
- contain every name people search (current name, capacity, legacy name);
- get internal links with the model name as anchor text;
- absorb the presta and KissKissBankBank signals.
This also concentrates links and engagement on official URLs that are eligible for Product rich results and merchant listings, and it reduces how often out-of-stock third-party pages appear for the brand.

**How to fix.**

1. **One canonical URL per model**, with colours as WooCommerce variations (see the duplicate-products finding). Use a short slug, e.g. /produit/sherpa-45/ or /produit/hiking-30/.
2. **Model-first SEO titles and H1s that include the capacity**, set in Yoast or Rank Math:
   - `Sherpa 45 L – sac de randonnée à exosquelette | Gravipack`
   - `Hiking 30 L (ex-Hiking 33) – sac de randonnée à exosquelette | Gravipack`. First confirm that the Hiking 30 L is the bag retailers sell as Hiking 33, and settle the measured capacity (see the product-data finding).
   - `Business Talk V4 20 L – sac à dos ordinateur à exosquelette | Gravipack`
   - H1 example: `Gravipack Sherpa 45 L`.
   The titles finding decides the 'anti mal de dos' wording. Do not strip it site-wide here.
3. **Show the model's history on each product page**, in a visible line near the title and in the specs table. For example: « Anciennement Hiking 33 : c'est sous ce nom que vous le trouverez chez nos revendeurs (Decathlon, Au Vieux Campeur, Fnac). » Add the legacy name as `alternateName` in the Product JSON-LD. It has no rich-result effect, but it ties the names together.
4. **Publish a page « Nos modèles et leurs anciens noms »** at /modeles-gravipack/ with this table:
   - Hiking 33 → Hiking 30 L (gris, terracotta), en vente
   - Sherpa 45 → Sherpa 45 L (bleu, orange, kaki), en vente
   - Business Talk → Business Talk V4 (20 L, 25 L, 25 L EVA), en vente
   - City Connect → City, en vente
   - Feather / Feather Plus → to be decided (step 5)
   - Road Adventure, Safar Vibe → successor, or « modèle arrêté »
   Link the page from the footer and the shop.
5. **Decide what to do with Feather.**
   - Gravipack still sells Feather on Decathlon itself, so the default is to add a Feather / Feather Plus product page on gravipack.com (school bag; sizes under and over 1,55 m).
   - If Feather is really discontinued, publish « Gravipack Feather – modèle remplacé par … » with `availability: https://schema.org/Discontinued` and a link to the successor. Redirect it once its traffic fades.
   - Do the same for Road Adventure and Safar Vibe.
6. **Redirect each legacy-store product to its model page:** Hiking33 → Hiking 30 L, Sherpa 45 → Sherpa 45 L, Business Talk → Business Talk V4 20 L, Feather → the Feather page. The presta finding covers how to implement this and the rule that the presta host must keep serving the 301s.
7. **KissKissBankBank.** KKBB support is winding down and points to Ulule, so post the update yourself as the creator. Add a final news update to each of the 4 campaigns, for example: « Le projet est terminé : retrouvez le Sherpa 45 L et toute la gamme sur la boutique officielle → https://www.gravipack.com/produit/sherpa-45/ ». If the project page allows it, also point the creator website link to gravipack.com.
8. **Internal links.** Link every model page from the home page and from the matching category hub, with model-name anchors ('Sherpa 45 L', 'Hiking 30 L', 'Business Talk V4').
9. **Partner and own listings.** Retitle Gravipack's own Decathlon listings now, e.g. 'Gravipack Business Talk V4 20 L – sac à dos ordinateur à exosquelette'. Ask Kid'abord, Au Vieux Campeur, Équilibre, Ergo-Corner and Nature & Découvertes to use the same model names (content pack in the licensee finding).
10. **Measure in Google Search Console.** Under Performance > Queries, use the regex filter `gravipack.*(sherpa|hiking|feather|business|oslo|city|tokyo)` and track position and clicks per model. Also check the google.fr top 10 by hand once a month.

- **First principle:** Search engines rank the page that best matches the words people search. Shoppers search the names they see on retailer listings, receipts and old campaigns ('Hiking 33', 'Sherpa 45', 'Feather'). The official store uses different names, leaves names out, or does not sell those models at all, so the closest match is a marketplace.
- **Do first:** [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), `presta-legacy-subdomain`, [#21 Model names, capacities, weights and warranty terms conflict across channels, and some specs are publicly disputed](#21-model-names-capacities-weights-and-warranty-terms-conflict-across-channels-and-some-specs-are-publicly-disputed)
- **How we'll know the fix failed:** Check 8-12 weeks after the model pages and redirects go live:
- GSC still shows an average position worse than 3, or flat clicks, for 'gravipack sherpa', 'gravipack hiking' and 'gravipack business talk'.
- A manual google.fr check still shows no gravipack.com URL in the top 3 for 'gravipack hiking 33' and 'gravipack feather'.
If positions improve but clicks do not, the problem is how the result looks (title, price), not relevance.
- **Leading indicator to monitor:** Track:
- GSC impressions and average position for the 'gravipack + modèle' query group (regex filter), per model;
- the number of models where gravipack.com holds #1 in a monthly google.fr check. Baseline from this audit: 1 of 5 models (Oslo), in the sampled non-Google results.
- **To verify on-site:** Check the following:
- In GSC Performance, filter queries containing 'gravipack' plus each model name and note the landing pages and positions. This is the baseline.
- Search gravipack.com for any mention of 'Hiking 33', 'Feather', 'Road Adventure' or 'Safar Vibe'.
- Confirm internally that the Hiking 30 L is the same product as the retail Hiking 33, and whether Feather is still produced.
- Check which links the 4 KissKissBankBank project pages show.

### 17. Who sells, makes and services Gravipack products is not explained, and partner listings are partly outside the brand's control

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | E-commerce & Marketplaces |

**Issue.** Gravipack products reach buyers through at least three different companies. No owned page that surfaced in our searches explains who does what.

- **Brand owner.** EXOSQUELETTE LIGHT SAS (SIREN 840 543 383, 10 rue de la Paix, 75002 Paris) is registered under NAF 7740Z (licensing of intellectual property) and has no declared employees. In an fnh.ma interview, the founder says the brand and patents are licensed to Décathlon, Packcraft, Kid'abord and BSGroupe. This is his statement; Packcraft and BSGroupe were not checked.
- **Licensee and marketplace seller.** Kid'abord is a separate company that acts as licensee and marketplace seller.
  - On Decathlon.fr, the Sherpa 45, the Hiking 33 and most Feather offers are 'Vendu et expédié par KID'ABORD'.
  - On Nature & Découvertes, Kid'abord sells the Feather Plus and the Hiking Terracota, and returns go to 'SODILOG / RETOUR GRAVIPACK' in Colmar.
  - Journal du Geek (2021) describes Gravipack as a bag 'conçu par Kid'abord, une entreprise de Loire-Atlantique'.
- **The brand's own marketplace account.** Gravipack also sells on Decathlon directly: Business Talk (199 €) and one Feather noir offer (149 €) are 'Vendu et expédié par GRAVIPACK'. Part of the Decathlon content is therefore already under the brand's control, and opening a seller account as a fallback is not needed.
- **Manufacturing origin is unclear.** Third parties describe it differently: compostelle-autrement says 'conçu en France, fabriqué au Portugal ou en Chine', and an Outzer reviewer says 'conçu en Chine'. No owned page in the results states the origin.

**Partner listings diverge from the official line.**
- Decathlon titles carry 'Allège la charge de 92%' (Sherpa 45, Hiking 33, Feather, Pearl).
- Nature & Découvertes files hiking and school bags under /sacs-a-dos-velo/ (bike backpacks).
- The Decathlon brand page averages 3.88/5 (16 ratings), and the Feather noir is at 1.5/5.

**After-sales confusion is visible in the reviews that rank for the brand.** The Trustpilot profile has 3.1/5 from 9 reviews. It has been claimed since December 2020, and none of the negative reviews has a reply.
- A June 2026 review describes a returned bag with no refund and no answer for two months.
- A second 2026 review makes the same complaint.
- An earlier review reports an order that arrived three months late.
A buyer cannot tell whether to contact Gravipack, the licensee or the logistics provider.

**Not checked on the site.** gravipack.com could not be fetched from the audit environment. We could not check whether its CGV, mentions légales and product pages name the seller of record, the manufacturer and the returns handler. The mentions légales snippet shows only EXOSQUELETTE LIGHT (Paris) and the host Gandi.

**Evidence.** <https://www.decathlon.fr/vc/gravipack> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-pour-ordinateur-tout-terrain-et-urbain-business-talk/_/R-p-641ecc4b-c138-4681-a51f-6130c39aa4db> · <https://www.decathlon.fr/p/sac-a-dos-scolaire-et-sport-gravipack-feather-noir/_/R-p-5473954c-4430-4566-9a58-48f26aae66e5> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-scolaire-et-sport-feather-bordeaux/_/R-p-240aa9ce-f438-44e4-a44a-c817382b5517> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-outdoor-pearl-gris-allege-la-charge-de-92percent/_/R-p-edd34ad7-a944-424e-a8cd-45a0ffe9730a> · <https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-hiking-terracota-gravipack-97687020> · <https://fnh.ma/article/actualite-economique/mohammed-errafi-le-succes-doit-etre-collectif-pour-qu-il-ait-du-sens> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383> · <https://www.societe.com/societe/exosquelette-light-840543383.html> · <https://fr.trustpilot.com/review/gravipack.com> · *(+2 more in findings/)*

**Why it matters.** **Trust.** For online shops, Google's Search Quality Rater Guidelines look at who is responsible for the site, who sells and how customer service and returns work. Buyers ask the same questions about a 90-289 € product sold with health-adjacent claims.

**Law.** Two rules apply:
- The EU General Product Safety Regulation (Reg. 2023/988, art. 19), applicable since 13/12/2024, requires every distance-sale offer to show the manufacturer's name and postal and electronic address, plus product identification and safety information. This covers gravipack.com and marketplaces. If the manufacturer is outside the EU, an EU responsible person must also be shown.
- French distance-selling rules (C. conso. art. L111-1 and L221-5) require the seller's identity and contact details before the order.

If the 'dispositif médical' wording relayed in the press were ever adopted, an identifiable manufacturer under the MDR would also be needed (see the health-claims finding).

**Visible symptom.** The unanswered refund complaints that rank for the brand today come from buyers who do not know who is responsible.

**Effect on SEO.** This is not a direct ranking factor. The effects are:
- Clear seller, manufacturer and returns information supports Trust and conversion on product pages.
- A business identity that is the same in the CGV, the Organization and Product markup, and the Merchant Center business information reduces misrepresentation risk for merchant listings and free listings.
- Aligned partner titles, claims and categories mean the marketplace pages that hold many brand and model results repeat the official facts. That helps brand-SERP click-through and the facts AI answers repeat.
- A clear after-sales route reduces the new negative reviews that rank for 'gravipack avis'.

**How to fix.**

1. **Map the roles internally (about 1 day).** For each channel and product line, record:
   - the seller of record;
   - the GPSR 'fabricant', meaning the company that has the bag designed or made and markets it under its name or trademark (confirm with counsel for licensed products);
   - the EU responsible person, if the bag is made outside the EU;
   - the warranty guarantor;
   - the returns address (e.g. SODILOG Colmar);
   - the customer-service contact.
   This table is the single source for steps 2-7.
2. **CGV and mentions légales.** Add an article « Vendeur, fabricant, garanties et retours » to the CGV with:
   - the seller for gravipack.com orders: EXOSQUELETTE LIGHT SAS, 10 rue de la Paix, 75002 Paris, RCS Paris, SIREN 840 543 383;
   - the manufacturer;
   - the returns address and procedure, and the refund deadline (14 days, art. L221-24 C. conso.);
   - the 2-year garantie légale de conformité plus one Gravipack commercial-warranty duration, stated the same everywhere;
   - this paragraph: « Les produits Gravipack achetés chez un revendeur (Decathlon, Nature & Découvertes…) sont vendus par ce revendeur : retours et SAV se font auprès de lui. Sans réponse sous 7 jours, contactez-nous à [e-mail SAV]. »
   Keep the mentions légales identical (LCEN art. 1-1 since the 2024 loi SREN).
3. **GPSR block on every product page.** Add a « Fabricant et garanties » tab fed from product meta, so it is maintained in one place, in a child theme:
```php
add_filter( 'woocommerce_product_tabs', function ( $tabs ) {
  $tabs['gp_fabricant'] = array(
    'title'    => 'Fabricant et garanties',
    'priority' => 25,
    'callback' => function () {
      global $product;
      $html = get_post_meta( $product->get_id(), '_gp_bloc_fabricant', true ) ?: get_option( 'gp_bloc_fabricant_defaut' );
      echo wp_kses_post( wpautop( $html ) );
    },
  );
  return $tabs;
} );
```
   Example copy: « Vendu par : Gravipack – EXOSQUELETTE LIGHT SAS, 10 rue de la Paix, 75002 Paris – [e-mail SAV]. Fabricant : [raison sociale], [adresse postale], [e-mail]. Origine : conçu en France, fabriqué en [pays]. Retours et SAV : [adresse de retour], réponse sous 2 jours ouvrés. Garanties : garantie légale de conformité 2 ans + garantie commerciale Gravipack [X] ans ([lien conditions]). » Add the safety and care warnings.
4. **Structured data that says the same.** Product JSON-LD should carry `brand`, `manufacturer` and `offers.seller`. Declare the return policy at Organization level (`hasMerchantReturnPolicy`) or in Search Console's shopping settings. To extend the Product piece, use the `wpseo_schema_product` filter in Yoast WooCommerce SEO or `rank_math/snippet/rich_snippet_product_entity` in Rank Math. For example:
```json
{"@context":"https://schema.org","@type":"Product","name":"Gravipack Sherpa 45 L",
 "brand":{"@type":"Brand","name":"Gravipack"},
 "manufacturer":{"@type":"Organization","name":"[Fabricant]","address":{"@type":"PostalAddress","streetAddress":"[…]","addressLocality":"[…]","addressCountry":"[FR/PT/…]"}},
 "offers":{"@type":"Offer","price":149.90,"priceCurrency":"EUR","availability":"https://schema.org/InStock",
   "seller":{"@type":"Organization","name":"EXOSQUELETTE LIGHT (Gravipack)"}}}
```
   Make the Merchant Center business information (name, address, customer-service contacts, return policy) match the CGV.
5. **Licence and partner content pack.** Through the licence with Kid'abord and the reseller agreements, agree on:
   - the title template « Gravipack [Modèle] [capacité] L – sac à dos à exosquelette »;
   - specs and GPSR manufacturer data from the master product sheet (see the product-data finding);
   - claim wording approved against the evidence page, with no 'Allège la charge de 92%' until it is substantiated;
   - correct categories (randonnée, scolaire, ville; not 'sacs à dos vélo' at Nature & Découvertes);
   - recommended, not imposed, prices (see the price finding);
   - an after-sales SLA that says who answers reviews and refund requests, and within what time.
   Fix Gravipack's own Decathlon listings (Business Talk, Feather noir) first: they are fully in its control.
6. **Split the models between the two Decathlon accounts.** Agree which account lists which model, so Gravipack and Kid'abord do not run competing offers for the same bag (Feather noir at 149 € and at 90 €).
7. **Publish the list of authorised sellers** on the 'Où acheter' page (see the where-to-buy finding). Label each channel « vendu par Gravipack » or « vendu par Kid'abord, licencié Gravipack ».
8. **Answer the ranking after-sales complaints** (Trustpilot, June 2026 and later) and point buyers to the route from step 2 (see the reviews-SERP finding).

- **First principle:** Shoppers and quality raters trust a store when they can see who sells the product, who made it and who will take it back. Gravipack's licensing model spreads these roles across three or more companies. Unless the brand explains them, every refund dispute looks like the brand ignoring its customers.
- **Do first:** [#23 Company facts are stale or conflicting across the contact page and third-party profiles (legal name, seat, headcount, awards)](#23-company-facts-are-stale-or-conflicting-across-the-contact-page-and-third-party-profiles-legal-name-seat-headcount-awards)
- **How we'll know the fix failed:** This fix has failed if, 60 days after release, any of the following is true:
- A test buyer cannot find the seller of record, the manufacturer's address and the returns address within two clicks of a gravipack.com product page.
- New Trustpilot or Decathlon refund complaints still go more than 7 days without a reply.
- Gravipack's own Decathlon listings still carry '92%', legacy titles or a divergent warranty.
- **Leading indicator to monitor:** Track monthly:
- the share of known partner listings that match the content pack (title, category, claim, warranty), with a target of 100% on Gravipack's own Decathlon listings within 30 days;
- the median reply time to after-sales complaints on Trustpilot and Decathlon;
- the number of new 1-2 star reviews that mention 'remboursement', 'retour' or 'pas de réponse'.
- **To verify on-site:** Check the following on the live site:
- Open the CGV, the mentions légales and two product pages (Sherpa orange 45 L, Business Talk V4 20 L). Check that they state the seller of record, the manufacturer's name and postal and e-mail address (GPSR art. 19), the returns address and who handles returns, and a single warranty duration.
- Run the Rich Results Test and check the Product JSON-LD for brand, manufacturer and offers.seller.
- Check that Merchant Center > Business information and the return policy match the CGV.

### 20. Prices differ across channels and on gravipack.com itself, with struck 'reference' prices almost everywhere

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | likely | E-commerce & Marketplaces |

**Issue.** Prices are as shown in search snippets checked on 12/10/2026. We do not know when the snippets were captured, so some differences reflect timing.

**On gravipack.com itself, one model shows 2-3 prices:**
- Sherpa 45 L: bleu 119 € (struck 249 €), orange and kaki 149.90 €, orange 99 € in a promo list.
- Tokyo: 189 € on one page, 129 € (was 249 €) on another.
- Pearl: 89 € (was 99.90 €), and 119 € in a list.
- Rome: 94.90 € (was 119.90 €), and 119.90 € on its own page.
- Hiking: 89-89.90 €, with list prices of 229 € or 129.90 €.
- Earlier snippets also show the Austerlitz at 79.90, 89.90, 129 and 149.90 €, and the Oslo rouge at 289, 239.92 and 149.90 €.

**Struck 'reference' prices appear on almost every channel:**
- 229 € on the Hiking (Decathlon 129.90 €, Nature & Découvertes 129 €, Au Vieux Campeur 160.30 €);
- 249 € on the Sherpa;
- 299.90 € on the Helsinki (sold at 149 €);
- 149 € on the Austerlitz (89.90 €) and the Business Talk (129 €).
The pattern is long-running: the 2020 KissKissBankBank campaign sold the Sherpa 45 at '89 € au lieu de 149 €', and a 2026 brand result shows a 35 L military model at '89,90 € au lieu de 149 €'. A Decathlon Hiking 33 buyer calls the promotional price 'mensonger', and that review ranks.

**Across channels, the live spread is about 1.5x, not 2.6-2.8x.** The earlier 2.6-2.8x figure mixed live prices with struck reference prices (249 €) and a stale out-of-stock Ergo-Corner price (89.10 €).
- Live Sherpa offers cluster at 149-149.90 €: official orange and kaki, Nature & Découvertes orange, Ergo-Corner bleu and orange.
- Decathlon was at 149.90 € during its promotion of 18/06-30/08/2026; its current price is unknown.
- The outliers are 119 € (official bleu) and 174.30 € (Au Vieux Campeur).

**The brand's own Decathlon account does not match its own store:**
- Business Talk costs 199 € on Decathlon ('Vendu et expédié par GRAVIPACK') and 129 € (was 149 €) on gravipack.com.
- On the same marketplace, Feather noir is offered at 149 € by Gravipack and at 90 € by Kid'abord. The offer dates are unknown.
- The legacy presta store still shows Feather at 149 € 'en stock', while marketplaces sell it at 90-127 €.

**Other gaps:**
- G-Pack: 69.20 € at Ergo-Corner vs 89.90 € official.
- Tokyo: 109.90 € at Ergo-Corner vs 189 € or 129 € official.
- Austerlitz: 99.90 € at Ergo-Corner vs 89.90 € official.
- Business Talk: 139.30 € at Au Vieux Campeur (reference 199 €).
- City is at parity (129.90 €).
- A ProSportEquip snippet showing a Hiking 33 at 40.08 € is unverified.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://www.gravipack.com/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/boutique-gravipack/> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-pour-ordinateur-tout-terrain-et-urbain-business-talk/_/R-p-641ecc4b-c138-4681-a51f-6130c39aa4db> · <https://www.decathlon.fr/p/sac-a-dos-scolaire-et-sport-gravipack-feather-noir/_/R-p-5473954c-4430-4566-9a58-48f26aae66e5> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.decathlon.fr/r/mp/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/093a557b-159a-4282-95a8-76495a70d99e/c5> · <https://www.natureetdecouvertes.com/v/sac-a-dos-gravipack> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-hiking-33.html> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-ville-business-talk.html> · *(+8 more in findings/)*

**Why it matters.** **Consumer law.** Since 28/05/2022 (art. L112-1-1 Code de la consommation, ordonnance 2021-1734), any announced price reduction in France must use as its reference the lowest price charged in the 30 days before the reduction. Permanent 'was 229/249/299.90 €' prices are a DGCCRF risk. They also damage trust and feed the 'arnaque' narrative in brand results.

**Google.** The risk sits in Gravipack's own data. Merchant listings and Merchant Center check that the price in your feed and structured data matches your landing page. Several prices for one model on gravipack.com, cached promo lists and stale struck prices invite mismatches. Price differences between different sellers do not cause disapprovals by themselves.

**Effect on SEO.** One live price per model, with real dated promotions marked up correctly, has three effects:
- product pages stay eligible for merchant listings and Shopping, with correct price and sale annotations;
- price-mismatch warnings are avoided;
- a recurring trigger for negative reviews that rank for brand queries goes away.
It does not change organic rankings directly.

**How to fix.**

1. **Fix gravipack.com first.**
   - Export all products (WooCommerce > Produits > Exporter) and set one regular price per model and colour. If colours really have different prices, say why on the page.
   - Find where the extra prices come from: duplicate product URLs (see the duplicate-products finding), stale promo pages or blocks with hard-coded prices, and page-cache copies.
   - Delete or update the promo lists, e.g. the one showing the Sherpa orange at 99 €.
   - Purge the cache after every price change.
2. **Run promotions only with WooCommerce scheduled sale prices** (Prix promo → « Planifier », with start and end dates), so the regular price comes back automatically.
   - Set the struck price to the lowest price of the previous 30 days (L112-1-1).
   - Display it, e.g. « Prix le plus bas des 30 derniers jours : 149,90 € ». Several WooCommerce 'Omnibus' price-history plugins can do this.
   - Remove any struck price that was never actually charged.
3. **Mark up sales the way Google's merchant-listing documentation now asks:**
   - the active price in `price`;
   - the reference price as a `priceSpecification` with `priceType` StrikethroughPrice;
   - the sale period with `validFrom`/`validThrough`;
   - not `priceValidUntil`.
```json
"offers": {
  "@type": "Offer",
  "url": "https://www.gravipack.com/produit/sherpa-45/",
  "price": 129.00,
  "priceCurrency": "EUR",
  "availability": "https://schema.org/InStock",
  "validFrom": "2026-11-27T00:00:00+01:00",
  "validThrough": "2026-12-01T23:59:59+01:00",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "priceType": "https://schema.org/StrikethroughPrice",
    "price": 149.90,
    "priceCurrency": "EUR"
  }
}
```
   Check whether Yoast WooCommerce SEO or Rank Math outputs this; if not, extend their Product schema filter. In the Merchant Center feed, send `price` (regular price), `sale_price` and `sale_price_effective_date`.
4. **Align Gravipack's own Decathlon offers with the store** (Business Talk at 199 € vs 129 €). Decide with Kid'abord which account sells the Feather, so that offers at 149 € and 90 € no longer run side by side.
5. **Recommend prices to partners; never impose them.** Publish a prix de vente conseillé list and a shared promo calendar for Kid'abord and the resellers. Imposing minimum resale prices is prohibited: Code de commerce art. L442-6 since ordonnance 2019-359, and a hardcore restriction under Reg. (EU) 2022/720 art. 4(a). Get legal advice before adding any pricing clause. Remind partners that L112-1-1 applies to their struck prices too.
6. **Take a monthly price snapshot** of the official store, presta (until it is redirected), Decathlon (both sellers), Nature & Découvertes, Au Vieux Campeur, Fnac, Ergo-Corner, Kiabi and Bureau Vallée. Log each price with its date.

- **First principle:** A price is only credible if it is the same wherever the buyer meets it on your own site, and if the 'before' price was real. Buyers and Google both compare the price they see with the price they are charged.
- **Do first:** [#7 The same products are indexed under several URLs, including a second /produit-gravipack/ base and duplicated slugs and titles](#7-the-same-products-are-indexed-under-several-urls-including-a-second-produit-gravipack-base-and-duplicated-slugs-and-titles), `schema-merchant-center`
- **How we'll know the fix failed:** This fix has failed if, after 30 days, any of the following is true:
- A crawl of gravipack.com (Screaming Frog custom extraction of the price element) still finds more than one price for the same model and colour.
- The Search Console Merchant listings report or Merchant Center diagnostics show price-mismatch issues.
- A struck price is shown that is higher than the 30-day lowest price.
- **Leading indicator to monitor:** Track:
- the number of models with more than one live price on gravipack.com (target: 0);
- the number of Merchant Center 'price mismatch' items;
- the number of channels whose live price is within ±10% of the recommended retail price in the monthly snapshot.
- **To verify on-site:** Check the following:
- Crawl all product, category and promo pages and extract the displayed and struck prices.
- Compare them with Offer.price in the JSON-LD (Rich Results Test) and with the Merchant Center feed.
- Check whether struck prices match the 30-day lowest price, and whether sales use scheduled dates.
- Check the Feather price on presta.gravipack.com.

### 21. Model names, capacities, weights and warranty terms conflict across channels, and some specs are publicly disputed

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **5** | Medium | confirmed | E-commerce & Marketplaces |

**Issue.** The same bags are described with different names, capacities, weights, sizes and warranties across gravipack.com, the brand's other storefronts and retailers.

- **Hiking.**
  - Capacity: 33 L at Decathlon, Au Vieux Campeur, Équilibre, Fnac, Kiabi and on the legacy store ('Hiking33'); 30 L on gravipack.com ('Hiking 30L gris', 'Hiking Terracotta') and on one Fnac listing. A gravipack.com Hiking page whose URL says 30L has also been seen stating 33 L.
  - Weight: 900 g, 990 g or 1,200 g depending on the source.
- **Sherpa.**
  - Name: 'Sherpa 45' on presta, Decathlon, Au Vieux Campeur and Kiabi; 'Sherpa bleu', 'Sherpa orange 45L' and 'Sherpa Kaki' on gravipack.com; 'Sherpa 45L bleu/orange/kaki' at Ergo-Corner.
  - Weight: 1.2, 1.25 or 1.4 kg.
  - An Outzer reviewer estimates, without stating a method, that the Sherpa 45 holds about 30 L, and writes that it was 'conçu en Chine… contrairement à la publicité'. compostelle-autrement says the bags are designed in France and made in Portugal or China. The Outzer review ranks for 'gravipack sherpa avis'.
- **Feather.**
  - Laptop size: 14 inches on one listing, 15 inches on the brand page.
  - Weight: 780 g vs 890 g.
  - Size threshold between Feather and Feather Plus: '<1m50 et 30 kg' at Kiabi, '<1m55' elsewhere.
- **Pearl.** Bureau Vallée's title says '33 litres', but its URL says '29-litres'. Nature & Découvertes lists 'Pearl 29L'.
- **Oslo and Rome.**
  - Oslo: '60+10 L' and 2.9 kg on the official product page; '70 L' on other gravipack.com snippets, Ergo-Corner, i-trekkings and a rental listing (2.4 kg).
  - Rome: 1.6 kg vs 1.9 kg across gravipack.com pages.
- **Warranty.** '1 an' appears on the gravipack.com school category snippet, the official Sherpa Bleu listing, the Ergo-Corner Sherpa kaki page and the gravipack.ma bureautique category. '10 ans' appears in the KissKissBankBank FAQ, at Équilibre and on other brand pages.
- **Broken prices.** Kiabi's indexed titles show '0.00€' or 'nu€' for the Feather, Feather Plus, Sherpa 45 kaki, Pearl Gray and an unavailable Hiking 33.
- **Name changes.** Business Talk became Business Talk V4 (20 L, 25 L, 25 L EVA). gravipack.ma uses yet other names (Trek Air 25L, Summit Air 35L, Sherpa Peak 50L, Dublin).

**Covered elsewhere or not actionable:**
- Duplicate gravipack.com URLs are handled in the duplicate-products finding. The two G-Pack URLs may be two different products.
- Fnac's indexed URLs with junk parameters are Fnac's problem; Gravipack cannot fix them.
- Cdiscount's /r-gravipack.html internal search page appeared only in domain-filtered searches.

We could not check whether gravipack.com and marketplace listings carry GTINs.

**Evidence.** <https://gravipack.com/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://presta.gravipack.com/accueil/19-sac-a-dos-gravipack-sherpa-45.html> · <https://equilibre-france-ergonomie.fr/produits/sac-a-dos-hiking-33-baroudeur-et-leger/> · <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://www.ergo-corner.com/gravipack/676-sherpa-45l-kaki-avec-exosquelette-gravipack-.html> · <https://gravipack.ma/categories-de-produits/sac-a-dos-bureautique/> · <https://www.kiabi.com/sac-a-dos-gravipack-sherpa-45-kaki-kaki_P1443012C1443014> · <https://www.kiabi.com/sac-a-dos-gravipack-feather-plus-noir-noir_P1459548C1459549> · <https://www.bureau-vallee.fr/gravipack-sac-a-dos-pearl-29-litres-gris-405222788.html> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html> · *(+2 more in findings/)*

**Why it matters.** Specs are what buyers compare and what reviewers test. When the 'Sherpa 45' is estimated at about 30 L, or the warranty is 1 year on one page and 10 years on another, the brand looks unreliable, returns increase, and the contradiction is what reviews and AI summaries repeat. Google's shopping systems and AI answer engines match products by brand, name and identifiers: GTIN first, with brand plus MPN as a fallback. Conflicting names and specs make it harder to tie all offers and reviews to one product.

**Effect on SEO.** One master data set with GTINs, pushed to every channel:
- improves offer matching in Google's Shopping Graph;
- reduces contradictory facts in AI answers;
- gives the official pages a specs table others can cite;
- removes the spec disputes that keep critical reviews relevant for 'gravipack <modèle> avis' queries.

**How to fix.**

1. **Build one product master sheet.** A shared Google Sheet is enough, with one row per model and variation. Columns:
   - official name, plus legacy and retailer names;
   - GTIN-13/EAN and MPN/SKU;
   - capacity in litres, measured with a stated, repeatable method (e.g. filled with small balls of known volume, with pockets listed separately);
   - weight with and without the exoskeleton, and dimensions;
   - laptop size;
   - user height and weight range, and the fitting tolerance (±10 cm / ±8 kg);
   - materials and origin wording;
   - warranty;
   - GPSR manufacturer.
2. **Settle the disputed values first.** Measure the Sherpa 45 and the Hiking. If the Sherpa holds less than 45 L, either rename it or state what the figure includes, e.g. « 45 L poches comprises, [x] L compartiment principal ».
3. **Use accurate origin wording on each product page**, e.g. « Conçu en France (exosquelette breveté), fabriqué au [pays] ». Write only what is true and documented.
4. **Use one warranty statement everywhere:** « Garantie Gravipack [X] ans sur l'exosquelette et les bretelles + garantie légale de conformité de 2 ans ». Fix the school category description, the Sherpa Bleu page and gravipack.ma first.
5. **Set up WooCommerce.**
   - Enter GTINs in the native « GTIN, UPC, EAN ou ISBN » field (Données produit > Inventaire, WooCommerce 9.2+, also per variation).
   - Make sure Yoast WooCommerce SEO or Rank Math and the feed plugin output it as `gtin13`.
   - Store capacity, weight and laptop size as global attributes (Produits > Attributs), so the same values feed the specs table, the schema and the feed.
6. **Push the sheet to every channel:**
   - Gravipack's own Decathlon listings, now;
   - Kid'abord, through the licence;
   - Ergo-Corner, Équilibre, Au Vieux Campeur, Nature & Découvertes and Fnac;
   - Bureau Vallée: correct the Pearl volume;
   - Kiabi: fix the 0.00 € offers or delist the discontinued items;
   - gravipack.ma.
7. **Publish the measured values and the method** in a specs table on each product page. Link to it in the reply to the Outzer review (see the reviews-SERP finding).
8. **Re-check every quarter** for the five best-selling models across the top channels.

- **First principle:** A product is one thing. If every channel describes it differently, buyers, reviewers and machines cannot tell which description is true, and they default to the most critical one.
- **Do first:** —
- **How we'll know the fix failed:** This fix has failed if, after 60 days, any of the following is true:
- A spot check of the five main models on gravipack.com and five channels still finds different capacities, weights or warranty terms.
- Kiabi titles still show 0.00 €.
- Merchant Center reports missing or invalid GTINs for active products.
- **Leading indicator to monitor:** Track:
- the number of conflicting values per model across the tracked channels. Baseline: Hiking has 2 capacities and 3 weights, and the warranty reads 1 year vs 10 years on 4 or more pages;
- the share of active products with a valid GTIN in Merchant Center.
- **To verify on-site:** Check the following:
- Compare every product page's specs (capacity, weight, laptop size, warranty, origin) with the master sheet.
- Check the school category description and the Sherpa Bleu page for '1 an'.
- Check whether GTINs exist in WooCommerce and appear as gtin13 in the Product JSON-LD and the feed.
- Check whether the Hiking Gris page text says 30 L or 33 L.

### 26. Marketplace ratings are weak and split across legacy model names (Decathlon brand page 3.88/5, Feather noir 1.5/5, Fnac Road Adventure about 3/5)

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Medium | confirmed | E-commerce & Marketplaces |

**Issue.** Ratings on marketplaces are modest, few in number and attached to names gravipack.com no longer sells.

- **Decathlon.**
  - The brand page vc/gravipack averages 3.88/5 (16 ratings), and the collection page 4.1/5 (26).
  - Hiking 33: 4.13/5 (8). Buyers say the adjustment is hard and that the straps rub the neck when the bag is lightly loaded. One buyer got custom straps after contacting the brand, and one calls the promo price 'mensonger'.
  - Feather noir: 1.5/5. Feather Plus gris: 4.5/5, from very few reviews.
- **Fnac.**
  - Road Adventure Noir: about 3/5 from 8 reviews (finish, size).
  - Feather Plus: 1/5 from 1 review (strap discomfort). Safar Vibe: 5/5 from 1. Hiking 33 Gris: 1 review. Feather Bordeaux: 2 reviews.
  - Fnac review pages ranked #2 and #4 for 'gravipack avis' in the results we sampled.
- **Au Vieux Campeur.** Feather has 0 reviews. Hiking 33 has 1 review, positive on value but noting little back-panel padding.
- **Amazon.fr.** No listing was found in 2 searches.

**The names do not match the current range.** Hiking 33, Road Adventure, Safar Vibe and Feather do not match gravipack.com's current range (Hiking 30 L, Tokyo, Kingston, G-Pack), so a buyer cannot tie these reviews to products on the official site. Business Talk is the exception: it continues as V4.

**Gravipack can reply only on its own offers.** It can respond as the seller only on offers sold through its own Decathlon account (Business Talk, one Feather noir). Kid'abord sells the Sherpa 45, the Hiking 33 and most Feather offers, so replies there need the licensee's cooperation.

**Some first-party proof exists.** A /gravipackers/ testimonials page is indexed; it ranked #4 for 'gravipack' in one run.

**Covered elsewhere:**
- Whether product pages carry on-site reviews and AggregateRating is checked in the schema/Merchant Center finding.
- Trustpilot (3.1/5, 9 reviews) is covered in the review-SERP finding.

**Evidence.** <https://www.decathlon.fr/vc/gravipack> · <https://decathlon.fr/browse/b/gravipack/_/N-19o8oxe> · <https://www.decathlon.fr/r/mp/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/093a557b-159a-4282-95a8-76495a70d99e/c5> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-scolaire-feather-noir-allege-la-charge-de-92percent/_/R-p-5473954c-4430-4566-9a58-48f26aae66e5> · <https://www.fnac.com/Sac-a-dos-Gravipack-Road-Adventure-Noir/a16167915/avis?qui=d4e5a2e925&thinga=03ed2700&l=e07c3281&t=3ce8763e> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Gris/a16809921/avis> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-hiking-33.html> · <https://www.gravipack.com/gravipackers/> · <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/>

**Why it matters.** Marketplace ratings appear in marketplace search, in Google results for those listings and in AI shopping answers. A 1.5/5 or 3/5 on a discontinued SKU shapes opinion of the current range. Replies show prospects that problems get solved. The Hiking 33 complaints are about strap adjustment, and the brand already offers a fix for that (adjustment guide, custom straps).

**Effect on SEO.** The effects are indirect:
- Better ratings, with replies, improve click-through on marketplace and brand results and improve the sentiment AI answers summarise.
- Mapping legacy SKUs to current models lets the review history support the current products.
- On-site verified reviews, if displayed with AggregateRating, can earn review stars for gravipack.com product results.

**How to fix.**

1. **Reply where Gravipack is the seller** (Business Talk and Feather noir on its own Decathlon account), within a week and in French, with the fix. For strap rubbing, for example: « Merci pour votre retour. Les bretelles se règlent selon votre taille et votre poids : voici le guide pas à pas [lien vers /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/]. Si le frottement persiste, écrivez-nous à [e-mail SAV] avec votre numéro de commande : nous ajustons ou échangeons les bretelles. »
2. **Agree in the licence who replies to reviews on Kid'abord listings, and how fast.** Use the same templates. Start with the Feather noir (1.5/5) and the 'prix mensonger' review, and also fix the promo practice behind it (see the price finding).
3. **Map legacy SKUs to current models** using the lineage page (see the model-SERP finding). Ask Fnac and Kiabi either to delist discontinued SKUs or to relist current models with GTINs, so new reviews land on current products.
4. **Collect on-site reviews from every buyer, without selection.**
   - In WooCommerce > Réglages > Produits, tick « Activer les avis produits », « Afficher le libellé 'propriétaire vérifié' sur les avis client » and « Les avis ne peuvent être laissés que par des 'propriétaires vérifiés' ».
   - Send one review request to every customer about 3 weeks after delivery. Do not tie any incentive to a positive rating.
   - If you use a provider (e.g. Avis Vérifiés/Skeepers or Trustpilot product reviews), choose one that can feed Google's Product Ratings and, where supported, syndicate to marketplaces.
   - State next to the reviews whether and how they are checked, as art. L111-7-2 C. conso. requires.
5. **Mark up only reviews that are visible on the page** with AggregateRating. Never mark up Google or Trustpilot ratings (see the schema finding).
6. **Ask satisfied B2B and repeat customers** (e.g. the people featured on /gravipackers/) to review the model they bought, on the channel where they bought it.
7. **Treat Amazon.fr (with Brand Registry) as a later business decision**, once names, data and prices are aligned.

- **First principle:** Shoppers judge a product by the ratings next to it. Ratings that are split across retired names and left unanswered tell a worse story than the product deserves. Only a steady flow of fresh, unfiltered reviews on current models replaces them.
- **Do first:** [#2 Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model names (Sherpa, Hiking 33, Feather, Business Talk)](#2-marketplaces-resellers-and-old-crowdfunding-pages-outrank-gravipackcom-for-its-own-model-names-sherpa-hiking-33-feather-business-talk), [#17 Who sells, makes and services Gravipack products is not explained, and partner listings are partly outside the brand's control](#17-who-sells-makes-and-services-gravipack-products-is-not-explained-and-partner-listings-are-partly-outside-the-brands-control)
- **How we'll know the fix failed:** This fix has failed if, after 90 days, any of the following is true:
- The Decathlon brand page is still below 4.0/5 with fewer than 25 ratings.
- Negative reviews on Gravipack's own Decathlon offers still have no reply.
- No new reviews have appeared under current model names (Hiking 30 L, Sherpa 45 L, Business Talk V4).
- **Leading indicator to monitor:** Track monthly:
- the number of new reviews under current model names, on gravipack.com and on marketplaces;
- the reply rate and median reply time on reviews where Gravipack is the seller;
- the Decathlon brand-page average and rating count (baseline: 3.88/5 from 16).
- **To verify on-site:** Check the following:
- Whether WooCommerce product reviews are enabled and limited to verified owners, and how many reviews each product has.
- Whether AggregateRating is built only from those on-page reviews (Rich Results Test).
- What the /gravipackers/ page contains.
- In the Decathlon seller back-office, which options exist for replying to reviews on Gravipack's own offers.

### 39. A reseller's Gravipack brand page and Decathlon lead several generic 'anti mal de dos' results

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | likely | E-commerce & Marketplaces |

**Issue.** **Ergo-Corner (extended mode).** The specialist reseller Ergo-Corner has a Gravipack brand page, ergo-corner.com/55-gravipack. In the extended-mode results we sampled (US-located, non-Google index), it ranks at or above gravipack.com for several generic 'anti mal de dos' queries:
- #1 for 'sac à dos ergonomique mal de dos', 'meilleur sac à dos anti mal de dos', 'sac à dos porte-outils anti mal de dos' and 'sac à dos tactique anti mal de dos';
- #2 for 'sac à dos anti mal de dos';
- #3 for 'sac à dos randonnée anti mal de dos' and #4 for 'sac à dos exosquelette'.
In total it appears in 7 of the 12 extended result sets, 6 of them 'mal de dos' queries. Ergo-Corner's editorial page /content/13-le-sac-a-dos-gravipack and a blog post also rank. For 'meilleur sac à dos anti mal de dos', Ergo-Corner holds #1 and #2 and the gravipack.com home page is #5.

**gravipack.com is still present** in the same sets: #4-#6 for 'sac à dos anti mal de dos', #2 for 'sac à dos ergonomique mal de dos', and #2 for the tactical query with the Austerlitz.

**Decathlon (standard mode).** decathlon.fr/vc/gravipack was:
- listed first for 'sac à dos anti mal de dos';
- also present for 'meilleur sac à dos pour le mal de dos' and 'sac à dos collège léger dos mal aux épaules ado';
- #1 even for a competitor-brand query ('Bodypack sac à dos ergonomique anti mal de dos marque').
In extended mode, Decathlon is absent for 'sac à dos anti mal de dos'. Its Hiking 33 listing does appear for 'sac à dos exosquelette'.

**These pages sell Gravipack products.** The clicks still go to Gravipack products, and an AI answer that cites them still names Gravipack. We did not measure whether AI assistants cite these pages rather than gravipack.com; that is an inference. The real cost is control of facts, price and margin.

**Their facts diverge from the official ones:**
- Decathlon titles say 'Allège la charge de 92%'.
- Ergo-Corner's Sherpa kaki page states a 1-year warranty (10 years elsewhere) and sells exoskeleton sizes M/L/XL/XXL.
- The Decathlon Sherpa 45 promotion (149.90 € instead of 249 €, 18/06-30/08/2026) has ended and is not a current price.

**Evidence.** <https://www.ergo-corner.com/55-gravipack> · <https://www.ergo-corner.com/content/13-le-sac-a-dos-gravipack> · <https://www.ergo-corner.com/gravipack/676-sherpa-45l-kaki-avec-exosquelette-gravipack-.html> · <https://www.decathlon.fr/vc/gravipack> · <https://www.decathlon.fr/browse/b/gravipack/_/N-19o8oxe> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/>

**Why it matters.** Resellers that rank for the category are useful distribution. But their pages become the version of Gravipack that shoppers and AI answer engines read first. If their claims, specs, warranty or prices differ from the official ones, those differences get repeated. The official pages also lose the chance to show the evidence and the fitting service that justify the price.

**Effect on SEO.** Aligned reseller content turns these slots into consistent support for the brand's facts, which helps entity consistency in AI answers. Where a reseller links to the official evidence and fitting pages, it also sends referral traffic and link signals to gravipack.com. It does not directly move gravipack.com rankings; that comes from the category-hub work.

**How to fix.**

1. **Treat Ergo-Corner and the Decathlon brand page as partners.** Send them the brand content kit: the master product sheet (measured specs, one warranty term), approved claim wording that matches the evidence page, current model names and images.
2. **Ask Ergo-Corner for links.** Ask for links from /55-gravipack and /content/13 to the official evidence page and to the fitting guide (/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/), e.g. « Voir l'étude et les mesures sur le site officiel Gravipack ». Specialist resellers usually accept this. Decathlon marketplace pages generally do not allow outbound links, so on vc/gravipack only align the text.
3. **Correct the Ergo-Corner Sherpa kaki page:** replace the 1-year warranty with the official term, and fix any old prices or model names.
4. **Remove or substantiate 'Allège la charge de 92%' in Decathlon titles.** Change Gravipack's own listings now, and Kid'abord's listings through the licence. The wording itself is owned by the health-claims finding.
5. **Keep the richest content on gravipack.com.** Do not give resellers the gravipack.com product copy. Give them a shorter, different description. Keep the measured spec table, the fitting by height and weight, videos, evidence and FAQ on gravipack.com.
6. **Strengthen gravipack.com's own pages where Ergo-Corner leads:** the existing 'tous les sacs' category for 'sac à dos anti mal de dos', and the outillage and tactique categories. This is covered by the cannibalisation and category findings.
7. **Measure branded share separately.** For the 12 head queries, track 'Gravipack-branded share' (official plus reseller URLs) separately from 'official share'. Each quarter, ask ChatGPT, Perplexity and Google AI Mode « meilleur sac à dos anti mal de dos ». Note which URLs they cite and whether the facts they quote match the master sheet.

- **First principle:** A reseller page that sells the brand's product is distribution, not competition. The only real loss is when it states different facts, and fixing those facts at the source costs less than trying to outrank a partner.
- **Do first:** [#21 Model names, capacities, weights and warranty terms conflict across channels, and some specs are publicly disputed](#21-model-names-capacities-weights-and-warranty-terms-conflict-across-channels-and-some-specs-are-publicly-disputed), `study-evidence-page`
- **How we'll know the fix failed:** This fix has failed if, after one quarter, any of the following is true:
- Ergo-Corner and Decathlon pages still show the 1-year warranty, '92%' or legacy specs.
- The quarterly AI-answer check still quotes facts that contradict the master sheet.
- GA4 still shows zero referral sessions from ergo-corner.com to gravipack.com after the links are added.
- **Leading indicator to monitor:** Track:
- the number of reseller pages aligned with the content kit (target: Ergo-Corner /55, /content/13 and the Sherpa pages within 60 days);
- GA4 referral sessions from ergo-corner.com;
- in the quarterly AI-answer check, the share of cited URLs that state the official specs.
- **To verify on-site:** Check the following:
- In GSC, check whether gravipack.com gets impressions for 'sac à dos anti mal de dos', 'meilleur sac à dos anti mal de dos', 'sac à dos porte-outils anti mal de dos' and 'sac à dos tactique anti mal de dos', and at what position.
- In GA4, check referral traffic from ergo-corner.com and decathlon.fr.

### 43. No 'Où acheter' page lists authorised sellers, and some channels (Amazon.fr, Cdiscount, ManoMano, pharmacies) were not found

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🔵 **Low** | **3** | Low | likely | E-commerce & Marketplaces |

**Issue.** **No page on gravipack.com says where else the bags can be bought.**
- A site-restricted search for revendeurs, points de vente, magasins partenaires and distributeurs returned only the CGV, the legal notice, /nos-clients/, /devis-gravipack/ and a post titled 'Gravipack bientôt en magasin : l'innovation en apesanteur prend son envol', which names no store.
- On the open web, 'où acheter Gravipack magasin revendeur point de vente' returned only randonner-leger.org posts from 2021: 'sur le site Decathlon mais pas en magasin', 'Vendu et expédié par GRAVIPACK', 'juste market place'.
- A Paris showroom appears only as a promise on KissKissBankBank.

**Channels actually found, all online:**
- Decathlon.fr marketplace, with two sellers: Gravipack's own account and the licensee Kid'abord;
- Nature & Découvertes (Kid'abord);
- Au Vieux Campeur (Feather, Hiking 33, Sherpa 45, Business Talk);
- Fnac (brand page; most models out of stock);
- Kiabi marketplace (Feather, Feather Plus, Sherpa 45 kaki, Pearl);
- Ergo-Corner (about 10 current models);
- Équilibre France Ergonomie (Hiking 33, Business Talk, City);
- Bureau Vallée (Pearl, 'retrait 2h en magasin');
- ProSportEquip (Hiking 33);
- an Oslo rental on location.planete-rando.fr.
No physical stockist with confirmed in-store stock was found.

**Channels not found.** These are absences in a small number of searches, not proof:
- Amazon.fr: 2 searches. The only hit is a customer review on a Kipling bag saying 'je vais passer à la marque GRAVIPACK…'.
- Cdiscount: 1 search. Its /r-gravipack.html internal search page shows look-alikes such as a Pacsafe 'Gravity Gray' bag.
- Rakuten, ManoMano and eBay.fr: 1 search each.
- Pharmacy, orthopaedic or osteopath channels: 1 search.

**Evidence.** <https://gravipack.com/gravipack-bientot-en-magasin-linnovation-en-apesanteur-prend-son-envol/> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626059> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626080> · <https://www.kisskissbankbank.com/en/projects/gravipack/tabs/faqs> · <https://www.decathlon.fr/vc/gravipack> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-pour-ordinateur-tout-terrain-et-urbain-business-talk/_/R-p-641ecc4b-c138-4681-a51f-6130c39aa4db> · <https://www.natureetdecouvertes.com/v/sac-a-dos-gravipack> · <https://www.fnac.com/Gravipack/m568883/w-4> · <https://www.kiabi.com/sac-a-dos-gravipack-sherpa-45-kaki-kaki_P1443012C1443014> · <https://www.ergo-corner.com/55-gravipack> · <https://equilibre-france-ergonomie.fr/produits/sac-a-dos-city-gravipack/> · <https://www.bureau-vallee.fr/gravipack-sac-a-dos-pearl-29-litres-gris-405222788.html> · *(+2 more in findings/)*

**Why it matters.** For a bag sold on fit and comfort, many buyers want to know where they can see or try it, or they prefer a retailer they already trust. When the brand does not answer, a five-year-old forum thread does. A list of authorised sellers also helps buyers avoid look-alikes, and it tells them who handles after-sales on each channel.

**Effect on SEO.** The effect is small, and demand is probably small, hence Low. An 'Où acheter' page can:
- rank for 'où acheter gravipack', 'gravipack magasin' and 'gravipack decathlon';
- give resellers an official page to link to;
- give AI assistants a source to cite for 'where to buy'.
It will not create in-store listings: Google's local inventory features need each retailer's own Merchant Center feed. A 'store locator' in the local-SEO sense is for a business's own locations; this is a stockist list.

**How to fix.**

1. **Create /ou-acheter-gravipack/** as a WordPress page in plain, crawlable HTML (no JS-only map). Title: « Où acheter Gravipack ? Boutique officielle et revendeurs agréés ». Sections:
   - « Boutique officielle » – gravipack.com, with what only it offers: réglage personnalisé de l'exosquelette selon votre taille et votre poids, garantie, SAV direct.
   - « En ligne » – Decathlon.fr (vendu par Gravipack ou par Kid'abord, licencié Gravipack), Nature & Découvertes (Kid'abord), Fnac, Kiabi. Each entry links to the Gravipack page on that site.
   - « Spécialistes » – Au Vieux Campeur, Ergo-Corner, Équilibre France Ergonomie.
   - « Retrait en magasin » – Bureau Vallée (Pearl, click & collect). List only stock points the retailer has confirmed.
   - An after-sales line: « Pour un achat chez un revendeur, le SAV est assuré par ce revendeur ; en cas de difficulté, contactez-nous. »
   - « Mis à jour le [date] ».
2. **List only confirmed, authorised partners.** If it is true, add « Gravipack n'est pas vendu sur Amazon.fr ni sur Cdiscount : méfiez-vous des imitations. »
3. **Do not add LocalBusiness or Store schema for third-party shops.** Google supports that markup only for the business the page is about. A BreadcrumbList is enough.
4. **Link to the page** from the footer, the FAQ (« Où acheter un Gravipack ? Peut-on l'essayer en magasin ? ») and the contact page. Update or unpublish the 'bientôt en magasin' post, adding a dated note that points to the new page.
5. **Ask the listed resellers** to link to the page or to the official model pages (see the link-reclamation finding).
6. **Do not position the bags in pharmacies or orthopaedic shops** until the medical-device status and the health claims are clarified (see the health-claims finding).
7. **Treat channel expansion as a business decision**, not an SEO defect. Consider Amazon.fr only after product data and pricing are aligned. Brand Registry would also protect the trademark against look-alikes.

- **First principle:** A buyer who searches 'où acheter' wants a list from the brand. If the brand does not publish one, whoever answered the question last becomes the answer; here, that is a 2021 forum thread.
- **Do first:** [#17 Who sells, makes and services Gravipack products is not explained, and partner listings are partly outside the brand's control](#17-who-sells-makes-and-services-gravipack-products-is-not-explained-and-partner-listings-are-partly-outside-the-brands-control)
- **How we'll know the fix failed:** This fix has failed if, three months after publication, any of the following is true:
- GSC shows no impressions for the page on queries like 'où acheter gravipack', 'gravipack magasin' or 'gravipack decathlon'.
- The 2021 randonner-leger thread still ranks above it in a manual google.fr check.
- Customer service still gets 'where can I buy or try it' questions at the same rate.
- **Leading indicator to monitor:** Track:
- GSC impressions and clicks for /ou-acheter-gravipack/;
- the number of resellers linking to it;
- outbound clicks from the page to partners (GA4 event).
- **To verify on-site:** Check the following:
- Search the site and the XML sitemap for any existing revendeurs or points-de-vente page or footer link.
- Check the current content of the 'Gravipack bientôt en magasin' post.
- Confirm with each partner which models they stock now, and whether any physical store holds stock.

## Local SEO

**Score:** **35/100** *(partial)* — Likely GBP and PagesJaunes/Mappy citations still show the old Vincennes "Maroquinerie" listing while the legal seat moved to Paris 2e; no store locator (gbp-local-citations, where-to-buy-channels).

**What works:**
- An aggregator reports ~4.7/5 from ~998 Google reviews for Gravipack Vincennes (to be confirmed in GBP)

### 24. The likely Google Business Profile and local citations still show the old Vincennes address, while the registered seat is now in Paris

| Severity | Impact (1-10) | Effort | Confidence | Pillar |
|---|---|---|---|---|
| 🟡 **Medium** | **4** | Medium | likely | Local SEO |

**Issue.** Gravipack's local listings still show an address the company has left. The listing that probably matters most, a Google Business Profile carrying about 1,000 reviews, has not been found or audited.

**1. The registered seat has moved.** Registry data (annuaire-entreprises, societe.com, verif.com) put EXOSQUELETTE LIGHT SAS at 10 rue de la Paix, 75002 Paris since 19/05/2026 (siège SIRET 840 543 383 00045). This company (SIREN 840 543 383, previously named GRAVIBAG and then GRAVIPACK SAS) owns the Gravipack brand. The previous seat, from the end of 2022, was 46 rue de la Bienfaisance, 94300 Vincennes. We could not verify whether the Paris address is a domiciliation (an address with no customer reception).

**2. Directory citations still point to Vincennes, under the wrong category.**
- PagesJaunes pros/60790927: 'Gravipack à Vincennes – Maroquinerie', 0 reviews; the page was about 670 days old when sampled.
- PagesJaunes pros/62263007: a second ID surfaced in a registry-filtered search. It is probably a duplicate listing.
- Mappy POI 605d2e7de32c7c1ed765382d: 'Gravipack – Maroquinerie, 46 r Bienfaisance, 94300 Vincennes'.
- 'Maroquinerie' (leather goods) is the wrong category for a maker of exoskeleton backpacks.
- Other surfaces still showed Vincennes in the search results we sampled: rubypayeur ('Société EXOSQUELETTE LIGHT à VINCENNES'), the motherbase.ai startup profile and the LinkedIn company page. The site's own contact pages, /contacts/ and /contact-gravipack/, showed 46 rue de la Bienfaisance in phase-1 search snippets (verify on-site). The mentions légales and CGV name EXOSQUELETTE LIGHT, Paris. The contact page gives a mobile number and contact@gravipack.com. Two contact URLs therefore carry the NAP.

**3. A Google Business Profile very probably exists, but we did not find it.** Two searches ('Gravipack Vincennes adresse téléphone' and 'Gravipack Vincennes avis Google My Business 998 avis') returned no Google Maps URL, and the search tool cannot see Maps or knowledge panels. Four other signals point to a profile:
- An aggregator page (groupe-ranque.fr/gravipack/, titled 'Gravipack – Vincennes – Sécurité et Stockage Blindé') reports '4.7/5 pour 998 avis sur Google My Business'.
- A third-party blog (compostelle-autrement.com) reports '4,8/5 sur Google avec déjà plus de 900 avis'.
- gravipack.com product pages show a '4,7' Google rating with 'plus de 1121 avis' (Hiking) and 'plus de 1126 avis' (Kingston), and the 'Avis Google des clients Gravipack' page shows 'plus de 1175 avis'.
- The sequence 900+ → 998 → 1,121–1,175 fits a live profile that is still gaining reviews.

The corroboration is weak. Phase 1 treated the aggregator as a homonym because of its odd category title, and the blog may simply repeat the brand's own figures. The earlier statement 'no GBP signal surfaced' is therefore corrected to: a GBP likely exists, unverified, and most likely still shows Vincennes.

**4. The risk.** A Google Business Profile is only eligible if staff meet customers in person at the address during stated hours, or if the business serves customers at their own locations (a service-area business). Online-only businesses, virtual offices and mail-drop addresses are not eligible. The evidence describes an online-first seller:
- Sales go through gravipack.com and marketplaces. On the marketplaces, Kid'abord, a separate company, acts as licensee and marketplace seller.
- Returns go to a logistics warehouse in Colmar.
- We found no showroom, and a 2020 forum post says the bags were sold only through the website.

Changing the profile's address to the Paris seat normally triggers re-verification. If the Paris address is a domiciliation, or no staffed premises exist, the profile could be suspended. Suspension would remove about 1,000+ Google reviews from Maps and the brand's knowledge panel. It would also leave the '4,7 Google' figure, the main trust figure the site displays, with no public source. Leaving the profile untouched is not safe either: it keeps sending people to an address Gravipack may no longer use.

**Evidence.** <https://www.pagesjaunes.fr/pros/60790927> · <https://www.pagesjaunes.fr/pros/62263007> · <https://fr.mappy.com/poi/605d2e7de32c7c1ed765382d> · <https://groupe-ranque.fr/gravipack/> · <https://www.compostelle-autrement.com/post/gravipack-le-sac-a-dos-en-apesanteur> · <https://annuaire-entreprises.data.gouv.fr/entreprise/exosquelette-light-840543383> · <https://www.societe.com/societe/exosquelette-light-840543383.html> · <https://gravipack.com/contacts/> · <https://www.gravipack.com/contact-gravipack/> · <https://gravipack.com/mentions-legales/> · <https://gravipack.com/conditions-generales-de-vente/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · *(+2 more in findings/)*

**Why it matters.** Gravipack sells mainly online, so ranking in the local pack is worth little. A probable Google Business Profile with about 1,000 reviews is a different matter. It is the source of the '4,7 Google / plus de 1 100 avis' figure shown on product pages, and those reviews appear in Maps and in the brand knowledge panel. As it probably stands (old Vincennes address, an online-only business behind it), the profile is exposed to a policy suspension. The address change will force re-verification, which makes that more likely. Losing the profile would erase the brand's largest review base, which cannot be rebuilt quickly. Separately, out-of-date NAP on PagesJaunes, Mappy, Bing and LinkedIn contradicts the registry. That weakens the entity data search engines and AI assistants use to describe the company. Bing Places data, for example, feeds Bing Maps, Copilot and ChatGPT search. The wrong 'Maroquinerie' category also mislabels the business.

**Effect on SEO.** There are three mechanisms.
- **Entity reconciliation.** Google, Bing and AI answer engines cross-check name, address and phone across the registry, the site and directories. Conflicting Vincennes and Paris data lowers confidence in knowledge-panel and AI-answer facts and can surface a wrong address.
- **GBP trust surface.** A verified, eligible profile keeps the review count and rating visible on Maps and in brand searches, which supports CTR and conversion. A suspended profile drops out of Maps and the knowledge panel, and its reviews disappear from public view.
- **Category relevance.** 'Maroquinerie' puts the business in the wrong local and directory classification.

On the website, aligned NAP (contact page, mentions légales, Organization JSON-LD) supports entity consistency. GBP reviews must never be marked up as Product aggregateRating.

**How to fix.**

**Phase A: locate and secure the GBP (week 1, before any other change).**
1. Find the profile. In Google Maps, logged out and from France, search 'Gravipack', 'Gravipack Vincennes' and 'Gravipack Paris'. A faster route is the WordPress plugin that renders the '4,7 Google' widget (for example Trustindex, Widgets for Google Reviews, Elfsight or a custom block): its settings hold the Place ID, which starts with `ChIJ`. You can also view the source of a product page and search for `ChIJ` or `place_id`. Then open `https://www.google.com/maps/place/?q=place_id:ChIJ…`.
2. Check who owns it. Sign in to business.google.com with every account that might hold it: contact@, the President's account, and any former agency or freelancer. If nobody does, use « Vous êtes propriétaire de cet établissement ? » and request access. If the current owner does not respond, Google usually offers to let you verify after about a week. Make a company-controlled Google account the primary owner, not a personal or agency account.
3. Record a baseline before editing anything: Place ID, CID, name, primary and secondary categories, address, phone, website URL, rating and exact review count, plus screenshots. Archive the reviews through the Business Profile API reviews endpoint or a review-monitoring tool.

**Phase B: decide eligibility. This decision drives every later step.**
4. Pick one model and document it in the entity master fact sheet.
   - **(a) Staffed location.** A real place (atelier, showroom or click-and-collect point) with signage, where staff meet customers during posted hours. This can be Vincennes if it is still in use, or a Paris showroom. Keep the address visible and set opening hours.
   - **(b) Service-area business.** Use this only if staff genuinely travel to customers, for example on-site fittings and demonstrations for employers and CSE days, or B2B deployments of the kind done with RATP. Hide the address (Infos → Adresse → supprimer l'adresse) and add service areas (Paris, Hauts-de-Seine, Val-de-Marne…; maximum 20).
   - **(c) Neither.** The business is online-only and not eligible. Do **not** move the profile to 10 rue de la Paix if that address is a domiciliation or virtual office; that is the most likely route to suspension. Leave the profile as it is, accept the risk knowingly, and stop relying on it as the site's main trust figure. Build Trustpilot, marketplace and on-site product reviews instead (see the review findings).
5. Never create a new profile for the Paris seat. A new profile starts at 0 reviews and creates a duplicate. Edit the address on the existing profile so the reviews move with it. Prepare for re-verification first (usually a video showing signage, premises, stock or tools, and a business document such as the Kbis), and align the website (Phase E) at the same time, because Google compares the two.

**Phase C: update the profile.**
6. Set the fields:
   - **Name:** exactly `Gravipack`. Do not add keywords such as 'sac à dos anti mal de dos'; keyword-stuffed names are a common cause of suspension.
   - **Primary category:** replace 'Maroquinerie' with the closest option in the picker for what actually happens at the location. That is a bag/luggage store or sporting-goods store category for a showroom, or a manufacturer category for an atelier.
   - **Website:** the canonical host's homepage, with `?utm_source=google&utm_medium=organic&utm_campaign=gbp`.
   - **Phone:** the same company number shown on the site and PagesJaunes.
   - **Description:** at most 750 characters, with no health claims or unverifiable claims. For example: « Gravipack conçoit et vend des sacs à dos équipés d'un exosquelette qui reporte une partie de la charge des épaules vers les hanches : modèles randonnée, urbains, ordinateur et scolaires. [Showroom : essayez les sacs sur place et retirez vos commandes passées sur gravipack.com.] Service client : contact@gravipack.com. Gravipack® est une marque d'EXOSQUELETTE LIGHT SAS. »
7. Reply to recent reviews, starting with the negative ones. After the edit, check the profile weekly for « modification en attente » or a suspension notice. If it is suspended, fix the eligibility problem first, then appeal with evidence (Kbis, lease, photos of the signage).

**Phase D: clean up citations (identical NAP, character for character).**
8. Write one NAP reference line: `Gravipack (EXOSQUELETTE LIGHT SAS) – [adresse publique retenue ou « vente en ligne, pas d'accueil du public »] – [téléphone] – contact@gravipack.com – https://[hôte canonique]/`.
9. PagesJaunes:
   - Claim pros/60790927 through the free PagesJaunes pro space (« Vous êtes ce professionnel ? »).
   - Update the address, website and description, and replace the 'Maroquinerie' activity with suitable rubriques (for example articles de sport, sacs/bagages).
   - Open pros/62263007. If it is the same business, ask PagesJaunes customer service to merge or delete it as a « fiche en doublon ».
   - If there are no public premises, ask PagesJaunes to remove the street address or close the listing rather than keep showing Vincennes.
10. Mappy: re-check POI 605d2e7de32c7c1ed765382d about 6 weeks after the PagesJaunes change. If it still shows the old data, submit a correction through the POI's report/modify link.
11. Bing Places: claim the listing and import it from Google Business Profile so Bing, Copilot and ChatGPT search get the same data. Apple Business Connect: claim a place card only under model (a) or (b).
12. Ask motherbase.ai to update its profile and update the LinkedIn company HQ. Registry mirrors (societe.com, pappers, rubypayeur) refresh from the RNE on their own; just re-check them in 1–2 months.

**Phase E: align the WordPress/WooCommerce site.**
13. Keep a single contact page and 301 the other one, either with the Redirection plugin or in .htaccess: `Redirect 301 /contacts/ https://[hôte canonique]/contact-gravipack/`. On the contact page, give the same NAP as the GBP and PagesJaunes. Under model (a), add the address, opening hours and a lazy-loaded map. Under model (c), say so plainly, for example: « Gravipack est une marque d'EXOSQUELETTE LIGHT SAS – siège social : 10 rue de la Paix, 75002 Paris (adresse administrative, pas d'accueil du public). Service client : contact@gravipack.com, du lundi au vendredi. Retours : voir notre page Retours. »
14. Update the remaining on-site copies of the address:
   - WooCommerce → Réglages → Général → Adresse de la boutique (used in emails and the tax base).
   - The shop address in any invoice plugin.
   - The footer widget, mentions légales and CGV.
15. Schema: keep one site-wide Organization node, merged with the node from the entity finding. With Rank Math, use the Local SEO module (Titres & méta → Local SEO). With Yoast, set Site representation, and add the address with Yoast Local SEO or the `wpseo_schema_organization` filter. The node should carry the seat address and, once known, the Maps CID in sameAs:
```json
{"@context":"https://schema.org","@type":"Organization","@id":"https://[hôte canonique]/#organization","name":"Gravipack","legalName":"EXOSQUELETTE LIGHT","url":"https://[hôte canonique]/","address":{"@type":"PostalAddress","streetAddress":"10 rue de la Paix","postalCode":"75002","addressLocality":"Paris","addressCountry":"FR"},"contactPoint":{"@type":"ContactPoint","contactType":"customer service","email":"contact@gravipack.com","telephone":"+33-[numéro]","areaServed":"FR","availableLanguage":"fr"},"sameAs":["https://maps.google.com/?cid=[CID]","https://www.pagesjaunes.fr/pros/60790927"]}
```
Under model (a) only, add a `Store` node on the showroom page. Give it `parentOrganization` {"@id":"https://[hôte canonique]/#organization"}, the showroom's own address, `openingHoursSpecification` and `hasMap`. Never output the GBP rating as Product `aggregateRating`.

If Phase A shows that no GBP exists, downgrade this finding to Low. In that case do Phases D and E only, and do not create a profile unless model (a) or (b) is genuinely true.

- **First principle:** Search engines and AI assistants recognise a business by checking that its name, address and phone match across the official registry, the website and listings. A listing whose address matches no official record is both a trust conflict and a policy liability. Here the listing at risk, a Google Business Profile with about 1,000 reviews, is also the hardest asset to rebuild, so it has to be located, protected and made eligible before any address is changed.
- **Do first:** `entity-identity-alignment`
- **How we'll know the fix failed:** The premise is falsified if Phase A finds no Gravipack Google Business Profile in Maps, in any company Google account or in the review widget's settings. In that case the 'roughly 1,000 reviews at risk' argument does not hold: downgrade to Low, and treat the site's '4,7 Google / 1 1xx avis' claims as a separate, more urgent substantiation problem. The fix has failed if any of these is true within 8 weeks of the edits: Maps still shows Vincennes or 'Maroquinerie' for Gravipack; the profile shows suspended/disabled or disappears; its review count falls well below the Phase A baseline; or PagesJaunes still shows two listings or the Vincennes address.
- **Leading indicator to monitor:** Watch these after the edit:
- GBP status (verified; address or service area as decided) and review count against the Phase A baseline: weekly for 8 weeks, then monthly. Third-party figures put it at 998; the site claims 1,121–1,175.
- GBP Performance website clicks, and GA4 sessions with utm_campaign=gbp.
- The share of citations showing the current NAP across GBP, PagesJaunes, Mappy, Bing Places, Apple, LinkedIn and motherbase.ai (target 100%, with a single PagesJaunes listing).
- Whether the brand knowledge panel shows the correct address.
- **To verify on-site:** 1. In Google Maps, logged out from France, search 'Gravipack', 'Gravipack Vincennes' and 'Gravipack Paris'. Record the Place ID/CID, address, category, rating, review count and whether the « Vous êtes propriétaire… » link appears (it appears only when the profile is unclaimed).
2. In WP admin, open the Google-reviews widget plugin, or search a product page's source for 'ChIJ' or 'place_id', to get the Place ID behind the '4,7' figure.
3. In business.google.com, under every company account, check who owns the profile, its verification state and any suspension notice.
4. Confirm whether 10 rue de la Paix is a domiciliation, and whether 46 rue de la Bienfaisance (Vincennes) still has staff or receives customers. Check whether any staffed showroom or click-and-collect point exists.
5. Check the address and phone shown on /contacts/, /contact-gravipack/, the footer, the mentions légales, the CGV and WooCommerce → Réglages → Général, and the HTTP status of both contact URLs.
6. Open PagesJaunes pros/62263007 to confirm whether it duplicates pros/60790927.
7. Run the Rich Results Test or Schema Markup Validator on the homepage and contact page to read the current Organization/LocalBusiness address and check for any aggregateRating built from Google reviews.

## Methodology & evidence

- **Phase 1** — 6 claude-seo specialist auditors (indexation/domains, keywords/SERP/SXO/cluster, backlinks/PR, E-E-A-T/YMYL, GEO/AI visibility, e-commerce/local/competitors), each followed by an adversarial verifier, a completeness critic and gap-fillers.
- **Phase 2** — 4 budget-capped gap researchers (legal entity & claims via public registries, brand SERP/reputation/social, marketplaces/competitors/price parity, freshness/B2B/local) + 4 adversarial verifiers that re-ran searches.
- **Consolidation** — 142 raw findings clustered and merged, phase-2 evidence superseding phase-1, verifier corrections applied, each merged batch QA-reviewed against source records.
- **Limits** — No crawl of the site (network policy). WebSearch is a US-located index (not Google.fr); titles are *as shown in search results* and may be rewritten by the engine. No paid data (Ahrefs/Moz/DataForSEO/GSC/GA4/CrUX), so backlinks are discovered mentions, not a measured link graph, and search volumes are not quantified.
- Raw specialist outputs, data tables, search logs and content briefs: [`findings/`](findings/) and [`appendix/`](appendix/).
