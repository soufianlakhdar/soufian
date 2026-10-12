# Phase 1 — indexation-domains

Searches run: 68

## Evidence base

I ran 68 WebSearch queries (about 40 extended, the rest standard). They covered site: operators for each host, brand plus model and page-type queries, generic money keywords, third-party domain references and entity checks. WebSearch is a US-based backend, not Google.fr. It honoured the site: operator only some of the time, so result order is a rough indicator, not a Google ranking. From those results I built an inventory of 114 unique Gravipack-owned URLs: 40 on https://gravipack.com (apex), 58 on https://www.gravipack.com and 16 on the legacy PrestaShop subdomain https://presta.gravipack.com. No URL on gravipack.fr or www.gravipack.fr appeared for any query (site:gravipack.fr, "gravipack.fr", "www.gravipack.fr", "gravipack.fr" sac à dos). No other TLD (.eu, .de, .ma, .net) or subdomain (shop., blog., boutique., en.) appeared either, and no http:// URL was seen. Titles are as shown in search results. Google or this engine may rewrite them, and several URLs returned two different titles across queries, which is evidence of rewriting or recent edits. Snippet text came from the tool's summaries, not raw meta descriptions. Per the network policy and the claude-seo rule, I did not fetch any live page. Canonical tags, meta robots, redirects, robots.txt, the XML sitemap, headers, schema and CWV were NOT observed and are listed as open questions. Findings rest only on URLs and titles actually returned. Inventory counts are a lower bound: the shop itself reports 83 products, and only 39 product URLs surfaced.

## claude-seo commands applied

- /seo technical (skills/seo-technical/SKILL.md + agents/seo-technical.md): Indexability (duplicates, www vs non-www, parameter URLs, thin archives, index bloat), URL Structure (descriptive slugs, >100-char flag, hierarchy), Security (HTTPS in index only). Applied from SERP evidence only.
- /seo sitemap (skills/seo-sitemap/SKILL.md + agents/seo-sitemap.md): 'compare crawled pages vs sitemap' method used as SERP-inventory vs expected-architecture comparison; the severity table was reused for non-canonical, redirected and duplicate URLs. The XML sitemap itself was not fetched.
- /seo hreflang (skills/seo-hreflang/SKILL.md): ccTLD (.fr) vs .com geo-signal hierarchy, cross-domain consolidation, protocol consistency, and whether any alternate-language versions exist. None were found.
- /seo page (skills/seo-page/SKILL.md): title 50-60 chars with the keyword first and the brand last, meta description 150-160 chars, URL short/descriptive/hyphenated/no parameters. Applied to SERP-shown titles and snippets.
- references/quality-gates.md: title gates (30-60 chars, unique, keyword near start, brand at end, no keyword stuffing), meta-description gates (120-160, unique, not templated), word-count minimums (cited only for missing page types).
- claude-seo error-handling rule 'URL unreachable → report clearly, do not guess site content': every live-site check (HTML, canonical, robots, headers, redirects, sitemap) is moved to open_questions_need_site_access.

## What works

- Every Gravipack URL seen in the search results (114/114) is served over HTTPS. No http:// URL is indexed.
- One brand domain is clearly established: LinkedIn, Les Pépites Tech and Trustpilot (fr/es) all reference gravipack.com. Brand equity is not split across .fr/.com in third-party citations.
- There is a clear WooCommerce architecture: /produit/ for products and /categorie-produit/tous-les-sacs-a-dos-exosquelette/<use-case>/ for products. Use-case subcategories exist for randonnée, scolaire, business/télétravail, voyage, urbain, médical, militaire, outillage and claie de portage. This is the right hub-and-spoke base for category-level keywords.
- Index coverage is broad. Home, shop, about 15 category URLs, about 39 product URLs, CGV, mentions légales, FAQ, contact, about/engagements and testimonials (/gravipackers/) are all indexed. A dated blog (/articles/, 2022-2025) with thematic categories also exists.
- The home page title leads with the brand and contains the two core terms ('anti mal de dos', 'exosquelette'). At 63 chars it is only slightly over the 60-char gate.
- The brand already shows up for generic money queries: 'sac à dos anti mal de dos', 'sac à dos exosquelette' and 'sac à dos anti mal de dos exosquelette' each return 2-8 gravipack.com URLs in this engine. The topical relevance exists, but it is spread over too many URLs.
- Several category titles are close to best practice in length and intent: hiking category 63 chars, outillage category 63, claie de portage 61, 'Tous les sacs à dos anti-mal de dos exosquelette Gravipack' 58.
- Legal and trust pages are present and indexed (mentions légales naming the publisher and host, CGV, FAQ). This is a baseline for e-commerce trust.

## Specialist scores

| Category | Score | Rationale |
|---|---|---|
| Index hygiene (duplicates, parameters, thin archives, test pages) | 30 | These are confirmed in the index: about 9 duplicate product clusters, 4 parameter URLs (including add-to-cart), 2 attribute archives, a tag archive, two blog category bases, a /test/ page, 2 contact pages and '-copie' slugs. Measured against seo-technical Indexability checks, most fail. |
| Domain / host consolidation (www vs apex, .fr vs .com, legacy subdomain) | 30 | Three hosts are indexed (apex 40, www 58, presta 16), and the legacy store has stale prices. The one positive is that gravipack.fr is not split off (0 indexed) and third parties point at .com. The redirect setup itself was not measurable. |
| Title tags as shown in SERP | 35 | Only 22/98 titles are within 60 chars, and 5 are under 30. There are 4 site-name suffix variants, 6 duplicate-title clusters, typos, missing model names and observed rewrites. Some category titles are near-good. |
| URL / slug structure | 40 | The hierarchy is logical (/produit/, /categorie-produit/<use-case>/) and everything is HTTPS. But 30/39 product URLs exceed 100 chars, slugs are sentence-like or keyword-stuffed, there are typos ('autresvos', 'randonner', 'oganizer'), slug/content mismatches, and a parallel /produit-gravipack/ base. |
| Keyword targeting / cannibalisation | 35 | 53/98 titles target 'anti mal de dos'. The home page sits behind product pages and a reseller for its own head term. More than 10 URLs target 'sac randonnée anti mal de dos', and none of them appeared for that query. There is no informational content for guide-intent SERPs. |
| Meta descriptions | n/a | Raw meta description tags could not be observed. WebSearch returns tool summaries, not the snippet text. Only indirect evidence was available (cart boilerplate in excerpts). |
| Crawlability (robots.txt, XML sitemap) | n/a | Not measurable. robots.txt and the sitemap could not be fetched because the sandbox blocks the site. See open questions. |
| Security / HTTPS | n/a | All 114 indexed URLs are https (positive), but certificate validity, HSTS, redirect chains and security headers were not measurable, so no category score is given. |
| Hreflang / international | n/a | Not applicable: a single French-language site with no alternate versions found. Nothing to validate. |
| Overall: indexation, domain setup and SERP-visible on-page signals | 34 | This is the weighted view of the measured categories above (index hygiene 30, host consolidation 30, titles 35, URLs 40, cannibalisation 35). The site is well indexed in breadth, but the indexed set is duplicated across hosts, URLs and parameters, and its SERP signals are long, repetitive and inconsistent. |

## Raw findings (with verifier verdicts)

### Legacy PrestaShop store presta.gravipack.com is still indexed (16+ URLs) with outdated prices, discontinued models and contradicting shipping terms

`legacy-presta-subdomain-indexed` · Technical SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** site:presta.gravipack.com and brand/model queries returned 16 URLs on the old PrestaShop host. They include the home page (title 'Gravipack, le sac a dos scolaire, business et randonnée, ce sac à dos allègent le poids…', 126 chars), categories (/2-accueil, /22-produit, /24-sac-a-dos-sport, /72-sac-a-dos-scolaire, /73-gravipack), products (Safar Vibe 199 €, Business Talk 199 €, 'hikking33' 229 €, Road Adventure 199 €, Sherpa 45 at 249 €, Feather 149 €), a CMS shipping page that says orders are 'commandes de réservation' with 2-3 months lead time, an HTML site map (/plan-du-site-gravipack), /40-etude-scientifique-soulage-le-dos-gravipack and /59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack. Presta URLs also surfaced inside site:gravipack.com queries for 'categorie-produit', 'sac business ordinateur', 'CGV livraison' and 'presse Lépine'. On gravipack.com the Sherpa is 99-149,90 € and delivery is 1-2 days in France.

<https://presta.gravipack.com/> · <https://presta.gravipack.com/accueil/19-sac-a-dos-gravipack-sherpa-45.html> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://presta.gravipack.com/content/1-livraison-sac-a-dos-gravipack> · <https://presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack> · <https://presta.gravipack.com/59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack> · <https://presta.gravipack.com/plan-du-site-gravipack> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html> · <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/>

**Why it matters.** Two storefronts for the same brand compete for the same queries (brand, 'Sherpa 45', 'Hiking 33', 'sac à dos scolaire Gravipack', 'Concours Lépine Gravipack'). Google has to choose which one to show. The legacy one shows prices 60-150 € higher, models that no longer exist, and a delivery promise that contradicts the CGV. Buyers who land there either bounce or lose trust. The 'commandes de réservation 2-3 mois' text is especially damaging given the forum scepticism about the brand.

