"""Build the client proposal and the deposit proforma invoice as print-ready A4 PDFs.

Fill in DETAILS below (empty values print as yellow placeholders), then run:
    python3 build_pdfs.py
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
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
WEBSITE_PACKAGE = ("Professional", 3500)
DEPOSIT_SHARE = 0.40

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


def eur(amount):
    return f"€{amount:,.2f}"


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
        Paragraph("Concept, development and search engine optimisation for a reseller "
                  "of the ASP Group range: Polaris, Segway Powersports, TGB, Linhai, "
                  "Indian Motorcycle, Royal Enfield and more.", sub),
        Spacer(1, 6.3 * cm),
        meta_t,
        NextPageTemplate("inner"),
        PageBreak(),
    ]


def summary_story():
    rec = [
        ["", "What", "Price", "When"],
        ["Website", "Professional package", "€3,500 one-off", "Live in 9 weeks"],
        ["SEO", "Growth plan", "€550 / month", "From the month after launch"],
        ["Care", "Hosting, updates, backups, security", "€60 / month", "From launch"],
    ]
    rec_t = grid(rec, [2.4 * cm, 6.4 * cm, 3.6 * cm, 4.6 * cm], zebra=False,
                 extra=[("BACKGROUND", (0, 1), (-1, -1), ACCENT_TINT),
                        ("BOX", (0, 0), (-1, -1), 1, ACCENT)])
    compare = [
        ["Area", "Keep from aspgroup.ro", "Add for you as a reseller"],
        ["Catalogue", "Models grouped by type (ATV, UTV, moto, XTV) and brand, one page per model with specs and gallery",
         "Filters by budget, engine size, seats, road registration and use (leisure, farm, forestry, kids)"],
        ["Prices", "EUR price with a RON equivalent (ASP uses a Banca Transilvania rate, 5.29 RON/EUR on 1 May 2026)",
         "RON recalculated automatically every day, so prices never go stale"],
        ["Financing", "“Rate de la 40 €/lună” on model pages, through BT Direct",
         "Payment calculator on every model and an online financing request sent straight to your partner"],
        ["Promotions", "A promotions page with old and new prices",
         "Promo landing pages built for Google Ads and Meta campaigns, with stock badges"],
        ["Leads", "Contact forms, phone and showroom addresses",
         "Request an offer, book a test ride, trade-in valuation, WhatsApp and click-to-call, all tracked in GA4"],
        ["Local presence", "4 own showrooms (Bucharest, Cluj, Timișoara, Sibiu)",
         "A page per showroom or service area with map, hours, Google reviews and dealer schema"],
        ["Content", "News posts, such as Royal Enfield through Rabla 2026",
         "Buying guides and comparisons written for Romanian searches"],
        ["Parts and gear", "A separate shop, aspshop.ro", "Optional built-in shop for parts, helmets and apparel (Premium)"],
        ["Used vehicles", "—", "A section for trade-ins and used units, a steady lead source for dealers"],
    ]
    return [
        P("Summary", "h1"),
        P("We recommend the Professional website plus the Growth SEO plan: a dealer site with the "
          "full ASP Group catalogue, built to win local Google searches and turn visitors into calls, "
          "test rides and financing requests.", "lead"),
        rec_t,
        Spacer(1, 0.2 * cm),
        P("All prices in EUR, excluding VAT.", "small"),
        P("The reference site, and what we add", "h2"),
        P("aspgroup.ro is a strong importer catalogue. Your site keeps its structure and adds what a "
          "reseller needs: local reach, lead capture and original content."),
        grid(compare, [2.9 * cm, 6.9 * cm, 7.2 * cm]),
        Spacer(1, 0.25 * cm),
        P("One rule: we write original text and do not copy from aspgroup.ro. Google ranks the original "
          "page, not the copy. Photos come from the importer's dealer marketing kit, with ASP's written OK.", "small"),
        PageBreak(),
    ]


def concept_story():
    img_w = CONTENT_W
    img = Image(str(HERE / "sitemap.png"), width=img_w, height=img_w * 1286 / 1344)
    return [
        P("Site concept", "h1"),
        P("Visitors land on any page from search, maps, ads or dealer listings. Every page keeps the five "
          "lead actions one tap away, and each lead is sent to the right showroom.", "lead"),
        img,
        PageBreak(),
    ]


def packages_story():
    rows = [
        ["", "Start", "Professional (recommended)", "Premium"],
        ["Price", "<b>€1,900</b>", "<b>€3,500</b>", "<b>€5,500</b>"],
        ["Live in", "5 weeks", "9 weeks", "12 weeks"],
        ["Design", "Premium theme adapted to your brand", "Custom UX/UI design in Figma, 2 revision rounds", "Same as Professional"],
        ["Catalogue", "Up to 60 models by brand and type, loaded by us", "Unlimited models, smart filters, compare up to 3 models", "Same as Professional"],
        ["Prices", "EUR + RON, updated daily", "Same", "Same"],
        ["Leads", "Request-an-offer form, call and WhatsApp buttons",
         "Adds test-ride booking, trade-in valuation, financing request and routing of each lead to the right showroom", "Same as Professional"],
        ["Financing", "—", "Monthly payment calculator on every model", "Adds instalments at checkout (e.g. TBI Bank, Mokka)"],
        ["Used vehicles", "—", "Used and trade-in section", "Same"],
        ["Online shop", "—", "—",
         "Parts, accessories, helmets and apparel: up to 2,000 products imported, card payments (Netopia or Stripe), "
         "couriers (Fan Courier, Sameday, Cargus), SmartBill or Oblio invoicing with e-Factura, Google Shopping and Meta feeds"],
        ["Languages", "Romanian", "Romanian + English", "Romanian + English"],
        ["SEO foundation", "Clean URLs, meta tags, XML sitemap, speed basics",
         "Adds schema markup (product, offer, dealer), Core Web Vitals in the green, redirect plan", "Adds product schema for the shop"],
        ["Tracking", "GA4 + Search Console", "Adds Google Tag Manager, Google Ads and Meta conversions, Consent Mode v2", "Same"],
        ["Compliance", "GDPR cookie banner, legal page templates, ANPC SAL/SOL badges", "Adds accessibility to WCAG 2.1 AA",
         "Adds ANPC-compliant checkout and returns pages"],
        ["After launch", "30 days of fixes, 1 h training", "60 days of fixes, 2 h training", "90 days of fixes, 3 h training"],
    ]
    highlight = [("BACKGROUND", (2, 1), (2, -1), ACCENT_TINT),
                 ("BACKGROUND", (2, 0), (2, 0), ACCENT),
                 ("LINEBEFORE", (2, 0), (2, -1), 1, ACCENT),
                 ("LINEAFTER", (2, 0), (2, -1), 1, ACCENT)]
    return [
        P("Website packages", "h1"),
        P("Professional fits a multi-brand dealer: the full catalogue and every lead tool, without an online "
          "shop. Choose Premium if you also want to sell parts and gear online.", "lead"),
        grid(rows, [2.7 * cm, 4.3 * cm, 5.0 * cm, 5.0 * cm], zebra=False, extra=highlight),
        Spacer(1, 0.25 * cm),
        P("Every package is built on WordPress, mobile-first, with SSL and a pre-launch checklist. "
          "You own the site, the code and the content. One-off prices in EUR, excluding VAT.", "small"),
        PageBreak(),
    ]


def seo_story():
    competitors = [
        ["Competitor", "How they win on Google", "Your answer"],
        ["aspgroup.ro (importer)", "Official model pages and prices, plus paid Google Ads",
         "Original model content; ask ASP to list and link your site on its dealer pages"],
        ["ATVRom network", "A separate site per city (atvrom-bucuresti.ro, atvrom-brasov.ro, atvrom-iasi.ro, "
         "atvrom-timisoara.ro and more), selling Linhai, TGB, Segway, CFMOTO and Can-Am",
         "Fewer, stronger local pages backed by a Google Business Profile and real reviews"],
        ["motoclass.ro, atv-mag.ro, atv-vanzari.ro", "Multi-brand dealer shops with category pages",
         "Better filters, financing tools and buying guides"],
        ["polarisofficial.ro", "Official Polaris site with a dealer list",
         "A listing in its dealer locator: a free, highly relevant backlink"],
        ["OLX", "ASP and other dealers list stock there", "A lead channel to run alongside SEO, not a ranking rival"],
    ]
    keywords = [
        ["Cluster", "Example searches (Romanian)", "Page that ranks", "Competition"],
        ["Model and price", "linhai 370 promax pret, segway at5 l eps pret, royal enfield hunter 350 pret, tgb blade 1000 pareri",
         "Model pages with original reviews and specs", "Low"],
        ["Use cases", "atv pentru agricultura, utv pentru ferma, atv pentru vanatoare, atv copii", "Landing pages and articles", "Low"],
        ["Comparisons", "linhai vs cfmoto, segway vs polaris, atv vs utv", "Articles", "Low"],
        ["Local", "dealer atv [oraș], atv [oraș], service atv [oraș], royal enfield [oraș]",
         "Showroom pages and Google Business Profile", "Low to medium"],
        ["Buying guides", "atv inmatriculare, ce permis trebuie pentru atv, atv in rate, motocicleta prin rabla", "Articles", "Low to medium"],
        ["Parts and gear", "piese linhai, accesorii atv, casca atv (Premium only)", "Shop categories", "Medium"],
        ["Category", "atv de vanzare, utv de vanzare, motociclete noi", "Category pages", "High: 6 to 12 months"],
    ]
    plans = [
        ["", "Local", "Growth (recommended)", "Authority"],
        ["Price per month", "<b>€300</b>", "<b>€550</b>", "<b>€900</b>"],
        ["Google Business Profile", "Optimisation for each showroom, weekly posts, review plan", "Same", "Same"],
        ["Romanian directory listings", "15 at start", "25 at start", "35 at start"],
        ["Pages optimised", "5 per month", "10 per month", "20 per month"],
        ["Original model descriptions", "—", "6 per month", "12 per month"],
        ["Articles in Romanian (1,000+ words)", "1 per month", "3 per month", "5 per month"],
        ["Quality Romanian backlinks", "—", "2 per month from moto, auto, agri and news sites",
         "4 per month, plus 1 press release per quarter"],
        ["Technical monitoring", "Monthly", "Weekly", "Weekly"],
        ["Reporting", "Monthly report", "Live dashboard of leads by channel, monthly call", "Adds a quarterly strategy workshop"],
        ["Extras", "—", "City landing pages",
         "YouTube SEO for walkaround videos, Google Shopping feed (with Premium site), 1 conversion test per month"],
    ]
    highlight = [("BACKGROUND", (2, 1), (2, -1), ACCENT_TINT),
                 ("BACKGROUND", (2, 0), (2, 0), ACCENT),
                 ("LINEBEFORE", (2, 0), (2, -1), 1, ACCENT),
                 ("LINEAFTER", (2, 0), (2, -1), 1, ACCENT)]
    expect = [
        ["Months 1–3", "Your showrooms appear in Google's local map results, and the first model pages reach page 1 or 2."],
        ["Months 4–6", "Model, comparison and guide pages bring steady organic leads; local searches sit on page 1."],
        ["Months 7–12", "We push for category terms such as “atv de vanzare” against ATVRom and the importer."],
    ]
    return [
        P("SEO opportunity in Romania", "h1"),
        P("Your opening is local and long-tail search. The importer and the ATVRom dealer network own the broad "
          "terms, but model-level questions and your own city are still winnable.", "lead"),
        grid(competitors, [3.6 * cm, 6.9 * cm, 6.5 * cm]),
        P("Keyword clusters we will target", "h2"),
        P("Search volumes are confirmed in the kickoff keyword study; competition is our estimate.", "small"),
        Spacer(1, 0.1 * cm),
        grid(keywords, [2.7 * cm, 7.0 * cm, 4.4 * cm, 2.9 * cm]),
        PageBreak(),
        P("SEO plans", "h1"),
        P("We recommend Growth: enough content and links to lead local searches within about 3 months and model "
          "searches within about 6. Plans start the month after launch; the technical SEO foundation is already "
          "in every website package.", "lead"),
        grid(plans, [4.0 * cm, 4.0 * cm, 4.5 * cm, 4.5 * cm], zebra=False, extra=highlight),
        Spacer(1, 0.25 * cm),
        P("Link and content costs are included, with no extra bills. Minimum term 6 months; a 12-month contract "
          "gets 10% off. Monthly prices in EUR, excluding VAT.", "small"),
        P("What to expect on Growth", "h2"),
        grid(expect, [2.7 * cm, 14.3 * cm], header=False),
        Spacer(1, 0.25 * cm),
        P("We judge success by leads (forms, calls, WhatsApp and financing requests) and track 50 keywords monthly. "
          "No one can honestly guarantee a #1 position on Google; we commit to the work and the reporting above."),
        PageBreak(),
    ]


def costs_story():
    costs = [
        ["Item", "Price (EUR, excl. VAT)", "Notes"],
        ["Care plan: EU hosting, plugin licences, updates, daily backups, security, uptime monitoring, 1 h of changes per month",
         "€60/month (€90/month with the Premium shop)", "Needed unless you host and maintain the site yourselves"],
        [".ro domain", "About €10/year", "Registered in your company's name"],
        ["Card payment fees (Premium only)", "Per transaction", "Paid to the processor, e.g. Netopia or Stripe"],
        ["Original model descriptions at launch", "€15 per model", "Growth and Authority SEO plans cover this over time"],
        ["Extra language", "€500 one-off", "Translation and setup of one more language"],
        ["Logo and visual identity", "€350 one-off", "Only if you do not have one yet"],
        ["Showroom photo and video shoot", "Quoted on request", "Walkaround videos also feed YouTube SEO"],
        ["Google Ads and Meta Ads management", "From €250/month plus ad budget", "The promo landing pages are already built for it"],
        ["Work beyond the plan", "€25/hour", "Quoted before we start"],
    ]
    terms = [
        "The website is paid 40% on signing, 30% when you approve the design and 30% at launch.",
        f"This proposal is valid until {VALID_UNTIL}.",
        "Prices are in EUR, excluding VAT. We can invoice in RON at the BNR rate on the invoice date.",
        "SEO and Care plans are billed monthly in advance, starting the month after launch.",
        "Two design revision rounds are included. Extra rounds or new features cost €25/hour and are always quoted first.",
        "The timeline starts when we receive the items on the checklist. A late item moves launch by the same number of days.",
        "The site, code, design files and content become yours on final payment. Domain, hosting and Google accounts "
        "are opened in your company's name.",
        "Legal pages (terms, privacy, cookies, returns) come as templates for your lawyer to approve.",
        "Brand logos and photos follow each manufacturer's dealer guidelines and need ASP's approval before launch.",
    ]
    return [
        P("Running costs and add-ons", "h1"),
        P("A live site costs €60 a month plus the domain; everything else here is optional.", "lead"),
        grid(costs, [7.4 * cm, 4.6 * cm, 5.0 * cm]),
        P("Payment terms and conditions", "h2"),
        *[P(f"•&nbsp;&nbsp;{t}") for t in terms],
        PageBreak(),
    ]


def process_story():
    steps = [
        ["Step", "What happens", "Who", "When", "Payment"],
        ["1. Accept", "You pick the package and plan, and sign the acceptance page", "You", "Week 0", "—"],
        ["2. Deposit", "We send a proforma invoice for the deposit", "Both", "Week 0", "40%"],
        ["3. Kickoff", "Keyword study, site map and content plan; you send the checklist items", "Both", "Weeks 1–2", "—"],
        ["4. Design", "Design in 2 revision rounds, then your approval", "Us, then you", "Weeks 2–4", "30%"],
        ["5. Build", "Development, catalogue loading, integrations and tracking", "Us", "Weeks 4–8", "—"],
        ["6. Test", "Phones, browsers and forms checked; your final review", "Both", "Week 8", "—"],
        ["7. Launch", "Site goes live; Search Console and Google Business Profile set up", "Us", "Week 9", "30%"],
        ["8. Grow", "Monthly SEO and care, with a monthly report", "Us", "From month 2", "Monthly"],
    ]
    needs = [
        "Your choice of website package and SEO plan",
        "The signed acceptance page and the deposit payment",
        "Company details: legal name, CUI, Trade Register number and registered address",
        "Your domain name, or approval to register one",
        "Logo and brand colours, or the identity add-on",
        "The brands and models you sell, and your dealer agreement with ASP Group East",
        "ASP's dealer marketing kit: photos, logos, spec sheets and price list",
        "For each showroom: address, hours, phone, WhatsApp number and the email that receives leads",
        "Your financing partner and its terms (bank, leasing or buy-now-pay-later)",
        "Access to any existing Google Business Profile, Google Ads, Search Console and Facebook accounts",
        "Premium only: Netopia or Stripe, courier and SmartBill or Oblio accounts",
    ]
    box = "<font face='Body' color='#2F6FDE'>□</font>"
    return [
        P("How we work, step by step", "h1"),
        P("Eight steps from signature to a site that brings in leads. The Professional site is live in week 9.", "lead"),
        grid(steps, [2.3 * cm, 8.0 * cm, 2.3 * cm, 2.4 * cm, 2.0 * cm]),
        P("What we need from you to start", "h2"),
        *[P(f"{box}&nbsp;&nbsp;{n}") for n in needs],
        PageBreak(),
    ]


def acceptance_story():
    box = "<font color='#2F6FDE' size='13'>□</font>"
    choices = [
        ["Website package", f"{box} Start, €1,900", f"{box} Professional, €3,500", f"{box} Premium, €5,500"],
        ["SEO plan", f"{box} Local, €300/month", f"{box} Growth, €550/month", f"{box} Authority, €900/month"],
        ["", f"{box} No SEO for now", "", ""],
        ["Care plan", f"{box} Yes, €60/month (€90 with Premium)", f"{box} We host it ourselves", ""],
        ["SEO term", f"{box} 6 months", f"{box} 12 months (10% off)", ""],
    ]
    choice_t = grid(choices, [3.2 * cm, 4.8 * cm, 4.6 * cm, 4.4 * cm], header=False, zebra=False)

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
        P(f"Tick your choices and sign to accept proposal {PROPOSAL_NO}. We then send the deposit proforma "
          "invoice and book the kickoff.", "lead"),
        choice_t,
        Spacer(1, 0.5 * cm),
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
    story = (cover_story() + summary_story() + concept_story() + packages_story() + seo_story()
             + costs_story() + process_story() + acceptance_story())
    doc.build(story)


# ================================================================ proforma
def build_proforma(path):
    package, total = WEBSITE_PACKAGE
    deposit = round(total * DEPOSIT_SHARE, 2)
    design_part = round(total * 0.30, 2)
    launch_part = round(total - deposit - design_part, 2)
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

    desc = (f"<b>Website development, {package} package: 40% advance payment</b><br/>"
            f"<font color='#5B6475'>Avans 40% pentru dezvoltare website, pachet {package}. "
            f"Total contract value {eur(total)}, per proposal {PROPOSAL_NO}.</font>")
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

    schedule = grid([
        ["Payment schedule / Calendar de plată", "Share", "Amount"],
        ["Advance at signing: <b>this proforma</b>", "40%", eur(deposit)],
        ["On design approval", "30%", eur(design_part)],
        ["At launch", "30%", eur(launch_part)],
        ["<b>Total website, excluding VAT</b>", "100%", f"<b>{eur(total)}</b>"],
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
        line_t, Spacer(1, 0.3 * cm), totals, Spacer(1, 0.7 * cm), schedule, Spacer(1, 0.6 * cm),
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
