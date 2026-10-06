"""Build the client proposal as a print-ready A4 PDF.

Optionally fill in DETAILS below (empty values stay blank), then run:
    python3 build_pdfs.py
"""
from pathlib import Path

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


def eur(amount):
    return f"€{amount:,.0f}"


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
    canvas.drawString(MARGIN, PAGE_H - 1.25 * cm, "Website & Google Proposal")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 1.25 * cm, f"Proposal {PROPOSAL_NO}")
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_H - 1.4 * cm, PAGE_W - MARGIN, PAGE_H - 1.4 * cm)
    canvas.line(MARGIN, 1.4 * cm, PAGE_W - MARGIN, 1.4 * cm)
    canvas.drawString(MARGIN, 1.0 * cm, "Prices in EUR, excluding VAT · Confidential")
    canvas.drawRightString(PAGE_W - MARGIN, 1.0 * cm, f"Page {doc.page}")
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
    meta = [["Proposal no.", PROPOSAL_NO], ["Date", ISSUE_DATE], ["Valid until", VALID_UNTIL]]
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
        Paragraph("Your new website<br/>and Google plan", title),
        Spacer(1, 0.5 * cm),
        Paragraph("A website that sells directly to customers, for a dealer of Polaris, Segway Powersports, "
                  "TGB, Linhai, Indian Motorcycle, Royal Enfield and more in Romania.", sub),
        Spacer(1, 7.2 * cm),
        meta_t,
        NextPageTemplate("inner"),
        PageBreak(),
    ]


def summary_story():
    offer = offer_box([
        ["Your package", "Normal price", "Your price", "When you pay"],
        ["Complete website that sells to customers, with online shop and card payments",
         f"<strike>{eur(WEBSITE_NORMAL)}</strike>", f"<b>{eur(WEBSITE_PRICE)}</b> one-off",
         f"Once it is finished and live (week {LIVE_WEEKS})"],
        ["Google plan (SEO), our best plan", f"<strike>{eur(SEO_NORMAL)}/month</strike>",
         f"<b>{eur(SEO_PRICE)}/month</b>", "Monthly, from the month after launch"],
        ["Hosting and care: we keep the site online, safe and up to date", "",
         f"<b>{eur(CARE_PRICE)}/month</b>", "Monthly, from the month after launch"],
    ], [6.6 * cm, 2.9 * cm, 3.2 * cm, 4.3 * cm])
    compare = [
        ["Area", "aspgroup.ro (the supplier)", "Your website (sells to customers)"],
        ["Who it is for", "Presents the brands and recruits dealers", "Turns local buyers into your customers"],
        ["Models", "All models by type and brand, with photos and specs",
         "Search by budget, engine size, number of seats and use (fun, farm, forest, kids)"],
        ["Prices", "Prices in euro and lei", "Lei prices update by themselves every day"],
        ["Financing", "“Rate de la 40 €/lună” on each model",
         "Customers see their monthly payment and apply for financing online"],
        ["Customers", "Contact form and phone numbers",
         "Buttons to ask for a price, book a test ride, reserve with a card deposit, value a trade-in, call or WhatsApp"],
        ["Showrooms", "The supplier's 4 showrooms", "Your showrooms, with map, hours and Google reviews"],
        ["Online shop", "Parts sold on a separate site", "Your own shop for parts, helmets and clothing, paid by card"],
        ["Used vehicles", "—", "A page for used vehicles and trade-ins"],
    ]
    return [
        P("Summary", "h1"),
        P("aspgroup.ro is the supplier's website: it presents the brands and serves dealers. We will build you "
          "something different: a website that sells directly to customers (B2C), so people in your area find you "
          "on Google and call, book a test ride, ask for financing, reserve a vehicle or buy parts online by card.", "lead"),
        offer,
        Spacer(1, 0.2 * cm),
        P(f"Because you are a friend: everything included, no deposit, and you pay for the website only when it "
          f"is finished. You save {eur(WEBSITE_NORMAL - WEBSITE_PRICE)} on the website and "
          f"{eur(SEO_NORMAL - SEO_PRICE)} every month on Google. All prices in EUR, excluding VAT.", "small"),
        P("Supplier site vs. your customer site", "h2"),
        grid(compare, [2.9 * cm, 6.2 * cm, 7.9 * cm]),
        Spacer(1, 0.25 * cm),
        P("Important: we write your own texts instead of copying aspgroup.ro, because Google ignores copied "
          "pages. Photos come from ASP's dealer kit, with their OK.", "small"),
        PageBreak(),
    ]


