# Phase 1 — ecommerce-local-competitors

Searches run: 0

## Evidence base

EVIDENCE LIMITATION, PLEASE READ FIRST. This sub-agent ran 0 searches. It sent 6 WebSearch queries in parallel ('gravipack amazon.fr sac à dos', 'gravipack decathlon marketplace sherpa 45', 'gravipack cdiscount OR fnac OR rakuten OR manomano', 'gravipack avis', 'gravipack prix sac exosquelette', 'gravipack trustpilot'). The tool refused all of them: 'this turn's web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)'. The network policy blocks gravipack.fr and gravipack.com, and no earlier search output was saved in the project directory. In line with the tool's instruction and claude-seo's rule 'URL unreachable → report clearly, do not guess site content', I did NOT work around this with curl, proxies, caches or archives. So:
(1) Every finding below rests ONLY on the 'already known' facts the orchestrator relayed from its own earlier searches. These are 7 SERP titles (titles as shown in search results; Google may rewrite them), URL patterns on gravipack.com / www.gravipack.com, the empty result for site:gravipack.fr, and a list of third-party domains (Decathlon brand page, Trustpilot ES, outzer.fr, randonner-leger.org, challenge.ma, journaldugeek.com, neozone.org, lespepitestech.com, KissKissBankBank, motherbase.ai). This sub-agent has not re-verified any of it. The evidence URLs are reproduced exactly as relayed; some are domain-only because the full URL was not relayed.
(2) I could NOT measure marketplace coverage (Amazon, Cdiscount, Fnac, ManoMano, Rakuten, Alltricks, pharmacies), prices per channel, review counts, competitor SERP ownership, NAP or directory listings, or GBP existence. These are all in open_questions_need_site_access and in a ready-to-run query backlog table.
(3) Confidence is therefore 'likely' at best and 'needs-on-site-check' for most items. Category scores are null wherever the evidence does not support a number. The only score given is for SERP-visible product titles, where the title strings themselves are the evidence.
To finish this dimension, send a follow-up message after this reply (a new turn gets a fresh search budget) or raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.

## claude-seo commands applied

- /seo ecommerce: I applied the Product Page checklist (title tag and meta part only) and the Gap Types logic to the 7 SERP titles relayed in the brief. I could not run the Shopping or Amazon (DataForSEO Merchant) steps because there are no credentials and no searches were left.
- /seo ecommerce schema: I used it to write the recommended Product and ProductGroup JSON-LD. I could not check the live schema because the site is blocked.
- /seo local: I applied business-type detection (e-commerce / online-only, so not brick-and-mortar or SAB), the GBP eligibility logic and the NAP checklist. I could not run the NAP comparison because no directory evidence could be gathered.
- /seo maps nap (Tier 0): I applied the workflow logic only. The Google, Bing, Apple and OSM lookups did not run (no searches, site and network blocked).
- /seo competitor-pages: I applied the page types (vs, alternatives, roundup, comparison table), the title formulas, the fairness rules and the schema advice to plan the recommendations. I could not collect competitor SERP data.
- claude-seo priority definitions (Critical / High / Medium / Low) and the quality-gates title rules (30–60 chars, keyword first, brand last, unique per page)

## What works

- The product has a clear, defensible differentiator: a patented 'exosquelette' with carbon inserts in the shoulder straps. Generic outdoor brands cannot easily claim this entity and keyword angle, which is good for brand and entity SEO and for AI-answer citability once substantiated (relayed evidence).
- The brand has earned media and directory mentions (journaldugeek.com, neozone.org, challenge.ma, lespepitestech.com, KissKissBankBank). This gives a starting base of brand mentions and potential links that AI systems use as entity signals (relayed evidence, link status not verified).
- There is a presence on a high-authority marketplace (Decathlon marketplace brand page for Sherpa 45, Hiking 33 and Feather). It extends reach to Decathlon's audience and builds brand legitimacy (relayed, seller and prices not verified).
- Product titles as shown in SERPs include use-case modifiers that match real query language (randonnée, montagne, léger, business, ergonomique), so the pages are topically relevant for long-tail queries (relayed SERP titles).
- The store uses a standard WooCommerce structure (/boutique-gravipack/, /produit/<slug>/). This is crawlable and supports the usual SEO and schema plugins, so the fixes below are low-effort to implement (relayed URL patterns).
- The range covers several segments (hiking, urban/business, school), which allows a clean hub-and-spoke category architecture without new products (relayed).

## Specialist scores

