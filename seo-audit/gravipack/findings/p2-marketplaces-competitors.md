# Phase 2 — marketplaces-competitors

Searches run: 28

## Evidence base

I ran 28 WebSearch calls against a cap of 40, then stopped to save the shared budget. The tool uses a US-located index, not google.fr. Before searching I read the phase-1 notes (serp-notes.md E1-E12, tables.md, offsite.json) and the two parallel phase-2 logs (reputation-social-brand-serp.md and entity-legal-claims.md), so I did not repeat their queries. The raw log is in /tmp/claude-0/-home-user-soufian/f48d95be-0ad3-5e07-bab2-7b53bc671068/scratchpad/phase2/marketplaces-competitors.md (M1-M28).

CHANNELS. Gravipack sells through many channels that do not match each other:
- Decathlon.fr marketplace. The seller is KID'ABORD for Sherpa 45, Hiking 33 and Feather.
- Nature & Découvertes marketplace. KID'ABORD sells some listings. Gravipack bags sit under 'sacs-a-dos-velo' (bike backpacks).
- Au Vieux Campeur.
- Fnac. Most models are out of stock, and URLs with junk tracking parameters are indexed.
- Kiabi marketplace. SERP titles show '0.00€' or 'nu€'.
- Ergo-Corner. Full catalogue with strap sizes M/L/XL/XXL.
- Équilibre France Ergonomie, Bureau Vallée (Pearl, click & collect), prosportequip, the comparison site 123comparer, and a rental listing on planete-rando.
- Brand-run sites: the legacy presta.gravipack.com and a separate EUR store on gravipack.ma (different model names, 'boutique en préparation').

NOT FOUND:
- Amazon.fr: 2 searches. The only hit is a customer review on a Kipling bag that mentions Gravipack.
- Cdiscount: its /r-gravipack.html internal search page returns look-alike products, not Gravipack.
- Rakuten, ManoMano, eBay.fr: 1 search.
- Pharmacies, orthopaedic shops, osteopaths: 1 search.

PRICES. Prices vary widely across channels and even within gravipack.com:
- Sherpa 45 runs from 89.10 (Ergo-Corner) to 249 (Au Vieux Campeur and Nature & Découvertes list price). The official site shows 99, 119 and 149.90.
- Hiking 33/30 runs from 89 (official) to 229 (Au Vieux Campeur).
- G-Pack costs 69.20 at Ergo-Corner against 89.90 official.
- Tokyo costs 109.90 at Ergo-Corner against 129 or 189 official.
- Oslo 60+10 at 289 was only seen on the official site.
- Feather is not on the main store. The legacy presta store still shows it at 149 and 'in stock', while marketplaces sell it for 90-127.

MODEL QUERIES (extended mode). Third parties outrank gravipack.com:
- 'gravipack sherpa': first owned result at #6.
- 'gravipack hiking 33': legacy presta at #8, main store at #9.
- 'gravipack feather': main store absent; only presta at #10.
- 'gravipack business talk': first owned result at #7.
- 'gravipack oslo 60+10' is the exception: owned results at #2-#4.

HEAD TERMS. gravipack.com is absent for 'sac à dos randonnée ergonomique', 'sac à dos ordinateur ergonomique', 'sac à dos ergonomique' and 'cartable ergonomique'. It is also missing from every comparison or 'best of' article seen: Toporando, Snowleader, Glisshop, Hardloop, Ridepark, Clubic, TechRadar, Accergo, Norveya, Avis-Parents, Futura-Sciences, Meilleurs.fr. Those articles list Osprey, Deuter, Gregory, Millet, Mammut, ergobag, Satch, Tann's, Baagl, Eastpak and Case Logic. Shops selling generic 'ergonomic' bags (mon-sac-a-dos.fr, ma-boutique-ergonomique.com, karkoa.com) hold the generic 'ergonomique' results.

COMPARISON CONTENT. No 'Gravipack vs X' page and no 'alternative à Gravipack' page exists anywhere in the results.

SIGNAL-ARNAQUES. The two parallel agents ran 6+ queries on this. Report #947856 was never indexed and no signal-arnaques report names Gravipack, so the result cannot be attributed to the brand.

LIMITS. Prices come from search snippets whose capture dates are unknown, so treat them as a snapshot. Google Shopping, free listings, on-site schema and Merchant Center status cannot be seen through WebSearch, so they are marked needs-on-site-check.

## Questions resolved

### [resolved] Where is Gravipack sold (Decathlon marketplace and seller name; Amazon.fr; Cdiscount; Fnac; Rakuten; ManoMano; Ergo-Corner and other resellers; pharmacies or orthopaedic shops)?