def concept_story():
    from PIL import Image as PILImage
    w, h = PILImage.open(HERE / "sitemap.png").size
    img = Image(str(HERE / "sitemap.png"), width=CONTENT_W, height=CONTENT_W * h / w)
    return [
        P("Site concept", "h1"),
        P("Visitors arrive from Google, Google Maps, ads or dealer listings. Every page gives them six easy "
          "ways to buy or ask, and each request goes straight to the right showroom.", "lead"),
        img,
        PageBreak(),
    ]


def process_story():
    steps = [
        ["Step", "What we do", "What you see and approve", "When"],
        ["1. Kick-off call", "We learn your business: brands, showrooms, best sellers, typical customers",
         "You send us the items on the checklist", "Days 1–7"],
        ["2. Research and site map", "We study what Romanian buyers search for and what other dealers do, then plan "
         "every page and how a visitor becomes a customer", "The list of pages, for your OK", "Days 1–14"],
        ["3. Wireframes", "Simple black-and-white sketches of the main pages (home, models, model page, shop, "
         "checkout), on phone and computer, showing what goes where", "The sketches; you comment and approve",
         "Days 8–21"],
        ["4. Design in Figma", "The full-colour design with your logo, colours and real photos, plus a clickable "
         "prototype that works like the real site", "A link you open on your phone; 2 rounds of changes, then your OK",
         "Days 15–35"],
        ["5. Build", "We build the site on a private test address: models, prices, shop, card payments, couriers, "
         "invoices and the financing calculator", "The test link, plus a short update every week", "Days 29–70"],
        ["6. Content", "We write the texts and load all models and shop products",
         "You check prices and texts", "Days 36–70"],
        ["7. Testing", "We test every page, form and payment on phones and computers, including a real test order",
         "Your final check and OK", "Days 71–77"],
        ["8. Launch", "The site goes live on your address and we connect it to Google, Google Maps and visitor stats; "
         "3 hours of training for your team", f"Your live website. You pay the {eur(WEBSITE_PRICE)}",
         f"Day {LIVE_WEEKS * 7}"],
        ["9. Grow", "Every month: Google work, site care and a simple report", "The monthly report",
         "From the next month"],
    ]
    return [
        P("How we will build your website", "h1"),
        P("We agree on the plan, the sketches and the design before we build anything. Changing a sketch takes "
          "minutes; changing a finished website takes days. So there are no surprises and no wasted money.", "lead"),
        grid(steps, [3.0 * cm, 6.8 * cm, 5.0 * cm, 2.2 * cm]),
        Spacer(1, 0.3 * cm),
        P("<b>Figma</b> is the professional tool designers use. You do not need to install anything: you get a "
          "link, open it on your phone, and click through your future website as if it were live."),
        P(f"The {LIVE_WEEKS * 7} days start when we receive the items on the checklist (last page). If something "
          "arrives late, launch moves by the same time.", "small"),
        PageBreak(),
    ]


