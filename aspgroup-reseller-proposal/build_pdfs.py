"""Build the client proposal as print-ready A4 PDFs, in Romanian (for the client) and English.

Optionally fill in DETAILS below (empty values stay blank), then run:
    python3 build_pdfs.py
"""
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, NextPageTemplate, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

HERE = Path(__file__).parent

# ---------------------------------------------------------------- details
DETAILS = {
    "agency_name": "",          # printed on the signature page when set
    "client_company": "",       # printed on the signature page when set
}
PROPOSAL_NO = "OF-2026-001"
ISSUE_DATE = "06.10.2026"
VALID_UNTIL = "05.11.2026"

# One complete package at a friend price (normal price shown as the anchor).
WEBSITE_NORMAL, WEBSITE_PRICE = 5500, 1900
SEO_NORMAL, SEO_PRICE = 900, 300
CARE_PRICE = 60
LIVE_WEEKS = 12
LIVE_DAYS = LIVE_WEEKS * 7

LANG = "ro"


def L(en, ro):
    """Pick the text for the language being built."""
    return ro if LANG == "ro" else en


def eur(amount, decimals=0):
    """€1,900 in English, 1.900 € in Romanian."""
    text = f"{amount:,.{decimals}f}"
    if LANG == "ro":
        return text.replace(",", "§").replace(".", ",").replace("§", ".") + "\u00a0€"
    return "€" + text


def was(normal, now):
    """Normal price struck through, then the friend price (cents only when needed)."""
    def fmt(x):
        return eur(x, 0 if float(x).is_integer() else 2)
    return f"<strike>{fmt(normal)}</strike> <b>{fmt(now)}</b>"


# ---------------------------------------------------------------- look
FONT_DIR = Path("/usr/share/fonts/truetype/crosextra")
pdfmetrics.registerFont(TTFont("Body", FONT_DIR / "Carlito-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", FONT_DIR / "Carlito-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", FONT_DIR / "Carlito-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", FONT_DIR / "Carlito-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                              italic="Body-Italic", boldItalic="Body-BoldItalic")

NAVY = colors.HexColor("#0F2742")
ACCENT = colors.HexColor("#2F6FDE")
ACCENT_TINT = colors.HexColor("#EAF1FD")
INK = colors.HexColor("#1D2433")
MUTED = colors.HexColor("#5B6475")
RULE = colors.HexColor("#D9DEE7")
ZEBRA = colors.HexColor("#F6F8FB")

PAGE_W, PAGE_H = A4
MARGIN = 2 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

S = {
    "body": ParagraphStyle("body", fontName="Body", fontSize=10.5, leading=14.5, textColor=INK, spaceAfter=6),
    "small": ParagraphStyle("small", fontName="Body", fontSize=8.5, leading=11, textColor=MUTED),
    "cell": ParagraphStyle("cell", fontName="Body", fontSize=8.8, leading=11.2, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName="Body-Bold", fontSize=8.8, leading=11.2, textColor=INK),
    "head": ParagraphStyle("head", fontName="Body-Bold", fontSize=8.8, leading=11.2, textColor=colors.white),
    "h1": ParagraphStyle("h1", fontName="Body-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=4),
    "lead": ParagraphStyle("lead", fontName="Body", fontSize=11.5, leading=16, textColor=MUTED, spaceAfter=12),
    "h2": ParagraphStyle("h2", fontName="Body-Bold", fontSize=13, leading=17, textColor=NAVY, spaceBefore=10, spaceAfter=6),
}


def P(text, style="body"):
    return Paragraph(text, S[style])


def grid(rows, widths, header=True, first_col_bold=True, zebra=True, extra=()):
    """A styled table; rows are lists of strings (header row first)."""
    data = []
    for r, row in enumerate(rows):
        cells = []
        for c, text in enumerate(row):
            if header and r == 0:
                style = "head"
            elif first_col_bold and c == 0:
                style = "cellb"
            else:
                style = "cell"
            cells.append(Paragraph(text, S[style]))
        data.append(cells)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
    ]
    if header:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
    if zebra:
        for r in range(1 if header else 0, len(rows)):
            if r % 2 == 0:
                cmds.append(("BACKGROUND", (0, r), (-1, r), ZEBRA))
    cmds.extend(extra)
    t.setStyle(TableStyle(cmds))
    return t


def offer_box(rows, widths):
    return grid(rows, widths, zebra=False, extra=[("BACKGROUND", (0, 1), (-1, -1), ACCENT_TINT),
                                                  ("BOX", (0, 0), (-1, -1), 1, ACCENT)])


# ================================================================ pages
def inner_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Body", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, PAGE_H - 1.25 * cm, L("Website & Google Proposal", "Propunere website și Google"))
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 1.25 * cm, L("Proposal ", "Propunerea ") + PROPOSAL_NO)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_H - 1.4 * cm, PAGE_W - MARGIN, PAGE_H - 1.4 * cm)
    canvas.line(MARGIN, 1.4 * cm, PAGE_W - MARGIN, 1.4 * cm)
    canvas.drawString(MARGIN, 1.0 * cm, L("Prices in EUR, excluding VAT · Confidential",
                                          "Prețuri în EUR, fără TVA · Confidențial"))
    canvas.drawRightString(PAGE_W - MARGIN, 1.0 * cm, L("Page ", "Pagina ") + str(doc.page))
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H * 0.42, PAGE_W, PAGE_H * 0.58, stroke=0, fill=1)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H * 0.42, PAGE_W, 0.25 * cm, stroke=0, fill=1)
    canvas.restoreState()


