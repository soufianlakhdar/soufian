# Data tables — geo-ai-visibility-entity (phase 1)

## A. Evidence provenance and limits

| Item | Detail |
|---|---|
| My WebSearch calls this turn | 4 attempted (gravipack / gravipack avis / gravipack sac / gravipack exosquelette). All refused: shared 200-search-per-turn budget used up. No workaround attempted. |
| Carried-over search evidence | serp-notes.md from earlier WebSearch runs in this workflow: 48 standard-mode queries, 12 extended-mode queries, 3 extra site: queries |
| Carried-over URL inventory | tables.md / inv.py: 98 gravipack.com URLs (apex and www mixed) and 16 presta.gravipack.com URLs, each with its search-result title |
| Index / locale | WebSearch tool, US-located, not google.fr. Titles are as shown in results and may be rewritten. |
| AI-platform measurement | None (no DataForSEO, SE Ranking or Profound). Visibility is a SERP proxy. |
| PSI / Lighthouse | Quota exceeded (HTTP 429 in scratchpad data/psi_fr_mobile.json) |
| gravipack.fr | site:gravipack.fr returned 0 results (orchestrator brief) |

## B. Brand SERP: queries about the brand, as recorded

| Query (mode) | Results recorded (in order) | Official site in results? | Sentiment / notes |
|---|---|---|---|
| gravipack (std) | motherbase.ai, neozone, lespepitestech, randonner-leger x2, lematin.ma, maddyness | NO | Neutral press, startup directories, forum. motherbase.ai shows a Vincennes address. |
| gravipack avis (std) | es.trustpilot.com/review/gravipack.com, then unrelated results (gravasac, graviti, generic 'avis') | NO | Weak match for brand intent. Spanish Trustpilot locale. |
| gravipack prix (std) | neozone, randonner-leger x2, lespepitestech, noise | NO | No official price or where-to-buy page shown |
| gravipack decathlon sherpa 45 (std) | decathlon.fr/brands/gravipack, Decathlon browse page 'gravipack sacs-a-dos', randonner-leger, kisskissbankbank FAQ, Trustpilot ES | NO | Decathlon price €149.90 (was €249), promo 18 Jun-30 Aug 2026, seller Kid'Abord |
| gravipack sherpa avis test (std) | outzer.fr Sherpa 45 review, randonner-leger x4, Trustpilot ES, noise | NO | outzer is negative: about €240, about 30 L measured for a bag named '45' |
| gravipack arnaque efficace 92% (std) | randonner-leger x8, kisskissbankbank | NO | 100% user-generated content, skeptical |
| gravipack étude Lyon (std) | randonner-leger x6, moodle univ-lyon1, maddyness, europe1 | NO | No study page on gravipack.com in the results |
| gravipack Kid'abord (std) | natureetdecouvertes Kid'Abord listings (return address 'RETOUR GRAVIPACK' c/o SODILOG, Colmar), lespepitestech | NO | Distributor link. The 'Loire-Atlantique' location is still unverified. |
| site:gravipack.fr | 0 results | n/a | Audited domain has no indexed pages |
| gravipack sac / gravipack exosquelette | NOT RUN (search limit) | n/a | Re-run in a follow-up |

## C. AI-answer proxy: standard-mode conversational and category prompts (FR)

