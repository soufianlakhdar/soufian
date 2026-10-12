# Phase 1 — keywords-serp-sxo-cluster

Searches run: 82

## Evidence base

I ran 82 WebSearch queries on 2026-10-12: about 62 in standard mode and 20 in extended mode. Among them were 7 site: or brand-navigational checks, about 60 non-brand keyword SERPs and about 15 brand or reputation SERPs.

Limits of this evidence:
1. The WebSearch tool is a US-based engine, not Google.fr. The order of results is only indicative, and neither SERP features (PAA, ads, AI Overview, shopping) nor positions could be observed.
2. Standard and extended modes return clearly different result sets. Extended mode is closer to a commercial top 10, so I used it for the head-term verdicts. Overlap scores only compare queries run in the same mode.
3. There is no search volume or difficulty data (no DataForSEO, GSC or Keyword Planner). Priorities therefore rest on SERP page-type evidence plus business fit, and volumes are left blank on purpose.
4. Titles are quoted as shown in search results, and the engine may rewrite them. The home page appeared with two different titles.
5. gravipack.fr never appeared in any result, including a quoted "gravipack.fr" search. The indexed brand site is gravipack.com, on both www and non-www hosts, plus a legacy store at presta.gravipack.com.
6. No page was fetched. Findings about Gravipack pages rely only on the URLs, titles and engine summaries visible in SERPs. Everything else (H1s, copy depth, internal links, canonicals, redirects, schema) is listed as an open question.

On the 'Kid'abord' question: Decathlon lists KID'ABORD as a seller of Gravipack products (for example the Sherpa 45). A Nature & Découvertes Kid'abord seller page gives a return address reading 'SODILOG / RETOUR GRAVIPACK' (Colmar). The legal notice of gravipack.com names EXOSQUELETTE LIGHT (Paris). The link is therefore commercial and probable, but the legal structure is unconfirmed.

## claude-seo commands applied

- /seo cluster plan 'sac à dos anti mal de dos' (seo-cluster SKILL.md + agents/seo-cluster.md; references serp-overlap-methodology.md and hub-spoke-architecture.md). Used the WebSearch fallback because no DataForSEO was available. Applied the overlap thresholds 7-10/4-6/2-3/0-1, the intent classification, the pillar/spoke constraints, the cannibalization check and the internal link matrix rules.
- /seo sxo (seo-sxo SKILL.md + agents/seo-sxo.md; references page-type-taxonomy.md, user-story-framework.md, persona-scoring.md). Covered SERP backwards analysis, SERP consensus per keyword, page-type mismatch severity, user stories and personas. Gravipack target pages were classified from the URLs and titles visible in SERPs only, because render_page.py/parse_html.py could not run (the domain is blocked by network policy).
- /seo plan ecommerce (seo-plan SKILL.md + assets/ecommerce.md). Covered site architecture, page types, schema per page type and a 4-phase roadmap with KPIs.
- /seo content-brief, new-page and improve modes (seo-content-brief SKILL.md; references page-type-templates.md and excluded-domains.md; meta length rules 50-60 / 130-150 characters verified with a script). Produced 3 detailed briefs.
- /seo competitor-pages (seo-competitor-pages SKILL.md). Planned X-vs-Y, technology comparison and roundup opportunities under the fairness and data-accuracy rules.
- Supporting references: seo/references/quality-gates.md conventions (severity definitions) and claude-seo's 'URL unreachable → report, do not guess' rule. All on-page facts that need the live site are listed in open_questions_need_site_access.

## What works

- In extended-mode SERPs, gravipack.com ranks for 10 of the 13 commercial queries tested that contain 'mal de dos' or 'exosquelette'. Examples: home + Pearl + Tokyo for 'sac à dos anti mal de dos'; the hiking category for 'sac à dos randonnée anti mal de dos'; the business category + Business Talk V4 for 'sac à dos ordinateur ergonomique anti mal de dos'; Austerlitz for 'sac à dos tactique anti mal de dos'; Tokyo and Rome for 'sac à dos vélo travail anti mal de dos'.
- The outillage category also appears for the generic transactional query 'sac à dos porte outils', next to ManoMano, DeWalt, Leroy Merlin and Rubix. Gravipack category pages can therefore rank for market head terms when they match the vocabulary.
- A use-case category tree already exists and is indexed: randonnée/trek/Compostelle, scolaire, business/ordinateur, urbain, outillage, médical, claie de portage, accessoires. The recommended architecture is mostly retargeting plus content, not a rebuild.
- PDP titles already combine use, benefit and technology (e.g. 'Sac à dos ordinateur 25L anti-mal de dos révolutionnaire', 'Sac à dos porte outil anti-douleur avec exosquelette'), so there is a clear semantic relevance signal for the 'anti mal de dos' long tail.
- The earned-media footprint ranks for generic queries. journaldugeek.com appears in 7+ SERPs. ici.fr (Concours Lépine) is listed first for 'sac à dos anti mal de dos' (ext). Others: maddyness.com 2024, neozone.org, lematin.ma, challenge.ma, the i-trekkings.net 7-month test, compostelle-autrement.com. These are ready-made link and citation sources.
- Distribution partners extend SERP real estate: decathlon.fr/vc/gravipack and Decathlon PDPs, ergo-corner.com (up to 3 URLs per 'anti mal de dos' SERP), and fnac.com review pages.
- Support-content seeds exist: /faq/ (sizing and custom fitting by height and weight, cabin baggage), /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/, and per search summaries a downloadable settings PDF and a YouTube adjustment video linked from PDPs.
- Positive user reviews exist across platforms to aggregate on an owned evidence page: Trustpilot 5-star reviews about children's back and shoulder relief and good after-sales service, and Fnac praise for the rigid straps.

## Specialist scores

| Category | Score | Rationale |
|---|---|---|
| Non-brand commercial keyword coverage | 35 | In extended mode, gravipack.com appears in 10 of 13 commercial SERPs that contain 'mal de dos' or 'exosquelette', and the outillage category appears for 'sac à dos porte outils'. It is absent for the main market head terms: sac à dos ergonomique, cartable ergonomique, randonnée léger ergonomique, 60+10, vélotaf, tactique militaire, porte-outils ergonomique, voyage, médical, Compostelle. In standard mode no generic SERP contained gravipack.com. |
| Informational keyword coverage | 5 | 0 of 25+ informational SERPs (carrying, adjusting, bag weight, pain, TMS, reimbursement) contain a gravipack.com URL. A brand-specific adjustment guide and an FAQ exist but target no market query. |
| Brand SERP control (navigational + evaluation) | 25 | For 'gravipack' (ext), 5/9 results are owned, but the home page is listed 6th behind KKBB (EN) and YouTube; standard mode shows no owned URL. For 'gravipack avis', 'sherpa avis test', 'arnaque/efficace 92%' and 'étude Lyon', third parties hold about 90-100% of results, mostly skeptical. |
| SXO page-type alignment | 35 | Product and category types exist and align where the query carries the brand's own vocabulary. Missing page types for the SERP consensus: collection for 'sac à dos ergonomique', category for 'cartable', a hub for 'anti mal de dos' (served today by home + PDPs), guides (100% of informational SERPs), comparisons (30-45% of commercial SERPs), an evidence page for brand evaluation, and tools (calculators). Based on SERP-visible page types only. |
| Keyword-to-URL mapping / cannibalization | 30 | Up to 5 Gravipack URLs compete for one query ('sac à dos porte-outils anti mal de dos'); 3-4 URLs (home + PDPs) for 'sac à dos anti mal de dos'; 3 URLs each for Business Talk V4 and Light Promax; 2 for Kingston; a second product base path; mixed hosts; and a legacy presta subdomain still indexed. |
| Topic cluster architecture & internal linking | n/a | Needs a crawl of gravipack.com (blocked) to measure internal links, menu depth, orphans and anchors. SERPs only show that a use-case category tree exists and that no guide hub exists. |
| Search demand sizing (volume / KD) | n/a | No volume or difficulty source (DataForSEO, GSC, Keyword Planner) was available, so priorities are based on SERP evidence and business fit. Validate them with GSC and Keyword Planner before final sequencing, including rentrée seasonality. |
| SXO Gap Score (7-dimension, per page) | n/a | seo-sxo requires fetching and parsing the target page (render_page.py), which the network policy blocks. Only the Page Type dimension could be inferred from SERP-visible URLs and titles, so no full score is computed. |

## Raw findings (with verifier verdicts)

### No dedicated page for the core money keyword 'sac à dos anti mal de dos': home and 3+ PDPs split relevance while a reseller holds 3 slots

`hub-anti-mal-de-dos-split-signals` · On-Page SEO · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Extended SERP for 'sac à dos anti mal de dos':
- Gravipack: gravipack.com/ (home), the Pearl 29 L PDP and the Tokyo PDP.
- ergo-corner.com, a reseller, holds 3 URLs: /55-gravipack, /content/13-le-sac-a-dos-gravipack and blog b14.
- ici.fr is listed first with its Concours Lépine piece.

Related queries:
- 'sac à dos ergonomique mal de dos' returned the home page and the Hiking 30L Gris PDP.
- 'meilleur sac à dos anti mal de dos' returned only the home page, next to the listicles norveya.com and accergo.fr.

These 3 keywords share 4 URLs pairwise, which meets the same-cluster threshold in serp-overlap-methodology.md, so one page should serve them. In standard mode no gravipack.com URL appeared at all; decathlon.fr/vc/gravipack did. No gravipack.com URL seen in any SERP is a category or guide built for this term. The catalogue is titled 'Achetez un sac à dos révolutionnaire avec exosquelette Gravipack' at /tous-les-sacs-a-dos-exosquelette/.