def cover_story():
    title = ParagraphStyle("ct", fontName="Body-Bold", fontSize=34, leading=40, textColor=colors.white)
    sub = ParagraphStyle("cs", fontName="Body", fontSize=15, leading=21, textColor=colors.HexColor("#C9D6EA"))
    tag = ParagraphStyle("tag", fontName="Body-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#8FB3F0"))
    meta = [[L("Proposal no.", "Nr. propunere"), PROPOSAL_NO], [L("Date", "Data"), ISSUE_DATE],
            [L("Valid until", "Valabilă până la"), VALID_UNTIL]]
    meta_t = Table([[P(k, "cellb"), P(v, "cell")] for k, v in meta], colWidths=[3.5 * cm, 10 * cm])
    meta_t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [
        Spacer(1, 4.2 * cm),
        Paragraph(L("PROPOSAL", "PROPUNERE"), tag),
        Spacer(1, 0.3 * cm),
        Paragraph(L("Your new website<br/>and Google plan", "Noul dumneavoastră website<br/>și planul Google"), title),
        Spacer(1, 0.5 * cm),
        Paragraph(L("A website that sells directly to customers, for a dealer of Polaris, Segway Powersports, "
                    "TGB, Linhai, Indian Motorcycle, Royal Enfield and more in Romania.",
                    "Un website care vinde direct clienților, pentru un dealer Polaris, Segway Powersports, "
                    "TGB, Linhai, Indian Motorcycle, Royal Enfield și alte branduri din România."), sub),
        Spacer(1, 7.2 * cm),
        meta_t,
        NextPageTemplate("inner"),
        PageBreak(),
    ]


def summary_story():
    offer = offer_box([
        [L("Your package", "Pachetul dumneavoastră"), L("Normal price", "Preț normal"),
         L("Your price", "Prețul dvs."), L("When you pay", "Când plătiți")],
        [L("Complete website that sells to customers, with online shop and card payments",
           "Website complet care vinde clienților, cu magazin online și plată cu cardul"),
         f"<strike>{eur(WEBSITE_NORMAL)}</strike>", f"<b>{eur(WEBSITE_PRICE)}</b> " + L("one-off", "o singură dată"),
         L(f"Once it is finished and live (week {LIVE_WEEKS})",
           f"La final, când site-ul este gata și online (săptămâna {LIVE_WEEKS})")],
        [L("Google plan (SEO), our best plan", "Planul Google (SEO), cel mai bun plan al nostru"),
         f"<strike>{eur(SEO_NORMAL)}/{L('month', 'lună')}</strike>", f"<b>{eur(SEO_PRICE)}/{L('month', 'lună')}</b>",
         L("Monthly, from the month after launch", "Lunar, din luna de după lansare")],
        [L("Hosting and care: we keep the site online, safe and up to date",
           "Găzduire și mentenanță: site-ul rămâne online, sigur și actualizat"), "",
         f"<b>{eur(CARE_PRICE)}/{L('month', 'lună')}</b>",
         L("Monthly, from the month after launch", "Lunar, din luna de după lansare")],
    ], [6.6 * cm, 2.9 * cm, 3.2 * cm, 4.3 * cm])
    compare = [
        [L("Area", "Zona"), L("aspgroup.ro (the supplier)", "aspgroup.ro (furnizorul)"),
         L("Your website (sells to customers)", "Website-ul dvs. (vinde clienților)")],
        [L("Who it is for", "Pentru cine"),
         L("Presents the brands and recruits dealers", "Prezintă brandurile și recrutează dealeri"),
         L("Turns local buyers into your customers", "Transformă cumpărătorii din zonă în clienții dvs.")],
        [L("Models", "Modele"),
         L("All models by type and brand, with photos and specs",
           "Toate modelele pe tipuri și branduri, cu poze și specificații"),
         L("Search by budget, engine size, number of seats and use (fun, farm, forest, kids)",
           "Căutare după buget, capacitate motor, număr de locuri și utilizare (distracție, fermă, pădure, copii)")],
        [L("Prices", "Prețuri"), L("Prices in euro and lei", "Prețuri în euro și lei"),
         L("Lei prices update by themselves every day", "Prețurile în lei se actualizează singure în fiecare zi")],
        [L("Financing", "Finanțare"),
         L("“Rate de la 40 €/lună” on each model", "„Rate de la 40 €/lună” pe fiecare model"),
         L("Customers see their monthly payment and apply for financing online",
           "Clienții își văd rata lunară și cer finanțare online")],
        [L("Customers", "Clienți"),
         L("Contact form and phone numbers", "Formular de contact și numere de telefon"),
         L("Buttons to ask for a price, book a test ride, reserve with a card deposit, value a trade-in, call or WhatsApp",
           "Butoane pentru cerere de ofertă, test drive, rezervare cu avans pe card, evaluare buy-back, apel sau WhatsApp")],
        [L("Showrooms", "Showroomuri"),
         L("The supplier's 4 showrooms", "Cele 4 showroomuri ale furnizorului"),
         L("Your showrooms, with map, hours and Google reviews", "Showroomurile dvs., cu hartă, program și recenzii Google")],
        [L("Online shop", "Magazin online"),
         L("Parts sold on a separate site", "Piese vândute pe un site separat"),
         L("Your own shop for parts, helmets and clothing, paid by card",
           "Magazinul dvs. pentru piese, căști și echipamente, cu plata cu cardul")],
        [L("Used vehicles", "Vehicule rulate"), "—",
         L("A page for used vehicles and trade-ins", "O pagină pentru vehicule second-hand și buy-back")],
    ]
    return [
        P(L("Summary", "Pe scurt"), "h1"),
        P(L("aspgroup.ro is the supplier's website: it presents the brands and serves dealers. We will build you "
            "something different: a website that sells directly to customers (B2C), so people in your area find you "
            "on Google and call, book a test ride, ask for financing, reserve a vehicle or buy parts online by card.",
            "aspgroup.ro este site-ul furnizorului: prezintă brandurile și se adresează dealerilor. Noi vă construim "
            "ceva diferit: un website care vinde direct clienților (B2C), astfel încât oamenii din zona dvs. să vă "
            "găsească pe Google și să vă sune, să programeze un test drive, să ceară finanțare, să rezerve un vehicul "
            "sau să cumpere piese online cu cardul."), "lead"),
        offer,
        Spacer(1, 0.2 * cm),
        P(L(f"Because you are a friend: everything included, no deposit, and you pay for the website only when it "
            f"is finished. You save {eur(WEBSITE_NORMAL - WEBSITE_PRICE)} on the website and "
            f"{eur(SEO_NORMAL - SEO_PRICE)} every month on Google. All prices in EUR, excluding VAT.",
            f"Pentru că sunteți prieten: totul inclus, fără avans, iar website-ul îl plătiți doar când este gata. "
            f"Economisiți {eur(WEBSITE_NORMAL - WEBSITE_PRICE)} la website și {eur(SEO_NORMAL - SEO_PRICE)} în "
            f"fiecare lună la Google. Toate prețurile sunt în EUR, fără TVA."), "small"),
        P(L("Supplier site vs. your customer site", "Site-ul furnizorului vs. site-ul dvs. pentru clienți"), "h2"),
        grid(compare, [2.9 * cm, 6.2 * cm, 7.9 * cm]),
        Spacer(1, 0.25 * cm),
        P(L("Important: we write your own texts instead of copying aspgroup.ro, because Google ignores copied "
            "pages. Photos come from ASP's dealer kit, with their OK.",
            "Important: scriem texte proprii și nu copiem de pe aspgroup.ro, pentru că Google ignoră paginile "
            "copiate. Pozele vin din kitul pentru dealeri al ASP, cu acordul lor."), "small"),
        PageBreak(),
    ]