| Category | Score | Rationale |
|---|---|---|
| Product titles & meta (SERP-visible) | 35 | Based on the 7 relayed SERP titles (as shown in search results): 6/7 are over 60 chars, 2/7 have no brand, 1/7 has no model name, the model name always sits in the truncated zone, the same head term repeats in every title, and spelling and casing are inconsistent. They are partly redeemed by relevant use-case modifiers (randonnée, montagne, business). Meta descriptions were not observed. Low confidence because Google may rewrite titles. |
| Product schema completeness | n/a | Requires the live site (JSON-LD inspection), which the network policy blocks. No evidence available. |
| Catalogue / variant architecture | n/a | Colour-per-URL is only suggested by two titles. URL count, variants, canonicals and categories need site access. |
| Marketplace presence & price consistency | n/a | Only the existence of a Decathlon brand page and one forum price (~€249) was relayed. Amazon, Cdiscount, Fnac and other marketplaces, sellers and per-model prices could not be searched (budget exhausted). |
| Reviews & reputation | n/a | Trustpilot existence and critical third-party reviews were relayed, but not star ratings, counts, recency or on-site reviews. A numeric score would be a guess. |
| Competitor / comparison content | n/a | No competitor SERP data could be gathered. The competitor set is still a hypothesis. |
| Local / entity (NAP, GBP, citations) | n/a | No directory or NAP evidence was gathered. GBP existence is unknown. Entity association (Kid'abord) is unverified. |
| B2B opportunity coverage | n/a | Whether B2B pages exist cannot be determined without site access or searches. The opportunity is real (army test, business models), but current coverage is unknown. |

## Raw findings (with verifier verdicts)

### Every product page targets the same head term ('anti mal de dos' + 'exosquelette'), so product pages compete with each other and the homepage

`ecom-title-cannibalisation` · On-Page SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** In the 7 titles relayed by the orchestrator (as shown in search results; Google may rewrite them), 7/7 contain 'mal de dos' and 6/7 contain 'exosquelette'. Examples: Home 'Gravipack : le sac révolutionnaire anti mal de dos exosquelette'; 'Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa'; 'Sac ergonomique de randonnée anti-mal de dos avec exosquelette' (Oslo); 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur'. The relayed URLs show no category page targeting 'sac à dos anti mal de dos'. The shop page slug is brand-only (/boutique-gravipack/). This sub-agent could not run its own searches (budget exhausted), so it could not check which URL Google actually ranks for the head term.

<https://gravipack.com/boutique-gravipack/> · <https://gravipack.com/> · <https://www.gravipack.com/>

**Why it matters.** When 7+ URLs on one site use near-identical primary keywords, Google has to choose one, and the choice often rotates between them. That splits internal links and click signals. It also leaves the high-volume, commercial head query ('sac à dos anti mal de dos', 'sac à dos ergonomique') without a dedicated, well-linked category page, which is the page type that usually ranks for that intent.

**SEO effect.** Rankings for the head term are diluted or unstable (several URLs swap position). CTR is lower because the ranking page may not match the query (e.g., a 60 L trekking bag shown for a commuter query). Category-level ranking potential is lost, and so are Shopping and organic product-grid units, which favour category and listing pages.

**How to fix.** 1) Build a keyword map (see data table 'Proposed keyword-to-URL map'). The homepage owns brand plus 'exosquelette'. A new category hub /sac-a-dos-anti-mal-de-dos/ owns the head term. Segment categories own 'sac de randonnée ergonomique', 'sac à dos ordinateur ergonomique' and 'cartable ergonomique'. 2) In WooCommerce, create these product categories (Produits > Catégories), give each 400+ words of unique intro text (claude-seo quality gate for category pages), and assign products. 3) Rewrite product titles so they lead with the model and capacity and drop the repeated head term, e.g. 'Sherpa 45 L – Sac de randonnée à exosquelette | Gravipack'. 4) Point internal links with the anchor 'sac à dos anti mal de dos' to the hub only. Product pages link up to their category with the segment anchor. 5) After 4–6 weeks, check Search Console > Performance > Pages for the head query to confirm only one URL gets impressions.

**Verifier notes.** Method: my WebSearch calls were refused because the 200-search turn budget was already used up. I re-checked against the WebSearch results recorded earlier in this run (scratchpad serp-notes.md, tables.md, inv.py: a 98-URL gravipack.com SERP inventory plus 16 presta.gravipack.com URLs). The search engine behind WebSearch is not Google.fr. The pattern holds at scale: 53/98 SERP titles contain 'anti mal de/au dos', 66/98 contain 'exosquelette', 28/39 product titles contain the head term and 37 slugs contain 'anti-mal-de-dos'. Two parts of the finding are wrong. (a) A category hub already exists: /categorie-produit/tous-les-sacs-a-dos-exosquelette/ (SERP title 'Achetez un sac à dos révolutionnaire avec exosquelette Gravipack'; page 2: 'Tous les sacs à dos anti-mal de dos exosquelette Gravipack') with 10 segment sub-categories. (b) 'Diluted/unstable rankings' is not shown. In extended-mode SERPs gravipack.com held 3 of about 9 results for 'sac à dos anti mal de dos' (Pearl product, homepage, Tokyo product), 3 for 'sac à dos ordinateur ergonomique anti mal de dos', and 5 for 'sac à dos porte-outils anti mal de dos'. Several URLs from one site in a SERP is extra visibility, not proof of cannibalisation. Rotation needs Search Console data. What is supported: the category hub is not the URL that ranks for the head term. Gravipack is absent for the broader 'sac à dos ergonomique' and 'cartable ergonomique'. In standard mode decathlon.fr/vc/gravipack ranked for the head term while gravipack.com did not. Downgraded to Medium (an optimisation opportunity under the claude-seo priority definitions).

### Product titles are too long, put the model name last, sometimes omit brand or model, and use inconsistent spelling

`ecom-product-title-format` · On-Page SEO · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** I measured the 7 relayed SERP titles (as shown in search results). Lengths are 63, 65, 85, 72, 62, 90 and 55 characters, so 6/7 exceed the claude-seo 60-character limit. The brand is missing in 2/7 ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa'; 'Sac ergonomique de randonnée anti-mal de dos avec exosquelette'). The Oslo 60+10L title (€289) has no model name at all. Where the model name appears, it starts at character 46–68, i.e. in the truncated zone. Spelling is inconsistent: 'anti mal de dos' vs 'anti-mal de dos', 'Gravipack' vs 'gravipack', 'ROME' in capitals. Google may have rewritten these titles, so the on-page <title> needs checking.

<https://gravipack.com/boutique-gravipack/> · <https://www.gravipack.com/>

**Why it matters.** seo-ecommerce checklist: the title should contain the primary product keyword and the brand, be under 60 characters, and follow '[Product Name] - [Key Feature] | [Brand]'. Buyers who have heard of a model (from Decathlon, press or crowdfunding) search for the model name ('gravipack sherpa 45'). If the model name is truncated or missing, the result cannot match that navigational intent.

**SEO effect.** Truncated titles lower CTR. Missing model names weaken rankings for model queries, which hands those clicks to marketplace listings (e.g., Decathlon 'Sherpa 45') and to third-party reviews. Google is also more likely to rewrite long titles, so you lose control of the SERP message.

