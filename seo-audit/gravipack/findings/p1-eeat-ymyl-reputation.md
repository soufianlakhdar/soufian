# Phase 1 — eeat-ymyl-reputation

Searches run: 0

## Evidence base

LIMITATION, READ FIRST: The WebSearch budget for this workflow turn (200 calls, shared by every agent) was used up before this agent's first query. I tried 6 searches in parallel (the scientific study, social-security reimbursement, SIREN/Pappers, Trustpilot, the patent, the Kid'abord link). All 6 were refused. Following the network policy, I did not use curl, proxies, archives or reader services, and the site itself is blocked. So this report rests only on the orchestrator's summary of earlier WebSearch results from this run. That summary contains: (a) gravipack.com titles as shown in search results (Google may rewrite titles), including the home page, Sherpa, Sherpa Kaki 'anti douleur', Austerlitz, Hiking Gris, Oslo 60+10L at €289 and ROME; (b) gravipack.com URL patterns (/boutique-gravipack/, /produit/…, and a blog post with a children's slug), both www and non-www indexed, and gravipack.fr not indexed; (c) third-party sources: decathlon.fr/brands/gravipack, es.trustpilot.com/review/gravipack.com, outzer.fr (critical Sherpa 45 test), randonner-leger.org (doubts about the study), journaldugeek.com (2021), neozone.org, challenge.ma (claims of social-security reimbursement and a French Army / Foreign Legion test in 2017), lespepitestech.com (French Tech Aix-Marseille / Région Sud, founder Mohammed Errafi), KissKissBankBank, motherbase.ai, a €346k love-money raise in 2019, and one unverified mention of 'Kid'abord (Loire-Atlantique)'. Where the summary named only a domain, I cite the domain rather than make up a path. In this report, 'UNVERIFIED' means no primary source appears in the available evidence. It does NOT mean the claim was shown to be false. Confidence is lowered to match. E-E-A-T sub-scores that need the live site are null. The few provisional off-site scores are low-confidence claude-seo heuristics, not Google signals. The table 'Follow-up verification queries' lists the exact searches to run when budget is available: the user can send a follow-up message, or raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.

## claude-seo commands applied

- seo-content (skills/seo-content/SKILL.md v2.4.2): Google Who/How/Why test, E-E-A-T framework, YMYL rules, AI-citation (GEO) guidance, and the error rule 'URL unreachable: report clearly, do not guess site content'
- agents/seo-content.md: E-E-A-T weights Experience 20 / Expertise 25 / Authoritativeness 25 / Trust 30, output format (content score, E-E-A-T breakdown, AI-citation readiness)
- seo/references/eeat-framework.md: signal checklists per factor, YMYL categories (health & safety), Sept 2025 QRG notes
- seo/references/eeat-scoring-guide.md: score bands (0-29 / 30-49 / 50-69 / 70-89 / 90-100) and improvement actions per band
- seo/SKILL.md priority levels (Critical = blocks indexing or causes penalties; High = significantly impacts rankings; Medium = optimisation opportunity; Low = nice to have)
- seo/references/quality-gates.md: title 30-60 characters, About page 400+ words, product page 400+ words
- NOT run: render_page.py and metadata_template.py, because the site is network-blocked and no meta descriptions were available. No on-page facts are asserted.

## What works

- Identifiable inventor-founder (Mohammed Errafi) linked to the product in third-party sources (lespepitestech.com, press). This is a real Person entity the brand can build Experience and Expertise around.
- Real-world validation through retail: a Gravipack brand page on Decathlon's marketplace (decathlon.fr/brands/gravipack) listing Sherpa 45, Hiking 33 and Feather school bags gives Trust by association and a second place to collect reviews.
- Genuine ecosystem and press mentions: French Tech Aix-Marseille / Région Sud listing, journaldugeek.com (2021), neozone.org, challenge.ma, plus a funding history (€346k love money in 2019) and KissKissBankBank campaigns. These are real brand mentions that support Authoritativeness, even if dated.
- A presence on a review platform exists (Trustpilot profile for gravipack.com), so a review program can be activated quickly.
- Clear, distinctive and consistent positioning across all titles seen (patented carbon exoskeleton that redistributes load). Strong topical focus is a good basis for an expert-reviewed content cluster on back health and load carrying.
- Claimed patent and claimed field tests (2017). If documented, these are exactly the kind of first-hand, checkable proof that the QRG 'How' test rewards.

## Specialist scores

