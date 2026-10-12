# Phase 2 — freshness-b2b-segments

Searches run: 25

## Evidence base

I ran 25 WebSearch calls, which was the hard cap. That count includes one API 400 error (S13). 20 used standard mode and 5 used extended mode. The raw log is at /tmp/claude-0/-home-user-soufian/f48d95be-0ad3-5e07-bab2-7b53bc671068/scratchpad/phase2/freshness-b2b-segments.md. I reused facts from phase 1 and the sibling phase-2 logs without searching them again: the PagesJaunes/Mappy listing in Vincennes, LinkedIn posts up to 2023-10-14, the EXOSQUELETTE LIGHT head office in Paris 75002 since 19/05/2026, and signal-arnaques. The index is US-based, not google.fr, so ranks are only indicative. LIMITATION: S13 showed that the search user agent cannot reach leparisien.fr, actu.fr, lyonne.fr, ouest-france.fr, francetvinfo.fr, 20minutes.fr, bfmtv.com or tf1info.fr. So I could not check regional or national press with domain filters, and the freshness result means 'not found in 25 searches', not 'proven absent'.

(1) FRESHNESS. I found no independent editorial coverage dated 2025 or 2026. Queries covered 2025/2026, actualité (extended), salons, Préventica, SOFINS, fundraising, LinkedIn and press domains. The most recent dated independent article is still Maddyness, 2024-02-08. Later third-party signals:
- A KKBB children's-bag campaign ended 2024-04-05 with 295 pre-orders (pre-orders, not equity funding).
- A Trustpilot review from Feb 2026 (UGC).
- Decathlon marketplace listings with a promo running 18/06 to 30/08/2026, sold by KID'ABORD.

The RATP Group CSR page (ratpgroup.com) names 'the exoskeleton backpack, developed by Gravipack' for track-inspection staff. It is the strongest independent institutional reference, but it is undated. The ICI article 'La RATP innove avec les exosquelettes' is also undated.

The owned site does show 2026 activity: Tokyo pre-orders shipping from mid-Sept 2026, Business Talk V4 'June 2026', and the Barracuda claie delivering from mid-Nov 2026. It also has posts about the SOFINS and Techterre Combat Futur military shows, but none of these has a date visible in search results and no third party corroborates them. A LinkedIn claim of being 'invité d'honneur' at two military shows with 57 delegations was not corroborated either. I found no Préventica exhibitor listing and no equity raise.

(2) B2B. gravipack.com has indexed B2B pages, but none is built as a landing hub:
- two quote URLs, /devis/ and /devis-gravipack/ (B2B team, reply within 24h, form asks for SIRET);
- /produit/fabrication-professionnelle-gravipack/ and an SNCF logo key-ring product (B2B services published as WooCommerce products);
- /dossier-de-presse/ and /nos-clients/;
- product sheets mentioning 'tarifs dégressifs entreprises & administrations', collectivités (Centurion), and AGEFIPH/FIPHFP funding (ExoTool).

No CSE, QVT, médecine du travail, prévention TMS, collectivités, pompiers/secours or entreprises hub surfaced. Gravipack is absent from the occupational TMS results (INRS, DREETS, CRAMIF). In segment-hub tests on generic head terms, only the outillage hub ranks: #9 for 'sac à dos porte-outils' (extended). The médical, business/ordinateur and militaire hubs are absent on extended queries, and scolaire and claie are absent per phase 1.

(3) LOCAL. No store-locator or points-de-vente page is indexed. A 2021 forum thread owns the 'où acheter Gravipack' intent ('vendu sur le site D4 mais pas en magasin'). An owned post 'bientôt en magasin' names no stores. ICI and JDG summaries list historical retail at Décathlon, Nature & Découvertes and Au Vieux Campeur (Paris). A Paris showroom appears only as a past KKBB promise. A GBP listing cannot be observed with this tool. The contact phone is a mobile number.

signal-arnaques #947856: siblings ran 8 queries across two logs and none tied it to Gravipack. I did not spend budget on it, and it remains not attributable.

## Questions resolved

### [partially-resolved] FRESHNESS: Is there any independent coverage of Gravipack in 2025 or 2026 (press, TV, trade shows such as Préventica, Eurosatory, Made in France or VivaTech, fundraising, new products)?

Not found in 25 searches. No independent press, TV or trade-show article dated 2025 or 2026 surfaced. Queries covered 'Gravipack 2025', 'Gravipack 2026', an extended actualité query, salons, Préventica, SOFINS, levée de fonds, LinkedIn, and press domains (ICI, France Bleu, Maddyness, JDG, Le Journal des Entreprises, L'Usine Nouvelle, Presse-citron, Futura, LSA, Objets du Futur). Eight major press domains (Le Parisien, actu.fr, L'Yonne Républicaine, Ouest-France, francetvinfo, 20 Minutes, BFM, TF1info) cannot be reached by the search tool, so absence there is not proven. Préventica: the exhibitor pages (Bordeaux 2025, Ex Villes 2023) are indexed but Gravipack was not shown. Eurosatory: only a 2022 LinkedIn post (sibling log). SOFINS and Techterre Combat Futur appear only on owned posts (/gravipack-soulage-les-forces-speciales-au-sofins/ plus a /test/ duplicate, and /gravipack-presentees-au-salon-militaire-techterre-combat-futur/), with no date in the results and no third-party confirmation. Fundraising: no equity round. The last financing events are KKBB crowdfunding: 294 contributions ending 8 Apr 2022, and the children's bag with 295 pre-orders ending 5 Apr 2024. New products exist only as owned pre-orders: Tokyo (shipping mid-Sept 2026), Business Talk V4 20L (June 2026), and the Barracuda claie (mid-Nov 2026).