FOUND:
- Decathlon.fr marketplace. Sherpa 45 and Hiking 33 are 'vendus et expédiés par KID'ABORD' (M9). A Feather bordeaux listing is also sold by KID'ABORD (entity log #31). An older forum post said the seller was 'GRAVIPACK'.
- Nature & Découvertes marketplace. KID'ABORD sells Feather Plus and Hiking Terracota.
- Au Vieux Campeur: Feather, Hiking 33, Sherpa 45 and Business Talk, including an ipad. host duplicate.
- Fnac: brand page m568883, Hiking 33 (3 colours), Feather Plus, Business Talk, Road Adventure and Safar Vibe. Most are out of stock.
- Kiabi marketplace: Feather, Feather Plus, Sherpa 45 kaki, Pearl Gray, and Hiking 33 (unavailable).
- Ergo-Corner: City, Hiking 30L, Light Promax, Kingston, Tokyo, G-Pack, Sherpa 45 (3 colours), Austerlitz and Oslo 70L.
- Others: Équilibre France Ergonomie (Hiking 33, Business Talk), Bureau Vallée (Pearl, click & collect), prosportequip.com (Hiking 33), 123comparer.fr (Feather Noir) and location.planete-rando.fr (Oslo rental).
- Brand-run: the legacy presta.gravipack.com and gravipack.ma.

NOT FOUND:
- Amazon.fr: 2 searches. The only hit is a customer review on a Kipling bag.
- Cdiscount: /r-gravipack.html is an internal search page that shows look-alikes such as Pacsafe 'Gravity Gray'.
- Rakuten, ManoMano, eBay.fr: 1 search.
- Pharmacy, orthopaedic or osteopath channel: 1 search. The only related claim is the inventor's statement in challenge.ma that occupational doctors can prescribe the bag.

<https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · <https://www.natureetdecouvertes.com/v/sac-a-dos-gravipack> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-sherpa-45.html> · <https://www.fnac.com/Gravipack/m568883/w-4> · <https://www.kiabi.com/sac-a-dos-gravipack-sherpa-45-kaki-kaki_P1443012C1443014> · <https://www.ergo-corner.com/gravipack/677-sherpa-45l-bleu-sac-a-dos-avec-exosquelette-gravipack.html> · <https://equilibre-france-ergonomie.fr/produits/sac-a-dos-hiking-33-baroudeur-et-leger/> · <https://www.bureau-vallee.fr/gravipack-sac-a-dos-pearl-29-litres-gris-405222788.html> · <https://www.cdiscount.com/bagages/r-gravipack.html> · <https://www.amazon.fr/Kipling-Seoul-Grand-Protection-Ordinateur/dp/B0B5RY3DDZ> · <https://gravipack.ma/> · <https://www.challenge.ma/?p=271181>

### [resolved] Price parity: marketplace and reseller prices compared with gravipack.com (e.g. Oslo 60+10L €289)

There is no price parity. All prices are in EUR, as shown in snippets on 2026-10-12.
- Sherpa 45: official 119 (bleu, struck price 249), 149.90 (orange, kaki) and 99 (orange in a promo list). Decathlon/KID'ABORD 149.90 (struck price 249; promo 18/06-30/08/2026, now ended). Nature & Découvertes 149 orange, about 249 bleu/kaki. Au Vieux Campeur 174.30-249. Ergo-Corner 89.10 or 149.90. Range 89.10-249, about 2.8x.
- Hiking 33/30: official 89-89.90 (list price 229 or 129.90). Decathlon 129.90 (reference 229). Nature & Découvertes 129 (was 229). Au Vieux Campeur 160.30-229. Ergo-Corner 89.10 (out of stock).
- Feather: not sold on the main store. Legacy presta 149 'in stock'. Decathlon 90. Nature & Découvertes 119 (was 149). Au Vieux Campeur 111.30-127.20 (reference 159). Kiabi displays 0.00€. Feather Plus is 99 at Decathlon and Nature & Découvertes.
- G-Pack: official 89.90, Ergo-Corner 69.20 (23% lower).
- Tokyo: official 189 or 129 (was 249), Ergo-Corner 109.90.
- Business Talk: official 129 (was 149), Au Vieux Campeur 139.30 (reference 199).
- Austerlitz: official 89.90, Ergo-Corner 99.90.
- City: 129.90 both on the official site and at Ergo-Corner (parity).
- Oslo 60+10: 289 seen only on the official site. Ergo-Corner lists it, but no price appeared in the snippet.

<https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://gravipack.com/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-feather-bordeaux-gravipack-97350110> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-ville-feather.html> · <https://www.ergo-corner.com/gravipack/672-g-pack-20l-noir-sac-a-dos-business-gravipack.html> · <https://www.ergo-corner.com/gravipack/738-sac-tokyo-avec-exosquelette-gravipack.html> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-ville-business-talk.html>

### [resolved] Do marketplace or reseller pages outrank gravipack.com for model queries ('gravipack sherpa', 'gravipack hiking', 'gravipack feather', 'gravipack oslo')?

Yes, for 4 of the 5 models tested (extended mode):
- 'gravipack sherpa': KissKissBankBank x2, Trustpilot, Nature & Découvertes and Au Vieux Campeur hold #1-#5. The first gravipack.com result is #6.
- 'gravipack hiking 33': KissKissBankBank, Fnac x3 (tracking-parameter URLs), Decathlon, Équilibre and Nature & Découvertes come first. The legacy presta is #8 and the main store #9.
- 'gravipack feather cartable': the main store is absent. Au Vieux Campeur, Nature & Découvertes x4, Fnac, Kiabi x2 and KissKissBankBank rank, and presta is #10.
- 'gravipack business talk': the first owned result is #7, after KissKissBankBank x2, Au Vieux Campeur, YouTube x2 and Équilibre.
- 'gravipack oslo 60+10': owned results hold #2-#4 behind the i-trekkings test. This is the only model the official site wins.

<https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-sherpa-orange-gravipack-97350080> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-sherpa-45.html> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Cooper/a16809926/w-4?m=a750bda958&h=gig&bo=48737913&piddl=836768> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://www.kiabi.com/sac-a-dos-gravipack-feather-plus-bleu-bleu-marine_P1459556C1459557> · <https://equilibre-france-ergonomie.fr/produits/sac-a-dos-business-talk-gravipack/> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/>

### [resolved] Which brands, retailers and comparison or 'best of' pages win the head terms, and are competitors listed where Gravipack is not?

- 'sac à dos randonnée ergonomique': Glisshop x2, Cdiscount, Rayonrando, Ridepark, Toporando, Hardloop, mon-sac-a-dos and Millet. These pages name Osprey, Deuter, Gregory, Millet and Mammut.
- 'sac à dos ordinateur ergonomique': mon-sac-a-dos x2, sac-a-dos-france, Eastpak, Darty, Karkoa, the Accergo list article, ma-boutique-ergonomique and Ergonovie.
- 'meilleur cartable ergonomique 2026': Futura-Sciences, Avis-Parents x2, meilleurs.fr, lemeilleuravis and others. These list ergobag Prime, Satch, Tann's, Baagl and Eastpak.
- 'meilleur sac à dos ergonomique comparatif 2026': Snowleader, Toporando, Clubic and TechRadar.
- Phase-1 results for 'sac à dos ergonomique' and 'cartable ergonomique' show Gravipack absent there too.
- Gravipack, as a brand or a product, does not appear in any comparison or 'best of' article seen.

<https://toporando.fr/meilleurs-sacs-a-dos-randonnee-trekking/> · <https://blog.snowleader.com/top-10-sac-a-dos-randonnee/> · <https://www.glisshop.com/conseils/les-meilleurs-sacs-a-dos-de-randonnee.html> · <https://www.hardloop.fr/article/les-15-meilleurs-sacs-a-dos-de-randonnee-et-trekking> · <https://www.clubic.com/materiel-informatique/article-852462-1-meilleur-sac-a-dos-ordinateur-portable-comparatif.html> · <https://www.accergo.fr/meilleurs-sacs-a-dos-ergonomiques/> · <https://norveya.com/blogs/organisation/les-meilleurs-sacs-a-dos-ergonomiques-contre-le-mal-de-dos> · <https://www.avis-parents.com/tests-avis/meilleur-cartable-primaire/> · <https://www.futura-sciences.com/conso/comparatifs/meilleur-cartable-comparatif/> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/>

### [partially-resolved] Is the signal-arnaques.com page (scam/view/947856) that appeared for 'Gravipack avis Trustpilot' actually about Gravipack?

It cannot be attributed to Gravipack, and the page was never seen directly. I spent no searches on this. The two parallel agents covered it this turn with 6+ searches: S6, S12, S15 and S22 in the reputation log, and #20, #21, #27 and #29 in the entity log. ID 947856 never appeared in any result. A repeat of the phase-1 query 'Gravipack avis Trustpilot' did not return signal-arnaques at all. Signal-arnaques reports titled 'Trustpilot' or 'fr.trustpilot.com' exist (e.g. scam/view/708821), but none names Gravipack. The most likely explanation is that the result matched on the keyword 'Trustpilot'. It should not be reported as a scam report against Gravipack.

<https://www.signal-arnaques.com/scam/view/947856> · <https://es.trustpilot.com/review/gravipack.com>

### [unresolved] Is Gravipack present in Google Merchant Center free listings or Shopping, and does gravipack.com carry Product/Offer/AggregateRating/MerchantReturnPolicy/ShippingDetails markup?

This cannot be checked with WebSearch. Shopping units are not exposed, and the network policy blocks gravipack.com. What the evidence does show: one model has 2-3 different prices across gravipack.com pages, and product pages show a first-party 'Avis Google 4,7 (1121-1175 avis)' widget that no third party corroborates (reputation log S27). Both are risks for merchant listings. Verify on-site with the Rich Results Test and Merchant Center diagnostics.

<https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://gravipack.com/boutique-gravipack/>

## What works

- Wide distribution through respected French retailers gives the brand legitimacy and many indexed product pages. Seen: Decathlon marketplace, Nature & Découvertes, Au Vieux Campeur, Fnac, Kiabi, Bureau Vallée, Ergo-Corner and Équilibre France Ergonomie.
- The official store wins its own model query for Oslo 60+10 (owned #2-#4, behind an independent i-trekkings test). Phase-2 S5 shows gravipack.com holding 8 of 9 results for 'gravipack exosquelette'.
- decathlon.fr/vc/gravipack ranks #1 for the head term 'sac à dos anti mal de dos' (phase-1 standard mode) and even for the competitor query 'Bodypack sac à dos ergonomique anti mal de dos' (M28). Decathlon's authority puts the brand on queries gravipack.com cannot yet win.
- Ergo-Corner is an active reseller. It publishes a brand article (content/13-le-sac-a-dos-gravipack) and a brand category, which reach the top of 'meilleur sac à dos anti mal de dos'. Its titles expose a real differentiator, strap sizes M/L/XL/XXL.
- Gravipack occupies a unique niche (an 'exosquelette' in the shoulder straps). No competitor, comparison article or marketplace targets 'sac à dos exosquelette', and no hostile 'Gravipack vs X' page exists. The comparison space is open for the brand to define fairly.
- City 20L is priced the same (129.90) on gravipack.com and Ergo-Corner, which shows parity is achievable.

## Raw findings (with verifier verdicts)

### Marketplaces, resellers and old crowdfunding pages outrank gravipack.com for its own model queries (Sherpa, Hiking 33, Feather, Business Talk)

`mc-model-serp-ceded` · E-commerce · auditor severity **High** → verifier **confirmed**, severity **High**

**Evidence.** Extended-mode searches:
- 'gravipack sherpa': first owned URL at #6, behind KKBB x2, Trustpilot, Nature & Découvertes and Au Vieux Campeur.
- 'gravipack hiking 33': legacy presta at #8, main store at #9, behind KKBB, 3 Fnac URLs with junk tracking parameters, Decathlon, Équilibre and Nature & Découvertes.
- 'gravipack feather cartable': main store absent from the top 10. Only presta at #10, behind Au Vieux Campeur, Nature & Découvertes x4, Fnac and Kiabi x2.
- 'gravipack business talk': first owned URL at #7.
- Only 'gravipack oslo 60+10' is won by the official site (#2-#4).
- For generic head terms, the reseller Ergo-Corner's brand category and article rank above gravipack.com for 'meilleur sac à dos anti mal de dos' (phase-1 E8).
- decathlon.fr/vc/gravipack ranked #1 for 'sac à dos anti mal de dos' in standard mode while gravipack.com was absent.

<https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-sherpa-orange-gravipack-97350080> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-sherpa-45.html> · <https://gravipack.com/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Gris/a16809921/w-4?gadzoo=99e3cb200c&quibbl=5590b4de&mum=0376dacb> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/_/R-p-093a557b-159a-4282-95a8-76495a70d99e> · <https://presta.gravipack.com/accueil/16-sac-a-dos-gravipack-hikking33.html> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-ville-business-talk.html> · <https://www.kisskissbankbank.com/en/projects/gravipack> · <https://www.decathlon.fr/vc/gravipack>

**Why it matters.** Brand-plus-model searches are the highest-intent, highest-margin traffic. When they land on a marketplace, Gravipack loses the margin, the customer data and control of the message. These include marketplace listings sold by a third-party licensee and Fnac pages that are mostly out of stock.

**SEO effect.** Reclaiming #1 for every 'gravipack <modèle>' query recovers direct-sale clicks. It also concentrates links and engagement on official URLs that can carry Product rich results, and it reduces how often out-of-stock third-party pages appear for the brand.

**How to fix.** 1. Give each model exactly one canonical official URL, with colours as variants rather than separate URLs. Use a short model-first title, e.g. 'Gravipack Sherpa 45 – sac de randonnée 45 L à exosquelette | Gravipack'. Put the model name in the H1 and the slug, e.g. /produit/sherpa-45/.
2. Put Feather and Feather Plus back on gravipack.com, or redirect them to a successor page.
3. 301-redirect every presta.gravipack.com product to the matching official URL (Hiking 33 → Hiking, Feather → Feather, Business Talk → Business Talk V4), then remove the subdomain.
4. Ask KissKissBankBank to add 'Projet terminé – boutique officielle : gravipack.com/…' with a link on the old campaign pages.
5. Ask resellers (Ergo-Corner, Équilibre, Au Vieux Campeur) to link each product to the matching official page, e.g. 'fiche officielle', and to use the same model names.
6. Link model pages from the home page and the category hubs using anchors that contain the model name.

**Verifier notes.** Re-ran 2 queries in extended mode and both reproduced the pattern.
- V1 'gravipack sherpa': KKBB, Trustpilot, KKBB, Decathlon Sherpa 45 (new), N&D Sherpa bleu and Au Vieux Campeur hold #1-#6. The first gravipack.com URL is now #7 (was #6).
- V2 'gravipack hiking 33': decathlon vc/gravipack is #1, then KKBB, Fnac x3, Decathlon PDP, Équilibre and N&D. Legacy presta is #9 and the main store is now ABSENT from the top 10 (was #9).

Caveats to state in the report:
(a) WebSearch is a US-located, non-Google index, and reputation-verify V7 showed brand SERPs are volatile between runs, so the positions are indicative.
(b) The KKBB pages are the brand's own crowdfunding campaigns (4, not 2), not a competitor.
(c) Part of Decathlon is brand-sold: Business Talk and one Feather offer are 'Vendu et expédié par GRAVIPACK' (V7). Other offers come from a licensee, so 'loses the margin' is only partly true.
(d) The official model name is 'Hiking 30L / Terracotta' while retailers say 'Hiking 33', so naming is part of the cause. Add retailer names as aliases on the page.
(e) 'decathlon vc/gravipack #1 for sac à dos anti mal de dos' holds only in standard mode. In extended mode (E1), gravipack.com is at #4-#6 and Decathlon is absent.

Fix issues:
- Step 3 'then remove the subdomain' would kill the 301s. The presta vhost must keep serving redirects (at least 1 year, ideally permanently), with 410 or the nearest category for discontinued models.
- Step 4: KKBB support is winding down (it redirects to Ulule). The creator can post a final news update with the link on all 4 campaign pages.

### No price parity: the same model ranges from 2.6x to 2.8x in price across channels and has 2-3 prices on gravipack.com itself

`mc-price-parity` · E-commerce · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Prices as shown in search snippets on 2026-10-12. The snippets' capture dates are unknown.
- Sherpa 45: gravipack.com 119 (bleu, struck price 249), 149.90 (orange/kaki) and 99 (orange in a promo list). Decathlon/KID'ABORD 149.90 (struck price 249; the promo '18/06/2026-30/08/2026' has ended). Nature & Découvertes 149 or about 249. Au Vieux Campeur 174.30-249. Ergo-Corner 89.10 or 149.90.
- Hiking: official 89-89.90 against Decathlon 129.90 (reference 229), Nature & Découvertes 129 (reference 229) and Au Vieux Campeur up to 229.
- G-Pack: Ergo-Corner 69.20 against official 89.90.
- Tokyo: Ergo-Corner 109.90 against official 189 or 129 (was 249).
- Feather: the legacy presta store shows 149 'in stock'; marketplaces sell it for 90-127.
- Struck-through reference prices of 229 and 249 appear on almost every channel.
- A Decathlon reviewer calls the promo price 'mensonger' (misleading) (reputation log S17).

<https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/> · <https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.decathlon.fr/r/mp/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/093a557b-159a-4282-95a8-76495a70d99e/c5> · <https://www.natureetdecouvertes.com/v/sac-a-dos-gravipack> · <https://www.auvieuxcampeur.fr/sac-a-dos-de-randonnee-hiking-33.html> · <https://www.ergo-corner.com/gravipack/675-sherpa-45l-orange-avec-exosquelette-gravipack-.html> · <https://www.ergo-corner.com/gravipack/672-g-pack-20l-noir-sac-a-dos-business-gravipack.html> · <https://www.ergo-corner.com/gravipack/738-sac-tokyo-avec-exosquelette-gravipack.html> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://presta.gravipack.com/accueil/21-sac-a-dos-gravipack-feather.html>

**Why it matters.** Google merchant listings and free listings disapprove offers whose feed or structured-data price does not match the landing page. When several sellers offer the same product, the cheapest offer, often a reseller's, wins the Shopping click. A permanent 'was 249' price is also a consumer-law risk: in France, a price-reduction announcement must reference the lowest price of the previous 30 days (Code de la consommation art. L112-1-1). Visible price swings feed the 'arnaque' narrative already present in brand results.

**SEO effect.** One consistent price per model makes the store eligible for merchant listings and free listings with price and promo annotations. It stops resellers from taking Shopping clicks on price alone and lowers the trust friction that hurts CTR on brand results.

**How to fix.** 1. Fix the official store first. Set one live price per model and colour. Remove stale promo lists. Show struck prices only during real, dated promotions, with the 30-day lowest price as the reference, and mark them up with priceValidUntil.
2. Publish a recommended retail price (prix de vente conseillé) list and a promo calendar for partners. Do not impose minimum resale prices on independent resellers: that is unlawful in France (Code de commerce art. L442-5). Use the licence agreement with KID'ABORD and the reseller agreements only within competition-law limits, and get legal advice.
3. Ask Ergo-Corner to align its displayed prices with the recommended prices where it agrees, or accept the gap knowingly.
4. Re-check monthly with a price snapshot of Decathlon, Nature & Découvertes, Au Vieux Campeur, Fnac and Ergo-Corner.

**Verifier notes.** The '2.6x-2.8x' spread mixes struck or reference prices (229/249) and stale prices with live selling prices.
- V9: on Ergo-Corner, Sherpa bleu and orange are 149.90. The 89.10 figure appears only on the kaki page marked 'rupture de stock' and in 'vous pourriez aussi aimer' thumbnails.
- Live Sherpa offers cluster at 149-149.90 (official orange/kaki, Decathlon, N&D orange, Ergo-Corner). Outliers are 119 (official bleu) and 174.30 (Au Vieux Campeur). That is about 1.5x, not 2.8x.
- The real issues are struck reference prices on almost every channel and 2-3 prices per model on gravipack.com.

New, stronger evidence (V7): the brand's OWN Decathlon seller account lists Business Talk at 199 against 129 (was 149) on gravipack.com. On the same marketplace, Feather is offered at 149 by GRAVIPACK and at 90 by KID'ABORD.

why_it_matters overreaches. Merchant Center disapprovals come from a mismatch between a merchant's own feed and its landing page or schema. Price differences between different sellers do not cause them. The 'cheapest reseller wins the click' point is speculation.

Fix issues:
- The minimum-resale-price ban is Code de commerce art. L442-6 since ordonnance 2019-359, not L442-5 (now revente à perte). It is also a hardcore restriction under Reg. 2022/720.
- 'priceValidUntil' is not the current way to mark up promos. Google merchant listings use a second priceSpecification with priceType StrikethroughPrice, plus validFrom/validThrough for the sale period.

### gravipack.com is absent from the head terms and from every comparison article for hiking, school and laptop 'ergonomique' queries

`mc-head-term-absence` · Off-Page / Authority · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** - 'sac à dos randonnée ergonomique' (M16): Glisshop, Cdiscount, Rayonrando, Ridepark, Toporando, Hardloop, mon-sac-a-dos and Millet. No Gravipack.
- 'sac à dos ordinateur ergonomique' (M17): mon-sac-a-dos x2, sac-a-dos-france, Eastpak, Darty, Karkoa, Accergo, ma-boutique-ergonomique and Ergonovie. No Gravipack.
- 'meilleur cartable ergonomique 2026' (M19): 8 of 9 results are comparison articles listing ergobag Prime, Satch, Tann's, Baagl and Eastpak. No Gravipack.
- 'meilleur sac à dos ergonomique comparatif 2026' (M18): Snowleader top 10 (Osprey Atmos AG, Millet Hanang, Deuter Futura), Toporando, Clubic and TechRadar. No Gravipack.
- Phase-1 E7 and E9 show the brand absent for 'sac à dos ergonomique' and 'cartable ergonomique'.
- Competitor and comparison domains searched with a domain filter (M21) returned no Gravipack mention in their snippets.
- Gravipack sells products for each of these segments: hiking (Sherpa, Hiking, Oslo), laptop (Business Talk V4, Kingston), school (G-Pack, Kingston, Feather).

<https://toporando.fr/meilleurs-sacs-a-dos-randonnee-trekking/> · <https://blog.snowleader.com/top-10-sac-a-dos-randonnee/> · <https://www.glisshop.com/conseils/les-meilleurs-sacs-a-dos-de-randonnee.html> · <https://ridepark.com/matos/meilleurs-sacs-a-dos-randonnee/> · <https://www.hardloop.fr/article/les-15-meilleurs-sacs-a-dos-de-randonnee-et-trekking> · <https://www.avis-parents.com/tests-avis/meilleur-cartable/> · <https://www.futura-sciences.com/conso/comparatifs/meilleur-cartable-comparatif/> · <https://www.accergo.fr/meilleurs-sacs-a-dos-ergonomiques/> · <https://norveya.com/blogs/organisation/les-meilleurs-sacs-a-dos-ergonomiques-contre-le-mal-de-dos> · <https://www.clubic.com/materiel-informatique/article-852462-1-meilleur-sac-a-dos-ortinateur-portable-comparatif.html> · <https://www.mon-sac-a-dos.fr/sac-a-dos-ergonomique/>

**Why it matters.** For these commercial-investigation queries Google mostly ranks comparison articles and retailer categories. A brand gets in by being listed in those articles and by having a category page that matches the wording 'ergonomique'. Gravipack titles use 'exosquelette / anti mal de dos' instead. AI answers also draw on the same comparison articles.

**SEO effect.** Placements in 3-5 comparison articles bring referral traffic, brand mentions and links (entity and AI-citation signals). Category pages worded with 'ergonomique' give gravipack.com a page Google can rank for each head term.

**How to fix.** 1. Digital PR. Offer test units, specs, a reproducible load test and a media kit to Toporando, Snowleader blog, Glisshop conseils, Hardloop, Ridepark (hiking: Sherpa, Hiking, Oslo), Avis-Parents and Futura-Sciences (school: Feather, G-Pack, Kingston), Clubic and TechRadar FR (laptop: Business Talk V4). Never pay for undisclosed placement.
2. Retitle and expand the segment category hubs to match the head terms. For example 'Sac à dos de randonnée ergonomique à exosquelette', 'Cartable et sac scolaire ergonomique', 'Sac à dos ordinateur ergonomique'. Each hub needs 400+ words of genuinely useful buying advice, a size table and a FAQ.
3. Ask Decathlon (via KID'ABORD) and Au Vieux Campeur to list Gravipack in their own 'meilleurs sacs' guides.

**Verifier notes.** Absence from comparison articles is reconfirmed. V3 (8 major resellers and owned domains blocked) returned only single-product tests (i-trekkings), press (Gomet, PresseSanté, INPI) and resellers. No listicle naming Gravipack appeared.

The title 'absent from the head terms' overstates it. Phase-1 extended data show gravipack.com ranking for its core 'anti mal de dos' head terms:
- E5 scolaire: #1-#3
- E2 ergonomique mal de dos: #2 and #4
- E1: #4-#6
- E4 randonnée: #5-#6
- E6 ordinateur: #3-#5
The absence is limited to generic 'ergonomique / randonnée / cartable' wordings and to listicles. Some of those are adjacent segments, such as primary-school cartables (ergobag, Satch).

Evidence URL typo: the Clubic URL reads 'ortinateur' instead of 'ordinateur', so the link is broken.

Fix issue: step 2's 'retitle' should ADD 'ergonomique' while keeping 'anti mal de dos'. Replacing it risks the rankings the hubs already hold. Any FAQ there is on-page content only (FAQ rich results have been restricted since 2023).

### No comparison or alternatives content exists anywhere for Gravipack; the brand can define the comparison fairly

`mc-comparison-pages-missing` · Content Quality · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** - 'gravipack vs osprey OR deuter OR alternative sac exosquelette' (M20) returned only Deuter-vs-Osprey content (outforia, mountainsforeverybody, bushwalk, expertworldtravel). No 'Gravipack vs X' page and no 'alternatives à Gravipack' page exists.
- The evaluation intent is real. Brand results already rank 'Idée de génie ou arnaque ?' (i-trekkings) and 'Gravipack Sherpa 45 : un sac à dos terrifiant' (Outzer, reputation log S26).
- Competitors own the explainers: Osprey has an official FR sizing guide, and Deuter has advice pages on back pain and maximum load (phase-1 #15 and #28).

<https://outforia.com/deuter-vs-osprey> · <https://www.i-trekkings.net/test-outdoor/test-sac-a-dos-gravipack-exosquelette-oslo-70-l/> · <https://www.outzer.fr/avis/accessoires/gravipack/sherpa-45/0/8651.html> · <https://www.osprey.com/fr/expert-advice/sizing>

**Why it matters.** Comparison queries ('X vs Y', 'quel sac choisir', 'alternative') convert well. When the brand has no balanced page of its own, sceptical third-party reviews define the comparison by default.

**SEO effect.** Six comparison or roundup pages give the brand rankable URLs for 'vs', 'quel modèle choisir' and 'meilleur … mal de dos' queries. They also give AI answers a citable, sourced comparison and channel internal links to model pages.

**How to fix.** Build the pages in the 'Recommended comparison and alternatives pages' table, in that priority order: own-range chooser; mechanism explainer; Sherpa 45 vs Osprey Talon 44 vs Deuter Aircontact Core 40+10; Feather vs ergobag vs Satch; laptop roundup; alternatives roundup.

Follow the seo-competitor-pages fairness rules:
- Every competitor fact must link to the maker's page.
- Show 'prix au [date]'.
- Disclose 'Gravipack est notre marque' (Gravipack is our brand).
- Acknowledge competitor strengths, such as hip-belt load transfer and ventilated backs.
- Use measured specs. Correct the disputed Sherpa volume (Outzer reports about 30 L).
- Make no medical claims, and present the 92% figure only as a manufacturer claim with the study's status.
- Add 'mis à jour le' and an author with physio or ergonomics credentials, and review quarterly.

Structure: at least 1,500 words per vs page, a comparison table, a CTA after the table and at the end, and a breadcrumb Accueil > Comparatifs > page.

Schema: ItemList for the roundups, Product only for Gravipack items, and Article for the explainer.

**Verifier notes.** Not refuted. M20 and V3 (open web, owned and reseller domains blocked) surfaced no 'Gravipack vs X', 'alternatives à Gravipack' or comparison page. The evaluation intent is real (the i-trekkings test and Gomet rank).

Wording: 'exists anywhere' rests on 2 searches. Say 'none found in 2 searches'.

Fix quality is good overall: fairness rules, disclosure, no medical claims, ItemList/Article/Product scoping. The one exception is the fixed 'at least 1,500 words per vs page' floor, which is arbitrary because Google does not rank on word count. Size each page to the intent instead.

### The largest marketplace presence (Decathlon, Nature & Découvertes) is run by licensee KID'ABORD, so titles, prices, claims and reviews are outside the brand's control

`mc-licensee-channel-control` · Brand / Reputation · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** - Decathlon Sherpa 45 and Hiking 33 are 'vendus et expédiés par KID'ABORD' (M9). Nature & Découvertes Feather Plus and Hiking Terracota are also sold by KID'ABORD (M5).
- Decathlon titles carry the health claim 'Allège la charge de 92%'.
- Nature & Découvertes files hiking and school bags under 'sacs-a-dos-velo' (bike backpacks).
- Decathlon ratings accrue to the brand: brand page 3.88/5 (16), Hiking 33 4.13/5 (8), Feather noir 1.5/5 (reputation log S17).
- The entity log (#8, societe.com) records KID'ABORD (SIREN 500 082 490, La Baule-Escoublac) under a 'procédure de sauvegarde' (court-supervised safeguard proceedings) since 16/02/2024, with recurring losses. A weak seller is a continuity risk for the channel that ranks #1 for 'sac à dos anti mal de dos'.

<https://www.decathlon.fr/p/mp/gravipack/sac-a-dos-randonnee-sherpa-45-allege-la-charge-de-92percent/_/R-p-b2fdb462-3699-459c-85fa-8ec3dcb54d7c> · <https://www.decathlon.fr/vc/gravipack> · <https://www.decathlon.fr/browse/b/gravipack/_/N-19o8oxe> · <https://www.natureetdecouvertes.com/outdoor/sac-a-dos-bagages/sacs-a-dos-velo/sac-a-dos-hiking-terracota-gravipack-97687020> · <https://www.societe.com/societe/kid-abord-500082490.html>

**Why it matters.** Marketplace pages rank for brand and head terms and are often the first brand touchpoint. Uncontrolled titles, unsubstantiated percentage claims, wrong categories and unanswered low ratings shape how buyers and Google see the brand. If the seller stops operating, the best-ranking pages disappear overnight.

**SEO effect.** Consistent marketplace content (titles, specs, claims, categories, answered reviews) improves brand-SERP CTR and trust. It also reduces the risk of a sudden loss of visibility on Decathlon.

**How to fix.** 1. Agree a content-syndication pack with KID'ABORD and every reseller: approved title template '[Modèle] [capacité] – sac à dos à exosquelette Gravipack', specs, images, substantiated claims, and the correct category (randonnée, scolaire, ville; not 'vélo').
2. Remove or substantiate '92%' in marketplace titles.
3. Answer marketplace reviews, especially those at 1-2 stars, from a brand account where the platform allows it.
4. Make sure the Decathlon brand page (vc/gravipack) describes the brand correctly. Decathlon pages generally do not link out, so do not rely on them for links.
5. Set up a contingency plan, such as a direct seller account on Decathlon marketplace or a second licensee, in case the licensee stops operating.

**Verifier notes.** The core premise that the brand cannot control the content is partly refuted.
- V7: Decathlon Business Talk (199 €) and one Feather noir offer (149 €) are 'Vendu et expédié par GRAVIPACK'. Other Feather offers are sold by KID'ABORD. The phase-1 site:decathlon.fr collection also listed both sellers.
- So the brand already holds a Decathlon seller account. Fix step 5 ('contingency: a direct seller account on Decathlon') already exists, and part of the Decathlon content is brand-controlled.

The KID'ABORD status is stale (entity-verify V8):
- The sauvegarde was opened by judgment on 31/01/2024; 16/02/2024 is the BODACC publication date.
- A 10-year plan was adopted in Feb 2025.
- Pappers reports an order of 13/05/2026 closing the procedure.
The 'continuity risk' is therefore overstated. 'Ranks #1 for sac à dos anti mal de dos' holds in standard mode only, not in extended E1.

Still valid: the N&D 'sacs-a-dos-velo' miscategorisation, '92%' in marketplace titles (a performance or health-adjacent claim, already covered by the entity claims findings), and unanswered low Decathlon ratings (Feather noir 1.5/5).

### Product data is inconsistent or broken across channels (prices showing 0.00€, wrong capacity, conflicting specs, warranty and sizing)

`mc-cross-channel-data-inconsistency` · E-commerce · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** - Kiabi SERP titles show 'SAC A DOS GRAVIPACK SHERPA 45 KAKI - Kaki - 0.00€' and 'nu€'; Hiking 33 is unavailable.
- Bureau Vallée titles the Pearl '33 litres' while its URL says '29-litres'.
- Hiking is listed as 33 L by retailers and 30 L by the brand and one Fnac listing. Its weight is given as 900 g, 990 g or 1200 g.
- Feather fits a 14-inch laptop on one listing and 15 inches on the brand page. Its weight is 780 g or 890 g. The size threshold for Feather vs Feather Plus is '<1m50 et 30 kg' on Kiabi and '<1m55' elsewhere.
- Warranty is '10 ans' on retailers and '1 an' on the gravipack.com school category snippet.
- Fnac indexes 3 brand-page duplicates with nonsense parameters (?snu=…&kookaburr=…), and most models are out of stock.
- Cdiscount's /r-gravipack.html internal search page ranks for the brand but shows look-alike products such as Pacsafe 'Gravity Gray'.

<https://www.kiabi.com/sac-a-dos-gravipack-sherpa-45-kaki-kaki_P1443012C1443014> · <https://www.kiabi.com/sac-a-dos-gravipack-feather-plus-noir-noir_P1459548C1459549> · <https://www.bureau-vallee.fr/gravipack-sac-a-dos-pearl-29-litres-gris-405222788.html> · <https://www.fnac.com/Sac-a-dos-Gravipack-Hiking-33-Vert/a16167921/w-4?ti=g&s=namby&bonker=37b2c34386> · <https://www.fnac.com/Gravipack/m568883/w-4?snu=d7c5d284&kookaburr=938536&namb=ho&a=7ee69b0b&mumbo-ju=acr&ninco=249545&hullab=16219aa2> · <https://equilibre-france-ergonomie.fr/produits/sac-a-dos-hiking-33-baroudeur-et-leger/> · <https://gravipack.com/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/> · <https://www.cdiscount.com/bagages/r-gravipack.html>

**Why it matters.** Conflicting specs and broken prices undermine trust, cause returns ('pas 45 L') and weaken entity consistency for search engines and AI answers. Without GTINs, Google cannot group offers, so it cannot show the official store as the brand's own offer.

**SEO effect.** One master data set with GTINs across all channels improves offer grouping in Shopping, reduces contradictory facts in AI answers and removes junk results from brand searches.

**How to fix.** 1. Create one master product sheet: GTIN/EAN, MPN, measured volume and weight, dimensions, laptop size, strap size range, height guidance and warranty. Send it to every reseller and to Merchant Center.
2. Ask Kiabi either to delist discontinued Gravipack items (410 or redirect) or to fix the 0.00€ offers.
3. Ask Bureau Vallée to correct the Pearl volume.
4. Ask Fnac to close out-of-stock listings or merge them into current models.
5. Choose one Feather size threshold and one warranty term, and use them everywhere.

**Verifier notes.** Reconfirmed and strengthened.
- V2 again shows 33 L vs 30 L and 990 g vs 1,200 g for Hiking.
- The 1-year warranty is not only on the school category snippet. It also appears on the official Sherpa Bleu listing (V1), the Ergo-Corner Sherpa kaki page (V9) and gravipack.ma bureautique (V8), against 10 years elsewhere.

Caveats:
(a) Cdiscount /r-gravipack.html surfaced only in domain-filtered or heavily filtered queries (M11, M13). It was not shown ranking in an open brand SERP, so 'ranks for the brand' is unproven.
(b) The Fnac nonsense-parameter URLs come from this non-Google index and are not something Gravipack can fix.
(c) 'Without GTINs, Google cannot group offers' is too absolute. GTIN is strongly recommended and is the main matching key, but brand plus MPN also exists.

### Product, Offer, AggregateRating, MerchantReturnPolicy and ShippingDetails markup and Merchant Center free listings cannot be verified, and current pricing and review practices would block them

`mc-schema-merchant-center` · Schema / Structured Data · auditor severity **Medium** → verifier **unverifiable**, severity **Medium**

**Evidence.** - WebSearch cannot show Shopping units, and gravipack.com is blocked, so markup and Merchant Center status are unknown.
- Known blockers: (a) one model shows 2-3 prices on gravipack.com (Sherpa 99/119/149.90; Tokyo 129/189; Pearl 89/119) (M26); (b) product pages display a first-party 'Avis Google 4,7 / plus de 1121-1175 avis' widget that no third party corroborates (reputation log S27); (c) colours are separate product URLs (tables.md) instead of variants; (d) no GTINs were seen in any listing snippet.
- No Gravipack offer was found on Amazon.fr, and the brand query on Cdiscount returns look-alikes, so Google Shopping and free listings are the remaining large comparison surface.

<https://gravipack.com/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/> · <https://www.gravipack.com/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/> · <https://gravipack.com/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/> · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** Under the claude-seo seo-ecommerce rules, merchant listings require name, image and an Offer with a price greater than zero and a priceCurrency. shippingDetails and hasMerchantReturnPolicy raise eligibility for richer results. Google's review-snippet guidelines forbid marking up ratings aggregated from other sites, such as a Google-reviews widget, as AggregateRating. A price mismatch between schema, feed and page leads to disapprovals.

**SEO effect.** Valid markup plus a Merchant Center feed makes the official store eligible for free product listings and price, shipping and return annotations. In model searches where resellers now win, the official offer would then appear beside them.

**How to fix.** 1. Use one product per model with colour and size variants (ProductGroup with variesBy color/size, or item_group_id in the feed).
2. Per variant, output JSON-LD: Product{name, image[], description, brand{Brand 'Gravipack'}, sku, gtin13, mpn, color, size, offers: Offer{url, price '119.00', priceCurrency 'EUR', availability 'https://schema.org/InStock', priceValidUntil for promos, seller{Organization: <legal entity in mentions légales>}, hasMerchantReturnPolicy{MerchantReturnPolicy, applicableCountry 'FR', returnPolicyCategory MerchantReturnFiniteReturnWindow, merchantReturnDays ≥14, returnMethod ReturnByMail, returnFees per CGV}, shippingDetails{OfferShippingDetails, shippingRate{MonetaryAmount, currency 'EUR'}, shippingDestination{DefinedRegion 'FR'}, deliveryTime{handlingTime, transitTime}}}}.
3. Add aggregateRating{ratingValue, reviewCount} only from reviews collected on gravipack.com for that product (e.g. a native WooCommerce or verified-review plugin). Do not mark up the Google 4.7 widget, and remove the '500 000 clients' and '4,7' claims unless substantiated.
4. Verify and claim gravipack.com in Merchant Center (the Content API for Shopping sunset on 2026-08-18; use the Merchant API or a WooCommerce plugin). Configure shipping and returns there or in Search Console, and enable free listings for France. Make sure the feed price equals the page price equals the schema price.
5. Validate with the Rich Results Test and the Merchant Center diagnostics.

**Verifier notes.** Markup and Merchant Center status still cannot be checked with WebSearch.

Checked:
- V5 confirms the Content API for Shopping sunset on 18/08/2026. It has already passed: intermittent 410 errors since 01/09/2026, full turn-down in early 2027. The advice to use the Merchant API or a plugin is current.
- ProductGroup/variesBy is current Google variant guidance.
- Not marking up Google reviews as AggregateRating is correct.

Evidence problem: blocker (b) 'widget that no third party corroborates' is contradicted by reputation-verify V5. A directory page reports 4.7/5 from 998 Google reviews and a blog reports 4.8 from 900+. These are weak sources but corroborate the figure, so fix step 3's 'remove the 4,7 claim unless substantiated' is too strong. Replace the hard-coded, inconsistent counts (1121/1126/1175) with a dated or live figure.

Fix issue: 'priceValidUntil for promos' is outdated. Google merchant listings now take the reference price as a priceSpecification with priceType StrikethroughPrice, and the sale window as validFrom/validThrough on the Offer or PriceSpecification ('Sale duration' section, July 2026).

### No sizing or fit guide, although Gravipack sells strap sizes and height-based models; Osprey and Arsayo own the size-guide content

`mc-size-guide-gap` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** - Ergo-Corner titles every Gravipack product with 'Personnalisation de l'exosquelette M/L/XL/XXL' (strap sizes).
- Feather (<1m50/1m55) and Feather Plus (above that height) are split by the wearer's height, and the threshold differs by channel.
- A Decathlon reviewer obtained custom straps only after contacting the brand (reputation log S17).
- Osprey publishes an official FR sizing guide (torso length C7 to iliac crest; S/M 43-52 cm, WXS/S 34-43 cm). Snowleader and Alpinstore republish Osprey size guides.
- Arsayo sizes its bags by shoulder width (S/M/L).
- No Gravipack sizing page surfaced in any search, including site-restricted ones.

<https://www.ergo-corner.com/gravipack/737-sac-a-dos-city-avec-exosquelette-gravipack.html> · <https://www.osprey.com/fr/expert-advice/sizing> · <https://www.snowleader.com/guide-des-tailles-osprey> · <https://www.alpinstore.com/fr/content/2744-guide-taille-osprey> · <https://www.kiabi.com/sac-a-dos-gravipack-feather-noir-noir_P1459532C1459533>

**Why it matters.** Fit is the main cause of the complaints seen (straps rubbing the neck, shoulder pain on the GR20, unsuitable for small sizes). A size guide reduces returns and negative reviews, and it is evergreen content that resellers can republish with a link back.

**SEO effect.** A 'Guide des tailles Gravipack' page can rank for 'taille sac à dos dos/épaules' long-tail queries. It earns reseller links and gives product pages a size attribute for schema and the feed.

**How to fix.** 1. Publish /guide-des-tailles/ with how to measure (shoulder width and torso length), a chart mapping measurements to strap size M/L/XL/XXL and to each model, the Feather vs Feather Plus height threshold (one value), and a short video.
2. Link it from every product page and the size selector.
3. Offer it to resellers as embeddable content with a link back.
4. Add size (and SizeSpecification if relevant) to Product and variant markup and to the feed.

**Verifier notes.** Partly refuted by V6.
- gravipack.com product pages (Business Talk V4, Hiking, Tokyo) say each bag is personalised free of charge to the buyer's height and weight, within ±10 cm and ±8 kg.
- The Austerlitz page asks for height and weight at order and adjusts the bag in the workshop.
- An official adjustment guide exists: /comment-regler-les-bretelles-exosquelette-de-mon-gravipack/. It was also in the phase-1 serp-notes, so 'No Gravipack sizing page surfaced in any search, including site-restricted ones' is internally inconsistent.

The remaining gap is narrower. There is no public table mapping height and weight to strap setting or size, and no 'how to measure' content. Ergo-Corner's M/L/XL/XXL (or '3 tailles') is the reseller's own wording.

'Fit is the main cause of the complaints' is overstated: the complaints also cover refunds and doubts about the 92% claim.

The fix's M/L/XL/XXL chart may conflict with the brand's personalised-fit model. Better: document the personalisation process with the height/weight table, link the existing adjustment guide from every product page, and expose size in markup and the feed.

### Several brand storefronts (presta.gravipack.com, gravipack.ma, gravipacker.com) show different catalogues, model names and prices

`mc-brand-store-fragmentation` · International / Domains · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** - The legacy presta.gravipack.com still ranks for Hiking 33, Feather, Business Talk and Sherpa 45, with prices such as Feather 149 'in stock' (M15, M25).
- gravipack.ma is a separate 'Gravipack®' store priced in euros (about 119-249.90). It uses different model names (Trek Air 25L, Summit Air 35L, Sherpa Peak 50L), has 2 category URL bases, and says 'boutique en préparation' (M22).
- gravipacker.com is another brand domain with the Vincennes address (M13).
- No hreflang or cross-domain relationship can be seen from search results.

<https://presta.gravipack.com/accueil/15-sac-a-dos-gravipack-business-talk.html> · <https://presta.gravipack.com/accueil/19-sac-a-dos-gravipack-sherpa-45.html> · <https://gravipack.ma/> · <https://gravipack.ma/product-category/sac-a-dos-gravipack/gravipack-edition-outdoor/> · <https://www.gravipacker.com/>

**Why it matters.** Merchant Center ties offers to one verified domain. Duplicate or conflicting brand stores split signals and confuse buyers about which shop is official. A EUR store on .ma with other model names may compete with the French store in French results.

**SEO effect.** Consolidating on gravipack.com, or setting clear market targeting with hreflang if .ma serves Morocco, concentrates link equity and removes duplicate shopping entities.

**How to fix.** 1. 301-redirect presta.gravipack.com URL by URL to gravipack.com equivalents.
2. Decide the role of gravipack.ma. If it serves Morocco, price in MAD, use market-specific content and hreflang fr-MA / fr-FR, and align model names. Otherwise, redirect it.
3. Redirect gravipacker.com to gravipack.com, or make it a non-commerce community page that links to the official store.
4. List every official domain in Organization sameAs and on the mentions légales page.

**Verifier notes.** V8 confirms that gravipack.ma prices in EUR (Rome 119.90, Dublin 249.90, Trek Air 25L 129, Sherpa Peak 50L 189). It also promises 'livraison rapide partout dans le monde', which overlaps the French market, uses different model names and shows a 1-year warranty on the bureautique page. Legacy presta still ranks (#9 for 'gravipack hiking 33' in V2).

Internal consistency: the presta URL-by-URL 301 appears in both this finding and mc-model-serp-ceded step 3. Consolidate it in one place, and keep the presta host serving the redirects rather than removing it.

### Not on Amazon.fr, Cdiscount, Rakuten or ManoMano, no pharmacy or orthopaedic channel, and no official 'Où acheter' page

`mc-channel-gaps-amazon-pharmacy` · E-commerce · auditor severity **Low** → verifier **weakened**, severity **Low**

**Evidence.** - Amazon.fr: 2 searches, no Gravipack listing. The only hit is a customer review on a Kipling bag saying 'je vais passer à la marque GRAVIPACK… sacs à dos anti mal de dos'.
- Cdiscount, Rakuten, ManoMano, eBay.fr: no products (1 search). Cdiscount's brand search page shows look-alikes.
- Pharmacy, orthopaedic or osteopath channel: none found (1 search).
- Physical availability exists, such as Bureau Vallée 'retrait 2h en magasin' and Au Vieux Campeur, but no official stockist page surfaced.

<https://www.amazon.fr/Kipling-Seoul-Grand-Protection-Ordinateur/dp/B0B5RY3DDZ> · <https://www.cdiscount.com/bagages/r-gravipack.html> · <https://www.bureau-vallee.fr/gravipack-sac-a-dos-pearl-29-litres-gris-405222788.html>

**Why it matters.** The Amazon review shows some demand. Without a brand presence, the brand query on these platforms returns competitors or look-alikes. Adding channels before prices are aligned would make the parity problem worse.

**SEO effect.** Small. A stockist page can rank for 'gravipack magasin' or 'où acheter' queries and give resellers a page to link to. Amazon Brand Registry protects the trademark from look-alike listings.

**How to fix.** 1. Publish /ou-acheter/ listing the official store, authorised resellers (Decathlon via KID'ABORD, Au Vieux Campeur, Nature & Découvertes, Ergo-Corner, Équilibre, Bureau Vallée) and physical availability. Link to it from the footer.
2. Consider Amazon.fr (with Brand Registry) only after the master data and price policy are fixed.
3. Do not market through pharmacies or orthopaedic shops until the medical-device status is clarified (see the entity log: no CE, EUDAMED or LPP record found).

**Verifier notes.** Not re-searched (budget). The finding is internally consistent and Low is proportionate, but the absence rests on thin evidence: 2 searches for Amazon and 1 each for Cdiscount, Rakuten, ManoMano, eBay and pharmacies. Present it as 'not found in N searches'.

Fix step 1 lists 'Decathlon via KID'ABORD'. The stockist page should name both Decathlon sellers: GRAVIPACK sells Business Talk and one Feather offer (V7).

Advising against pharmacy marketing until the medical-device status is clarified is sound.
