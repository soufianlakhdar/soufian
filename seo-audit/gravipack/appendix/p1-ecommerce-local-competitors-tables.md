# Data tables — ecommerce-local-competitors (phase 1)

## Search log for this sub-agent (budget exhausted)

| # | Query (mode) | Result |
|---|---|---|
| 1 | gravipack amazon.fr sac à dos (standard) | REFUSED – shared 200/turn WebSearch budget used up |
| 2 | gravipack decathlon marketplace sherpa 45 (standard) | REFUSED |
| 3 | gravipack cdiscount OR fnac OR rakuten OR manomano (standard) | REFUSED |
| 4 | gravipack avis (standard) | REFUSED |
| 5 | gravipack prix sac exosquelette (standard) | REFUSED |
| 6 | gravipack trustpilot (standard) | REFUSED |

No fallback was used: no curl, proxy, cache or archive, as the network policy and tool instructions require. Searches completed: **0**.

## SERP-visible title audit (titles relayed by the orchestrator, as shown in search results; Google may rewrite titles)

| Page (as relayed) | Title as shown in SERP | Chars | ≤60? | Brand present / position | Model name first? | 'exosquelette' | 'mal de dos' |
|---|---|---|---|---|---|---|---|
| Home | Gravipack : le sac révolutionnaire anti mal de dos exosquelette | 63 | No | Yes / start | n/a | Yes | Yes |
| Sherpa (colour not stated) | Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa | 65 | No | **No** | No (end) | Yes | Yes |
| Austerlitz | Sac à dos léger et ergonomique anti-mal de dos avec exosquelette Gravipack Austerlitz | 85 | No | Yes / char 65 | No (end) | Yes | Yes (hyphenated) |
| Hiking Gris | Sac à dos exosquelette anti-mal de dos de montagne Hiking Gris Gravipack | 72 | No | Yes / char 63 | No (end) | Yes | Yes (hyphenated) |
| Oslo 60+10L (€289) | Sac ergonomique de randonnée anti-mal de dos avec exosquelette | 62 | No | **No** | **No model name at all** | Yes | Yes (hyphenated) |
| Sherpa Kaki | Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur | 90 | No | Yes / char 68 | No (end) | Yes | Yes |
| Rome | Sac anti mal de dos business ROME ergonomique gravipack | 55 | Yes | Yes (lowercase) / char 46 | No | No | Yes |

**Summary:** 6/7 titles are over 60 chars. 2/7 have no brand. 1/7 has no model name. 7/7 target 'mal de dos' and 6/7 target 'exosquelette'. Hyphenation ('anti mal de dos' vs 'anti-mal de dos') and brand casing are inconsistent. 'anti douleur' is a health claim inside a product title.

## Catalogue inventory reconstructed from relayed evidence (NOT re-verified)

| Model | Segment (inferred from title / source) | Capacity | Colour(s) seen | Price seen | Channel(s) where seen | Source |
|---|---|---|---|---|---|---|
| Sherpa | Randonnée / montagne | 45 L (Decathlon listing name 'Sherpa 45') | Kaki; another colour (title without colour) | ~€249 (forum mention, channel and model not tied precisely) | gravipack.com, Decathlon marketplace | relayed SERP titles; decathlon.fr/brands/gravipack; outzer.fr review |
| Hiking | Randonnée / montagne | 33 L (Decathlon 'Hiking 33') | Gris | unknown | gravipack.com, Decathlon marketplace | relayed |
| Oslo | Randonnée (trekking) | 60+10 L | unknown | €289 | gravipack.com | relayed |
| Austerlitz | Urbain / léger | unknown | unknown | unknown | gravipack.com | relayed |
| Rome | Business / ordinateur | unknown | unknown | unknown | gravipack.com | relayed |
| Feather | Scolaire (cartable) | unknown | unknown | unknown | Decathlon marketplace; KissKissBankBank campaign | relayed |
| City Connect | Urbain (crowdfunding-era name) | unknown | unknown | unknown | KissKissBankBank | relayed |
| Business Talk | Business (crowdfunding-era name) | unknown | unknown | unknown | KissKissBankBank | relayed |
| Road Adventure | Voyage / outdoor (crowdfunding-era name) | unknown | unknown | unknown | KissKissBankBank | relayed |

Not possible to determine without searches or site access: full model list, GTINs, current prices per channel, stock, colourways per model, and whether colours are separate URLs.

## Third-party / channel / entity inventory (relayed by the orchestrator, status = not re-verified here)

| Source | Type | What was relayed | SEO relevance | Verification needed |
|---|---|---|---|---|
| gravipack.com and www.gravipack.com | Official store (WooCommerce-style /boutique-gravipack/, /produit/…) | Both hosts appear in results | Duplicate host indexing | Redirect and canonical check |
| gravipack.fr | Audited domain | site:gravipack.fr returned nothing | Domain consolidation | Check 301 to .com |
| decathlon.fr/brands/gravipack | Marketplace brand page | Sherpa 45, Hiking 33, Feather; ~€249 on a forum | Channel cannibalisation, price parity | Seller name, prices, reviews |
| es.trustpilot.com/review/gravipack.com | Review platform | Profile exists (shown on ES locale) | Brand SERP trust | Review count, rating, reply rate |
| outzer.fr | Editorial review | Critical review of Sherpa 45 | Negative brand+model SERP result | Ranking position for 'gravipack sherpa avis' |
| randonner-leger.org | Forum | Threads doubting the scientific study | Trust / E-E-A-T, brand SERP | Ranking position, sentiment |
| challenge.ma | Press | Says 'premier sac à dos remboursé par la sécurité sociale'; tested by French Army / Foreign Legion 2017 | Health claim that needs substantiation | Is the claim true (LPPR code)? |
| journaldugeek.com (2021), neozone.org | Tech press | Coverage | Earned links and mentions | Link status |
| lespepitestech.com | Startup directory | French Tech Aix-Marseille / Région Sud | Entity / citation | NAP shown |
| KissKissBankBank | Crowdfunding | Feather, City Connect, Business Talk, Road Adventure | Legacy model names | Links to the official site |
| motherbase.ai | Unknown / AI directory | Mentioned | Entity | Content |
| 'Kid'abord (Loire-Atlantique)' | Possible related company | One search summary linked it to the brand | Entity confusion risk | **Unverified, may be a false association** |