<https://my.motherbase.ai/startup/107826-gravipack> · <https://www.decathlon.fr/brands/gravipack> · <https://www.preventica.com/salon/bordeaux-2025/exposants?page=7> · <https://www.kisskissbankbank.com/en/projects/gravipack-le-sac-a-dos-enfant-muni-d-exosquelette/tabs/news> · <https://www.kisskissbankbank.com/nl/projects/gravipack-lesacadosenapesanteur/tabs/backers> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/gravipack-presentees-au-salon-militaire-techterre-combat-futur/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/>

### [resolved] What is the most recent dated third-party mention?

Editorial: Maddyness, 2024-02-08 (date in the URL), confirmed again in S4, S9, S14 and S25. Non-editorial: the Decathlon marketplace promo (18 June to 30 Aug 2026, seller KID'ABORD) and a Trustpilot review dated Feb 2026. The last crowdfunding milestone was KKBB on 2024-04-05. The newest decoded LinkedIn IDs are company posts from 2023-07-10, 2023-07-28 and 2023-08-03; the sibling log found 2023-10-14 as the newest. Undated but potentially recent: the RATP Group CSR page naming Gravipack, the ICI article 'La RATP innove avec les exosquelettes', and a TVEX distributor LinkedIn post shown as '~3 weeks' old relative to crawl. Older dated coverage: ICI/France Bleu 2020-09-03 (decoded from the URL) and 2021-09-02, Journal du Geek 2021-09-04, Objets du Futur 2022-02-14.

<https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://www.decathlon.fr/vc/gravipack> · <https://es.trustpilot.com/review/gravipack.com> · <https://ratpgroup.com/en/heart-of-ratp-groups-csr-commitments/improve-quality-working-life-ratp-group-staff/> · <https://www.ici.fr/infos/transports/la-ratp-innove-avec-les-exosquelettes-5885238> · <https://www.ici.fr/infos/economie-social/la-nouvelle-eco-le-cartable-revolutionnaire-de-la-societe-gravipack-a-sens-fait-un-carton-1599115911> · <https://www.objetsdufutur.fr/2022/02/14/gravipack-le-sac-a-dos-qui-soulage-le-dos-maintenant-a-destination-des-chasseurs-dimages/> · <https://www.linkedin.com/in/thibault-valgalier-b0327215a/> · <https://fr.linkedin.com/posts/gravipack_surprise-cest-lheure-du-golden-ticket-activity-7092887700071931904-ssVE>

### [resolved] B2B: Does gravipack.com have indexed pages targeting entreprises, professionnels, QVT, CSE, médecine du travail, prévention TMS, collectivités, armée or secours?

Partly. Indexed B2B assets exist, but none is a dedicated landing or hub page:
- Two quote pages: /devis/ (B2B team, reply within 24h, free mock-up, form asks for company name and SIRET) and /devis-gravipack/.
- /produit/fabrication-professionnelle-gravipack/ ('cadeaux d'entreprise et objets publicitaires') and an SNCF-branded key-ring product, i.e. B2B services published as WooCommerce products.
- Custom-logo key rings with an inconsistent minimum order (20 vs 30).
- /dossier-de-presse/ and /nos-clients/.
- Military and secours news posts: SOFINS and Techterre.
- Product sheets that mention 'tarifs dégressifs pour entreprises & administrations', collectivités (Centurion), SAMU and médecins militaires, and AGEFIPH/FIPHFP funding (ExoTool).
No indexed URL targets CSE, QVT, médecine du travail, prévention TMS, collectivités/marchés publics or pompiers/secours as a hub. For 'Gravipack prévention TMS médecine du travail salariés', the results are 100% institutional (INRS, DREETS, CRAMIF Préventica, FNTR TMS Pros) and Gravipack does not appear.

<https://gravipack.com/devis/> · <https://gravipack.com/devis-gravipack/> · <https://gravipack.com/produit/fabrication-professionnelle-gravipack/> · <https://gravipack.com/produit/porte-cle-flamme-personnalise-avec-logo-sncf-broderie-premium-gravipack/> · <https://www.gravipack.com/produit/porte-cle-flamme-personnalise-sur-mesure-avec-votre-logo-broderie-premium-gravipack/> · <https://gravipack.com/dossier-de-presse/> · <https://gravipack.com/nos-clients/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-porte-outils-exotool-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/> · <https://www.inrs.fr/dms/inrs/CataloguePapier/DMT/TI-QR-161/qr161.pdf>

### [resolved] Do the segment hubs (randonnée, scolaire, business, militaire, médical, outillage, claie) rank for anything other than 'anti mal de dos' queries?

Only the outillage hub does. /categorie-produit/.../sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/ ranks #9 for the generic head term 'sac à dos porte-outils' (extended mode), after ManoMano, Leboncoin, DeWalt, Leroy Merlin, Hellopro, Rubix, OPPBTP and Fischer Darex. On extended head-term queries Gravipack is absent for 'sac à dos médical secouriste', 'sac à dos ordinateur ergonomique' and 'sac à dos militaire tactique léger'. Phase 1 already showed the scolaire hub absent for 'cartable ergonomique' and 'sac à dos ergonomique', claie absent for 'claie de portage ergonomique', and randonnée and business ranking only when 'anti mal de dos' is in the query (E4, E6).

<https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/> · <https://www.manomano.fr/cat/sac+a+dos+porte+outils> · <https://www.girodmedical.com/urgence-et-reanimation/trousse-de-secours-1/valise-sac-a-dos.html> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/sac-dos-ergonomique-etanche-ordinateur-gris/> · <https://www.projet13.com/291-sac-a-dos-militaire>

### [resolved] POINTS DE VENTE / LOCAL: Are there physical retailers, a showroom, a store locator, a Google Business Profile, or an address on PagesJaunes?

Store locator: none. No 'points de vente', 'revendeurs' or 'où acheter' page is indexed on gravipack.com. One owned post, 'bientôt en magasin', names no stores. The 'où acheter Gravipack' intent is held by 2021 randonner-leger posts saying the bags sold on Decathlon's website 'mais pas en magasin' and 'Vendu et expédié par GRAVIPACK'. Historical physical retail, per the ICI and JDG summaries: Décathlon, Nature & Découvertes, Au Vieux Campeur (Paris). The current Decathlon brand page wording mentions models 'proposés dans les magasins Decathlon', but the marketplace seller is KID'ABORD, so in-store availability is unverified. Showroom: only a past KKBB promise of a Paris showroom; no address or listing was found. PagesJaunes and Mappy: the sibling log found 'Gravipack à Vincennes, Maroquinerie' (pagesjaunes.fr/pros/60790927) and the Mappy POI at 46 r Bienfaisance 94300 Vincennes, both with 0 reviews. The sibling entity log says the legal head office has been in Paris 75002 since 19/05/2026, so these citations are probably out of date. A GBP or knowledge panel cannot be observed with WebSearch. No Sens shop surfaced. The contact phone published by the site is a mobile number (+33 6 66 20 52 49).

<https://gravipack.com/gravipack-bientot-en-magasin-linnovation-en-apesanteur-prend-son-envol/> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626059> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626080> · <https://www.decathlon.fr/vc/gravipack> · <https://www.kisskissbankbank.com/en/projects/gravipack/tabs/faqs> · <https://www.ici.fr/infos/economie-social/la-nouvelle-eco-le-cartable-revolutionnaire-de-la-societe-gravipack-a-sens-fait-un-carton-1599115911> · <https://gravipack.com/conditions-generales-de-vente/> · <https://gravipack.com/contact-gravipack/>

### [unresolved] Is the signal-arnaques.com page https://www.signal-arnaques.com/scam/view/947856 actually about Gravipack?

Not attributable. The two sibling phase-2 logs ran 8 targeted queries: reputation S6, S12 and S15, and entity #20, #21, #27 and #29, including allowed_domains=signal-arnaques.com with the terms 'gravipack', 'gravipack.com avis' and 'Gravipack Trustpilot'. None returned a signal-arnaques report naming Gravipack, and ID 947856 was never returned. The page most likely surfaced because the phase-1 query contained 'Trustpilot', since many signal-arnaques reports are titled 'Trustpilot'. I did not spend budget re-searching this, the page itself was never seen, and it cannot be fetched. Treat it as noise unless someone checks it in a browser.



## What works

- RATP Group's own CSR page (ratpgroup.com) names 'the exoskeleton backpack, developed by Gravipack' for staff who inspect tracks on foot. It is an independent institutional B2B reference the brand can cite and build a case study on.
- The outillage category hub ranks #9 for the generic head term 'sac à dos porte-outils' (extended mode) next to ManoMano, DeWalt and Leroy Merlin. It is the only segment hub seen ranking without the 'anti mal de dos' modifier, so it proves the model works.
- A B2B quote flow exists and is indexed (/devis/: B2B team, reply within 24h, free mock-up, SIRET field), so lead capture is already in place to build on.
- A press page (/dossier-de-presse/) and a references page (/nos-clients/) are indexed and can host dated releases and case studies.
- The owned site shows a live 2026 product pipeline (Tokyo, Business Talk V4, Barracuda claie pre-orders) and military show participation (SOFINS, Techterre Combat Futur). These are ready-made news hooks for a PR cadence.
- There is a track record of regional public-broadcaster coverage (ICI/France Bleu 2020 and 2021), national tech and startup media (JDG 2021, Maddyness 2024) and repeated KKBB campaigns (2022, 2024). Journalists already know the story.
- The Decathlon marketplace presence stayed active with a dated summer-2026 promo, which keeps the brand visible on high-authority retail results.

## Raw findings (with verifier verdicts)

### No independent editorial coverage found since February 2024, and none for 2025 or 2026

`fresh-no-independent-coverage-since-2024` · Off-Page / Authority · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** 12 freshness-oriented searches (S1-S3, S5, S6, S9, S10, S14-S16, S24, S25) returned no independent article dated 2025 or 2026. The most recent dated independent editorial is Maddyness (2024-02-08). After that come only a KKBB pre-order campaign ending 2024-04-05, a Trustpilot review (Feb 2026) and a Decathlon marketplace promo (18/06-30/08/2026). Newer-looking items (the RATP CSR page, the ICI article 'La RATP innove avec les exosquelettes', a TVEX distributor LinkedIn post) carry no date in results. Préventica exhibitor pages are indexed but did not show Gravipack. No equity round surfaced. Caveat: 8 major French press domains (Le Parisien, actu.fr, L'Yonne Républicaine, Ouest-France, francetvinfo, 20 Minutes, BFM, TF1info) cannot be reached by the search tool (S13 API error), so this is 'not found in 25 searches', not proof of absence.

<https://www.maddyness.com/2024/02/08/votre-sac-a-dos-est-toujours-beaucoup-trop-lourd-la-soluce-de-cette-startup/> · <https://www.kisskissbankbank.com/en/projects/gravipack-le-sac-a-dos-enfant-muni-d-exosquelette/tabs/news> · <https://es.trustpilot.com/review/gravipack.com> · <https://www.decathlon.fr/brands/gravipack> · <https://my.motherbase.ai/startup/107826-gravipack> · <https://www.preventica.com/salon/bordeaux-2025/exposants?page=7> · <https://www.ici.fr/infos/transports/la-ratp-innove-avec-les-exosquelettes-5885238>

**Why it matters.** Under claude-seo's E-E-A-T and GEO guidance, brand mentions correlate with AI visibility more strongly than backlinks. A 32-month gap in editorial mentions means link and mention velocity is flat. It also means AI answers and journalists keep repeating 2018-2021 facts: 'apesanteur', the Lépine 2018 award and the 2019 study. Meanwhile sceptical UGC (forum, Outzer, Trustpilot 3.1) stays the freshest third-party content about the brand.

**SEO effect.** Fresh editorial links and mentions would strengthen the brand result page (the official site currently first appears at #6-#7 for 'gravipack'). They would give AI engines recent citable sources and offset the sceptical UGC. The flat velocity is one reason third parties outrank the official site for brand queries.

**How to fix.** 1) Publish dated releases on /dossier-de-presse/ for every real event: Barracuda deliveries (Nov 2026), Tokyo and Business Talk V4 shipments, and show participation. 2) Run the 12-month cadence in data_tables, one hook per month. 3) Pitch three layers: regional (ICI Yonne/Paris, the Val-de-Marne and Paris editions of regional dailies), business/startup (a Maddyness follow-up, Le Journal des Entreprises) and trade (occupational safety and defence media). 4) Get listed in show exhibitor directories, which are indexed. 5) Check the blocked press domains manually in a browser or with a SERP API (DataForSEO) before closing this finding.