| Category | Score | Rationale |
|---|---|---|
| E-E-A-T overall (claude-seo content model, 0-100) | n/a | Needs on-site evidence (mentions légales, About page, authors and reviewers, proof pages, policies, HTTPS) and the off-site verification searches, all of which were blocked in this run. Indicative only: off-site signals point to the 'Weak' band (30-49), but no number is given. |
| Experience (weight 20) | n/a | Off-site hints exist (inventor-built product, crowdfunding, claimed 2017 field tests, Decathlon distribution), but first-hand content on the site cannot be assessed, and the independent testers are critical (Outzer) or skeptical (randonner-leger). |
| Expertise (weight 25) | n/a | No credentialed health professional seen in the third-party evidence and no published methodology, but on-site bylines and review boxes cannot be checked. Likely weak; verify on site. |
| Authoritativeness, off-site only (weight 25) — PROVISIONAL | 45 | Low confidence, based on the orchestrator's summary. Positives: Decathlon marketplace brand page, French Tech Aix-Marseille / Région Sud listing, tech and business press (Journal du Geek 2021, Neozone, Challenge.ma), KissKissBankBank. Negatives: no health, scientific or medical citations; coverage is 2017-2021; a skeptical enthusiast community. That puts it in the 'Weak' band (30-49). |
| Trustworthiness (weight 30) | n/a | Mainly on-site (contact details, mentions légales, CGV, returns, HTTPS, payment) plus reputation data (Trustpilot rating), none of which could be retrieved. Known off-site negatives: unresolved legal entity (Aix-Marseille vs Kid'abord, Loire-Atlantique), several indexed hosts, unverified headline claims. |
| YMYL health-claim substantiation, off-site — PROVISIONAL | 20 | Low confidence. None of the 6 headline claims (anti mal de dos / anti douleur, -92 % pressure, social-security reimbursement, prescribed by occupational doctors, army / Foreign Legion test, patent) could be tied to a primary source in the available evidence, and the only independent discussion is skeptical. Re-score once the follow-up verification queries have run. |
| Entity transparency, off-site — PROVISIONAL | 35 | Low confidence. Founder identifiable and a startup-ecosystem listing exists, but legal entity, SIREN and address were not found. There is a conflicting association with Kid'abord (Loire-Atlantique) and a split domain set (gravipack.fr not indexed; gravipack.com indexed on both www and non-www). |
| Off-site reputation / reviews | n/a | Trustpilot rating, count and recency, Decathlon review stars and Google reviews were not retrievable (searches refused). Qualitative picture: retail and press positive, independent testers critical or skeptical. |

## Raw findings (with verifier verdicts)

### The core health promise ('anti mal de dos', TMS relief, '-92 % de pression') cannot be traced to any independent source in the evidence

`ymyl-health-claims-unsubstantiated` · Content Quality · auditor severity **High** → verifier **confirmed**, severity **High**

**Evidence.** From earlier WebSearch results in this run, gravipack.com titles as shown in search results lead with a health outcome. Home: 'Gravipack : le sac révolutionnaire anti mal de dos exosquelette'. Products: 'Sac randonnée léger anti mal de dos exosquelette bretelles Sherpa', 'Sac anti mal de dos business ROME ergonomique gravipack', '…Sherpa Kaki Gravipack anti douleur'. The quantified claim ('jusqu'à 92 % de pression en moins'), 'prescrit par les médecins du travail' and the 'étude scientifique' could not be traced to any published, peer-reviewed or institutional source. The only independent discussion found (randonner-leger.org threads) doubts the study. Press coverage (challenge.ma, neozone.org, journaldugeek.com) repeats brand claims without testing them. This agent's verification searches were refused (budget used up), so 'unverified' means no primary source was found, not that the claim is false.

<https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/> · `randonner-leger.org (forum threads skeptical of the study; exact URLs from the orchestrator summary, not re-retrieved)` · `challenge.ma (article relaying claims; exact URL not re-retrieved)` · `neozone.org` · `journaldugeek.com`

**Why it matters.** Back pain and musculoskeletal disorders fall under the 'health and safety' YMYL category in Google's Quality Rater Guidelines (Sept 2025), which demands the highest E-E-A-T. Google says Trust is the most important part of E-E-A-T, and raters are told to give unsupported YMYL claims low ratings. Separately, unsubstantiated product-property claims can be a 'pratique commerciale trompeuse' (Code de la consommation L121-1/L121-2), enforced by the DGCCRF.

**SEO effect.** Google's core ranking systems (which absorbed the helpful-content signals in March 2024) favour pages with demonstrable expertise on YMYL-adjacent queries such as 'sac à dos mal de dos', 'sac anti mal de dos', 'sac à dos TMS' and 'cartable mal de dos'. That can keep Gravipack below retailers and health publishers even on its own category term. Skeptical forum and review pages ranking next to the brand reduce CTR. AI Overviews, AI Mode, ChatGPT and Perplexity are less likely to cite claims that have no attributable source.

**How to fix.** 1) Build a claims register (spreadsheet) covering every health or performance claim in WooCommerce product titles, short and long descriptions, SEO titles and meta descriptions (Yoast / Rank Math), image alt text, blog posts, ads, Decathlon marketplace listings and crowdfunding pages, with the proof behind each one. 2) Keep only claims backed by documented proof. Link each to a new proof page (/preuves-et-etudes/) with an inline footnote. 3) Rewrite cure or therapy promises as mechanism or benefit statements: drop 'anti douleur'; replace 'sac anti mal de dos' with 'sac à dos à exosquelette conçu pour mieux répartir la charge'. Example intro: 'Les inserts carbone de l'exosquelette Gravipack reportent une partie du poids des bretelles vers le centre de gravité du corps. Lors d'un test mené par [laboratoire] sur [n] porteurs avec une charge de [x] kg, la pression mesurée sur les épaules a diminué jusqu'à 92 % (voir la méthodologie).' 4) Always give the conditions for any number ('jusqu'à …, dans les conditions du test X'). 5) Have a French consumer-law or regulatory adviser validate the final wording. 6) After the rewrite, request re-indexing of the main URLs in Search Console (URL Inspection).

**Verifier notes.** Method: new WebSearch calls were refused (the 200-call budget for this turn was used up). I checked this finding against the run's own WebSearch log (scratchpad serp-notes.md: 48 standard + 12 extended queries; tables.md: 114 indexed URLs with titles as shown by the search tool, which is not Google.fr). The defect is real and wider than stated. 'Allège le poids de 92%' appears in the gravipack.com school-bag category title and in the post /inventeur-dun-sac-a-dos-en-apesanteur/. 'Anti-TMS' appears in the hiking category and the claie-de-portage category. 'Anti-douleur' appears on two Light Promax tool-bag URLs as well as Sherpa Kaki. Decathlon marketplace titles (Feather) also say 'Allège la charge de 92%', so the claim has spread off-site. The query 'gravipack arnaque efficace 92%' returned only randonner-leger UGC (8 results, all skeptical) plus KissKissBankBank. Corrections: (1) 'prescrit par les médecins du travail' appears in no logged search result. It came from the task brief and must not be presented as an observed site fact. (2) 'Cannot be traced to any source' is too strong. An indexed legacy page exists, presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack ('L'étude scientifique du sac à dos en apesanteur Gravipack.'), and the query 'gravipack étude Lyon' surfaced a moodle.univ-lyon1 result plus Maddyness and Europe 1. A university link is therefore possible but unverified. The accurate wording is 'no independent, published methodology found'. (3) The SEO-effect line 'can keep Gravipack below retailers even on its own category term' is partly contradicted. In extended-mode results, gravipack.com/ appears in the top 10 for 'sac à dos anti mal de dos' (E1), 'sac à dos ergonomique mal de dos' (E2) and 'meilleur sac à dos anti mal de dos' (E8), although the ergo-corner reseller page ranks above it. Present any ranking effect as a risk, not an observed outcome. High stays justified: the claims run site-wide across 100+ URLs in a health and safety YMYL context, with legal exposure.

### 'Anti douleur' / 'anti mal de dos' wording suggests a medical purpose, but medical-device (CE DM) status is unknown

`therapeutic-claims-medical-device-status` · Content Quality · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Product title as shown in search results: 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur'; home title 'le sac révolutionnaire anti mal de dos'. No CE medical-device marking, EUDAMED registration or ANSM reference for Gravipack appears in the available evidence (the verification search was refused). The 'reimbursed by social security' claim relayed by challenge.ma would also imply medical-device status.

