"""Build the client proposal and the deposit proforma invoice as print-ready A4 PDFs.

Fill in DETAILS below (empty values print as yellow placeholders), then run:
    python3 build_pdfs.py
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
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
    "agency_name": "",          # e.g. "Studio Name SRL"
    "agency_address": "",
    "agency_tax_id": "",        # VAT / CUI
    "agency_reg_no": "",        # trade register number
    "agency_contact": "",       # email · phone
    "agency_bank": "",
    "agency_iban": "",
    "agency_swift": "",
    "client_company": "",       # e.g. "Moto Dealer SRL"
    "client_address": "",
    "client_tax_id": "",        # CUI
    "client_reg_no": "",        # J../..../....
    "client_contact": "",       # contact person
    "vat_rate": None,           # e.g. 21 or 0 (reverse charge); None = to be confirmed
}
PROPOSAL_NO = "OF-2026-001"
PROFORMA_NO = "PF-2026-001"
ISSUE_DATE = "06.10.2026"
VALID_UNTIL = "05.11.2026"
DUE_DATE = "13.10.2026"

# One complete package at a friend price (normal price shown as the anchor).
WEBSITE_NORMAL, WEBSITE_PRICE = 5500, 1900
SEO_NORMAL, SEO_PRICE = 900, 300
CARE_PRICE = 60
LIVE_WEEKS = 12
DEPOSIT_SHARE, DESIGN_SHARE = 0.40, 0.30

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
PLACEHOLDER_BG = "#FFF1A8"

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
    "right": ParagraphStyle("right", fontName="Body", fontSize=8.8, leading=11.2, textColor=INK, alignment=TA_RIGHT),
    "rightb": ParagraphStyle("rightb", fontName="Body-Bold", fontSize=8.8, leading=11.2, textColor=INK, alignment=TA_RIGHT),
}


def ph(key, label):
    """The configured value, or a highlighted placeholder to fill in."""
    value = DETAILS.get(key)
    if value:
        return value
    return f"<font backColor='{PLACEHOLDER_BG}'>&nbsp;[{label}]&nbsp;</font>"


def eur(amount, cents=True):
    return f"€{amount:,.2f}" if cents else f"€{amount:,.0f}"


def schedule():
    deposit = round(WEBSITE_PRICE * DEPOSIT_SHARE, 2)
    design = round(WEBSITE_PRICE * DESIGN_SHARE, 2)
    return deposit, design, round(WEBSITE_PRICE - deposit - design, 2)


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


# ================================================================ proposal
def proposal_frame_pages(canvas, doc):
    canvas.saveState()
    canvas.setFont("Body", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, PAGE_H - 1.25 * cm, "Website & SEO Proposal")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 1.25 * cm, f"Proposal {PROPOSAL_NO}")
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_H - 1.4 * cm, PAGE_W - MARGIN, PAGE_H - 1.4 * cm)
    canvas.line(MARGIN, 1.4 * cm, PAGE_W - MARGIN, 1.4 * cm)
    canvas.drawString(MARGIN, 1.0 * cm, "Prices in EUR, excluding VAT · Confidential")
    canvas.drawRightString(PAGE_W - MARGIN, 1.0 * cm, f"Page {doc.page}")
    canvas.restoreState()


def proposal_cover(canvas, doc):
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
    meta = [
        ["Prepared for", ph("client_company", "Client company")],
        ["Prepared by", ph("agency_name", "Your company name")],
        ["Proposal no.", PROPOSAL_NO],
        ["Date", ISSUE_DATE],
        ["Valid until", VALID_UNTIL],
    ]
    meta_t = Table([[P(k, "cellb"), P(v, "cell")] for k, v in meta], colWidths=[3.5 * cm, 10 * cm])
    meta_t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [
        Spacer(1, 4.2 * cm),
        Paragraph("PROPOSAL", tag),
        Spacer(1, 0.3 * cm),
        Paragraph("Website & SEO for a<br/>powersports dealer in Romania", title),
        Spacer(1, 0.5 * cm),
        Paragraph("Design, build and Google visibility for a dealer "
                  "of the ASP Group range: Polaris, Segway Powersports, TGB, Linhai, "
                  "Indian Motorcycle, Royal Enfield and more.", sub),
        Spacer(1, 6.3 * cm),
        meta_t,
        NextPageTemplate("inner"),
        PageBreak(),
    ]


def summary_story():
    deposit, _, _ = schedule()
    offer = [
        ["Your package", "Normal price", "Your price", "When"],
        ["Complete website, every feature including the online shop",
         f"<strike>{eur(WEBSITE_NORMAL, False)}</strike>", f"<b>{eur(WEBSITE_PRICE, False)}</b> one-off",
         f"Live in {LIVE_WEEKS} weeks"],
        ["Google plan (SEO), our best plan",
         f"<strike>{eur(SEO_NORMAL, False)}/month</strike>", f"<b>{eur(SEO_PRICE, False)}/month</b>",
         "From the month after launch"],
        ["Hosting and care: we keep the site online, safe and up to date", "", f"<b>{eur(CARE_PRICE, False)}/month</b>",
         "From launch"],
    ]
    offer_t = grid(offer, [7.0 * cm, 3.0 * cm, 3.4 * cm, 3.6 * cm], zebra=False,
                   extra=[("BACKGROUND", (0, 1), (-1, -1), ACCENT_TINT),
                          ("BOX", (0, 0), (-1, -1), 1, ACCENT)])
    compare = [
        ["Area", "What aspgroup.ro has", "What your site adds"],
        ["Models", "All models by type (ATV, UTV, motorcycle) and brand, with photos and specs",
         "Search by budget, engine size, number of seats and use (fun, farm, forest, kids)"],
        ["Prices", "Prices in euro and lei", "Lei prices update by themselves every day"],
        ["Financing", "“Rate de la 40 €/lună” on each model",
         "Customers see their monthly payment and can apply for financing online"],
        ["Offers", "A page with current offers", "Offer pages ready for Google and Facebook ads"],
        ["Customers", "Contact form and phone numbers",
         "Buttons to ask for a price, book a test ride, value a trade-in, call or WhatsApp. "
         "You see which ones bring customers"],
        ["Showrooms", "Their 4 showrooms listed", "A page for each of your showrooms with map, hours and Google reviews"],
        ["Articles", "Company news", "Buying guides and comparisons that people in Romania search for"],
        ["Parts and gear", "A separate shop (aspshop.ro)", "Your own online shop for parts, helmets and clothing"],
        ["Used vehicles", "—", "A page for used vehicles and trade-ins"],
    ]
    return [
        P("Summary", "h1"),
        P("One complete package, everything included, at a friend price: a website that sells the full "
          "ASP Group range and has its own online shop, plus our best Google plan so local buyers find "
          "you and call, book a test ride or ask for financing.", "lead"),
        offer_t,
        Spacer(1, 0.2 * cm),
        P(f"You save {eur(WEBSITE_NORMAL - WEBSITE_PRICE, False)} on the website and "
          f"{eur(SEO_NORMAL - SEO_PRICE, False)} every month on Google. To start: a 40% deposit of "
          f"{eur(deposit, False)}. All prices in EUR, excluding VAT.", "small"),
        P("Compared with aspgroup.ro", "h2"),
        P("Your site keeps everything good about the importer's site and adds what a dealer needs to "
          "win customers in your area."),
        grid(compare, [2.9 * cm, 6.4 * cm, 7.7 * cm]),
        Spacer(1, 0.25 * cm),
        P("Important: we write your own texts instead of copying aspgroup.ro, because Google ignores copied "
          "pages. Photos come from ASP's dealer kit, with their OK.", "small"),
        PageBreak(),
    ]


def concept_story():
    img = Image(str(HERE / "sitemap.png"), width=CONTENT_W, height=CONTENT_W * 1286 / 1344)
    return [
        P("Site concept", "h1"),
        P("Visitors land on any page from search, maps, ads or dealer listings. Every page keeps the five "
          "lead actions one tap away, and each lead is sent to the right showroom.", "lead"),
        img,
        PageBreak(),
    ]


def website_story():
    rows = [
        ["Part", "What you get"],
        ["Design", "A design made for your brand. You see it first and can ask for changes twice before we build"],
        ["Models", "Every model you sell, sorted by type and brand. Customers search by budget, engine size, seats "
                   "and use, and can compare up to 3 models side by side"],
        ["Prices", "Prices in euro and lei. The lei prices update by themselves every day"],
        ["Getting customers", "On every page: ask for a price, book a test ride, value a trade-in, apply for financing, "
                              "call or WhatsApp. Each request goes straight to the right showroom by email"],
        ["Financing", "A monthly payment calculator on every model. In the shop, customers can pay in instalments"],
        ["Used vehicles", "A page for used vehicles and trade-ins"],
        ["Online shop", "Sell parts, accessories, helmets and clothing online. We set up to 2,000 products for you. "
                        "Card payment, courier delivery (Fan Courier, Sameday, Cargus) and automatic invoices"],
        ["Languages", "Romanian and English"],
        ["Ready for Google", "Built so Google can read and rank it: fast on phones and easy for Google to understand"],
        ["Results you can see", "You can see how many people visit, where they come from and how many contact you"],
        ["Legal", "Cookie banner, privacy and terms pages, and the ANPC consumer badges required in Romania"],
        ["After launch", "90 days of free fixes and 3 hours of training, so your team can add models and offers alone"],
        ["Ownership", "The website is 100% yours"],
    ]
    return [
        P("What the website includes", "h1"),
        P(f"Every feature we offer, in one build, live in {LIVE_WEEKS} weeks: "
          f"<b>{eur(WEBSITE_PRICE, False)}</b> one-off instead of {eur(WEBSITE_NORMAL, False)}.", "lead"),
        grid(rows, [3.6 * cm, 13.4 * cm]),
        PageBreak(),
    ]


def seo_story():
    competitors = [
        ["Who you compete with", "How they get customers from Google", "How you beat them"],
        ["aspgroup.ro (the importer)", "Official pages for every model, plus paid Google ads",
         "Your own texts (Google ignores copies), and a link from ASP's dealer page to your site"],
        ["ATVRom", "A separate website for each city (Bucharest, Brașov, Iași, Timișoara and more)",
         "Strong pages for your own area, plus Google Maps reviews from your customers"],
        ["motoclass.ro, atv-mag.ro, atv-vanzari.ro", "Online catalogues with several brands",
         "Easier search, monthly payments and buying guides"],
        ["polarisofficial.ro", "The official Polaris site, with a list of dealers",
         "Get listed there: it is free and Google values it"],
        ["OLX", "Dealers post vehicles for sale there", "Use it too, for extra customers"],
    ]
    keywords = [
        ["What people search for", "Examples of what they type in Google", "How hard to win"],
        ["A model and its price", "linhai 370 promax pret, segway at5 l eps pret, royal enfield hunter 350 pret", "Easy"],
        ["A vehicle for a job", "atv pentru agricultura, utv pentru ferma, atv pentru vanatoare, atv copii", "Easy"],
        ["Comparisons", "linhai vs cfmoto, segway vs polaris, atv vs utv", "Easy"],
        ["A dealer near them", "dealer atv [oraș], atv [oraș], service atv [oraș]", "Medium"],
        ["Buying advice", "atv inmatriculare, ce permis trebuie pentru atv, atv in rate", "Medium"],
        ["Parts and gear", "piese linhai, accesorii atv, casca atv", "Medium"],
        ["The big general searches", "atv de vanzare, utv de vanzare, motociclete noi", "Hard: 6 to 12 months"],
    ]
    plan = [
        ["Every month", "What we do for you"],
        ["Google Maps", "We look after your Google Maps listing for each showroom: photos, weekly posts and more reviews"],
        ["Business directories", "We list your business on 35 Romanian business directories (first month)"],
        ["Your pages", "We improve 20 pages of your site so Google ranks them higher"],
        ["Model texts", "We write 12 original model descriptions"],
        ["Articles", "We write 5 articles in Romanian, such as “Which ATV for a farm?” or “Linhai vs CFMOTO”"],
        ["Recommendations", "4 Romanian moto, auto, farming or news websites link to yours (Google trusts sites "
                            "that others recommend), plus 1 press article every 3 months"],
        ["Health check", "We check the site every week and fix any problem"],
        ["Extras", "Pages for the cities you serve, help with your YouTube videos, your shop products shown on Google Shopping"],
        ["Report", "A simple monthly report: how many calls, messages and requests came from Google, and a monthly call"],
    ]
    expect = [
        ["Months 1–3", "Your showrooms start showing on Google Maps, and the first model pages appear on Google."],
        ["Months 4–6", "People who search for models, comparisons or a dealer in your city find you and contact you."],
        ["Months 7–12", "We go after the big searches, such as “atv de vanzare”."],
    ]
    return [
        P("Your chance on Google", "h1"),
        P("When someone in Romania wants an ATV or a motorcycle, they search on Google. The importer and the "
          "big dealer networks show up for the general searches. But searches for a specific model, or for a dealer "
          "in your city, are still easy to win, and those people are ready to buy.", "lead"),
        grid(competitors, [3.6 * cm, 6.4 * cm, 7.0 * cm]),
        P("What your future customers search for", "h2"),
        P("We will confirm the exact searches in the first two weeks.", "small"),
        Spacer(1, 0.1 * cm),
        grid(keywords, [4.0 * cm, 9.6 * cm, 3.4 * cm]),
        PageBreak(),
        P("What the Google plan (SEO) includes", "h1"),
        P("SEO means getting your website onto the first page of Google when people search for what you sell, "
          f"without paying for each click. Our best plan: <b>{eur(SEO_PRICE, False)}/month</b> instead of "
          f"{eur(SEO_NORMAL, False)}. It starts the month after launch, for at least 6 months, with no extra costs.", "lead"),
        grid(plan, [3.6 * cm, 13.4 * cm]),
        P("What to expect", "h2"),
        grid(expect, [2.7 * cm, 14.3 * cm], header=False),
        Spacer(1, 0.25 * cm),
        P("We measure success in customers who contact you, not just in Google positions. Nobody can honestly "
          "promise you #1 on Google; we promise the work above and a clear report every month."),
        PageBreak(),
    ]


def costs_story():
    deposit, design, launch = schedule()
    costs = [
        ["Item", "Price (EUR, excl. VAT)", "Notes"],
        ["Hosting and care: we keep the site online, safe, backed up and up to date, plus 1 hour of small "
         "changes per month", f"{eur(CARE_PRICE, False)}/month", "Needed unless you have your own technical team"],
        ["Website address (.ro domain)", "About €10/year", "Registered in your company's name"],
        ["Card payment fees", "A small % per sale", "Paid to the payment company, e.g. Netopia or Stripe"],
        ["Model texts written before launch", "€15 per model", "After launch, the Google plan writes 12 per month"],
        ["One more language", "€500 one-off", "For example Hungarian"],
        ["Logo and brand design", "€350 one-off", "Only if you do not have one yet"],
        ["Photo and video shoot at your showroom", "Price on request", "Your own photos and videos sell better"],
        ["Running your Google and Facebook ads", "From €250/month plus ad budget", "The offer pages are already ready for it"],
        ["Extra work not in the package", "€25/hour", "Always priced and agreed before we start"],
    ]
    terms = [
        f"The website is paid in three parts: 40% to start ({eur(deposit, False)}), 30% when you approve the "
        f"design ({eur(design, False)}) and 30% when the site goes live ({eur(launch, False)}).",
        f"This friend price is valid until {VALID_UNTIL}.",
        "Prices are in EUR, excluding VAT. You can also pay in lei at the National Bank (BNR) rate on the invoice date.",
        "The Google plan and hosting are paid monthly, starting the month after launch. The Google plan runs at least 6 months.",
        "You can ask for design changes twice. Anything extra costs €25/hour and is always agreed first.",
        "The 12 weeks start when we receive the items on the checklist. If something arrives late, launch moves by the same time.",
        "Once fully paid, the website, its design and its texts are 100% yours, and every account is in your company's name.",
        "We provide the legal pages (terms, privacy, cookies, returns) as templates; your lawyer should approve them.",
        "Brand logos and photos follow each brand's rules for dealers and need ASP's OK before launch.",
    ]
    return [
        P("Running costs and add-ons", "h1"),
        P(f"After launch the site costs {eur(CARE_PRICE, False)} a month plus the domain; the add-ons are optional.", "lead"),
        grid(costs, [7.4 * cm, 4.6 * cm, 5.0 * cm]),
        P("Payment terms", "h2"),
        *[P(f"•&nbsp;&nbsp;{t}") for t in terms],
        PageBreak(),
    ]


def process_story():
    deposit, design, launch = schedule()
    steps = [
        ["Step", "What happens", "Who", "When", "Payment"],
        ["1. Accept", "You sign the acceptance page", "You", "Week 0", "—"],
        ["2. Deposit", "We send a proforma invoice for the deposit", "Both", "Week 0", f"40%: {eur(deposit, False)}"],
        ["3. Start", "We study what your customers search for and plan the pages; you send us the items below",
         "Both", "Weeks 1–2", "—"],
        ["4. Design", "We show you the design; you ask for changes (twice) and approve it", "Us, then you", "Weeks 2–4",
         f"30%: {eur(design, False)}"],
        ["5. Build", "We build the site, add your models and set up the shop", "Us", "Weeks 4–11", "—"],
        ["6. Test", "We test everything on phones and computers; you check it too", "Both", "Week 11", "—"],
        ["7. Launch", "The site goes live and we connect it to Google and Google Maps", "Us", f"Week {LIVE_WEEKS}",
         f"30%: {eur(launch, False)}"],
        ["8. Grow", "Every month: Google work, site care and a simple report", "Us", "From the next month",
         f"{eur(SEO_PRICE + CARE_PRICE, False)}/month"],
    ]
    needs = [
        "The signed acceptance page and the deposit payment",
        "Company details: legal name, CUI, Trade Register number and registered address",
        "The website address you want (we can help you choose and register one)",
        "Your logo and brand colours, if you have them",
        "The brands and models you sell",
        "ASP's dealer kit: photos, logos, spec sheets and price list",
        "For each showroom: address, opening hours, phone, WhatsApp number and the email that should receive requests",
        "Your financing partner and its terms (bank or leasing company)",
        "Access to your Google and Facebook business accounts, if you have any",
        "For the shop: accounts for card payments (Netopia or Stripe), a courier and invoicing (SmartBill or Oblio); "
        "we help you open them",
    ]
    box = "<font color='#2F6FDE'>□</font>"
    return [
        P("How we work, step by step", "h1"),
        P(f"Eight steps from signature to a site that brings in leads, live in week {LIVE_WEEKS}.", "lead"),
        grid(steps, [2.2 * cm, 7.5 * cm, 2.2 * cm, 2.6 * cm, 2.5 * cm]),
        P("What we need from you to start", "h2"),
        *[P(f"{box}&nbsp;&nbsp;{n}") for n in needs],
        PageBreak(),
    ]


def acceptance_story():
    deposit, _, _ = schedule()
    accepted = grid([
        ["What you accept", "Price"],
        [f"Complete website, every feature including the online shop, live in {LIVE_WEEKS} weeks",
         f"<b>{eur(WEBSITE_PRICE, False)}</b> one-off"],
        ["Google plan (SEO), our best plan, for at least 6 months", f"<b>{eur(SEO_PRICE, False)}/month</b>"],
        ["Hosting and care", f"<b>{eur(CARE_PRICE, False)}/month</b>"],
    ], [12.0 * cm, 5.0 * cm], first_col_bold=False, zebra=False,
        extra=[("BACKGROUND", (0, 1), (-1, -1), ACCENT_TINT), ("BOX", (0, 0), (-1, -1), 1, ACCENT)])

    def sign_block(title, company):
        rows = [
            [P(f"<b>{title}</b>", "cell")],
            [P(f"Company: {company}", "cell")],
            [P("Name and role:", "cell")],
            [P("Signature:", "cell")],
            [P("Date:", "cell")],
        ]
        t = Table(rows, colWidths=[8.2 * cm], rowHeights=[0.8 * cm, 0.9 * cm, 0.9 * cm, 1.6 * cm, 0.9 * cm])
        t.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.75, RULE),
            ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
            ("BACKGROUND", (0, 0), (-1, 0), ZEBRA),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
        ]))
        return t

    signs = Table([[sign_block("Client", ph("client_company", "Client company")),
                    sign_block("Agency", ph("agency_name", "Your company name"))]],
                  colWidths=[8.5 * cm, 8.5 * cm])
    signs.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return [
        P("Acceptance", "h1"),
        P(f"Sign below to accept proposal {PROPOSAL_NO}. We then send the proforma invoice for the "
          f"{eur(deposit, False)} deposit and book the kickoff.", "lead"),
        accepted,
        Spacer(1, 0.4 * cm),
        P("By signing, both parties accept the scope, prices and terms in this proposal. "
          "All prices in EUR, excluding VAT.", "small"),
        Spacer(1, 0.6 * cm),
        KeepTogether(signs),
        Spacer(1, 0.8 * cm),
        P("Sources", "h2"),
        P("aspgroup.ro (home, despre-noi, devino-dealer, promotii, Linhai 110 and Rabla 2026 pages); atvrom.ro and its "
          "city sites; motoclass.ro; atv-mag.ro; atv-vanzari.ro; polarisofficial.ro/dealeri-polaris; aspgroup.olx.ro; "
          "Romanian 2026 price guides from ddc.ro, instatic.ro, aurelcirlan.ro and trifumedia.com; ANPC Order 449/2022 "
          "(SAL/SOL badges); Law 232/2022 on accessibility. Checked on 6 October 2026.", "small"),
    ]


def build_proposal(path):
    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=2 * cm, bottomMargin=2 * cm,
                          title="Website & SEO Proposal", author=DETAILS["agency_name"] or "Proposal",
                          subject=f"Proposal {PROPOSAL_NO}")
    frame = Frame(MARGIN, 2 * cm, CONTENT_W, PAGE_H - 4 * cm, id="f", leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate("cover", frames=[frame], onPage=proposal_cover),
        PageTemplate("inner", frames=[frame], onPage=proposal_frame_pages),
    ])
    story = (cover_story() + summary_story() + concept_story() + website_story() + seo_story()
             + costs_story() + process_story() + acceptance_story())
    doc.build(story)


# ================================================================ proforma
def build_proforma(path):
    deposit, design_part, launch_part = schedule()
    vat_rate = DETAILS["vat_rate"]

    def page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 0.5 * cm, PAGE_W, 0.5 * cm, stroke=0, fill=1)
        canvas.setFont("Body", 8.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, 1.0 * cm, f"Proforma {PROFORMA_NO} · Proposal {PROPOSAL_NO}")
        canvas.drawRightString(PAGE_W - MARGIN, 1.0 * cm, "Page 1 of 1")
        canvas.restoreState()

    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=1.6 * cm, bottomMargin=1.8 * cm,
                          title=f"Proforma invoice {PROFORMA_NO}", author=DETAILS["agency_name"] or "Proforma",
                          subject="Website deposit")
    frame = Frame(MARGIN, 1.8 * cm, CONTENT_W, PAGE_H - 3.4 * cm, leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate("p", frames=[frame], onPage=page)])

    title = ParagraphStyle("t", fontName="Body-Bold", fontSize=22, leading=26, textColor=NAVY)
    title_ro = ParagraphStyle("tr", fontName="Body", fontSize=12, leading=15, textColor=MUTED)
    agency = ParagraphStyle("ag", fontName="Body-Bold", fontSize=13, leading=16, textColor=INK, alignment=TA_RIGHT)

    head = Table([[
        [Paragraph("PROFORMA INVOICE", title), Paragraph("Factură proformă", title_ro)],
        [Paragraph(ph("agency_name", "Your company name"), agency)],
    ]], colWidths=[9 * cm, 8 * cm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))

    meta = Table([[P("<b>No. / Nr.</b>", "cell"), P(PROFORMA_NO, "cell"),
                   P("<b>Issue date / Data emiterii</b>", "cell"), P(ISSUE_DATE, "cell")],
                  [P("<b>Reference / Referință</b>", "cell"), P(f"Proposal {PROPOSAL_NO}", "cell"),
                   P("<b>Due date / Scadență</b>", "cell"), P(DUE_DATE, "cell")],
                  [P("<b>Currency / Monedă</b>", "cell"), P("EUR", "cell"), P("", "cell"), P("", "cell")]],
                 colWidths=[3.6 * cm, 4.9 * cm, 4.1 * cm, 4.4 * cm])
    meta.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ZEBRA), ("BOX", (0, 0), (-1, -1), 0.5, RULE),
                              ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))

    def party(label, lines):
        cells = [[P(f"<b>{label}</b>", "cell")]] + [[P(line, "cell")] for line in lines]
        t = Table(cells, colWidths=[8.2 * cm])
        t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 1, ACCENT), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        return t

    seller = party("From / Furnizor", [
        ph("agency_name", "Your company name"),
        ph("agency_address", "Address"),
        f"VAT / CIF: {ph('agency_tax_id', 'Tax ID')}",
        f"Reg. no.: {ph('agency_reg_no', 'Trade register no.')}",
        ph("agency_contact", "Email · phone"),
    ])
    buyer = party("Bill to / Cumpărător", [
        ph("client_company", "Client company SRL"),
        ph("client_address", "Registered address"),
        f"CUI: {ph('client_tax_id', 'CUI')}",
        f"Reg. Com.: {ph('client_reg_no', 'J../..../....')}",
        f"Attn.: {ph('client_contact', 'Contact person')}",
    ])
    parties = Table([[seller, buyer]], colWidths=[8.5 * cm, 8.5 * cm])
    parties.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))

    desc = ("<b>Website development, complete package: 40% advance payment</b><br/>"
            "<font color='#5B6475'>Avans 40% pentru dezvoltare website, pachet complet. "
            f"Total contract value {eur(WEBSITE_PRICE)}, per proposal {PROPOSAL_NO}.</font>")
    lines = [
        [P("#", "head"), P("Description / Descriere", "head"), P("Qty", "head"),
         Paragraph("Unit price", ParagraphStyle("hr", parent=S["head"], alignment=TA_RIGHT)),
         Paragraph("Amount", ParagraphStyle("hr2", parent=S["head"], alignment=TA_RIGHT))],
        [P("1", "cell"), P(desc, "cell"), P("1", "cell"), P(eur(deposit), "right"), P(eur(deposit), "right")],
    ]
    line_t = Table(lines, colWidths=[0.8 * cm, 10.2 * cm, 1.2 * cm, 2.4 * cm, 2.4 * cm])
    line_t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("LINEBELOW", (0, 1), (-1, -1), 0.5, RULE),
                                ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))

    if vat_rate is None:
        vat_label = f"VAT / TVA {ph('vat_rate', '__%')}"
        vat_value = ph("vat_amount", "amount")
        total_value = f"{eur(deposit)} + VAT"
    else:
        vat = round(deposit * vat_rate / 100, 2)
        vat_label = f"VAT / TVA {vat_rate}%" + (" (reverse charge)" if vat_rate == 0 else "")
        vat_value = eur(vat)
        total_value = eur(deposit + vat)
    totals = Table([
        [P("Subtotal", "right"), P(eur(deposit), "right")],
        [P(vat_label, "right"), P(vat_value, "right")],
        [Paragraph("<b>Total due / Total de plată</b>", ParagraphStyle("tt", parent=S["rightb"], fontSize=11, textColor=colors.white)),
         Paragraph(f"<b>{total_value}</b>", ParagraphStyle("tv", parent=S["rightb"], fontSize=11, textColor=colors.white))],
    ], colWidths=[5.0 * cm, 3.2 * cm], hAlign="RIGHT")
    totals.setStyle(TableStyle([("BACKGROUND", (0, 2), (-1, 2), ACCENT), ("LINEBELOW", (0, 0), (-1, 1), 0.5, RULE),
                                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))

    plan = grid([
        ["Payment schedule / Calendar de plată", "Share", "Amount"],
        ["Advance at signing: <b>this proforma</b>", "40%", eur(deposit)],
        ["On design approval", "30%", eur(design_part)],
        ["At launch", "30%", eur(launch_part)],
        ["<b>Total website, excluding VAT</b>", "100%", f"<b>{eur(WEBSITE_PRICE)}</b>"],
    ], [10.6 * cm, 2.6 * cm, 3.8 * cm], first_col_bold=False)

    pay = Table([
        [P("<b>Payment details / Date de plată</b>", "cell"), P("", "cell")],
        [P("Beneficiary", "cell"), P(ph("agency_name", "Your company name"), "cell")],
        [P("Bank", "cell"), P(ph("agency_bank", "Bank name"), "cell")],
        [P("IBAN", "cell"), P(ph("agency_iban", "IBAN"), "cell")],
        [P("SWIFT / BIC", "cell"), P(ph("agency_swift", "SWIFT"), "cell")],
        [P("Payment reference", "cell"), P(f"<b>{PROFORMA_NO}</b>", "cell")],
    ], colWidths=[3.8 * cm, 13.2 * cm])
    pay.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.75, ACCENT), ("BACKGROUND", (0, 0), (-1, 0), ACCENT_TINT),
                             ("SPAN", (0, 0), (-1, 0)), ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
                             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))

    story = [
        head, Spacer(1, 0.6 * cm), meta, Spacer(1, 0.6 * cm), parties, Spacer(1, 0.7 * cm),
        line_t, Spacer(1, 0.3 * cm), totals, Spacer(1, 0.7 * cm), plan, Spacer(1, 0.6 * cm),
        pay, Spacer(1, 0.6 * cm),
        P("This is a proforma invoice, not a fiscal document. The fiscal invoice is issued once payment is received. "
          "Payable in EUR, or in RON at the BNR rate on the payment date.", "small"),
        P("Acest document nu este factură fiscală. Factura fiscală se emite după încasarea plății. "
          "Plata se poate face în EUR sau în RON, la cursul BNR din ziua plății.", "small"),
    ]
    doc.build(story)


if __name__ == "__main__":
    build_proposal(HERE / f"Proposal-{PROPOSAL_NO}-Website-SEO.pdf")
    build_proforma(HERE / f"Proforma-{PROFORMA_NO}-Website-Deposit.pdf")
    print("PDFs written to", HERE)