**How to fix.** Use one template in Yoast or Rank Math (Produits > SEO title): '%%title%% – %%primary_category%% | Gravipack'. Rename the products so the product name is the model plus capacity. Examples (all ≤60 chars): 'Sherpa 45 L – Sac de randonnée à exosquelette | Gravipack'; 'Oslo 60+10 L – Sac de trekking ergonomique | Gravipack'; 'Hiking 33 L – Sac de randonnée léger | Gravipack'; 'Rome – Sac à dos ordinateur ergonomique | Gravipack'; 'Austerlitz – Sac à dos urbain léger | Gravipack'. Standardise on one spelling ('anti-mal de dos' with a hyphen, if used at all, and only on the category hub) and on 'Gravipack' casing. Meta description template: '[Modèle] [capacité] : exosquelette breveté en carbone qui reporte la charge vers le centre de gravité. À partir de [prix] €. [Livraison/retours selon vos conditions].' (≤155 chars). Keep H1 = product name (model + capacity).

**Verifier notes.** I re-measured the 7 relayed titles from the recorded inventory: 63, 65, 85, 72, 62, 90 and 55 characters, which matches the finding. Brand is missing from Sherpa bleu and Oslo, and the Oslo title has no model name (only the slug has 'oslo'). Correction: one of the 7 (the homepage) is not a product title. The site-wide evidence is stronger than the finding states. 76/98 titles exceed 60 characters (median 65). Several titles run to 182–204 characters because a site-wide suffix ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant' is appended (Compostelle 25/35/65 L, archives, posts). Google rewrites usually shorten titles, so this is almost certainly the template, not a rewrite. Exact duplicate titles appear on different URLs: G-Pack ×2, Light Promax 'Sac à dos outillage anti-douleur exosquelette Gravipack®' ×2, Cargo Max ×2, Sherpa Kaki ×3. Typos: 'Sac randonner léger' (Pearl), 'Sac a dos', 'assault'. Caveat: 60 characters is the claude-seo guideline. Google truncates by pixel width and does not enforce a length. The actual <title> still needs an on-site check.

### Colour variants appear to be separate product URLs with near-duplicate titles (e.g., Sherpa vs Sherpa Kaki, Hiking Gris)

`ecom-colour-variant-urls` · E-commerce · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** The relayed SERP titles include one Sherpa title without a colour ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa') and a separate 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur'. They also include 'Sac à dos exosquelette anti-mal de dos de montagne Hiking Gris Gravipack', with the colour in the title. Separate indexed titles that differ by colour suggest one /produit/ URL per colour. This needs confirming on the live site (blocked here), because the two Sherpa titles may also be different products.

<https://gravipack.com/boutique-gravipack/>

**Why it matters.** Colour-per-URL product pages usually share 90%+ of their description, specs and images. That creates near-duplicates that split reviews, links and ranking signals for the model query, and conflicts with the claude-seo product quality gate (≥80% unique content per product page).

**SEO effect.** Signals are split between colour URLs. Google may choose the 'wrong' colour as canonical. Review counts are fragmented, which weakens aggregateRating rich results. There is a crawl and index-bloat risk as the catalogue grows.

**How to fix.** Preferred: merge colours into one WooCommerce variable product per model (Produits > Type de produit: 'Produit variable', attribute 'Couleur'), then 301-redirect the old colour URLs to the parent model URL. Alternative, if colour URLs must stay for Shopping feeds: keep them, but add rel=canonical to the parent model URL, or mark them up as variants. Add Google-supported variant markup on the parent: {"@context":"https://schema.org","@type":"ProductGroup","name":"Gravipack Sherpa 45 L","productGroupID":"SHERPA45","variesBy":["https://schema.org/color"],"brand":{"@type":"Brand","name":"Gravipack"},"hasVariant":[{"@type":"Product","name":"Gravipack Sherpa 45 L Kaki","color":"Kaki","sku":"…","gtin13":"…","image":["…"],"offers":{"@type":"Offer","price":"…","priceCurrency":"EUR","availability":"https://schema.org/InStock"}}]}. Use the same productGroupID / item_group_id in the Merchant Center feed.

**Verifier notes.** The slugs in the recorded inventory prove one URL per colour: Sherpa bleu, Sherpa 45L orange and Sherpa kaki; Hiking 30L gris and Hiking terracotta; Oslo rouge; Pearl 29L gris. So the claim moves from 'needs-on-site-check' to 'likely'. How similar the page content is still needs an on-site check. A separate URL per variant is a pattern Google supports (the ProductGroup multi-page approach), so the colour split is not itself the defect. The worse problem, which this finding misses, is exact duplicates. A second product base path, /produit-gravipack/ (sac-a-dos-sherpa, sac-a-dos-sherpa-kaki, sac-a-dos-revolutionnaire, sac-a-dos-exosquelette-gravipack-pearl), repeats /produit/ pages: the Sherpa Kaki title appears on 3 URLs. Light Promax has 3 URLs, Cargo Max 2, Business Talk V4 25L 2 and G-Pack 2, and two slugs end in '-copie'. These duplicates could justify a separate High finding.

### Product and category URLs are indexed on both gravipack.com and www.gravipack.com

`ecom-host-duplication` · Technical SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** The orchestrator reports that search results show both https://gravipack.com/... and https://www.gravipack.com/... URLs. This sub-agent could not re-run searches or check redirect or canonical headers (site blocked by network policy).

<https://gravipack.com/> · <https://www.gravipack.com/>

**Why it matters.** If both hosts answer with 200 and no consistent canonical, every product exists twice. External links (Decathlon, press, crowdfunding) are split between hosts. For Shopping and free listings, the feed's link domain must match the verified website, and a host mismatch can cause disapprovals.

