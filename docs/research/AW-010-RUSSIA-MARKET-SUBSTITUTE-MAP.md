# AW-010-A — Russia market and substitute map

Status: `Evidence draft / public-source research`
Observed: `2026-09-17`
Task: `AW-010-A-MARKET-MAP`

## 1. Question

What do Russian buyers use today instead of buying a verified unit of machine work from an autonomous Executor?

This artifact maps current substitutes. It does **not** prove demand for Arvectum Work, select a winning wedge, or count vendor claims as buyer evidence.

## 2. Market structure observed

| Substitute class | Examples observed | What the buyer purchases today | Pricing / packaging evidence | Acceptance / trust mechanism | Relevance to Arvectum Work |
|---|---|---|---|---|---|
| Horizontal freelance marketplaces | Kwork, FL.ru | Human-delivered task/service result | Kwork defines a minimum service price of 500 RUB; FL.ru supports fixed-price service cards and project postings | Kwork: buyer prepays via payment partners, result is checked before release; FL.ru: customer accepts or returns for revision before freelancer receives fee | Strong evidence that Russian buyers already understand `task → result → acceptance → payout`, but executor is primarily human |
| Project / tender marketplace for professional services | Workspace | Agency/project delivery in digital services | Public marketplace/tender format; price usually depends on project proposal rather than atomic task | Selection via agency profiles/tender response; acceptance remains project/customer-specific | Shows B2B buyers already source external outcome delivery through marketplace mechanisms, but at agency/project granularity |
| AI-agent catalogs / software marketplaces | Aienter; pickTech AI-agent catalog | Access to an AI product, agent or vendor solution | Aienter exposes solution prices/starting prices; pickTech lists monthly subscriptions for many tools | Product ratings, demos, vendor claims and software trial rather than acceptance of one paid work result | Direct contrast: these sell tools/agents, not a transaction for a verified completed Job |
| AI-agent platforms / builders | SimpleOne GenAI, GigaChat API ecosystem, Ladcraft and similar products listed in current Russian catalogs | Software capability / agent platform for the buyer to configure or integrate | Predominantly subscription, platform or quote-based packaging; catalog examples begin from low-thousands RUB/month for SMB tools | Buyer validates the product/platform and then owns implementation/operation risk | Substitute when buyer is willing to buy infrastructure instead of a result; Arvectum Work hypothesis is that some buyers prefer the result itself |
| AI automation studios / custom implementation | UKLAD; development offers represented in current market listings | Custom AI agent implementation, integration, RAG, CRM/ERP automation | UKLAD publishes a basic-agent MVP from 250,000 RUB; another current Moscow service listing shows PoC/custom-agent development from ~122,400 / 459,000 RUB | Project scope, milestones, warranty/delivery review | Supports the hypothesis that current AI procurement often means buying development rather than buying one machine-executed outcome |
| Managed AI automation subscription | Ruaibot and similar managed automation offers | Recurring preconfigured automations with reporting/support | Ruaibot publicly lists packages at 1,800 / 5,000 / 19,000 RUB per month | Service monitoring, recurring reports and support | Important adjacent model: a viable Arvectum business may prove closer to managed machine-work service than to a two-sided marketplace |
| Task-capacity AI subscription | DAAP and similar agent-hosting offerings | A quota of agent tasks / hosted AI worker capacity | DAAP publicly lists PRO 7,900 RUB/month for 300 tasks/week and MAX 14,900 RUB/month for 600 tasks/week at observed promotional prices | Platform availability and quota, not customer-specific per-Job acceptance | Indicates buyers can already purchase machine capacity, but not necessarily verified outcome-by-outcome settlement |

## 3. Concrete evidence notes

### Kwork

Observed public terms on 2026-09-17:

- a `kwork` is a freelance service; minimum fixed price is stated as 500 RUB;
- buyer and seller agree order conditions including deadline, price and task;
- buyer funds the order in advance through payment partners;
- the order is accepted after buyer confirmation, or after the defined review period if no revision/dispute is opened;
- payments can include bank cards, SBP and settlement-account payment through partners;
- Kwork explicitly separates itself from the payment-partner role.

Source: https://kwork.ru/terms_of_service

**Observed pattern:** existing Russian marketplace semantics are already close to `Order → Delivery → Buyer check → Payout`, with a legal/payment intermediary contour around human service delivery.

### FL.ru

Observed public service rules on 2026-09-17:

- a fixed-price service has declared scope, deadline and price;
- customer pays before execution;
- freelancer confirms taking the order;
- result is delivered for customer review;
- customer either accepts or returns it for revision;
- after acceptance, freelancer receives the fee;
- legal entities/IP may pay by invoice/payment order and obtain closing documents when configured correctly.