| # | Prompt | gravipack.com present | Third-party Gravipack mention | Dominant sources |
|---|---|---|---|---|
| 1 | sac à dos ergonomique | No | No | osprey.com/fr, manor.ch, markenkoffer (ergobag), randonner-leger x3, alpinstore x3, lavenir.net |
| 2 | sac à dos anti mal de dos | No | YES: Decathlon vc/gravipack, journaldugeek, maddyness (2024) | cssdgs.gouv.qc.ca PDF, globe-trotting, consoglobe, courrierlaval, randonner-leger x2 |
| 3 | sac à dos exosquelette | No | YES: journaldugeek, EPO patents x3 | ffrandonnee news, i-trekkings, neozone (LEX), scire PDF, percko |
| 4 | meilleur sac à dos pour le mal de dos | No | YES: Decathlon vc/gravipack, journaldugeek | cisss-lanaudiere PDF, randonner-leger x2, allodocteurs, globe-trotting x2, courrierlaval |
| 5 | sac à dos mal aux épaules solution | No | YES: journaldugeek | randonner-leger x4, pass-education, globe-trotting x2, consoglobe |
| 6 | cartable ergonomique mal de dos enfant | No | No | laposte, dhnet, assemblee-nationale, tendanceouest, enseignons.be, ufapec, pourquoidocteur, 24matins, gambin |
| 7 | sac à dos randonnée léger ergonomique | No | No | rayonrando, deuter x4, glisshop top 5, alpinstore x3 |
| 8 | sac à dos ordinateur ergonomique dos | No | No | startech x3, markenkoffer x2, materiel.net x2, kensington |
| 9 | sac à dos remboursé sécurité sociale mal de dos | No | YES: challenge.ma (reimbursement claim) | insurers (april, lecomparateurassurance x2, previssima, lelynx, groupama), 24matins |
| 14 | comment bien porter son sac à dos | No | No | pourquoidocteur, 24matins, consoglobe x2, CISSS/CSS PDFs, allodocteurs x2, courrierlaval |
| 15 | poids max sac rando % | No | No | deuter x2, glisshop, rtbf, cimalp, ffrandonnee x2, baragneurs PDF, sawyer |
| 19 | sac à dos troubles musculo-squelettiques TMS travail | No | No | inspq x4, osha.europa.eu, factorial x2, myrhline, pharma-gdd |
| 22 | sac à dos scolaire ergonomique collège | No | No | manor.ch, marques-de-france (Bon Chic Bon Dos), alcuinfonds x2, jumia x2, meilleurtest comparatif, gambin |
| 23 | poids cartable 10% | No | No | dhnet, assemblee-nationale PDFs x6, pourquoidocteur, allafrica, showroomprive PDF |
| 24 | sac à dos porte-outils ergonomique artisan | No | No | legallais, hoffmann x2, castorama, toptex x2, sonepar |
| 25 | sac à dos tactique militaire ergonomique | No | No | military.eu x7, Decathlon marketplace (Inuitz), crateclub |
| 26 | sac à dos vélotaf ergonomique | No | No | tonton-outdoor best-of, culturevelo x8 |
| 27 | sac à dos femme ergonomique mal de dos | No | YES: journaldugeek | osprey x2, protegez-vous, maif x2, cssdgs PDF, marjanemall |
| 28 | mal au dos sac à dos randonnée que faire | No | No | globe-trotting x2, rtbf, deuter x2, osprey guide, salomon x2, randonner-leger |
| 29 | bretelles ergonomiques sac à dos soulager épaules | No | YES: randonner-leger Gravipack threads x3, journaldugeek | Québec school PDFs x3, kaufland, thule, consoglobe |
| 31 | sac à dos qui soulage le dos et les épaules | No | YES: KKBB Gravipack FAQ, randonner-leger x3 (570298/570316/570392), journaldugeek, i-trekkings | consoglobe x2, 811.novascotia |
| 32 | sac à dos recommandé par les ostéopathes | No | No | gambin, marques-de-france x2, cisss PDF, chiropractic.ca PDF, my-podologie |
| 33 | meilleur cartable ergonomique comparatif 2026 | No | No | avis-parents x4, meilleurtest x3, futura-sciences x2 (listicles) |
| 34 | claie de portage ergonomique | No | No | alpinstore x3, tonton-outdoor x2, pearl x2, cnesst |
| 39 | sac à dos ordinateur anti mal de dos | No | No | pearl.fr (Tucano Marte Gravity) x3, dell, manutan, wardow, techradar best-of, kensington, meilleurtest |
| 40 | sac à dos anti mal de dos enfant école | No | No | maif, 24matins, allodocteurs x2, ufapec, noovo, courrierlaval, pourquoidocteur |
| 41 | sac à dos Compostelle mal de dos | No | No | conseilsport.decathlon.fr, compostelle-bretagne PDF, camino sites x2, mec.ca |
| 42 | sac à dos scoliose enfant | No | No | newswire x2, protegez-vous, allodocteurs x2, pourquoidocteur, noovo |
| 44 | sac à dos anti gravité | No | Possibly (randonner-leger x4, topic unconfirmed) | mec (Osprey Aura AG) x2, i-run, i-trekkings, pearl (Luna Gravity) |
| 45 | sac à dos hernie discale | No | No | lasante, lematin x4, editions-tissot, vidal |
| 46 | exosquelette passif TMS | No | No | ffbatiment x2, inrs, travail-industrie, batiweb, osha |
| 47 | sac à dos randonnée 60+10 | No | No | alltricks, outzer (Deuter), fflose best-of x2, tonton-outdoor x2, alpinstore x4 |
| 48 | sac à dos voyage ergonomique | No | No | deuter x7, osprey x2, thule |
| **Total** | 33 prompts | **0/33** | **8/33 confirmed (+1 possible)**. journaldugeek (2021) alone appears in 7. | |