def concept_story():
    image = HERE / L("sitemap.png", "sitemap-ro.png")
    w, h = PILImage.open(image).size
    return [
        P(L("Site concept", "Conceptul site-ului"), "h1"),
        P(L("Visitors arrive from Google, Google Maps, ads or dealer listings. Every page gives them six easy "
            "ways to buy or ask, and each request goes straight to the right showroom.",
            "Vizitatorii vin din Google, Google Maps, reclame sau liste de dealeri. Fiecare pagină le oferă șase "
            "moduri simple de a cumpăra sau de a cere informații, iar fiecare cerere ajunge direct la showroomul "
            "potrivit."), "lead"),
        Image(str(image), width=CONTENT_W, height=CONTENT_W * h / w),
        PageBreak(),
    ]


def process_story():
    days = lambda a, b: L(f"Days {a}–{b}", f"Zilele {a}–{b}")
    steps = [
        [L("Step", "Pas"), L("What we do", "Ce facem noi"), L("What you see and approve", "Ce vedeți și aprobați"),
         L("When", "Când")],
        [L("1. Kick-off call", "1. Discuția de start"),
         L("We learn your business: brands, showrooms, best sellers, typical customers",
           "Înțelegem afacerea dvs.: branduri, showroomuri, cele mai vândute modele, clienții tipici"),
         L("You send us the items on the checklist", "Ne trimiteți elementele din lista de verificare"), days(1, 7)],
        [L("2. Research and site map", "2. Analiză și harta site-ului"),
         L("We study what Romanian buyers search for and what other dealers do, then plan every page and how a "
           "visitor becomes a customer",
           "Studiem ce caută cumpărătorii din România și ce fac alți dealeri, apoi planificăm fiecare pagină și "
           "drumul unui vizitator până devine client"),
         L("The list of pages, for your OK", "Lista paginilor, pentru aprobare"), days(1, 14)],
        [L("3. Wireframes", "3. Wireframe-uri (schițe)"),
         L("Simple black-and-white sketches of the main pages (home, models, model page, shop, checkout), on phone "
           "and computer, showing what goes where",
           "Schițe simple, alb-negru, ale paginilor principale (acasă, modele, pagina de model, magazin, coș), pe "
           "telefon și calculator, care arată ce se află și unde"),
         L("The sketches; you comment and approve", "Schițele; comentați și aprobați"), days(8, 21)],
        [L("4. Design in Figma", "4. Design în Figma"),
         L("The full-colour design with your logo, colours and real photos, plus a clickable prototype that works "
           "like the real site",
           "Designul complet, color, cu logo-ul, culorile și pozele dvs., plus un prototip pe care puteți da click, "
           "ca pe site-ul real"),
         L("A link you open on your phone; 2 rounds of changes, then your OK",
           "Un link pe care îl deschideți pe telefon; 2 runde de modificări, apoi aprobarea dvs."), days(15, 35)],
        [L("5. Build", "5. Construcție"),
         L("We build the site on a private test address: models, prices, shop, card payments, couriers, invoices "
           "and the financing calculator",
           "Construim site-ul pe o adresă de test privată: modele, prețuri, magazin, plăți cu cardul, curieri, "
           "facturi și calculatorul de rate"),
         L("The test link, plus a short update every week", "Link-ul de test, plus un scurt raport săptămânal"),
         days(29, 70)],
        [L("6. Content", "6. Conținut"),
         L("We write the texts and load all models and shop products",
           "Scriem textele și încărcăm toate modelele și produsele"),
         L("You check prices and texts", "Verificați prețurile și textele"), days(36, 70)],
        [L("7. Testing", "7. Testare"),
         L("We test every page, form and payment on phones and computers, including a real test order",
           "Testăm fiecare pagină, formular și plată pe telefon și calculator, inclusiv o comandă reală de test"),
         L("Your final check and OK", "Verificarea finală și aprobarea dvs."), days(71, 77)],
        [L("8. Launch", "8. Lansare"),
         L("The site goes live on your address and we connect it to Google, Google Maps and visitor stats; "
           "3 hours of training for your team",
           "Site-ul intră online pe adresa dvs. și îl conectăm la Google, Google Maps și statistici; 3 ore de "
           "instruire pentru echipa dvs."),
         L(f"Your live website. You pay the {eur(WEBSITE_PRICE)}", f"Website-ul dvs. online. Plătiți {eur(WEBSITE_PRICE)}"),
         L(f"Day {LIVE_DAYS}", f"Ziua {LIVE_DAYS}")],
        [L("9. Grow", "9. Creștere"),
         L("Every month: Google work, site care and a simple report",
           "În fiecare lună: lucru pe Google, mentenanță și un raport simplu"),
         L("The monthly report", "Raportul lunar"), L("From the next month", "Din luna următoare")],
    ]
    return [
        P(L("How we will build your website", "Cum construim website-ul dumneavoastră"), "h1"),
        P(L("We agree on the plan, the sketches and the design before we build anything. Changing a sketch takes "
            "minutes; changing a finished website takes days. So there are no surprises and no wasted money.",
            "Stabilim împreună planul, schițele și designul înainte să construim ceva. O schiță se schimbă în câteva "
            "minute; un site terminat se schimbă în câteva zile. Așa nu există surprize și nici bani pierduți."),
          "lead"),
        grid(steps, [3.0 * cm, 6.8 * cm, 5.0 * cm, 2.2 * cm]),
        Spacer(1, 0.3 * cm),
        P(L("<b>Figma</b> is the professional tool designers use. You do not need to install anything: you get a "
            "link, open it on your phone, and click through your future website as if it were live.",
            "<b>Figma</b> este instrumentul profesional folosit de designeri. Nu trebuie să instalați nimic: primiți "
            "un link, îl deschideți pe telefon și navigați prin viitorul site ca și cum ar fi deja online.")),
        P(L(f"The {LIVE_DAYS} days start when we receive the items on the checklist (last page). If something "
            "arrives late, launch moves by the same time.",
            f"Cele {LIVE_DAYS} de zile încep când primim elementele din lista de verificare (ultima pagină). Dacă "
            "ceva întârzie, lansarea se mută cu același timp."), "small"),
        PageBreak(),
    ]