Source: https://www.fl.ru/uslugi-freelancera/

**Observed pattern:** fixed outcome packaging and explicit acceptance are already normal buyer concepts. The unexplored question is whether the same model remains attractive when the material Executor is autonomous software/AI under a legal/economic Principal.

### Workspace

Observed 2026-09-17: Workspace positions itself as a platform connecting customers and agencies in digital services and operates a tender marketplace plus agency catalog.

Source: https://workspace.ru/

**Observed pattern:** B2B sourcing exists, but transaction unit is usually an agency/project rather than a small machine-executable Job.

### AI-agent catalogs and platforms

pickTech's current AI-agent catalog reports 110 evaluated agent products and many Russian vendors across support, voice, sales, marketing, HR, procurement and platform/builder categories. Public examples include monthly subscription prices for several products.

Source: https://picktech.ru/catalog/ai-agents/

Aienter currently exposes a catalog of hundreds of AI-agent solutions and visible starting prices for many cards.

Source: https://aienter.ru/catalog

**Observed pattern:** the Russian market already has supply discovery for AI products. This is **not** evidence of a market for tradable machine work, because the buyer still selects/buys a solution rather than posts an outcome and settles after verified execution.

### Custom AI implementation

UKLAD publishes a basic RAG/FAQ agent MVP from 250,000 RUB with a stated 2–4 week range.

Source: https://ukladai.ru/prices/

A current Moscow service listing for AI-agent automation publishes separate prices for audit, PoC, production agent, CRM/ERP integration and document/OCR work; production-agent development is listed from 459,000 RUB.

Source: https://avikey.ru/ai-agenty-dlya-avtomatizatsii

**Observed pattern:** a buyer may currently face a large implementation purchase even where the actual need is a recurring bounded work outcome. This is a hypothesis-generating contrast, not proof that the buyer would switch.

### Managed recurring automation

Ruaibot publishes monthly recurring packages: 1,800 RUB, 5,000 RUB and 19,000 RUB for increasing numbers of automations and monitoring/reporting features.

Source: https://ruaibot.ru/

**Observed pattern:** recurring managed automation is already sold as a service. This is a serious substitute and a possible operating-model pivot if marketplace matching never creates additional value.

### Task-capacity subscription

DAAP publishes plans framed partly as task capacity: 300 tasks/week and 600 tasks/week in its PRO/MAX tiers.

Source: https://www.daap.ru/

**Observed pattern:** machine task volume can already be packaged commercially, but observed packaging is subscription capacity rather than per-Job `Result + Evidence + Acceptance + Settlement`.

## 4. What is fact vs hypothesis

### Public-source facts observed

1. Russian marketplaces already support prepaid task/service transactions with explicit result acceptance and revision mechanics.
2. B2B buyers can already source agency/project work through digital tender/catalog platforms.
3. Russian AI supply is broad: catalogs include many agent products, builders and enterprise platforms.
4. Public prices span very different purchase models: hundreds/thousands of RUB for small services or subscriptions, to hundreds of thousands of RUB for custom AI implementation.
5. Managed recurring AI automation and task-capacity subscriptions exist as alternatives to custom development.

### Hypotheses requiring buyer evidence

1. Buyers will prefer buying a defined machine-executed result instead of buying an agent/platform/implementation.
2. `Result + Evidence + Acceptance` materially reduces trust friction versus ordinary freelance delivery.
3. Local/self-hosted execution creates enough value to affect purchase decisions.
4. B2B Russian legal/payment contours create a defensible moat rather than only operational complexity.
5. A two-sided marketplace will outperform a managed machine-work service.

## 5. Early strategic implications — not decisions

The public landscape suggests three distinct existing buying motions:

`buy human work` → freelance/service marketplaces;

`buy software/capability` → AI-agent products/platforms;

`buy implementation/managed automation` → AI studios and recurring managed services.

Arvectum Work is testing a fourth motion:

`buy a verifiable machine-executed result`.

That motion is not yet validated. The most important next evidence is therefore not another agent catalog comparison; it is concrete paid-task evidence and buyer interviews about recent work, current cost, acceptance and buying route.

## 6. Gaps for AW-010 continuation

This first map is sufficient for `AW-010-A` category coverage but not for AW-010 stage completion. Remaining evidence includes:

- 30+ concrete public task/deal/substitute examples;
- stronger coverage of document extraction/data cleanup/monitoring/research/code-task pricing;
- direct observation of current acceptance mechanisms by job family;
- official/current constraints relevant to B2B settlement and data locality for the actual model;
- counterexamples where custom implementation or human work is clearly superior.

No AW-010 `GO / PIVOT / STOP` conclusion is made here.