<https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/> · `challenge.ma (exact URL not re-retrieved)`

**Why it matters.** Under EU Regulation 2017/745 (MDR), a product whose manufacturer-intended purpose includes alleviating disease, injury or disability is a medical device. It must carry MDR CE marking before being marketed for that purpose. Intended purpose is judged from labelling, advertising and website copy. If Gravipack is not a certified medical device, pain-relief wording creates regulatory exposure (ANSM) on top of consumer-law exposure. If it IS certified, that is a strong Trust signal that is currently invisible off-site.

**SEO effect.** Unsupported therapeutic claims are the YMYL pattern quality raters discount most. Google Merchant Center's misrepresentation and healthcare policies can disapprove listings with unproven health claims, losing free product listings and Shopping visibility. A verifiable CE-DM status, by contrast, would strengthen Trust for 'mal de dos' queries.

**How to fix.** 1) Choose a regulatory route with a regulatory consultant. (a) Certify the exoskeleton as a class I medical device (technical file, clinical evaluation, EU declaration of conformity, EUDAMED registration), then show the CE marking, intended purpose and instructions for use on product pages. Or (b) position it as an ergonomic consumer product and remove all therapeutic wording. 2) Under route (b), rewrite titles to 60 characters or fewer, e.g. 'Sac de montagne Sherpa Kaki à exosquelette | Gravipack' and 'Gravipack | Sacs à dos ergonomiques à exosquelette carbone'. Keep 'mal de dos' only in informational, non-curative framing ('Sac à dos et mal de dos : comment bien répartir la charge ?'). 3) Apply the same wording everywhere: WooCommerce product names, SEO titles, short descriptions, image alt text, the product feed and Decathlon marketplace listings. 4) Under route (a), add the schema.org Certification type (Product.hasCertification) for the CE/DM status and link the declaration-of-conformity PDF.

**Verifier notes.** The wording evidence is stronger than stated. 'Anti-douleur' appears in titles of Sherpa Kaki (3 URLs) and Light Promax (2 URLs: 'Sac à dos outillage anti-douleur exosquelette Gravipack®'), and 'anti-TMS' appears in 2 category titles. The /sac-a-dos-medical/ category is a bag for medics ('allégez vos missions sauvez des vies'), not a medical-device claim, so do not cite it. The MDR reasoning holds: under Art. 2(1), intended purpose includes 'prevention … treatment or alleviation of disease', judged from labelling, advertising and promotional material. Medical-device status is still unknown, and it is a legal and regulatory matter whose ranking effect is indirect. Under claude-seo's priority definitions (High = significantly impacts rankings), Medium is proportionate. The Merchant Center part duplicates merchant-center-health-claim-risk; keep it in one place. Corrections to the fix: a class I non-sterile, non-measuring device is self-declared through the manufacturer's technical documentation and EU declaration of conformity, with no notified-body certificate, so 'certify' is imprecise. Product.hasCertification is valid schema.org, but Google's Certification markup for merchant listings covers specific schemes (e.g. EU energy labels), so present it as transparency with no rich-result benefit.

### The 'scientific study' behind the pressure-reduction figure is not public and no independent source cites it

`scientific-study-not-published` · Content Quality · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** Earlier searches surfaced randonner-leger.org threads expressing doubt about the study (per the orchestrator's summary). No journal article, preprint, university or lab report, or trial record for Gravipack appears in the available evidence. Press articles (neozone.org, journaldugeek.com 2021, challenge.ma) repeat the figures without any methodology.

`randonner-leger.org (exact thread URLs not re-retrieved)` · `neozone.org` · `journaldugeek.com` · `challenge.ma`

**Why it matters.** The QRG 'How was it created?' test: for YMYL claims, readers expect to see how a result was established. First-party data is the strongest Experience and Expertise signal, and seo-content guidance notes AI systems cite it heavily, but only when the methodology is published.

**SEO effect.** A published study page would (a) earn citations and backlinks from health, ergonomics and outdoor media (Authoritativeness), (b) give AI Overviews, ChatGPT and Perplexity a quotable, attributable source, and (c) counter the forum doubts ranking for 'gravipack avis'. Unpublished, the 92 % figure works against trust.

**How to fix.** 1) Publish /etude-scientifique-gravipack/ with: who ran the study (lab, university or ergonomist; names and credentials), date, funding and conflict-of-interest statement, protocol (number of participants, loads, measurement device such as pressure-mapping sensors, control backpack), results with variance or confidence intervals, limitations, and the full PDF. 2) If the study was internal, commission an independent replication (a STAPS or biomechanics university lab, or an ergonomics consultancy) and aim for a preprint or peer-reviewed paper. 3) Add Article JSON-LD (author as Person or Organization, datePublished, citation) and link to the page from every claim footnote. 4) Post the link openly, as the brand, in the randonner-leger threads and offer the latest model to skeptical testers. 5) Pitch the study to physiotherapy, ergonomics and occupational-health media for earned links.

**Verifier notes.** Partly contradicted by the run's own search log. The brand did publish a study page, but on an indexed legacy PrestaShop subdomain: presta.gravipack.com/40-etude-scientifique-soulage-le-dos-gravipack, titled 'L'étude scientifique du sac à dos en apesanteur Gravipack.' The query 'gravipack étude Lyon' returned 6 randonner-leger threads, a moodle.univ-lyon1 result, Maddyness and Europe 1, which suggests the study is tied to Lyon (possibly Université Lyon 1). It is not unknown. The valid core is narrower: no study page on the main gravipack.com domain appeared in any site: query; whether the legacy page shows protocol, sample size and authors is unknown; and no peer-reviewed or independent publication was found. The forum skepticism is confirmed. Fix change: do not build /etude-scientifique-gravipack/ from scratch. Migrate and expand the existing legacy page on www.gravipack.com and 301-redirect the presta URL to it, so the URL others already reference (forum threads, press) keeps its equity. Then add methodology, authors and limitations as proposed.

### 'Premier sac à dos remboursé par la Sécurité sociale' is unverified; no LPP listing was found

`social-security-reimbursement-claim-unverified` · Brand / Reputation · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** challenge.ma coverage (per the earlier search summary) says Gravipack is the 'first backpack reimbursed by social security' and was tested by the French Army / Foreign Legion in 2017. No LPP code or ameli.fr reference was found in the available evidence. This agent's verification query was refused (budget used up). It is unknown whether gravipack.com itself repeats the claim.

`challenge.ma (exact URL not re-retrieved)`