def website_story():
    rows = [
        [L("Part", "Parte"), L("What you get", "Ce primiți")],
        [L("Design", "Design"),
         L("A design made for your brand, approved by you before we build",
           "Un design creat pentru brandul dvs., aprobat de dvs. înainte de construcție")],
        [L("Models", "Modele"),
         L("Every model you sell, sorted by type and brand. Customers search by budget, engine size, seats and use, "
           "and can compare up to 3 models side by side",
           "Toate modelele pe care le vindeți, pe tipuri și branduri. Clienții caută după buget, capacitate, locuri "
           "și utilizare și pot compara până la 3 modele unul lângă altul")],
        [L("Prices", "Prețuri"),
         L("Prices in euro and lei. The lei prices update by themselves every day",
           "Prețuri în euro și lei. Prețurile în lei se actualizează singure în fiecare zi")],
        [L("Getting customers", "Atragerea clienților"),
         L("On every page: ask for a price, book a test ride, value a trade-in, apply for financing, call or "
           "WhatsApp, plus a “call me back” button. Each request goes straight to the right showroom by email",
           "Pe fiecare pagină: cerere de ofertă, test drive, evaluare buy-back, cerere de finanțare, apel sau "
           "WhatsApp, plus butonul „Vă sunăm noi”. Fiecare cerere ajunge pe email direct la showroomul potrivit")],
        [L("Financing", "Finanțare"),
         L("A monthly payment calculator on every model. In the shop, customers can pay in instalments",
           "Calculator de rate pe fiecare model. În magazin, clienții pot plăti în rate")],
        [L("Reserve by card", "Rezervare cu cardul"),
         L("Customers reserve a vehicle in stock online with a card deposit you choose (e.g. €300), then sign and "
           "pay the rest at your showroom: cash, card, transfer or financing",
           "Clienții rezervă online un vehicul din stoc cu un avans pe card stabilit de dvs. (ex. 300 €), apoi "
           "semnează și plătesc restul la showroom: numerar, card, transfer sau finanțare")],
        [L("Used vehicles", "Vehicule rulate"),
         L("A page for used vehicles and trade-ins", "O pagină pentru vehicule second-hand și buy-back")],
        [L("Online shop", "Magazin online"),
         L("Sell parts, accessories, helmets and clothing online. We set up to 2,000 products for you. Card, cash "
           "on delivery or interest-free instalments; delivery by courier (Fan Courier, Sameday, Cargus) or to "
           "easybox lockers; automatic invoices",
           "Vindeți online piese, accesorii, căști și echipamente. Configurăm noi până la 2.000 de produse. Card, "
           "ramburs sau rate fără dobândă; livrare prin curier (Fan Courier, Sameday, Cargus) sau la easybox; "
           "facturi automate")],
        [L("Languages", "Limbi"), L("Romanian and English", "Română și engleză")],
        [L("Ready for Google", "Pregătit pentru Google"),
         L("Built so Google can read and rank it: fast on phones and easy for Google to understand",
           "Construit ca Google să îl înțeleagă și să îl afișeze sus: rapid pe telefon și ușor de citit pentru Google")],
        [L("Results you can see", "Rezultate vizibile"),
         L("You can see how many people visit, where they come from and how many contact you",
           "Vedeți câți oameni intră pe site, de unde vin și câți vă contactează")],
        [L("Legal", "Legal"),
         L("Cookie banner, privacy and terms pages, and the ANPC consumer badges required in Romania",
           "Banner de cookie-uri, pagini de confidențialitate și termeni și pictogramele ANPC obligatorii în România")],
        [L("After launch", "După lansare"),
         L("90 days of free fixes and 3 hours of training, so your team can add models and offers alone",
           "90 de zile de remedieri gratuite și 3 ore de instruire, ca echipa dvs. să adauge singură modele și oferte")],
        [L("Ownership", "Proprietate"), L("The website is 100% yours", "Website-ul este 100% al dvs.")],
    ]
    return [
        P(L("What the website includes", "Ce include website-ul"), "h1"),
        P(L(f"Every feature we offer, in one build, live in {LIVE_WEEKS} weeks: <b>{eur(WEBSITE_PRICE)}</b> instead "
            f"of {eur(WEBSITE_NORMAL)}, paid when it is finished.",
            f"Toate funcțiile pe care le oferim, într-un singur proiect, gata în {LIVE_WEEKS} săptămâni: "
            f"<b>{eur(WEBSITE_PRICE)}</b> în loc de {eur(WEBSITE_NORMAL)}, plătit la final."), "lead"),
        grid(rows, [3.6 * cm, 13.4 * cm]),
        PageBreak(),
    ]


