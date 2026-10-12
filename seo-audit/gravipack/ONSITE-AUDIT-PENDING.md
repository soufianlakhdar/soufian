# On-site audit — pending (blocked by network policy)

The sandbox could not reach `gravipack.fr` / `gravipack.com`. Allow these hosts (environment → Network access → Allowed domains: `gravipack.fr`, `www.gravipack.fr`, `gravipack.com`, `www.gravipack.com`, plus `presta.gravipack.com`) and run:

```text
/seo audit https://gravipack.com/          # full crawl (≤500 pages) + 17 specialist subagents → final Health Score
/seo technical https://gravipack.com/      # robots.txt, sitemaps, canonicals, redirects, security headers, CWV, JS rendering, IndexNow
/seo hreflang https://gravipack.fr/        # .fr → .com redirect / consolidation check
/seo sitemap https://gravipack.com/sitemap_index.xml
/seo schema https://gravipack.com/         # + one product, one category, the FAQ
/seo page https://gravipack.com/           # home; repeat for top product (Sherpa) and the scolaire category
/seo content https://gravipack.com/faq/    # E-E-A-T on-page, claims wording
/seo images https://gravipack.com/
/seo geo https://gravipack.com/ ; /seo agentic https://gravipack.com/
/seo ecommerce https://gravipack.com/produit/<sherpa-url>/
/seo google pagespeed https://gravipack.com/ ; /seo google crux https://gravipack.com/   # needs a Google API key
/seo drift baseline https://gravipack.com/  # snapshot before fixes
```

Per-finding on-site checks are in each finding's **To verify on-site** line in the full report. Questions raised by the specialists:

## indexation-domains