**Why it matters.** In France, reimbursement by the Assurance Maladie requires an LPP listing (with a code and tariff) and usually a prescription, so the claim is easy to check. If it is wrong, it is a misleading commercial practice and a strong distrust trigger for buyers who then try to claim the refund. It may be a confusion with mutuelle (complementary insurance) cover, employer or occupational-health purchases, or disability funding such as AGEFIPH. Those are different things and must be named exactly.

**SEO effect.** Wrong or vague reimbursement claims produce negative reviews (customers refused a refund), forum threads and press corrections that rank for brand queries. LLMs also repeat them, spreading misinformation attributed to the brand.

**How to fix.** 1) Check whether the claim appears on gravipack.com (copy, FAQ, product pages). 2) If an LPP code exists, show it with exact conditions ('pris en charge sur prescription médicale, code LPP xxxxxxx, base de remboursement x €') and link to the ameli LPP database. 3) If not, remove the claim and replace it with accurate wording such as 'Certaines mutuelles ou services de santé au travail peuvent participer au financement : renseignez-vous auprès de votre organisme', and only if that is true. 4) Ask challenge.ma and any other outlet to correct their article. 5) Add an FAQ entry 'Le sac Gravipack est-il remboursé ?' with the accurate answer so search engines and LLMs have a canonical source.

**Verifier notes.** Confirmed that the third-party claim exists and is visible. For the query 'sac à dos remboursé sécurité sociale mal de dos' (log query 9), the challenge.ma Gravipack article ranks next to insurer and comparison pages, and gravipack.com does not appear. No LPP or ameli evidence was logged. Not shown: that gravipack.com repeats the claim. Caveat the finding misses: challenge.ma and lematin.ma (also in the 'gravipack' brand SERP) are Moroccan outlets, so 'sécurité sociale' may refer to a non-French scheme or be a journalist's shorthand. Check before calling it a French LPP issue. It is a reputational and accuracy risk carried by a third party, with no demonstrated ranking effect, so High is overstated and Medium fits. The fix is sound. If an FAQ answer is added, do not promise FAQ rich results: claude-seo records FAQ rich results as fully retired on 2026-05-07.

### No independent health professional (kiné, ergonomist, occupational doctor) is visibly attached to the claims

`no-independent-health-expert-backing` · Content Quality · auditor severity **High** → verifier **weakened**, severity **Medium**

**Evidence.** The brand says occupational doctors prescribe or recommend the bag (per the task brief). Yet none of the third-party sources surfaced in earlier searches names a credentialed health professional who endorses or reviewed the product: Decathlon brand page, Trustpilot, Outzer, randonner-leger, Journal du Geek, Neozone, Challenge.ma, lespepitestech. The only identifiable person is the inventor-founder, Mohammed Errafi.

<https://www.decathlon.fr/brands/gravipack> · <https://es.trustpilot.com/review/gravipack.com> · `lespepitestech.com` · `outzer.fr` · `randonner-leger.org`

**Why it matters.** QRG 'Who created it?' test: for YMYL content, readers expect it to be written or reviewed by people with relevant expertise. The claude-seo Expertise checklist asks for author credentials, evidence-backed claims and a byline with credentials. Without them, Expertise scores 'Weak'.

**SEO effect.** Expertise is a key differentiator for ranking health-adjacent pages. Adding reviewed-by credentials and expert content supports rankings for informational queries ('sac à dos ergonomique', 'quel sac à dos pour le dos', 'comment régler son sac à dos', 'cartable mal de dos enfant') and makes AI citation more likely.

**How to fix.** 1) Recruit 2-3 independent experts: masseur-kinésithérapeute DE, certified ergonomist, occupational or rehabilitation physician. Disclose any paid or unpaid advisory arrangement. 2) Add a 'Contenu vérifié par' box on product, guide and study pages with: name, title, RPPS/ADELI or professional registration number, short bio, review date and a conflict-of-interest line. 3) Mark it up, e.g. {"@context":"https://schema.org","@type":"WebPage","reviewedBy":{"@type":"Person","name":"[Nom]","jobTitle":"Masseur-kinésithérapeute DE","sameAs":"[URL profil]"},"lastReviewed":"2026-10-12"}, added via ACF fields plus a JSON-LD snippet or Rank Math / Yoast schema filters. 4) Create an /experts/ hub with full bios. 5) Replace the anonymous 'prescrit par les médecins du travail' with named, consenting testimonials. 6) Publish expert-led guides: 'Comment régler son sac à dos', 'Sac à dos et TMS au travail', 'Cartable et dos de l'enfant : l'avis d'un kiné'.

**Verifier notes.** Absence of evidence, consistent with the log. The query 'sac à dos recommandé par les ostéopathes' (log 32) returned no Gravipack result, and no third-party source names a credentialed health professional. However: (a) the 'prescrit par les médecins du travail' premise is from the task brief, not from any logged result; (b) whether gravipack.com product, FAQ or study pages show a reviewer cannot be seen from SERPs; (c) there are adjacent professional references the finding ignores, namely gravipack.com posts about RATP agents using the Light Promax tool bag (Vivatech / Le Parisien) and the possible Lyon 1 study link. Those are occupational and academic signals, though not health-professional endorsements. Medium is proportionate given the indirect ranking effect. Fix safety issue: putting named doctors' endorsements ('named, consenting testimonials') on commercial product pages conflicts with French medical deontology (CSP R.4127-20: a doctor must not let his name or status be used for advertising), and kinés have similar rules. If the product is positioned as a medical device, payments to health professionals also fall under Transparence Santé (CSP L.1453-1). Use experts as study authors or reviewers of educational content, with disclosure, not as product endorsers. reviewedBy and lastReviewed are valid schema.org but feed no Google feature, so present them as transparency.

### Entity ambiguity: who owns the brand, where it is based and which domain is official are all unclear

`entity-ambiguity-legal-owner-domains` · Brand / Reputation · auditor severity **High** → verifier **confirmed**, severity **Medium**

**Evidence.** Earlier searches: lespepitestech.com lists Gravipack as a French Tech Aix-Marseille / Région Sud startup founded by Mohammed Errafi, but one search summary tied the brand to a company 'Kid'abord (Loire-Atlantique)', which is unverified and in a different region. site:gravipack.fr returned no indexed pages, so the audited URL http://gravipack.fr/ is not the indexed property. gravipack.com is indexed under both https://gravipack.com/ and https://www.gravipack.com/. The SIREN/Pappers and Kid'abord searches were refused in this run, so the legal entity is still unconfirmed.