def website_story():
    rows = [
        ["Part", "What you get"],
        ["Design", "A design made for your brand, approved by you before we build"],
        ["Models", "Every model you sell, sorted by type and brand. Customers search by budget, engine size, seats "
                   "and use, and can compare up to 3 models side by side"],
        ["Prices", "Prices in euro and lei. The lei prices update by themselves every day"],
        ["Getting customers", "On every page: ask for a price, book a test ride, value a trade-in, apply for financing, "
                              "call or WhatsApp, plus a “call me back” button. Each request goes straight to the right showroom by email"],
        ["Financing", "A monthly payment calculator on every model. In the shop, customers can pay in instalments"],
        ["Reserve by card", "Customers reserve a vehicle in stock online with a card deposit you choose (e.g. €300), "
                            "then sign and pay the rest at your showroom: cash, card, transfer or financing"],
        ["Used vehicles", "A page for used vehicles and trade-ins"],
        ["Online shop", "Sell parts, accessories, helmets and clothing online. We set up to 2,000 products for you. "
                        "Card, cash on delivery or interest-free instalments; delivery by courier (Fan Courier, Sameday, Cargus) "
                        "or to easybox lockers; automatic invoices"],
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
          f"<b>{eur(WEBSITE_PRICE)}</b> instead of {eur(WEBSITE_NORMAL)}, paid when it is finished.", "lead"),
        grid(rows, [3.6 * cm, 13.4 * cm]),
        PageBreak(),
    ]


def sales_story():
    rows = [
        ["What we add", "Why it sells more"],
        ["Clear prices on every model, in euro and lei, plus “from €X/month”",
         "Buyers compare price and monthly payment first. If they cannot see them, they leave for a dealer who shows them"],
        ["“In stock, ready now” labels and a list of vehicles available immediately",
         "Buyers want to ride this season, not wait for an order"],
        ["Reserve online with a card deposit",
         "Catches buyers the moment they decide, before they visit another dealer"],
        ["Free test ride, booked in 2 clicks", "Many buyers decide only after riding the vehicle"],
        ["“Call me back” button with a fast-response promise (e.g. 15 minutes, during opening hours)",
         "Buyers often contact several dealers; the first one to answer has the best chance"],
        ["Call and WhatsApp buttons always visible on phones",
         "Most visitors browse on their phone, and many prefer to call or message rather than fill in a form"],
        ["“Which ATV is right for me?”: 3 quick questions (use, budget, passengers)",
         "Guides first-time buyers to the right model and turns them into a request"],
        ["Trust on every page: authorized dealer badges, warranty, your own service, Google reviews, real photos of your team",
         "People spend thousands only with a dealer they trust"],
        ["Trade-in valuation", "Many buyers need to sell their old vehicle first"],
        ["A page for farms and companies: leasing, invoice with VAT, work models",
         "ATVs and UTVs are work tools for farms, forestry and hunting groups"],
        ["A Rabla page for motorcycles",
         "The government program lowers the price of a new motorcycle; ASP already promotes Royal Enfield through Rabla 2026"],
        ["Shop options Romanians expect: cash on delivery, card, interest-free instalments, easybox lockers, "
         "free delivery above a set amount",
         "When their preferred payment or delivery option is missing, shoppers abandon the cart"],
        ["Accessory packs suggested with each vehicle (winch, plough, top case)", "Raises the value of every sale"],
        ["Automatic follow-ups: abandoned-cart reminders, a review request after each sale, seasonal offers by email",
         "Brings back people who did not buy the first time, and grows your Google reviews"],
        ["Ads tracking for Google and Facebook", "You can show ads again to people who visited but did not buy"],
    ]
    return [
        P("Built to sell", "h1"),
        P("Every feature below has one job: turn a visitor into a buyer. Each one is chosen for how people in "
          "Romania buy ATVs, UTVs and motorcycles, and all are included in your price.", "lead"),
        grid(rows, [7.6 * cm, 9.4 * cm]),
        PageBreak(),
    ]