- [ ] Do http://gravipack.fr, https://gravipack.fr, http://www.gravipack.fr and https://www.gravipack.fr resolve? If they redirect, where to (page-to-page or home), with which status code (301/302), and through how many hops? Is the .fr TLS certificate valid?
- [ ] What does https://www.gravipack.com/<path> return: a 301 to apex, a 200 (duplicate), or a 302? And the reverse? Run 'curl -sI' on /, /faq/, /boutique-gravipack/ and one product on each host.
- [ ] Which host do the canonical tags (rel=canonical) and og:url use on www vs apex pages? Are they absolute and self-referencing? Do any point to the other host?
- [ ] What are the WordPress Address and Site Address settings, and which host do internal links in menus and content use?
- [ ] robots.txt content on gravipack.com, www.gravipack.com and presta.gravipack.com: Sitemap: lines, Disallow for parameters, AI crawler rules.
- [ ] XML sitemap(s): location (sitemap_index.xml / wp-sitemap.xml), host used, whether they include /produit-gravipack/, '-copie', attribute/tag archives, payment-link product, /test/. URL count vs the 83 products the shop reports. Run claude-seo sitemap_discovery.py.
- [ ] Is presta.gravipack.com still live (200) or partially redirected? Is the PrestaShop install still taking orders? Which old URLs have backlinks (Ahrefs/GSC Links)?
- [ ] What produces the /produit-gravipack/ URLs (old product permalink base, custom rewrite, redirect/shortlink plugin)? What status code do they return?
- [ ] Meta robots and canonical on parameter URLs (?add-to-cart=, ?order=, filter_product_cat=) and on paginated /page/2/ URLs. Which filter plugin generates ?order=?
- [ ] Do /actualites-gravipack/ (without -2), /category/ equivalents of the /categorie/ archives, and old slugs return 301, 200 or 404?
- [ ] Actual <title> and meta description tags per page (vs the SERP-rewritten titles observed). Yoast/Rank Math title templates and Site name setting.
- [ ] Google Search Console: Page indexing report (Duplicate without user-selected canonical, Alternate page with proper canonical, Crawled - currently not indexed counts), Performance by query → pages for 'sac à dos anti mal de dos', 'sac à dos exosquelette', 'sac randonnée anti mal de dos', 'cartable anti mal de dos' to confirm cannibalisation on Google.fr (WebSearch is not Google).
- [ ] Product JSON-LD: price, priceValidUntil and availability vs the visible price on duplicate SKUs. Merchant Center/GSC Merchant listings warnings.
- [ ] Is the scientific study (LBMC, Faculté de Médecine Lyon-Sud) published anywhere on gravipack.com, e.g. linked from /faq/?
- [ ] Who is the Decathlon marketplace seller (KID'ABORD?), and what is its relationship to EXOSQUELETTE LIGHT SAS? Needed to write consistent Organization data.
- [ ] Server/CDN setup at Gandi (Apache .htaccess available?) to implement host, .fr and presta redirects at server level.

## keywords-serp-sxo-cluster

- [ ] Google.fr reality check: GSC Performance (queries, pages, positions, impressions) for the 68-keyword universe. The WebSearch tool is US-based and its standard and extended modes disagree, so Google.fr positions must be measured with GSC and a FR rank tracker.
- [ ] Search volume, KD and seasonality per keyword (Keyword Planner / DataForSEO), in particular cartable ergonomique, poids du cartable, sac à dos ergonomique, sac à dos anti mal de dos and sac à dos vélotaf, to finalize the P1/P2/P3 order.
- [ ] For each duplicate group (Business Talk V4 ×3, Light Promax ×3, Kingston ×2, batterie solaire + '-copie', /produit-gravipack/ vs /produit/): are these distinct SKUs or copies? What are the current canonical tags, redirects and GSC indexing statuses?
- [ ] Canonical host (www vs non-www): do both hosts serve 200, or is one 301-redirected? Are WordPress Address and Site Address consistent?
- [ ] Does presta.gravipack.com still return 200, is it noindexed or blocked in robots.txt, and does its checkout still work?
- [ ] Does gravipack.fr 301-redirect to gravipack.com (to which URL, and with which status code)? It could not be tested because the domain is blocked.
- [ ] Current category pages: real title, H1, meta description, copy length, number of products, presence of filters and how faceted URLs are handled (index bloat risk).
- [ ] Internal linking: menu structure, links from the home page to categories, breadcrumbs, related-product blocks, and orphan pages (needs a crawl, e.g. Screaming Frog / seo-firecrawl).
- [ ] Website Relevance Rule checks before creating facets: do women-specific fits, child sizes (primaire) and the Feather school range exist on gravipack.com? Which models are designed for bike use?
- [ ] Content and performance of existing posts (/et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/, /cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/, /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/, /actualites-gravipack-2/, /articles/), to decide whether to merge, 301 or refresh them into the new spokes.
- [ ] Evidence base: the measurement protocol behind '92 %', the 2019 Lyon study document (scope and sample size), any medical-device registration (EU MDR class I, CE marking), and the basis of the 'remboursé par la sécurité sociale' claim. All are needed before the T4 and W2 pages can be published.
- [ ] Review data: on-site review counts and ratings per product, the current fr.trustpilot score and volume, and the Google reviews widget (a search summary reported 4.7 from 1,126 reviews on the home page; verify the source and eligibility for markup).
- [ ] Legal and entity data: the exact relationship between EXOSQUELETTE LIGHT, Gravipack and Kid'Abord, and the official address, so Organization schema and the About page are consistent.
- [ ] Analytics: conversion rate by landing-page type (home, category, PDP, blog) and by channel (own site vs Decathlon), to weight the commercial vs informational investment.
- [ ] Whether the existing YouTube adjustment videos and the settings PDF can be embedded or indexed on the B1 guide.

## backlinks-mentions-pr

- [ ] Does http(s)://gravipack.fr and www.gravipack.fr resolve, and does every URL return a page-to-page 301 to the canonical gravipack.com URL? Or does .fr serve its own or duplicate content?
- [ ] Which host is canonical for .com (gravipack.com or www.gravipack.com)? Do http→https and www↔non-www both 301 in a single hop? Do WordPress Site URL and the Yoast/Rank Math canonicals match?
- [ ] GSC Links report for both gravipack.com and gravipack.fr: top linking sites, top linked pages, anchor texts. Do any linked pages return 404 (e.g. old KKBB-era or pre-WooCommerce URLs) and need 301s?
- [ ] For each URL in the inventory, run verify_backlinks.py (or check manually): does it link, is it follow, nofollow, ugc or sponsored, what is the anchor text, and which host and page does it target?
- [ ] Moz DA/PA/Spam Score, Bing Webmaster inbound links, and Ahrefs Webmaster Tools referring-domain counts for gravipack.com, so a numeric Backlink Health Score can be produced.
- [ ] Does gravipack.com have a /presse/ ('Ils parlent de nous') page linking out to coverage, a downloadable press kit, an /a-propos/ page and an evidence/study page?
- [ ] Does the site's Organization JSON-LD exist, and does its sameAs list Facebook, LinkedIn, YouTube, Trustpilot and others? Which Instagram, TikTok or Pinterest accounts exist, if any?
- [ ] Which legal entity operates gravipack.com (mentions légales, SIREN, registered address: Vincennes, Sens or another)? What are Kid'abord's exact rights (licensee, manufacturer, Decathlon seller)?
- [ ] Can the 2019 Lyon (LBMC) biomechanical study be published, and what exactly is the medical-device and reimbursement status (official references)?
- [ ] What are the exact patent publication numbers (FR/EP/WO) and their status?
- [ ] Is the Trustpilot profile claimed, and are review invitations possible? Are any other review sources (Avis Vérifiés, Google) collected?
- [ ] Do the KKBB project pages, the Les Pépites Tech and MyFrenchStartup profiles, and the licensee websites (Kid'abord, Packcraft, BSGroupe) link to the canonical site?
- [ ] Re-run the 3 searches refused by the budget ('Gravipack PME de France trophée jeune pousse 2020', 'Gravipack Vincennes SIREN', 'Gravipack 2025/2026 nouveauté'), and run google.fr-specific checks of brand and category rankings.

## eeat-ymyl-reputation

- [ ] Does gravipack.com (and gravipack.fr, if live) show LCEN-compliant mentions légales: legal entity name, legal form and share capital, SIREN/RCS, head-office address, phone and email, directeur de la publication, host?
- [ ] Is there an À propos / About page (400+ words) with the founder's bio, team, dated history and photos? Is there a /presse/ page?
- [ ] Exactly where, and in what wording, does the site use 'anti mal de dos', 'anti douleur', 'jusqu'à 92 % de pression en moins', 'remboursé par la Sécurité sociale', 'prescrit par les médecins du travail' and 'testé par l'Armée / la Légion étrangère' (titles, H1s, product descriptions, FAQ, banners, image alt text)?
- [ ] Is the scientific study published on the site (PDF, authors, lab, date, n, protocol, funding, conflicts of interest)? If not, does it exist and can it be published?
- [ ] Does the product carry CE medical-device marking (EU declaration of conformity, EUDAMED registration)? Is there an LPP code? Or is it positioned as a non-medical consumer product?
- [ ] What are the patent numbers (FR/EP/WO), their status (filed or granted) and territories, and are they cited on the site?
- [ ] Do product, blog and guide pages have author bylines, 'reviewed by' boxes with credentials (RPPS/ADELI), publication dates and last-updated dates?
- [ ] What structured data is present: Organization (legalName, founder, identifier, sameAs), Person, Product (offers, brand, hasCertification), Review/AggregateRating, Article with author / reviewedBy?
- [ ] How are on-site product reviews collected (WooCommerce verified owners, Trustpilot widget, other)? How many and how recent? Is the L111-7-2 review-verification notice displayed? Is AggregateRating markup limited to reviews shown on the page?
- [ ] Current Trustpilot rating, review count, date of the latest review and reply rate; whether the profile is claimed and set to French. Does a Google Business Profile exist, and with what rating? Review stars and counts on Decathlon marketplace listings.
- [ ] Are the trust pages present and easy to reach: CGV, returns / refund policy (14-day withdrawal right), warranty, delivery times, SAV contact, privacy policy / RGPD cookie banner, secure payment badges, valid HTTPS on every host?
- [ ] Ownership: is Kid'abord (Loire-Atlantique) the current owner, licensee or distributor of Gravipack? Does the site name the operating company consistently with Infogreffe / Pappers?
- [ ] Does http://gravipack.fr/ 301-redirect to the canonical gravipack.com host? Which host is canonical (www or non-www), and do the canonical tags agree?
- [ ] Is there a Google Merchant Center account, and does it show any misrepresentation or healthcare-policy disapprovals?
- [ ] Search Console: any manual actions? How do the 'mal de dos', 'sac à dos ergonomique' and 'cartable' queries perform, and how did they move around core updates (check with seo_updates.py)?
- [ ] Has the brand ever received a DGCCRF, ARPP or ANSM notice or complaint about its health or reimbursement claims?
- [ ] Is there 2017 army / Foreign Legion test documentation, and written permission to cite the institution?

## geo-ai-visibility-entity

- [ ] Does gravipack.fr (and www.gravipack.fr) resolve, and does it 301 path-for-path to the canonical gravipack.com host? Or does it serve its own content behind noindex or a robots.txt block (which would raise entity-home-fragmented to Critical)?
- [ ] Which host is canonical, gravipack.com or www.gravipack.com? Do non-canonical hosts 301, and do rel=canonical tags point to one host?
- [ ] Is presta.gravipack.com still live? Does it return 200, 301 or 410? Is the old 'étude scientifique' page content still available to move to the main site?
- [ ] robots.txt: report each group separately. Search: OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot. Training: GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended. User-triggered: ChatGPT-User, Claude-User, Perplexity-User. Also note any Content-Signal lines and any 5xx on robots.txt.
- [ ] WAF / Cloudflare: are verified bots challenged? Is there a CAPTCHA on content pages? (Run agentic_check.py --ua-matrix only with the owner's authorization.)
- [ ] Server rendering: are product descriptions, prices, FAQ answers and category intros in the raw HTML (render_page.py --mode auto, agentic_check.py 'server-rendered')?
- [ ] Structured data: is Organization, Brand or Person JSON-LD present, with legalName, founder, logo and sameAs? Does Product markup carry brand, GTIN and offers?
- [ ] /llms.txt and /llms-full.txt: present, well-formed, or a soft 404? (Zero weight; reported for completeness.)
- [ ] /faq/ and category pages: heading hierarchy, question-style H2/H3, answer length, and how near the top the answers sit (citability and structural readability).
- [ ] What exactly does the '92%' figure measure? Do the Lyon / univ-lyon1 study report, sample size, date and authors exist and can they be published?
- [ ] Mentions légales: confirm legal name (EXOSQUELETTE LIGHT?), SIREN, registered address, publication director. Explain the Paris / Vincennes / Aix-Marseille / Kid'Abord / Colmar facts.
- [ ] Is the product a CE-marked medical device or listed on the LPP for social-security reimbursement? (Determines which health claims can stay.)
- [ ] Search Console: brand-query impressions and CTR on google.fr, whether a knowledge panel appears, and the 'Search generative AI' setting (include by default).
- [ ] Bing Webmaster Tools: is the site verified, which sitemaps are submitted, is IndexNow active? (Copilot uses Bing's index.)
- [ ] Does Gravipack have a LinkedIn company page, YouTube channel, Crunchbase profile, Wikidata item or Google Business Profile? Run the dedicated searches in a follow-up message (this turn's search limit was used up).
- [ ] Are 'gravipack sac', 'gravipack exosquelette' and 'sac à dos exosquelette c'est quoi' still unchecked? Re-run them, plus a google.fr check of the brand results (WebSearch is US-located).
- [ ] Lighthouse Agentic Browsing X/N (mobile and desktop) once the PSI quota or an API key is available.
- [ ] Merchant Center: is a Gravipack product feed live, with GTINs matching the Decathlon listings?

## ecommerce-local-competitors

- [ ] Which host is canonical: gravipack.com or www.gravipack.com? Does the other one 301 to it, path-preserving? What does rel=canonical output on /produit/ pages?
- [ ] Does gravipack.fr (apex and www) 301 to the .com store? What status code does it return?
- [ ] Is each colour a separate /produit/ URL (e.g., Sherpa bleu vs Sherpa kaki), or one variable product? What canonicals do colour URLs carry?
- [ ] What Product JSON-LD do product pages output (name, image, offers.price, priceCurrency EUR, availability, sku, gtin13, brand, aggregateRating, shippingDetails, hasMerchantReturnPolicy)? Is it ProductGroup/hasVariant? Is it server-rendered?
- [ ] Are there on-site product reviews? How many per model, what average rating, and is aggregateRating marked up?
- [ ] The actual <title>, meta description and H1 per product. Are the relayed SERP titles Google rewrites or the real on-page titles?
- [ ] Full current catalogue: models, capacities, weights, colourways, prices and GTINs. Are Feather, City Connect, Business Talk and Road Adventure still sold or redirected?
- [ ] Is a Google Merchant Center account active (free listings or Shopping ads)? Any disapprovals for health claims or misrepresentation?
- [ ] Decathlon marketplace: seller name, per-model prices, review counts and ratings, and whether those listings outrank gravipack.com for 'gravipack sherpa 45', 'gravipack hiking 33' and 'gravipack feather'.
- [ ] Presence and prices on Amazon.fr, Cdiscount, Fnac, Rakuten, ManoMano, Alltricks, Galeries Lafayette, pharmacies and orthopaedic or ergonomics shops (not searchable: budget exhausted).
- [ ] Trustpilot: total reviews, TrustScore, reply rate, recency. Is the profile claimed? Any other review platforms (Avis Vérifiés, Google Seller Ratings)?
- [ ] Legal entity details (legal name, SIREN, registered address, phone) on societe.com, Pappers or the RNE. Is 'Kid'abord (Loire-Atlantique)' related, a former name, or a false association?
- [ ] Does the company have premises where staff meet customers (eligible for a Google Business Profile)? Does a GBP or Bing Places listing exist?
- [ ] Are there physical stockists (Decathlon stores, outdoor shops, pharmacies) that would justify a /points-de-vente/ page?
- [ ] Do category pages exist for 'sac à dos anti mal de dos', 'sac de randonnée ergonomique', 'sac à dos ordinateur ergonomique' and 'cartable ergonomique'? How much unique text do they have?
- [ ] Is there a B2B / entreprises page (QVT, CSE, médecine du travail, forces armées), and is the 2017 army / Foreign Legion test documented with permission?
- [ ] Is the scientific study published (methodology, authors, results)? Is the social-security reimbursement claim true (LPPR code / medical-device class)?
- [ ] Which competitors actually rank in French SERPs for the target clusters (needs the competitor queries in the backlog table to be run in a follow-up turn)?
- [ ] Search Console: which URLs get impressions for 'sac à dos anti mal de dos' and 'exosquelette' (to confirm cannibalisation)? Is brand-query traffic split between hosts?
