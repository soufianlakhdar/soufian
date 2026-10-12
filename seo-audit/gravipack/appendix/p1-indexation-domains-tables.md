# Data tables — indexation-domains (phase 1)

## 1. Domain / host inventory (what search shows per hostname)

| Host | Indexed URLs seen | Role observed | Evidence / notes |
|---|---|---|---|
| gravipack.fr | 0 | None. The user-supplied audit target has no indexed presence | site:gravipack.fr, "gravipack.fr", "www.gravipack.fr" and "gravipack.fr" sac à dos returned only third-party pages or gravipack.com URLs |
| www.gravipack.fr | 0 | None | same queries |
| gravipack.com (apex) | 40 | Home page, shop root, most product categories, ~20 products, legal pages, /contacts/, /nos-engagements/ | Home https://gravipack.com/ is indexed on the apex host |
| www.gravipack.com | 58 | Blog (/articles/, /categorie/*, posts), FAQ, /contact-gravipack/, about, ~25 products, taxonomy archives, parameter URLs | Mixed with apex. A site:www.gravipack.com query returned apex URLs too |
| presta.gravipack.com | 16 | Legacy PrestaShop store: home, categories, 6 products, CMS shipping page, site-map page, study page, Lépine page | Prices and models out of date (Sherpa 45 at 249 €, Feather, Safar Vibe, Road Adventure) |
| gravipack.eu / .de / .ma / .net | 0 | None found | quoted-domain query |
| shop./blog./boutique./en.gravipack.* | 0 | None found | quoted-subdomain query |
| http:// variants | 0 | No non-HTTPS URL surfaced | "http://gravipack.com" OR "http://www.gravipack.com" |

## 2. URL inventory: gravipack.com + www.gravipack.com (98 URLs, SERP titles as shown, char counts)

| # | Host | Path | SERP title (as shown) | Title chars | URL chars | Type |
|---|---|---|---|---|---|---|
| 1 | (apex) | `/` | Gravipack : le sac révolutionnaire anti mal de dos exosquelette | 63 | 22 | home |
| 2 | (apex) | `/?add-to-cart=6527` | Accueil - Le sac à dos exosquelette GRAVIPACK anti mal au dos | 61 | 39 | param-dup home |
| 3 | (apex) | `/boutique-gravipack/` | Boutique Gravipack | 18 | 41 | shop |
| 4 | www. | `/boutique-gravipack/page/2/` | Boutique Gravipack | 18 | 52 | shop pagination |
| 5 | www. | `/boutique-gravipack/?order=price` | Boutique Gravipack | 18 | 57 | shop sort param |
| 6 | www. | `/boutique-gravipack/?order=price&filter_product_cat=nouveau-sac-a-dos` | Boutique - Sac a dos anti mal de dos GRAVIPACK avec exosquelette allège le poids sur les épaules et le dos. | 107 | 94 | shop filter param |
| 7 | www. | `/boutique-gravipack/?add-to-cart=2678` | Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos. | 95 | 62 | shop add-to-cart param |
| 8 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/` | Achetez un sac à dos révolutionnaire avec exosquelette Gravipack | 64 | 73 | product cat |
| 9 | www. | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/page/2/` | Tous les sacs à dos anti-mal de dos exosquelette Gravipack | 58 | 84 | product cat p2 |
| 10 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-de-randonnee-montagne-trek-compostelle/` | Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS | 63 | 151 | product cat |
| 11 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-anti-mal-de-dos-scolaire-college-lycee-et-etudiant/` | Sac à dos exosquelette scolaire Gravipack allège le poids de 92% | 64 | 147 | product cat |
| 12 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-ordinateur-anti-mal-de-dos-business-tele-travail-professionnel/` | Sac à dos exosquelette anti-mal de dos business voyage d'affaires | 65 | 140 | product cat |
| 13 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-voyage-gravipack-anti-mal-de-dos/` | Sac à dos exosquelette de voyage Gravipack, léger et prêt à partir | 66 | 129 | product cat |
| 14 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-urbain/` | Sac à dos exosquelette urbain Gravipack allege le poids sur le dos | 66 | 90 | product cat |
| 15 | www. | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-medical/` | Sac à dos médical Gravipack allégez vos missions sauvez des vies | 64 | 95 | product cat |
| 16 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-militaire-tactique-assault-anti-mal-de-dos/` | Sac à dos exosquelette militaire d'assault allège le poids Gravipack | 68 | 139 | product cat |
| 17 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/sac-a-dos-exosquelette-outillage-gravipack-anti-mal-de-dos-professionnel/` | Sac à dos exosquelette pour l'outillage professionnel Gravipack | 63 | 146 | product cat |
| 18 | (apex) | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/claie-de-portage/` | Claie de portage Gravipack anti-TMS pour charges très lourdes | 61 | 90 | product cat |
| 19 | www. | `/categorie-produit/tous-les-sacs-a-dos-exosquelette/nouveaux-sacs-a-dos-gravipack-exosquelette-confort-et-innovation/` | Nouveaux sacs à dos Gravipack exosquelette, confort et innovation | 65 | 142 | product cat |
| 20 | www. | `/categorie-produit/accessoires-sac-a-dos/` | Accessoires sac à dos Archives - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 104 | 66 | product cat |
| 21 | www. | `/attribut-produit/accessoires/exosquelette-gravipack/` | Archives des Exosquelette Gravipack - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 109 | 78 | attribute archive |
| 22 | www. | `/attribut-produit/accessoires/poches-frontales/` | Archives des Poches frontales - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 103 | 72 | attribute archive |
| 23 | www. | `/etiquette-produit/precommande/` | Précommande - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos. | 109 | 56 | product tag archive |
| 24 | www. | `/produit/sac-a-dos-ergonomique-anti-mal-de-dos-avec-exosquelette-centurion-gravipack/` | Sac à dos ergonomique anti-mal de dos avec exosquelette Gravipack | 65 | 110 | product |
| 25 | www. | `/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/` | Sac randonner léger anti mal de dos exosquelette Pearl Gravipack | 64 | 103 | product |
| 26 | www. | `/produit-gravipack/sac-a-dos-exosquelette-gravipack-pearl/` | Sac à dos de voyage Pearl femme muni de l'exosquelette innovant Gravipack | 73 | 83 | product alt path |
| 27 | (apex) | `/produit/sac-a-dos-exosquelette-de-montagne-sherpa-bleu-gravipack-anti-mal-de-dos/` | Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa | 65 | 103 | product |
| 28 | (apex) | `/produit/sac-a-dos-de-montagne-sherpa-45l-orange-anti-mal-de-dos-orange-avec-exosquelette-gravipack-ideal-pour-la-randonnee/` | Sac anti mal de dos exosquelette de montagne Sherpa orange (also shown as: Sac randonner léger anti-mal de dos avec exosquelette) | 58 | 145 | product |
| 29 | www. | `/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-gravipack-anti-mal-de-dos-legerete-en-haute-montagne/` | Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur | 90 | 127 | product |
| 30 | (apex) | `/produit-gravipack/sac-a-dos-sherpa-kaki` | Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur | 90 | 61 | product alt path |
| 31 | (apex) | `/produit-gravipack/sac-a-dos-sherpa` | Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur | 90 | 56 | product alt path |
| 32 | (apex) | `/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-easy-travel-gravipack/` | Sac à dos randonnée & business avec exosquelette anti-mal de dos (also shown as: Sac à dos exosquelette anti-mal de dos Gravipack Business et Outdoor) | 64 | 106 | product |
| 33 | www. | `/produit/sac-a-dos-randonnee-80l-revolutionnaire-anti-mal-de-dos-pas-cher-gravipack-compostelle-80l-ergonomie-eva-haute-performance-bretelles-memoire-de-forme-adaptatives/` | Sac à dos randonnée 80L révolutionnaire anti mal de dos pas cher | 64 | 196 | product |
| 34 | www. | `/produit/sac-a-dos-de-survie-35-litres-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme/` | Sac à dos de Survie 35 litres Compostelle Gravipack - Montagne et randonnée EVA ergonomique mémoire de forme - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 182 | 141 | product |
| 35 | www. | `/produit/sac-a-dos-de-survie-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme/` | Sac à dos de survie 25 litres Compostelle Gravipack - Montagne et randonnée EVA ergonomique mémoire de forme - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 182 | 131 | product |
| 36 | www. | `/produit/sac-anti-mal-de-dos-de-survie-65-litres-ergonomique-compostelle-gravipack-montagne-et-randonnee-eva-ergonomique-memoire-de-forme-copie/` | Sac anti mal de dos de Survie 65 litres ergonomique Compostelle Gravipack - Montagne et randonnée EVA ergonomique mémoire de forme - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 204 | 169 | product |
| 37 | www. | `/produit/sac-randonner-leger-anti-mal-de-dos-avec-exosquelette-helsinki-gravipack-60l-10l-70l/` | Sac à dos GRAVIPACK exosquelette 60+10 L : soulage le dos et les épaules, répartit la charge. Recommandé pour randonnée et port prolongé | 136 | 119 | product |
| 38 | (apex) | `/produit/sac-de-randonnee-anti-mal-de-dos-avec-exosquelette-oslo-rouge-gravipack-60l-10l/` | Sac ergonomique de randonnée anti-mal de dos avec exosquelette | 62 | 110 | product |
| 39 | (apex) | `/produit/sac-a-dos-hiking-30l-gris-avec-exosquelette-gravipack-anti-mal-de-dos-confort-en-randonnee/` | Sac à dos exosquelette anti-mal de dos de montagne Hiking Gris Gravipack | 72 | 121 | product |
| 40 | www. | `/produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-avec-exosquelette-gravipack-pour-toutes-vos-aventures/` | Sac ergonomique de randonnée anti mal de dos avec exosquelette Hiking Terracotta Gravipack | 90 | 161 | product |
| 41 | (apex) | `/produit-gravipack/sac-a-dos-revolutionnaire` | Sac ergonomique de randonnée anti mal de dos avec exosquelette Hiking Terracotta Gravipack | 90 | 65 | product alt path |
| 42 | (apex) | `/produit/sac-a-dos-innovant-utilise-la-technologie-gravipack-la-seule-au-monde-pour-reduire-efficacement-le-poids-sur-le-dos/` | Sac à dos Tokyo Gravipack, anti-mal de dos, randonnée, vélo & travail avec exosquelette intégré | 95 | 146 | product |
| 43 | www. | `/produit/sac-a-dos-austerlitz-tactique-hybride-avec-exosquelette-gravipack-anti-mal-de-dos/` | Sac à dos léger et ergonomique anti-mal de dos avec exosquelette Gravipack Austerlitz | 85 | 116 | product |
| 44 | (apex) | `/produit/sac-a-dos-exosquelette-professionnel-et-velo-rome-gravipack-anti-mal-de-dos/` | Sac anti mal de dos business ROME ergonomique gravipack (also shown as: Sac anti mal de dos business, ergonomie pour le dos, avec exosquelette) | 55 | 106 | product |
| 45 | (apex) | `/produit/sac-a-dos-college-lycee-anti-mal-de-dos-avec-exosquelette-g-pack-gravipack/` | Sac à dos exosquelette révolutionnaire et unique G-Pack Gravipack | 65 | 105 | product |
| 46 | www. | `/produit/sac-anti-mal-de-dos-pour-la-journee-g-pack-avec-exosquelette-gravipack-pour-professionnels-et-velo/` | Sac à dos exosquelette révolutionnaire et unique G-Pack Gravipack | 65 | 133 | product |
| 47 | www. | `/produit/anti-mal-de-dos-certainement-le-meilleur-sac-au-monde-pour-le-travail-et-le-velo-sac-a-dos-ordinateur-city-avec-exosquelette-gravipack-anti-mal-de-dos-elegance-et-confort/` | Sac à dos exosquelette révolutionnaire City Gravipack | 53 | 205 | product |
| 48 | www. | `/produit/sac-a-dos-teletravail-kingston-avec-exosquelette-gravipack-anti-mal-de-dos-ergonomie-impressionnante/` | Sac à dos ergonomique ordinateur, business et scolaire petite taille - Gravipack exosquelette Kingston anti-mal de dos | 118 | 135 | product |
| 49 | www. | `/produit/sac-a-dos-ordinateur-ergonomique-anti-mal-de-dos-avec-exosquelette-business-talk-v4-gravipack-20l/` | Sac à dos exosquelette révolutionnaire Business Talk V4 Gravipack | 65 | 132 | product |
| 50 | www. | `/produit/sac-a-dos-exosquelette-25l-anti-mal-de-dos-pour-deux-ordinateurs-gravipack-business-talk-v4-revolutionnaire/` | Sac à dos exosquelette 25L anti-mal de dos pour deux ordinateurs | 64 | 142 | product |
| 51 | www. | `/produit/sac-a-dos-ordinateur-25l-anti-mal-de-dos-revolutionnaire-gravipack-business-talk-v4-ergonomie-eva-memoire-de-forme/` | Sac à dos ordinateur 25L anti-mal de dos révolutionnaire | 56 | 149 | product |
| 52 | (apex) | `/produit/sac-a-dos-exosquelette-cabine-avion-extensible-dublin-gravipack-anti-mal-de-dos/` | Sac a dos ergonomique léger avec exosquelette anti-mal de dos - cabine et extensible Dublin Gravipack | 101 | 110 | product |
| 53 | (apex) | `/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/` | Sac à dos outillage anti-douleur exosquelette Gravipack® (also shown as: Sac à dos porte outil anti-douleur avec exosquelette) | 56 | 106 | product |
| 54 | www. | `/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/` | Sac à dos outillage anti-douleur exosquelette Gravipack® | 56 | 106 | product |
| 55 | www. | `/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/` | Sac anti-mal au dos innovant outillage Light Promax de Gravipack | 64 | 96 | product |
| 56 | www. | `/produit/sac-anti-mal-de-dos-exosquelette-porte-outils-exotool-gravipack/` | Sac à dos léger anti-mal de dos exosquelette porte-outils Gravipack | 67 | 98 | product |
| 57 | www. | `/produit/sac-anti-mal-de-dos-exosquelette-outillage-toolmaster-orange-gravipack/` | Sac outillage anti-mal de dos exosquelette | 42 | 105 | product |
| 58 | www. | `/produit/claie-de-portage-exosquelette-cargo-max-gravipack-anti-mal-de-dos/` | Claie de portage aluminium exosquelette Gravipack pour charges lourdes | 70 | 100 | product |
| 59 | www. | `/produit/claie-de-portage-aluminium-exosquelette-anti-mal-de-dos-cargo-max-gravipack/` | Claie de portage aluminium exosquelette Gravipack pour charges lourdes | 70 | 110 | product |
| 60 | (apex) | `/produit/fourreau-de-portage-exosquelette-gravitech-anti-mal-de-dos-gravipack/` | Claie de portage révolutionnaire exosquelette anti-mal de dos (snippet names it 'Barracuda') | 61 | 99 | product |
| 61 | www. | `/produit/batterie-solaire-externe-multi-port-avec-lampe-torche-et-boussole-infinity-gravipack-copie/` | Batterie solaire externe multi-port avec lampe torche et boussole | 65 | 125 | product |
| 62 | www. | `/produit/lien-de-paiement-unique-pour-votre-commande-personnalisee-gravipack/` | Lien de paiement pour votre commande personnalisée Gravipack® | 61 | 102 | utility product |
| 63 | (apex) | `/produit/fabrication-professionnelle-gravipack/` | fabrication professionnelle, cadeaux d'entreprise et objets publicitaires haut de gamme. | 88 | 68 | service product |
| 64 | (apex) | `/produit/boucle-de-sangle-abdominale-pour-sac-a-dos-exosquelette-gravipack/` | Boucle de sangle abdominale pour sac à dos exosquelette Gravipack® | 66 | 96 | accessory |
| 65 | www. | `/produit/porte-cle-flamme-gravipack-noir-en-tissu-brode-premium-accessoire-pour-sac-a-dos-exosquelette-et-cles/` | Porte-clé flamme Gravipack noir en tissu brodé, accessoire chic | 63 | 136 | accessory |
| 66 | www. | `/produit/porte-outils-elastique-amovible-velcro-oganizer-gravipack/` | Porte-outils élastique amovible Velcro | 38 | 92 | accessory |
| 67 | (apex) | `/produit/bracelet-de-survie-en-paracorde-tressee-avec-boucle-a-clip-paracord-blanc-violet-gravipack/` | Bracelets de survie en paracorde tressée avec boucle blanc violet | 65 | 121 | accessory |
| 68 | www. | `/produit/coussinets-bretelles-exosquelette-accessoire-confort/` | Coussinets de sac à dos, poitrine et confort, bretelles exosquelette Gravipack | 78 | 87 | accessory |
| 69 | (apex) | `/produit/dragonne-en-corde-tressee-mousqueton-pivotant-rope-orange-gravipack/` | Dragonne en corde tressée mousqueton pivotant orange | 52 | 98 | accessory |
| 70 | (apex) | `/mentions-legales/` | Le sac à dos ergonomique - Mentions légales, tout ce que vous devez savoir sur Gravipack. | 89 | 39 | legal |
| 71 | (apex) | `/conditions-generales-de-vente/` | Conditions Générales de Vente des sacs anti mal de dos exosquelette Gravipack | 77 | 52 | legal |
| 72 | www. | `/faq/` | Foire Aux Questions des sacs à dos exosquelettes Gravipack | 58 | 30 | faq |
| 73 | www. | `/contact-gravipack/` | Contactez Gravipack | 19 | 44 | contact |
| 74 | (apex) | `/contacts/` | Contacts - Le sac à dos exosquelette GRAVIPACK anti mal au dos | 62 | 31 | contact dup |
| 75 | (apex) | `/nos-engagements/` | Nos engagements (also shown as: GraviPack®) | 15 | 38 | about |
| 76 | www. | `/a-propos-de-nous-gravipack-au-service-de-votre-dos/` | Le sac anti mal de dos léger Gravipack au service de votre dos et de vos épaules | 80 | 77 | about |
| 77 | www. | `/gravipackers/` | Gravipackers - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 86 | 39 | testimonials |
| 78 | www. | `/articles/` | Articles - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 82 | 35 | blog index |
| 79 | www. | `/actualites-gravipack-2/` | Découvrez toutes les actualités sur l'innovation Gravipack | 58 | 49 | news index |
| 80 | www. | `/categorie/innovation/` | Innovation Archives - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 93 | 47 | blog cat |
| 81 | www. | `/categorie/technologie/` | Technologie Archives - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 94 | 48 | blog cat |
| 82 | www. | `/categorie/militaire/` | Militaire Archives - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 92 | 46 | blog cat |
| 83 | (apex) | `/categorie/outillage/` | Outillage Archives - Sac à dos exosquelette anti-mal de dos | 59 | 42 | blog cat |
| 84 | www. | `/category/gravipack-engage-dans-le-handicap-et-l-inclusion/` | Actualité Handicap - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos. | 116 | 84 | blog cat (2nd base) |
| 85 | www. | `/gravipack-soulage-les-forces-speciales-au-sofins/` | Gravipack soulage les forces spéciales au SOFINS | 48 | 75 | post |
| 86 | www. | `/test/` | Gravipack soulage les forces spéciales au SOFINS - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 122 | 31 | test dup post |
| 87 | (apex) | `/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/` | Un sac à dos pas comme les autres… les épaules de vos enfants vont adorer | 73 | 79 | post |
| 88 | www. | `/cest-une-veritable-revolution-pour-le-marche-colossal-du-sac-dos/` | Cette innovation ergonomique française protège vos épaules et soulage votre dos. - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant | 154 | 91 | post |
| 89 | (apex) | `/gravipack-recompense-et-pret-a-conquerir-le-monde-du-portage/` | Gravipack, récompensé et prêt à conquérir le monde du portage | 61 | 83 | post |
| 90 | www. | `/et-si-votre-sac-a-dos-ne-pesait-presque-plus-rien/` | Et si votre sac à dos ne pesait presque plus rien ? | 51 | 76 | post |
| 91 | www. | `/letonnante-reconversion-du-footballeur-bacary-sagna/` | L’étonnante reconversion du footballeur Bacary Sagna, Gravipack. | 64 | 78 | post |
| 92 | www. | `/evolution-du-portage-de-sac-a-dos-jusqu-a-la-revolution-gravipack/` | L'évolution du portage de sac à dos jusqu'à la révolution Gravipack | 67 | 92 | post |
| 93 | (apex) | `/inventeur-dun-sac-a-dos-en-apesanteur/` | Le sac à dos en apesanteur anti-mal de dos allège le poids de 92% | 65 | 60 | post |
| 94 | www. | `/le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/` | Le droit de la propriété industrielle expliqué avec Gravipack | 61 | 97 | post |
| 95 | www. | `/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/` | Gravipack : le sac anti mal de dos primé au Concours Lépine | 59 | 84 | post |
| 96 | www. | `/et-si-tout-commencait-par-un-sac-trop-lourd-et-un-reve-de-le-rendre-leger-pour-tous/` | Et si tout commençait par un sac trop lourd… et un rêve ? | 57 | 110 | post |
| 97 | (apex) | `/gravipack-au-salon-vivatech-cet-outil-de-pointe-au-service-des-voyageurs-et-des-agents-du-metro-le-parisien/` | Sac à dos porte-outils exosquelette Gravipack des agents RATP | 61 | 130 | post |
| 98 | (apex) | `/le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/` | Gravipack : le porte-outils anti-mal de dos utilisé par la RATP ... | 67 | 88 | post |

## 3. Legacy subdomain inventory: presta.gravipack.com (16 URLs)

| # | Path | SERP title (as shown) | Title chars | Type | Conflict with main site |
|---|---|---|---|---|---|
| 1 | `/` | Gravipack, le sac a dos scolaire, business et randonnée, ce sac à dos allègent le poids sur le dos pour une meilleure posture. | 126 | legacy home | Competes with https://gravipack.com/ for the brand |
| 2 | `/2-accueil` | Accueil - Gravipack | 19 | legacy cat | n/a |
| 3 | `/22-produit` | L'univers des sacs à dos Gravipack se décline en plusieurs collections | 70 | legacy cat | vs /categorie-produit/tous-les-sacs-a-dos-exosquelette/ |
| 4 | `/24-sac-a-dos-sport` | Sac à dos de randonnée Gravipack soulagera vos épaules et votre dos. | 68 | legacy cat | vs hiking category |
| 5 | `/72-sac-a-dos-scolaire` | Sac a dos scolaire Gravipack, le sac à dos qui soulage le poids des épaules et du dos. | 86 | legacy cat | vs school category |
| 6 | `/73-gravipack` | Gravipack, le sac à dos en apesanteur qui ne fait pas mal au dos et aux épaules | 79 | legacy cat | n/a |
| 7 | `/40-etude-scientifique-soulage-le-dos-gravipack` | L'étude scientifique du sac à dos en apesanteur Gravipack. | 58 | study page | Only indexed study page (LBMC / Faculté de Médecine Lyon-Sud). No equivalent seen on gravipack.com |
| 8 | `/59-concours-lepine-medaille-argent-meilleur-sac-a-dos-gravipack` | Le concours Lépine médaille le sac à dos en apesanteur Gravipack. | 65 | award page | vs www /gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/ |
| 9 | `/plan-du-site-gravipack` | Plan du site Gravipack le sac a dos en apesanteur qui révolutionne le monde | 75 | HTML sitemap | n/a |
| 10 | `/content/1-livraison-sac-a-dos-gravipack` | Sac à dos scolaire, randonnée, sport, Gravipack le meilleur sac a dos au monde - livraison client | 97 | CMS shipping | Says orders are 'commandes de réservation', 2-3 months; main CGV/products say 1-2 days in France |
| 11 | `/accueil/13-sac-a-dos-gravipack-safar-vibe.html` | sac à dos safar vibe - Gravipack | 32 | product (199 €) | Model not seen on main site |
| 12 | `/accueil/15-sac-a-dos-gravipack-business-talk.html` | sac à dos business talk - Gravipack | 35 | product (199 €) | vs Business Talk V4 (129-149 €) |
| 13 | `/accueil/16-sac-a-dos-gravipack-hikking33.html` | Le seul sac à dos au monde qui allège le poids Hiking 33 Gravipack. | 67 | product (229 €) | vs Hiking Terracotta/Gris (89-129 €); typo 'hikking' |
| 14 | `/accueil/17-sac-a-dos-gravipack-road-adventure.html` | Sac à dos en apesanteur Road Adventure Gravipack contre le mal de dos. | 70 | product (199 €) | Model not seen on main site |
| 15 | `/accueil/19-sac-a-dos-gravipack-sherpa-45.html` | Sac à dos Sherpa 45 Gravipack - Le meilleur sac à dos de montagne. | 66 | product (249 €) | vs Sherpa bleu/orange/kaki (99-149,90 €) |
| 16 | `/accueil/21-sac-a-dos-gravipack-feather.html` | Sac à dos scolaire Feather Gravipack contre le mal de dos. | 58 | product (149 €) | Model not seen on main site |

## 4. Duplicate / near-duplicate URL clusters (same entity, several indexed URLs)

| Cluster | Indexed URLs | Evidence of duplication |
|---|---|---|
| Light Promax tool bag | apex `/produit/sac-a-dos-porte-outil-anti-douleur-avec-exosquelette-light-promax-gravipack/`; www `/produit/sac-a-dos-exosquelette-outillage-light-promax-gravipack-anti-mal-de-dos/`; www `/produit/sac-anti-mal-de-dos-exosquelette-outillage-parcours-gravipack/` | First two have the identical title 'Sac à dos outillage anti-douleur exosquelette Gravipack®'. The third is titled '…Light Promax de Gravipack'. Prices 169,90 € vs 169,00 € |
| Cargo Max carrying frame | www `/produit/claie-de-portage-exosquelette-cargo-max-gravipack-anti-mal-de-dos/`; www `/produit/claie-de-portage-aluminium-exosquelette-anti-mal-de-dos-cargo-max-gravipack/` | Identical title 'Claie de portage aluminium exosquelette Gravipack pour charges lourdes' |
| G-Pack | apex `/produit/sac-a-dos-college-lycee-anti-mal-de-dos-avec-exosquelette-g-pack-gravipack/`; www `/produit/sac-anti-mal-de-dos-pour-la-journee-g-pack-avec-exosquelette-gravipack-pour-professionnels-et-velo/` | Identical title 'Sac à dos exosquelette révolutionnaire et unique G-Pack Gravipack' |
| Hiking Terracotta | www `/produit/sac-a-dos-revolutionnaire-anti-mal-de-dos-de-randonnee-hiking-terracotta-…/`; apex `/produit-gravipack/sac-a-dos-revolutionnaire` | Identical title |
| Sherpa Kaki | www `/produit/sac-a-dos-sherpa-kaki-avec-exosquelette-…/`; apex `/produit-gravipack/sac-a-dos-sherpa-kaki`; apex `/produit-gravipack/sac-a-dos-sherpa` | Identical title on all 3 |
| Pearl | www `/produit/sac-a-dos-anti-mal-de-dos-de-voyage-pearl-29l-gris-avec-exosquelette/`; www `/produit-gravipack/sac-a-dos-exosquelette-gravipack-pearl/` | Same model on a second path base |
| Business Talk V4 | 20L `/produit/sac-a-dos-ordinateur-ergonomique-…-business-talk-v4-gravipack-20l/`; 25L `/produit/sac-a-dos-exosquelette-25l-…-business-talk-v4-revolutionnaire/`; 25L `/produit/sac-a-dos-ordinateur-25l-…-business-talk-v4-ergonomie-eva-memoire-de-forme/` | Two separate 25L product pages for one model |
| Compostelle 65L | `/produit/sac-anti-mal-de-dos-de-survie-65-litres-…-memoire-de-forme-copie/` | WooCommerce 'Duplicate product' slug suffix '-copie' |
| Infinity power bank | `/produit/batterie-solaire-externe-…-infinity-gravipack-copie/` | '-copie' slug |
| SOFINS post | `/gravipack-soulage-les-forces-speciales-au-sofins/` + `/test/` | Same title; /test/ is a draft copy |
| Contact | www `/contact-gravipack/` + apex `/contacts/` | Two contact pages |
| News index | `/actualites-gravipack-2/` (+ `/articles/`) | '-2' suffix means a page with slug 'actualites-gravipack' exists or existed |
| RATP story | `/gravipack-au-salon-vivatech-…-le-parisien/` + `/le-porte-outils-anti-mal-de-dos-gravipack-soulage-les-agents-ratp/` | Same topic in 2 posts |
| Home | `/` + `/?add-to-cart=6527` | Parameter duplicate of the home page with a different (older) title |
| Shop | `/boutique-gravipack/`, `/page/2/`, `?order=price`, `?order=price&filter_product_cat=…`, `?add-to-cart=2678` | 5 indexed shop variants |
| Lépine award | www `/gravipack-le-sac-anti-mal-de-dos-prime-au-concours-lepine/` + presta `/59-concours-lepine-…` | Cross-host duplicate topic |
| Blog category base | `/categorie/…` and `/category/…` | Two taxonomy bases indexed |

## 5. Title-template variants (site-name suffixes) and titles that changed between queries

| Pattern | Example URL | Note |
|---|---|---|
| ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant' (73-char suffix) | /articles/, /categorie/innovation/, /test/, Compostelle products, /gravipackers/ | Current default WordPress/SEO-plugin %%sitename%% / tagline |
| ' - Sac à dos exosquelette anti-mal de dos' | /categorie/outillage/ | 2nd suffix variant |
| ' - Le sac à dos exosquelette GRAVIPACK anti mal au dos' | /contacts/, /?add-to-cart=6527 | 3rd variant (older site title) |
| ' - Sac a dos exosquelette anti-mal de dos Gravipack qui allège le poids sur les épaules et le dos.' | /category/gravipack-engage-…, /etiquette-produit/precommande/, /boutique-gravipack/?add-to-cart=2678 | 4th variant |
| 'XXX Archives - …' / 'Archives des XXX - …' | /categorie-produit/accessoires-sac-a-dos/, /attribut-produit/… | Default archive template not customised |
| Same URL, two titles | /nos-engagements/: 'Nos engagements' vs 'GraviPack®' | Rewrite or recent edit |
| Same URL, two titles | Easy Travel: 'Sac à dos randonnée & business avec exosquelette anti-mal de dos' vs 'Sac à dos exosquelette anti-mal de dos Gravipack Business et Outdoor' | Rewrite or recent edit |
| Same URL, two titles | Sherpa orange: 'Sac anti mal de dos exosquelette de montagne Sherpa orange' vs 'Sac randonner léger anti-mal de dos avec exosquelette' | Rewrite or recent edit |
| Same URL, two titles | Rome: 'Sac anti mal de dos business ROME ergonomique gravipack' vs 'Sac anti mal de dos business, ergonomie pour le dos, avec exosquelette' | Rewrite or recent edit |
| Same URL, two titles | Light Promax (apex): 'Sac à dos outillage anti-douleur exosquelette Gravipack®' vs 'Sac à dos porte outil anti-douleur avec exosquelette' | Rewrite or recent edit |

## 6. Aggregate SERP-signal statistics (98 main-domain URLs)

| Metric | Value | claude-seo threshold |
|---|---|---|
| URLs > 100 characters (all main) | 42 / 98 | seo-technical: flag > 100 |
| Product URLs > 100 characters | 30 / 39 | flag > 100 |
| Median product URL length | 110 chars | < 100 |
| Longest URL | 205 chars (City product) | < 100 |
| SERP titles > 60 chars | 76 / 98 | quality-gates: max 60 |
| SERP titles < 30 chars | 5 (Boutique Gravipack ×3, Contactez Gravipack, Nos engagements) | min 30 |
| Longest title | 204 chars (Compostelle 65L) | 60 |
| Median title length | 65 chars | 50-60 |
| Titles containing 'anti mal de dos' / 'anti-mal de dos' / 'anti mal au dos' | 53 / 98 | unique intent per page |
| Product titles containing it | 28 / 39 | n/a |
| Slugs containing 'anti-mal-de-dos' | 37 | n/a |
| Titles containing 'exosquelette' | 66 / 98 | n/a |
| Identical titles shared by ≥2 URLs | 6 clusters (Light Promax, Cargo Max, G-Pack, Hiking Terracotta, Sherpa Kaki ×3, Boutique Gravipack ×3) | must be unique |
| Non-HTTPS URLs | 0 | HTTPS only |

## 7. Keyword cannibalisation map (title-based, plus result order in WebSearch; not Google.fr positions)

| Query (FR) | Gravipack URLs whose SERP title targets it | Result order observed in WebSearch |
|---|---|---|
| sac à dos anti mal de dos | Home ('…sac révolutionnaire anti mal de dos exosquelette'), Pearl, Tokyo, Centurion, Austerlitz, Rome, Dublin, Kingston, about page ('Le sac anti mal de dos léger Gravipack…'), CGV ('…des sacs anti mal de dos…'), /categorie-produit/…/page/2/, /boutique-gravipack/?add-to-cart=2678, /etiquette-produit/precommande/, /category/…handicap…, presta /73-gravipack | 1 ici.fr (France Bleu Lépine show), 2 ergo-corner.com/55-gravipack, 3 ergo-corner.com/content/13-le-sac-a-dos-gravipack, 4 gravipack.com/ (home), 5 www Pearl, 6 apex Tokyo, 7 arsayo.com, 8 ergo-corner blog, 9 oqlf |
| sac à dos anti mal de dos exosquelette | Same set + Light Promax, outillage category | 1 ergo-corner.com/55-gravipack, 2 Easy Travel, 3 Light Promax (www), 4 Centurion, 5 home, 6 Pearl, 7 outillage category, 8 Austerlitz, 9 Tokyo. Home is 5th behind 3 product pages and a reseller |
| sac à dos exosquelette | /categorie-produit/tous-les-sacs-a-dos-exosquelette/ ('Achetez un sac à dos révolutionnaire avec exosquelette Gravipack'), its /page/2/ ('Tous les sacs à dos anti-mal de dos exosquelette Gravipack'), Nouveaux sacs category, home, G-Pack ×2, City, Business Talk V4, Hiking Gris | 1 kentfaith.fr blog, 2 i-trekkings.net Oslo test, 3 alloprod.com, 4 ergo-corner.com, 5 compostelle-autrement.com, 6 gravipack category, 7 gravipack home, 8 decathlon.fr marketplace Hiking 33, 9 Google Patents |
| sac randonnée anti mal de dos | Hiking category ('Sac à dos exosquelette de randonnée anti-mal de dos et anti-TMS'), Sherpa bleu ('Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa'), Pearl ('Sac randonner léger…'), Sherpa orange (alt 'Sac randonner léger anti-mal de dos…'), Easy Travel (slug 'sac-randonner-leger-anti-mal-de-dos'), Helsinki (same slug pattern), Compostelle 80L ('Sac à dos randonnée 80L révolutionnaire anti mal de dos pas cher'), Oslo Rouge ('Sac ergonomique de randonnée anti-mal de dos avec exosquelette'), Hiking Terracotta, Hiking Gris, Sherpa Kaki, presta /24-sac-a-dos-sport | No Gravipack URL in the 9 results (randonner-leger.org ×3, glisshop.com guide, osprey.com ×2, decathlonpro.fr, alpinstore.com guide, allodocteurs.fr) |
| cartable / sac scolaire anti mal de dos | School category ('…scolaire Gravipack allège le poids de 92%'), G-Pack ×2, Kingston ('…scolaire petite taille…'), blog post /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/, presta /72-sac-a-dos-scolaire, presta Feather | No gravipack.com URL. Results were guides (pass-education.fr, maif.fr, 24matins.fr, dhnet.be) + maddyness.com mention |
| sac à dos ordinateur anti mal de dos (ergonomique, exosquelette) | Business category, City, Business Talk V4 ×3, Kingston, Rome, Centurion | No gravipack.com URL. Results: motherbase.ai, maddyness, allodocteurs, pearl.fr (Tucano Marte Gravity) ×3, Kensington, journaldugeek, ffrandonnee.fr |
| Gravipack (brand) | Home, boutique, every product | 1 kisskissbankbank.com/en/projects/gravipack, 2 youtube.com/@Gravipack, 3 equilibre-france-ergonomie.fr, 4 gravipack.com/, 5 boutique, 6 G-Pack, 7 nos-engagements, 8 Austerlitz, 9 Hiking Gris |
| gravipack avis | Tokyo product (embedded reviews), /gravipackers/ | 1 fr.trustpilot.com/review/gravipack.com, 2 fnac Hiking 33 avis, 3 outzer.fr Sherpa 45, 4 fnac Road Adventure avis, 5 ergo-corner, 6 lespepitestech, 7 gravipack Tokyo, 8 i-trekkings, 9 randonner-leger forum p2 |

## 8. Price / spec / availability inconsistencies visible in SERP snippets

| Product | Values seen (source page) | Note |
|---|---|---|
| Pearl 29L | 99,90 € / 119,00 € / 199 → 149,00 € / 89 € | Different snippets on gravipack.com |
| Hiking Terracotta 33L | 129,90 → 89,90 € (product), 89,00 € and 129,00 € (category) | |
| Hiking Gris | URL says '30l', page says 33 L; weight 1,6 kg vs Terracotta 1,1 kg | slug/spec mismatch |
| Oslo Rouge 60+10L | 289,00 € / 299,90 → 239,92 € / 149,90 € ('Nouveauté'); also called 'Oslo 70L' | |
| Austerlitz 35L | 79,90 € / 149 → 89,90 € / 129,00 € / up to 149,90 € | |
| Sherpa 45 | 149,90 € / 149,00 € / 149,90 → 99,00 € (main); 249 € (presta); Decathlon marketplace 249 → 149,90 € | |
| Business Talk V4 20L | 149 € vs 129 €; 'précommande … disponibilité prévue en juin 2026' | Stale preorder text as of Oct 2026 |
| Business Talk V4 25L | 129,90 € struck → 59,90 €; 'Prévente – Offre Early Bird : livraison garantie en août' | Stale preorder text |
| Rome 28L | 119,90 € / 94,90 €; 1,6 kg vs '20/30L' 1,9 kg | |
| Light Promax | 169,90 € / 169,00 € | across duplicate URLs |
| Delivery terms | Products/CGV: 1-2 days France; presta CMS: 'commandes de réservation', 2-3 months | legacy page contradicts main |

## 9. Entity / legal-identity signals seen in search (for Organization and knowledge-graph consistency)

| Source | Name / entity | Location | Other |
|---|---|---|---|
| gravipack.com/mentions-legales/ | Publisher EXOSQUELETTE LIGHT (SAS) | Paris | Host Gandi.net; contact@gravipack.com |
| gravipack.com/contacts/ + /contact-gravipack/ | Gravipack | 46 rue de la Bienfaisance, 94300 Vincennes | quote form for bulk/custom orders |
| societe.com | Établissement GRAVIPACK, SIRET 84054338300029 | Sens (89100) | |
| lespepitestech.com | Gravipack / EXOSQUELETTE LIGHT | Sens; also tagged French Tech Aix-Marseille Région Sud | 2-10 staff; website gravipack.com |
| myfrenchstartup.com | raison sociale GRAVIBAG | n/a | |
| fr.linkedin.com/company/gravipack | Gravipack | Vincennes | 201-500 employees (vs about 4-5 elsewhere); website gravipack.com |
| pagesjaunes.fr / mappy | Gravipack, category 'Maroquinerie' | Vincennes | |
| decathlon.fr/vc/gravipack (search summary) | Marketplace seller KID'ABORD | n/a | journaldugeek.com 2021: 'Kid'abord, Loire-Atlantique'. Not independently verified |
| groupe-ranque.fr/gravipack | Unrelated homonym ('Sécurité et Stockage Blindé', Vincennes) | Vincennes | brand-name collision in local results |

## 10. Third-party references: which domain they point to

| Third party | URL seen | Domain referenced / role |
|---|---|---|
| LinkedIn | https://fr.linkedin.com/company/gravipack | gravipack.com |
| Les Pépites Tech | https://lespepitestech.com/startup-de-la-french-tech/gravipack | gravipack.com |
| Trustpilot | https://fr.trustpilot.com/review/gravipack.com , https://es.trustpilot.com/review/gravipack.com | gravipack.com (review profile keyed to .com) |
| Decathlon marketplace | https://www.decathlon.fr/vc/gravipack , https://www.decathlon.fr/brands/gravipack , PDP /p/mp/gravipack/sac-a-dos-randonnee-hiking-33-allege-la-charge-de-92percent/… | Reseller PDP ranks for 'sac à dos exosquelette' |
| ergo-corner.com | /55-gravipack , /content/13-le-sac-a-dos-gravipack , blog b14 | Reseller outranks gravipack.com for 'sac à dos anti mal de dos (exosquelette)' |
| equilibre-france-ergonomie.fr | /les-nouveaux-sacs-gravipack/ , /produits/sac-a-dos-hiking-33-… | Reseller, #3 on brand query |
| Fnac / Au Vieux Campeur | fnac.com/Gravipack/m568883 ; auvieuxcampeur.fr Hiking 33 | Resellers |
| KissKissBankBank | https://www.kisskissbankbank.com/en/projects/gravipack (+ child-bag campaign) | #1 on brand query in WebSearch |
| gravipack.fr | none | No third-party page seen naming gravipack.fr as the official site in the results' content |

## 11. Search log (68 queries)

| # | Query (mode) | Gravipack-owned URLs returned |
|---|---|---|
| 1 | site:gravipack.com (ext) | 9 (apex + www mixed) |
| 2 | site:gravipack.fr (std) | 0 |
| 3 | "gravipack.fr" (std) | 0 |
| 4 | gravipack.com produit sac à dos exosquelette (std) | 0 |
| 5 | Gravipack boutique sac anti mal de dos (std) | 0 |
| 6 | www.gravipack.com (std) | 0 |
| 7 | site:gravipack.com produit (ext) | 9 |
| 8 | site:www.gravipack.com (ext) | 9 |
| 9-12 | Gravipack Sherpa / Oslo 60+10L / Austerlitz / ROME (std) | 0 (third parties only) |
| 13 | site:gravipack.com sac randonnée (ext) | 9 |
| 14 | site:gravipack.com cartable enfant scolaire (ext) | 10 |
| 15 | site:gravipack.com categorie-produit (ext) | 10 incl. presta |
| 16 | site:gravipack.com sac business ordinateur (ext) | 9 incl. presta |
| 17 | site:presta.gravipack.com (ext) | 7 presta |
| 18 | site:gravipack.com -www (std) | 0 |
| 19 | site:gravipack.com CGV … (ext) | 8 incl. presta |
| 20 | site:gravipack.com étude brevet médecin ergonome (ext) | 10 incl. presta study |
| 21 | site:gravipack.com actualités blog article (ext) | 9 |
| 22 | site:gravipack.com tag OR auteur OR author OR feed (std) | 0 |
| 23 | site:gravipack.com militaire tactique médical (ext) | 9 |
| 24 | site:gravipack.com porte-bébé (std) | 0 |
| 25 | site:gravipack.com Hiking 33 exosquelette (ext) | 7 incl. presta, ?order=price |
| 26 | site:gravipack.com Feather OR City OR G-Pack (ext) | 10 incl. presta |
| 27 | site:gravipack.com ToolMaster MedMax ExoTool (std) | 0 |
| 28 | Gravipack English exoskeleton backpack (std) | 0 |
| 29 | Kid'abord Gravipack Loire-Atlantique (std) | 0 |
| 30 | "EXOSQUELETTE LIGHT" Gravipack SAS (std) | 0 |
| 31 | gravipack.eu/.de/.ma/.net (std) | 0 |
| 32 | site:gravipack.com accueil add-to-cart (std) | 0 |
| 33 | lespepitestech Gravipack site web gravipack.fr (ext) | 1 (home) |
| 34 | "www.gravipack.fr" (ext) | 5 (.com) |
| 35 | sac à dos anti mal de dos exosquelette (ext) | 8 |
| 36 | sac randonnée anti mal de dos (std) | 0 |
| 37 | Gravipack LinkedIn company site web Vincennes (ext) | 1 (/contacts/) |
| 38 | sac à dos exosquelette (ext) | 2 |
| 39 | sac à dos anti mal de dos (ext) | 3 |
| 40 | Gravipack (ext) | 6 |
| 41 | site:gravipack.com panier OR mon compte… (ext) | 9 incl. presta |
| 42 | site:gravipack.com témoignages avis gravipackers (ext) | 10 |
| 43 | site:gravipack.com claie Cargo Max Centurion (std) | 0 |
| 44 | site:gravipack.com remboursement mutuelle… (ext) | 9 |
| 45 | site:gravipack.com Oslo exosquelette 60L (ext) | 10 incl. ?order&filter |
| 46 | site:gravipack.com Sherpa 45L (ext) | 9 incl. ?add-to-cart=2678, presta |
| 47 | site:gravipack.com copie (std) | 0 |
| 48 | site:gravipack.com Rome 28L sac (ext) | 10 |
| 49 | gravipack avis (ext) | 1 |
| 50 | "http://gravipack.com" OR "http://www.gravipack.com" (std) | 0 |
| 51 | site:gravipack.com inventeur Mohammed Errafi (ext) | 9 |
| 52 | site:gravipack.com presse Europe 1 Lépine (ext) | 10 incl. presta |
| 53 | site:gravipack.com categorie anti-tms militaire (ext) | 10 incl. /category/, /etiquette-produit/ |
| 54 | kisskissbankbank Gravipack FAQ gravipack.fr (std) | 0 |
| 55 | site:gravipack.com English backpack back pain (std) | 0 |
| 56 | site:gravipack.com Compostelle Dublin Helsinki Pearl (ext) | 10 |
| 57 | presta.gravipack.com sac à dos gravipack (ext) | 10 presta |
| 58 | shop./blog./boutique./en.gravipack (std) | 0 |
| 59 | decathlon.fr Gravipack marque (std) | 0 |
| 60 | site:gravipack.com à propos qui sommes-nous (std) | 0 |
| 61 | cartable anti mal de dos exosquelette collège (std) | 0 |
| 62 | sac à dos ordinateur anti mal de dos ergonomique exosquelette (std) | 0 |
| 63 | site:gravipack.com page 2 OR page 3 boutique (std) | 0 |
| 64 | site:gravipack.com sac outillage artisan porte-outils (ext) | 9 |
| 65 | "gravipack.fr" sac à dos (ext) | 8 (.com) |
| 66 | site:presta.gravipack.com content mentions légales CGV (std) | 0 |
| 67 | site:gravipack.com Business Talk V4 (std) | 0 |
| 68 | site:gravipack.com contact devis entreprise CE (std) | 0 |