## D. AI-answer proxy: extended-mode prompts (closer to a real top 10)

| # | Prompt | gravipack.com URLs (count) | Other Gravipack sources | Other dominant sources |
|---|---|---|---|---|
| E1 | sac à dos anti mal de dos | 3 (Pearl, home, Tokyo) | ici.fr Gravipack article (#1), ergo-corner /55-gravipack (#2) | arsayo, oqlf |
| E2 | sac à dos ergonomique mal de dos | 2 (Hiking 30 L gris, home) | ergo-corner /55 (#1) | arsayo, ergonovie, ma-boutique-ergonomique, blogs |
| E3 | sac à dos exosquelette | 2 (category 'tous', home; positions 6-7) | i-trekkings Oslo test, ergo-corner /55, Decathlon Hiking 33, Google Patents | kentfaith blog (#1), alloprod, compostelle-autrement |
| E4 | sac à dos randonnée anti mal de dos | 2 (randonnée category, home with title 'Le sac bureautique ou randonnée révolutionnaire...') | ergo-corner /55, randonner-leger 12300 | snowleader (#1), zeoutdoor comparatif, norveya, accergo, trivent PDF |
| E5 | sac à dos scolaire anti mal de dos | 3 (Kingston x2, scolaire category; #1-3) | none | bodypack, sac-a-dos-france, ma-boutique-ergonomique, PDFs |
| E6 | sac à dos ordinateur ergonomique anti mal de dos | 3 (Business Talk V4 25 L, business category, home) | none | bureaucosy x2 (#1-2), mon-sac-a-dos.fr, arsayo, norveya |
| E7 | sac à dos ergonomique | **0** | none | sacados.fr, mon-sac-a-dos.fr, karkoa, sacroche, accergo (listicle), le-repaire (listicle), arsayo, ma-boutique-ergonomique guide |
| E8 | meilleur sac à dos anti mal de dos | 1 (home, #5) | ergo-corner /55 (#1), randonner-leger 44698 | norveya, accergo, karkoa, arsayo, techradar |
| E9 | cartable ergonomique | **0** | none | lespetitsbaroudeurs (ergobag) x2, mon-sac-a-dos.fr, mahilana, ma-boutique-ergonomique x4, univers-cartable |
| E10 | sac à dos porte-outils anti mal de dos | 5 (Exotool, Light Promax x2, Toolmaster, outillage category; cannibalization) | ergo-corner /55 (#1) | arsayo, rs-online |
| E11 | sac à dos tactique anti mal de dos | 2 (Austerlitz, home) | ergo-corner /55 (#1) | amgpro, le-repaire, mode-tactique, tac-store |
| E12 | sac à dos vélo travail anti mal de dos | 2 (Tokyo, Rome) | none | velotafeur (#1), asadventure, guide-velo, techradar |
| **Total** | 12 prompts | **10/12 prompts; 25 of 108 result slots (23%)** | ergo-corner /55-gravipack is in 7 of 12, usually at #1 | |

## E. Source types that dominate the result sets AI engines draw from

| Source type | Examples observed | Prompts where they dominate | Gravipack present? |
|---|---|---|---|
| Health and institutional | CISSS/CSS Québec PDFs, allodocteurs, pourquoidocteur, MAIF, Assemblée nationale PDFs, INSPQ, OSHA, INRS, Vidal | Informational and health prompts (#6, 14, 19, 23, 32, 40, 42, 45, 46) | Never |
| Outdoor brand guides and federations | Deuter, Osprey, Salomon, Thule, Rab, FFRandonnée | How-to and hiking prompts (#7, 15, 28, 48) | Never |
| Listicles and comparison pages ('comparatifs') | accergo, le-repaire, karkoa, norveya, zeoutdoor, meilleurtest, avis-parents, futura-sciences, techradar, glisshop, tonton-outdoor, fflose | 'Meilleur...' and head-term prompts (#33, 39, E4, E7, E8) | Not visible in the results. Whether the articles mention Gravipack in their text is UNVERIFIED. |
| E-commerce categories and resellers | alpinstore, snowleader, sacados.fr, mon-sac-a-dos.fr, ma-boutique-ergonomique, bureaucosy, lespetitsbaroudeurs, ergo-corner, Decathlon | Commercial prompts | Yes, through ergo-corner /55-gravipack and Decathlon |
| Forums and user content | randonner-leger.org | Every Gravipack validation query and the shoulder-relief prompts | Yes, mostly skeptical |
| Press | journaldugeek (2021), maddyness (2024), europe1, ici.fr, neozone, lematin.ma, challenge.ma | Brand and 'anti mal de dos' prompts | Yes, but dated |
| Reddit / YouTube / Wikipedia / Wikidata / LinkedIn | none | n/a | **0 occurrences recorded across about 60 result sets** (no dedicated query was run) |

## F. Entity fact consistency matrix (Gravipack)

| Attribute | Value | Source (as recorded) | Consistent? |
|---|---|---|---|
| Official domain | gravipack.com (apex AND www both indexed) + legacy presta.gravipack.com. gravipack.fr has 0 indexed pages. | inv.py / tables.md; site:gravipack.fr | NO: 4 hosts |
| Legal entity | EXOSQUELETTE LIGHT, Paris (hosting by Gandi) | gravipack.com/mentions-legales/ result snippet | Verify |
| Startup ecosystem | French Tech Aix-Marseille / Région Sud | lespepitestech (brief) | Conflicts with Paris |
| Address shown by a directory | Vincennes | motherbase.ai (brand result) | Conflicts |
| Marketplace seller / distributor | Kid'Abord (Decathlon seller). Returns 'RETOUR GRAVIPACK' c/o SODILOG, Colmar (Nature & Découvertes) | serp-notes #11, #36 | Not explained anywhere official |
| Founder / inventor | Mohammed Errafi | brief (lespepitestech, press) | Not checked against LinkedIn / Wikidata |
| Funding | €346k from friends and family ('love money', 2019); KissKissBankBank crowdfunding | brief | n/a |
| Award | 'Médaille d'argent concours Lépine international' (legacy Business Talk page) vs 'primé au Concours Lépine' vs 'récompensé' (posts) | presta / gravipack.com posts | Year and category not stated consistently |
| Validation claims | Tested by French Army / Foreign Legion 2017; 'first backpack reimbursed by social security' | challenge.ma | No official page found in results |
| Institutional users | RATP agents (porte-outils), SOFINS special forces, Vivatech | gravipack.com posts | Only first-party sources |
| Bacary Sagna | Post 'L'étonnante reconversion du footballeur Bacary Sagna, Gravipack.' | www.gravipack.com post | Relationship unclear |
| Price | Sherpa 45: €149.90 promo / €249 (Decathlon), about €240 (outzer). Oslo 60+10: €289. Range €90-289. Compostelle 80 L titled 'pas cher' | serp-notes, tables.md | Varies by channel |

## G. Descriptor and product-name variants seen in search-result titles

| Type | Variant | Where |
|---|---|---|
| Core descriptor | 'exosquelette' (current) | Most gravipack.com titles |
| Core descriptor | 'sac à dos en apesanteur' | presta /73-gravipack, /40-etude..., /59-concours-lepine..., Road Adventure; gravipack.com /inventeur-dun-sac-a-dos-en-apesanteur/ |
| Core descriptor | 'bretelles carbone' / 'inserts carbone' | brief (press) |
| Core descriptor | 'EVA ergonomique mémoire de forme' (no 'exosquelette' in the title) | Compostelle survie 25 / 35 / 65 / 80 L products |
| Efficacy claim | 'allège le poids de 92%' / 'Allège la charge de 92%' / 'réduire efficacement le poids' | scolaire category, /inventeur... post, Decathlon titles, Tokyo slug |
| Superlatives | 'le seul sac à dos au monde', 'la seule au monde', 'certainement le meilleur sac au monde', 'le meilleur sac à dos de montagne', 'le meilleur sac a dos au monde', 'révolutionnaire' (about 15 titles) | presta Hiking 33, Tokyo slug, City slug, presta Sherpa 45, presta livraison |
| Health wording | 'anti-douleur', 'anti douleur', 'anti-TMS', 'sauvez des vies' | Light Promax, Sherpa Kaki, randonnée category, médical category |
| Product names | Hiking 33 (Decathlon, presta) vs Hiking 30 L gris / Terracotta (gravipack.com) | volume mismatch |
| Product names | Sherpa 45 (presta, Decathlon) vs Sherpa bleu / orange 45 L / kaki (3 URLs for kaki). outzer measured about 30 L | |
| Product names | Feather (school bag: KKBB, Decathlon, presta) vs G-Pack (2 URLs with the same title) / Kingston (current school range) | |
| Product names | Business Talk (presta) vs Business Talk V4 20 L / 25 L / 25 L EVA (3 URLs) | |
| Product names | Road Adventure, Safar Vibe, City Connect (KKBB / legacy) vs City, Tokyo, Rome, Dublin, Oslo, Helsinki, Pearl, Austerlitz, Centurion, Easy Travel | Many names, no lineage shown |
| Off-topic products | external solar battery (slug ends '-copie'), paracord bracelet, wrist strap, keyring, 'fabrication professionnelle, cadeaux d'entreprise et objets publicitaires', payment link | gravipack.com /produit/ |
| Name collision | 'anti-gravité' / 'Gravity' results are owned by Osprey Anti-Gravity (AG), Tucano Marte Gravity, Pearl Luna Gravity | prompt #44, #39 |

## H. Entity-source checklist (knowledge graph and AI corroboration)

| Source | Status | Evidence |
|---|---|---|
| Wikipedia (fr) | Not observed | Not in any recorded result set; dedicated query not run |
| Wikidata | Not observed | Same as above |
| LinkedIn company page | Not observed | Same as above |
| Crunchbase | Not observed | Same as above |
| Google Business Profile / knowledge panel | Unknown | Needs a google.fr brand search |
| YouTube | Not observed | 0 youtube.com results in about 60 result sets |
| Reddit | Not observed | 0 reddit.com results in about 60 result sets |
| Trustpilot | Present (es.trustpilot.com/review/gravipack.com) | Brand queries; FR locale and review volume unknown |
| Decathlon marketplace brand page | Present (decathlon.fr/brands/gravipack + collection / product pages) | site:decathlon.fr gravipack |
| KissKissBankBank | Present (FAQ page) | #31, #37, brand queries |
| Startup directories | lespepitestech, motherbase.ai (AI-generated directory) | Brand query results |
| Patents | EPO / Google Patents results for 'sac à dos exosquelette' | #3, E3 |
| Press | journaldugeek (2021), maddyness (2024), europe1, ici.fr, neozone, lematin.ma, challenge.ma | various |
| Independent tests | i-trekkings (Oslo), outzer (Sherpa 45, negative) | E3, #35 |