**SEO effect.** Links and relevance are split between hosts. The main domain may lose impressions to stale URLs for brand+model queries, because the presta pages are older and have accumulated links (crowdfunding era, 2019-2021 press). Quality and helpfulness signals are diluted by outdated, contradictory content. If Merchant listings or Product snippets are used, price mismatches across the brand's own URLs add risk. Users who click a presta URL and bounce send negative engagement signals for the brand query.

**How to fix.** 1) Before you redirect, move the one unique asset: rebuild the study page from /40-etude-scientifique-soulage-le-dos-gravipack on gravipack.com (e.g. /etude-scientifique-lbmc-lyon-sud/) with the method, sample, authors and a PDF. Link it from the FAQ, home page and every product.
2) Build a 1:1 redirect map (spreadsheet: old URL → new URL → status):
- Sherpa 45 → current Sherpa product (pick the main colour)
- hikking33 → Hiking Terracotta
- Business Talk → Business Talk V4 20L
- /24-sac-a-dos-sport → hiking category
- /72-sac-a-dos-scolaire → school category
- /22-produit and /2-accueil → /categorie-produit/tous-les-sacs-a-dos-exosquelette/
- /59-concours-lepine… → /gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/
- /content/1-livraison… → /conditions-generales-de-vente/ (or a /livraison-retours/ page)
- / → https://gravipack.com/
- Safar Vibe, Road Adventure and Feather (discontinued, no successor) → 410 Gone, or 301 to the closest category if they still get traffic or links.
3) Apply the map on the presta vhost (Apache/.htaccess at the PrestaShop root, or nginx). Example:
RewriteEngine On
RewriteRule ^accueil/19-sac-a-dos-gravipack-sherpa-45\.html$ https://gravipack.com/produit/<sherpa-slug>/ [R=301,L]
RewriteRule ^59-concours-lepine- https://gravipack.com/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/ [R=301,L]
RewriteRule ^accueil/13-sac-a-dos-gravipack-safar-vibe\.html$ - [G,L]
RewriteRule ^(.*)$ https://gravipack.com/ [R=301,L]   (last-resort catch-all only after the specific rules)
4) Do NOT block presta in robots.txt yet. Google must recrawl the URLs to see the 301s. If the PrestaShop back-office must stay online, put it behind HTTP auth on another path.
5) Verify presta.gravipack.com inside a Search Console Domain property (gravipack.com). Use the Removals tool only as a temporary hide while the redirects are processed. Watch the Page indexing report until presta URLs show 'Page with redirect'.
6) Keep the redirects for at least 12 months. Update any links you control (KissKissBankBank project pages, old press releases, social bios) to point to gravipack.com.

**Verifier notes.** I could not run new searches because the shared 200-call WebSearch budget was used up. I checked this against the saved SERP notes and URL inventory instead. Several separate queries did surface presta.gravipack.com URLs (/73-gravipack, Road Adventure, Business Talk, home, /72-sac-a-dos-scolaire, /24-sac-a-dos-sport, Hiking33), so 'present in the WebSearch index' holds. Three caveats:
(1) This is a US-only, non-Google engine. It can keep stale entries, and nothing shows whether presta still returns 200 or already redirects. That needs a curl -I check.
(2) The 'outdated prices' point is partly contradicted. Notes for 'gravipack decathlon sherpa 45' show Decathlon listing the Sherpa at 149,90 € 'was 249 €' (promo 18 June to 30 Aug 2026, seller Kid'Abord). So 249 € was still the regular price in 2026 and is not a stale price.
(3) The prices, the 'commandes de réservation 2-3 mois' wording and the gravipack.com '1-2 days' delivery came from search summaries that are not in the saved notes. I could not re-verify them.
A legacy subdomain that mainly affects brand+model queries is an optimisation issue (claude-seo Medium), not a sitewide ranking blocker. Raise it to High only if curl shows presta still serves 200 pages.

### Both gravipack.com and www.gravipack.com are indexed: no single canonical host (40 apex vs 58 www URLs)

`www-vs-apex-host-split` · Technical SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** The inventory splits 40 URLs on https://gravipack.com/ and 58 on https://www.gravipack.com/. The home page, /boutique-gravipack/, /mentions-legales/, /conditions-generales-de-vente/, /contacts/, /nos-engagements/ and most product categories are indexed on the apex host. /faq/, /contact-gravipack/, /articles/, /categorie/*, the about page, product/attribute archives and about 25 products are indexed on www. The shop root is on apex while its page 2 and sort/filter variants are on www. A site:www.gravipack.com query returned apex URLs mixed in. The same product appears on both hosts under different slugs (Light Promax: apex /produit/sac-a-dos-porte-outil-… vs www /produit/sac-a-dos-exosquelette-outillage-light-promax-…; G-Pack apex vs www; Sherpa Kaki apex /produit-gravipack/ vs www /produit/).

<https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/> · <https://www.gravipack.com/boutique-gravipack/page/2/> · <https://www.gravipack.com/faq/> · <https://www.gravipack.com/contact-gravipack/> · <https://gravipack.com/contacts/> · <https://gravipack.com/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/> · <https://gravipack.com/produit/sac-a-dos-college-lycee-anti-mal-de-dos-avec-exosquelette-g-pack-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-pour-la-journee-g-pack-avec-exosquelette-gravipack-pour-professionnels-et-velo/>

**Why it matters.** seo-technical Indexability lists 'www vs non-www' duplicates as a core check. When both hosts resolve without a consistent 301 and canonical, Google treats them as separate URLs. It must cluster them, and it may pick a canonical you did not choose. Mixed hosts in the index, years after launch, usually mean the redirect is missing or inconsistent, internal links point to both hosts, or canonical tags disagree with the redirect.

**SEO effect.** Internal PageRank and external link equity are split between two hosts. Crawl budget is wasted on duplicate fetches, and recrawl/consolidation of updated pages is slower. Search Console data can be fragmented if only one host property is verified. Sitemaps may list the 'wrong' host. Duplicate clusters can show a non-preferred URL in results (e.g. a www product URL with an older title).

**How to fix.** 1) Pick one host and keep it forever. Recommend https://gravipack.com: the home page, shop root and Trustpilot profile already use it.
2) WordPress → Réglages → Général: set both 'Adresse web de WordPress (URL)' and 'Adresse web du site (URL)' to https://gravipack.com.
3) Add a server-level 301 before WordPress loads. With Apache on Gandi hosting, at the top of .htaccess:
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.gravipack\.com$ [NC]
RewriteRule ^(.*)$ https://gravipack.com/$1 [R=301,L]
Also force HTTPS in the same block if it is not already done, to avoid chains.
4) Clean the database: run the 'Better Search Replace' plugin in dry-run, then live, replacing https://www.gravipack.com with https://gravipack.com in wp_posts, wp_postmeta and wp_options. Clear page cache and CDN.
5) In Yoast or Rank Math, confirm canonicals are absolute on the apex host. Regenerate the XML sitemap so it lists apex URLs only, and reference it in robots.txt (Sitemap: https://gravipack.com/sitemap_index.xml).
6) In Search Console, create a Domain property (DNS TXT at Gandi) so www, apex and presta are all covered. Resubmit the sitemap. Use URL Inspection on 10 key www URLs to confirm 'Google-selected canonical = apex'. Google can take up to about two weeks to re-cluster duplicates, so do not treat an unchanged canonical right after the fix as failure.
7) Test with 'curl -I https://www.gravipack.com/faq/'. Expect a single 301 to https://gravipack.com/faq/, no chain.

**Verifier notes.** Recomputed from the inventory: 58 www, 40 apex and 16 presta URLs, 114 in total. These counts describe the sample of URLs seen across about 60 queries, not the size of the index. Describe them as 'of the URLs observed'.
Caveats:
(1) WordPress's redirect_canonical() normally already redirects a host that does not match the site URL, and Yoast emits one canonical host. Both hosts serving 200 would therefore be unusual. The mixed index may be stale entries in a non-Google engine.
(2) Several mixed-host examples are really slug duplicates, not host duplicates: Light Promax apex /produit/sac-a-dos-porte-outil-... vs www /produit/...-outillage-light-promax-..., and the two G-Pack slugs. Those belong in the duplicate-product finding.
(3) Trustpilot always strips 'www' from profile names, so 'review/gravipack.com' is not evidence that the brand prefers the apex host.
Re-rate to High only if curl -I shows both hosts return 200 with self-referencing canonicals.

### The same products are indexed under several URLs: duplicate SKUs, '-copie' slugs and a second /produit-gravipack/ path base

`duplicate-product-urls` · E-commerce · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Identical or near-identical SERP titles on different URLs:
- Light Promax: 3 URLs (two titled 'Sac à dos outillage anti-douleur exosquelette Gravipack®').
- Cargo Max: 2 URLs titled 'Claie de portage aluminium exosquelette Gravipack pour charges lourdes'.
- G-Pack: 2 URLs titled 'Sac à dos exosquelette révolutionnaire et unique G-Pack Gravipack'.
- Hiking Terracotta: /produit/… and /produit-gravipack/sac-a-dos-revolutionnaire.
- Sherpa Kaki: /produit/… plus /produit-gravipack/sac-a-dos-sherpa-kaki and /produit-gravipack/sac-a-dos-sherpa, all with the same title.
- Pearl: /produit/… and /produit-gravipack/sac-a-dos-exosquelette-gravipack-pearl/.
- Business Talk V4: two separate 25L product pages.
- WooCommerce 'Dupliquer' leftovers: …-compostelle-…-memoire-de-forme-copie/ and …-infinity-gravipack-copie/.