**Verifier notes.** The core absence held across three new angles: English news (V2), awards (V9), and VivaTech/Le Parisien (V8). None found an independent editorial piece from 2025 or 2026. The ICI article 'La RATP innove avec les exosquelettes' (5885238) does name Gravipack. The tool dated it about 2.5 years before the crawl, so roughly early 2024, which fits the RATP press release of 29/02/2024. It is not a 2025 or 2026 item. Four reasons High overstates the case. (1) Eight major French press domains cannot be searched, so this is absence of evidence only. (2) The seo-backlinks skill says link velocity is 'DataForSEO only' and free sources give point-in-time snapshots, so the claim 'link and mention velocity is flat' goes beyond the toolkit's own evidence rules. The phase-1 critic had already downgraded the predecessor 'decaying-editorial-velocity' to Medium for this reason. (3) The seo_effect line 'official site first appears at #6-#7 for gravipack' is stale: the sibling re-run (reputation verify V7) shows the brand SERP is volatile, with the first owned URL at #4 and 8 of 9 results owned. (4) The finding ignores third-party institutional mentions. A domain-restricted search returned at least six RATP URLs naming Gravipack, including VivaTech 2023 pages and https://ratpgroup.com/en/2024-asdr/development/. That report covers 2024 and was probably published in 2025, so it may be a dated 2025 non-editorial mention (unverified). The claim that AI answers repeat facts from 2018-2021 was not measured. Keep the finding, but word it 'no independent editorial coverage found since early 2024 (WebSearch, 8 press domains unsearchable)' and set it to Medium.