**SEO effect.** Link equity and ranking signals are split. Duplicate-content clustering lets Google choose the canonical. Merchant Center landing-page mismatches are possible. Search Console data is fragmented.

**How to fix.** 1) Choose one host (whichever already has more backlinks, as shown in Search Console > Links). 2) In WordPress > Réglages > Général, set both 'Adresse web de WordPress' and 'Adresse web du site' to that host. 3) Add a server-level 301 for the other host, preserving the path. Apache example: RewriteCond %{HTTP_HOST} ^gravipack\.com$ [NC] / RewriteRule ^(.*)$ https://www.gravipack.com/$1 [R=301,L] (invert if the apex is chosen). 4) Make sure the SEO plugin outputs a self-referencing absolute canonical on the chosen host. 5) Use a Domain property in Search Console, resubmit the sitemap, and update the Merchant Center feed URLs. 6) Ask Decathlon, press and KissKissBankBank to update their links (optional).

**Verifier notes.** The recorded inventory holds 40 apex (gravipack.com) and 58 www.gravipack.com URLs, but they are different paths. No product or category path was recorded on both hosts; only the homepage was reported on both, by the orchestrator. So 'every product exists twice' and 'product and category URLs indexed on both hosts' are not shown. What is shown is mixed-host indexing. That fits a missing or inconsistent host redirect or canonical, but it also fits a stale index after a fix, and WebSearch's engine is not Google. Redirects and canonicals can only be checked on the live site (blocked here) or in Search Console URL Inspection. The finding misses a more concrete host problem: a third host, presta.gravipack.com (the legacy PrestaShop store), has 16 indexed URLs, including the home page, categories and 6 legacy product pages. Downgraded from High to Medium until a 200 response on both hosts is confirmed.

### The audited domain gravipack.fr has no indexed pages, and it is unclear whether it 301-redirects to the official .com store

`ecom-fr-domain-consolidation` · International / Domains · auditor severity **Medium** → verifier **unverifiable**, severity **Low**

**Evidence.** The orchestrator reports that a search for site:gravipack.fr returned nothing from gravipack.fr, while the official indexed store is gravipack.com. The network policy blocks gravipack.fr, so I could not check its redirect status.

<https://gravipack.com/>

**Why it matters.** French users and journalists naturally type or link to the .fr. If it does not redirect path-for-path to the store, those visits and any links pointing to it are lost. If it serves a parked or duplicate site, it confuses the brand entity.

**SEO effect.** Type-in and referral traffic is lost, link equity from links to .fr is wasted, and there is entity ambiguity (two brand domains) for Google's Knowledge Graph and AI answers.

**How to fix.** Make gravipack.fr (apex and www) return a 301 to the chosen .com host with the path preserved (registrar or server rule: https://gravipack.fr/* → https://www.gravipack.com/$1). Never serve a copy of the store on .fr without hreflang/canonical. List only the .com in Organization schema 'url' and in all directory profiles. Keep the .fr registered to protect the brand.

**Verifier notes.** Nothing new could be checked. gravipack.fr is blocked by the network policy, and a PageSpeed call against gravipack.fr earlier in this run failed with a 429 quota error, so no final URL is known. The backlink sub-report recorded in this run lists 'gravipack-fr-no-link-profile'. That suggests few or no links point to .fr, which weakens the 'wasted link equity' effect. Lowered to Low. Raise it back to Medium if gravipack.fr appears on packaging, press or old campaigns, or if it does not resolve at all. The user named gravipack.fr as the site, so its status must be stated clearly in the report.

### Unsubstantiated health claims ('anti douleur', 'anti mal de dos', 'reimbursed by social security') in product titles and press create E-E-A-T and Shopping-policy risk

`ecom-health-claims` · Brand / Reputation · auditor severity **High** → verifier **confirmed**, severity **High**

**Evidence.** A relayed product SERP title contains 'anti douleur': 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur'. All 7 relayed titles use 'anti mal de dos'. challenge.ma reportedly calls it the 'first backpack reimbursed by social security'. randonner-leger.org forum threads reportedly doubt the scientific study. None of this was re-verified here (search budget exhausted).

`challenge.ma` · `randonner-leger.org` · <https://gravipack.com/>

**Why it matters.** Back-pain relief is a health topic, so Google applies stricter E-E-A-T expectations (YMYL-adjacent). Google Merchant Center policies on misrepresentation and on unsupported health claims can lead to product disapprovals or account-level issues when product data promises therapeutic effects without substantiation. In France, health claims for non-medical products also draw consumer-protection scrutiny (DGCCRF). Visible scepticism on forums turns into a trust deficit in the brand SERP.

**SEO effect.** There is a risk of Shopping and free-listing disapproval and lower trust signals in quality assessment. Negative sentiment in third-party results lowers brand-query CTR and conversion. AI answer engines may repeat the scepticism instead of the claim.

**How to fix.** 1) Remove 'anti douleur' from all titles, feed titles and meta. Use mechanism-based wording: 'exosquelette qui reporte la charge vers le centre de gravité'. 2) Publish a /etude-exosquelette/ page with the methodology, sample size, who conducted it (lab or university), results with limitations, and a downloadable PDF. Name a qualified reviewer (kinésithérapeute or ergonome) with a bio, and add Person plus ScholarlyArticle or Report schema. 3) Check the reimbursement claim. If there is an LPPR code or medical-device (classe I) status, state it with the reference. If not, ask challenge.ma to correct it and never repeat it. 4) Keep 'mal de dos' language for the informational guide and the category hub, framed as 'conçu pour réduire la charge ressentie', backed by the study. 5) Run a Merchant Center diagnostics check after editing the feed.