<https://www.ici.fr/emissions/les-nouveaux-inventeurs-du-concours-lepine/gravipack-le-sac-anti-mal-de-dos-8017902> · <https://www.ergo-corner.com/55-gravipack> · <https://www.ergo-corner.com/content/13-le-sac-a-dos-gravipack> · <https://www.ergo-corner.com/blog/gravipack-ou-l-exosquelette-qui-porte-votre-sac-a-dos-b14.html> · <https://gravipack.com/> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/> · <https://norveya.com/blogs/organisation/les-meilleurs-sacs-a-dos-ergonomiques-contre-le-mal-de-dos> · <https://www.accergo.fr/meilleurs-sacs-a-dos-ergonomiques/> · <https://www.decathlon.fr/vc/gravipack>

**Why it matters.** This cluster's SERP is commerce-dominant: 6/9 results are product, category or landing pages, and the 'meilleur' variant adds about 33% listicles. The page type that wins is a hybrid category plus buying-guide hub. A home page is navigational and a PDP covers a single model; per seo-sxo both are the wrong type for broad category intent. This is the brand's own positioning phrase, so losing it to a reseller and a marketplace is a strategic loss.

**SEO effect.** Relevance, links and engagement are split across 4-5 URLs (keyword cannibalization), so no single URL builds enough signal to hold the top 3 against ergo-corner and Decathlon. Google may rotate which URL ranks. The listicle and comparison intent stays unserved, and AI Overviews or answer engines cite resellers and media instead of the brand.

**How to fix.** 1. Create a WordPress page at /sac-a-dos-anti-mal-de-dos/ following brief T9. It combines an answer box, a criteria table, a technology comparison table, four usage sections with the WooCommerce 'Produits par catégorie' block (or 'Produits sélectionnés'), a measured-evidence section, an FAQ and a selector CTA.
2. Make it the only URL optimised for the head term:
   - Home title becomes brand-led: « Gravipack® – sacs à dos à exosquelette breveté | Site officiel ».
   - PDP titles become model + use + capacity, e.g. « Sac à dos de voyage Pearl 29 L à exosquelette | Gravipack », instead of 'Sac randonner léger anti mal de dos…'.
   - Set this in Rank Math/Yoast per product, keeping the focus keyword unique.
3. Link to the hub from:
   - the main menu (label « Sac à dos anti mal de dos »);
   - the home hero;
   - every PDP, through a template block « Pourquoi ce sac soulage le dos »;
   - every category intro.
4. Ask ergo-corner, ici.fr, journaldugeek and maddyness to link to the hub.
5. Schema: WebPage + ItemList of the featured products + BreadcrumbList + Article with an author Person.
6. Track Google.fr positions for the 4 cluster keywords and confirm in GSC (Performance > Pages) that impressions consolidate on the hub within 4-8 weeks.

H1 example: « Sac à dos anti mal de dos : comment choisir celui qui soulage vraiment votre dos ».

**Verifier notes.** I could not re-run any search: the shared WebSearch budget (200 calls per turn) was used up before my first query. I checked this against the auditor's saved SERP data (scratchpad serp-notes.md, overlap.py, tables.md).

What holds:
- The extended list for E1 matches: ici.fr, ergo-corner ×3, Pearl, home, Tokyo, arsayo, oqlf.
- overlap.py gives exactly 4 shared URLs for each pair among K2, K3 and K4.

What is overstated:
- The 4 shared URLs are ergo-corner/55, ergo-corner/13, arsayo and gravipack.com/. These are the most frequent URLs in the whole set: ergo-corner/55 and the home page each appear in 7 of 12 extended SERPs, arsayo in 6.
- Anti-pattern 5 in serp-overlap-methodology says to discount such ubiquitous domains. Without ergo-corner the overlap drops to 2, which means 'interlink', not 'same page'.
- Even at face value, 4 is the bottom of the 4-6 band ('may be separate posts or same post') and falls in the 3-4 tiebreak range. 'One page should serve them' does not follow.
- 'Losing it to a reseller' is overstated. In extended mode 7 of 9 results relate to Gravipack: 3 gravipack.com URLs, 3 ergo-corner URLs that sell Gravipack, and ici.fr about Gravipack.
- Several URLs from one domain in a SERP is host crowding, not proof of cannibalization. That needs GSC (query > pages, position volatility).
- Standard mode showed no gravipack.com URL for the same query, and the tool is US-only (oqlf.gouv.qc.ca appears). Positions are directional, not Google.fr rankings.

The hub and comparison opportunity is real, but per claude-seo definitions it is an optimization opportunity: Medium, not High.

Fix risks:
- Retitling the home page brand-first and removing 'anti mal de dos' from PDP titles before the hub ranks could cost existing positions. WHAT_WORKS itself credits those PDP titles for long-tail relevance. Stage it: publish and link the hub first, de-emphasize the home page later, and keep 'anti mal de dos' as a secondary modifier in PDP titles.
- On a commercial hub, use CollectionPage or WebPage + ItemList + BreadcrumbList rather than Article.

### The biggest generic head term 'sac à dos ergonomique' is won by collection pages; Gravipack has no matching collection and is absent

`no-collection-sac-a-dos-ergonomique` · E-commerce · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Extended SERP for 'sac à dos ergonomique':
- Collections or products whose title equals the query: sacados.fr/collections/sac-a-dos-ergonomique ('Sac à dos ergonomique - SAC À DOS.FR'), mon-sac-a-dos.fr/sac-a-dos-ergonomique, karkoa.com/fr/sac-a-dos-ergonomique, sacroche.fr/collections/sac-a-dos-ergonomique-1, la-sacoche-officielle.com/products/sac-a-dos-ergonomique.
- Listicles: accergo.fr and le-repaire-du-sac-a-dos.fr.
- Also: an arsayo landing page and a ma-boutique-ergonomique guide.

That is 6/9 commerce pages, a strong collection consensus. The standard-mode SERP (osprey, manor, ergobag, deuter Scula, randonner-leger) had no Gravipack either.

Gravipack's closest page is the catalogue category 'Achetez un sac à dos révolutionnaire avec exosquelette Gravipack'. The only gravipack.com URL whose SERP title carries the exact phrase is the legal page /mentions-legales/ ('Le sac à dos ergonomique - Mentions légales…').

<https://sacados.fr/collections/sac-a-dos-ergonomique/> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/> · <https://karkoa.com/fr/sac-a-dos-ergonomique> · <https://sacroche.fr/collections/sac-a-dos-ergonomique-1> · <https://la-sacoche-officielle.com/products/sac-a-dos-ergonomique> · <https://le-repaire-du-sac-a-dos.fr/blogs/tout-savoir-sur-les-sacs-a-dos/les-meilleurs-sac-a-dos-ergonomique-pour-lutter-contre-le-mal-de-dos> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/> · <https://gravipack.com/mentions-legales/>

**Why it matters.** seo-sxo page-type alignment: the SERP expects a category or collection page named after the query. Gravipack sells exactly that (ergonomic backpacks for every use) but names its catalogue after its technology, not the market term. The competitors ranking here are small DTC shops with generic padded bags, so the bar is achievable.

**SEO effect.** Gravipack is invisible for the broadest commercial term in its niche, and the catalogue page cannot rank because its title, H1 and slug do not match. Placing the phrase on a legal page wastes it and can send mixed relevance signals.

**How to fix.** 1. In WooCommerce > Produits > Catégories, rename 'Tous les sacs à dos exosquelette' to 'Sacs à dos ergonomiques' with the slug 'sac-a-dos-ergonomique'. Keep or remove the category base with Rank Math 'Strip category base'. Add a 301 from the old URL (Rank Math > Redirections, or the Redirection plugin) and update the menu.
2. Title « Sac à dos ergonomique : modèles anti mal de dos | Gravipack » (59 chars). H1 « Sacs à dos ergonomiques anti mal de dos ».
3. Put about 120 words of intro above the grid and 600-900 words below it, following brief T10. To output an ACF term field below the loop, use:
add_action('woocommerce_after_shop_loop', function () { if ( is_product_category() ) { $t = get_queried_object(); $h = get_term_meta( $t->term_id, 'seo_bottom_text', true ); if ( $h ) { echo '<section class=cat-guide>' . wp_kses_post( wpautop( $h ) ) . '</section>'; } } }, 20);
4. Add filters (Usage, Volume, Ordinateur, Poids à vide) with WooCommerce attributes and the filter blocks. Set filter-combination URLs to noindex,follow and canonical to the base category.
5. Retitle the legal page « Mentions légales | Gravipack » and set it to noindex,follow.
6. Schema: CollectionPage + ItemList + BreadcrumbList.

**Verifier notes.** Not re-run (search budget exhausted).

What holds:
- The saved E7 set matches: sacados, mon-sac-a-dos, karkoa, sacroche, accergo, le-repaire, la-sacoche, arsayo, ma-boutique-ergonomique, with no Gravipack.
- The saved standard set #1 matches: osprey, manor.ch, ergobag, randonner-leger ×3, alpinstore, with no Gravipack.
- No Gravipack category or collection page targets the term.

Sub-claim refuted by the auditor's own title table: the legal page is NOT the only gravipack.com URL with the exact phrase in its SERP title.
- Centurion PDP: 'Sac à dos ergonomique anti-mal de dos avec exosquelette Gravipack', slug starting /sac-a-dos-ergonomique-.
- Kingston PDP: 'Sac à dos ergonomique ordinateur, business et scolaire…'.
- Dublin: 'Sac a dos ergonomique léger…'.
The 'phrase wasted on a legal page' argument is therefore weaker.

Severity drops to Medium: this is a new-ranking opportunity on a competitive generic term, not a loss of existing rankings.