### B2B demand has no indexable hub: quote pages are duplicated, and services are published as WooCommerce products

`b2b-no-landing-hub` · On-Page SEO · auditor severity **High** → verifier **confirmed**, severity **Medium**

**Evidence.** Indexed B2B assets:
- two quote URLs with the same intent: /devis/ ('Devis - Le sac à dos exosquelette GRAVIPACK...', B2B team, reply within 24h, SIRET field) and /devis-gravipack/;
- 'fabrication professionnelle, cadeaux d'entreprise et objets publicitaires' at /produit/fabrication-professionnelle-gravipack/, and an SNCF-branded key ring at /produit/porte-cle-flamme-personnalise-avec-logo-sncf-.../, both published as products;
- B2B selling points only inside product sheets ('tarifs dégressifs pour entreprises & administrations', collectivités on Centurion, AGEFIPH/FIPHFP funding on ExoTool).
No entreprises, CSE, QVT, collectivités, pompiers/secours or prévention TMS URL surfaced in two site-restricted searches (S7, S22).

<https://gravipack.com/devis/> · <https://gravipack.com/devis-gravipack/> · <https://gravipack.com/produit/fabrication-professionnelle-gravipack/> · <https://gravipack.com/produit/porte-cle-flamme-personnalise-avec-logo-sncf-broderie-premium-gravipack/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-porte-outils-exotool-gravipack/> · <https://www.gravipack.com/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/>

**Why it matters.** claude-seo local and plan guidance rates dedicated service pages as the #1 organic factor for service intent. The brand claims institutional buyers (army, RATP, police, gendarmerie, regions) and has a B2B team, but there is no page that can rank for 'sac à dos professionnel', 'équipement port de charge salariés', 'cadeau CSE personnalisé' or 'achat public'. Two quote pages split signals, and services sitting in the product catalogue confuse Merchant/Product schema and site taxonomy.

**SEO effect.** A hub-and-spoke /entreprises/ section would create rankable landing pages for high-value B2B queries that currently show zero visibility. It would consolidate quote-page equity and give PR and case studies a link target, raising lead volume per session.

