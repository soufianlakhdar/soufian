# Master Build Prompt — All-in-One Customer Messaging Platform (Crisp-class)

## How to use this prompt (for you, the founder)

1. Optional: change the values in **Variables** below (brand name, domain, color).
2. Copy **everything from "PROMPT START" to "PROMPT END"** and paste it into your AI builder (Claude Code, Cursor, Windsurf, Lovable, Bolt, Replit Agent, v0, …).
3. The AI builds the product **one phase at a time**. When it finishes a phase and shows you the report, reply: **"Continue with the next phase."**
4. If it ever stops early, reply: **"Re-read PROMPT.md section 14 (Definition of Done) and finish the current phase completely."**
5. The prompt is long on purpose. If your tool has a small memory (Lovable, Bolt, v0…), first save it in the project as `PROMPT.md`, then tell the AI: **"Read PROMPT.md fully and start with section 15."**
6. Prices, limits and competitor facts come from public research in October 2026. Check them before you launch; all prices live in one file (`plans.ts`) and are easy to change.

---

# ===================== PROMPT START =====================

## 0. Variables (use these everywhere)

| Variable | Value |
|---|---|
| BRAND_NAME | **Parlo** |
| BRAND_SLUG (lowercase, code identifiers) | **parlo** |
| DOMAIN | **yourdomain.com** |
| PRIMARY_COLOR | **#5A4BFF** (electric violet) |
| DARK_TEXT_COLOR | **#0F1530** |
| DEFAULT_LANGUAGE | **English (en)** |

Where this prompt writes `Parlo`, `parlo`, `$parlo`, `PARLO_` or `yourdomain.com`, use the values above. Keep the brand name in **one config file** so it can be renamed in a single place.

---

## 1. Your role and mission

You are a **senior full-stack engineer, product designer and tech lead**. You will build, from scratch, a **production-quality SaaS startup** called **Parlo**: an all-in-one customer messaging platform that businesses use to talk with their website visitors and customers.