Fix problems:
(a) 'Tous les sacs à dos exosquelette' is the PARENT product category; its slug is part of every child category URL (/categorie-produit/tous-les-sacs-a-dos-exosquelette/<child>/). Renaming it changes about 12 child URLs too, so effort is not 'Low'.
(b) It removes 'exosquelette' from a URL that currently ranks for 'sac à dos exosquelette' (E3), which conflicts with the exosquelette finding. Safer options: a new top-level 'Sacs à dos ergonomiques' category or landing page, or a title and H1 carrying both terms without changing the slug.
(c) noindex plus a canonical pointing to another URL on filter pages sends conflicting signals; use one.
(d) The Rank Math option for products is 'Remove product category base'. 'Strip category base' applies to post categories.

### No gravipack.com URL appears for any informational back-pain or carrying query tested, while commerce competitors win them with blog guides

`informational-intent-zero-coverage` · Content Quality · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Across 25+ informational SERPs, not one gravipack.com URL appeared. Examples:
- 'comment bien porter son sac à dos' (ext): thenorthface.com, globe-trotting.com, sacprincesse.com/blog, mah-official.fr/blogs, cliniqueinspiration.com, bodyhousekine.fr, nina-sac.com/blogs, la-sacoche-officielle.com/blogs.
- 'poids du cartable enfant recommandé' (ext): matmut.fr, fcpe.asso.fr, dhnet.be, senat.fr, wondermomes.fr, pourquoidocteur.fr, avis-parents.com.
- 'comment régler les bretelles d'un sac à dos': salomon.com ×4, deuter.com, rab.equipment, blog.snowleader.com, tonton-outdoor.com ×2.
- 'poids maximum sac à dos randonnée': ffrandonnee.fr (20 % of body weight), deuter, glisshop, cimalp.
- Also: 'mal au dos sac à dos randonnée que faire', 'sac à dos mal aux épaules solution', 'quel sac à dos quand on a mal au dos', 'sac à dos scoliose enfant', 'sac à dos ou sacoche', 'sac à dos hernie discale', 'sac à dos TMS travail'.

The editorial content visible in site: searches is brand news (/actualites-gravipack-2/, /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/, /cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/) plus a brand-specific how-to (/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/).

<https://www.thenorthface.com/fr-ca/approach/how-to-fit-and-wear-a-backpack-for-all-day-comfort> · <https://www.sacprincesse.com/blog/porter-sac-dos/> · <https://la-sacoche-officielle.com/blogs/la-sacoche-officielle/5-astuces-pour-bien-porter-un-sac-a-dos-sans-avoir-mal-au-dos> · <https://www.matmut.fr/assurance/scolaire/conseils/poids-cartable-enfants-primaire-college> · <https://www.fcpe.asso.fr/actualite/poids-du-cartable-pensez-son-dos> · <https://www.salomon.com/fr-ch/sg/a/how-to-properly-adjust-your-backpack> · <https://www.ffrandonnee.fr/randonner/conseils/preparer-son-sac-a-dos> · <https://www.allodocteurs.fr/actualite-sante-mal-de-dos-des-enfants-a-cause-d-un-sac-trop-lourd-_4170.html> · <https://www.gravipack.com/comment-regler-les-bretelles-exosquelette-de-mon-gravipack/> · <https://www.gravipack.com/actualites-gravipack-2/> · <https://www.gravipack.com/et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/>

**Why it matters.** These are the awareness-stage queries of people with back or shoulder pain, which is exactly Gravipack's audience. The SERPs are 100% guides. Four small bag e-shops rank with blog posts, which shows an e-commerce domain can win them with the right page type. Informational spokes also build topical authority for the commercial hub and supply internal-link equity to categories.

**SEO effect.** There is no top-of-funnel traffic and no remarketing pool. Topical authority on the 'mal de dos / port de charge' entity cluster stays weak, which caps category rankings. Gravipack is also absent from AI Overviews and answer engines, which synthesize exactly these guides.