**Verifier notes.** The recorded SERP evidence strengthens this finding. 'anti douleur' / 'anti-douleur' appears in the Sherpa Kaki title (3 URLs), in the Light Promax titles and in the slug 'porte-outil-anti-douleur'. 'allège le poids de 92%' appears in the scolaire category title and in the post /inventeur-dun-sac-a-dos-en-apesanteur/, and Decathlon listing titles repeat 'Allège la charge de 92%'. 'anti-TMS' appears in the randonnée and claie-de-portage category titles. Superlatives appear too: 'Le seul sac à dos au monde…' (presta Hiking 33), 'le meilleur sac a dos au monde' (presta livraison page), and the City slug 'certainement-le-meilleur-sac-au-monde'. challenge.ma ranks for 'sac à dos remboursé sécurité sociale mal de dos' with the reimbursement claim, and no official source appeared in that SERP. 'gravipack arnaque efficace 92%' returned 8 randonner-leger.org threads, all sceptical. 'gravipack étude Lyon' returned only third-party pages (randonner-leger, a univ-lyon1 Moodle page, maddyness, europe1), with no study page on gravipack.com. A legacy study page does exist at presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack. Whether Gravipack uses Merchant Center is unknown, so the Shopping-disapproval part still needs an on-site or account check. I kept High because of the YMYL-adjacent claims, the possible regulatory exposure and the sceptical UGC that dominates brand-plus-claim SERPs.

### Review footprint is thin and fragmented: Trustpilot is surfaced on the Spanish locale, there is no evidence of on-site product reviews, and critical third-party reviews occupy brand and model results

`ecom-reviews-footprint` · Brand / Reputation · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Relayed by the orchestrator (not re-verified): the Trustpilot result surfaced is es.trustpilot.com/review/gravipack.com, not the FR locale. outzer.fr has a critical review of the Sherpa 45. randonner-leger.org forum threads are sceptical of the study. The orchestrator relayed no star counts or review volumes, and this sub-agent could not search for them. Whether product pages have on-site reviews or aggregateRating schema could not be checked (site blocked).

`es.trustpilot.com/review/gravipack.com` · `outzer.fr` · `randonner-leger.org`

**Why it matters.** For a premium product (around €249–289 relayed) that makes a novel claim, reviews are the main conversion and trust lever. Product review stars need first-party, on-page reviews with aggregateRating (ratingValue + reviewCount). A thin first-party review base pushes third-party critical pages up in brand-plus-'avis' SERPs. The claude-seo local and maps benchmarks use 10+ reviews, 4.5+ stars and steady recency as health thresholds.

**SEO effect.** No review-star rich results on product pages, so CTR is lower. Negative results dominate for 'gravipack avis' and 'gravipack sherpa avis'. AI assistants weight third-party sentiment when answering 'Gravipack est-il efficace ?'.

**How to fix.** 1) Turn on WooCommerce native reviews limited to verified owners (Réglages > Produits > 'Les avis ne peuvent être laissés que par des clients vérifiés'), or use a Google-approved review aggregator for Seller Ratings and Product Ratings (e.g., Trustpilot or Avis Vérifiés/Skeepers). 2) Send post-purchase review emails at about 3 weeks of use, to every customer and without pre-screening, because review gating is banned. 3) Output Product.aggregateRating and review only from reviews visible on the page. 4) Point the Trustpilot invitations to the FR profile and reply to every review, negative ones included. 5) Publish a factual reply to the outzer.fr critique: thank them and, in a 'Questions fréquentes sur l'exosquelette' page, address weight, ventilation and price trade-offs. 6) Track 'gravipack avis' SERP composition monthly.

**Verifier notes.** The SERP composition is confirmed from recorded results. 'gravipack avis' returned es.trustpilot.com/review/gravipack.com and unrelated noise, with gravipack.com absent. 'gravipack sherpa avis test' returned the outzer.fr Sherpa 45 review (negative: about €240, real capacity reported at about 30 L), randonner-leger.org ×4 and Trustpilot. Brand-plus-'92%/arnaque' queries are 100% sceptical UGC. However, no Trustpilot rating or review count was recorded, so 'thin' is unproven. The site also has a /gravipackers/ testimonials page in the index, so some first-party social proof exists; whether product pages have reviews or aggregateRating needs an on-site check. The 'Spanish locale' point is a misreading. Trustpilot has one global profile per domain, and es./fr. subdomains only change the interface language. The US-based WebSearch index simply surfaced the es. URL. Downgraded to Medium: rating and volume are unknown, and the impact is mainly on CTR and conversion, not rankings.

### Decathlon marketplace listings probably compete with the official store for model queries, and price parity across channels is unverified

`ecom-marketplace-cannibalisation` · E-commerce · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Relayed: decathlon.fr/brands/gravipack lists Sherpa 45, Hiking 33 and Feather school bags. A forum mentions about €249. The official Oslo 60+10L shows €289 in a relayed SERP. The Decathlon seller name, prices per model and listing ranks for 'gravipack sherpa 45' or 'gravipack hiking 33' could not be checked here (search budget exhausted). Amazon, Cdiscount, Fnac, Rakuten, ManoMano and Alltricks coverage is unknown.

`decathlon.fr/brands/gravipack` · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** Decathlon's domain authority usually outranks a small D2C store for exact product-name queries. If Decathlon also shows a lower price, or more reviews, the official site loses the sale and the margin. Different model names across channels (e.g., 'Sherpa 45' on Decathlon vs 'Sherpa Kaki' on the site) split brand demand.

**SEO effect.** Channel cannibalisation for model and navigational queries, lower share of clicks for the official store, and possibly the Shopping Buy Box or price-comparison units favouring the marketplace.