The reference product is **Crisp (https://crisp.chat)**. Parlo must match Crisp's full feature set, then **beat it** (see section 13). It is a direct competitor, not a copy.

What Parlo is, in one sentence:
> A business pastes one line of code (or installs our WordPress plugin or Shopify app). A chat bubble then appears on their website, and their whole team answers every customer conversation from live chat, WhatsApp, email, Messenger, Instagram, Telegram and more, in **one shared inbox**, with a CRM, a knowledge base, AI answers, chatbots and campaigns built in.

Target customers: startups, SaaS companies, e-commerce stores (Shopify / WooCommerce), agencies and small businesses. They want a cheaper, simpler and faster alternative to Intercom, Zendesk and Crisp.

---

## 2. Non-negotiable rules (read twice)

1. **Original brand, no copying.** Copy Crisp's *feature set and information architecture* only. **Never** copy Crisp's text, logos, images, illustrations, icons, CSS or exact layouts, and never use the word "Crisp" in the product UI. The only exceptions are factual, dated `/compare/*` pages and an "Import from …" tool. Write all copy yourself. Use no third-party brand logos: integration icons are colored tiles with initials, or simple generic SVG glyphs.
2. **Work in phases** (section 12). Finish one phase completely before starting the next. Never jump ahead.
3. **No fake features.** Every button, page and setting you build must really work end to end, with a database, an API, the UI and tests. No "TODO", no lorem ipsum, no mocked UI that does nothing. If a feature belongs to a later phase, do not show it yet, or show it clearly labeled "Coming soon".
4. **External services you cannot reach** (Meta/WhatsApp, Shopify, Stripe, Slack, email provider, LLM API): implement the integration fully and drive it with environment variables. Also write test fixtures/mocks so all tests pass without real credentials. Document exactly how to get each credential in `docs/SETUP_<SERVICE>.md`.
5. **Do not stop to ask me questions.** Make a sensible, industry-standard decision, record it in `docs/DECISIONS.md` (one line: decision + why), and continue. Ask only if you are truly blocked (for example, you need a paid account).
6. **Verify everything yourself.** After each phase run lint, typecheck, unit tests, integration tests and end-to-end tests. Start the app, click through the flows in a real browser (Playwright), fix every error, and only then report.
7. **Security by default** (section 10). Never trust input, escape all user content, verify every webhook signature, and encrypt integration secrets at rest.
8. **Keep docs current.** Keep `README.md` (setup and run), `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `CHANGELOG.md` and `.env.example` up to date after every phase.
9. **Commit often**, with clear messages. One logical change per commit.
10. **Quality bar:** it should feel like a funded startup built it. Fast, polished, responsive, accessible, consistent design, helpful empty states, helpful error messages, loading skeletons, keyboard shortcuts.

---

## 3. Tech stack (use exactly this unless impossible; log any change in DECISIONS.md)

| Layer | Choice |
|---|---|
| Language | **TypeScript** everywhere (strict mode); PHP only for the WordPress plugin |
| Monorepo | **pnpm workspaces + Turborepo** |
| Web app (marketing site + dashboard + help center) | **Next.js (latest stable, App Router)**, React, **Tailwind CSS**, **shadcn/ui**, lucide icons |
| API + realtime | **Node.js + Fastify** (REST) and **Socket.IO** (realtime) in the same service, with the Socket.IO **Redis adapter** for horizontal scaling |
| Background jobs | **BullMQ** on Redis (emails, webhooks, campaigns, AI, integration syncs, retries) |
| Database | **PostgreSQL 16+** + **Prisma** ORM + **pgvector** (AI embeddings) + Postgres full-text search |
| Cache / pub-sub / rate limits | **Redis** |
| File storage | **S3-compatible** (MinIO locally, S3/R2 in prod), signed upload URLs |
| Email | Provider-agnostic mailer (SMTP + Postmark/Resend/SES adapters), **React Email** templates; **Mailpit** locally |
| Chat widget | **TypeScript + Preact**, built with Vite in library mode into a single file **`l.js`**, under **35 KB gzipped**, rendered inside **Shadow DOM** so the host site's CSS can never break it |
| Validation | **zod** schemas shared between API, web and widget |
| Payments | **Stripe** (Checkout, Customer Portal, webhooks, Stripe Tax) |
| AI | Provider-agnostic LLM layer. Default **Anthropic Claude API** (latest Sonnet-class model for quality, latest Haiku-class model for cheap/fast tasks), with an OpenAI-compatible adapter. Model names come from env vars |
| Realtime calls (later phase) | **WebRTC** via LiveKit (self-hostable) |
| Testing | **Vitest** (unit/integration), **Playwright** (end-to-end, including the widget on a fake customer site), **Supertest** for API |
| Observability | Structured logs (pino), **Sentry**, OpenTelemetry traces, `/health` and `/ready` endpoints |
| Local dev | **docker-compose**: postgres (with pgvector), redis, minio, mailpit |
| CI | **GitHub Actions**: install → lint → typecheck → test → build → e2e |
| Deploy | Dockerfiles for every app; document deploys to Fly.io/Render/Railway **and** AWS. Serve the widget from a CDN with versioned files |

### Repository layout

```
/apps
  /web         Next.js: marketing site, dashboard (/app), help centers (/help), docs (/docs)
  /api         Fastify REST API + Socket.IO realtime + webhooks receivers
  /worker      BullMQ workers (email, webhooks, campaigns, AI, syncs)
  /widget      Embeddable chat widget → dist/l.js
/packages
  /db          Prisma schema, migrations, client, seed script
  /shared      zod schemas, TypeScript types, realtime event names, constants, integrations catalog data
  /ui          Shared design-system components
  /emails      React Email templates
  /llm         LLM provider abstraction + prompts
/integrations
  /wordpress   WordPress plugin "Parlo Live Chat" (PHP), packaged as a zip
  /shopify     Shopify app (Shopify CLI project with a theme app extension)
/docs          ARCHITECTURE.md, DECISIONS.md, SETUP_*.md, API reference (OpenAPI)
docker-compose.yml, .env.example, README.md, CHANGELOG.md
```

**URLs:** marketing site `yourdomain.com`; dashboard `app.yourdomain.com` (or `/app`); API `api.yourdomain.com`; widget `client.yourdomain.com/l.js`; help centers `help.yourdomain.com/{workspace}` plus optional custom domains. The dashboard calls the API same-site (proxy `/api/*` through Next.js rewrites) so session cookies stay first-party.

---

## 4. Design system and brand

- **Style:** modern, friendly and trustworthy SaaS. Lots of white space, rounded corners (12–16px), soft shadows, crisp typography (Inter or the system font stack), subtle motion (150–250ms).
- **Colors:** primary #5A4BFF; dark text #0F1530; neutral grays; success green, warning amber, danger red. Define everything as CSS variables / Tailwind tokens. The dashboard supports **light and dark mode** (follow the system setting, with a toggle).
- **Logo:** design an original, simple logo mark (a rounded speech bubble plus the wordmark) as SVG, with a favicon.
- **Tone of copy:** clear, warm, confident, no jargon. Short sentences.
- **Accessibility:** WCAG 2.1 AA: contrast, visible focus rings, keyboard navigation everywhere, aria labels, `aria-live` for new messages, reduced-motion support.
- **Responsive:** everything works from 360px phones to 4K. The operator dashboard is usable on a phone and installable as a **PWA**.
- **Internationalization:** all UI strings in translation files (start with en, fr, es, de, pt, ar). Arabic must render **RTL** correctly. The widget auto-detects the visitor's language.

---

## 5. Core concepts and data model

**Concepts:**
- **Workspace** (= one website or brand; Crisp calls this a "website"). A user can belong to many workspaces. Each workspace has a public **Website ID** used in the widget snippet.
- **Brand** = a website/brand *inside* a workspace. Each has its own widget settings, help center, email address, logo and reports, so agencies and multi-brand companies don't pay per brand the way Crisp customers do. Every workspace starts with one brand; the Website ID belongs to the brand.
- **Region** = where the workspace's data lives (**EU** or **US**), chosen at signup.
- **Operator** = a team member (user) inside a workspace. Roles: **Owner**, **Admin**, **Agent**.
- **Contact** = an end customer. They start as an anonymous visitor and become identified when we learn an email, phone or WhatsApp number. Contacts are merged when the same person is recognized again.
- **Conversation** = a thread between a contact and the team on one **channel** (chat, email, whatsapp, messenger, instagram, telegram, sms). Status: **open**, **snoozed**, or **resolved**.
- **Message** = an item in a conversation. Sender: visitor | operator | bot | system. Type: text, file, note (private, operators only), event (e.g. "Sam assigned to Lea"), rating, card (buttons/carousel from bots).

**Prisma models** (add fields as needed; every table has `id` (cuid/uuid), `createdAt`, `updatedAt`; every workspace-owned table has `workspaceId` with an index; all queries are scoped by workspace):

```
User(email unique, name, avatarUrl, passwordHash, emailVerifiedAt, twoFactorSecret?, locale, timezone)
Session(userId, tokenHash, userAgent, ip, expiresAt)
Workspace(name, domain, logoUrl, websiteId (public, unique), settings JSON, identitySecret, plan, timezone)
Membership(workspaceId, userId, role: OWNER|ADMIN|AGENT, availability: ONLINE|AWAY, notificationPrefs JSON)
Invite(workspaceId, email, role, tokenHash, invitedById, expiresAt)
Team(workspaceId, name) + TeamMember(teamId, userId)          // e.g. "Sales", "Support"
Contact(workspaceId, email?, name?, phone?, avatarUrl?, whatsappId?, messengerId?, instagramId?, telegramId?,
        visitorTokenHash?, companyId?, country?, city?, locale?, timezone?, userAgent?, customData JSON,
        segments String[], firstSeenAt, lastSeenAt, isBlocked)
Company(workspaceId, name, domain, customData JSON)
PageView(contactId, url, title, referrer, at)
ContactEvent(contactId, name, data JSON, at)                   // custom events via SDK/API
ContactNote(contactId, authorId, body)
Segment(workspaceId, name, rules JSON)                          // dynamic filters
Conversation(workspaceId, contactId, channel, status, assigneeId?, teamId?, priority, subject?, tags String[],
             snoozedUntil?, unreadByOperator Int, unreadByVisitor Int, lastMessageAt, lastMessagePreview,
             firstResponseAt?, resolvedAt?, rating? (1-5), ratingComment?, language?, externalThreadId?)
Message(conversationId, workspaceId, sender, authorId?, type, content, attachments JSON, metadata JSON,
        externalId? (unique per workspace, for dedupe), deliveryStatus (pending|sent|delivered|read|failed),
        translatedContent JSON?, editedAt?, deletedAt?)
SavedReply(workspaceId, shortcut, title, content, teamId?)
Tag(workspaceId, name, color)
OfficeHours(workspaceId, timezone, schedule JSON)
RoutingRule(workspaceId, conditions JSON, action JSON, order)
Article(workspaceId, categoryId, locale, title, slug, contentJson, contentText, status DRAFT|PUBLISHED, views, helpfulYes, helpfulNo)
ArticleCategory(workspaceId, name, slug, icon, order)
HelpCenter(workspaceId, customDomain?, theme JSON, enabled)
Bot(workspaceId, name, trigger JSON, flow JSON, enabled)       // visual chatbot flows
AiSettings(workspaceId, agentEnabled, tone, handoffRules JSON, monthlyCreditLimit)
AiSource(workspaceId, type URL|PDF|ARTICLE|TEXT, ref, status) + AiChunk(sourceId, content, embedding vector)
Campaign(workspaceId, name, type EMAIL|CHAT, segmentId, trigger JSON?, subject, contentJson, status, scheduledAt, stats JSON)
CampaignRecipient(campaignId, contactId, status, openedAt, clickedAt)
IntegrationCatalogItem(slug, name, tagline, category, status, installType, popularity, addedAt, color, description, features[], setupSteps[], docsUrl)
Integration(workspaceId, kind, enabled, configEncrypted, lastError?, lastSyncAt?)  // installed integrations
ApiKey(workspaceId, name, prefix, keyHash, scopes[], lastUsedAt)
WebhookEndpoint(workspaceId, url, secret, events[], enabled) + WebhookDelivery(endpointId, event, payload, status, attempts, responseCode, nextRetryAt)
Subscription(workspaceId, stripeCustomerId, stripeSubscriptionId, plan, status, seats, currentPeriodEnd, trialEndsAt)
Notification(userId, type, data JSON, readAt)
AuditLog(workspaceId?, actorId?, action, target, metadata JSON, ip)
Brand(workspaceId, name, domain, websiteId (public), widgetSettings JSON, helpCenterId?, emailAddress?, logoUrl)
Ticket fields on Conversation: type (chat|ticket), ticketTypeId?, slaPolicyId?, slaDueAt?, slaBreachedAt?, parentId? (split/merge), linkedIds[]
TicketType(workspaceId, name, fields JSON) + SlaPolicy(workspaceId, name, conditions JSON, firstResponseMins, nextResponseMins, resolutionMins, businessHoursId)
SideConversation(conversationId, channel, to, subject) + its own messages
AiAction(workspaceId, name, description, inputSchema JSON, http JSON | builtin, requiresApproval, approvalThreshold JSON, enabled)
AiActionRun(actionId, conversationId, input, output, status, approvedById?)
AiSimulation(workspaceId, questions JSON, results JSON, score, createdAt)
QaScore(conversationId, scores JSON, predictedCsat, reviewerId?)
Topic(workspaceId, label, language, conversationCount, trend) + ConversationTopic(conversationId, topicId)
UsageMeter(workspaceId, metric, periodStart, used, included, capped)
Referral(referrerWorkspaceId, referredWorkspaceId, status, rewardGrantedAt) + Partner(userId, commissionRate, payoutDetails)
PhoneNumber(workspaceId, provider, number, capabilities) + Call(conversationId, direction, durationSec, recordingUrl, transcript)
TrustSafetyCase(workspaceId, reason, signals JSON, status, reviewedById, decision, appealText)
StatusPage + Monitor + Incident (phase 5)
```

**Rules:** integration secrets (tokens, app secrets) are encrypted with **AES-256-GCM** using a key from env. Visitor tokens, session tokens, API keys and invite tokens are stored **hashed (SHA-256)**. Passwords use **argon2id**.

---

## 6. Product modules: full specification

### 6.1 Marketing website (public, SEO-optimized, server-rendered)

Shared header: logo, nav (Product ▾ [Chat widget, Shared inbox, Multichannel, CRM, Knowledge base, AI & chatbots, Campaigns], Integrations, Pricing, Docs), "Log in", and a primary button "Start free". Mobile hamburger menu. Footer with Product, Integrations (top 6), Resources, Company and Legal columns, a language switcher, and © year.

Pages:
1. **Home `/`:** a hero with a strong headline in your own words (e.g. "Every customer conversation. One inbox."), a subheadline, CTAs "Start free — no credit card" and "See it live", and an **animated product mockup built in HTML/CSS** (an inbox with a conversation list and a chat, and a floating chat bubble). Below the hero: a strip of integration tiles, a feature grid (8 features), a channels section, the "See what they type before they hit send" live typing preview, AI section, "Set up in 2 minutes" 3-step section (create a workspace → paste the snippet / install the WordPress plugin or Shopify app → reply from your inbox), a placeholder area for real testimonials (the founder fills it later; don't invent customer names or logos), a pricing teaser and a final CTA band. **Parlo's own chat widget runs live on the marketing site**, connected to a demo workspace.
2. **Feature pages** `/features/chat-widget`, `/features/shared-inbox`, `/features/multichannel`, `/features/crm`, `/features/knowledge-base`, `/features/ai`, `/features/chatbot`, `/features/campaigns`: each with a hero, 3–6 benefit sections with HTML/CSS mockups, an FAQ and a CTA.
3. **Pricing `/pricing`:** the freemium plans, AI calculator, comparison table and FAQ exactly as specified in **6.12**, plus `/compare/{competitor}` pages and the "Add free live chat" landing page for "Powered by" referral traffic.
4. **Integrations marketplace:** see 6.1.1. This must match the structure exactly.
5. **Docs `/docs`:** installation guide, JavaScript SDK reference, REST API reference (rendered from OpenAPI), webhooks reference, and guides for every integration.
6. **Blog `/blog`** (MDX), **Changelog `/changelog`** (MDX), **About**, **Contact** (form → creates a conversation in Parlo's own workspace), **Legal**: `/terms`, `/privacy`, `/dpa`, `/cookies` (clearly marked templates for a lawyer to review).
7. **Auth pages:** `/signup`, `/login`, `/forgot-password`, `/reset-password`, `/verify-email`, `/invite/[token]`.
8. A styled **404 and 500**.
9. **SEO:** per-page `<title>` and meta description, Open Graph and Twitter images (generated), `sitemap.xml`, `robots.txt`, canonical URLs, JSON-LD (Organization, SoftwareApplication, FAQPage), i18n-ready routes (`/en/...`, `/fr/...` with hreflang), and a Lighthouse score ≥ 95 on every page.
10. **Cookie consent** banner (only when non-essential cookies/analytics are enabled).

#### 6.1.1 Integrations marketplace (mirror this information architecture exactly)

URL structure:
- `/integrations` → landing: a "Most popular" section first, then "All integrations"
- `/integrations/category/recent`
- `/integrations/category/popular`
- `/integrations/category/automation`
- `/integrations/category/cms`
- `/integrations/category/crm`
- `/integrations/category/marketing`
- `/integrations/category/messaging`
- `/integrations/category/other`
- `/integrations/category/teamwork`
- `/integrations/[slug]` → detail page for each integration

Layout:
- **Left sidebar** (becomes a horizontal scrollable chip list on mobile):
  - Recent
  - Most popular
  - Heading **"Categories"**: Automation, CMS, CRM, Marketing, Messaging, Other, Team-work
  - Highlight the active item.
- **Main area:** page title + one-line description, a search box (filters instantly), and a responsive grid of cards. Each card shows an icon tile (the integration color with initials, white or dark text depending on contrast), the name, a one-line tagline, and a badge ("Coming soon" or "Beta" when relevant). The whole card is a link.
- **"Recent"** = sorted by `addedAt` descending. **"Most popular"** = sorted by real install count (from the `Integration` table), falling back to the `popularity` field.
- **Detail page:** breadcrumb (Integrations › Category › Name), large icon, name, tagline, status badge, and a primary CTA that depends on the install type:
  - `plugin` → "Download plugin" + "Create free account"
  - `native` → "Connect in dashboard" (deep link to that integration's settings page)
  - `snippet` → "Get your snippet" + a code block with the snippet and a copy button
  - `soon` → disabled "Coming soon" + a "Notify me" email capture that stores interest per integration
  
  The page then shows "Overview", "What you get" (feature bullets), "How to set it up" (numbered steps), FAQ, and "More in this category" cards. Store catalog data in `packages/shared/catalog.ts` and seed it into `IntegrationCatalogItem` so the dashboard and the website share one source of truth.

**The "Most popular" section must show these three first, in this order:**
1. **WordPress**: "Live chat plugin for WordPress" (category CMS, install type plugin)
2. **Shopify**: "Answer shoppers faster and see their orders right in your inbox" (category CMS, native)
3. **WhatsApp**: "Shared team inbox for the WhatsApp Business Platform" (category Messaging, native)

**Full catalog to seed** (write your own original tagline, description, features and setup steps for each):

| Category | Available (fully working, in the phase that builds it) | Coming soon (listed, labeled) |
|---|---|---|
| **Messaging** | WhatsApp, Email (Gmail / Microsoft 365 / forwarding / SMTP), Messenger, Instagram DMs, Telegram, LINE, Viber, X/Twitter DMs, SMS (Twilio), Discord, Slack Connect, Microsoft Teams, Amazon Buyer Messages, Klaviyo replies, Phone (native, then Aircall, Ringover) | Apple Messages for Business, Google Business Messages successor, RCS |
| **CMS** | WordPress (plugin), Shopify (app), WooCommerce (via the WordPress plugin), PrestaShop (module), Adobe Commerce / Magento 2 (module), WHMCS (module), Webflow, Wix, Squarespace, Ghost, Drupal, Joomla, Framer, Bubble, Notion sites, Google Tag Manager (snippet guides) | BigCommerce, Shopware |
| **CRM** | (built-in CRM) HubSpot (2-way sync), Salesforce, Pipedrive, Zoho CRM, Microsoft Dynamics 365 | Attio, Close, monday CRM |
| **Marketing** | Google Analytics 4, Google Tag Manager, Mailchimp, Klaviyo, Segment, PostHog, Mixpanel, Amplitude, Brevo, ActiveCampaign | Customer.io, HubSpot Marketing |
| **Automation** | Webhooks, Zapier, Make, n8n, Dialogflow (external bot), Calendly / Cal.com (booking actions) | Pipedream, Workato |
| **Team-work** | Slack (alerts + reply from Slack), Microsoft Teams, Discord, Jira, Linear, GitHub, Trello, Notion | Asana, ClickUp |
| **Other** | JavaScript SDK, React / Next.js guide, REST API, MCP server, Stripe (customer & billing sidebar + actions), ChargeDesk-style billing view, iOS / Android / React Native / Flutter SDKs, Status page reporters | Zendesk / Intercom / Crisp importers (listed under Other) |

"Available at launch" means available by the end of the phase that builds it (section 12). Until then it shows "Coming soon".

### 6.2 Authentication, workspaces and team

- Sign up with email + password (with a password strength meter) or **Google OAuth**. Email verification, forgot/reset password, and an optional magic link.
- **Two-factor authentication (TOTP)** with recovery codes; owners can enforce 2FA for the workspace.
- Sessions use secure, httpOnly, SameSite=Lax cookies with rotation. Users can see their active sessions and revoke them. Changing the password signs out other sessions.
- **Onboarding wizard** after signup: workspace name, website URL, then pick the install method (snippet / WordPress / Shopify / Wix / …) with copy-paste instructions. A "Send test message" button opens the user's own site, or a preview page with the widget. Then invite teammates. A checklist stays visible in the dashboard until setup is complete.
- **Workspace switcher** (one user, many workspaces). Create workspace. Delete workspace (owner only, typed confirmation, 7-day soft delete).
- **Team:** invite by email (the invite email has a link; invites expire in 14 days; resend/revoke), roles Owner/Admin/Agent with a clear permission matrix (Agents can't change billing, integrations, workspace settings or delete data), **Teams** (Sales/Support), each operator's availability (Online/Away, plus auto-away after inactivity), avatar, and display name shown to visitors (first name).
- An **Enterprise SSO (SAML/OIDC)** placeholder architecture, built in phase 5.

### 6.3 Chat widget (the embeddable chatbox)

**Install snippet** (shown in Settings → Installation, pre-filled with the workspace's Website ID):
```html
<script type="text/javascript">
  window.$parlo = [];
  window.PARLO_WEBSITE_ID = "WEBSITE_ID";
  (function () {
    var d = document, s = d.createElement("script");
    s.src = "https://client.yourdomain.com/l.js";
    s.async = 1;
    d.getElementsByTagName("head")[0].appendChild(s);
  })();
</script>
```

**Behavior and features:**
- Loads **asynchronously after page load**, never blocks rendering, causes no layout shift, < 35 KB gzipped, and renders inside **Shadow DOM** with a z-index-safe container. Works on any site, framework or CMS. Works in Chrome, Safari, Firefox, Edge and mobile browsers.
- **Launcher bubble** (bottom right or left, configurable) with an unread badge and a gentle animation when a new message arrives.
- **Chat window:** header with team avatars (up to 3), workspace name, availability ("Online — we reply in a few minutes" / "Away — we'll reply by email"), and a close button. On mobile it opens full-screen.
- **Home tab:** welcome message, "Start a conversation" button, knowledge base search with top articles (when the help center is enabled), and recent conversation preview.
- **Messages:** grouped by sender, avatars, timestamps, **delivery and read receipts**, the operator typing indicator ("Lea is typing…"), safe auto-linking (http/https only, `rel="noopener noreferrer nofollow"`), emoji picker, **file and image upload** (drag-and-drop, paste, previews, 10 MB limit, virus-scan hook), image lightbox, and link previews.
- **Live typing preview:** as the visitor types, the draft text (debounced, max 500 chars) streams to operators in real time. Crisp is famous for this feature; build our own version and **never** use Crisp's name for it. Workspaces can turn it off.
- **Pre-chat form / email capture:** optional "ask for email before chat". When no operator is online, the widget asks for the visitor's email so the team can reply later by email.
- **Persistence:** the visitor session token lives in `localStorage` (with a cookie fallback), so the conversation survives reloads and new tabs. Open tabs stay in sync (BroadcastChannel). Messages missed while the socket was disconnected are fetched on reconnect.
- **Sounds and title notification:** a soft sound plus a "(1) New message" tab title when a reply arrives and the window is closed or the tab is hidden.
- **Proactive messages / triggers:** e.g. "Show 'Need help choosing a plan?' after 20 seconds on /pricing", configurable in the dashboard (rules: URL contains, time on page, number of visits, scroll %, exit intent, country, language, returning visitor, segment).
- **CSAT rating:** when a conversation is resolved, the widget asks "How was your conversation?" (5 emoji or stars plus an optional comment).
- **Bot / AI messages** render buttons, quick replies, cards and carousels.
- **Customization (from the dashboard, applied live without reload):** color, position, launcher icon, logo, welcome text, team tagline, offline message, language, hide on mobile, hide the launcher (open via the SDK only), and "Powered by Parlo" (removable on paid plans).
- **Visitor context captured:** current page URL and title, page history, referrer, UTM parameters, browser, OS, device, screen size, language, timezone, and approximate location (country/city from the IP via a GeoIP database, without storing raw IPs after lookup).
- **Security:** allowed-domains list (the widget refuses other origins), rate limiting, spam/abuse protection (blocked contacts, honeypot, per-IP limits), and **identity verification**. When a site identifies a user, it passes `signature = HMAC_SHA256(email, workspace.identitySecret)` generated on its own server, so nobody can impersonate another user's email.
- **JavaScript SDK (`window.$parlo` command queue,** works before and after load):
  ```js
  $parlo.push(["set", "user:email", ["jane@acme.com", "<hmac-signature>"]]);
  $parlo.push(["set", "user:nickname", ["Jane Doe"]]);
  $parlo.push(["set", "user:phone", ["+33612345678"]]);
  $parlo.push(["set", "user:avatar", ["https://…/jane.png"]]);
  $parlo.push(["set", "user:company", ["Acme", { url: "https://acme.com" }]]);
  $parlo.push(["set", "session:data", [[["plan", "pro"], ["mrr", 99]]]]);
  $parlo.push(["set", "session:segments", [["vip", "beta"]]]);
  $parlo.push(["set", "session:event", [[["signed_up", { source: "ads" }]]]]);
  $parlo.push(["do", "chat:open"]);   // also chat:close, chat:toggle, chat:show, chat:hide
  $parlo.push(["do", "message:send", ["text", "Hi, I need help with my order"]]);
  $parlo.push(["do", "message:show", ["text", "Hey 👋 want a demo?"]]);   // local operator-style message
  $parlo.push(["do", "session:reset"]);   // on logout
  $parlo.push(["on", "message:received", function (m) {}]);   // events: chat:opened, chat:closed, message:sent, message:received, session:loaded
  $parlo.push(["config", "locale", "fr"]);
  ```
- **Mobile SDKs** (phase 5): native iOS (Swift), Android (Kotlin), React Native and Flutter chat SDKs using the same widget API.

### 6.4 Shared inbox (the heart of the product)

Layout: **3 panes**: a conversation list (left), the conversation (center), and contact details (right, collapsible). Left icon rail: Inbox, Contacts, Campaigns, Knowledge base, Bots & AI, Analytics, Settings, plus the workspace switcher and a profile menu with availability toggle.

**Conversation list:**
- Views with live counts: **Unassigned, Mine, All open, Unread, Snoozed, Resolved**, by **Team**, by **Channel**, by **Tag**, and saved custom views (filter builder: status, channel, assignee, tag, segment, rating, country, date…).
- Each row: contact avatar with online dot, name/email, channel icon, last message preview (bold when unread), time, unread count, assignee avatar, and priority flag.
- Real-time updates: new conversations and messages bump to the top with a subtle highlight. Infinite scroll. **Bulk actions** (assign, tag, resolve, snooze).
- **Full-text search** across contacts and message content (Postgres tsvector) with highlighted results.

**Conversation view:**
- Message thread with day separators, visitor vs operator styling, **private notes** (yellow, never sent to the visitor), system events (assigned, resolved, rated…), delivery status for each message (pending/sent/delivered/read/failed with retry), attachments, and image previews.
- **Live typing preview** of what the visitor is typing (gray italic bubble at the bottom).
- **Collision detection:** "Lea is viewing" / "Lea is typing a reply" avatars.
- **Composer:** reply / note tabs (keyboard: `Cmd/Ctrl+Enter` send, `Tab` switches reply/note); **saved replies** via `/` (fuzzy search) with variables (`{{contact.first_name}}`, `{{operator.first_name}}`, `{{workspace.name}}`); emoji; attachments; **@mention** teammates in notes (they get notified); AI tools (section 6.7: suggest reply, improve writing, change tone, translate, summarize). Drafts are saved per conversation.
- Actions: **assign** to an operator or team (and "assign to me"), **resolve / reopen**, **snooze** (1h, tomorrow 9am, next week, custom), **tags**, **priority**, **block contact**, **mark as spam**, **export transcript (PDF)**, **email the transcript** to the visitor, **merge** conversations, start a new conversation with a contact (outbound, on any connected channel).
- **Replying to an unassigned conversation automatically assigns it to you.** A visitor writing into a resolved conversation **reopens** it.
- **Keyboard shortcuts** (`?` shows the cheat sheet): `j/k` next/previous, `r` reply, `n` note, `e` resolve, `a` assign, `s` snooze, `/` saved replies, `Cmd+K` command palette.

**Contact sidebar:**
- Name, email, phone (inline editable), avatar, online status, **local time**, location (flag + city), language, browser/OS/device, **current page (live)**, page history, referrer and UTM, segments, tags, **custom data** (from the SDK/API), company, internal notes, **previous conversations**, and **events timeline**.
- **Integration widgets:** Shopify customer + last orders (6.8.2), HubSpot contact link, etc.

**Notifications:**
- In-app toasts plus a notification center (mentions, assignments, new conversations).
- **Browser push** (Web Push/VAPID) and **desktop notifications** with sound (configurable per user). Unread count in the tab title and favicon badge.
- **Email notifications** to operators for unanswered messages after X minutes (per-user preference).
- **Visitor email fallback:** when a visitor has left the website and an operator replies, the visitor gets the reply by email after 2 minutes unread. **The visitor's email reply goes back into the same conversation** (via the inbound email pipeline, 6.8.5). This is critical.

**Automation in the inbox:**
- **Routing rules:** e.g. "if channel = WhatsApp → team Support", "if page URL contains /pricing → team Sales", "if segment = VIP → priority high". Auto-assign modes: manual, round-robin, or least-busy among online agents, with a max concurrent chats per agent.
- **Office hours** per workspace (weekly schedule, timezone, holidays). Outside hours, the widget shows away mode and an auto-reply.
- **SLA timers** (first response target) with a visual warning (Business plan).

### 6.4.1 Tickets, SLAs and long-running issues (a Crisp gap)
- A conversation can be turned into a **ticket** (or created as one from email, the customer portal, the API or the widget's "Send us a request" form). **Ticket types** have custom fields (e.g. Bug: severity, URL).
- **SLA policies** (conditions → first response, next response and resolution targets, counted in **business hours**), countdown badges in the inbox, breach alerts (in-app, email, Slack), and SLA reports.
- **Merge** (duplicates are detected and suggested automatically), **split** a message into a new ticket, **link** related tickets, **side conversations** (email a supplier or colleague from inside the ticket without the customer seeing it), **mark as unread**, and **follow** a ticket.
- **Customer portal** (`help.yourdomain.com/{workspace}/requests`, or the custom domain): the customer logs in by magic link, sees their open/closed tickets, replies, and adds attachments.
- **Delivery guarantee** (applies to all conversations): every outbound message shows pending → sent → delivered → read, retries automatically with backoff, and on final failure shows a red banner with "Retry" or "Send by email instead". **Unanswered-chat backup alert:** if a conversation waits longer than X minutes (configurable) and no operator is online, email/SMS the on-call operator.

### 6.5 Contacts / CRM

- Contacts list: search, sort, filter builder (any attribute, custom data, segment, last seen, country, number of conversations), saved **segments** (dynamic), column chooser, pagination, **CSV import** (field mapping, dedupe by email/phone) and **CSV export**.
- Contact profile page: everything from the sidebar plus the full timeline (conversations, page views, events, campaign emails, notes), and edit/delete. **GDPR export** (JSON) and **GDPR erase** (deletes contact + conversations + files).
- **Companies:** list and profile, contacts in the company, custom data.
- **Automatic merging:** when an anonymous visitor gives an email that already belongs to a contact, merge the visitor into that contact (keeping all conversations), with an audit log entry.
- Custom attributes manager (name, type: text/number/date/boolean/list).

### 6.6 Knowledge base / help center

- Article editor (TipTap rich text: headings, lists, images, video embeds, code, callouts, tables), drafts/publish, categories with icons and ordering, **multi-language** versions of each article, SEO fields, and slug.
- **Public help center** at `help.yourdomain.com/{workspace}` with an optional **custom domain** (`help.customer.com`, CNAME + automatic TLS via the hosting provider or Caddy/Let's Encrypt). Themed with the workspace logo and color, fast instant search, an "Was this helpful?" vote, and a "Still need help? Chat with us" button that opens the widget.
- **Inside the widget:** article search, suggested articles while the visitor types, and articles read without leaving the widget.
- **In the inbox:** search articles and insert the link into a reply.
- Analytics: views, searches with no results (content gaps), and helpfulness.

### 6.7 AI and chatbots (make this Parlo's strongest area)

**LLM layer** (`packages/llm`): one interface `complete()`, `stream()`, `embed()`. Default provider: Anthropic Claude (model IDs from env), with adapters for OpenAI-compatible APIs, Google and Mistral. Workspaces can pick the provider/model, including an **EU-hosted model** for EU data. Meter **AI resolutions and copilot actions** per workspace exactly as 6.12 defines them (included volume, rollover, spend caps, per-conversation cap), with timeouts, retries, prompt-injection-resistant system prompts, and never send secrets to the model.

1. **AI Copilot for operators** (in the composer):
   - **Suggest reply** using the conversation, the contact profile, the knowledge base and saved replies (streamed, editable before sending).
   - **Improve writing:** fix grammar, make it friendlier / more formal / shorter / longer.
   - **Translate:** detect the visitor's language. Show incoming messages translated into the operator's language (original on hover), and send replies translated into the visitor's language. Auto-translate can be turned on per conversation.
   - **Summarize** long conversations (shown at the top, and also when a conversation is reassigned).
   - **Auto-tagging, sentiment** and **intent detection** on new conversations (feeds routing rules).
2. **AI Agent (answers visitors automatically):**
   - Trained on **sources**: knowledge base articles, website pages (crawler: sitemap or URL list, respects robots.txt, re-crawl schedule), uploaded PDFs/DOCX, and custom Q&A snippets. Text is chunked → embedded → stored in **pgvector**, and answers use **RAG** with citations (links to articles).
   - Settings: on/off, which channels, office hours only / always, tone, max replies before handoff, **confidence threshold**, and topics it must never answer (e.g. refunds → human).
   - **Human handoff:** the visitor asks for a human, or confidence is low, or a sensitive topic comes up → the AI says a teammate will reply, assigns per routing rules, and adds a summary note.
   - **Playground** in the dashboard to test questions and see which sources were used. Feedback loop: operators mark AI answers good/bad, and unanswered questions are suggested as new articles.
   - Analytics: AI resolution rate, handoff rate, credits used.
3. **Chatbot builder (visual flows, no-code):**
   - Drag-and-drop canvas (React Flow). Nodes: Send message, Ask a question with buttons/quick replies, Collect email/phone/name (with validation), Condition (attribute/segment/page/office hours), Set attribute/tag, Assign to team/operator, AI answer, Webhook call (send data / branch on response), Wait, Close conversation.
   - Triggers: conversation started, first visitor message, page URL, office hours closed, specific channel.
   - Test mode (simulate in a side panel), versioning (draft vs live), and analytics per node (drop-off).
4. **AI actions** (the AI agent and copilot *do things*, not only talk):
   - **Built-in actions:** look up an order, track a shipment, cancel/refund/edit an order (Shopify, WooCommerce), look up a Stripe subscription or invoice and update billing details, create a ticket, book or reschedule a meeting (Cal.com/Calendly), and add a tag or assign.
   - **Action builder:** the workspace defines its own action: name, description, input schema, HTTP request (URL, method, headers, auth stored encrypted, body template), and how to read the response. The AI decides when to call it.
   - **Guardrails:** per-action approval rules (e.g. "refunds over $50 need a human"), a human **approval queue** in the inbox, identity verification before account-specific actions (verified email/HMAC or a one-time code), and a full log of every run (AiActionRun).
5. **AI that improves itself, safely:**
   - **Learning from past conversations** (opt-in): mine resolved conversations into suggested Q&A snippets that a human approves before the AI uses them.
   - **Simulations:** before going live (and after every change), run the AI against 50+ real past questions, show each answer, its sources and a score, and block publishing below a threshold. **Simulations and playground use are never billed.**
   - **Knowledge gap detection:** questions the AI could not answer are clustered and turned into **drafted articles** for one-click approval.
6. **AI quality & insights:**
   - **AI QA:** automatically score 100% of human and AI conversations (accuracy, tone, empathy, resolution, policy compliance), with a coaching view per operator and a review queue for low scores.
   - **Predicted CSAT** for every conversation, even without a survey.
   - **Topic clustering in every language:** what customers ask about this week, trending topics, and spike alerts.
7. **"Paste your URL → AI agent live in 5 minutes"** guided setup: crawl the site, auto-generate FAQ snippets, run a simulation, then publish.

### 6.8 Channels and integrations: exact technical requirements

General rules: each integration is a module with `validateConfig`, `connect` (OAuth or credentials), `disconnect`, `test` ("Send test" button), `onEvent` handlers, an inbound webhook receiver (raw body + **signature verification**) and a settings UI. Store config encrypted. Show the connection status, last error and last activity in Settings → Integrations. Deduplicate inbound events with `externalId`. All outbound HTTP goes through the job queue with retries and exponential backoff.

#### 6.8.1 WhatsApp (WhatsApp Business Platform, Cloud API)
- Settings form: **Phone number ID**, **WhatsApp Business Account ID**, **permanent access token** (from a Meta System User), **App secret**, plus an auto-generated **Verify token**. Display the **callback URL** `https://api.yourdomain.com/webhooks/whatsapp/{workspaceId}` with copy buttons and step-by-step instructions (create a Meta app → add the WhatsApp product → add a phone number → configure the webhook → subscribe to the **`messages`** field). Phase 4+: Meta **Embedded Signup** (become a Tech Provider) so customers connect in 3 clicks.
- **Webhook verification:** `GET` with `hub.mode=subscribe`, `hub.verify_token`, `hub.challenge` → if the token matches, respond with the challenge as plain text, else 403.
- **Inbound:** `POST` → verify `X-Hub-Signature-256` = `sha256=` + HMAC-SHA256(raw body, app secret) with a constant-time comparison; reject otherwise. Parse `entry[].changes[].value`: check that `metadata.phone_number_id` matches; `contacts[].profile.name` → contact name; `messages[]` → find or create the contact by `wa_id` (phone `+{wa_id}`), then find or create the WhatsApp conversation, then add the message with `externalId = wamid` (dedupe). Support types: text, image, video, audio/voice, document, sticker, location (maps link), contacts, interactive (button/list reply), button, reaction. **Download media** (`GET /{media-id}` → URL → download with the token) into S3 and show it inline. `statuses[]` → update the message's `deliveryStatus` (sent → delivered → read; failed shows the error), never downgrading. Always respond 200 quickly once the signature is valid (process in a job).
- **Outbound:** an operator reply in a WhatsApp conversation → `POST https://graph.facebook.com/{version}/{phone-number-id}/messages` with `{ messaging_product: "whatsapp", recipient_type: "individual", to: wa_id, type: "text", text: { preview_url: true, body } }` and Bearer token; store the returned `messages[0].id` as `externalId`; on error mark the message failed and add a system note with the reason. Support sending images/documents.
- **24-hour customer service window:** track the last inbound message time. Outside 24h the composer switches to **template messages**: sync approved templates from `GET /{waba-id}/message_templates`, pick one, fill the variables, and send `type: "template"`. Show a countdown "Window closes in 3h".
- Graph API version comes from an env var (default the current stable `vXX.0`).

#### 6.8.2 Shopify (public app)
- Build with the **Shopify CLI** in `/integrations/shopify`:
  - **OAuth install:** the dashboard asks for the store domain (validate `^[a-z0-9][a-z0-9-]*\.myshopify\.com$`) → redirect to `https://{shop}/admin/oauth/authorize?client_id&scope=read_customers,read_orders&redirect_uri&state`. The callback verifies the **`hmac` query parameter** (HMAC-SHA256 of the sorted query string without `hmac`, using the app secret), the **`state`** (stored, single-use, 15-minute expiry) and the shop domain, then exchanges `code` at `https://{shop}/admin/oauth/access_token` for an **offline access token** (stored encrypted). Also support installs that start from the Shopify App Store or admin (embedded app + session token exchange).
  - **Theme app extension (app embed block)** that loads the widget on the storefront. Merchants enable it in Online Store → Themes → Customize → App embeds. It passes the Website ID automatically and identifies **logged-in customers** with Liquid (`customer.email`, `customer.first_name`, `customer.last_name`, with an HMAC signature computed by an app proxy or metafield), plus cart contents as session data.
  - **Embedded admin page** (App Bridge + Polaris): connection status, a "Open Parlo inbox" link, and widget on/off.
- **Inbox sidebar widget:** look up the contact's email via the **Admin GraphQL API** (`customers(first:1, query:"email:\"...\"")` → displayName, numberOfOrders, amountSpent, createdAt, last 5 orders with name, date, financial status, fulfillment status, total, admin links). Phase 4: actions (view order, copy tracking link, create a draft order/discount code).
- **Mandatory compliance webhooks:** `customers/data_request`, `customers/redact`, `shop/redact`, plus `app/uninstalled`. Verify `X-Shopify-Hmac-Sha256` (base64 HMAC-SHA256 of the raw body with the app secret). On uninstall/shop redact, delete the stored token and config.
- Pin the Admin API version from an env var (quarterly versions `YYYY-01/04/07/10`). Write `docs/SETUP_SHOPIFY.md` (Partner account, app creation, protected customer data access request, App Store listing checklist).

#### 6.8.3 WordPress plugin "Parlo Live Chat" (`/integrations/wordpress/parlo-live-chat`)
- Standard plugin header, text domain `parlo-live-chat`, `readme.txt` in WordPress.org format (Stable tag, Tested up to, FAQ, screenshots section), `uninstall.php` that removes options, GPLv2+ license.
- **Settings page** (Settings → Parlo Live Chat) using the Settings API, `manage_options` capability and nonces: Website ID, a **"Connect with Parlo" one-click button** (opens `app.yourdomain.com/connect/wordpress?return_url=…`; after login the user picks a workspace and is sent back with the Website ID filled in), enable/disable, hide on specific pages/post types/user roles, and a "Identify logged-in users" toggle.
- Injects the snippet via `wp_footer` (or `wp_enqueue_script` + `wp_add_inline_script`), with every value escaped (`esc_js`, `wp_json_encode`). Identifies logged-in users (`wp_get_current_user`: email, display name), with an HMAC signature computed server-side using the identity secret saved in the settings.
- **WooCommerce support:** pass cart total, item count and the customer's last order as session data. Show recent WooCommerce orders in the Parlo inbox via the WooCommerce REST API (phase 4).
- The zip is downloadable from the integration page (`/downloads/parlo-live-chat.zip`, built in CI). Passes `php -l`, WordPress Coding Standards (PHPCS) and Plugin Check. Document submission to the WordPress.org plugin directory.

#### 6.8.4 Slack
- Phase 2: Incoming-webhook notifications (new conversation / every visitor message / mentions), with a button linking to the conversation.
- Phase 4: a full **Slack app** (OAuth v2) where each conversation becomes a Slack thread and **operators can reply from Slack** (Events API, signing-secret verification with `X-Slack-Signature`/`X-Slack-Request-Timestamp`, replay protection < 5 min).

#### 6.8.5 Email channel
- Each workspace gets a forwarding address `{slug}@inbound.yourdomain.com`; customers forward `support@theirdomain.com` to it. Inbound is parsed from the provider's inbound webhook (Postmark/SendGrid/Mailgun/SES, signature verified): strip quoted replies and signatures, keep attachments, and thread replies by `Message-ID` / `In-Reply-To` / `References` plus a per-conversation reply-to token.
- Outbound replies are sent "from" the workspace's verified custom domain (SPF/DKIM/DMARC setup screen with DNS records and a verification check), falling back to `notifications@yourdomain.com`.
- Visitor email fallback (6.4) uses this same pipeline.

#### 6.8.6 Messenger & Instagram DMs
- Meta login (Facebook Login for Business) → pick a Page / Instagram professional account → subscribe the app to page webhooks (`messages`, `messaging_postbacks`, `message_reads`, `message_deliveries`). Verify `X-Hub-Signature-256`. Send via the Send API. Respect the 24h messaging window (human agent tag where allowed).

#### 6.8.7 Telegram
- Customer pastes a bot token from @BotFather → call `setWebhook` with a random `secret_token`. Verify `X-Telegram-Bot-Api-Secret-Token` on every update. Send with `sendMessage` / `sendPhoto` / `sendDocument`.

#### 6.8.8 Outbound webhooks (Automation)
- Endpoints with selectable events: `conversation.created`, `conversation.updated`, `conversation.resolved`, `message.created`, `message.updated`, `contact.created`, `contact.updated`, `rating.created`, `campaign.sent`.
- Payload `{ id, event, workspaceId, createdAt, data }`. Header `X-Parlo-Signature: t=<timestamp>,v1=<hex HMAC-SHA256("<t>.<raw body>", secret)>` and `X-Parlo-Event`.
- Retries with exponential backoff for 24h, auto-disable after repeated failures (email the owner), a delivery log with request/response, a "Replay" button and a "Send test" button.
- **SSRF protection:** resolve DNS and reject private, loopback and link-local IPs, both at save time and at send time. Don't follow redirects.

#### 6.8.9 Zapier, Make, n8n
- A public Zapier app: triggers (new conversation, new message, new contact, conversation resolved) via REST hooks; actions (create contact, send message, add note, tag conversation). Make/n8n use the webhooks plus REST API (docs + templates).

#### 6.8.10 HubSpot, Mailchimp, GA4, Teams, Discord, snippet platforms
- **HubSpot:** OAuth; sync contacts both ways (email as key); log each resolved conversation as a note/engagement on the HubSpot contact; show the HubSpot link in the sidebar.
- **Mailchimp:** OAuth; choose an audience; push contacts that opted in (with a tag).
- **GA4 / GTM:** the widget pushes `parlo_chat_opened`, `parlo_message_sent`, `parlo_email_captured` to `dataLayer` when enabled.
- **Microsoft Teams / Discord:** webhook notifications like Slack v1.
- **Snippet platforms** (Webflow, Wix, Squarespace, Ghost, Drupal, Joomla, Framer, GTM, React/Next.js): detail pages with accurate step-by-step instructions plus the user's personal snippet when logged in.

#### 6.8.11 E-commerce suite (beat Crisp and match Gorgias/Tidio)
- One sidebar for **Shopify, WooCommerce and Stripe** customers: profile, lifetime value, orders, shipments with tracking links, subscriptions, and **cart preview** (what the visitor has in their cart right now, sent by the widget/theme extension).
- **Order actions** from the inbox and through the AI agent (6.7 actions), with guardrails: refund (full/partial), cancel, edit the shipping address, resend confirmation, create a discount code, and duplicate the order.
- **AI shopping assistant** in the widget: searches the product catalog (synced from Shopify/WooCommerce), recommends products with images and prices, adds to cart and applies discount codes.
- **Revenue attribution:** orders placed within N days after a conversation or an AI reply are attributed (by customer email/cart token), and the analytics show "revenue influenced by support" per operator, AI and campaign.
- **WhatsApp commerce:** share product catalogs, send template broadcasts to opted-in contacts, and track click-to-WhatsApp ads.

#### 6.8.12 Phone channel and AI voice receptionist (Phase 5)
- Buy or port phone numbers (Twilio/Telnyx). Calls ring in the browser and the mobile app (WebRTC), with IVR menus, voicemail and a recording consent message, plus **transcripts and AI summaries in the conversation timeline**.
- An **AI voice receptionist** answers calls 24/7 using the same knowledge base and actions, and transfers to a human or takes a message. Resolutions are billed like chat resolutions.
- SMS (send and receive) on the same numbers.

#### 6.8.13 B2B support channels (Phase 4)
- **Slack Connect** shared channels: each customer's shared channel becomes a source of conversations; threads map to tickets and replies sync both ways.
- **Microsoft Teams** and **Discord** as inbound support channels (not only notifications), using the same thread-to-ticket model.

#### 6.8.14 More messaging channels (Phase 4), all landing in the same inbox
Every channel must verify the platform's request signature, dedupe by external ID, support attachments where the platform does, and show its icon in the inbox.
- **LINE:** Messaging API, verify `X-Line-Signature` (base64 HMAC-SHA256 of the body with the channel secret); reply/push messages.
- **Viber:** bot API, verify `X-Viber-Content-Signature` (hex HMAC-SHA256 with the bot token).
- **SMS:** Twilio (later Telnyx/Vonage), verify `X-Twilio-Signature`; MMS images; STOP/opt-out handling.
- **X/Twitter DMs:** Account Activity API (CRC challenge + signature); needs a paid X API tier, so document the cost.
- **Instagram:** also handle story replies and story mentions. **Messenger:** postbacks and quick replies.
- **Discord:** a bot for support servers/DMs (Gateway events, or interactions verified with Ed25519).
- **Amazon buyer messages:** via the Amazon seller email relay into the email channel, with Amazon policy warnings (no external links/marketing).
- **Klaviyo replies:** replies to Klaviyo email/SMS land in the inbox (Klaviyo webhook/integration).
- **Custom channel API:** developers push inbound messages and receive outbound replies through signed webhooks.

### 6.9 Campaigns (email & in-chat marketing)
- Audience = segment or filter. **One-off** (send now / schedule) or **automated** (trigger: event or attribute change + delay, e.g. "2 days after signed_up if plan = free").
- Email editor (blocks: text, image, button, divider, columns; templates; variables with fallbacks; preview on desktop/mobile; test send). In-chat campaigns appear as a message in the widget the next time the contact visits.
- Compliance: unsubscribe link mandatory and one-click (List-Unsubscribe header), only contacts with marketing consent, physical address in the footer, suppression list, and bounce/complaint webhooks auto-suppress.
- Stats: sent, delivered, opens, clicks, replies (replies land in the inbox), unsubscribes. Throttled sending through the queue.

### 6.10 Analytics
- Dashboards with a date-range picker and comparison to the previous period: conversations (new, resolved, by channel), **first response time** (median/p90), **resolution time**, **CSAT** (average, distribution, comments), messages sent/received, busiest hours **heatmap** (day × hour), per-operator performance table, per-team, tags breakdown, **AI agent resolution rate** and credits, campaign performance, help center views and failed searches.
- **Report builder** (pick a metric, breakdowns, filters, chart type) and **shared dashboards** saved on the server for the whole team (not private, and not saved only in one browser).
- **SLA reports** (achieved vs breached, by policy/team/operator), **agent activity** (online/away/idle time, conversations handled vs resolved, response times, and the "conversation in progress" timeline for each day), **topics** and **AI QA scores** over time, and **revenue influenced** (6.8.11).
- **Raw exports** of conversations, messages, contacts and events (CSV, JSON, Parquet, with date filters), plus a full transcript export. **Data warehouse sync** (S3, BigQuery, Snowflake) on Scale. Scheduled reports by email.
- Charts with an accessible color palette, tooltips, empty states, and CSV export. Nightly rollups into aggregate tables for speed.

### 6.11 Settings (dashboard)
- **Workspace:** name, logo, timezone, language, data region (EU/US, shown read-only), **brands** (add/edit brands, each with its Website ID and domain), **self-serve full data export** and **self-serve account/workspace deletion** (no support ticket needed).
- **Chat widget:** appearance (live preview next to the form), texts, behavior (pre-chat email, live typing preview on/off, sounds, hide on mobile), **triggers / proactive messages**, allowed domains, **identity verification secret** (reveal/rotate).
- **Installation:** snippet with copy button, plus tabs per platform (HTML, WordPress, Shopify, Wix, Webflow, Squarespace, GTM, React/Next.js) and a "Verify installation" check (detects the first widget load from that domain).
- **Inbox:** office hours, routing rules, auto-assign mode, SLA targets, CSAT on/off, auto-resolve after X days of inactivity.
- **Team:** members, roles, teams, invites. **Saved replies. Tags. Contact attributes.**
- **Channels:** WhatsApp, Email, Messenger, Instagram, Telegram (connect/disconnect, status).
- **Integrations:** the catalog inside the dashboard (same data as the website) with connect forms and status.
- **AI:** copilot and agent settings, sources, credits.
- **Help center:** domain, theme, languages.
- **Developers:** API keys (create with scopes, shown once, revoke), webhooks, and docs links.
- **Billing:** current plan, usage (seats, AI credits), upgrade/downgrade, invoices (Stripe Customer Portal).
- **Personal:** profile, avatar, password, 2FA, sessions, notification preferences, language, theme.

### 6.12 Freemium business model, plans & billing (Stripe)

**Strategy in one line:** a **genuinely useful free-forever plan** (more generous than Crisp, Tidio and Chatwoot) to win signups and word of mouth. Every new account also gets a **14-day reverse trial** of the Growth plan. Revenue comes from a **hybrid model**: a flat price per workspace with seats included, plus **metered AI resolutions**. Copilot (AI help for operators) is bundled into every paid plan, never sold per seat.

**Single source of truth:** all plans, prices, limits and feature flags live in `packages/shared/plans.ts`. The pricing page, the billing UI, the upgrade prompts and the **server-side entitlement checks** all read from this one file. Changing a number there changes it everywhere. All prices below are starting proposals the founder can edit.

#### Plans

| | **Free** | **Starter** | **Growth** ⭐ most popular | **Scale** | **Enterprise** |
|---|---|---|---|---|---|
| Price / month (billed yearly) | $0 forever | $29 ($24) | $79 ($66) | $249 ($208) | Custom (from ~$1k) |
| Seats included / extra seat | 3 / — | 4 / +$12 | 8 / +$15 | 20 / +$15 | Custom |
| Human conversations | Unlimited (fair use; review above 5k/month, never hard-block) | Unlimited | Unlimited | Unlimited | Unlimited |
| History visible | 90 days (stored 1 year, unlocked instantly on upgrade) | 1 year | Unlimited | Unlimited | Custom retention |
| Channels | Chat widget + 1 email inbox + operator PWA/mobile | + WhatsApp, Messenger, Instagram, Telegram | + 2 brands/websites | 5 brands | Unlimited |
| Contacts / CRM | Unlimited contacts, 5 custom attributes | 20 attributes, segments | Unlimited attributes, companies, import/export | + custom roles, audit log | + SCIM |
| Knowledge base | 1 help center, 30 articles, our subdomain, "Powered by" | Unlimited articles | Custom domain, multilingual | Multiple help centers | — |
| Chatbot flows (active) | 1 | 3 | Unlimited | Unlimited | Unlimited |
| AI agent resolutions / month | 50 (renews monthly, hard cap) | 200 | 600 | 2,000 | Committed volume |
| AI copilot (drafts, rewrite, summaries, translation) | 50 actions / month | Included (fair use) | Included | Included | Included |
| Campaigns | In-widget proactive messages only | 2,000 email sends / month | 10,000 | 50,000 | Custom |
| Office hours, saved replies, tags, notes, mentions, CSAT | ✅ | ✅ | ✅ | ✅ | ✅ |
| Routing rules, SLAs, auto-assign, advanced analytics | — (7-day analytics) | 30-day analytics | ✅ full | ✅ | ✅ |
| Integrations | WordPress, Shopify, WooCommerce, Slack alerts, all snippet platforms | + REST API, webhooks, Zapier/Make | + HubSpot & CRMs, Shopify order actions | + sandbox workspace | Custom |
| Widget branding | "Powered by Parlo" shown | **Removed** | Removed | Removed | Removed |
| Security | 2FA | 2FA | 2FA enforcement | + SAML SSO, audit log UI | + data residency, DPA, SLA, HIPAA-ready option |
| Support | Help center + community | Email | Priority email + chat | Priority + onboarding call | Dedicated manager |

Why this beats the market, as a short "Why Parlo" block on the pricing page:
- **3 free seats and unlimited conversations.** Tidio caps free at 50 conversations; Crisp gives 2 seats.
- **An email inbox on Free.**
- **WhatsApp and branding removal from $29.** Crisp gates WhatsApp at $95 and branding removal at $295.
- **Private notes, saved replies, search, office hours and an email inbox on Free.** Crisp's Free plan has none of these and only 2 seats.
- **AI included every month**, not a one-time allowance.
- **Copilot bundled** instead of $29+/seat.
- **Capped AI spend**: no surprise bills.

#### Reverse trial
- Every signup gets **14 days of Growth for free, with no card**. During the trial, AI resolutions are capped at 100 to control cost.
- When the trial ends, the workspace moves to **Free automatically. Nothing is ever deleted.** Paid-only features become locked (visible but disabled with an upgrade prompt), and conversations older than 90 days are shown greyed out with "Upgrade to see full history".
- In-app banner countdown, plus emails on day 1, 7, 12 and 14 that show what the team used ("Your AI agent resolved 37 conversations this trial").

#### AI pricing (resolution-based, capped, honest)
- **Definition of a resolution:** an AI agent conversation where the customer confirms it's solved, **or** the conversation ends with no human handoff and is not reopened within 24 hours. **Handoffs to a human are never charged.** Show this definition on the pricing page and in the billing screen.
- Each plan includes resolutions (table above). Above that, paid plans pay **$0.15 per resolution** overage, or buy prepaid packs: 1,000 for $99 or 5,000 for $399 (~$0.08 each).
- Why $0.15: Intercom charges about $0.99 and Zendesk $1.50–2.00 per resolution. Crisp bills tokens per AI *conversation* (roughly $0.05–0.10 each, resolved or not); its credits expire monthly and the bot stops when they run out. Parlo charges only for resolutions, is capped and predictable, and costs about the same as Crisp or less. **Founder: verify the real LLM cost per resolution in the super-admin and adjust `plans.ts`; keep AI gross margin above 60%.**
- **Spend cap:** the default cap is 2× the included amount. Alerts go to owners at 80% and 100% (email and in-app). Owners can raise or lower the cap. Free plans have a hard cap with no overage: when it is reached, the AI hands off to humans and the dashboard shows "AI could have answered 23 more conversations this month — upgrade".
- Unused included resolutions roll over **one** month.
- Meter usage in a `UsageMeter` table (per workspace, per metric, per billing period) and report overage to Stripe usage-based billing (Billing Meters) at the end of each period.
- Track AI cost per resolution internally (tokens × model price) in the super-admin so prices stay profitable.

#### Add-ons
Extra seats; AI resolution packs; extra brand/website ($19/month); extra campaign sends. **WhatsApp conversation fees are passed through at Meta's cost with 0% markup**, shown transparently. Phone/voice minutes come later. There is **no** "remove branding" add-on on Free; that is the main reason to move to Starter.

#### Upgrade moments (in-product paywalls, with no dead ends)
Show a friendly upgrade modal or inline card **exactly when the user hits the limit**. It shows their own usage, what they unlock, and the price, and offers a one-time "Try it free for 7 days". **Never interrupt a user mid-reply and never block an incoming customer message.** Trigger points:
1. Inviting a 4th teammate on Free.
2. Clicking "Connect WhatsApp / Instagram / Messenger / Telegram" on Free.
3. AI usage at 80% and 100%.
4. Weekly "missed chats" email: "14 chats arrived while you were offline — your AI agent could have answered them."
5. Opening or searching a conversation older than 90 days.
6. Toggling "Remove branding" in the widget editor.
7. Creating a 2nd chatbot flow, a 31st article, a help-center custom domain or a 2nd website.
8. Creating an API key or webhook.
9. Analytics: 7 days visible, longer ranges blurred with a preview.
10. Turning on routing rules / SLAs once 2+ operators are active.
11. Starting the first email campaign.
12. A milestone celebration at the 100th conversation, with a plan suggestion.

Log every paywall view, click and conversion as analytics events (below).

#### Viral loop and referrals
- The widget footer, email transcripts, help-center footer and CSAT pages of Free workspaces show **"⚡ Powered by Parlo"**. The link carries `?ref={workspaceId}&utm_source=widget` and goes to a landing page "Add free live chat to your website in 2 minutes".
- **Referral program:** when a referred signup becomes paid, the referrer gets 1 month free or 200 AI resolutions, and the new customer gets 20% off for 3 months. There is a referral dashboard in Settings → Billing.
- **Agency / partner program:** a multi-client dashboard (switch between client workspaces, bill centrally or per client), 20% recurring commission (founder adjustable), a partner directory page and white-label options on Scale.

#### Special programs
- **Startups** (raised under $5M, under 20 staff): Growth at 90% off year 1 and 50% off year 2, with 300 AI resolutions/month. Application form + manual approval in the super-admin.
- **Nonprofits & education:** 50% off any plan.
- **Open-source projects:** Growth free (verified via GitHub org).

#### Anti-abuse for the free plan
- Email verification required; disposable email domains blocked; per-IP and device-fingerprint signup limits; Cloudflare Turnstile CAPTCHA on signup and when spam is detected.
- One Free workspace per **verified widget domain** (verified by the snippet's first ping).
- **Phone verification is required before enabling the AI agent on Free.** The free AI only trains on the verified domain.
- Per-visitor limits (e.g. 20 AI messages per conversation, message rate limits) to stop bots draining credits.
- No bulk email campaigns on Free. On paid plans: double opt-in for imported lists, manual review of the first campaign, sender-reputation scoring, auto-pause on high bounce/complaint rates.
- Free workspaces with no widget activity for 90 days are archived (owner warned twice by email); their data is kept for 12 months and then deleted (documented in the privacy policy).

#### Billing implementation (Stripe)
- **Stripe Checkout** for upgrades, **Customer Portal** for cards/invoices/cancel, proration for seat and plan changes, monthly/yearly ("2 months free"), and **Stripe Tax** for VAT/GST. Coupons and promotion codes power startups, referrals and partners.
- **Localized pricing:** charge in USD, EUR, GBP, INR and BRL, with purchasing-power-adjusted prices (30–50% lower) for emerging markets, selected by card country + IP. AI packs get at most 20% off because of the cost floor.
- Webhooks: `checkout.session.completed`, `customer.subscription.created|updated|deleted`, `invoice.paid`, `invoice.payment_failed`, `customer.subscription.trial_will_end`. Signature verified, idempotent handling (store processed event IDs).
- **Downgrades never delete data.** Extra seats beyond the new plan become read-only (the owner picks who stays active). Over-limit features lock, but conversations keep flowing in. Failed payments trigger dunning emails at day 0/3/7, a 14-day grace period, then an automatic move to Free.
- **Entitlements engine:** `can(workspace, "feature")` and `limit(workspace, "metric")` helpers, used by **every** API route and UI component. Never trust the client. Every limit has an integration test.
- **Pricing page:** 4 columns + Enterprise, Growth highlighted, annual selected by default, an **AI cost calculator** (slider: monthly conversations × % AI-resolved → price), the resolution definition, a full comparison table, a "Free forever — no credit card" note and an FAQ.
- **Comparison pages** `/compare/{competitor}` (Crisp, Intercom, Tidio, tawk.to, Zendesk, LiveChat, Chatwoot): factual, dated, fair tables with sources, plus migration help.

#### Growth metrics to instrument (product analytics, e.g. self-hosted PostHog)
Track these events and show the funnel in the super-admin:
- **Acquisition:** visitor → signup, plus the share of signups from "Powered by" links.
- **Setup:** widget live (first ping) within 24h, and median minutes to widget live.
- **Aha moment:** first visitor conversation answered within 7 days, and first AI resolution.
- **Habit:** conversations replied in 3 of the first 4 weeks; 2+ active seats or 2+ channels.
- **Product-qualified lead (PQL):** hit a limit + invited a teammate + more than 50 conversations/month. Flag PQLs to the founder.
- **Conversion:** free → paid within 180 days (target 3–5%, great is 6–8%) and reverse-trial conversion.
- **Economics:** net revenue retention, annual vs monthly mix, AI gross margin per resolution, cost per active free workspace, abuse rate.

### 6.13 Public REST API & developer platform
- `https://api.yourdomain.com/v1/...` with **API keys** (`Authorization: Bearer pk_live_…`, scopes like `conversations:read`, `conversations:write`, `contacts:read`, `contacts:write`, `messages:write`, `articles:read`), per-key rate limits (headers `X-RateLimit-*`), cursor pagination, consistent errors `{ error: { code, message } }`, and idempotency keys for POST.
- Resources: workspaces (current), conversations (list/get/update/assign/resolve), messages (list/send/note), contacts (CRUD, search, events, data), companies, segments, tags, saved replies, articles, operators, webhooks.
- An **OpenAPI 3.1 spec** generated from zod schemas, a rendered API reference in `/docs/api`, and copy-paste examples (curl, JS, Python).
- **MCP server** (Phase 4), **read + write** with OAuth and the same scopes: list/search conversations, read a conversation, reply, add a note, tag, assign, look up contacts, search the knowledge base, and run AI actions. Customers can plug Parlo into Claude, ChatGPT or their own agents.
- Phase 5: a **realtime API** (WebSocket) for customers' own bots, and an official Node SDK.

### 6.14 Super-admin back office (internal, `/admin`, staff only)
- Search workspaces and users; view plan, usage and health; impersonate a user (time-limited, logged in the audit log, banner shown); **trust & safety queue** (automated signals may only *throttle*; suspending a workspace requires a human decision with a written reason sent to the owner, plus an appeal form; every case is stored in TrustSafetyCase); freemium funnel and PQL list (6.12); startup/partner program approvals; AI cost per resolution; feature flags per workspace; global announcement banner; job queue dashboard (Bull Board); webhook failure overview.

### 6.15 Phase-5 extras (Crisp parity and beyond)
- **Status page** product: HTTP/TCP/ping monitors, a public status page per workspace (custom domain), incidents and maintenance, subscribers notified by email.
- **Audio/video calls and screen sharing** from a conversation (WebRTC/LiveKit), and **co-browsing** (operator sees the visitor's page with consent).
- **Mobile apps** for operators (React Native/Expo, push notifications) plus a **desktop app** (Tauri/Electron).
- **Native mobile chat SDKs** (6.3).
- **SSO SAML/OIDC + SCIM**, **data residency** (EU/US), and an **audit log UI**.
- **Importers** from Intercom, Zendesk and other competitors (CSV/API) to make switching easy.

---

## 7. Realtime contract (Socket.IO)

- Namespaces: `/operator` (auth: session cookie, joins rooms `workspace:{id}` and `user:{id}`) and `/visitor` (auth: Website ID + visitor token, joins room `contact:{id}`).
- Server → operator events: `conversation:created`, `conversation:updated`, `conversation:read`, `message:created`, `message:updated` (delivery status, edits), `visitor:typing` (with live `preview` text), `visitor:presence`, `visitor:page`, `operator:presence`, `operator:typing`, `operator:viewing`, `contact:updated`, `notification:created`.
- Server → visitor events: `message:created`, `operator:typing`, `availability` (online/away), `settings:updated` (widget appearance changed live), `conversation:status` (resolved → show rating).
- Client → server: `typing` (debounced, with preview for visitors), `page` (visitor navigated), `read`, `viewing` (operator opened a conversation).
- **Reliability:** every message is first persisted via REST (or a socket ack), then broadcast. Clients reconcile with temporary IDs (optimistic UI). On reconnect, clients fetch everything newer than their last known message. Use the Redis adapter so it works across multiple API instances. Heartbeats and presence have a 30s timeout.

---

## 8. API conventions (internal dashboard API)
- REST + JSON, validated with zod. Every route checks auth → membership → role permission → workspace scoping (**never** trust a workspace ID from the client without the membership check).
- Errors: `{ error: { code, message, fields? } }` with correct HTTP status codes. Friendly messages the UI can show directly.
- The widget API (`/widget/v1/{websiteId}/...`) is public with open CORS, uses the visitor token header `X-Visitor-Token` (no cookies), is rate limited per IP and token, and enforces the allowed-domains check on `Origin`.

---

## 9. Performance & scalability targets
- Widget: < 35 KB gzipped, interactive < 300 ms after load, no impact on the host site's Core Web Vitals.
- Message delivery visitor → operator screen: **< 300 ms p95**.
- Dashboard: first load < 2 s on 4G; conversation switch < 150 ms (cache + prefetch); lists virtualized.
- Must handle 10,000 concurrent widget connections per API instance and scale horizontally (stateless API, Redis adapter, queue workers).
- Database: indexes for every list query, no N+1 queries, pagination everywhere, message archive strategy (partition by month when large).

---

## 10. Security & compliance checklist (all required)
- [ ] Passwords argon2id; login rate limiting + lockout; 2FA; secure session cookies; CSRF protection for cookie-authenticated routes.
- [ ] Every query scoped by workspace + membership; authorization tests for every route ("user from workspace A cannot read workspace B").
- [ ] All user content escaped/sanitized (React escaping; DOMPurify for rich text; no `dangerouslySetInnerHTML` with raw input; widget builds DOM nodes with `textContent`).
- [ ] Webhook signatures verified for Meta (WhatsApp/Messenger/Instagram), Shopify, Stripe, Slack, Telegram and email providers, with constant-time comparison and raw-body access.
- [ ] Integration secrets encrypted at rest (AES-256-GCM); tokens/API keys stored hashed; secrets never returned to the client after saving (show "••••").
- [ ] SSRF protection on any user-supplied URL (webhooks, crawler, link previews).
- [ ] File uploads: size/type limits, randomized keys, served with `Content-Disposition` + correct content type from a separate domain, virus-scan hook.
- [ ] Security headers: CSP (strict on the dashboard), HSTS, X-Frame-Options/frame-ancestors, Referrer-Policy, X-Content-Type-Options.
- [ ] Rate limiting on auth, widget, public API and webhooks (Redis based).
- [ ] Widget identity verification (HMAC) and an allowed-domains option.
- [ ] Audit log for sensitive actions (role changes, deletes, exports, impersonation, integration changes).
- [ ] GDPR: data export, erasure, retention settings, DPA page, cookie consent on the marketing site, sub-processor list, EU hosting option documented.
- [ ] Dependency scanning (npm audit/Dependabot) in CI, secrets never committed, `.env.example` documented.
- [ ] Backups: daily Postgres backups + restore procedure documented.

---

## 11. Testing & quality requirements
- **Unit tests:** services (message creation, unread counters, reopen on visitor message, auto-assign on reply, routing rules, entitlements), signature verification helpers (with real known test vectors), and zod schemas.
- **API integration tests** (real Postgres in Docker): auth flows, permissions matrix, conversations, contacts, widget endpoints, every webhook receiver (valid signature → processed; invalid → 401; duplicate → ignored), Stripe webhooks.
- **End-to-end tests (Playwright):**
  1. Sign up → onboarding → copy snippet → open a fake customer site with the widget → visitor sends a message → the operator sees the **live typing preview** and the message in real time → operator replies → visitor sees it → reload keeps history.
  2. Invite a teammate → they accept → assign the conversation → mention in a note → notification.
  3. Resolve → visitor rates 5 stars → CSAT shows in analytics.
  4. Simulated WhatsApp inbound webhook (signed fixture) → appears in the inbox → reply calls the mocked Graph API → status webhook updates the ticks.
  5. Integrations marketplace: every category page loads and the search filters; detail pages for WordPress/Shopify/WhatsApp show the right CTA.
  6. Mobile viewport runs of the widget and the dashboard.
- **Seed script** (`pnpm db:seed`): demo user `demo@yourdomain.com` / `demo1234`, workspace "Acme Store", 3 teammates, 40 realistic conversations across channels and statuses, contacts with custom data, saved replies, tags, 10 help articles, analytics history for 60 days, and the full integrations catalog. The marketing site's live widget points at a demo workspace.
- CI must be green before a phase is considered done.

---

## 12. Build phases (do them in order; each ends with the Definition of Done in section 14)

**Phase 0: Foundation**
- Monorepo, tooling (ESLint, Prettier, TypeScript strict, Husky + lint-staged), docker-compose, Prisma schema v1 + migrations (including Brand, Region, UsageMeter), design system (tokens, components, light/dark), app shells (marketing layout, dashboard layout with icon rail), CI pipeline, error tracking, logging, product analytics (PostHog), `.env.example`, README.
- The **entitlements engine** and `plans.ts` (6.12).
- `docs/PARITY.md` (copy of section 16) and `docs/COMPETITIVE_ANALYSIS.md` (section 13.4).

**Phase 1: MVP (the product people can actually use, free plan live)**
- Auth (email/password, verify email, reset, Google OAuth, 2FA TOTP, active sessions), workspaces + switcher, onboarding wizard (platform auto-detection), team invites, roles and Teams.
- **Chat widget:** all of 6.3, including file/image uploads, identity verification, `user:id` session continuity and the JavaScript SDK, **except** the items section 16.1 assigns to later phases.
- **Realtime shared inbox:** all of 6.4, including views, live typing preview, notes, @mentions, assign, open/pending/snoozed/resolved, tags, priority, saved replies with `/`, exact + full-text search, attachments, bulk actions, mark unread, keyboard shortcuts, collision detection, notifications, sounds and browser push. **Except** AI tools (Phase 3), integration sidebar widgets, routing rules, office hours and SLA (Phase 2).
- **Delivery guarantee** + **unanswered-chat backup alert** (6.4.1).
- **Visitor email fallback**, both directions (core inbound/outbound email pipeline from 6.8.5).
- Contacts list + profile + custom data + automatic merging + GDPR export/erase.
- Settings: workspace, widget appearance with live preview, installation + verify, team, saved replies, tags, personal profile/password/notifications, **self-serve data export and deletion**.
- **Freemium foundations:** every workspace gets the 14-day Growth reverse trial and then Free. Free-plan limits are enforced by the entitlements engine. "Powered by Parlo" badge with `ref` tracking and the "Add free live chat" landing page. Activation events tracked. (Paid upgrades arrive with Stripe in Phase 2. Until then, locked features show "Available on paid plans soon — you're on the free plan".)
- **Marketing site:** home, feature pages, pricing (6.12), About, Contact, legal templates **including the trust & safety policy**, 404/500, SEO, `/docs` (installation + JavaScript SDK), `/blog` and `/changelog` each with a real launch post.
- **The full integrations marketplace** (6.1.1: every page plus catalog data).
- The **WordPress plugin** (complete, with one-click connect and zip download) and all snippet-platform guides.
- PWA install for operators. Seed data. E2E tests 1, 2, 5 and 6.

**Phase 2: Monetization, channels, helpdesk & insights**
- **Stripe billing + the complete freemium system** (6.12): checkout, portal, seats, upgrade moments/paywalls, AI cost calculator, referrals, localized/PPP prices, dunning, downgrade rules, comparison pages.
- **Email channel** complete (Gmail/Microsoft 365 OAuth, forwarding, custom SMTP, custom domains with SPF/DKIM/DMARC, CC/BCC, outbound compose).
- **WhatsApp** (complete, including media and templates).
- **Shopify app** (OAuth, theme app embed, orders in the sidebar, compliance webhooks).
- Slack/Teams/Discord notifications; outbound webhooks (retries, logs, replay); public REST API v1 + API keys + OpenAPI docs (`/docs/api`).
- **Tickets, SLA policies, customer portal, contact form, side conversations, merge/split** (6.4.1).
- **Inboxes (sub-inboxes)**, triage rule builder, routing + auto-assign, office hours, reminders, automations (time-based), AI-free spam filter v1.
- **Analytics** (6.10): report builder, shared dashboards, SLA, agent activity, raw exports.
- CSAT, proactive triggers, live visitors list + map, and the widget extras from 16.1 (dark mode, GIFs, voice notes, cookieless mode, vacation mode, other-channel buttons, email detection, block rules).
- GA4/GTM events, file attachments on all channels, integration sidebar widgets. E2E tests 3 and 4.

**Phase 3: Knowledge base, AI & e-commerce**
- Knowledge base editor + public help center (custom domains, visibility levels, versions, importers, AI translation) + widget article search + AI site-search overlay.
- AI copilot (suggest reply, rewrite, translate, summarize, auto-tag/sentiment, voice-note transcription).
- AI agent with sources + RAG + handoff + playground + **simulations** + observability.
- **AI actions** (built-ins, Action builder, external MCP servers as tools, browser tools, approvals).
- Learning from past conversations, knowledge gap detection, **AI QA**, **predicted CSAT**, **topic clustering**.
- Chatbot builder + templates.
- **E-commerce suite** (6.8.11): order actions, cart preview, AI shopping assistant, revenue attribution.
- Model choice (incl. EU-hosted), AI metering, per-conversation caps, "AI live in 5 minutes" setup.

**Phase 4: Growth, more channels & scale**
- Campaigns (one-off + automated); segments, CSV import/export, companies, contact merging UI.
- Messenger, Instagram, Telegram, LINE, Viber, X DMs, SMS, Amazon Messages, Klaviyo replies; **Slack Connect / Teams / Discord as support channels**; Slack app (reply from Slack); custom channel API.
- **Multi-brand workspaces.**
- HubSpot, Salesforce, Pipedrive, Zoho, Dynamics 365, Mailchimp, Klaviyo, Segment, PostHog, Mixpanel, Amplitude, Brevo, ActiveCampaign, Jira, Linear, GitHub, Trello, Notion, Stripe, Calendly/Cal.com, Zapier app, Make, Dialogflow.
- WooCommerce, PrestaShop, Magento and WHMCS modules; WhatsApp commerce + Embedded Signup.
- **Read/write MCP server**; data warehouse sync.
- Partner/agency program, startup/nonprofit/open-source programs.
- Super-admin back office with the trust & safety queue.
- Custom roles, passkeys, SOC 2 readiness (Vanta/Drata), 30+ languages.

**Phase 5: Parity+ and enterprise**
- Status page product; audio/video calls + screen share; co-browsing.
- **Phone channel + AI voice receptionist**, plus Aircall/Ringover.
- Native operator apps (Expo iOS/Android with AI copilot) and desktop apps (macOS, Windows, Linux); native chat SDKs (iOS, Android, React Native, Flutter).
- SSO SAML/OIDC + SCIM, audit log UI, HIPAA option, multi-region data residency.
- Importers (Intercom/Zendesk/Crisp/Freshchat/tawk.to); realtime API + official API libraries.
- **App Marketplace for third-party developers**; standalone AI agent for other helpdesks; self-hosted Enterprise edition.

---

## 13. Crisp's gaps and how Parlo wins (build these into the phases, they are requirements, not ideas)

These come from real user reviews (G2, Capterra, GetApp, Trustpilot, Shopify App Store, Google Play, Product Hunt, Reddit) and competitor analysis, researched in October 2026. **Re-verify them in Phase 0** (section 13.4).

### 13.1 Where Crisp is strong (match these, don't fall behind)
- **EU data hosting** and a privacy-first image → offer **EU and US regions** from day one (choose at signup), list sub-processors publicly, and keep the AI on EU-hosted models for EU workspaces when possible.
- **Very light, fast widget** (tiny main-thread cost) → our budget: < 35 KB gzipped, < 40 ms main-thread time, measured in CI with Lighthouse on a test page.
- **Live translation, co-browsing, an MCP server, and AI "widget tools"** (the AI performs actions on the site) → all are in our spec (6.7, 6.13, 6.15). Ours must be better (13.3).
- **Responsive human support** → offer in-app chat support on every paid plan, run by the founders on Parlo itself.

### 13.2 Crisp's top weaknesses → our required answer

| # | Crisp weakness (what users complain about) | Parlo's required answer |
|---|---|---|
| 1 | **Price cliffs**: plans were repackaged (a 4-seat plan went from $25 to $45; a plan went from 20 to 10 seats), there is a hard seat cap, and big jumps between tiers ($95 → $295) | Extra seats on **every** plan, no tier cliffs (6.12), a public **price-lock promise**: "your price won't change for 24 months; existing customers are grandfathered", and a public pricing changelog |
| 2 | **AI credits run out and the bot silently stops**; unused credits expire; credits are consumed while testing the trial; real cost is unpredictable | Resolution-based pricing with included volume, **rollover, spend caps and 80/100% alerts**, testing in the playground/simulations is **never billed**, and a clear AI cost calculator (6.12) |
| 3 | **Reliability**: replies not delivered, unstable notifications, duplicate conversations, glitchy app | **Delivery guarantee**: every message has sent → delivered → read states, automatic retries, and a visible alert to the operator on failure. A **notification health check** in settings (test push/email/sound). A **backup alert** (email/SMS) when a chat waits longer than X minutes with nobody online. **Automatic dedupe/merge** of duplicate conversations and contacts. Published uptime and latency targets, plus a public status page |
| 4 | **Core features locked behind expensive tiers** (knowledge base, WhatsApp/social channels, branding removal, ticketing) | All channels + knowledge base + branding removal on the **cheapest paid plan** ($29); a generous Free plan (6.12) |
| 5 | **Shallow reporting**: topline only, no SLA breakdown, no transcript/CSV export, no agent activity, private dashboards | A **report builder** with shared dashboards. **SLA reports**. **Agent activity** (online/away/idle time, handled vs resolved, response times). Conversation-level drill-down. **Raw export** (CSV/JSON/Parquet) of conversations, messages and contacts. A **warehouse sync** (S3, BigQuery, Snowflake) on Scale. Scheduled email reports |
| 6 | **AI quality**: off-topic answers, weeks of tweaking, the AI does not learn from past conversations, weak copilot | (a) **Opt-in learning from past resolved conversations** (reviewed and approved before use). (b) **Simulations**: run the AI against 50+ real past questions and score it before going live. (c) **Knowledge gap detection** that drafts missing articles for approval. (d) **Confidence-based handoff**. (e) Answers with **citations**. (f) An "AI went live in 5 minutes" guided setup: paste your URL → crawl → test → publish |
| 7 | **Unexplained account suspensions**, slow vendor support, account deletion only via a GDPR request | A **written trust & safety policy**: automated systems may only *throttle*; **suspension requires human review**, a written reason and an appeal path. **Self-serve data export and account deletion** in settings. A guaranteed human first response time on paid plans |
| 8 | **Mobile app quality**: missed notifications, crashes, no AI on mobile | Operator mobile app (PWA first, native Expo app in Phase 5) at **feature parity** with the web inbox, **including AI copilot**, reliable push with fallback email/SMS, and offline drafts |
| 9 | **Thin helpdesk**: no real tickets/SLA, no merge/split, no mark-as-unread, weak long-running conversations | **Tickets** (6.4.1): ticket types, SLA policies with business hours and breach alerts, merge/split, **side conversations** (email a supplier from inside a conversation), linked tickets, **mark as unread**, and a **customer portal** where customers see their tickets |
| 10 | **No native phone / AI voice** | **Phone channel** (Twilio/Telnyx numbers): calls ring in the browser and the app, voicemail with transcripts, and an **AI voice receptionist** using the same knowledge base and actions, with transcripts in the inbox (Phase 5) |
| 11 | **Shallow e-commerce** (Shopify is just an integration; no order actions, no revenue attribution) | **E-commerce suite** (6.8.11): order lookup, **actions with guardrails** (refund under $X, cancel, edit address, resend, discount code) from both the inbox and the AI agent, **cart preview**, product recommendations, an **AI shopping assistant**, and **revenue attribution** per conversation and per AI reply |
| 12 | **Per-workspace billing punishes multi-brand teams and agencies** | **Multiple brands inside one workspace** (separate widget, help center, email address, branding and reports per brand) plus the agency program (6.12) |
| 13 | **Compliance gaps** (no SOC 2 audit, no visible HIPAA BAA, limited SSO) | **SOC 2 Type II readiness from day one** (controls, policies, evidence collection via Vanta/Drata in Phase 4), a HIPAA-ready option with BAA (Enterprise), SAML + SCIM on Scale, audit logs, configurable retention |
| 14 | **Lock-in**: the AI only works inside Crisp, no self-hosting | **Full data portability** (export everything, documented import/export formats), a **read/write MCP server**, the **AI agent available standalone** on top of other helpdesks (Zendesk/Freshdesk/Help Scout connectors, Phase 5), and an optional **self-hosted Enterprise edition** (Docker/Helm) |
| 15 | **Cluttered UI, hard triggers/bots, weak search** (can't find exact order IDs) | An opinionated, calm default inbox. **Templates** for bots/triggers/campaigns. **Exact-match + full-text search** with filters (quotes for exact phrases, order IDs, emails, phone numbers). Contextual help and a product tour. Usability test every main flow (section 14) |

### 13.3 "Beat them" features (all required, placed in phases in section 12)
1. **Capped, resolution-based AI pricing** with verified resolutions (6.12).
2. **AI actions library** (6.7): track order, refund/cancel/edit order (Shopify/WooCommerce/Stripe), reschedule booking, update billing details, create ticket, call any customer API via an **"Action builder"** (HTTP request + auth + input schema). Approval thresholds and a human-approval queue for risky actions.
3. **AI QA**: automatically score 100% of human and AI conversations (tone, accuracy, resolution, policy compliance) with a coaching view per operator.
4. **CSAT without surveys**: an AI-predicted satisfaction score for every conversation, alongside the real CSAT.
5. **Topic clustering in every language**: see what customers ask about this week, trending issues, and spikes with alerts.
6. **Live two-way translation** (the operator writes in their language; the customer reads theirs) on every channel, including email and WhatsApp.
7. **Revenue attribution and an AI shopping assistant** for stores.
8. **WhatsApp commerce**: product catalogs, template broadcasts to opted-in contacts, and click-to-WhatsApp ads tracking.
9. **B2B support channels**: **Slack Connect** shared channels, **Microsoft Teams** and **Discord** as inbound channels (not just notifications), for B2B SaaS customers (Phase 4).
10. **Read/write MCP server** with OAuth, so customers' own AI agents (and Claude/ChatGPT) can read conversations, reply, tag and look up contacts safely (Phase 4).
11. **Delivery guarantee + backup alerts** (13.2 #3).
12. **Multi-brand workspaces** (13.2 #12).
13. **Real ticketing + customer portal** (13.2 #9).
14. **Agent activity & light workforce management**: schedules, shifts, capacity, and auto-away when idle.
15. **Data warehouse sync + raw exports** (13.2 #5).
16. **2-minute setup**: detect the platform from the website URL during onboarding, show tailored one-click instructions, and a live "installation detected ✅" check.
17. **"Paste your URL → AI agent live in 5 minutes"**: crawl, auto-generate FAQ snippets, simulate, publish.
18. **Weekly AI insights email for owners**: volume, response times, CSAT, top topics, knowledge gaps with drafted articles to approve in one click.
19. **Delightful details**: a command palette, a keyboard-first inbox, smart snooze, "undo send" (5s), message scheduling, and emoji reactions on messages.
20. **Price-lock promise and transparent public pricing changelog.**

### 13.4 Do your own competitive research (Phase 0, then before every phase)
If you can browse the web:
1. Read crisp.chat (features, pricing, integrations, changelog/blog) and the main competitors (Intercom/Fin, Tidio, tawk.to, Chatwoot, Zendesk, Freshchat, Gorgias, Help Scout, Front, LiveChat).
2. Read recent reviews (G2, Capterra, Trustpilot, Reddit, Shopify App Store).
3. Update `docs/COMPETITIVE_ANALYSIS.md` with: the feature parity table (section 16), new competitor features, and new complaints.
4. Add any feature Parlo is missing to the parity checklist **and** to the right phase. Tell the founder in the phase report what you added and why.

If you cannot browse, use sections 13 and 16 as the source of truth.

After Phase 5, write `docs/IDEAS.md` with 10 more prioritized ideas (impact vs effort) and implement the top 3.

---

## 14. Definition of Done (for every phase)

Before saying a phase is finished, you must:
1. Have implemented **every** item listed for that phase, end to end (DB → API → UI → tests), with no placeholders.
2. Pass `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm build` and `pnpm e2e` with 0 errors.
3. Have started the full stack locally (`docker compose up` + `pnpm dev`), clicked through every new flow in a real browser on desktop and mobile widths, and checked that there are no console errors or broken layouts. Also walk each new flow as a **first-time user** (usability check): clear labels, helpful empty states that say what to do next, no dead ends, and no step that needs reading the docs.
4. Have run the security checklist (section 10) for the new code.
5. Have ticked every row of `docs/PARITY.md` (section 16) and every 13.2/13.3 item assigned to this phase, and enforced the right plan limits for every new feature through the entitlements engine.
6. Have updated README, ARCHITECTURE, DECISIONS, CHANGELOG, `.env.example` and the `SETUP_*.md` docs.
7. Have committed with clear messages.
8. Post a **phase report** in this format:
   - ✅ What was built (bullet list mapped to this prompt's sections)
   - 🧪 Test results (counts, all green)
   - ▶️ How to run and what to click to see it working
   - 🔑 Credentials/accounts the founder must create for real-world use (with links to the SETUP docs)
   - ⚠️ Known limitations / decisions taken
   - 📊 Parity status (rows done / total) and competitive findings from 13.4
   - ⏭️ What the next phase will do

## 15. Start now

1. Restate in 10 bullet points what you are going to build (to prove you understood), including the freemium model.
2. If you can browse the web, do the competitive research in 13.4 and list anything new you found.
3. Print the final repository tree for Phase 0 + Phase 1.
4. Begin **Phase 0**, then continue straight into **Phase 1**. Stop only when Phase 1 meets the Definition of Done, and post the phase report.

---

## 16. Appendix: Crisp feature parity checklist (every row is a requirement)

Copy this table into `docs/PARITY.md` in Phase 0 and tick rows off as you build them. "✚" means Parlo must do **better** than Crisp, as described. Research date: October 2026 (Crisp's own changelog, help center, developer docs and GitHub). Phase numbers refer to section 12.

### 16.1 Chat widget
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| Launcher, welcome message, left/right position, colors, z-index | 6.3 customization with live preview ✚ (logo, launcher icon, brand per site) | 1 |
| 60+ languages, locale overrides, automatic right-to-left text | i18n framework + 6 languages at launch, then 30+ via translation files; auto RTL; per-workspace text overrides | 1 → 4 |
| Dark mode widget | Widget follows the visitor's system theme, or forced light/dark | 2 |
| Hide when away / hide on mobile / vacation mode / availability tooltip | All four settings | 2 |
| Lock maximized/full view, "safe mode" (CSS-conflict-proof) | Full-screen mode option; Shadow DOM makes safe mode the default ✚ | 1 |
| Session continuity across devices (`tokenId`), session merge | `$parlo.push(["set","user:id", [id, signature]])` restores the same conversations on any device; anonymous sessions merge on identify | 1 |
| Cookie domain & expiry; **total privacy / cookieless mode** | Cookie settings + a cookieless mode (memory/localStorage only, no tracking of page history) | 2 |
| Text, files, images, emoji, quick replies, buttons/pickers, carousel, input fields | 6.3 + bot cards (6.7) | 1 / 3 |
| **GIFs** and **audio messages** (record voice notes) | GIF picker (Tenor/Giphy, can be disabled) + voice notes with AI transcription shown to operators ✚ | 2 |
| Contact form (when away, or as an alternative to chat) | "Send us a message" form that creates a ticket | 2 |
| Show other channels in the chatbox | Buttons to continue on WhatsApp, Messenger, Instagram, Telegram, email or phone | 2 |
| Detect & confirm email typed in a message | "Is this your email? ✓" chip that saves it to the contact | 2 |
| Message triggers (open chatbox, show message, play sound, change quick replies) | 6.3 proactive triggers with templates ✚ | 2 |
| **MagicType** (see what visitors type) | Live typing preview (6.3 / 6.4) | 1 |
| **MagicMap** (live map of visitors) + visitor list & count | "Live visitors" page: list + world map of visitors on the site right now, with current page, source, and a "Start chat" button (proactive outbound message) | 2 |
| Ratings (1–5 + comment) in chatbox and transcript emails | CSAT (6.3) + predicted CSAT ✚ | 2 / 3 |
| Email transcripts (automatic/manual) | Transcript email on resolve (setting) + manual send | 1 |
| Knowledge base search in widget; Overlay full-page AI site search | KB tab (6.6) + optional full-page "Ask AI" search overlay for the customer's site | 3 |
| Widget homepage, launch AI from widget | Home tab (6.3) with AI entry point | 1 / 3 |
| Identity verification (HMAC) | 6.3 identity verification | 1 |
| Block visitors with rules | Block by IP range/country/email/domain/keyword; blocked visitors see the widget as away | 2 |
| Widget Tools (AI runs actions in the visitor's browser) | `$parlo.push(["on","ai:tool:<name>", handler])`: the site registers browser-side tools the AI can call (e.g. open cart, fill form, navigate) ✚ with a typed schema | 3 |
| Chat SDKs: web, iOS, Android, React Native, Flutter | Web SDK (1); native SDKs (5) | 1 / 5 |

### 16.2 Inbox
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| Shared inbox, states unresolved/pending/resolved | open / pending (waiting on customer) / snoozed / resolved | 1 |
| Manual & automatic assignment, routing rules | 6.4 routing + round-robin/least-busy + capacity ✚ | 2 |
| **Sub-inboxes** with their own members & access rules | **Inboxes** (e.g. Sales, Support, Billing): each with members, permissions, channels and routing; operators see only inboxes they belong to | 2 |
| Triage rules (route by data, body, origin; block; set segments; AND/OR; email subject/"to") | Rule builder with AND/OR groups on any field (message text, channel, email to/subject, page, country, segment, custom data) → actions (route, assign, tag, priority, block, segment, auto-reply, close as spam) | 2 |
| Private notes, @mentions, participants/CC, reminders | Notes + mentions (1); email CC/BCC participants (2); **reminders** ("remind me about this conversation tomorrow at 9") (2) | 1 / 2 |
| Shortcuts (canned replies), keyboard shortcuts, filters, segments, search | 6.4 saved replies `/`, shortcuts, views, exact + full-text search ✚ | 1 |
| Rich editor with blocks, embeds, RTL, date separators, jump to date | Composer with markdown, code blocks, images, link embeds, RTL; thread with date separators and "jump to date" | 1 / 2 |
| Automations inbox (AI-handled work) + Review Mode + report good/bad AI answers | "AI" view listing every AI-handled conversation, a review queue with 👍/👎 and "correct the answer" that becomes a snippet ✚ | 3 |
| Spam filter (AI) + spam decisions | AI spam classifier on inbound chat/email, spam folder, "not spam" feedback, auto-block repeat spammers | 2 |
| Batch actions (resolve, read, route, delete, tag), mark unread, block, report | All, in 6.4 bulk actions + mark unread | 1 / 2 |
| Sidebar: browsed pages, events, device, plugin widgets | 6.4 contact sidebar + integration widgets + marketplace app widgets (16.9) | 1 / 2 / 5 |
| LiveTranslate | 2-way live translation on every channel (6.7) | 3 |
| Email: forwarding from Gmail/Google Workspace/Outlook, custom sending domain (SPF/DKIM/DMARC), custom SMTP (e.g. SES), start outbound email | 6.8.5 + **direct Gmail and Microsoft 365 OAuth connection** (no forwarding needed) ✚ + custom SMTP + compose new outbound email | 2 |
| Custom channels via plugins | Custom channel API: any developer can push inbound messages and receive outbound replies through webhooks (16.9) | 4 |

### 16.3 CRM / contacts
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| Profiles with company & job data, custom data, past conversations | 6.5 contacts + companies + job title | 1 / 4 |
| Segments (incl. AI-assigned segments) | Rule-based segments + AI auto-segmenting (e.g. "lead", "churn risk") | 4 / 3 |
| Events timeline with colors | Custom events via SDK/API with icon/color on the timeline | 2 |
| Geolocation, device info, email subscription status | 6.5 + marketing consent status (subscribed/unsubscribed/bounced) | 1 / 4 |
| CSV import/export, contact statistics | 6.5 import/export + stats (contacts by country/source/segment) | 4 |
| Two-way CRM sync (HubSpot etc.) | 6.8.10 HubSpot + Salesforce, Pipedrive, Zoho CRM, Dynamics 365 | 4 |

### 16.4 Knowledge base
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| Multilingual + **automatic translation from a reference language** | 6.6 + one-click AI translation of articles, kept in sync when the source changes ✚ | 3 |
| Custom domain, SEO, feedback, categories & sections | 6.6 | 3 |
| **Import from other providers**, export, redirects | Importers (Zendesk Guide, Intercom Articles, Help Scout Docs, HTML/Markdown zip), export, 301 redirect manager | 3 |
| Password/JWT-protected internal knowledge base | Visibility per article/category: public, logged-in customers (JWT/SSO), internal (operators only) | 3 |
| Folders, drag & drop, version history with rollback | Editor with tree navigation, drag & drop ordering, version history + diff + rollback | 3 |
| Turn closed conversations into articles | Knowledge gap detection + "Create article from conversation" (6.7) ✚ | 3 |

### 16.5 Chatbots & automation (Crisp "Workflows")
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| No-code builder (events, actions, conditions, AI handoff) | 6.7 visual chatbot builder | 3 |
| Per-channel flows, start manually, start from the SDK | Flow triggers include channel, operator "Run flow" button, `$parlo.push(["do","flow:run",["id",{vars}]])` | 3 |
| Templates (out-of-office, drip sequences…) | 20+ templates (lead qualification, out-of-office, order status, booking, feedback, onboarding drip) | 3 |
| Dialogflow connector | Generic "external bot" connector (webhook) + Dialogflow | 4 |
| Task automations | "Automations": when X happens → do Y (time-based too, e.g. auto-close after 3 days pending, SLA escalation) | 2 |

### 16.6 AI (Crisp "Hugo")
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| AI agent on web chat, WhatsApp, Messenger, Instagram, email | 6.7 AI agent on **every** channel, including voice (6.8.12) ✚ | 3 / 5 |
| Training: crawl, KB, files (PDF/CSV/TXT), Q&A snippets, guided instructions | 6.7 sources + DOCX/Notion/Google Docs ✚ + guided setup | 3 |
| Guardrails, escalation, routing to flows/humans, topic detection | 6.7 guardrails + confidence handoff + topics | 3 |
| Playground, observability & debugging, setup reviews | Playground + **simulations** ✚ + per-answer trace (sources, tools called, latency, cost) | 3 |
| External MCP servers as AI tools (with email/SMS OTP identity checks) + Widget Tools | AI actions (6.7): built-ins, Action builder, **external MCP servers as tools**, browser tools, OTP identity check, approval queue ✚ | 3 |
| Personalization (segments, custom data, location, device) | AI answers use contact profile, segments, custom data, order data | 3 |
| Model choice (OpenAI, Anthropic, Google, Mistral, EU-hosted model) | Provider-agnostic layer (3); workspace can choose the provider/model, including an EU-hosted option | 3 |
| Copilot: summarize, draft replies, handover notes, citations; writing assistant; auto-tagging; audio transcription | 6.7 copilot (all) ✚ + copilot on mobile | 3 |
| Per-conversation AI spend cap | Per-conversation cap + monthly spend cap (6.12) | 3 |
| AI key metrics dashboard, escalation rate, "saved time" | AI analytics: resolution rate, escalation rate, saved time, cost, top unanswered topics | 3 |
| *(Crisp lacks)* learning from past conversations, AI QA, predicted CSAT, multilingual topics, AI shopping assistant | 6.7 / 6.8.11 ✚ | 3 |

### 16.7 Campaigns, status page, analytics
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| One-off & automated campaigns by chat or email, segment targeting | 6.9 | 4 |
| HTML templates + visual builder, variables, event data in subject/body | 6.9 block editor + raw HTML mode + variables incl. event data | 4 |
| Test send, pause/resume, recipient list, stats (open/click/unsubscribe) + export | 6.9 + pause/resume + recipient list + export | 4 |
| Status page: HTTP/S, TCP, ICMP checks, push reporters (Node/Go/Rust/Python), local agent for internal hosts, nodes, thresholds, custom domain, announcements, alerts (apps, Pushover) | 6.15 status page with all of these + alerts by email/SMS/Slack/push and **incident updates posted automatically to the widget** ✚ | 5 |
| Prebuilt reports, custom dashboards (summary, chart, articles, map, heat map, operators, rating), split by office hours, filters | 6.10 report builder with all chart types incl. map and heat map, office-hours split | 2 |
| Dashboard export/import, templates, shared dashboards | 6.10 shared dashboards + JSON export/import + templates | 2 |
| *(Crisp lacks)* raw transcript/CSV export, SLA reports, agent activity, warehouse sync | 6.10 ✚ | 2 / 4 |

### 16.8 Team, security, apps, channels
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| Roles Owner/Admin/Member, operator teams, availability, last active | 6.2 Owner/Admin/Agent + Teams + **custom roles** (Scale) ✚ | 1 / 4 |
| Multiple workspaces | 6.2 + **multiple brands per workspace** ✚ | 1 / 4 |
| 2FA (authenticator app or SMS) | TOTP (1) + SMS/WebAuthn passkeys ✚ (4) | 1 / 4 |
| EU hosting, GDPR + DPA, cookieless mode, EU AI model option | EU/US regions, DPA, cookieless mode, EU model option | 1 / 2 / 3 |
| *(Crisp lacks)* SOC 2 audit, HIPAA BAA, SAML/SCIM | 13.2 #13 ✚ | 4 / 5 |
| Web app, desktop (macOS, Windows), iOS & Android apps with push | PWA (1); native mobile (Expo) + desktop for macOS, Windows **and Linux** ✚ (5) | 1 / 5 |
| Channels: web chat, in-app chat, email, WhatsApp, Messenger, Instagram (incl. story replies), X/Twitter DMs, Telegram, LINE, Viber, SMS (Twilio), Discord, Slack, phone (Aircall/Ringover), Klaviyo replies, Amazon buyer messages, contact form, ticket portal, custom channels | Web chat + email (1/2); WhatsApp (2); Messenger, Instagram incl. story replies/mentions, Telegram, LINE, Viber, X DMs, SMS, Discord, Slack Connect, Teams, Klaviyo replies, Amazon Messages, custom channels (4); native phone + Aircall/Ringover (5); contact form + customer portal (2) | 1–5 |

### 16.9 Developer platform & marketplace
| Crisp feature | Parlo requirement | Phase |
|---|---|---|
| REST API with token tiers (user / website / plugin), dev vs prod tokens, scopes | 6.13 API keys with scopes + OAuth apps for third-party developers + test-mode keys | 2 / 5 |
| RTM (realtime WebSocket) API | Realtime API (6.13) | 5 |
| Web hooks (website hooks + plugin hooks) | 6.8.8 webhooks with retries, logs, replay ✚ | 2 |
| API libraries: Node, Go, PHP, Python, Ruby | Official SDKs generated from OpenAPI: Node/TypeScript, Python, PHP, Go, Ruby | 5 |
| **Plugin marketplace** for third-party developers (sidebar widgets defined in JSON, plugin settings, paid plugins with usage-based billing) | **Parlo App Marketplace**: developers register OAuth apps; apps can add inbox sidebar cards (JSON UI kit), settings pages, custom channels, AI actions; listed in the integrations marketplace; paid apps with revenue share | 5 |
| MCP server | Read **and write** MCP server with OAuth ✚ (6.13) | 4 |
| Conversation importer | Importers from Intercom, Zendesk, Crisp, Freshchat, tawk.to (CSV/API) | 5 |
| Status reporters (Node/Go/Rust/Python) | Push reporters in Node and Python + generic HTTP push endpoint | 5 |

# ===================== PROMPT END =====================