**How to fix.** Build /entreprises/ with spokes for prévention TMS, maintenance/outillage, secours-santé, défense-sécurité, collectivités/achats publics, CSE/cadeaux personnalisés, and maintien dans l'emploi (only once verified); see the architecture table. 301-redirect /devis/ and /devis-gravipack/ to a single /entreprises/devis/. Move 'fabrication professionnelle' and the logo key rings out of /produit/ into a service page with Service schema, and 301 the old product URLs. Add the hub to the main navigation and footer. Track quote submissions as a GA4 conversion.

**Verifier notes.** A third site-restricted search (V4) again returned no /entreprises/, CSE, collectivités or B2B hub URL. It returned only /dossier-de-presse/, /produit/fabrication-professionnelle-gravipack/, the SNCF key-ring product and product sheets. The B2B copy lives inside product pages: 'adopted by more than 120 B2B and B2G clients', 'déployé dans entreprises et administrations pour prévenir les TMS et améliorer la QVT', prescription by doctors or occupational health, AGEFIPH/FIPHFP/MDPH/Escavie funding, and 'tarifs dégressifs' on Austerlitz. That confirms services are published as products and B2B intent is scattered. Severity drops to Medium for four reasons. Demand for the target queries ('cadeau CSE personnalisé', 'achat public') is unquantified, since there is no volume data. The site: operator is weak in this tool. The /devis/ and /devis-gravipack/ 'duplicate intent' is inferred from titles only. The rationale cites seo-local's 'dedicated service pages = #1 local organic factor', a Whitespark local-pack factor, for national B2B intent, which stretches the source.

### No presence in occupational prevention results (prévention TMS, médecine du travail, port de charges)

`b2b-absent-occupational-tms-serp` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** The results for 'Gravipack prévention TMS médecine du travail salariés' are 100% institutional: INRS PDFs (qr161, tc161, ED 6094, do16), the DREETS ARA TMS deck, Assemblée nationale written questions, the FNTR TMS Pros guide and the CRAMIF Préventica conference PDF. No Gravipack URL appears, even with the brand name in the query. Phase 1 saw the same pattern for 'sac à dos troubles musculo-squelettiques TMS travail' and 'exosquelette passif TMS'.

<https://www.inrs.fr/dms/inrs/CataloguePapier/DMT/TI-QR-161/qr161.pdf> · <https://auvergne-rhone-alpes.dreets.gouv.fr/sites/auvergne-rhone-alpes.dreets.gouv.fr/IMG/pdf/tms-web-2.pdf> · <https://www.cramif.fr/sites/default/files/inline-files/Preventica-presentation-conference-TMS-cramif-assurance-maladie-risques-professionnels_0.pdf> · <https://fntr.fr/sites/default/files/2021-04/Pre%CC%81vention%20des%20TMS%20avec%20TMS_Pros_09042021.pdf>

**Why it matters.** HSE managers, occupational physicians and CSE members research through informational queries before they ask for a quote. These are YMYL-adjacent topics where Google favours institutional sources. A brand page can only earn visibility with careful, sourced content that does not overclaim and positions the backpack as a complement to collective prevention, as the INRS hierarchy requires.

**SEO effect.** Sourced prevention guides would capture top-of-funnel B2B traffic and earn links from HSE and trade sites. They would also make the brand citable in AI answers about port de charges.

**How to fix.** Publish 3-5 guides: port de charges and TMS (cite INRS principles); choosing equipment for staff who walk with tools; how to fund equipment (TMS Pros, AGEFIPH/FIPHFP, only after verification). Have an ergonomist or occupational physician review them, show the reviewer, and avoid 'anti douleur' or medical claims. Link from the /entreprises/ spokes. Pitch the guides to OPPBTP, whose solution sheet already ranks for 'sac à dos porte-outils', and to occupational-safety media.

**Verifier notes.** The headline evidence is weak. The query 'Gravipack prévention TMS médecine du travail salariés' includes the brand name, and V4 shows that Gravipack product pages do contain TMS, QVT and occupational-health wording. Getting zero Gravipack results for that query is therefore an artefact of the WebSearch tool, not evidence of how Google.fr ranks. The generic phase-1 tests ('sac à dos TMS travail', 'exosquelette passif TMS') still support the claim of no presence. However, those results are 100% institutional (INRS, DREETS, CRAMIF, OSHA), so a vendor has little chance of ranking there, and the finding describes an opportunity, not a defect. The fix is sound on caution (reviewer, no medical claims, complement to collective prevention). One gap: OPPBTP's preventionbtp.fr 'solutions' database publishes company field cases. The better approach is to submit a documented case such as RATP track inspectors, not to pitch vendor guides.

### Segment hubs rank only with the 'anti mal de dos' modifier; outillage is the only exception (#9)

`segment-hubs-rank-only-with-brand-modifier` · On-Page SEO · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Extended-mode head-term tests:
- 'sac à dos porte-outils': the outillage hub ranks #9.
- 'sac à dos médical secouriste': absent (Girodmedical, SMSP, Praxisdienst).
- 'sac à dos ordinateur ergonomique': absent (mon-sac-a-dos, Eastpak, Darty, Ergonovie).
- 'sac à dos militaire tactique léger': absent (Projet13, Mode-Tactique, V8).
Phase 1 found the scolaire, claie and randonnée hubs absent for their generic terms. The hub slugs run 90-151 characters and titles stack 'exosquelette anti-mal de dos' instead of the market term.

<https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/> · <https://www.manomano.fr/cat/sac+a+dos+porte+outils> · <https://www.smsp.fr/c/materiel-intervention-secours/sac-premier-secours> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/sac-dos-ergonomique-etanche-ordinateur-gris/> · <https://www.mode-tactique.fr/444-sac-a-dos>