<https://www.gravipack.com/produit/claie-de-portage-exosquelette-cargo-max-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/claie-de-portage-aluminium-exosquelette-anti-mal-de-dos-cargo-max-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/> · <https://gravipack.com/produit-gravipack/sac-a-dos-revolutionnaire> · <https://www.gravipack.com/produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-avec-exosquelette-gravipack-pour-toutes-vos-aventures/> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa-kaki> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa> · <https://www.gravipack.com/produit-gravipack/sac-a-dos-exosquelette-gravipack-pearl/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-25l-anti-mal-de-dos-revolutionnaire-gravipack-business-talk-v4-ergonomie-eva-memoire-de-forme/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-de-survie-65-litres-ergonomique-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme-copie/> · <https://www.gravipack.com/produit/batterie-solaire-externe-multi-port-avec-lampe-torche-et-boussole-infinity-gravipack-copie/>

**Why it matters.** Each duplicate splits reviews, links, internal links and engagement for the same product. Google consolidates the duplicates and may show the weaker URL. Duplicate titles break the quality-gates 'each page must have a unique title' rule, and the shop looks less trustworthy (same bag at several prices).

**SEO effect.** Product pages rank lower for model queries ('Gravipack Sherpa', 'Light Promax', 'Cargo Max') because signals are split. Index bloat grows ('Duplicate without user-selected canonical' in GSC). Merchant listing and Product rich results may pick inconsistent prices or URLs.