## Ready-to-run query backlog for the follow-up turn (not executed)

| Purpose | Queries |
|---|---|
| Marketplaces | `gravipack amazon.fr`, `gravipack cdiscount`, `gravipack fnac`, `gravipack rakuten`, `gravipack manomano`, `gravipack alltricks`, `gravipack galeries lafayette`, `site:decathlon.fr gravipack`, `gravipack pharmacie`, `gravipack orthopédie` |
| Price parity | `gravipack sherpa 45 prix`, `gravipack hiking 33 prix`, `gravipack oslo 60+10 prix`, `gravipack feather prix`, `gravipack rome prix`, `gravipack austerlitz prix` |
| Reviews | `gravipack avis`, `gravipack sherpa avis`, `gravipack trustpilot`, `gravipack avis vérifiés`, `gravipack decathlon avis` |
| Competitor SERPs (FR) | `sac à dos anti mal de dos`, `sac à dos ergonomique mal de dos`, `sac de randonnée report de charge`, `sac à dos dos ventilé confortable`, `cartable ergonomique mal de dos`, `sac à dos ordinateur ergonomique`, `meilleur sac de randonnée confortable 2026`, `sac à dos exosquelette`, `osprey anti-gravity avis`, `deuter aircontact avis` |
| Entity / NAP | `gravipack societe.com`, `gravipack pappers`, `gravipack SIREN`, `gravipack pagesjaunes`, `gravipack linkedin`, `gravipack adresse Aix`, `"Kid'abord" gravipack`, `Mohammed Errafi gravipack` |
| Retail / B2B | `gravipack revendeur`, `gravipack points de vente`, `gravipack entreprise`, `gravipack armée`, `gravipack CE CSE`, `gravipack médecine du travail` |
| Health claim | `gravipack sécurité sociale remboursement`, `gravipack LPPR`, `gravipack étude scientifique`, `gravipack dispositif médical` |

## Proposed keyword-to-URL map (to validate with search volume data)

| Intent cluster (FR) | Target URL type (proposed) | Example slug | Primary keyword | Notes |
|---|---|---|---|---|
| Brand + concept | Homepage | / | gravipack, sac exosquelette | Only page that owns 'exosquelette' at head level |
| Back-pain backpack (commercial) | Category hub | /sac-a-dos-anti-mal-de-dos/ | sac à dos anti mal de dos | Substantiated wording; links to every segment |
| Hiking | Category | /sac-de-randonnee-ergonomique/ | sac de randonnée ergonomique / léger | Sherpa, Hiking, Oslo |
| Urban / business | Category | /sac-a-dos-ordinateur-ergonomique/ | sac à dos ordinateur ergonomique | Rome, Austerlitz |
| School | Category | /cartable-ergonomique/ | cartable ergonomique / sac scolaire mal de dos | Feather; parent-oriented guide |
| Each model | Product (one URL per model, colours as variants) | /produit/sherpa-45/ | gravipack sherpa 45 | Model-first title |
| Proof | Evidence page | /etude-exosquelette/ | gravipack étude, efficacité | Methodology, authors, results |
| Comparison | Comparison pages | /comparatif/gravipack-vs-sac-randonnee-classique/ | gravipack vs … | Follow seo-competitor-pages fairness rules |
| B2B | Landing page | /entreprises/ | sac ergonomique entreprise / QVT | Quotes, bulk orders, CSE |

## Proposed comparison / alternatives pages (titles only; competitor facts must be sourced before publishing)

| Page type | Proposed H1 / title (FR) | Target query pattern | Prerequisite |
|---|---|---|---|
| X vs Y (architecture) | Exosquelette Gravipack vs ceinture lombaire classique : quelle différence pour le dos ? | gravipack vs sac de randonnée classique | Own study plus published load-transfer data |
| X vs Y (named) | Gravipack Sherpa 45 vs [concurrent 45 L] : comparatif 2026 | [modèle] vs [modèle] | Pick the competitor from real FR SERP data (not gathered here); cite the competitor's spec page; add 'prix au [date]' |
| Alternatives | Alternatives au [modèle concurrent] pour le mal de dos | alternative [modèle] | Only if SERPs show 'alternative' demand |
| Roundup / buying guide | Comment choisir un sac à dos quand on a mal au dos (guide 2026) | sac à dos mal de dos comment choisir | Expert author (kiné/ergonome), balanced, discloses own brand |
| Comparison table | Comparatif des sacs Gravipack : Sherpa, Hiking, Oslo, Rome, Austerlitz, Feather | gravipack quel modèle choisir | Internal; low risk; immediate |