**How to fix.** 1) Audit every channel. Run the 'Marketplaces' and 'Price parity' queries in the backlog table, then record seller, price, shipping, review count and rating per model. 2) Align naming: same model name plus capacity everywhere ('Sherpa 45 L'), with the same GTIN-13 on the site, in the Merchant Center feed and on marketplaces. 3) Make the official PDP the most complete page: unique 400+ word description, a specs table (volume, weight, back length, materials), a size and fit guide, a video, the study link, FAQ and reviews. Give marketplaces a shorter, different description so they do not duplicate the PDP. 4) Keep advertised prices consistent or justify differences (bundle, warranty), within French competition law (no imposed resale price; use a recommended retail price). 5) Add Product + Offer schema with price, priceCurrency EUR, availability, shippingDetails and hasMerchantReturnPolicy, and activate Merchant Center free listings so the official store appears next to the marketplace in Shopping.

**Verifier notes.** This is off-site SERP evidence, so 'needs-on-site-check' is not the right confidence. In standard-mode results, decathlon.fr/vc/gravipack ranked for 'sac à dos anti mal de dos' and 'meilleur sac à dos pour le mal de dos' while gravipack.com did not. The Decathlon Hiking 33 listing ranked for 'sac à dos exosquelette' (extended mode). site:decathlon.fr gravipack showed Feather noir, Feather gris, Feather Plus, Safar Vibe, Business Talk and Hiking 33 listings, with titles 'Allège la charge de 92%'. The Decathlon seller is Kid'Abord, not Gravipack. Sherpa 45 was €149.90 (was €249) during an 18 June–30 August 2026 promotion, which has now ended, so current prices and parity are unknown. Gravipack is also listed on Nature & Découvertes through Kid'Abord (return address 'RETOUR GRAVIPACK', SODILOG, Colmar). Third-party listicles and retailers (ergo-corner with a dedicated Gravipack page, accergo, norveya) also take head-term clicks. The marketplace listings use legacy model names (Feather, Safar Vibe, Business Talk), which supports the naming-alignment fix.

### Crowdfunding-era model names (Feather, City Connect, Business Talk, Road Adventure) differ from the current range (Sherpa, Hiking, Oslo, Austerlitz, Rome) without a visible lineage

`ecom-legacy-model-names` · E-commerce · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** Relayed: the KissKissBankBank campaign named the models Feather, City Connect, Business Talk and Road Adventure. The current relayed SERP product titles name Sherpa, Hiking, Oslo, Austerlitz and Rome. Feather is reportedly still listed on Decathlon. Whether legacy URLs redirect could not be checked.

`decathlon.fr/brands/gravipack` · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** Press articles (journaldugeek 2021, neozone) and crowdfunding pages still send people searching for the old names. If those searches end on 404s or on nothing, the demand goes to forums or competitors, and links to old product URLs are wasted.

**SEO effect.** Brand-plus-model queries that hit discontinued names are lost, and links pointing to retired product URLs are wasted.

**How to fix.** 1) Keep a 'Nos modèles' page that maps each legacy model to its successor ('Business Talk → Rome'), with short text so Google can link the names. 2) Use the Redirection plugin to 301 retired product URLs to the successor or the category, not to the homepage. 3) For discontinued models, keep the page with 'Ce modèle est remplacé par …' and Offer.availability = Discontinued while it still gets traffic, then redirect.

**Verifier notes.** The premise is partly wrong. Several crowdfunding or early names continue in the current range: Business Talk (now 'Business Talk V4', 3 URLs), Hiking (30 L gris, terracotta), Sherpa (Sherpa 45 already existed on the legacy store) and City ('City Connect' became 'City'). So 'names differ without lineage' applies only to Feather, Road Adventure and Safar Vibe. What the finding misses is that the legacy PrestaShop store presta.gravipack.com is still indexed with product pages for Safar Vibe, Business Talk, Hiking33, Road Adventure, Sherpa 45 and Feather. Decathlon still sells Feather, Safar Vibe and Business Talk under those names, and KissKissBankBank FAQ pages rank for 'sac à dos qui soulage le dos et les épaules'. Recommend a separate Medium finding: 'Legacy store presta.gravipack.com still indexed'. Whether it serves 200s or redirects needs an on-site check.

### No evidence of segment hubs (randonnée / urbain-business / scolaire) or a B2B page (entreprises, QVT, CSE, médecine du travail, forces armées)

`ecom-segment-and-b2b-landing` · E-commerce · auditor severity **Medium** → verifier **refuted**, severity **Low**

**Evidence.** The relayed range spans hiking (Sherpa, Hiking, Oslo), business and urban (Rome 'business', Austerlitz) and school (Feather, plus a blog post aimed at children: /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/). challenge.ma reportedly says the product was tested by the French Army / Foreign Legion in 2017. No category or B2B URLs appeared in the relayed evidence. Whether they exist on the site could not be checked.

<https://gravipack.com/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/> · <https://gravipack.com/boutique-gravipack/> · `challenge.ma`

**Why it matters.** Each segment has its own query language and buyer: parents ('cartable ergonomique', 'poids cartable mal de dos'), commuters ('sac à dos ordinateur ergonomique'), hikers ('sac de randonnée report de charge'). B2B buyers (occupational-health services, HR/QVT, CSE gifts, public bodies, armed forces) search for 'sac ergonomique entreprise', 'prévention TMS port de charge' and 'cadeau CSE'. These are higher-value, lower-competition opportunities, and the brand already has proof points for them (army test, startup credentials).

**SEO effect.** Without matching pages, the site cannot rank for segment-specific or B2B intent. The army and test credentials are not used as E-E-A-T and B2B trust signals.

**How to fix.** 1) Create three segment categories (see keyword map). Each gets a unique intro, a short buying guide (how to fit a pack, the load-to-bodyweight rule of thumb for school bags with a cited source), FAQ and links to the matching models. 2) Create /entreprises/ (Solutions pour les entreprises): use cases (TMS prevention, field technicians, commuting staff, CSE gifts), volume pricing request form, customisation, invoices, case studies, any army/Legion test reference with written permission. Add Organization plus Service schema. 3) Add a 'Professionnels' link in the header and footer. 4) Have the school guide reviewed by a paediatric physio for E-E-A-T.