`lespepitestech.com` · <https://gravipack.com/> · <https://www.gravipack.com/> · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** Trust (30 % in claude-seo's model) starts with knowing who runs the site. The QRG tells raters to identify who is responsible for a website and check that party's reputation. Conflicting entity data (two regions, possibly two companies, several domains and hosts) weakens Knowledge Graph matching and buyer confidence, which matters more for a store selling health-adjacent products and taking payments. French law (LCEN art. 6-III) also requires mentions légales identifying the publisher.

**SEO effect.** Weak entity matching can mean no brand knowledge panel or a wrong one, brand signals split across domains and hosts, reviews or legal listings attributed to the wrong company, and LLMs describing the brand inconsistently. Indexing both www and non-www also splits link equity (the technical agent covers redirects and canonicals).

**How to fix.** 1) Confirm the current legal entity on Infogreffe or Pappers: name, SIREN, RCS, head office, director. Establish whether Kid'abord owns, licenses or distributes the brand, and say so plainly on the site, e.g. 'La marque Gravipack® est exploitée par [Société], SAS au capital de [x] €, RCS [ville] [SIREN]'. 2) Publish /mentions-legales/ (publisher, SIREN, address, phone, email, directeur de la publication, host) and /a-propos/ (400+ words: story, inventor, team, dated timeline from the 2017 field tests to the 2019 raise, crowdfunding and Decathlon). 3) Pick one canonical host (e.g. https://www.gravipack.com/) and 301-redirect every other variant to it, including gravipack.fr. 4) Add Organization JSON-LD on the home page, e.g. {"@context":"https://schema.org","@type":"Organization","name":"Gravipack","legalName":"[Raison sociale]","url":"https://www.gravipack.com/","founder":{"@type":"Person","name":"Mohammed Errafi"},"identifier":{"@type":"PropertyValue","propertyID":"SIREN","value":"[SIREN]"},"address":{"@type":"PostalAddress","addressCountry":"FR"},"sameAs":["https://www.decathlon.fr/brands/gravipack","https://fr.trustpilot.com/review/gravipack.com","[LinkedIn]","[KissKissBankBank]"]}. 5) Align company name, address and phone on Trustpilot, the Decathlon seller profile, LinkedIn and Google Business Profile.

**Verifier notes.** The run's log confirms entity fragmentation, with more detail than the finding has. (1) gravipack.com/mentions-legales/ (indexed) names EXOSQUELETTE LIGHT, Paris, hosted by Gandi. (2) The Decathlon marketplace seller is Kid'Abord (log 11: Sherpa 45 at €149.90, down from €249, promo 18 June to 30 Aug 2026). Nature & Découvertes listings by Kid'abord give a return address 'SODILOG / RETOUR GRAVIPACK, Colmar'. (3) motherbase.ai shows a Vincennes address. (4) lespepitestech lists it as French Tech Aix-Marseille / Région Sud. The 'Loire-Atlantique' location of Kid'abord remains unconfirmed; drop it unless verified. Host fragmentation is also larger: apex and www both indexed, a legacy presta.gravipack.com subdomain with 16 indexed URLs, two product base paths (/produit/ and /produit-gravipack/), and gravipack.fr not indexed. Corrections to the fix: /mentions-legales/, /a-propos-de-nous-gravipack-au-service-de-votre-dos/, /contact-gravipack/ and /contacts/ already exist and are indexed. Step 2 should be to complete and align them (SIREN, RCS, brand-operator relationship with Kid'Abord, returns address), not to publish them. For Organization JSON-LD, prefer Google-documented identifiers (vatID, or iso6523Code with ICD 0002 for SIREN) over a generic PropertyValue. Use the canonical www.trustpilot.com/review/gravipack.com in sameAs, not a locale subdomain. A Google Business Profile is only eligible if the business has in-person customer contact (showroom or pickup); an online-only brand is not eligible. Severity: a Trust and Knowledge Graph issue with an inferred ranking effect, so Medium. The host and redirect duplication belongs to the technical dimension.

### Critical independent reviews and forum doubts rank for product research queries, with no brand response found

`critical-independent-reviews-unanswered` · Brand / Reputation · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Earlier searches surfaced outzer.fr's critical test of the Sherpa 45 and randonner-leger.org threads doubting the scientific study. These are the most independent (non-promotional) sources found about the product. No brand reply or rebuttal appeared in the evidence summary.

`outzer.fr (Sherpa 45 review; exact URL not re-retrieved)` · `randonner-leger.org (exact thread URLs not re-retrieved)`

**Why it matters.** Raters are told to look for independent reviews when judging reputation. For a YMYL-adjacent product, negative opinions from expert enthusiasts weigh heavily. These pages also shape 'gravipack avis' results and LLM summaries.

**SEO effect.** Brand + 'avis' queries are high-intent. Skeptical results lower CTR to gravipack.com and conversion, and LLMs end up summarising the brand as 'mixed opinions'. This is not a ranking penalty, but reputation feeds how Google's systems and raters judge Trust.

**How to fix.** 1) Read the Outzer test and list each criticism (weight, fit, ventilation, claims). 2) Publish an honest update or FAQ page, e.g. 'Ce que nous avons amélioré depuis le test d'Outzer', linking to the study. 3) Offer Outzer and other independent testers (randonner-leger members, outdoor YouTubers) the latest model to re-test, with no conditions. 4) Reply in the forum threads openly as the brand, with the study PDF. 5) Build an on-site 'Avis clients' hub fed by verified purchases. 6) Check the brand SERP monthly ('gravipack avis', 'gravipack sherpa avis', 'gravipack arnaque').

**Verifier notes.** The existence and ranking of critical independent content is confirmed. For 'gravipack sherpa avis test' (log 35), the outzer.fr Sherpa 45 review is negative (about €240 price, real capacity around 30 L despite the '45' name) and appears with 4 randonner-leger threads. For 'gravipack arnaque efficace 92%' (log 37), all results are skeptical randonner-leger UGC. Randonner-leger threads also rank on generic queries such as 'sac à dos qui soulage le dos et les épaules' (threads 570298/570316/570392) and 'bretelles ergonomiques sac à dos soulager épaules'. Correction: the plain 'gravipack avis' query (log 10) surfaced only es.trustpilot plus noise, not Outzer or the forum. 'Unanswered' is unverifiable because the threads were not read; the founder may have posted in them. The capacity criticism is also a product-claim accuracy issue (model name vs. measured volume). Fix addition: free products given to testers must be disclosed (loi n° 2023-451 on influence commerciale), and Google's review-snippet guidelines exclude fake or undisclosed incentivized reviews (claude-seo note dated 2026-07-24).