def sales_story():
    rows = [
        [L("What we add", "Ce adăugăm"), L("Why it sells more", "De ce vinde mai mult")],
        [L("Clear prices on every model, in euro and lei, plus “from €X/month”",
           "Prețuri clare pe fiecare model, în euro și lei, plus „de la X €/lună”"),
         L("Buyers compare price and monthly payment first. If they cannot see them, they leave for a dealer who "
           "shows them",
           "Cumpărătorii compară întâi prețul și rata. Dacă nu le văd, pleacă la un dealer care le afișează")],
        [L("“In stock, ready now” labels and a list of vehicles available immediately",
           "Etichete „În stoc, disponibil imediat” și o listă cu vehiculele gata de livrare"),
         L("Buyers want to ride this season, not wait for an order",
           "Cumpărătorii vor să meargă cu el sezonul acesta, nu să aștepte o comandă")],
        [L("Reserve online with a card deposit", "Rezervare online cu avans pe card"),
         L("Catches buyers the moment they decide, before they visit another dealer",
           "Prinde cumpărătorul în momentul în care se decide, înainte să meargă la alt dealer")],
        [L("Free test ride, booked in 2 clicks", "Test drive gratuit, programat în 2 click-uri"),
         L("Many buyers decide only after riding the vehicle", "Mulți cumpărători se decid abia după ce conduc vehiculul")],
        [L("“Call me back” button with a fast-response promise (e.g. 15 minutes, during opening hours)",
           "Butonul „Vă sunăm noi”, cu răspuns rapid promis (ex. 15 minute, în timpul programului)"),
         L("Buyers often contact several dealers; the first one to answer has the best chance",
           "Cumpărătorii contactează adesea mai mulți dealeri; primul care răspunde are cele mai mari șanse")],
        [L("Call and WhatsApp buttons always visible on phones", "Butoane de apel și WhatsApp mereu vizibile pe telefon"),
         L("Most visitors browse on their phone, and many prefer to call or message rather than fill in a form",
           "Majoritatea vizitatorilor navighează de pe telefon și mulți preferă să sune sau să scrie decât să "
           "completeze un formular")],
        [L("“Which ATV is right for me?”: 3 quick questions (use, budget, passengers)",
           "„Ce ATV mi se potrivește?”: 3 întrebări rapide (utilizare, buget, pasageri)"),
         L("Guides first-time buyers to the right model and turns them into a request",
           "Îi ghidează pe cei care cumpără prima dată spre modelul potrivit și îi transformă în cereri")],
        [L("Trust on every page: authorized dealer badges, warranty, your own service, Google reviews, real photos "
           "of your team",
           "Încredere pe fiecare pagină: insigne de dealer autorizat, garanție, service propriu, recenzii Google, "
           "poze reale cu echipa"),
         L("People spend thousands only with a dealer they trust",
           "Oamenii cheltuie mii de euro doar la un dealer în care au încredere")],
        [L("Trade-in valuation", "Evaluare buy-back"),
         L("Many buyers need to sell their old vehicle first", "Mulți cumpărători trebuie să își vândă întâi vehiculul vechi")],
        [L("A page for farms and companies: leasing, invoice with VAT, work models",
           "O pagină pentru ferme și firme: leasing, factură cu TVA, modele de lucru"),
         L("ATVs and UTVs are work tools for farms, forestry and hunting groups",
           "ATV-urile și UTV-urile sunt unelte de lucru pentru ferme, silvicultură și asociații de vânătoare")],
        [L("A Rabla page for motorcycles", "O pagină Rabla pentru motociclete"),
         L("The government program lowers the price of a new motorcycle; ASP already promotes Royal Enfield "
           "through Rabla 2026",
           "Programul guvernamental reduce prețul unei motociclete noi; ASP promovează deja Royal Enfield prin "
           "Rabla 2026")],
        [L("Shop options Romanians expect: cash on delivery, card, interest-free instalments, easybox lockers, "
           "free delivery above a set amount",
           "Opțiunile pe care le așteaptă românii în magazin: ramburs, card, rate fără dobândă, easybox, livrare "
           "gratuită peste o anumită sumă"),
         L("When their preferred payment or delivery option is missing, shoppers abandon the cart",
           "Când lipsește metoda preferată de plată sau de livrare, cumpărătorii abandonează coșul")],
        [L("Accessory packs suggested with each vehicle (winch, plough, top case)",
           "Pachete de accesorii sugerate la fiecare vehicul (troliu, lamă de zăpadă, cutie de transport)"),
         L("Raises the value of every sale", "Crește valoarea fiecărei vânzări")],
        [L("Automatic follow-ups: abandoned-cart reminders, a review request after each sale, seasonal offers by email",
           "Mesaje automate: reamintiri pentru coșuri abandonate, cerere de recenzie după fiecare vânzare, oferte "
           "de sezon pe email"),
         L("Brings back people who did not buy the first time, and grows your Google reviews",
           "Îi aduce înapoi pe cei care nu au cumpărat prima dată și vă crește recenziile pe Google")],
        [L("Ads tracking for Google and Facebook", "Urmărire pentru reclamele Google și Facebook"),
         L("You can show ads again to people who visited but did not buy",
           "Puteți afișa din nou reclame celor care au vizitat site-ul, dar nu au cumpărat")],
    ]
    return [
        P(L("Built to sell", "Construit să vândă"), "h1"),
        P(L("Every feature below has one job: turn a visitor into a buyer. Each one is chosen for how people in "
            "Romania buy ATVs, UTVs and motorcycles, and all are included in your price.",
            "Fiecare funcție de mai jos are un singur scop: să transforme un vizitator în cumpărător. Toate sunt "
            "alese după felul în care oamenii din România cumpără ATV-uri, UTV-uri și motociclete și toate sunt "
            "incluse în preț."), "lead"),
        grid(rows, [7.6 * cm, 9.4 * cm]),
        PageBreak(),
    ]