**Verifier notes.** Recorded site: SERPs contradict 'no evidence of segment hubs'. Ten segment sub-categories under /categorie-produit/tous-les-sacs-a-dos-exosquelette/ are indexed: randonnée, scolaire, business/télétravail, voyage, urbain, médical, militaire/tactique, outillage, claie de portage and nouveaux. B2B signals are also indexed: /produit/fabrication-professionnelle-gravipack/ ('fabrication professionnelle, cadeaux d'entreprise et objets publicitaires haut de gamme'), a custom-order payment-link product, posts on RATP agents and SOFINS special forces, and /categorie/militaire/. What survives, at Low: the B2B offer sits on a WooCommerce product URL rather than a dedicated landing page. The real segment problem is different and could be reframed as a new finding: the hubs exist but do not rank. Gravipack was absent for 'cartable ergonomique', 'sac à dos scolaire ergonomique collège', 'sac à dos porte-outils ergonomique artisan', 'sac à dos tactique militaire ergonomique' and 'sac à dos secouriste médical ergonomique'. The category slugs run to 129–151 characters, and their intro content is unknown (needs an on-site check). The 'Foreign Legion 2017' claim is still unverified.

### No comparison or alternatives content to answer comparison intent and the scepticism visible on forums and reviews

`ecom-comparison-content-gap` · Content Quality · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Relayed: randonner-leger.org threads question the study, and outzer.fr published a critical Sherpa 45 review. Both are typical comparison and evaluation intent ('est-ce mieux qu'un sac classique ?'). I could not collect competitor SERP data (which brands and domains rank for 'sac à dos anti mal de dos', 'sac de randonnée report de charge', and so on) because the search budget was exhausted. Competitor names in the brief (Osprey, Deuter, Gregory, Lowe Alpine, Aarn, Ergobag, Satch, Tann's, Cameleon, Decathlon Forclaz) are hypotheses that still need checking against French SERPs.

`randonner-leger.org` · `outzer.fr`

**Why it matters.** Buyers of a €250+ niche bag compare it with known brands and with 'normal' hip-belt designs. If the brand does not publish a fair comparison, third parties set the narrative. Per seo-competitor-pages, vs, alternatives and comparison-table pages target high-intent patterns and earn AI citations when they are factual and sourced.

**SEO effect.** Comparison and 'avis' queries are left to forums and reviewers, with lower conversion from undecided buyers and weaker topical authority for the 'ergonomic backpack' cluster.

**How to fix.** 1) Start with low-risk internal content: 'Comparatif des sacs Gravipack', a model-picker table (volume, weight, use, price 'au [date]'). 2) Then 'Exosquelette vs ceinture lombaire : comment chaque système répartit la charge' (mechanism page with diagrams and the study). 3) Only after running the competitor-SERP queries in the backlog table, publish 1–3 named comparisons following the seo-competitor-pages fairness rules: verifiable specs linked to the competitor's own page, 'prix au [date]', a statement that the page is written by Gravipack, honest strengths of the competitor, a 'Dernière mise à jour' date, and a named expert author. Title formula: '[A] vs [B] : [différenciateur clé] (2026)'. Use ItemList schema for roundups and Product schema only for your own products. Avoid mass 'alternative' pages, which the claude-seo quality gates flag as a penalty risk.

**Verifier notes.** Recorded SERPs support the gap. For 'meilleur sac à dos anti mal de dos' (extended), ergo-corner ×2, norveya, accergo, karkoa, arsayo, techradar and randonner-leger ranked, with only the gravipack.com homepage among them. 'meilleur cartable ergonomique comparatif 2026' returned avis-parents ×4, meilleurtest ×3 and futura-sciences ×2. zeoutdoor's comparison ranked for 'sac à dos randonnée anti mal de dos'. None of the 98 recorded gravipack.com URLs is a comparison page, but that sample is SERP-based, so absence on the site is likely rather than certain. Competitors seen in French SERPs: Osprey (including Aura AG 'Anti-Gravity', which is directly relevant to 'sac à dos anti gravité', a query where Gravipack is absent), Deuter (Futura, Voyager, Scula), Ergobag, Tucano Marte Gravity, Bon Chic Bon Dos, Thule, Salomon, Arsayo, Karkoa and Ergonovie. The hypothesised Gregory, Lowe Alpine, Aarn, Satch, Tann's, Cameleon and Forclaz did not appear and should be dropped unless verified. A faster route the fix misses is digital PR: getting included in, or corrected in, the listicles that already rank.

### Legal entity, NAP and GBP status are unverified, with a possible confusion with another company ('Kid'abord', Loire-Atlantique)

`local-entity-nap-unverified` · Local SEO · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Relayed: lespepitestech.com lists Gravipack as a French Tech Aix-Marseille / Région Sud startup (founder Mohammed Errafi; love-money raise of €346k in 2019). One search summary linked the brand to a company 'Kid'abord (Loire-Atlantique)', which is unverified and conflicts geographically with Aix-Marseille. This sub-agent could not search societe.com, Pappers, PagesJaunes, LinkedIn or Google Maps (budget exhausted), so the NAP comparison could not be done. Under seo-local business-type detection, Gravipack is an online-only e-commerce brand (no evidence of a showroom), so GBP eligibility depends on whether staffed premises exist.

`lespepitestech.com`

**Why it matters.** For an e-commerce brand, consistent entity data (legal name, SIREN, address, phone, founder, sameAs) lets Google and AI systems resolve 'Gravipack' to one organisation. An association with an unrelated company (or a former legal entity) can show the wrong address or phone in knowledge panels and directories. That hurts trust, and some buyers check societe.com or Pappers before spending €250+.