def seo_story():
    competitors = [
        ["Who you compete with", "How they get customers from Google", "How you beat them"],
        ["aspgroup.ro (the supplier)", "Official pages for every model, plus paid Google ads",
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
        P("When someone in Romania wants an ATV or a motorcycle, they search on Google. The supplier and the "
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
          f"without paying for each click. Our best plan: <b>{eur(SEO_PRICE)}/month</b> instead of "
          f"{eur(SEO_NORMAL)}. It starts the month after launch, for at least 6 months, with no extra costs.", "lead"),
        grid(plan, [3.6 * cm, 13.4 * cm]),
        P("What to expect", "h2"),
        grid(expect, [2.7 * cm, 14.3 * cm], header=False),
        Spacer(1, 0.25 * cm),
        P("We measure success in customers who contact you, not just in Google positions. Nobody can honestly "
          "promise you #1 on Google; we promise the work above and a clear report every month."),
        PageBreak(),
    ]


def costs_story():
    costs = [
        ["Item", "Price (EUR, excl. VAT)", "Notes"],
        ["Hosting and care: we keep the site online, safe, backed up and up to date, plus 1 hour of small "
         "changes per month", f"{eur(CARE_PRICE)}/month", "Needed unless you have your own technical team"],
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
        f"No deposit: you pay the website ({eur(WEBSITE_PRICE)}) once it is finished and live.",
        "The Google plan and hosting are paid monthly, starting the month after launch. The Google plan runs at "
        "least 6 months.",
        f"This friend price is valid until {VALID_UNTIL}.",
        "Prices are in EUR, excluding VAT. You can also pay in lei at the National Bank (BNR) rate on the invoice date.",
        "You can ask for design changes twice. Anything extra costs €25/hour and is always agreed first.",
        "Once paid, the website, its design and its texts are 100% yours, and every account is in your company's name.",
        "We provide the legal pages (terms, privacy, cookies, returns) as templates; your lawyer should approve them.",
        "Brand logos and photos follow each brand's rules for dealers and need ASP's OK before launch.",
    ]
    return [
        P("Running costs and payment", "h1"),
        P(f"After launch the site costs {eur(CARE_PRICE)} a month plus the domain; the extras are optional.", "lead"),
        grid(costs, [7.4 * cm, 4.6 * cm, 5.0 * cm]),
        P("Payment terms", "h2"),
        *[P(f"•&nbsp;&nbsp;{t}") for t in terms],
        PageBreak(),
    ]


def acceptance_story():
    needs = [
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
    accepted = offer_box([
        ["What you accept", "Price"],
        [f"Complete website that sells to customers, with online shop, live in {LIVE_WEEKS} weeks, "
         "paid when finished", f"<b>{eur(WEBSITE_PRICE)}</b> one-off"],
        ["Google plan (SEO), our best plan, for at least 6 months", f"<b>{eur(SEO_PRICE)}/month</b>"],
        ["Hosting and care", f"<b>{eur(CARE_PRICE)}/month</b>"],
    ], [12.0 * cm, 5.0 * cm])

    def sign_block(title, company):
        rows = [[P(f"<b>{title}</b>", "cell")], [P(f"Company: {company}", "cell")], [P("Name:", "cell")],
                [P("Signature:", "cell")], [P("Date:", "cell")]]
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
                    sign_block("Agency", DETAILS["agency_name"])]], colWidths=[8.5 * cm, 8.5 * cm])
    signs.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return [
        P("What we need from you to start", "h1"),
        P("Send us these and we start the same week.", "lead"),
        *[P(f"{box}&nbsp;&nbsp;{n}") for n in needs],
        P("Acceptance", "h2"),
        accepted,
        Spacer(1, 0.3 * cm),
        P("By signing, both parties accept the scope, prices and terms in this proposal. "
          "All prices in EUR, excluding VAT.", "small"),
        Spacer(1, 0.4 * cm),
        KeepTogether(signs),
    ]


def build_proposal(path):
    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=2 * cm, bottomMargin=2 * cm,
                          title="Your new website and Google plan", author=DETAILS["agency_name"] or "Proposal",
                          subject=f"Proposal {PROPOSAL_NO}")
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
    build_proposal(HERE / f"Proposal-{PROPOSAL_NO}-Website-SEO.pdf")
    print("PDF written to", HERE)