def seo_story():
    competitors = [
        [L("Who you compete with", "Cu cine concurați"),
         L("How they get customers from Google", "Cum obțin clienți de pe Google"),
         L("How you beat them", "Cum îi depășiți")],
        [L("aspgroup.ro (the supplier)", "aspgroup.ro (furnizorul)"),
         L("Official pages for every model, plus paid Google ads",
           "Pagini oficiale pentru fiecare model, plus reclame Google plătite"),
         L("Your own texts (Google ignores copies), and a link from ASP's dealer page to your site",
           "Texte proprii (Google ignoră copiile) și un link de pe pagina de dealeri ASP către site-ul dvs.")],
        ["ATVRom",
         L("A separate website for each city (Bucharest, Brașov, Iași, Timișoara and more)",
           "Câte un site separat pentru fiecare oraș (București, Brașov, Iași, Timișoara și altele)"),
         L("Strong pages for your own area, plus Google Maps reviews from your customers",
           "Pagini puternice pentru zona dvs., plus recenzii Google Maps de la clienții dvs.")],
        ["motoclass.ro, atv-mag.ro, atv-vanzari.ro",
         L("Online catalogues with several brands", "Cataloage online cu mai multe branduri"),
         L("Easier search, monthly payments and buying guides", "Căutare mai ușoară, rate lunare și ghiduri de cumpărare")],
        ["polarisofficial.ro",
         L("The official Polaris site, with a list of dealers", "Site-ul oficial Polaris, cu lista dealerilor"),
         L("Get listed there: it is free and Google values it", "Listați-vă acolo: este gratuit și Google îl apreciază")],
        ["OLX", L("Dealers post vehicles for sale there", "Dealerii publică acolo vehicule de vânzare"),
         L("Use it too, for extra customers", "Folosiți-l și dvs., pentru clienți în plus")],
    ]
    keywords = [
        [L("What people search for", "Ce caută oamenii"),
         L("Examples of what they type in Google", "Exemple de ce scriu pe Google"),
         L("How hard to win", "Cât de greu")],
        [L("A model and its price", "Un model și prețul lui"),
         "linhai 370 promax pret, segway at5 l eps pret, royal enfield hunter 350 pret", L("Easy", "Ușor")],
        [L("A vehicle for a job", "Un vehicul pentru o activitate"),
         "atv pentru agricultura, utv pentru ferma, atv pentru vanatoare, atv copii", L("Easy", "Ușor")],
        [L("Comparisons", "Comparații"), "linhai vs cfmoto, segway vs polaris, atv vs utv", L("Easy", "Ușor")],
        [L("A dealer near them", "Un dealer aproape"), "dealer atv [oraș], atv [oraș], service atv [oraș]",
         L("Medium", "Mediu")],
        [L("Buying advice", "Sfaturi de cumpărare"), "atv inmatriculare, ce permis trebuie pentru atv, atv in rate",
         L("Medium", "Mediu")],
        [L("Parts and gear", "Piese și echipamente"), "piese linhai, accesorii atv, casca atv", L("Medium", "Mediu")],
        [L("The big general searches", "Căutările generale mari"), "atv de vanzare, utv de vanzare, motociclete noi",
         L("Hard: 6 to 12 months", "Greu: 6–12 luni")],
    ]
    plan = [
        [L("Every month", "În fiecare lună"), L("What we do for you", "Ce facem pentru dvs.")],
        ["Google Maps",
         L("We look after your Google Maps listing for each showroom: photos, weekly posts and more reviews",
           "Ne ocupăm de profilul Google Maps al fiecărui showroom: poze, postări săptămânale și mai multe recenzii")],
        [L("Business directories", "Directoare de firme"),
         L("We list your business on 35 Romanian business directories (first month)",
           "Vă listăm afacerea în 35 de directoare de firme din România (prima lună)")],
        [L("Your pages", "Paginile dvs."),
         L("We improve 20 pages of your site so Google ranks them higher",
           "Îmbunătățim 20 de pagini ale site-ului, ca Google să le afișeze mai sus")],
        [L("Model texts", "Texte de model"),
         L("We write 12 original model descriptions", "Scriem 12 descrieri originale de modele")],
        [L("Articles", "Articole"),
         L("We write 5 articles in Romanian, such as “Which ATV for a farm?” or “Linhai vs CFMOTO”",
           "Scriem 5 articole în română, de exemplu „Ce ATV să aleg pentru fermă?” sau „Linhai vs CFMOTO”")],
        [L("Recommendations", "Recomandări"),
         L("4 Romanian moto, auto, farming or news websites link to yours (Google trusts sites that others "
           "recommend), plus 1 press article every 3 months",
           "4 site-uri românești de moto, auto, agricultură sau știri pun link către site-ul dvs. (Google are "
           "încredere în site-urile recomandate de alții), plus 1 articol de presă la 3 luni")],
        [L("Health check", "Verificare tehnică"),
         L("We check the site every week and fix any problem", "Verificăm site-ul săptămânal și rezolvăm orice problemă")],
        [L("Extras", "Extra"),
         L("Pages for the cities you serve, help with your YouTube videos, your shop products shown on Google Shopping",
           "Pagini pentru orașele în care vindeți, ajutor pentru clipurile YouTube, produsele din magazin afișate în "
           "Google Shopping")],
        [L("Report", "Raport"),
         L("A simple monthly report: how many calls, messages and requests came from Google, and a monthly call",
           "Un raport lunar simplu: câte apeluri, mesaje și cereri au venit de pe Google, plus o discuție lunară")],
    ]
    expect = [
        [L("Months 1–3", "Lunile 1–3"),
         L("Your showrooms start showing on Google Maps, and the first model pages appear on Google.",
           "Showroomurile dvs. încep să apară pe Google Maps, iar primele pagini de model apar pe Google.")],
        [L("Months 4–6", "Lunile 4–6"),
         L("People who search for models, comparisons or a dealer in your city find you and contact you.",
           "Oamenii care caută modele, comparații sau un dealer în orașul dvs. vă găsesc și vă contactează.")],
        [L("Months 7–12", "Lunile 7–12"),
         L("We go after the big searches, such as “atv de vanzare”.",
           "Atacăm căutările mari, precum „atv de vanzare”.")],
    ]
    return [
        P(L("Your chance on Google", "Șansa dumneavoastră pe Google"), "h1"),
        P(L("When someone in Romania wants an ATV or a motorcycle, they search on Google. The supplier and the "
            "big dealer networks show up for the general searches. But searches for a specific model, or for a dealer "
            "in your city, are still easy to win, and those people are ready to buy.",
            "Când cineva din România vrea un ATV sau o motocicletă, caută pe Google. Furnizorul și rețelele mari de "
            "dealeri apar la căutările generale. Dar căutările pentru un anumit model sau pentru un dealer din "
            "orașul dvs. sunt încă ușor de câștigat, iar acești oameni sunt gata să cumpere."), "lead"),
        grid(competitors, [3.6 * cm, 6.4 * cm, 7.0 * cm]),
        P(L("What your future customers search for", "Ce caută viitorii dvs. clienți"), "h2"),
        P(L("We will confirm the exact searches in the first two weeks.",
            "Confirmăm căutările exacte în primele două săptămâni."), "small"),
        Spacer(1, 0.1 * cm),
        grid(keywords, [4.0 * cm, 9.6 * cm, 3.4 * cm]),
        PageBreak(),
        P(L("What the Google plan (SEO) includes", "Ce include planul Google (SEO)"), "h1"),
        P(L("SEO means getting your website onto the first page of Google when people search for what you sell, "
            f"without paying for each click. Our best plan: <b>{eur(SEO_PRICE)}/month</b> instead of "
            f"{eur(SEO_NORMAL)}. It starts the month after launch, for at least 6 months, with no extra costs.",
            "SEO înseamnă ca site-ul dvs. să apară pe prima pagină Google când oamenii caută ce vindeți, fără să "
            f"plătiți pentru fiecare click. Cel mai bun plan al nostru: <b>{eur(SEO_PRICE)}/lună</b> în loc de "
            f"{eur(SEO_NORMAL)}. Începe în luna de după lansare, pe minimum 6 luni, fără costuri suplimentare."),
          "lead"),
        grid(plan, [3.6 * cm, 13.4 * cm]),
        P(L("What to expect", "La ce să vă așteptați"), "h2"),
        grid(expect, [2.7 * cm, 14.3 * cm], header=False),
        Spacer(1, 0.25 * cm),
        P(L("We measure success in customers who contact you, not just in Google positions. Nobody can honestly "
            "promise you #1 on Google; we promise the work above and a clear report every month.",
            "Măsurăm succesul în clienți care vă contactează, nu doar în poziții pe Google. Nimeni nu vă poate "
            "promite cinstit locul 1 pe Google; noi vă promitem munca de mai sus și un raport clar în fiecare lună.")),
        PageBreak(),
    ]