**How to fix.** 1) For every product family, choose one canonical URL.
2) Convert colour/size siblings into one WooCommerce VARIABLE product (attribute 'Couleur' for Sherpa bleu/orange/kaki, Oslo, Hiking; 'Contenance' for Compostelle 25/35/65/80 L and Business Talk V4 20/25 L) instead of separate simple products. Keep separate products only when the search demand per variant is real and the content is genuinely different.
3) Redirect every merged or duplicate URL with a 301 to the canonical (Redirection plugin or Rank Math → Redirections). Map /produit-gravipack/* to its /produit/* equivalent, then find out what creates /produit-gravipack/ (old permalink base under Réglages → Permaliens → 'Base des produits', a Pretty Links-type plugin, or a custom rewrite) and remove it.
4) Rename the '-copie' slugs (e.g. /produit/compostelle-65l/) and 301 the old slug. Delete obsolete drafts in Produits → Corbeille.
5) Give each remaining product a unique title (see title findings) and a self-referencing canonical.
6) Re-crawl with Screaming Frog (Duplicate titles / Near duplicates reports) and confirm in GSC Page indexing.

**Verifier notes.** The inventory and notes confirm the multiple URLs:
- Light Promax: 3 URLs (notes 18 and 53-55).
- Cargo Max: 2 URLs with the same title.
- G-Pack: 2 URLs with the same title.
- Sherpa Kaki: 3 URLs.
- Hiking Terracotta and Pearl: on /produit-gravipack/ as well as /produit/. The notes for 'site:gravipack.com comment choisir' confirm the second path base.
- Business Talk V4: 3 URLs.
However, a URL being indexed does not prove a live duplicate:
- An old slug that 301s, or a /produit-gravipack/ shortlink that redirects, would still show in a stale non-Google index. A short /produit-gravipack/sac-a-dos-sherpa URL showing the Sherpa Kaki title looks like a redirect or shortlink.
- The '-copie' Compostelle 65L is a different capacity from the 25L and 35L, so it is a slug-hygiene issue (product created by duplication), not a duplicate URL.
- G-Pack 'college-lycee' and G-Pack 'pour-la-journee...professionnels-et-velo' may be two real listings.
Check the HTTP status of each URL before counting it as a duplicate.

### Cart, sort and filter parameter URLs are indexed (?add-to-cart=, ?order=, filter_product_cat=)

`parameter-urls-indexed` · Technical SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Indexed parameter URLs:
- https://gravipack.com/?add-to-cart=6527, with an older title 'Accueil - Le sac à dos exosquelette GRAVIPACK anti mal au dos'.
- https://www.gravipack.com/boutique-gravipack/?add-to-cart=2678 ('Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids…').
- https://www.gravipack.com/boutique-gravipack/?order=price.
- https://www.gravipack.com/boutique-gravipack/?order=price&filter_product_cat=nouveau-sac-a-dos ('Boutique - Sac a dos anti mal de dos GRAVIPACK…', 107 chars).

<https://gravipack.com/?add-to-cart=6527> · <https://www.gravipack.com/boutique-gravipack/?add-to-cart=2678> · <https://www.gravipack.com/boutique-gravipack/?order=price> · <https://www.gravipack.com/boutique-gravipack/?order=price&filter_product_cat=nouveau-sac-a-dos>

**Why it matters.** An add-to-cart URL is an action, not a page. Each crawl can add an item to a session cart, and the URL duplicates the home or shop page. Sort and filter combinations multiply into near-infinite crawlable URLs. seo-technical flags parameter duplicates and index bloat, and seo-page requires URLs without parameters for content.

**SEO effect.** Crawl budget is wasted. Duplicate home and shop pages compete with the real ones, and the add-to-cart home duplicate even carries a different title. Parameter URLs can be chosen as canonical for the shop, and cart-session side effects can distort analytics and stock.

**How to fix.** 1) Make sure 'add to cart' buttons on archives use AJAX (WooCommerce → Réglages → Produits → 'Activer les boutons Ajout au panier en AJAX') and carry rel='nofollow' (WooCommerce default; check the theme does not override it).
2) Send noindex for parameter states. With Yoast, in a code-snippets plugin:
add_filter('wpseo_robots', function ($robots) { foreach (array('add-to-cart','order','orderby','filter_product_cat','min_price','max_price') as $p) { if (isset($_GET[$p])) { return 'noindex, follow'; } } return $robots; });
(Rank Math equivalent: filter 'rank_math/frontend/robots').
3) Make sure the canonical on these states points to the clean URL (/boutique-gravipack/ or /).
4) Once Google has dropped them (check GSC → Pages → 'Excluded by noindex'), add to robots.txt:
Disallow: /*?add-to-cart=
Disallow: /*&add-to-cart=
Disallow: /*?order=
Disallow: /*filter_product_cat=
Do this only after deindexing: a robots.txt block stops Google from seeing the noindex.
5) Identify the plugin that creates the '?order=' and 'filter_product_cat' links (WOOF, YITH Ajax Filter, etc.) and enable its 'nofollow/noindex filtered URLs' option.

**Verifier notes.** The four parameter URLs are in the inventory. Their SERP titles use old suffixes ('Accueil - Le sac à dos exosquelette GRAVIPACK anti mal au dos', '...qui allège le poids sur les épaules et le dos.') that differ from the current home and shop titles. That suggests old crawl snapshots, not current behaviour.
Four parameter URLs out of about 100 is minor index bloat, so High (claude-seo: 'significantly impacts rankings') is overstated. Medium fits.
The why_it_matters claim that bot add-to-cart hits can distort 'stock' is wrong. WooCommerce does not reduce or reserve stock on add-to-cart, only at checkout or order. Analytics and session distortion is the only valid side effect.
Current rel=nofollow, canonical and robots on these states need a live check.

### Keyword cannibalisation: 53 of 98 titles target 'anti mal de dos' and over 10 URLs compete for 'sac randonnée anti mal de dos'

`cannibalisation-anti-mal-de-dos` · On-Page SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** 53/98 SERP titles contain 'anti mal de dos', 'anti-mal de dos' or 'anti mal au dos' (28/39 product titles), and 37 slugs contain 'anti-mal-de-dos'. 66/98 titles contain 'exosquelette'.
- 'sac à dos anti mal de dos exosquelette': WebSearch returned ergo-corner.com (reseller) 1st, then Easy Travel, Light Promax and Centurion product pages, with the HOME page only 5th.
- 'sac à dos anti mal de dos': ici.fr and two ergo-corner URLs ranked above the home page.
- 'sac à dos exosquelette': the main category and the home page both appear (6th and 7th) behind a blog, a test, alloprod, ergo-corner and compostelle-autrement.
- 'sac randonnée anti mal de dos': no Gravipack URL in the results. At least 11 Gravipack URLs target it by title or slug: hiking category, Sherpa bleu ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa'), Pearl and Sherpa orange ('Sac randonner léger…'), Easy Travel and Helsinki (slug 'sac-randonner-leger-anti-mal-de-dos'), Compostelle 80L ('…randonnée 80L révolutionnaire anti mal de dos pas cher'), Oslo Rouge, Hiking Terracotta, Hiking Gris, Sherpa Kaki, plus presta /24-sac-a-dos-sport.

<https://gravipack.com/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-easy-travel-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://www.ergo-corner.com/55-gravipack> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/>

**Why it matters.** When dozens of pages send the same signal, no single page becomes the obvious best answer. Google rotates between them or prefers a focused reseller page. The home page and category pages, which should own the head terms, get outranked by individual products and by ergo-corner.com, a reseller of Gravipack's own products.

**SEO effect.** Head-term rankings ('sac à dos anti mal de dos', 'sac à dos exosquelette', 'sac de randonnée anti mal de dos', 'cartable anti mal de dos') are diluted. Positions swing as Google alternates URLs, CTR is lower because titles all look the same, and resellers take the brand's own demand.

**How to fix.** 1) Build a keyword-to-URL map (one primary query per URL) and enforce it in titles, H1s and internal anchors:
- Home → 'sac à dos anti mal de dos' (+ brand)
- /categorie-produit/tous-les-sacs-a-dos-exosquelette/ → 'sac à dos exosquelette'
- Hiking category → 'sac de randonnée anti mal de dos' / 'sac à dos randonnée ergonomique'
- School category → 'cartable / sac scolaire anti mal de dos'
- Business category → 'sac à dos ordinateur ergonomique'
- Outillage → 'sac à dos porte-outils'
- Claie → 'claie de portage'
- Products → model name + capacity + use (e.g. 'Sherpa 45L').
2) Remove the generic head term from the START of product titles. Lead with the model. Examples (≤60 chars):
- 'Sac randonnée Sherpa 45L à exosquelette | Gravipack' (51)
- 'Oslo 60+10L rouge – Sac de trek à exosquelette | Gravipack' (58)
- 'Sac à dos ordinateur City 20L à exosquelette | Gravipack' (56)
- 'Sac scolaire G-Pack 20L anti mal de dos | Gravipack' (51)
Category examples:
- 'Sac de randonnée anti mal de dos à exosquelette | Gravipack' (59)
- 'Sac à dos exosquelette : toute la gamme | Gravipack' (51)
- Home: 'Sac à dos anti mal de dos à exosquelette | Gravipack' (52).
3) Internal linking: every product links to its category with an exact-match anchor ('sacs de randonnée anti mal de dos'). The home page links to each category with its target anchor. Blog posts link to categories, not to random products.
4) Give each category 400+ words of unique intro/buying-guide copy (quality-gates: Category Page min 400 words) so it outranks its own products.
5) After two months, check GSC → Performance → Query → Pages for each head term. If more than one URL still gets impressions, consolidate further.

**Verifier notes.** Recomputed counts match:
- 53/98 titles contain 'anti mal de dos'.
- 28/39 product titles contain it.
- 37 slugs contain 'anti-mal-de-dos'.
- 66 titles contain 'exosquelette'.
The saved extended-mode notes partly contradict the SERP narrative:
- For 'sac à dos randonnée anti mal de dos' (E4), the Gravipack hiking category ranks about 5th and the home page about 6th. The intended category is ranking, so 'no Gravipack URL' only holds for the other wording or for standard mode.
- For 'sac à dos porte-outils anti mal de dos' (E10), Gravipack holds 5 of the top 10. That is SERP domination, not proof of harmful cannibalisation.
- Standard and extended results disagree with each other (standard mode showed no gravipack.com URL for 'sac à dos anti mal de dos').
Real cannibalisation (URLs alternating for one query, split impressions) can only be confirmed in GSC Performance, query to pages. That is site-owner data, so: needs-on-site-check. The keyword-repetition pattern itself is real, and Medium (optimisation opportunity) is proportionate.

### Title tags are too long and inconsistently templated: 76/98 are over 60 chars, up to 204, with four different site-name suffixes

`title-template-length` · On-Page SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Median SERP title is 65 chars; 76/98 exceed 60 and 42 exceed about 80. Worst cases: Compostelle 65L 204 chars, Compostelle 25L/35L 182, the post /cest-une-veritable-revolution… 154, Helsinki 136 ('Sac à dos GRAVIPACK exosquelette 60+10 L : soulage le dos et les épaules, répartit la charge. Recommandé pour randonnée et port prolongé'), /test/ 122, Kingston 118, /category/…handicap 116.
Four site-name suffixes coexist:
- ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant' (73 chars)
- ' - Sac à dos exosquelette anti-mal de dos'
- ' - Le sac à dos exosquelette GRAVIPACK anti mal au dos'
- ' - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos.'
Default archive patterns remain ('Innovation Archives - …', 'Archives des Poches frontales - …'). Five titles are under 30 chars ('Boutique Gravipack' ×3, 'Contactez Gravipack', 'Nos engagements'). Five URLs returned two different titles across queries (Easy Travel, Sherpa orange, Rome, Light Promax, nos-engagements, which also showed as 'GraviPack®'), a sign of rewriting.

<https://www.gravipack.com/produit/sac-anti-mal-de-dos-de-survie-65-litres-ergonomique-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme-copie/> · <https://www.gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-helsinki-gravipack-60l-10l-70l/> · <https://www.gravipack.com/cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/> · <https://www.gravipack.com/categorie/innovation/> · <https://gravipack.com/categorie/outillage/> · <https://gravipack.com/contacts/> · <https://www.gravipack.com/category/gravipack-engage-dans-le-handicap-et-l-inclusion/> · <https://gravipack.com/boutique-gravipack/> · <https://gravipack.com/nos-engagements/> · <https://www.gravipack.com/attribut-produit/accessoires/poches-frontales/>

**Why it matters.** quality-gates.md requires 30-60 characters, the primary keyword near the beginning, the brand at the end and a unique title per page. Titles over 60 chars get truncated in Google, so the model name or brand disappears. Google also rewrites titles it finds too long, boilerplate-heavy or keyword-stuffed, and the double titles seen per URL show that is already happening. A 73-char tagline suffix repeats 'exosquelette anti-mal de dos' on every page, which adds to the stuffing and cannibalisation.

**SEO effect.** Lower CTR from truncated or rewritten titles. Weaker relevance because the useful words (model, capacity, use) are pushed past the cut-off. Sitewide keyword repetition adds to the cannibalisation. Thin titles like 'Boutique Gravipack' waste the shop page's ranking potential for 'boutique sac à dos exosquelette'.

**How to fix.** 1) Yoast → Réglages → Apparence du site: set Site name = 'Gravipack' (not the long tagline), separator '|'. Tagline can stay in Réglages → Général but must not be in title templates.
2) Templates:
- Products: %%title%% %%sep%% %%sitename%%
- Product categories: %%term_title%% %%page%% %%sep%% %%sitename%%
- Posts: %%title%% %%sep%% %%sitename%%
- Blog categories: %%term_title%% – Actualités %%page%% %%sep%% %%sitename%%
Remove 'Archives'. With Rank Math, use the equivalent %title% %sep% %sitename%.
3) Write a custom SEO title for every product and category (≤60 chars, model first, brand last). Examples:
- 'Compostelle 65L – Sac de trek ergonomique | Gravipack' (53)
- 'Sac outillage Light Promax à exosquelette | Gravipack' (53)
- 'Claie de portage Cargo Max à exosquelette | Gravipack' (53)
- Shop: 'Boutique sacs à dos à exosquelette | Gravipack' (46)
- Contact: 'Contact et devis entreprise | Gravipack' (39)
- Engagements: 'Nos engagements : santé, dos, inclusion | Gravipack' (51).
4) Fix the long editorial titles. H1s can stay expressive, but the <title> must be under 60.
5) Bulk-edit with Yoast's or Rank Math's bulk editor, or export/import via WP All Import. Re-crawl with Screaming Frog (Page Titles > Over 60 characters / Duplicate) until zero.

**Verifier notes.** Recomputed: 76/98 titles over 60 characters, median 65, and 5 under 30. These are titles as shown by a non-Google engine.
- One counted title ends in '...' (the RATP post), so it was truncated in display and its length is a lower bound.
- The 182-204 character titles are almost certainly the raw <title> including the long site-name suffix. Engines do not lengthen titles, so the bloated-suffix template is well supported.
- The 'four suffixes' may partly reflect crawl snapshots from different dates, not four live templates. Several appear only on URLs with otherwise stale signals (parameter URLs, /contacts/, Précommande).
- 'Titles differ per URL across queries, so Google is rewriting' is unsupported. This engine is not Google, and query-dependent title display is the engine's own behaviour.
- Notes E4 show a different home title in another snapshot ('Le sac bureautique ou randonnée révolutionnaire...'), so the WHAT_WORKS home-title claim also rests on one snapshot.
Per claude-seo, title length mainly affects CTR, not ranking eligibility, so Medium is proportionate rather than High.

### Thin taxonomy archives are indexed: product attributes, product tags, two blog category bases and paginated shop pages

`thin-taxonomy-archives-indexed` · Technical SEO · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Indexed:
- /attribut-produit/accessoires/exosquelette-gravipack/ and /attribut-produit/accessoires/poches-frontales/ (WooCommerce attribute archives)
- /etiquette-produit/precommande/ (product tag)
- /categorie-produit/accessoires-sac-a-dos/ titled '… Archives'
- blog categories /categorie/innovation/, /categorie/technologie/, /categorie/militaire/, /categorie/outillage/ AND a second base /category/gravipack-engage-dans-le-handicap-et-l-inclusion/
- /boutique-gravipack/page/2/ and /categorie-produit/tous-les-sacs-a-dos-exosquelette/page/2/ (page 2 titled differently from page 1).
Search summaries show the Innovation and Militaire archives listing the same few posts (SOFINS, Techterre, VivaTech).

<https://www.gravipack.com/attribut-produit/accessoires/exosquelette-gravipack/> · <https://www.gravipack.com/attribut-produit/accessoires/poches-frontales/> · <https://www.gravipack.com/etiquette-produit/precommande/> · <https://www.gravipack.com/category/gravipack-engage-dans-le-handicap-et-l-inclusion/> · <https://www.gravipack.com/categorie/militaire/> · <https://www.gravipack.com/categorie/innovation/> · <https://www.gravipack.com/boutique-gravipack/page/2/> · <https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/page/2/>

**Why it matters.** seo-technical lists index bloat and thin content under Indexability. Attribute and tag archives on a catalogue of about 80 products add near-empty listing pages that duplicate the categories. Two category bases (/categorie/ and /category/) show the permalink setting was changed without redirects.

**SEO effect.** Low-value URLs dilute the site's overall quality signals and soak up crawl. They can also outrank or cannibalise real categories (e.g. the 'Précommande' tag title carries 'anti-mal de dos'). Old /category/ URLs that resolve may be duplicates of /categorie/.

**How to fix.** 1) Yoast → Réglages → Taxonomies: set 'Afficher dans les résultats de recherche' = Non for product tags (etiquette-produit) and every product attribute (pa_*). For blog categories, keep them indexable only if each gets a unique 150-300 word intro; otherwise noindex.
2) Pick one blog category base (Réglages → Permaliens → Préfixe des catégories = 'categorie') and 301 /category/(.*) → /categorie/$1. Merge the 'Actualité Handicap' category into /categorie/handicap-inclusion/.
3) Pagination: keep /page/2/ indexable with a self-referencing canonical (Google no longer uses rel=prev/next). Make the title '… – Page 2 | Gravipack', make sure page-2 links are plain <a href>, and do not canonicalise page 2 to page 1.
4) Remove product attribute archive links from the front end, or make them non-public (Produits → Attributs → uncheck 'Activer les archives').
5) Make sure the XML sitemap excludes noindexed taxonomies (Yoast does this automatically).

**Verifier notes.** The inventory confirms the attribute archives, the 'precommande' tag, the blog categories and the /category/ second base. However:
(1) Calling them 'thin' requires on-page word and product counts, which are not available. The 'Innovation and Militaire list the same posts' claim comes from a search summary not in the saved notes.
(2) The finding lists paginated /page/2/ URLs as a problem, but its own fix (correctly, per claude-seo) says to keep page 2 indexable with a self-canonical. Remove pagination from the finding.
(3) /category/... may be a stale entry rather than a live second base.
About 8 low-value URLs on a site of about 100 is Low priority, not Medium.

### Duplicate CMS pages are indexed: a /test/ copy of a post, two contact pages, a '-2' news slug and two RATP posts

`duplicate-cms-test-pages` · Technical SEO · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** - /test/ is indexed with the same title as /gravipack-soulage-les-forces-speciales-au-sofins/ (search summary: 'appears to be a draft copy of the SOFINS article').
- Two contact pages: www /contact-gravipack/ ('Contactez Gravipack') and apex /contacts/ ('Contacts - Le sac à dos exosquelette GRAVIPACK anti mal au dos').
- The news index slug /actualites-gravipack-2/ implies a sibling 'actualites-gravipack' page or trash item, and /articles/ is a second listing.
- Two posts on the RATP story: /gravipack-au-salon-vivatech-cet-outil-de-pointe-…-le-parisien/ and /le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/.
- Two 'about' pages: /nos-engagements/ and /a-propos-de-nous-gravipack-au-service-de-votre-dos/.

<https://www.gravipack.com/test/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/contact-gravipack/> · <https://gravipack.com/contacts/> · <https://www.gravipack.com/actualites-gravipack-2/> · <https://www.gravipack.com/articles/> · <https://gravipack.com/gravipack-au-salon-vivatech-cet-outil-de-pointe-au-service-des-voyageurs-et-des-agents-du-metro-le-parisien/> · <https://gravipack.com/le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/>

**Why it matters.** Test and draft pages in the index look unprofessional and duplicate real content. Duplicate contact and about pages split the trust signals Google looks for when assessing a merchant (who you are, how to reach you).

**SEO effect.** Duplicate-content clustering means Google may show /test/ instead of the real post. Link equity to contact and about pages is split. Same-topic posts cannibalise news queries like 'Gravipack RATP'.

**How to fix.** 1) 301 /test/ → /gravipack-soulage-les-forces-speciales-au-sofins/, then delete the test post and empty the trash.
2) Keep one contact page (recommend /contact/ on the canonical host). 301 /contacts/ and /contact-gravipack/ to it and update menu links.
3) Rename /actualites-gravipack-2/ to /actualites/ (check Pages → Corbeille for the original 'actualites-gravipack' and delete it first). Decide whether /articles/ or /actualites/ is the blog index, and 301 the other.
4) Merge the two RATP posts into one complete article (Le Parisien quote, 250 agents equipped, VivaTech). 301 the weaker one.
5) Merge /nos-engagements/ into the about page, or give it a distinct purpose (CSR/handicap) and a distinct title.

**Verifier notes.** /test/ is in the inventory with the SOFINS title plus the old long suffix. It is a real hygiene issue if it still returns 200, but the old suffix suggests an old snapshot.
- /contacts/ also carries the old 'GRAVIPACK anti mal au dos' suffix and may be stale.
- '-2' in /actualites-gravipack-2/ only shows there was a slug collision when the page was created. It does not prove a sibling page still exists.
- The two RATP posts (VivaTech/Le Parisien vs RATP agents) and /nos-engagements/ vs /a-propos-.../ can be legitimately distinct pieces. Calling them duplicates is speculative without the page content.
Low priority, and the HTTP status of each URL needs checking.

### Product slugs are very long, sentence-like, keyword-stuffed and sometimes wrong (30/39 product URLs over 100 chars)

`slug-quality` · On-Page SEO · auditor severity **Medium** → verifier **confirmed**, severity **Low**

**Evidence.** 30/39 product URLs exceed 100 chars (median 110). Longest:
- City, 205: /produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/ ('anti-mal-de-dos' twice, superlatives).
- Compostelle 80L, 196: …-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/.
Slugs without the model name: Tokyo (/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/) and Light Promax (…-outillage-parcours-gravipack/).
Slug/content mismatches:
- /fourreau-de-portage-exosquelette-gravitech-… is titled 'Claie de portage…' and named 'Barracuda'.
- /sac-a-dos-hiking-30l-gris… is a 33 L bag.
- Pearl slug says 'de-voyage' while its title says 'randonner'.
Spelling errors: 'sac-randonner-leger' (Easy Travel, Helsinki), 'oganizer', 'autresvos' (/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/), presta 'hikking33', category 'militaire-tactique-assault'.
Repetition: Sherpa orange '…-orange-anti-mal-de-dos-orange-…'.

<https://www.gravipack.com/produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/> · <https://www.gravipack.com/produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/> · <https://gravipack.com/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/> · <https://gravipack.com/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://www.gravipack.com/produit/porte-outils-elastique-amovible-velcro-oganizer-gravipack/>

**Why it matters.** seo-technical flags URLs over 100 chars, and seo-page asks for short, descriptive slugs. Words in the URL are a small relevance signal, but over-long slugs are truncated in SERP breadcrumbs, look spammy when shared, and repeat the cannibalising head term. Slugs that contradict the page (30l vs 33 L, fourreau vs claie) make the page less clear to users and to Google.

**SEO effect.** Minor relevance and CTR effect (SERP breadcrumb or URL display). It adds to the keyword-stuffing pattern across the site. Wrong model names in slugs weaken matching for model queries ('Gravipack Tokyo', 'Light Promax').

**How to fix.** Treat this as low-risk, staged work, because every slug change needs a 301:
1) Use this pattern for new products: /produit/<modele>-<contenance>[-<couleur>]/, e.g. /produit/sherpa-45l-orange/, /produit/city-20l/, /produit/tokyo-30l/, /produit/compostelle-80l/, /produit/claie-barracuda/.
2) Rewrite only the worst slugs first (City, Compostelle 80L, Tokyo, Light Promax 'parcours', fourreau→claie, hiking-30l→hiking-33l, 'autresvos'). Add a 301 from each old slug. WordPress auto-adds 'old slug' redirects for posts but not reliably for products, so use the Redirection plugin.
3) Update internal links and the sitemap, and check there are no redirect chains (old presta → old slug → new slug must become old presta → new slug).
4) Fix spelling in new slugs ('organizer', 'assaut', 'randonnee').
5) Do not change slugs of URLs that earn backlinks unless the 301 is in place the same day.

**Verifier notes.** The URLs themselves are the evidence. Recomputed: 30/39 product URLs exceed 100 characters, with a median of 110. That meets claude-seo's URL >100 characters flag.
The spelling errors are visible in the URLs: 'randonner' (Easy Travel, Helsinki), 'oganizer', 'autresvos', 'hikking33', 'assault'.
The content mismatches ('30l' vs a 33 L bag; 'Barracuda') come from page snippets and need a live check.
URL words are a minor signal and every slug change carries 301 risk, so Low (backlog) is more proportionate than Medium. The fix's staged, redirect-first approach is sound.

### Titles have spelling errors and many product titles omit the model name

`title-typos-missing-model` · On-Page SEO · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Typos in SERP titles:
- 'Sac randonner léger…' (Pearl; alt title of Sherpa orange), where 'randonner' is a verb and should be 'randonnée'.
- 'militaire d'assault' (should be 'd'assaut').
- 'allege' without the accent (urbain category).
- 'Sac a dos' without the accent (Dublin, shop filter, Précommande tag, presta).
- 'ce sac à dos allègent' (grammar, presta home).
- 'fabrication professionnelle…' starts lowercase.
- Brand casing varies: 'gravipack' lowercase (Rome), 'GRAVIPACK', 'GraviPack®', 'Gravipack®'.
Product titles without a model name:
- Oslo Rouge: 'Sac ergonomique de randonnée anti-mal de dos avec exosquelette'
- Centurion: 'Sac à dos ergonomique anti-mal de dos avec exosquelette Gravipack'
- ToolMaster: 'Sac outillage anti-mal de dos exosquelette'
- Business Talk V4 25L ×2: 'Sac à dos exosquelette 25L anti-mal de dos pour deux ordinateurs' / 'Sac à dos ordinateur 25L anti-mal de dos révolutionnaire'
- Gravitech/Barracuda: 'Claie de portage révolutionnaire exosquelette anti-mal de dos'
- Light Promax (2 URLs): 'Sac à dos outillage anti-douleur exosquelette Gravipack®'.

<https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-militaire-tactique-assault-anti-mal-de-dos/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-toolmaster-orange-gravipack/> · <https://gravipack.com/produit/fabrication-professionnelle-gravipack/> · <https://gravipack.com/produit/sac-a-dos-exosquelette-professionnel-et-velo-rome-gravipack-anti-mal-de-dos/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-urbain/>

**Why it matters.** French users notice spelling errors, which cut trust and CTR, and they reinforce the 'arnaque?' scepticism already visible on forums. Without the model name, the product page cannot match navigational model queries ('Gravipack Oslo', 'Centurion Gravipack') and looks identical to its siblings in the SERP.

**SEO effect.** Lost long-tail and model-query rankings. Google is more likely to rewrite these titles. More cannibalisation, because generic titles compete with each other.

**How to fix.** 1) Proofread every title and H1. Use 'randonnée' (noun), 'assaut', 'allège', 'Sac à dos', and one brand spelling: 'Gravipack' in titles, keeping ® only in body copy.
2) Put the model and capacity first in every product title, e.g. 'Oslo 60+10L rouge – Sac de trek à exosquelette | Gravipack', 'Centurion – Sac à dos ergonomique à exosquelette | Gravipack', 'ToolMaster orange – Sac outillage à exosquelette | Gravipack', 'Business Talk V4 25L – Sac 2 ordinateurs | Gravipack'.
3) Install a French spell-checker (LanguageTool browser extension) for whoever edits products.
4) Export all titles to a sheet and run a uniqueness and spelling pass before re-import.

**Verifier notes.** These appear verbatim in the saved inventory titles:
- 'Sac randonner léger ... Pearl'
- 'militaire d'assault'
- 'allege' (urbain category)
- 'Sac a dos' (Dublin, shop filter, Précommande tag, presta)
- 'allègent' (presta home)
- lowercase 'fabrication professionnelle' and 'gravipack' (Rome)
- missing model names: Oslo Rouge, Centurion, ToolMaster, both Business Talk V4 25L, Gravitech
Search engines do not introduce typos, so these existed in the source <title> at crawl time. They may since have been fixed, so confidence is 'likely', not 'confirmed'.
The claim that Sherpa orange had an alternate 'Sac randonner' title is not in the saved inventory, which shows 'Sac anti mal de dos exosquelette de montagne Sherpa orange'. Treat that part as unverified.

### gravipack.fr, the audited URL, has zero indexed pages, and the brand lives on gravipack.com

`gravipack-fr-domain-setup` · International / Domains · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** site:gravipack.fr, "gravipack.fr", "www.gravipack.fr" and "gravipack.fr" sac à dos returned no URL on gravipack.fr or www.gravipack.fr. Every official result was on gravipack.com. Third parties name gravipack.com as the website (LinkedIn company page, Les Pépites Tech, Trustpilot profile 'review/gravipack.com'). The legal notice on gravipack.com/mentions-legales/ describes the gravipack.com site. Whether gravipack.fr resolves, redirects, or is parked could not be checked (the domain is blocked in this sandbox).

<https://lespepitestech.com/startup-de-la-french-tech/gravipack> · <https://fr.linkedin.com/company/gravipack> · <https://fr.trustpilot.com/review/gravipack.com> · <https://gravipack.com/mentions-legales/> · <https://gravipack.com/>

**Why it matters.** seo-hreflang's geo-signal heuristic ranks a ccTLD as the strongest locale signal. For a France-first brand, .fr would be a natural asset, but splitting content across .fr and .com would divide authority. Right now all equity is on .com, which is fine, provided gravipack.fr (if owned) redirects page-to-page to .com. If it is parked, serving a duplicate, or not owned, brand type-in traffic and any legacy links are lost, or a third party could squat it.

**SEO effect.** With a correct 301, any links to gravipack.fr are consolidated and brand searches stay unified. Without one, legacy links and type-in visitors are lost and the brand looks inconsistent. Consumers and press who guess '.fr' can land on a dead page.

**How to fix.** 1) Confirm ownership of gravipack.fr and www.gravipack.fr at AFNIC/registrar (Gandi). Renew both for multiple years.
2) Configure a host-level 301 that preserves the path: https://gravipack.fr/* and https://www.gravipack.fr/* → https://gravipack.com/$1. Gandi web forwarding or Apache:
RewriteCond %{HTTP_HOST} ^(www\.)?gravipack\.fr$ [NC]
RewriteRule ^(.*)$ https://gravipack.com/$1 [R=301,L]
The .fr host needs a valid TLS certificate so the https:// form redirects without a browser warning.
3) Do not add hreflang between .fr and .com. Both would be fr-FR, and hreflang is for distinct language/region versions only.
4) Add gravipack.fr to the Search Console Domain property list. If .fr ever had content, use the Change of Address tool.
5) Use gravipack.com consistently in every profile (Google Business Profile, Decathlon brand page, KissKissBankBank, YouTube, press kit).

**Verifier notes.** site:gravipack.fr returning nothing matches the earlier findings, and the saved backlink report also logs 'gravipack-fr-no-link-profile'. Third parties (Trustpilot es 'review/gravipack.com', LinkedIn, Les Pépites Tech) point to .com.
Zero indexed pages on .fr is exactly what a correct 301 to .com produces, so the observation is not a problem in itself. It is only a problem if .fr is parked, lapsed, or serves duplicate content, and none of that can be checked here.
Frame it as Low (brand protection and type-in traffic), conditional on the redirect check. Keep the key context for the user: the audited URL (http://gravipack.fr/) is not where the brand's indexed site lives.

### Utility and service items are indexed as products (payment link, 'fabrication professionnelle', buckle in 'Services')

`utility-pages-indexed-as-products` · E-commerce · auditor severity **Low** → verifier **confirmed**, severity **Low**

**Evidence.** Indexed as products:
- /produit/lien-de-paiement-unique-pour-votre-commande-personnalisee-gravipack/ ('Lien de paiement pour votre commande personnalisée Gravipack®'). It surfaced for queries about CGV, remboursement and testimonials.
- /produit/fabrication-professionnelle-gravipack/ (title starts lowercase: 'fabrication professionnelle, cadeaux d'entreprise et objets publicitaires haut de gamme.').
- /produit/boucle-de-sangle-abdominale-pour-sac-a-dos-exosquelette-gravipack/, assigned to a 'Services Gravipack®' category per the summary.

<https://www.gravipack.com/produit/lien-de-paiement-unique-pour-votre-commande-personnalisee-gravipack/> · <https://gravipack.com/produit/fabrication-professionnelle-gravipack/> · <https://gravipack.com/produit/boucle-de-sangle-abdominale-pour-sac-a-dos-exosquelette-gravipack/>

**Why it matters.** A payment-link product is a transactional utility and has no search value. Indexing it adds thin pages, and it can show for brand+payment queries, which looks odd. A B2B manufacturing service sold as a 'product' should be a proper landing page if it is a real offer.

**SEO effect.** Thin-page index bloat. Missed opportunity for a real B2B page ('sac à dos personnalisé entreprise', 'cadeau d'entreprise ergonomique').

**How to fix.** 1) For the payment link: Produit → Visibilité du catalogue = 'Caché', and in the Yoast box set 'Autoriser les moteurs de recherche à afficher ce produit' = Non. It is then also removed from the sitemap.
2) Rebuild 'fabrication professionnelle' as a page (/entreprises/sac-a-dos-personnalise/) with 600+ words (quality-gates Landing Page), MOQ, delivery times, logos, quote form, and a title like 'Sacs à dos personnalisés pour entreprises | Gravipack'. 301 the product URL to it.
3) Keep spare parts such as the buckle as accessories in the 'Accessoires' category, not 'Services'.

**Verifier notes.** The payment-link product and 'fabrication professionnelle' are in the inventory as /produit/ URLs, so presence in this engine's index is confirmed. Presence in Google needs GSC.
The buckle (boucle de sangle abdominale) is a real spare part. Indexing it is normal; only its 'Services' category assignment (from a summary, not in the saved notes) would be odd, so drop it from the 'utility page' list.
Low is proportionate.

### Prices, specs and pre-order dates differ across indexed pages and snippets (stale 'juin 2026' and 'août' pre-orders)

`price-availability-inconsistency` · E-commerce · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Search snippets show different prices for the same model across gravipack.com pages:
- Pearl 99,90 / 119,00 / 149,00 / 89 €
- Oslo Rouge 289,00 / 239,92 / 149,90 €
- Austerlitz 79,90 / 89,90 / 129,00 / 149,90 €
- Hiking Terracotta 89,00 / 89,90 / 129,00 €
- Business Talk V4 149 / 129 €
- Rome 119,90 / 94,90 €
- Sherpa 99,00 / 149,00 / 149,90 € (presta 249 €).
Specs: Hiking 'Gris' URL says 30L while the page says 33 L; Rome 1,6 kg vs 1,9 kg; Oslo '60+10L' vs '70L'.
Business Talk V4 20L snippet: 'précommande … disponibilité prévue en juin 2026'. 25L: 'Prévente – Offre Early Bird : livraison garantie en août'. As of 12 Oct 2026 both are past. Some differences may be snapshot timing (sales).

<https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://www.gravipack.com/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/> · <https://gravipack.com/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/> · <https://gravipack.com/produit/sac-a-dos-exosquelette-professionnel-et-velo-rome-gravipack-anti-mal-de-dos/>

**Why it matters.** Google Merchant listings and Product rich results need the price in structured data to match the visible price. Mismatches can cause item disapprovals or removal of the price from snippets. Expired pre-order promises in snippets hurt trust and CTR, and conflicting weights or capacities undermine the main product claim (lightness).

**SEO effect.** Possible loss of price and availability rich-result enhancements and free Shopping listings. Lower CTR and higher bounce when the SERP price differs from the page price. Trust signals (Helpful Content) are weakened.

**How to fix.** 1) Remove duplicate SKUs first (see duplicate-product finding) so each model has one price.
2) For sales, use WooCommerce scheduled sale prices ('Programmer'), so the Product schema shows price plus priceValidUntil and the regular price is restored automatically.
3) Update or remove the Business Talk V4 pre-order text. Set the stock status to 'En stock' or 'En réapprovisionnement' and make sure Offer.availability in the JSON-LD matches (InStock / PreOrder / BackOrder).
4) Standardise specs in WooCommerce attributes (Contenance, Poids, Dimensions) so the same value feeds the page, schema and feed.
5) In Search Console → Merchant listings / Product snippets, fix 'price mismatch' warnings. In Merchant Center, turn on automatic item updates.
6) Request reindexing of the top 20 products after the fixes.

**Verifier notes.** The price spreads come from snippets captured at different crawl dates. The saved Decathlon notes show a dated promotion (149,90 € instead of 249 €, 18 June to 30 Aug 2026), which shows prices really moved over time. Most of the spread is therefore likely to be timing and sales, not live inconsistency. The finding admits this itself.
A Merchant listings or Product snippet 'price mismatch' is only an issue if the Offer.price in the structured data differs from the visible price on the live page, which cannot be checked here.
The expired pre-order texts ('juin 2026', 'août') matter only if the live pages still show them on 12 Oct 2026, so they also need a live check.
I downgraded it to Low until a live check confirms it.

### The only indexed page about the scientific study is on the legacy presta subdomain

`study-only-on-legacy-subdomain` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** The study summary (Plateforme d'Analyse Physiologique du Mouvement du LBMC, Faculté de Médecine Lyon-Sud) surfaced only at presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack. No study page on gravipack.com appeared in a site:gravipack.com query for 'étude brevet médecin ergonome'. Product pages instead carry claims such as 'recommandé par kinés, ergonomes et médecins du travail' and 'protégé par 13 brevets'. A randonner-leger.org thread (2021) says the FAQ mentions a study section with no link, and that nothing is on PubMed.

<https://presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack> · <https://www.gravipack.com/faq/> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=627454> · <https://www.gravipack.com/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/>

**Why it matters.** The brand's central promise ('jusqu'à 92 % de poids ressenti en moins', 'dispositif médical préventif') is a health-adjacent claim. Without a findable, citable evidence page on the main domain, both Google's quality systems and AI answer engines see unsupported claims, while sceptical forum threads rank for the brand. Redirecting presta without moving this content would delete the only evidence page.

**SEO effect.** Weaker E-E-A-T and trust signals on health-related pages. No page can rank for 'Gravipack étude', so forum scepticism fills that SERP. Low citability in AI Overviews and ChatGPT for 'sac à dos anti mal de dos efficace'.

**How to fix.** 1) Publish /etude-scientifique-lbmc-lyon-sud/ on gravipack.com: who ran it (lab, names, dates), protocol, sample size, measured variables, results with numbers and limits, plus a downloadable PDF. Add an Article/ScholarlyArticle-style JSON-LD with author and datePublished.
2) Explain precisely how the '92 %' figure was measured (perceived load? shoulder pressure?).
3) Link the page from the FAQ, home page, every product ('Voir l'étude'), and the about page.
4) 301 the presta study URL to it.
5) Have it reviewed by a named health professional (kinésithérapeute, ergonome) with a visible bio.

**Verifier notes.** The saved notes support the core claim. For 'gravipack étude Lyon', results were randonner-leger x6, moodle univ-lyon1, maddyness and europe1, with no study page on gravipack.com. The presta study URL is in the inventory, titled 'L'étude scientifique du sac à dos en apesanteur Gravipack.' The '92 %' claim appears in gravipack.com titles (scolaire category, /inventeur-dun-sac-a-dos-en-apesanteur/).
Absence from the SERP is not absence from the site. The FAQ or a product tab may contain the study summary without it being indexed separately. The randonner-leger/PubMed details were not re-verified.
Medium is fair for health-adjacent (YMYL-leaning) trust signals. The moodle univ-lyon1 result may be a citable third-party source worth linking.

### The blog is press/PR only: no guide content for the informational queries that dominate the target SERPs

`informational-content-gap` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** Indexed blog posts are news and PR: SOFINS, VivaTech/RATP ×2, Concours Lépine, Bacary Sagna, propriété industrielle, 'Et si votre sac à dos ne pesait presque plus rien ?', 'Et si tout commençait par un sac trop lourd…'. No guide or how-to URL surfaced. The target generic SERPs are led by guides:
- 'sac randonnée anti mal de dos' → glisshop.com/conseils/regler-son-sac-a-dos-de-randonnee.html, alpinstore.com guide, allodocteurs.fr 'Syndrome du havresac'.
- 'cartable anti mal de dos' → pass-education.fr, maif.fr, 24matins.fr, dhnet.be.
- 'sac à dos exosquelette' → kentfaith.fr blog 'Sac A Dos Exosquelette ?' ranks 1st.

<https://www.gravipack.com/articles/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/letonnante-reconversion-du-footballeur-bacary-sagna/> · <https://www.glisshop.com/conseils/regler-son-sac-a-dos-de-randonnee.html> · <https://www.allodocteurs.fr/bien-etre-psycho-sport-et-sante-syndrome-du-havresac-comment-bien-porter-son-sac-a-dos-4453.html> · <https://www.pass-education.fr/actualites/cartable-trop-lourd-dos-enfant/> · <https://www.kentfaith.fr/blog/article_sac-a-dos-exosquelette_6410>

**Why it matters.** Google reads intent from the SERP. For 'sac randonnée anti mal de dos' and 'cartable anti mal de dos' it shows guides, not product grids, so product and category pages alone cannot rank there. With no guides, Gravipack also cannot win the 'what is a sac à dos exosquelette' definition query it invented, and a generic blog (kentfaith) owns it.

**SEO effect.** Missed top-of-funnel traffic and internal-link sources for categories. Weak topical authority on back-pain and backpack-ergonomics topics, and low AI-Overview citability.

**How to fix.** 1) Create a hub /guides/ with 8-12 articles of 1,500+ words each (quality-gates Blog Post), each linking to one category. Examples:
- 'Sac à dos exosquelette : définition, fonctionnement, pour qui ?' (→ main category)
- 'Comment régler son sac de randonnée pour ne plus avoir mal au dos' (→ hiking category)
- 'Poids du cartable : quelle limite selon l'âge ?' (→ school category)
- 'Sac à dos ordinateur : comment éviter les douleurs aux épaules' (→ business)
- 'TMS et port de charges au travail : solutions' (→ outillage / claie)
- 'Syndrome du havresac : causes et prévention'
2) Each guide needs a named author with credentials, sources, a date, and an honest comparison (including limits of the product).
3) Keep PR posts in a separate /actualites/ section so the two content types do not dilute each other.

**Verifier notes.** The saved notes partly contradict this finding.
(1) A 'site:gravipack.com comment choisir' query surfaced /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/, a how-to guide on the main domain. The host prefix was not recorded in the notes. /evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/ and /le-droit-de-la-propriete-industrielle-explique.../ are also informational. 'Press/PR only' and 'no guide or how-to URL surfaced' are therefore inaccurate.
(2) The intent claim is mixed. For 'sac à dos randonnée anti mal de dos' (extended), the top results include snowleader and Gravipack category pages next to guides (zeoutdoor comparatif, norveya blog). The SERP is mixed-intent, not guide-only.
(3) 'sac à dos exosquelette' does have a kentfaith blog at #1 (E3), which supports the definition-query point.
The gap in guide content is real but smaller than stated.

### Company identity differs across SERP sources (EXOSQUELETTE LIGHT / GRAVIPACK / GRAVIBAG / Kid'abord; Paris / Vincennes / Sens)

`entity-identity-inconsistency` · Brand / Reputation · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** - gravipack.com/mentions-legales/: publisher EXOSQUELETTE LIGHT SAS, Paris.
- Contact pages: 46 rue de la Bienfaisance, 94300 Vincennes.
- societe.com: établissement GRAVIPACK in Sens (89100), SIRET 84054338300029.
- lespepitestech: Sens, also tagged French Tech Aix-Marseille Région Sud.
- myfrenchstartup: raison sociale GRAVIBAG.
- LinkedIn: Vincennes, 201-500 employees, vs about 4-5 on rocketreach/motherbase.
- PagesJaunes: Vincennes, category 'Maroquinerie'.
- journaldugeek.com (2021) and a Decathlon search summary: 'Kid'abord (Loire-Atlantique)' as maker/seller. I could not verify this independently.
- An unrelated 'Gravipack' (groupe-ranque.fr, Vincennes, security storage) shares the name and city.

<https://gravipack.com/mentions-legales/> · <https://gravipack.com/contacts/> · <https://www.societe.com/etablissement/gravipack-84054338300029.html> · <https://lespepitestech.com/startup-de-la-french-tech/gravipack> · <https://www.myfrenchstartup.com/fr/startup-france/243153/gravipack> · <https://fr.linkedin.com/company/gravipack> · <https://www.pagesjaunes.fr/pros/60790927> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://www.decathlon.fr/vc/gravipack> · <https://groupe-ranque.fr/gravipack/>

**Why it matters.** Search engines and LLMs build an entity profile (Organization: legal name, address, founder, sameAs) from consistent signals. Conflicting legal names and addresses make the knowledge panel less likely and less accurate. They also feed the 'is this a scam?' doubts on forums, which matter for a merchant selling health-related products.

**SEO effect.** Weaker Organization entity and trust signals. Possible knowledge-panel confusion with the homonym, and inconsistent local/NAP data.

**How to fix.** 1) Decide the public identity: brand Gravipack, legal entity EXOSQUELETTE LIGHT SAS (or the current one), one head-office address.
2) Put it consistently in mentions légales, CGV, contact page, footer, and Organization JSON-LD on the home page (name 'Gravipack', legalName, address, founder 'Mohammed Errafi', logo, sameAs: LinkedIn, YouTube, Trustpilot, Decathlon brand page, Les Pépites Tech).
3) Correct LinkedIn company size, PagesJaunes category (Maroquinerie → Fabricant de sacs à dos / articles de sport), and myfrenchstartup.
4) If Kid'abord is a distributor, say so on the about page ('Distribué par…') so the relationship is explicit.

**Verifier notes.** The saved notes confirm:
- EXOSQUELETTE LIGHT, Paris, in the mentions légales, with Gandi as host.
- A Vincennes address (motherbase).
- Kid'Abord as the Decathlon marketplace seller of Gravipack.
- Nature & Découvertes listings by Kid'abord with the return address 'SODILOG / RETOUR GRAVIPACK, Colmar'.
So Kid'abord is a distributor/marketplace seller, not a competing identity. That explains the link, and the finding should say so instead of 'could not verify'.
A brand name (Gravipack) that differs from the legal entity (EXOSQUELETTE LIGHT SAS) is normal and not an inconsistency in itself. Address changes over a company's life are also normal.
The societe.com Sens, GRAVIBAG and LinkedIn 201-500 details are not in the saved notes and remain unverified.
Low is proportionate.

### The official site does not lead its own brand SERP in the observed results (crowdfunding, YouTube and a reseller rank above it)

`brand-serp-not-owned` · Brand / Reputation · auditor severity **Low** → verifier **confirmed**, severity **Low**

**Evidence.** For the query 'Gravipack', WebSearch ranked kisskissbankbank.com/en/projects/gravipack 1st, youtube.com/@Gravipack 2nd, equilibre-france-ergonomie.fr 3rd and gravipack.com/ 4th. For 'gravipack avis', no gravipack.com page appears before 7th (Tokyo product). Trustpilot, Fnac reviews and a negative outzer.fr test lead. This engine is not Google.fr, so confirm in GSC or a French SERP.

<https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.youtube.com/@Gravipack> · <https://equilibre-france-ergonomie.fr/les-nouveaux-sacs-gravipack/> · <https://gravipack.com/> · <https://fr.trustpilot.com/review/gravipack.com> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html>

**Why it matters.** Brand queries are the highest-converting traffic. If an old crowdfunding page, a reseller or critical reviews come first, buyers leave the official funnel or meet negative framing first. Host splits and the legacy subdomain make this worse, because they spread the home page's authority.

**SEO effect.** Lost brand clicks to resellers, so lower margin. Reputation risk on '… avis' queries. Weaker sitelinks for the official site.

**How to fix.** 1) Fix host consolidation and presta redirects first (they split brand authority).
2) Add Organization + WebSite JSON-LD on the home page with sameAs links. Use 'Gravipack' as the first word of the home page title.
3) Create /avis-clients/ (or upgrade /gravipackers/) with verified reviews (Trustpilot widget, Avis Vérifiés), answers to common criticisms (fit, rigidity, capacity), and a clear returns process.
4) Ask KissKissBankBank, YouTube channel, resellers and press to link the product names to gravipack.com, and update the YouTube 'about' links.
5) Track the brand SERP monthly.

**Verifier notes.** A separate saved run supports this and is even stronger. The standard query 'gravipack' returned motherbase.ai, neozone, lespepitestech, randonner-leger x2, lematin.ma and maddyness, with no gravipack.com URL at all. 'gravipack avis' returned es.trustpilot and noise, again without gravipack.com.
Results vary between runs, and this US-only engine is not Google.fr, where an indexed official domain usually ranks #1 for its own brand. Confirm in Google.fr or GSC before treating it as more than Low.

### No alternate-language or regional version exists, so hreflang is not applicable

`no-international-version` · International / Domains · auditor severity **Info** → verifier **confirmed**, severity **Info**

**Evidence.** Searches for English pages (site:gravipack.com English backpack exoskeleton 'back pain') and for en./other-TLD hosts returned no Gravipack-owned URL. All indexed pages are French. Meanwhile, international demand signals exist: an English KissKissBankBank campaign ('The weightless backpack'), English press (gearxnews.com, new.in-24.com), Moroccan press (lematin.ma, challenge.ma, fnh.ma), and a Trustpilot ES profile.

<https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.gearxnews.com/2021/09/04/gravipack-this-backpack-has-an-exoskeleton-that-frees-the-shoulders/> · <https://es.trustpilot.com/review/gravipack.com> · <https://lematin.ma/journal/2020/gravipack-permet-gra-bretelles-munies-dinserts-innovants-placer-sac-dos-apesanteur-epaules/329564/amp>

**Why it matters.** Under seo-hreflang there is nothing to validate today. If international sales (EU or Morocco) are a goal, the structure decision (subfolders /en/, /es/ on .com vs ccTLDs) should be made before content is created, so authority is not split again.

**SEO effect.** None today. Possible future upside from English and Spanish demand.

**How to fix.** If expanding: use subfolders on the single canonical host (https://gravipack.com/en/, /es/) with WPML or Polylang. Add self-referencing, bidirectional hreflang (fr-FR, en, es, x-default → /), preferably in the XML sitemap. Do not machine-translate product pages without review. Until then, no action needed.

**Verifier notes.** Nothing in the saved notes shows a non-French Gravipack-owned URL. Per seo-hreflang, when no hreflang exists you report the absence, so Info is correct.
A language switcher or hreflang tags in the HTML could only be confirmed on the live site, so confidence is 'likely'.
gearxnews (EN) is a 2021 translation of the journaldugeek article and a weak demand signal.

### Snippets pull boilerplate (empty-cart widget '0 items - 0,00 €'), which suggests weak or missing meta descriptions

`snippet-boilerplate` · On-Page SEO · auditor severity **Low** → verifier **unverifiable**, severity **Low**

**Evidence.** A search summary of gravipack.com product, legal and CGV results noted that excerpts often show an empty cart ('0 items - 0,00 €'). Presta pages showed the same cart-widget text. Snippet text otherwise varied by query, consistent with engines building snippets from body text rather than a meta description. Actual meta description tags could not be inspected.

<https://gravipack.com/mentions-legales/> · <https://gravipack.com/conditions-generales-de-vente/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://presta.gravipack.com/accueil/15-sac-a-dos-gravipack-business-talk.html>

**Why it matters.** seo-page and quality-gates require a unique 150-160 char meta description per page, written for that page and not templated. When it is missing or ignored, engines pick page text, sometimes navigation or cart boilerplate, which reads poorly in the SERP.

**SEO effect.** Lower CTR on product and category results. Missed chance to show price, delivery and guarantee arguments in the snippet.

**How to fix.** 1) Write unique meta descriptions (150-160 chars) for the home page, all categories and the top 30 products. Avoid opening with the title and avoid a stock CTA. Example (157 chars): 'Sherpa 45L : sac de randonnée à exosquelette breveté, 1,9 kg, housse pluie incluse. Soulage épaules et dos sur les longues marches. Livraison 48 h en France.'
2) Wrap the header mini-cart in a non-indexable element (e.g. render it via AJAX fragments only) or add data-nosnippet to it: <div class='mini-cart' data-nosnippet>.
3) Check templated descriptions with claude-seo's metadata_template.py once the site is reachable.

**Verifier notes.** The saved notes do not record the snippet text, and I could not search again.
Snippets are generated by this non-Google engine. Google rewrites meta descriptions in most cases regardless of their quality. So mini-cart text appearing in snippets does not show that meta descriptions are missing.
The why_it_matters misquotes quality-gates: the gate is 120-160 characters, not 150-160.
Leave this in open questions until the HTML can be inspected.