**How to fix.** 1. Build Hub B /conseils/comment-bien-porter-son-sac-a-dos/ and 8 spokes (B1-B3, R1-R3, E1-E2 in table T7), each 1,200-1,800 words.
2. Give each spoke an answer-first paragraph of 40-60 words, numbered steps, original photos or diagrams, and embedded videos from the existing YouTube channel.
3. Cite primary sources: the FFRandonnée 20 % rule, the 1995 ministerial note on 10 %, the BJSM 2018 systematic review and INRS.
4. Add simple calculators (child's bag weight, hiking pack weight) as a JS block or the 'Calculated Fields Form' plugin. A tool is information gain the ranking guides lack.
5. In WordPress, create a 'Conseils' post category with the /conseils/ base; add Article + Person schema in Rank Math/Yoast, an author box with credentials, and 'Mis à jour le'.
6. Every guide links contextually to its matching category (A1-A4) and to Hub B.
7. Publish the rentrée spokes (E1, E2) by May-June 2027.

Answer box example for E1: « Le poids d'un cartable chargé ne devrait pas dépasser 10 % du poids de l'enfant (note ministérielle de 1995), soit 3 kg pour un enfant de 30 kg. Les pesées de la FCPE montrent des cartables de collégiens souvent au-delà de 17 %. »

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the 12 informational SERPs saved in overlap.py (K13-K24) contain 0 gravipack.com URLs.

Problems with the evidence:
- The list quoted for 'comment bien porter son sac à dos' (ext) (thenorthface, sacprincesse, mah-official, nina-sac, la-sacoche) does not match the saved K13 set (pourquoidocteur, 24matins, consoglobe, cisss PDF, allodocteurs, cssphares, courrierlaval). It must come from an unsaved later run and cannot be cross-checked.
- Most informational SERPs were run in standard mode, which also missed gravipack.com for its own core term.
- These SERPs are full of Quebec, Belgian and Swiss sources (cisss-lanaudiere, cssdgs.gouv.qc.ca, dhnet.be, rtbf, inspq), so they are not Google.fr. Absence there is 'likely', not 'confirmed'.
- 'Absent from AI Overviews' was never tested (WebSearch shows no AIO data) and should be removed from seo_effect.

Severity drops to Medium: a content gap and topical-authority opportunity, not a ranking blocker.

Fix notes:
- The BJSM 2018 systematic review (Yamato et al.) found no convincing evidence that schoolbag weight causes back pain. Content citing it must say so honestly; this is a YMYL accuracy point and partly undercuts 'anti mal de dos' messaging.
- Verify the FCPE '17 %' figure in the example answer box before publishing.

### Brand evaluation queries (avis, test, arnaque, étude, 92 %) are almost entirely third-party and mostly skeptical, with no owned page answering them

`brand-evidence-serp-owned-by-third-parties` · Brand / Reputation · auditor severity **High** → verifier **weakened**, severity **High**

**Evidence.** 'gravipack avis' (ext):
- fr.trustpilot.com/review/gravipack.com: the summary reports complaints about a replacement and refund that never arrived.
- fnac.com review pages: Hiking 33; Road Adventure, with zipper weakness reported.
- outzer.fr Sherpa 45: bought for €240, 'closer to 30 L', uncomfortable, neck pressure.
- Also: lespepitestech, ergo-corner, the i-trekkings Oslo test ('idée de génie ou arnaque ?') and randonner-leger thread 37663 p2.
- The only gravipack.com URL is the Tokyo PDP.

'gravipack sherpa avis test' (std): outzer, 4 randonner-leger threads and es.trustpilot.

'gravipack arnaque efficace 92%' (std): 8 randonner-leger posts plus KKBB. Users report a 10 kg load felt like 11 kg, find nothing on PubMed, EU clinical trials or Open trial, and argue the load moves to the lumbar area.

'gravipack étude faculté médecine Lyon': 6 forum posts plus moodle.univ-lyon1, maddyness and europe1. A forum post says the study was a pre-study with 5 people (unverified).

The same skeptical threads also rank for the generic 'sac à dos qui soulage le dos et les épaules' and 'bretelles ergonomiques sac à dos'.

<https://fr.trustpilot.com/review/gravipack.com> · <https://es.trustpilot.com/review/gravipack.com> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Gris/a16809921/avis> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · <https://www.randonner-leger.org/forum/viewtopic.php?id=37663&p=2> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626080> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=627454> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=570392> · <https://www.kisskissbankbank.com/en/projects/gravipack/tabs/faqs>

**Why it matters.** These are the last queries before purchase, and critics shape the SERP. The product makes health-adjacent claims (YMYL-like), where claude-seo's E-E-A-T framework treats Trust as the most important factor. Without an owned, evidence-based answer, every brand-curious visitor meets doubt first.

**SEO effect.** Branded searches convert less. The negative narrative flows into AI answers: every search summary in this audit labelled the 92 % figure an unverified manufacturer claim. Gravipack has no URL that can rank in the top 3 for its own 'avis' query, and the same threads also hold generic 'soulage les épaules' SERPs.

**How to fix.** 1. Publish /avis-gravipack/ following brief T11:
   - aggregated ratings per platform with links;
   - fair summaries of the i-trekkings and Outzer tests with a measured response (e.g. litre capacity of the Sherpa 45);
   - the full protocol behind the 92 % figure and the 2019 study document, or an honest statement of its scope.
2. Collect verified-owner reviews on PDPs (native WooCommerce reviews with 'verified owner' enabled, plus a post-purchase email via a review plugin). Use Product AggregateRating only from on-site reviews and never on the Organization or home page (self-serving reviews are not eligible).
3. Invite French customers to Trustpilot through its WooCommerce integration so fr.trustpilot reflects current service.
4. Reply transparently once, as the brand, on the main randonner-leger threads, linking to the protocol page.
5. Rewrite claim wording everywhere, including Decathlon titles, from « allège le poids de 92 % » to the measured statement, e.g. « jusqu'à 92 % de pression en moins mesurée sur les trapèzes (protocole) ».
6. Add a site-wide footer link « Avis & preuves » and a link from every PDP.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the saved standard-mode notes (#10, #35, #37, #38) agree. Trustpilot, outzer, randonner-leger ×4-8, KKBB, moodle univ-lyon1, maddyness and europe1 appear, with no gravipack.com page for avis, test, arnaque or étude queries.

Corrections:
(1) 'No owned page answering them' is overstated. The saved title table shows owned pages that address these queries but do not rank for them:
- /gravipackers/ (testimonials);
- /inventeur-dun-sac-a-dos-en-apesanteur/ ('…allège le poids de 92%');
- /gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/;
- a study page on the legacy store, presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack.
The fix should consolidate these into the evidence page (with a 301 from presta), not start from zero.
(2) 'Every search summary labelled the 92 % figure unverified' describes this audit tool's own summarizer, not Google AI Overviews or ChatGPT. Reword to 'third-party sources frequently question the 92 % claim'.
(3) 'Mostly skeptical' is strong. WHAT_WORKS cites positive Trustpilot and Fnac reviews, so 'mixed, with skeptical forum threads prominent' is more accurate.

High is kept because the claims are health-adjacent (YMYL, where Trust weighs most) and these are bottom-of-funnel queries.

### The same models are indexed under several product URLs, two product base paths and two hosts, creating cannibalization inside Gravipack's own SERPs

`product-url-cannibalization-duplicates` · E-commerce · auditor severity **High** → verifier **unverifiable**, severity **High**

**Evidence.** Seen in SERPs:
- Business Talk V4 at 3 URLs: …business-talk-v4-gravipack-20l/, …25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/, …25l…business-talk-v4-ergonomie-eva-memoire-de-forme/.
- Light Promax at 3 URLs: …outillage-light-promax-gravipack-anti-mal-de-dos/, …outillage-parcours-gravipack/ (title 'Sac anti-mal au dos innovant outillage Light Promax de Gravipack'), …porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/.
- Kingston at 2 URLs: …teletravail-kingston…/ and …/vive-la-rentree-scolaire-…-kingston-avec-exosquelette/ (title 'Vive la rentrée scolaire'). Both ranked together for 'sac à dos scolaire anti mal de dos'.
- A solar battery at 2 URLs, one slug ending '-copie'.
- A second product base path /produit-gravipack/ (sac-a-dos-sherpa, sac-a-dos-revolutionnaire = Hiking Terracotta).
- Results mix https://gravipack.com/… and https://www.gravipack.com/… URLs.
- 'sac à dos porte-outils anti mal de dos' returned 5 Gravipack URLs (4 PDPs + the category).

<https://www.gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-25l-anti-mal-de-dos-revolutionnaire-gravipack-business-talk-v4-ergonomie-eva-memoire-de-forme/> · <https://www.gravipack.com/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/> · <https://gravipack.com/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · <https://gravipack.com/produit/vive-la-rentree-scolaire-sac-anti-mal-de-dos-college-gravipack-kingston-avec-exosquelette/> · <https://www.gravipack.com/produit/batterie-solaire-externe-multi-port-avec-lampe-torche-et-boussole-infinity-gravipack-copie/> · <https://gravipack.com/produit-gravipack/sac-a-dos-sherpa> · <https://gravipack.com/produit-gravipack/sac-a-dos-revolutionnaire> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-outillage-toolmaster-orange-gravipack/>

**Why it matters.** The seo-cluster cannibalization rule is that no two pages share the same primary keyword. Duplicate or near-duplicate PDPs split links, reviews and engagement, and they make Google choose a canonical for you.

**SEO effect.** Rankings fluctuate between sibling URLs and none reaches its potential. Crawl budget goes to duplicates, review stars stay fragmented, and GSC is likely to show 'Duplicate without user-selected canonical' or 'Alternate page with proper canonical' at scale (to verify).

**How to fix.** 1. Using site access, confirm for each group whether the URLs are distinct SKUs (e.g. 20 L vs 25 L) or copies.
2. Same model: merge into one WooCommerce variable product (attributes Capacité / Couleur), 301 the others (Rank Math Redirections), move or merge reviews, update internal links.
3. Distinct SKUs: differentiate them, with titles stating capacity and use (e.g. « Business Talk V4 20 L – sac à dos ordinateur 1 PC » vs « … 25 L – 2 ordinateurs ») and a unique focus keyword each.
4. Product base: keep /produit/ and 301 /produit-gravipack/(.*) to the matching /produit/ URL.
5. Host: choose one host, make WordPress Address = Site Address, and add for www:
RewriteCond %{HTTP_HOST} ^gravipack\.com$ [NC]
RewriteRule ^(.*)$ https://www.gravipack.com/$1 [R=301,L]
6. Merge 'Vive la rentrée scolaire' into the Kingston PDP (301), or retitle it « Sac à dos scolaire Kingston 20 L à exosquelette | Gravipack ». Delete the '-copie' product with a 301.
7. Maintain the keyword-to-URL map (T1/T7) as the single source of truth.

**Verifier notes.** Not re-run (search budget exhausted).

The auditor's saved title table corroborates the evidence and makes it stronger. These URL groups show identical SERP titles:
- Sherpa Kaki ×3: /produit/…, /produit-gravipack/sac-a-dos-sherpa-kaki and /produit-gravipack/sac-a-dos-sherpa;
- Hiking Terracotta ×2 (/produit/ vs /produit-gravipack/sac-a-dos-revolutionnaire);
- Light Promax ×2;
- G-Pack ×2;
- Cargo Max claie ×2.
Compostelle also has 25, 35 and 65 L variants, one slug ending '-copie'. Apex and www hosts appear roughly 50/50.

What cannot be seen from SERPs: whether these URLs return 200 or already 301, and whether canonicals exist. Indexes lag behind redirects. The cannibalization consequence therefore needs a crawl plus GSC (Pages report, URL Inspection).

Severity: High is proportionate if the duplicates are 200 and self-canonical; Medium if the alternate paths already redirect. For 'sac à dos porte-outils anti mal de dos', the 5 Gravipack URLs held 5 of 9 slots, so ranking harm there is not shown.

The fix is sound (variable products, 301s, one host). Add http→https to the same rule set, and coordinate with the planned category slug changes to avoid redirect chains.

### Back-to-school demand is missed: the 'cartable ergonomique' SERP is all product and category pages, but Gravipack's school category never uses 'cartable' and its school URLs cannibalize each other

`school-cartable-vocabulary-mismatch` · E-commerce · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** 'cartable ergonomique' (ext) returned 9/9 commerce pages: lespetitsbaroudeurs.com (ergobag Prime and a 'Sac à dos scolaire ergonomique' category), mon-sac-a-dos.fr, mahilana.com, ma-boutique-ergonomique.com ×4, univers-cartable.com. Gravipack was absent.

'sac à dos scolaire anti mal de dos' (ext) returned the Kingston teletravail PDP, the school category ('Sac à dos exosquelette scolaire Gravipack allège le poids de 92%') and the 'Vive la rentrée scolaire' Kingston PDP. The two SERPs share 0 URLs, so they are separate SERP worlds.

No Gravipack URL appeared for 'sac à dos scolaire ergonomique collège', 'sac à dos ergonomique enfant primaire' or 'cartable ergonomique mal de dos enfant'. 'meilleur cartable ergonomique comparatif 2026' returned only listicles (avis-parents ×4, meilleurtest ×3, futura-sciences ×2; ergobag Prime ~98 €, Tann's, Baagl).

Decathlon sells Gravipack Feather and Feather Plus school bags (titles 'Sac à dos scolaire - Feather Plus noir - Allège la charge de 92%', 99 € down from 159 €). The Feather range never appeared on gravipack.com in any SERP. The category slug is …/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/.

<https://www.lespetitsbaroudeurs.com/ergobag-prime-cartable-cp-primaire-sac-a-dos-1053.html> · <https://www.lespetitsbaroudeurs.com/sac-a-dos-scolaire-ergonomique-117> · <https://www.ma-boutique-ergonomique.com/mobilite-ergonomique/cartable-ergonomique/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://www.gravipack.com/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/> · <https://gravipack.com/produit/vive-la-rentree-scolaire-sac-anti-mal-de-dos-college-gravipack-kingston-avec-exosquelette/> · <https://www.avis-parents.com/tests-avis/meilleur-cartable-primaire/> · <https://meilleurtest.fr/comparatif-sac-a-dos-college-lycee/> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-scolaire-feather-plus-noir-allege-la-charge-de-92percent/_/R-p-4a4f8602-5689-4a78-97e9-26fd7d415a2a>

**Why it matters.** The rentrée is the highest-intent seasonal moment for the 'parent' persona. The market's own word ('cartable') leads to a pure category SERP, so the category itself must carry it. Comparison listicles are the second way in and depend on outreach.

**SEO effect.** Gravipack is invisible for the main school term while the Kingston duplicates split the visibility it does have. Parents searching the brand land on Decathlon's Feather pages instead of gravipack.com.

**How to fix.** 1. Retarget the school category:
   - name 'Cartable ergonomique et sac à dos scolaire';
   - title « Cartable ergonomique et sac à dos scolaire | Gravipack » (54 chars);
   - H1 « Cartable ergonomique et sac à dos scolaire anti mal de dos »;
   - slug /cartable-ergonomique/ with a 301 from the old URL.
2. Copy of 600-900 words:
   - choosing by school level (primaire / collège / lycée-étudiant), only for models actually sold;
   - empty weight, volume, laptop sleeve;
   - the two strap sizes mentioned in the brand's content;
   - a link to the bag-weight guide (E1) and calculator.
3. Merge the Kingston duplicates (see the cannibalization finding).
4. If the Feather range is current, list it on gravipack.com with unique copy; otherwise explain the range.
5. Outreach: send samples to avis-parents.com, meilleurtest.fr and futura-sciences for their 2027 comparisons (with disclosure).
6. Publish E1 and E2 by June 2027 and add a seasonal homepage block from mid-June.
7. Schema: CollectionPage + ItemList + BreadcrumbList.

**Verifier notes.** Not re-run (search budget exhausted).

What holds:
- The saved E9 and E5 sets match.
- overlap.py gives K7∩K9 = 0 shared URLs, so these are separate SERPs as claimed.

Weaker or unchecked evidence:
- Absence for 'sac à dos scolaire ergonomique collège' (#22) and 'cartable ergonomique mal de dos enfant' (#6) comes from standard mode only.
- The Feather Plus price (99 € down from 159 €) is not in the saved data and could not be checked.

Missing nuance: the 'cartable ergonomique' SERP is led by primary-school cartables (ergobag Prime 'cartable CP primaire', univers-cartable). Gravipack's school category targets collège, lycée and étudiant (per its slug), and its school PDPs (Kingston, G-Pack 'collège-lycée') are backpacks.
- Retargeting the category to 'cartable' only makes sense if the products suit primary-school children, which needs product data.
- Otherwise 'sac à dos scolaire ergonomique / collège' is the better match.
- G-Pack also has 2 URLs with identical titles, another school cannibalization case.

Severity drops to Medium: a seasonal opportunity, not a ranking blocker.

Fix notes:
- In WooCommerce a child product category cannot live at /cartable-ergonomique/; it would be /categorie-produit/<parent>/cartable-ergonomique/.
- Coordinate with the parent-category rename proposed in another finding to avoid redirect chains.

### Use-case categories rank only when the query contains 'anti mal de dos' and are absent for the market's head terms (randonnée léger, 60+10, vélotaf, tactique, porte-outils ergonomique, voyage, médical, Compostelle)

`categories-target-brand-vocabulary-not-market-terms` · On-Page SEO · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** Present (ext):
- hiking category for 'sac à dos randonnée anti mal de dos';
- Tokyo and Rome for 'sac à dos vélo travail anti mal de dos';
- Austerlitz for 'sac à dos tactique anti mal de dos';
- outillage category for 'sac à dos porte outils' (8th).

Absent:
- 'sac à dos randonnée léger ergonomique': deuter.com ×4, alpinstore ×3, glisshop top 5, rayonrando.
- 'sac à dos randonnée 60+10 litres': deuter, alpinstore, tonton, alltricks, fflose, outzer.
- 'sac à dos vélotaf' (ext): tonton-outdoor, velotafeur ×3, karkoa, gravelrepublic, ratio-bags, guide-velo.
- 'sac à dos tactique militaire ergonomique': military.eu ×7.
- 'sac à dos porte-outils ergonomique artisan', 'sac à dos électricien plombier'.
- 'sac à dos voyage ergonomique': deuter Voyager ×7, osprey, thule.
- 'sac à dos secouriste médical ergonomique': military.eu, usinenouvelle, inforisque.
- 'claie de portage charge lourde ergonomique': alpinstore, tonton.
- 'sac à dos Compostelle mal de dos': conseilsport.decathlon.fr, pilgrim sites. This despite a Compostelle 35 L product and 'compostelle' in the hiking category slug.

Category titles as shown in SERPs: 'Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS', 'Sac à dos exosquelette urbain Gravipack allege le poids sur le dos', 'Sac à dos médical Gravipack allégez vos missions sauvez des vies'.

<https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-urbain/> · <https://www.gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-medical/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/> · <https://www.deuter.com/fr-fr/futura-23/3400126> · <https://www.glisshop.com/conseils/top-5-des-sacs-a-dos-de-rando-legers.html> · <https://www.velotafeur.fr/sacs-a-dos-velo/sacs-a-dos-velotaf/> · <https://www.tonton-outdoor.com/fr_FR/blog/articles/les-meilleurs-sacs-a-dos-pour-le-velotaf-patagonia-the-north-face-gregory> · <https://military.eu/fr/c/sacs-a-dos/sacs-a-dos-selon-l-usage/sacs-a-dos-militaires-et-tactiques/sacs-a-dos-militaires-stoirm> · <https://conseilsport.decathlon.fr/chemin-de-compostelle-que-mettre-dans-son-sac-a-dos> · <https://www.manomano.fr/cat/sac+a+dos+porte+outils> · <https://www.gravipack.com/produit/sac-a-dos-de-survie-35-litres-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme/>

**Why it matters.** Category pages are the winning page type for these queries (67-90% product or category). Ranking only for a self-coined modifier ('anti mal de dos') captures a narrow slice of demand. Buyers search by activity plus feature (léger, 60+10, vélotaf, porte-outils, tactique) and compare specs.

**SEO effect.** Most of the commercial demand in each use case never sees Gravipack, because category titles, H1s and slugs lack the head term and the copy lacks the spec vocabulary competitors show (grams, litres, kg of load).

**How to fix.** 1. Keyword-map each category to 'market head term + differentiator' (T7):
   - randonnée: « Sac à dos randonnée ergonomique anti mal de dos | Gravipack » (59 chars), slug /sac-a-dos-randonnee-ergonomique/;
   - business: « Sac à dos ordinateur ergonomique anti mal de dos | Gravipack » (60);
   - outillage: « Sac à dos porte-outils ergonomique anti-TMS | Gravipack » (55);
   - militaire: 'Sac à dos tactique ergonomique';
   - médical: 'Sac à dos secouriste et médical ergonomique';
   - urbain: a new sub-category 'Sac à dos vélotaf', only with models designed for bike use (Tokyo and Rome per their titles).
2. Add a 301 for each slug change and update menus.
3. Write 400-600 words of buying guide per category:
   - volume, empty weight, maximum load, laptop size, rain cover, ventilation, sizing and fitting service;
   - a spec comparison table across models;
   - links to the related guides (R1-R3, E1, W1);
   - a 'Compostelle' H2 inside the hiking category.
4. PDP titles: model + use + capacity, e.g. « Sac à dos de trek Helsinki 60+10 L à exosquelette | Gravipack ».
5. Run 'sac à dos porte outils' and 'sac à dos vélotaf' in rank tracking as success benchmarks.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the presence data matches the saved E4, E10, E11 and E12 sets.

Weak evidence:
- Most 'absent' evidence comes from standard mode (notes #7, #24, #25, #30, #34, #41, #47, #48): randonnée léger, 60+10, tactique militaire, voyage, secouriste, claie, Compostelle, porte-outils artisan.
- Standard mode returned no gravipack.com URL even for 'sac à dos anti mal de dos', where extended mode found 3. These absences are weak, US-only signals: 'likely', not 'confirmed'.
- 'Sac à dos porte outils (8th)' and the vélotaf extended set are not in the saved notes and could not be checked.

Omissions:
- A voyage category (/sac-a-dos-exosquelette-voyage-gravipack-anti-mal-de-dos/) and a militaire category already exist. Both belong in the keyword map, and voyage is missing from the fix.

Realistic upside: head-term SERPs are dominated by Deuter, Osprey and military.eu, so a small brand's likely gain from retargeting is long-tail, not a head-term top 3. Medium is appropriate.

Fix notes:
- Category slug changes cascade under the parent category; batch all category URL changes into one migration.
- 'anti-TMS' in a title is an occupational-health claim and needs substantiation.

### Health and reimbursement claims circulate in SERPs without an authoritative Gravipack page, and the 'remboursé sécurité sociale' and 'prescrit médecin du travail' queries are unowned

`health-claims-and-reimbursement-queries-unowned` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** 'sac à dos remboursé sécurité sociale mal de dos': the only Gravipack-related result is challenge.ma, where the inventor says it is the first backpack reimbursed by social security, via the médecin du travail and the employer. The rest are insurer and mutuelle guides about the ceinture lombaire (april.fr, lecomparateurassurance ×2, groupama, previssima).

'sac à dos prescrit médecin du travail employeur prise en charge': legal pages (legisocial, lefebvre-dalloz, previssima) citing Cass. soc. 5 July 2017 n°15-29.424 (a prescription alone does not oblige reimbursement) and art. L4122-2.

Claims in titles: Decathlon PDPs say 'Allège la charge de 92%'; the Gravipack school category says 'allège le poids de 92%'. Search summaries in 8+ SERPs explicitly describe the 92 % figure and the 'dispositif médical' status as unverified manufacturer claims.

<https://www.challenge.ma/?p=271181> · <https://www.april.fr/complementaire-sante/guide/ceinture-lombaire> · <https://formation.lefebvre-dalloz.fr/actualite/preconisations-du-medecin-du-travail-lemployeur-doit-il-prendre-en-charge-des-lunettes> · <https://www.legisocial.fr/actualites-sociales/2343-achat-lunettes-preconise-medecin-travail-rembourse-salarie.html> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · <https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/>

**Why it matters.** The topic is YMYL-adjacent: quality raters and AI systems discount unsubstantiated health claims. A factual page explaining how employer coverage actually works would capture B2B and consumer queries that nobody answers well today, and it would support HR/HSE purchases.

**SEO effect.** Trust erodes and AI answers summarize Gravipack as 'unverified'. B2B leads (HSE managers, médecins du travail) are lost, and there is a regulatory and reputational risk if the claims are challenged.

**How to fix.** 1. Create W2 /prise-en-charge-employeur-sac-a-dos/ (1,200 words):
   - employer obligations (art. L4122-2 Code du travail) and médecin du travail recommendations (art. L4624-3);
   - the limits set by Cass. soc. 2017;
   - the documents Gravipack provides (devis, fiche technique, attestation);
   - a clear statement of whether any Assurance maladie or LPP reimbursement exists. Only say it does if it is documented.
2. Use 'dispositif médical' only if the product is registered as one (EU MDR 2017/745 class I, CE marking), and show the reference.
3. Replace '92 %' title claims with a measured, scoped sentence linked to the protocol on T4, and ask Decathlon and resellers to update their titles.
4. Have the claims reviewed by legal counsel.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: saved note #9 matches (challenge.ma, april, lecomparateurassurance ×2, previssima, groupama, no gravipack.com).

Corrections:
(1) 'Search summaries in 8+ SERPs describe the 92 % as unverified' refers to the audit tool's summarizer, not public AI answers. The seo_effect line 'AI answers summarize Gravipack as unverified' is not supported by evidence.
(2) The saved data shows two more owned places carrying the 92 % claim: the post /inventeur-dun-sac-a-dos-en-apesanteur/ ('…allège le poids de 92%') and the legacy presta study page. The fix should cover them.
(3) The reading of Cass. soc. 5 July 2017 n°15-29.424 ('a prescription alone does not oblige reimbursement') could not be verified here and must be checked by counsel before publication.

Correctly cited:
- art. L4122-2 (health and safety measures must not cost workers anything);
- art. L4624-3 (médecin du travail proposes individual measures).

Search volume for 'remboursé sécurité sociale' is probably tiny, so the value is mainly trust and compliance. Medium is kept for the YMYL and regulatory risk: a product with a medical intended purpose falls under MDR 2017/745. Add the DGCCRF misleading-claims risk (Code de la consommation L121-2).

### Comparison and best-of intent (30-45% of commercial SERPs) has no Gravipack page type

`comparison-page-type-missing` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** Listicles or comparisons appear in:
- 'meilleur sac à dos anti mal de dos' (norveya, accergo, techradar);
- 'sac à dos randonnée anti mal de dos' (zeoutdoor comparatif, norveya, accergo);
- 'sac à dos ergonomique' (accergo, le-repaire);
- 'sac à dos scolaire anti mal de dos' (bodypack, sac-a-dos-france, laboutiquedestoons);
- 'sac à dos vélotaf' (tonton-outdoor, gravelrepublic, guide-velo);
- 'sac à dos anti mal de dos avis comparatif' (meilleurtest, globe-trotting, snowleader);
- 'meilleur cartable ergonomique comparatif 2026' (avis-parents, meilleurtest, futura).

Alternative technologies visible in SERPs:
- Osprey AntiGravity (mec.ca, i-run) and Deuter Aircontact;
- Tucano Marte Gravity 'AGS Anti Gravity' (3 pearl.fr results for 'sac à dos ordinateur anti mal de dos');
- Kensington Contour lumbar support;
- ergobag, Bon Chic Bon Dos (designed by osteopaths), Jeune Premier Ergomaxx (claims -30 %);
- the LEX exoskeleton (neozone).

<https://norveya.com/blogs/organisation/les-meilleurs-sacs-a-dos-ergonomiques-contre-le-mal-de-dos> · <https://zeoutdoor.com/randonnee/comparatif-sac-a-dos-de-randonnee> · <https://www.pearl.fr/article/TG3837/sac-a-dos-pour-pc-portable-15-6-16-marte-gravity-avec-redresse-dos-noir> · <https://www.mec.ca/fr/product/6016-968/sac-a-dos-aura-ag-60-de-osprey-femmes> · <https://guide-velo.com/sac-a-dos-velotaf-982> · <https://meilleurtest.fr/comparatif-sac-a-dos/> · <https://www.avis-parents.com/tests-avis/meilleur-cartable/> · <https://www.neozone.org/innovation/lexosquelette-lex-se-transforme-en-chaise-et-reduit-de-50-le-poids-de-votre-sac-a-dos>

**Why it matters.** Per seo-competitor-pages and the taxonomy in page-type-taxonomy.md, comparison intent needs a comparison layout (matrix, pros and cons, a 'best for' verdict). A single product page facing comparison intent is a HIGH mismatch. Gravipack's differentiator (a passive exoskeleton in the straps) only becomes legible when compared with filet tendu, anti-gravity suspensions and lumbar supports.

**SEO effect.** These SERP slots go to third parties who may omit or misdescribe Gravipack, and the brand cannot shape how it is evaluated during the consideration stage.

**How to fix.** 1. Build T2 'Sac à dos exosquelette vs sac à dos classique' and T3 'Exosquelette vs dos filet tendu / anti-gravité' (Osprey AG, Deuter Aircontact).
2. Add a laptop roundup inside A3: 'Sac à dos ordinateur anti mal de dos : 4 technologies comparées' (exosquelette, bretelles à suspension élastique, support lombaire, dos 3D).
3. Follow the fairness rules:
   - verifiable specs only, with prices marked 'au [date]';
   - disclose that Gravipack is your brand;
   - acknowledge competitor strengths (ventilation, lighter weight, lower price);
   - state the methodology;
   - write 'Non communiqué' for missing data.
4. Schema: ItemList; never Product ratings for competitors.
5. Do not create a separate 'meilleur sac à dos anti mal de dos' page: it shares 4 URLs with Hub A, so a separate page would cannibalize it. Put that comparison table inside P1.
6. Pitch independent listicles (zeoutdoor, guide-velo, tonton-outdoor, meilleurtest) with samples.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: listicle presence matches the saved extended data.
- K4: norveya, accergo, techradar.
- K6: zeoutdoor, norveya, accergo.
- K1: accergo, le-repaire.
- K7: bodypack, sac-a-dos-france, laboutiquedestoons.

Corrections:
- '30-45 % of commercial SERPs' is slightly high. K1 is 2/9 (22 %) and K4 and K6 are 3/9 (33 %); about 20-35 % is accurate.
- page-type-taxonomy does not rate 'product page against comparison intent' as HIGH. It lists 'Comparison Page when user wants to buy' as MEDIUM and 'Blog → Comparison' as HIGH. Drop the 'HIGH mismatch' wording.
- A brand-authored 'best of' that includes its own product rarely ranks for 'meilleur…' queries, where Google's reviews system favours independent first-hand testing. Own-brand 'X vs Y' explainers (T2, T3) are realistic; the listicle slots are mainly won through outreach, as the fix already says.
- 'P1' is undefined (elsewhere the page is called Hub A or T9); align the references.

### The category term 'sac à dos exosquelette' is defined by third parties (some inaccurately) and Gravipack has no explainer page

`exosquelette-concept-defined-by-third-parties` · AI Search Readiness · auditor severity **Medium** → verifier **weakened**, severity **Medium**

**Evidence.** Extended SERP:
- kentfaith.fr blog 'Sac A Dos Exosquelette ?' (the search summary flags dubious claims: sensors, automatic adjustment, army use);
- i-trekkings.net test of the Oslo 70 L;
- alloprod.com, ergo-corner, compostelle-autrement.com;
- the Gravipack catalogue category and home;
- a Decathlon Hiking 33 PDP and Google Patents.

Standard SERP: an ffrandonnee.fr news item 'Une innovation : un exosquelette pour alléger le poids du sac à dos', journaldugeek, neozone (LEX) and EPO patents.

Search summaries describe the mechanism inconsistently: 'inserts en carbone relevant les bretelles comme des pouces', 'armature métallique', transfer 'vers le centre de gravité', and critics saying the load is simply moved to the lumbar area.

<https://www.kentfaith.fr/blog/article_sac-a-dos-exosquelette_6410> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · <https://www.alloprod.com/sac-a-dos-exosquelette/> · <https://www.compostelle-autrement.com/post/gravipack-le-sac-a-dos-en-apesanteur> · <https://www.ffrandonnee.fr/s-informer/actualites/une-innovation-un-exosquelette-pour-alleger-le-poids-du-sac-a-dos> · <https://www.journaldugeek.com/2021/09/04/gravipack-ce-sac-a-dos-a-un-exosquelette-qui-libere-les-epaules/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/>

**Why it matters.** The SERP is fragmented, with no page-type consensus, which seo-sxo flags as a differentiation opportunity. Entity clarity matters for AI search (seo-geo): the inventor of the category should own its definition, mechanism and limits.

**SEO effect.** Featured snippets and AI answers take their definition from third parties, and misinformation (sensors, automatic adjustment) persists. No Gravipack URL can rank for 'comment fonctionne un sac à dos exosquelette' variants, and PDPs lack a strong supporting explainer to link to.

**How to fix.** Publish T1 /sac-a-dos-exosquelette/ (1,500-1,800 words) with:
- a 50-word definition box: « Un sac à dos exosquelette est un sac dont les bretelles intègrent une structure rigide passive (sans moteur) qui modifie le trajet de la charge… »;
- a force-path diagram;
- what it does not do: it does not remove weight. Show where the load goes, with measurements, to answer the lumbar critique;
- patent numbers, insert material and the weight they add (g);
- history as reported by the press (Concours Lépine 2018 silver medal, armée tests 2017);
- an FAQ and an embedded video.

Schema: Article + BreadcrumbList. Link from every PDP (« Comment fonctionne l'exosquelette »), from the categories and from P1. Title « Sac à dos exosquelette : comment ça marche ? | Gravipack » (56 chars).

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the saved E3 set matches.

What is overstated:
- Gravipack already holds 2 of 9 results (catalogue and home).
- 5 more results are about Gravipack: ergo-corner, i-trekkings, compostelle-autrement, the Decathlon Hiking 33 page and Google Patents.
- Only kentfaith and alloprod are generic third parties. So 'defined by third parties' is overstated.
- The saved title table shows existing explainer-like posts: /evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/, /et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/ and /inventeur-dun-sac-a-dos-en-apesanteur/. Audit and consolidate them into T1 with 301s rather than adding a page that cannibalizes them.

Fix notes:
- Decide whether T1 or the catalogue category is the primary URL for 'sac à dos exosquelette'; both currently target it.
- Verify the 'Concours Lépine 2018 silver medal' year. The legacy presta page title says 'médaille d'argent concours Lépine international' with no year.
- An FAQ block is fine as content, but since 2023 FAQ rich results only show for authoritative government and health sites, so do not expect them.

### Legacy PrestaShop store presta.gravipack.com is still indexed with competing category and product pages and old prices

`legacy-prestashop-subdomain-indexed` · Technical SEO · auditor severity **Medium** → verifier **unverifiable**, severity **Medium**

**Evidence.** site:presta.gravipack.com returned:
- / ('Gravipack, le sac a dos scolaire, business et randonnée…')
- /73-gravipack
- /72-sac-a-dos-scolaire ('Sac a dos scolaire Gravipack, le sac à dos qui soulage le poids des épaules et du dos.')
- /24-sac-a-dos-sport ('Sac à dos de randonnée Gravipack soulagera vos épaules et votre dos.')
- /accueil/15-sac-a-dos-gravipack-business-talk.html (199 €, 'Medaille d'argent concours Lepine international.')
- /accueil/16-sac-a-dos-gravipack-hikking33.html (229 €; also surfaced in site:gravipack.com searches)
- /accueil/17-sac-a-dos-gravipack-road-adventure.html

Whether these URLs still return 200 cannot be checked from here.

<https://presta.gravipack.com/> · <https://presta.gravipack.com/73-gravipack> · <https://presta.gravipack.com/72-sac-a-dos-scolaire> · <https://presta.gravipack.com/24-sac-a-dos-sport> · <https://presta.gravipack.com/accueil/15-sac-a-dos-gravipack-business-talk.html> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://presta.gravipack.com/accueil/17-sac-a-dos-gravipack-road-adventure.html>

**Why it matters.** A second indexed store duplicates the main store's school and hiking categories and brand pages, and its prices may be stale. It competes in exactly the clusters this audit wants to consolidate.

**SEO effect.** Relevance and links are split between two stores, outdated offers can appear in SERPs (a trust and conversion issue), and crawl is wasted. If the old store still takes orders, it creates confusion.

**How to fix.** 1. Crawl the legacy store and map every URL to its WooCommerce equivalent.
2. On the presta host, add one-to-one 301 rules in .htaccess, for example:
RewriteEngine On
RewriteRule ^72-sac-a-dos-scolaire/?$ https://www.gravipack.com/cartable-ergonomique/ [R=301,L]
RewriteRule ^24-sac-a-dos-sport/?$ https://www.gravipack.com/sac-a-dos-randonnee-ergonomique/ [R=301,L]
RewriteRule ^73-gravipack/?$ https://www.gravipack.com/sac-a-dos-ergonomique/ [R=301,L]
RewriteRule ^accueil/16-sac-a-dos-gravipack-hikking33\.html$ https://www.gravipack.com/produit/<hiking-33-canonical>/ [R=301,L]
RewriteRule ^accueil/17-sac-a-dos-gravipack-road-adventure\.html$ - [G,L]
RewriteRule ^$ https://www.gravipack.com/ [R=301,L]
3. Return 410 for discontinued products with no equivalent. Do not send everything to the home page (soft 404).
4. Add a GSC Domain property to see the subdomain, use Removals temporarily, and drop its sitemap.

**Verifier notes.** Not re-run (search budget exhausted).

The saved data corroborates this finding and shows more indexed legacy URLs: /2-accueil, /22-produit, /40-etude-scientifique-soulage-le-dos-gravipack, /59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack, /plan-du-site-gravipack, /content/1-livraison… and /accueil/13-sac-a-dos-gravipack-safar-vibe.html.

Live status (200, 301 or 404) is unknown and indexes lag, so severity depends on a check (curl -I, a GSC Domain property).

Fix issues:
- The example .htaccess rules redirect to URLs that do not exist yet (/cartable-ergonomique/, /sac-a-dos-randonnee-ergonomique/, /sac-a-dos-ergonomique/). Deployed now, they would land on 404s. Point them at the current live URLs, then update them during the slug migration so no redirect chains form.
- The study and Concours Lépine pages hold evidence content. Migrate that content to the planned evidence page (T4/T11) before redirecting with a 301, rather than returning 410.

### The brand query 'gravipack' does not return the home page first, and the company entity is described inconsistently across sources

`brand-navigational-serp-and-entity-fragmented` · Brand / Reputation · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** 'gravipack' (ext), in the tool's order: kisskissbankbank.com/en/projects/gravipack (English crowdfunding page) 1st, YouTube ×2, equilibre-france-ergonomie.fr, gravipack.com/gravipackers/, then the home page 6th. 'gravipack' (std) returned no gravipack.com URL at all (motherbase.ai, neozone, lespepitestech, randonner-leger ×2, lematin.ma, maddyness, plus the unrelated GravPack and Gravis).

Entity details differ by source:
- the mentions légales name the operator EXOSQUELETTE LIGHT (Paris);
- motherbase gives Vincennes;
- lespepitestech says French Tech Aix-Marseille and also 'startup Applications à Sens';
- journaldugeek and several summaries say Kid'abord (Loire-Atlantique);
- Decathlon lists the seller as KID'ABORD;
- Nature & Découvertes' Kid'abord seller gives the return address 'SODILOG / RETOUR GRAVIPACK' (Colmar).

A quoted 'gravipack.fr' search returned nothing from gravipack.fr.

<https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.youtube.com/@Gravipack> · <https://equilibre-france-ergonomie.fr/les-nouveaux-sacs-gravipack/> · <https://www.gravipack.com/gravipackers/> · <https://gravipack.com/> · <https://my.motherbase.ai/startup/107826-gravipack> · <https://lespepitestech.com/startup-de-la-french-tech/gravipack> · <https://www.natureetdecouvertes.com/enfant/loisirs-creatifs/peinture-coloriage/cartable-38-cm-pol-fox-space-invider-92681490> · <https://gravipack.com/mentions-legales/> · <https://www.decathlon.fr/brands/gravipack>

**Why it matters.** A navigational query should return the owned site first, with sitelinks. Consistent entity data (name, legal entity, founder, address, sameAs) feeds the Knowledge Graph and how AI systems describe the brand.

**SEO effect.** Brand traffic leaks to KKBB and YouTube, sitelinks and a knowledge panel are unlikely, AI answers mix entities (Kid'abord / Exosquelette Light / Gravipack), and trust drops when users see conflicting company data.

**How to fix.** 1. Home title brand-first; add Organization JSON-LD on the home page: name 'Gravipack', legalName 'EXOSQUELETTE LIGHT' (verify), founder Mohammed Errafi, address, logo, and sameAs for the YouTube channel, KKBB, LinkedIn, Trustpilot and the Decathlon brand page.
2. Write an About page that explains the relationship between EXOSQUELETTE LIGHT, Gravipack and Kid'Abord (seller, returns) in one place.
3. Update the directory profiles (lespepitestech, motherbase) with the same NAP and URL.
4. Make sure gravipack.fr 301-redirects to the canonical gravipack.com home (blocked here; verify).
5. Ask KKBB to link to the official site; consider a Wikidata item once notability sources are consolidated.
6. Monitor the brand SERP monthly.

**Verifier notes.** Not re-run (search budget exhausted). Saved standard note #13 matches: no gravipack.com URL for 'gravipack'.

Why the brand-SERP claim is weak:
- The WebSearch tool is US-only and not Google.fr. The standard 'gravipack' SERP mixed in the unrelated GravPack and Gravis, and the same mode missed gravipack.com for its own core term.
- The tool's order is not a Google position. Even in extended mode a gravipack.com URL (/gravipackers/) was 5th and the home page 6th.
- 'Brand traffic leaks to KKBB and YouTube' needs GSC (query 'gravipack' → average position and landing pages) or a real Google.fr check.

The entity-inconsistency part is useful (EXOSQUELETTE LIGHT vs Kid'abord vs French Tech Aix-Marseille vs Vincennes), but some of its evidence is weak:
- The Nature & Découvertes URL is a Pol Fox 'Space Invider' cartable listing, not a Gravipack page.
- 'startup Applications à Sens' is probably a lespepitestech category label, not a location.

Severity drops to Low. The Organization schema and About-page work is still cheap and worth doing.

Fix note: sameAs should list profiles that represent the entity (YouTube, LinkedIn, social profiles, later Wikidata). Trustpilot, the Decathlon brand page and a KKBB campaign page are weak sameAs targets.

### The Decathlon marketplace and the reseller ergo-corner capture generic and brand SERP slots from Gravipack demand

`marketplace-reseller-serp-capture` · E-commerce · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** decathlon.fr/vc/gravipack ranked for 'sac à dos anti mal de dos' (std, listed 1st), 'meilleur sac à dos pour le mal de dos' and 'sac à dos collège léger dos mal aux épaules ado'.

site:decathlon.fr gravipack returned the collection (13 items; sellers KID'ABORD and Gravipack) and the Feather, Feather Plus, Hiking 33, Safar Vibe and Business Talk PDPs, with titles carrying 'Allège la charge de 92%'. The Sherpa 45 on Decathlon was €149.90, down from €249 (promotion 18/06-30/08/2026, seller Kid'Abord).

ergo-corner.com/55-gravipack appeared in 8 extended 'anti mal de dos' SERPs, alongside /content/13 and blog b14. fnac.com review pages rank for 'gravipack avis'.

<https://www.decathlon.fr/vc/gravipack> · <https://www.decathlon.fr/browse/b/gravipack/_/N-19o8oxe> · <https://www.decathlon.fr/brands/gravipack> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-scolaire-et-sport-gravipack-feather-noir/_/R-p-5473954c-4430-4566-9a58-48f26aae66e5> · <https://www.ergo-corner.com/55-gravipack> · <https://www.fnac.com/Sac-a-dos-Gravipack-Road-Adventure-Noir/a16167915/avis?qui=d4e5a2e925&thinga=03ed2700&l=e07c3281&t=3ce8763e>

**Why it matters.** Marketplaces have more domain strength and often outrank the brand for generic intent. If their pages show lower prices or carry the same copy, the brand site loses both the ranking and the sale.

**SEO effect.** There is less direct traffic, margin and first-party data, and price differences across channels in SERPs undermine trust. Duplicate product descriptions across channels can lead Google to prefer the marketplace version.

**How to fix.** 1. Make gravipack.com the most useful destination:
   - the fitting service (sizing by height and weight per the FAQ);
   - full spec tables;
   - guides and the evidence page;
   - the warranty statement.
2. Write unique product descriptions per channel and never paste site copy into marketplace listings.
3. Ask Decathlon (brand page) and ergo-corner to link 'Site officiel' or the relevant guide.
4. Align price communication, or explain the official-site advantages.
5. Make sure own-site Product structured data and Merchant Center free listings are in place (handled by the e-commerce or schema auditors).
6. Track share of voice on the T1 keywords, including marketplace URLs.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the Decathlon data matches the saved standard notes (collection N-19o8oxe, Feather, Feather Plus, Hiking 33, Safar Vibe and Business Talk pages, titles 'Allège la charge de 92%').

Corrections:
(1) In the saved overlap data ergo-corner/55 appears in 7 of the 12 extended commercial SERPs, 6 of them 'mal de dos' queries, not 8.
(2) The Sherpa 45 at €149.90 was a promotion that ended 30/08/2026. It had expired by the audit date (12/10/2026); do not present it as current.
(3) The 'capture' framing is overstated. ergo-corner and Decathlon sell Gravipack products, and the Decathlon seller is Kid'Abord, which several sources link to the brand itself. These slots are distribution share rather than lost demand; whether they matter depends on channel margins.

Severity drops to Low. The advice on unique descriptions per channel and on making the official site the most useful destination is sound.

### Occupational/TMS demand (artisans, HSE, BTP, emergency services) is served by INRS, OSHA, FFB and OPPBTP, with no Gravipack B2B content despite its 'anti-TMS' products

`b2b-occupational-cluster-missing` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** 'sac à dos TMS travail': inspq ×4, osha.europa.eu, factorial ×2, myrhline, pharma-gdd.

'exosquelette passif prévention TMS port de charge': ffbatiment ×2, inrs.fr, bul.ch, travail-industrie, sante-sur-le-net, batiweb, hal.univ-lorraine, osha.

'sac à dos porte outils' (ext) includes preventionbtp.fr 'Un sac à dos pour faciliter le port d'outils lors de déplacements verticaux'.

Meanwhile Gravipack's own SERP titles position products as anti-TMS: 'Claie de portage Gravipack anti-TMS pour charges très lourdes' and 'Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS'. The ToolMaster PDP is made to order on quote.

<https://www.inspq.qc.ca/troubles-musculo-squelettiques-lies-au-travail> · <https://osha.europa.eu/fr/themes/musculoskeletal-disorders> · <https://www.ffbatiment.fr/actualites-batiment/actualite-bam/exosquelettes-et-prevention-des-tms-de-necessaires-precautions-d-usage> · <https://inrs.fr/dam/jcr:e1ee1abc-4724-493b-82a9-cba5ec660b47/nt62.pdf> · <https://www.preventionbtp.fr/ressources/solutions/un-sac-a-dos-pour-faciliter-le-port-d-outils-lors-de-deplacements-verticaux_vX8vkah2YYzmVWGTvhZeqT> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/claie-de-portage/>

**Why it matters.** B2B buyers (HSE managers, médecins du travail, BTP companies, emergency services) research through institutional prevention content. That is where a passive load-carrying exoskeleton has to be framed (assessment, field trial, limits) to be bought in volume.

**SEO effect.** Gravipack misses high-value B2B queries and authoritative links (OPPBTP, FFB), and the 'anti-TMS' claim on categories lacks a supporting content layer.

**How to fix.** 1. Publish W1 /conseils/tms-port-de-charge-sac-a-dos/: what a passive load-carrying exoskeleton is; the INRS/OSHA framing; the employer process (risk assessment, field trial, training); limits; case studies (only real ones).
2. Publish W3 /professionnels/: quotes, trial units, fleet pricing, customisation (ToolMaster on quote), a downloadable spec sheet, and a contact form with Service schema.
3. Submit Gravipack tool packs to the OPPBTP 'Solutions' database (preventionbtp.fr) and to FFB innovation channels, if eligible.
4. Link W1, W2 and W3 from the outillage, médical and claie categories.

**Verifier notes.** Not re-run (search budget exhausted).

What holds: the SERP lists match saved notes #19 and #46. The preventionbtp result (extended 'sac à dos porte outils') is not in the saved data and could not be checked.

Correction: 'no Gravipack B2B content' is partly contradicted by the saved title table. These B2B pages exist:
- /le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/ (case study);
- the Vivatech/RATP post;
- /gravipack-soulage-les-forces-speciales-au-sofins/;
- /produit/fabrication-professionnelle-gravipack/.
They are written as news and do not rank. The gap is structure (no B2B hub, no TMS guide), not zero content.

Realistic upside: the TMS SERPs are institutional (INRS, OSHA, and INSPQ ×4 from Quebec, a sign of the tool's US/Canada geography), and a brand page will rarely rank there. The SEO value is mainly links and listings (OPPBTP, FFB) plus the B2B landing page.

Severity drops to Low. W1 should use the RATP deployment as its real case study.

### Titles and slugs as shown in SERPs waste or misplace keywords (legal page, 'Vive la rentrée scolaire', 'Archives', 120+ character titles, non-descriptive slugs)

`serp-titles-slugs-off-target` · On-Page SEO · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** SERP titles and URLs seen:
- /mentions-legales/ → 'Le sac à dos ergonomique - Mentions légales, tout ce que vous devez savoir sur Gravipack.'
- A Kingston PDP titled 'Vive la rentrée scolaire'.
- Blog archives indexed as 'Innovation Archives - …' and 'Technologie Archives - …'; the accessories category as 'Accessoires sac à dos Archives - …'.
- The Helsinki PDP title is 120+ characters; the Compostelle PDP title includes the full site tagline ('… - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant').
- The Tokyo slug '/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/' contains neither the model nor the use.
- A '/actualites-gravipack-2/' slug.
- The home page appeared with two different titles.

The engine may rewrite titles, so verify these against the HTML.

<https://gravipack.com/mentions-legales/> · <https://gravipack.com/produit/vive-la-rentree-scolaire-sac-anti-mal-de-dos-college-gravipack-kingston-avec-exosquelette/> · <https://www.gravipack.com/categorie/innovation/> · <https://www.gravipack.com/categorie/technologie/> · <https://www.gravipack.com/categorie-produit/accessoires-sac-a-dos/> · <https://www.gravipack.com/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-helsinki-gravipack-60l-10l-70l/> · <https://www.gravipack.com/produit/sac-a-dos-de-survie-35-litres-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/actualites-gravipack-2/>

**Why it matters.** Titles are the main relevance and CTR lever in SERPs. Off-target or truncated titles waste the keyword map designed in T1/T7.

**SEO effect.** CTR is lower because titles are truncated or generic, low-value archive pages are indexed, and the legal page sends head-term signals.

**How to fix.** 1. In Rank Math or Yoast, set the product title template to '%title% | Gravipack' and write each product title (≤60 chars) as model + use + capacity.
2. Set the blog category and tag archives to noindex,follow (Innovation, Technologie), or turn them into real hubs with intro copy.
3. Remove 'Archives' from the taxonomy title templates.
4. Retitle the legal page and set it to noindex.
5. Change the Tokyo slug to /produit/sac-a-dos-tokyo-30l-exosquelette/ with a 301.
6. Fix '-2' slugs after checking for a duplicate original.
7. Lock in a single home page title.

**Verifier notes.** Not re-run (search budget exhausted).

The saved title table corroborates most bullets:
- the mentions-légales title;
- 'Archives' titles on /categorie/innovation/, /technologie/, /militaire/ and the accessories category;
- the Helsinki title at 136 characters;
- Compostelle titles at 182-204 characters including the tagline;
- the Tokyo slug and /actualites-gravipack-2/.

'Home appeared with two different titles' is weak. One title belongs to a parameter URL (/?add-to-cart=6527); the other came from title rewriting by the tool or Google (E4). Verify in the HTML.

The table also shows more indexation clutter, to hand to the technical auditor:
- /test/, a duplicate of the SOFINS post;
- /contacts/ vs /contact-gravipack/;
- a second blog base /category/…;
- attribute archives;
- ?add-to-cart and ?order parameter URLs.

Fix caveat: changing the Tokyo slug brings little, because URL words are a light signal and Tokyo already ranks for 2 tested queries. Only do it as part of a merge or redirect project.