def costs_story():
    month = L("month", "lună")
    once = L("one-off", "o singură dată")
    costs = [
        [L("Item", "Ce"), L("Price (EUR, excl. VAT)", "Preț (EUR, fără TVA)"), L("Notes", "Detalii")],
        [L("Hosting and care: we keep the site online, safe, backed up and up to date, plus 1 hour of small changes "
           "per month",
           "Găzduire și mentenanță: site-ul rămâne online, sigur, cu backup și actualizat, plus 1 oră de mici "
           "modificări pe lună"),
         f"{eur(CARE_PRICE)}/{month}",
         L("Needed unless you have your own technical team", "Necesar dacă nu aveți propria echipă tehnică")],
        [L("Website address (.ro domain)", "Adresa site-ului (domeniu .ro)"),
         L("About €10/year", "Aprox. 10 €/an"),
         L("Registered in your company's name", "Înregistrat pe numele firmei dvs.")],
        [L("Card payment fees", "Comisioane pentru plățile cu cardul"),
         L("A small % per sale", "Un mic procent din vânzare"),
         L("Paid to the payment company, e.g. Netopia or Stripe", "Plătite firmei de plăți, ex. Netopia sau Stripe")],
        [L("Model texts written before launch", "Texte de model scrise înainte de lansare"),
         was(15, 4.5) + L(" per model", " pe model"),
         L("After launch, the Google plan writes 12 per month", "După lansare, planul Google scrie 12 pe lună")],
        [L("One more language", "Încă o limbă"), was(500, 150) + " " + once,
         L("For example Hungarian", "De exemplu maghiară")],
        [L("Logo and brand design", "Logo și identitate de brand"), was(350, 105) + " " + once,
         L("Only if you do not have one yet", "Doar dacă nu aveți deja unul")],
        [L("Photo and video shoot at your showroom", "Ședință foto și video la showroom"),
         L("Price on request", "Preț la cerere"),
         L("Your own photos and videos sell better", "Pozele și clipurile proprii vând mai bine")],
        [L("Running your Google and Facebook ads", "Administrarea reclamelor Google și Facebook"),
         L("From ", "De la ") + was(250, 75) + f"/{month}"
         + L(" plus ad budget, plus 5% of the net profit from sales the ads bring",
             " plus bugetul de reclame, plus 5% din profitul net al vânzărilor aduse de reclame"),
         L("The offer pages are already ready for it", "Paginile de oferte sunt deja pregătite")],
        [L("Extra work not in the package", "Lucrări în afara pachetului"),
         was(25, 7.5) + L("/hour", "/oră"),
         L("Always priced and agreed before we start", "Întotdeauna stabilite și agreate înainte")],
    ]
    return [
        P(L("Running costs and add-ons", "Costuri lunare și opțiuni extra"), "h1"),
        P(L(f"After launch the site costs {eur(CARE_PRICE)} a month plus the domain; the add-ons are optional.",
            f"După lansare, site-ul costă {eur(CARE_PRICE)} pe lună plus domeniul; opțiunile extra sunt la alegere."),
          "lead"),
        grid(costs, [6.4 * cm, 5.6 * cm, 5.0 * cm]),
        PageBreak(),
    ]