### The Trustpilot profile shows up in its Spanish version and its rating and recency are unknown; the review program needs active management

`trustpilot-and-review-program` · Brand / Reputation · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Earlier search results surfaced https://es.trustpilot.com/review/gravipack.com (Spanish locale) rather than fr.trustpilot.com. Rating, review count and date of the latest review could not be retrieved in this run (search budget used up). Review counts on the Decathlon marketplace are also unknown.

<https://es.trustpilot.com/review/gravipack.com> · <https://www.decathlon.fr/brands/gravipack>

**Why it matters.** The Trust checklist includes customer reviews and testimonials. Review volume, recency and reply rate are reputation signals that both raters and buyers check. For a €250-€290 product sold on comfort and health claims, real-world reviews are the key Experience evidence.

**SEO effect.** Third-party ratings appear in brand search results and in LLM answers, so low or stale ratings reduce brand CTR and conversions. Genuine product reviews on gravipack.com, with AggregateRating markup that follows Google's rules, can earn review snippets.

**How to fix.** 1) Claim or verify the Trustpilot business profile, set French as the main language, and make the company details match the mentions légales. 2) Connect WooCommerce to Trustpilot's automatic invitations (official integration) so every buyer is invited. Selective inviting breaks Trustpilot's rules and French consumer rules. 3) Reply to every review within 48-72 hours, especially negative ones about after-sales service, delivery or comfort. 4) Collect product reviews on gravipack.com (WooCommerce verified-owner reviews) and on the Decathlon marketplace. 5) Publish a review policy stating whether and how reviews are verified (Code de la consommation L111-7-2). 6) Only mark up AggregateRating for reviews collected and shown on that page; Google ignores self-serving third-party aggregates.

**Verifier notes.** Only the existence of the profile is evidenced. Rating, volume and recency remain unknown, so the severity rests on an assumption. The 'Spanish version' point is very likely an artifact of the search tool: the log header notes 'WebSearch tool, not Google.fr', and it is US-based. Trustpilot profiles are per domain and locale subdomains mirror the same reviews, so 'set French as the main language' is not a real fix. What holds: on 'gravipack avis' (log 10), Trustpilot is the only relevant result, so it is the main brand-reputation surface, and managing invitations and replies is worthwhile. L111-7-2 Code de la consommation (transparency of online reviews) is cited correctly. The AggregateRating guidance is correct, since Google requires ratings collected on the site itself. Low until the actual rating is known.

### 'Tested by the French Army / Foreign Legion (2017)' implies an institutional endorsement, but no public documentation was found

`military-endorsement-claim-undocumented` · Brand / Reputation · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** challenge.ma coverage (per the earlier search summary) reports tests by the French Army / Foreign Legion in 2017. No Ministère des Armées, DGA or Foreign Legion source appears in the available evidence (the verification search was refused).

`challenge.ma (exact URL not re-retrieved)`

**Why it matters.** Naming a state institution implies endorsement. Without documentation it is a misleading-claim risk, and it cannot count as an Authoritativeness signal for Google or for users.

**SEO effect.** A documented test (report, letter, photos used with permission) would be a strong, linkable trust asset and a press hook. An unprovable one becomes a reputation risk if challenged on forums.

**How to fix.** 1) Retrieve the 2017 test documentation: which regiment or unit, how many soldiers, how long, what results. Obtain written permission to cite it. 2) Publish it on the proof page with accurate wording, e.g. 'Prototype testé en 2017 par des militaires du [régiment] lors de [contexte] : retours d'expérience'. Do not write 'approuvé par l'Armée' unless an official approval exists. 3) If there is no documentation, drop the claim. 4) Do not use military insignia or names without authorisation.

**Verifier notes.** The Foreign Legion 2017 test is still undocumented. The finding misses that gravipack.com itself uses military framing: the post 'Gravipack soulage les forces spéciales au SOFINS', duplicated at /test/ with the same title, plus a /categorie/militaire/ blog category and a 'militaire tactique assault' product category. SOFINS is an industry seminar and exhibition linked to the special-forces ecosystem, so exhibiting there is not an endorsement, and 'soulage les forces spéciales' implies more than attendance. The misleading-claim risk is real but small for SEO; Low under claude-seo priorities. The /test/ duplicate should be noindexed or redirected (technical dimension).

### The 'exosquelette breveté' claim is not linked to a patent number

`patent-number-not-cited` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Brand messaging and tech press (journaldugeek.com, neozone.org, per earlier searches) describe a patented exoskeleton. No FR, EP or WO patent number appears in the available evidence (the patent search was refused).

`journaldugeek.com` · `neozone.org` · <https://gravipack.com/>

**Why it matters.** A verifiable patent is objective evidence of innovation and expertise. 'Brevet' without a number reads as marketing.

**SEO effect.** Links to INPI, Espacenet or WIPO records give users and AI systems a checkable fact and strengthen the brand and inventor entity. Google Patents pages often rank for inventor + brand queries.

**How to fix.** 1) List the patent numbers (e.g. 'Brevet FR xxxxxxx / EP xxxxxxx') in the product-page footer and on /a-propos/, linked to data.inpi.fr and worldwide.espacenet.com. 2) State the status (filed vs granted) and territories accurately. 3) Add the number to the Organization and Product JSON-LD (description or additionalProperty).

**Verifier notes.** Whether gravipack.com cites a number cannot be seen from SERPs. The site has an indexed post '/le-droit-de-la-propriete-industrielle-explique-avec-lexemple-gravipack/' that may well state it. The 'sac à dos exosquelette' query returned EPO patent documents (3) and Google Patents (log 3, E3), but they were not tied to Gravipack or Errafi in the log. The fix is sound and cheap; at Low priority it is a trust-detail enhancement, not a ranking issue.

### The inventor-founder is the brand's strongest E-E-A-T asset but has no visible entity footprint in the evidence

`founder-expertise-underleveraged` · Content Quality · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** lespepitestech.com and press identify Mohammed Errafi as inventor and founder (per earlier searches). No founder bio, interview hub or Person profile on gravipack.com showed up in the search-result evidence; this cannot be confirmed without site access.

`lespepitestech.com` · `journaldugeek.com` · `neozone.org`