**SEO effect.** Knowledge-panel and AI-answer accuracy suffer (wrong company details possible). Trust signals are weaker. If GBP is ineligible but created anyway, there is a suspension risk.

**How to fix.** 1) Check the legal entity (SIREN, registered address, legal name) on the INSEE/RNE register. Then record the NAP in a single source of truth and apply it to the site footer, the mentions légales page, the CGV, LinkedIn, lespepitestech, Decathlon seller info and Trustpilot. 2) If 'Kid'abord' is a former name or holding company, say so on the 'À propos' page. If it is unrelated, ask the directories that show the link to correct it. 3) Add Organization schema on the homepage: name, legalName, url (the chosen .com host), logo, founder (Person: Mohammed Errafi), foundingLocation, address (PostalAddress), telephone, vatID/identifier (SIREN), sameAs [LinkedIn, Trustpilot, KissKissBankBank, lespepitestech, Decathlon brand page]. 4) Create a Google Business Profile only if the company has premises where staff meet customers during stated hours (Google requires in-person contact; online-only stores are not eligible). Otherwise rely on the Organization entity plus Merchant Center. 5) Claim Bing Places / Bing entity data (feeds Copilot and ChatGPT search) only if eligible on the same basis.

**Verifier notes.** The recorded evidence confirms that entity data conflicts across sources. The gravipack.com mentions légales (as shown in SERP) name the publisher 'EXOSQUELETTE LIGHT', Paris, hosted by Gandi. motherbase.ai shows a Vincennes address. lespepitestech places the company in French Tech Aix-Marseille / Région Sud. Logistics returns go to 'RETOUR GRAVIPACK', SODILOG, Colmar. The 'Kid'abord' link is now largely explained: Kid'Abord is the seller of Gravipack listings on the Decathlon marketplace and on Nature & Découvertes. It looks like a reseller or distribution partner, not an unrelated company confused with the brand. Its Loire-Atlantique location was not verified. The site has two contact URLs (/contact-gravipack/ and /contacts/). The GBP reasoning is correct: an online-only brand without staffed premises open to customers is not eligible.

### No 'points de vente' or store-locator page is evident for physical retail or partner pharmacies

`local-store-locator` · Local SEO · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** No retailer, pharmacy or outdoor-shop stockist pages appear in the relayed evidence. Decathlon presence is described as the marketplace (online). Whether Decathlon stores, orthopaedic shops or pharmacies stock the bags could not be checked (search budget exhausted, site blocked).

`decathlon.fr/brands/gravipack`

**Why it matters.** A bag sold mainly on fit and comfort benefits from 'try before you buy'. If physical stockists exist, a crawlable store locator captures 'gravipack [ville]' and 'où acheter gravipack' queries and drives in-store conversions. If none exist, an 'Essai 30 jours' policy page plays the same reassurance role.

**SEO effect.** 'Où acheter' and local-intent brand queries are missed, and the brand loses a trust and conversion signal.

**How to fix.** If stockists exist: build /points-de-vente/ with one crawlable, server-rendered entry per stockist (name, address, phone, models stocked), plus an index page by region. Avoid thin city-swap pages (claude-seo warns at 30+ location pages and requires 60%+ unique content). Mark up each stockist with Store schema linked to the Organization via 'brand'. Ask stockists to link to the official model pages. If there are no stockists: publish a clear 'Essai et retours' page and reference it with hasMerchantReturnPolicy in the Product schema.

**Verifier notes.** No stockist or 'points de vente' URL is in the 98-URL recorded inventory. The retail presence seen off-site is online: the Decathlon marketplace and Nature & Découvertes listings (both through Kid'Abord), plus ergo-corner, an ergonomics retailer whose Gravipack page ranks at the top for head terms. No physical stockist was found, so the finding's premise is still hypothetical. The fallback, a 'where to buy / authorised resellers' page linking to the Decathlon, Nature & Découvertes and ergo-corner pages, is the more realistic version.

### A blog post slug has a word-join error ('…autresvos-enfants…'), a sign of slugs auto-generated from titles

`url-slug-hygiene` · On-Page SEO · auditor severity **Low** → verifier **confirmed**, severity **Low**

**Evidence.** The relayed URL is /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/. 'autresvos' is missing a separator, probably from a title with a line break or punctuation ('… les autres ! Vos enfants …'). Relayed product URLs follow a /produit/<long-slug>/ pattern, which suggests long, keyword-stuffed slugs.

<https://gravipack.com/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/>

**Why it matters.** Clean, short slugs that contain words help readability and sharing. A small but visible quality signal, and the long product slugs probably repeat the same head term as the titles.

**SEO effect.** Minor. A slightly weaker URL relevance signal and lower trust and shareability. Changing slugs without redirects would cause 404s.

**How to fix.** Only if the page gets little traffic: change the slug to /sac-a-dos-ergonomique-enfant/ (or merge it into the new 'cartable ergonomique' guide) with a 301 from the old URL via the Redirection plugin. For new products, use short model slugs (/produit/sherpa-45/) and do NOT mass-rename existing product slugs unless you redirect every one.

**Verifier notes.** The URL is confirmed in the recorded inventory. Its SERP title is 'Un sac à dos pas comme les autres… les épaules de vos enfants vont adorer'. The slug drops 'les épaules de', so the title was edited after the slug was generated. The broader slug problems are confirmed too. 30/39 product URLs exceed 100 characters (median 110, longest 205 for the City product). 37 slugs repeat 'anti-mal-de-dos'. Two slugs end in '-copie' (Compostelle 65 L, batterie solaire). Others contain 'pas-cher' and 'certainement-le-meilleur-sac-au-monde', and the typo 'randonner' appears in 2 slugs. Low is the right severity; the no-mass-rename advice is correct.