def acceptance_story():
    needs = [
        L("Company details: legal name, CUI, Trade Register number and registered address",
          "Datele firmei: denumire, CUI, număr de înregistrare la Registrul Comerțului și sediul social"),
        L("The website address you want (we can help you choose and register one)",
          "Adresa de site dorită (vă putem ajuta să o alegeți și să o înregistrați)"),
        L("Your logo and brand colours, if you have them", "Logo-ul și culorile brandului, dacă le aveți"),
        L("The brands and models you sell", "Brandurile și modelele pe care le vindeți"),
        L("ASP's dealer kit: photos, logos, spec sheets and price list",
          "Kitul pentru dealeri ASP: poze, logo-uri, fișe tehnice și lista de prețuri"),
        L("For each showroom: address, opening hours, phone, WhatsApp number and the email that should receive requests",
          "Pentru fiecare showroom: adresa, programul, telefonul, numărul de WhatsApp și emailul care primește cererile"),
        L("Your financing partner and its terms (bank or leasing company)",
          "Partenerul de finanțare și condițiile lui (bancă sau firmă de leasing)"),
        L("Access to your Google and Facebook business accounts, if you have any",
          "Acces la conturile Google și Facebook ale firmei, dacă există"),
        L("For the shop: accounts for card payments (Netopia or Stripe), a courier and invoicing (SmartBill or Oblio); "
          "we help you open them",
          "Pentru magazin: conturi pentru plata cu cardul (Netopia sau Stripe), curier și facturare (SmartBill sau "
          "Oblio); vă ajutăm să le deschideți"),
    ]
    box = "<font color='#2F6FDE'>□</font>"
    accepted = offer_box([
        [L("What you accept", "Ce acceptați"), L("Price", "Preț")],
        [L(f"Complete website that sells to customers, with online shop, live in {LIVE_WEEKS} weeks, paid when finished",
           f"Website complet care vinde clienților, cu magazin online, gata în {LIVE_WEEKS} săptămâni, plătit la final"),
         f"<b>{eur(WEBSITE_PRICE)}</b> " + L("one-off", "o singură dată")],
        [L("Google plan (SEO), our best plan, for at least 6 months",
           "Planul Google (SEO), cel mai bun plan al nostru, minimum 6 luni"),
         f"<b>{eur(SEO_PRICE)}/{L('month', 'lună')}</b>"],
        [L("Hosting and care", "Găzduire și mentenanță"), f"<b>{eur(CARE_PRICE)}/{L('month', 'lună')}</b>"],
    ], [12.0 * cm, 5.0 * cm])

    def sign_block(title, company):
        rows = [[P(f"<b>{title}</b>", "cell")], [P(L("Company: ", "Firma: ") + company, "cell")],
                [P(L("Name:", "Nume:"), "cell")], [P(L("Signature:", "Semnătura:"), "cell")],
                [P(L("Date:", "Data:"), "cell")]]
        t = Table(rows, colWidths=[8.2 * cm], rowHeights=[0.8 * cm, 0.9 * cm, 0.9 * cm, 1.6 * cm, 0.9 * cm])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.75, RULE),
            ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
            ("BACKGROUND", (0, 0), (-1, 0), ZEBRA),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
        ]))
        return t

    signs = Table([[sign_block("Client", DETAILS["client_company"]),
                    sign_block(L("Agency", "Agenție"), DETAILS["agency_name"])]], colWidths=[8.5 * cm, 8.5 * cm])
    signs.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return [
        P(L("What we need from you to start", "De ce avem nevoie ca să începem"), "h1"),
        P(L("Send us these and we start the same week.",
            "Trimiteți-ne aceste elemente și începem în aceeași săptămână."), "lead"),
        *[P(f"{box}&nbsp;&nbsp;{n}") for n in needs],
        P(L("Acceptance", "Acceptare"), "h2"),
        accepted,
        Spacer(1, 0.3 * cm),
        P(L("By signing, both parties accept the scope and prices in this proposal. All prices in EUR, excluding VAT.",
            "Prin semnare, ambele părți acceptă conținutul și prețurile din această propunere. Toate prețurile sunt "
            "în EUR, fără TVA."), "small"),
        Spacer(1, 0.4 * cm),
        KeepTogether(signs),
    ]


def build_proposal(lang, path):
    global LANG
    LANG = lang
    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=2 * cm, bottomMargin=2 * cm,
                          title=L("Your new website and Google plan", "Noul dumneavoastră website și planul Google"),
                          author=DETAILS["agency_name"] or L("Proposal", "Propunere"),
                          subject=L("Proposal ", "Propunerea ") + PROPOSAL_NO)
    frame = Frame(MARGIN, 2 * cm, CONTENT_W, PAGE_H - 4 * cm, id="f", leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate("cover", frames=[frame], onPage=cover_page),
        PageTemplate("inner", frames=[frame], onPage=inner_page),
    ])
    story = (cover_story() + summary_story() + concept_story() + process_story() + website_story()
             + sales_story() + seo_story() + costs_story() + acceptance_story())
    doc.build(story)


if __name__ == "__main__":
    build_proposal("ro", HERE / f"Propunere-{PROPOSAL_NO}-Website-Google-RO.pdf")
    build_proposal("en", HERE / f"Proposal-{PROPOSAL_NO}-Website-Google-EN.pdf")
    print("PDFs written to", HERE)