**Why it matters.** The Experience factor and the 'Who' test reward first-hand stories. An inventor's account (why he designed the exoskeleton, the prototypes, the tests) is unique content that AI-generated or mass-produced competitor content cannot copy.

**SEO effect.** A founder Person entity linked to the Organization helps Knowledge Graph matching and brand queries. Founder interviews and podcasts earn links and mentions.

**How to fix.** 1) Create a founder page or a founder section on /a-propos/ with background, design journey, prototype photos and dates. 2) Add Person JSON-LD (name, jobTitle 'Fondateur et inventeur', worksFor Gravipack, sameAs LinkedIn and press interviews). 3) Publish founder-bylined posts, e.g. 'Pourquoi j'ai inventé l'exosquelette Gravipack'. 4) Pitch founder interviews to French Tech and regional media.

**Verifier notes.** 'No visible entity footprint' is contradicted on-site. gravipack.com has founder-story content indexed: '/inventeur-dun-sac-a-dos-en-apesanteur/', '/et-si-tout-commencait-par-un-sac-trop-lourd-et-un-reve-de-le-rendre-leger-pour-tous/' and an about page. Off-site, lespepitestech and press name Mohammed Errafi. What cannot be verified is whether those pages carry a proper bio, photos, dates and Person markup linked to the Organization. The remaining recommendation is to consolidate the founder story into one authoritative bio with Person JSON-LD. Low.

### Authority signals are dated (army test 2017, raise 2019, Journal du Geek 2021) and no recent independent coverage was found

`stale-authority-signals` · Off-Page / Authority · auditor severity **Medium** → verifier **refuted**, severity **Low**

**Evidence.** The press and ecosystem sources found earlier date from 2017-2021: the army-test claim (2017), the €346k love-money raise (2019) and journaldugeek.com (2021). The KissKissBankBank campaigns and the lespepitestech listing have no date in the summary. No 2024-2026 coverage appears in the evidence, but recency searches could not be run in this agent.

`journaldugeek.com` · `challenge.ma` · `lespepitestech.com` · `kisskissbankbank.com`

**Why it matters.** Authoritativeness means ongoing recognition. Old mentions suggest an inactive brand, especially when the Kid'abord question hints at a possible change of ownership.

**SEO effect.** Fresh, relevant mentions and links from health, outdoor and retail media support rankings on competitive commercial terms against Osprey, Deuter and Decathlon's own ranges, and feed LLM brand knowledge. A stale footprint means weaker brand authority.

**How to fix.** 1) Run a digital PR plan around new study results, new models, the Decathlon partnership and B2B occupational-health use cases (TMS prevention). Pitch outdoor media (Outzer, Trekmag), physiotherapy and ergonomics publications, and regional press near the real head office. 2) Enter innovation awards (e.g. ISPO Award, Janus by the Institut Français du Design, Concours Lépine) and show any results with links. 3) Keep a /presse/ page listing dated coverage with links.

**Verifier notes.** The run's own log contradicts the central claims ('no 2024-2026 coverage', 'suggests an inactive brand'). There is Maddyness coverage from 2024 (log 2: 'maddyness gravipack 2024'), an ici.fr (France Bleu) article ranking first for 'sac à dos anti mal de dos' in extended mode (E1), and Europe 1 coverage (log 38). The brand has RATP agent-deployment posts (Vivatech / Le Parisien). Decathlon marketplace commerce was active in 2026 (promo 18 June to 30 Aug 2026). A Concours Lépine medal is claimed on-site and on the legacy site ('Médaille d'argent concours Lépine international'). The ergo-corner reseller page leads several head-term SERPs. The fix recommends entering the Concours Lépine, which the brand has already won. The advice should be to document and use the existing award (date, category, proof link). A /presse/ page with dated coverage is the only part worth keeping.

### The children's school-bag line (Feather) raises the YMYL bar: health claims aimed at parents need pediatric or physiotherapy backing

`children-schoolbag-ymyl` · Content Quality · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** The Decathlon brand page lists Feather school bags. gravipack.com has a blog-style post at /un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/ (URL as seen in search results; note the missing hyphen in 'autresvos'). The children's line sits under the same 'anti mal de dos' positioning.

<https://gravipack.com/un-sac-a-dos-pas-comme-les-autresvos-enfants-vont-adorer/> · <https://www.decathlon.fr/brands/gravipack> · `kisskissbankbank.com`

**Why it matters.** Children's health content is squarely YMYL (health and safety, a vulnerable group). Parents searching 'cartable mal de dos enfant' or 'poids cartable' expect pediatric or physiotherapy guidance, and unreviewed claims are judged strictly.

**SEO effect.** Done well, this is a strong opportunity on informational queries ('poids cartable enfant', 'cartable ergonomique', 'cartable mal de dos'). Without expert backing, it risks a low quality assessment.

**How to fix.** 1) Have a pediatric physiotherapist review the children's product pages and the blog post, and add a 'Vérifié par' box. 2) Write a guide, 'Cartable et dos de l'enfant : les bons réflexes', citing dated, authoritative French health or pediatric sources. 3) Fix the slug to /un-sac-a-dos-pas-comme-les-autres-vos-enfants-vont-adorer/ with a 301 from the old URL. 4) Avoid absolute promises ('protège le dos de votre enfant'); prefer 'aide à mieux répartir le poids du cartable'.

**Verifier notes.** Confirmed and broader. The school-bag category title is 'Sac à dos exosquelette scolaire Gravipack allège le poids de 92%'. Other examples: the G-Pack collège/lycée product, the Kingston product promoted as 'Vive la rentrée scolaire', Decathlon Feather titles 'Allège la charge de 92%', and the legacy presta Feather page 'Sac à dos scolaire Feather Gravipack contre le mal de dos'. The children's information SERPs ('cartable ergonomique mal de dos enfant', 'sac à dos anti mal de dos enfant école', 'sac à dos scoliose enfant', 'cartable ergonomique' E9) are led by health and parent publishers and specialist retailers, with Gravipack absent. That supports the opportunity statement. Correction: the blog post's title as shown is 'Un sac à dos pas comme les autres… les épaules de vos enfants vont adorer', which makes no explicit health claim; the claims are in category and product titles. The slug-typo 301 is cosmetic and low value; keep it in the backlog.

### Home and product titles stack claim keywords ('anti mal de dos' + 'anti douleur' + 'ergonomique' + 'exosquelette' + superlatives) and run up to ~90 characters

`claim-stuffed-titles` · On-Page SEO · auditor severity **Medium** → verifier **confirmed**, severity **Medium**