**Why it matters.** Head terms such as 'sac à dos porte-outils', 'sac à dos médical' and 'sac à dos tactique' carry most segment demand. Hubs written around the brand's own vocabulary only catch the narrow 'anti mal de dos' long tail. The outillage result shows that a hub with a clear professional use case can rank against big retailers.

**SEO effect.** Retargeting the hub titles, H1s and intro copy to market terms, with a use-case qualifier, could extend visibility from long-tail-only to head and mid-tail segment queries in médical, business, militaire and scolaire.

**How to fix.** For each hub: write the title as market term + use case + brand (e.g. 'Sac à dos d'intervention secouriste ergonomique | Gravipack'); write a 150-300-word intro answering buyer questions (volume, load, compartments); add an internal comparison table and FAQ block. Shorten slugs (e.g. /sacs-a-dos/secours/) with 301s. Link each hub from the matching /entreprises/ spoke. Copy the outillage pattern first to médical and militaire, where B2B intent overlaps.

**Verifier notes.** An extended-mode re-run of 'sac à dos porte-outils' (V5) reproduced the same top 9 in the same order, with the outillage hub at #9, so the result is stable. The hub's SERP title now reads 'Sac à dos exosquelette pour l'outillage professionnel Gravipack', a market-term title without 'anti mal de dos', which supports the finding's thesis. Caveats: the positions are WebSearch result order, not Google.fr rankings. 'Anti mal de dos' is a feature modifier, not a brand modifier, so the id is mislabelled. The médical, ordinateur and militaire absences rest on a single run each.

### RATP Group's independent mention is the best B2B proof but is not turned into a case study or a link

`ratp-proof-point-underleveraged` · Off-Page / Authority · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** ratpgroup.com's CSR page 'Innovation to improve the quality of working life for RATP Group staff' cites 'the exoskeleton backpack, developed by Gravipack, to alleviate the weight carried by staff in charge of infrastructure monitoring who walk along tracks'. ICI also has an article 'La RATP innove avec les exosquelettes' (undated). On gravipack.com the RATP story sits in two news posts, one of them titled after the VivaTech/Le Parisien coverage (phase 1). No /cas-clients/ or references page with the RATP use case surfaced (S7, S21, S22). Whether the RATP page links to gravipack.com is unknown.

<https://ratpgroup.com/en/heart-of-ratp-groups-csr-commitments/improve-quality-working-life-ratp-group-staff/> · <https://www.ici.fr/infos/transports/la-ratp-innove-avec-les-exosquelettes-5885238> · <https://www.ratp.fr/en/discover/coulisses/daily-life/exoskeletons-ratp>

**Why it matters.** An independent reference from a large public-transport operator is exactly the trust signal B2B buyers and AI engines need. It also partly answers the scepticism in UGC. It currently lives on RATP's site and in owned news posts, not in a structured case study that ranks for 'Gravipack RATP' or sector queries.

**SEO effect.** A case-study page citing RATP's own wording, plus a requested link from RATP's CSR page, would add a high-authority referring domain if granted. It would also give the entreprises hub a ranking proof asset and AI engines a verifiable fact.

**How to fix.** Merge the two owned RATP posts into one /cas-clients/ratp/ page with dates, context, a quote and an outbound link to the ratpgroup.com page (no exaggerated numbers). 301 the duplicate post. Ask RATP's CSR or innovation team to link 'Gravipack' to the case study or home page. Reuse the case in transport and HSE trade-press pitches.

**Verifier notes.** The evidence is stronger than the finding states. A search restricted to ratpgroup.com and ratp.fr (V10) found at least six RATP-owned URLs naming Gravipack:
- the FR and EN CSR pages;
- the VivaTech 2023 newsroom page and event page, which say close to 50 roaming maintenance workers already used it and that RATP planned to equip all track teams;
- the 'Cahiers d'expertise' innovation PDFs in FR and GB;
- an Askip' internal reportage;
- the 2024 ASDR page.
The ICI article (~early 2024) frames Gravipack at RATP as a project in progress. The VivaTech year behind the owned post is therefore 2023. The finding should list these as several link-reclamation targets, not 'the RATP page'. One accuracy issue: per phase-1 notes, the owned posts quote '250 agents equipped' (Le Parisien), while RATP itself says about 50 as of 2023. The case study must use RATP's dated figure. RATP also relays the brand's 92% figure, which is not an independent measurement.

### Military show participation and institutional-user claims appear only on undated owned posts

`military-show-claims-uncorroborated-undated` · Brand / Reputation · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Owned pages make these claims:
- /gravipack-soulage-les-forces-speciales-au-sofins/ (duplicated at /test/) and /gravipack-presentees-au-salon-militaire-techterre-combat-futur/, with the volume range stated as 20-100 L on one and 20-60 L on the other;
- the home page lists Armée de Terre, Légion étrangère, Préfecture de police, gendarmerie, pompiers and régions/départements as users;
- a founder LinkedIn post says the brand was 'invité d'honneur' at two military shows with 57 delegations.
No third-party page confirms SOFINS, Techterre or the honoured-guest claim (S3, S9, S16), and none of the posts shows a date in results.

<https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/test/> · <https://www.gravipack.com/gravipack-presentees-au-salon-militaire-techterre-combat-futur/> · <https://www.linkedin.com/in/errafi/> · <https://www.challenge.ma/?p=271181>

**Why it matters.** Institutional endorsements that cannot be checked weaken the Trust part of E-E-A-T. They can also backfire with defence and public buyers, who check references. Undated news also sends no freshness signal.

**SEO effect.** Dated, evidenced show reports (NewsArticle with datePublished, organiser links, photos) turn claims into freshness and trust signals and earn links from organisers and defence media. Removing the /test/ duplicate also removes index bloat.

**How to fix.** Add a visible publication date and NewsArticle/BlogPosting schema with datePublished and dateModified to every news post. Link to the organiser's exhibitor page and add photos from the stand. Settle on one capacity range. Remove or soften institutional-user logos unless a written reference exists. 301 /test/ to the SOFINS post. Ask show organisers for exhibitor-directory listings with a website link.

**Verifier notes.** The show claims are still uncorroborated. A search for 'salon Techterre "Combat Futur" exposants' (V6) found no trace of such a show at all, only noise and the Eurosatory 2026 MoD page. The finding's broader claim, that 'institutional-user claims appear only on owned posts', is partly wrong. RATP documents Gravipack itself (V10), and army testing plus the 2018 MoD innovation silver are relayed by Maddyness, Neozone, Europe 1 and challenge.ma (founder-sourced, but third-party). Phase-1 notes describe a dated blog (/articles/, 2022-2025), so 'undated' only applies to SERP snippets. The '20-100 L vs 20-60 L' inconsistency may refer to different products (Barracuda claie vs backpacks) and needs a page check. The trust impact is real but small; Low.

### No 'où acheter' or store-locator page; a 2021 forum owns the where-to-buy intent

`local-no-store-locator-where-to-buy` · Local SEO · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** The site-restricted search for revendeurs / points de vente / magasins partenaires / distributeurs returned no store locator, only the CGV, legal notice, /nos-clients/, /devis-gravipack/ and an owned post 'bientôt en magasin' that names no store. The open-web 'où acheter Gravipack magasin revendeur point de vente' results are all randonner-leger 2021 posts saying the bags were on Decathlon's site 'mais pas en magasin', 'Vendu et expédié par GRAVIPACK', 'juste market place'. Historical stockists per the ICI/JDG summaries: Décathlon, Nature & Découvertes, Au Vieux Campeur (Paris). The current Decathlon seller is KID'ABORD. A Paris showroom appears only as a KKBB promise.

<https://gravipack.com/gravipack-bientot-en-magasin-linnovation-en-apesanteur-prend-son-envol/> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626059> · <https://www.randonner-leger.org/forum/viewtopic.php?pid=626080> · <https://www.decathlon.fr/vc/gravipack> · <https://www.kisskissbankbank.com/en/projects/gravipack/tabs/faqs> · <https://www.ici.fr/infos/economie-social/la-nouvelle-eco-le-cartable-revolutionnaire-de-la-societe-gravipack-a-sens-fait-un-carton-1599115911>

**Why it matters.** Buyers who want to try a 'try-before-you-buy' ergonomic product on before buying search for where to buy it. Outdated UGC answers that query instead of the brand. Under claude-seo seo-local, a store locator with crawlable stockist URLs is the standard for brands sold through third-party stores.

**SEO effect.** An official 'Où acheter Gravipack' page would take over the where-to-buy query and add a link target for retailers. Verified stockist listings could also feed Google's local inventory and in-store features for retailers.

**How to fix.** Create /ou-acheter/ listing verified online channels (official store, Decathlon marketplace, others) and physical stockists with addresses, only after confirming each stock point. Use crawlable HTML, not a JS-only map. Do not add LocalBusiness schema for stores the brand does not operate; link to the retailer's store page instead. Update or unpublish the 'bientôt en magasin' post. If a showroom opens, create its own location page.

**Verifier notes.** The absence of a where-to-buy page is consistent across S11 and S21 (no new search spent). The rationale misattributes the toolkit. In seo-local SKILL.md, 'Store locator with individual crawlable URLs' sits under 'Multi-location specific', meaning a business's own locations, not a stockist list for a brand sold by third parties. The seo_effect claim that stockist listings 'could feed Google's local inventory and in-store features' is also wrong: local inventory requires the retailer's own Merchant Center feed, so the brand cannot supply it. The brand is online-first, demand for 'où acheter gravipack' is likely tiny, and impact_score 4 fits Low better than Medium. A simple 'Où acheter' page listing the official store, the Decathlon marketplace, Fnac and Au Vieux Campeur is still worthwhile.

### Local citations point to an old Vincennes 'Maroquinerie' listing with 0 reviews, while the legal seat is now Paris

`local-citations-outdated-nap` · Local SEO · auditor severity **Low** → verifier **confirmed**, severity **Low**

**Evidence.** Sibling phase-2 searches surfaced PagesJaunes 'Gravipack à Vincennes - Maroquinerie' (0 reviews) and a Mappy POI at 46 r Bienfaisance 94300 Vincennes. The sibling registry log reports the EXOSQUELETTE LIGHT head office in Paris 75002 since 19/05/2026. The CGV I saw name SAS EXOSQUELETTE LIGHT as the seller. The contact page publishes a mobile number (+33 6 66 20 52 49) and contact@gravipack.com. 'Gravipack Vincennes adresse téléphone' returned no listing (sibling S28). A GBP cannot be observed with WebSearch.

<https://www.pagesjaunes.fr/pros/60790927> · <https://fr.mappy.com/poi/605d2e7de32c7c1ed765382d> · <https://gravipack.com/conditions-generales-de-vente/> · <https://gravipack.com/contact-gravipack/> · <https://gravipack.com/mentions-legales/>

**Why it matters.** Gravipack is an online brand without a public storefront, so the local pack matters little. But NAP consistency still feeds entity trust and AI answers: claude-seo notes that 3 of the top 5 AI visibility factors are citation-related, and Bing Places feeds ChatGPT and Copilot. An outdated 'Maroquinerie' category also mislabels the business.

**SEO effect.** Consistent NAP across PJ, Mappy, Bing Places, Apple Business Connect and the site's Organization schema reduces entity confusion. It also stops directories showing a stale address.

**How to fix.** Decide the public contact address (Paris head office, or a service-area business with a hidden address). Update or close the PJ and Mappy listings, change the category to sac à dos / équipement ergonomique, and claim Bing Places and Apple Business Connect. Add Organization schema with legalName EXOSQUELETTE LIGHT, address and sameAs. Only create a GBP if there is a staffed showroom or service area, following Google eligibility rules.

**Verifier notes.** The entity verify (V9) confirmed the Paris seat at 10 rue de la Paix, 75002, since 19/05/2026 through societe.com, pappers and annuaire-entreprises. PJ 60790927 and the Mappy POI at Vincennes are sibling-observed. The finding omits sibling reputation-verify V5: an aggregator (groupe-ranque.fr/gravipack) reports 'Gravipack, Vincennes, 4.7/5 from 998 Google My Business reviews', and a third-party blog reports 4.8 from 900+ Google reviews. Phase 1 had labelled groupe-ranque a homonym, so this is contested, but a GBP probably exists. If it does, it is the most important NAP surface. 'A GBP cannot be observed' should become 'a GBP likely exists (unverified); locate and update it first'.

### Owned news has no visible dates, and 2026 pre-order copy is likely to go stale

`owned-freshness-undated-stale-preorders` · Content Quality · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** A site-restricted search for 2025/2026 surfaced pre-order statements: Tokyo 'premières expéditions à partir de mi-septembre 2026', Business Talk V4 20L 'disponibilité en juin 2026', and the Barracuda claie 'livraison à partir de mi-novembre 2026'. It also surfaced news posts (/actualites-gravipack-2/, SOFINS, Techterre, 'bientôt en magasin') whose publication dates the results summaries could not determine. On the audit date (2026-10-12) the Tokyo and Business Talk V4 dates are already past.

<https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://www.gravipack.com/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/> · <https://gravipack.com/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/> · <https://www.gravipack.com/actualites-gravipack-2/>

**Why it matters.** Past-due pre-order promises in snippets hurt click-through and trust, and they conflict with Merchant Center availability. Undated news gives neither users nor search engines a freshness signal.

**SEO effect.** Up-to-date availability (Offer.availability, plus availabilityStarts for pre-orders) and dated news improve snippet accuracy and give a small freshness and trust gain.

**How to fix.** Check the product pages. Replace pre-order text with current stock status once shipped, and keep Product schema availability in sync. Show the publication date on every news post and include datePublished/dateModified in Article schema. Rename /actualites-gravipack-2/ to /actualites/ with a 301.

**Verifier notes.** The title claims 'owned news has no visible dates', but phase-1 offsite.json what_works records 'A dated blog (/articles/, 2022-2025) with thematic categories'. So at least the blog has dates, and the evidence only shows that SERP snippets lacked them. The pre-order staleness logic holds: Tokyo 'mid-Sept 2026' and Business Talk V4 'June 2026' are both past as of 2026-10-12. Snippets may be cached, though, so 'needs-on-site-check' is the right confidence. No search was spent.

### B2B facts conflict across pages (minimum order, capacity range, funding claims)

`b2b-inconsistent-facts` · Content Quality · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** The custom-logo key ring shows a minimum order of 20 units on one product sheet and 30 on another. Capacity is '20 à 100 litres' on the Techterre post and '20 à 60 litres' on the SOFINS post. ExoTool says the product 'peut être financé par l'AGEFIPH / FIPHFP' in job-retention cases, with no supporting reference found.

<https://gravipack.com/produit/porte-cle-flamme-personnalise-avec-logo-sncf-broderie-premium-gravipack/> · <https://www.gravipack.com/produit/porte-cle-flamme-personnalise-sur-mesure-avec-votre-logo-broderie-premium-gravipack/> · <https://www.gravipack.com/gravipack-presentees-au-salon-militaire-techterre-combat-futur/> · <https://www.gravipack.com/gravipack-soulage-les-forces-speciales-au-sofins/> · <https://www.gravipack.com/produit/sac-anti-mal-de-dos-exosquelette-porte-outils-exotool-gravipack/>

**Why it matters.** B2B and public buyers compare specifications and funding eligibility closely. Conflicting numbers and unsourced funding claims weaken trust and can lead AI summaries to repeat wrong facts.

**SEO effect.** A single source of truth on each B2B spoke page gives consistent facts that AI engines and buyers can cite. Fewer unsupported claims lowers the risk of misrepresentation reviews.

**How to fix.** Set one MOQ per product. Publish one capacity range per model family. Confirm AGEFIPH/FIPHFP eligibility with the agencies (or a written case) before mentioning it, cite the source, or remove the claim.

**Verifier notes.** The MOQ conflict is confirmed: V4 shows 30 units on one key-ring sheet, and S7 had 20 on the other. The capacity 'conflict' (20-100 L on the Techterre post vs 20-60 L on the SOFINS post) may describe different product families, since one post presents the Barracuda claie, so it needs a page check before being called an inconsistency. The AGEFIPH/FIPHFP claim is not inherently unsupported: both bodies fund individual workplace-adaptation equipment for workers with recognised disabilities, case by case (general knowledge, not searched). The product pages also name MDPH and Escavie (V4). The issue is imprecise wording, not a fabricated claim; the fix should be 'reword and source precisely', not 'remove'.