**Evidence.** Titles as shown in search results (Google may rewrite them): 'Sac léger avec exosquelette anti mal de dos de montagne Sherpa Kaki Gravipack anti douleur' (~90 characters), 'Sac à dos léger et ergonomique anti-mal de dos avec exosquelette Gravipack Austerlitz' (~84), 'Gravipack : le sac révolutionnaire anti mal de dos exosquelette' (~63), 'Sac anti mal de dos business ROME ergonomique gravipack'.

<https://gravipack.com/> · <https://gravipack.com/boutique-gravipack/>

**Why it matters.** claude-seo quality gates set titles at 30-60 characters, primary keyword first, brand last. Claim-stacked titles look over-optimised to users and amplify the unsubstantiated-claim problem in the most visible part of the snippet.

**SEO effect.** Truncation beyond ~60 characters and Google title rewrites reduce control over the snippet. Claim stacking can lower CTR among skeptical buyers and raises Merchant Center policy risk.

**How to fix.** Rewrite using the 'SERP title claim audit' table, e.g. 'Sac de montagne Sherpa Kaki à exosquelette | Gravipack'. In WooCommerce, keep product names clean and set SEO titles with a Yoast / Rank Math template such as '%%title%% à exosquelette | Gravipack' or '%title% | Gravipack'. Use 'mal de dos' in the meta description and body only with benefit framing, and only where it is substantiated.

**Verifier notes.** Confirmed at scale. Of the 114 indexed URLs logged in tables.md, 87 titles exceed claude-seo's 60-character gate, and the longest runs to 204 characters (Compostelle 65 L). 13 URLs carry a templated suffix ' - Gravipack, le sac à dos exosquelette anti-mal de dos homme femme enfant'; seo-content treats templated metadata as high-severity. Superlative or claim tokens: 'révolutionnaire' ×9, 'apesanteur' ×6, 'soulage' ×6, 'meilleur' ×3 (including 'certainement le meilleur sac au monde' in a slug), 'la seule au monde' (Tokyo slug), '92%' ×2, 'anti-TMS' ×2. Minor correction: Austerlitz is 85 characters, not ~84; Sherpa Kaki 90 and home 63 are verified. The titles were captured by the run's search tool, not Google.fr, so they may differ from the real title tag. This is an on-page item; deduplicate it with the on-page/content agent.

### Health-claim wording may trigger Google Merchant Center misrepresentation or healthcare policy reviews

`merchant-center-health-claim-risk` · E-commerce · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** Product titles shown in search results include 'anti douleur' and 'anti mal de dos'. Whether gravipack.com has a Merchant Center account, and its policy status, is unknown.

<https://gravipack.com/boutique-gravipack/> · <https://gravipack.com/>

**Why it matters.** Google's Shopping policies prohibit misleading or unsubstantiated claims (misrepresentation) and restrict health claims. Disapproved products lose free listings and Shopping ads.

**SEO effect.** Free product listings and product rich results are a large part of e-commerce visibility. An account-level misrepresentation suspension removes every product.

**How to fix.** 1) Check Merchant Center diagnostics for policy flags. 2) Use the cleaned titles in the product feed; feed titles may differ from the H1 but must be accurate. 3) Remove 'anti douleur' from feed titles and descriptions, and link the proof page from landing pages. 4) Make the business details in Merchant Center (address, phone, returns policy) match the mentions légales and the on-site policies, because Google checks this for misrepresentation.

**Verifier notes.** Whether a Merchant Center account exists, and its status, is entirely unknown, so the risk is hypothetical. The policy reference needs correcting. Google's Shopping 'Healthcare and medicines' policy mainly targets drugs, supplements and unapproved substances, so it is unlikely to apply to a backpack unless it is sold as a medical device. The relevant policy for unproven health benefits is Misrepresentation (unreliable or unrealistic claims). Feed operations note: the Content API for Shopping was sunset on 2026-08-18. Any WooCommerce feed plugin must be on the Merchant API, or feed fixes will not land. Overlaps with therapeutic-claims-medical-device-status.

### Third-party press and AI directories repeat unverified claims, and there is no canonical facts page for LLMs to cite

`no-canonical-facts-page-for-ai` · AI Search Readiness · auditor severity **Medium** → verifier **weakened**, severity **Low**

**Evidence.** challenge.ma repeats 'first backpack reimbursed by social security' and the 2017 army test. motherbase.ai (an AI and brand directory) and press (neozone.org, journaldugeek.com) relay brand descriptions, while randonner-leger.org gives the opposite view. These are the sources LLMs absorb about Gravipack. No first-party proof or facts page appeared in the search-result evidence.

`challenge.ma` · `motherbase.ai` · `neozone.org` · `journaldugeek.com` · `randonner-leger.org`

**Why it matters.** seo-content GEO guidance: AI systems cite clear, attributable first-party data and entity facts. If the only sources are secondary press and forums, AI answers to 'Gravipack est-il efficace ?' will mix unverified claims with skepticism.

**SEO effect.** Risk of the brand being misrepresented in AI Overviews, AI Mode, ChatGPT and Perplexity, and a missed chance to be the cited source on 'sac à dos exosquelette' and 'sac à dos mal de dos' answers.

**How to fix.** 1) Publish a short 'Gravipack en bref : faits et preuves' page covering: company facts (legal entity, founder, dates, patent numbers), what the exoskeleton does (mechanism), measured results with links, what the product does NOT claim (not a medical treatment unless certified), and reimbursement status. 2) Add answer-first FAQ sections, e.g. 'Le sac Gravipack soulage-t-il le mal de dos ?' with an evidence-based answer and its sources. 3) Keep these facts identical on the Decathlon listing, Trustpilot, LinkedIn and crowdfunding pages. 4) Ask outlets to correct outdated claims.

**Verifier notes.** Conflicting third-party facts are confirmed: motherbase.ai gives a Vincennes address, the mentions légales give Paris (EXOSQUELETTE LIGHT), the Decathlon seller is Kid'Abord, returns go to Colmar (SODILOG), challenge.ma and lematin.ma relay the reimbursement and army claims, and randonner-leger is skeptical. But 'no first-party facts page' cannot be judged: gravipack.com has an indexed /faq/ ('Foire Aux Questions des sacs à dos exosquelettes Gravipack') and /nos-engagements/, whose content is unknown. Most of the fix duplicates the entity and study findings; merge them. If an FAQ is expanded, present it as content for users and LLMs only. claude-seo records FAQ rich results as retired on 2026-05-07.
