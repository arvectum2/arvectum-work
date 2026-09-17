# AW-010 — Russia market and substitute map

Status: `Public-source evidence / first map`
Observed: `2026-09-17`
Task: `AW-010-A-MARKET-MAP`

## 1. Purpose and evidence boundary

This artifact maps current Russian substitutes for buying or automating bounded knowledge/operations work. It is not a competitor ranking and does not claim that Arvectum Work has product-market fit.

The sampled market currently separates into four broad mechanisms:

1. **human freelance/service marketplaces** — buyer purchases a task/result from a human seller;
2. **B2B contractor infrastructure** — company finds, documents and pays external human executors;
3. **AI-agent / model platforms** — company builds or operates its own AI solution;
4. **RPA / AI implementation and managed automation** — company buys software, integration or a custom automation project.

Arvectum Work's thesis sits between these mechanisms: purchase of a verifiable result produced by an autonomous digital Executor, while legal/economic responsibility stays with a Principal. This remains a hypothesis to validate with paid transactions.

## 2. Human freelance and service marketplaces

### Kwork

Observed facts:

- Kwork has categories for parsers, scripts, machine learning, AI agents and AI bots, alongside research/data tasks.
- Its terms define explicit buyer acceptance: after delivery the buyer has a review period; acceptance also occurs if the buyer does not return the order for revision or open a dispute within the defined period.
- Payment handling/holding is performed by partners under their offers rather than by Kwork itself according to the current terms.
- Public listings expose packaged result/price examples; one observed parsing offer was `500 RUB` for a declared volume.

Packaging model: packaged freelance service / result offered by a human seller.

Acceptance signal: buyer confirmation, revision/dispute window.

Settlement signal: protected payment contour via partners.

Sources:

- https://kwork.ru/categories
- https://kwork.ru/terms_of_service
- https://kwork.ru/information-bases/53160912/parsing

### FL.ru

Observed facts:

- FL.ru operates a freelance marketplace and offers `Безопасная сделка` with refund protection when an executor fails or misses the deadline.
- Public service cards can expose a concrete scope, delivery time, result and price.
- Example observed 2026-09-17: a public parsing service priced at `2,990 RUB`, two-day delivery, up to 1,000 records / 10 fields in the base scope, with sample checking and one correction iteration.

Packaging model: human freelance service, including clearly bounded output packages.

Acceptance signal: safe-deal completion/refund logic plus seller-specific scope/revision terms.

Sources:

- https://www.fl.ru/promo/bezopasnaya-sdelka/
- https://www.fl.ru/uslugi-freelancera/31039/soberu-dannye-s-sayta-v-excel-csv-ili-google-tablicu.html

### Workzilla

Observed facts:

- Workzilla exposes task categories including data/product parsing.
- Its public task pages state that executor compensation is reserved after assignment and released after task confirmation.
- The platform markets continuous task availability and uses an AI system to help match executors to tasks.

Packaging model: posted task matched to a human freelancer.

Acceptance signal: customer confirmation before payout.

Settlement signal: reserved remuneration / protected payment flow.

Sources:

- https://work-zilla.com/freelance-jobs/development-and-it/parsing
- https://work-zilla.com/freelance-jobs/development-and-it/parsing/parsing-of-data-or-products

## 3. B2B contractor / outsourcing infrastructure

### YouDo Business

Observed facts:

- YouDo Business positions itself as a platform for finding and working with self-employed/external human executors, including contracts/documents, checks and payouts.
- The public site states that organizations can find executors through the YouDo marketplace or use mass recruitment.
- Current public tariffs include a free/start contour and a `Про` tariff shown at `15,000 RUB/month` for a single legal entity and `20,000 RUB/month` for groups of companies where the stated commission condition applies.
- The payment-automation page states support for transfers to Russian bank accounts and SBP.

Packaging model: contractor sourcing + compliance/document/payment operations, not machine execution.

Acceptance signal: project/task management exists, but the sampled public pages emphasize contractor administration rather than machine-checkable result acceptance.

Sources:

- https://b2b.youdo.com/poisk-vneshtatnogo-personala
- https://b2b.youdo.com/samozanyatye
- https://b2b.youdo.com/payment-automation
- https://b2b.youdo.com/tariffs

## 4. AI-agent / model platforms — build rather than buy the result

### Yandex AI Studio

Observed facts:

- Yandex AI Studio is a Yandex Cloud platform for building AI applications and AI agents from experimentation through production use.
- It includes Agent Atelier, search tools, MCP Hub, workflows/API integration and documented access controls/quotas/tarification.
- Current 2026 documentation describes AI Studio agents connected into workflows, with tool confirmation controls (`auto_approve` is not the default).
- Yandex publicly describes research agents and MCP-based automation of routine work.

Packaging model: infrastructure/platform for the customer or integrator to build and operate agents.

Acceptance signal: technical workflow/tool controls; not a marketplace acceptance/settlement model for external Jobs.

Sources:

- https://yandex.cloud/ru/docs/ai-studio/
- https://yandex.cloud/en/docs/serverless-integrations/concepts/workflows/yawl/integration/aistudioagent
- https://yandex.cloud/ru/blog/web-search-update-july-2026
- https://yandex.cloud/ru/blog/mcp-yandex-ai-studio-ai-agents-automation

### GigaChat API / GigaChain

Observed facts:

- GigaChat exposes API/model access and agent-building examples, including MCP-connected agents and tool/function use.
- For legal entities the public tariff documentation supports token packages and pay-as-you-go with RUB prices and VAT; from `2026-09-01`, new-client model payments are directed to cloud.ru according to current documentation.
- Example current pay-as-you-go generation prices published for existing legal-entity clients include `0.065 RUB / 1,000 tokens` for GigaChat Lite synchronous usage, with higher prices for Pro/Max and lower asynchronous prices.

Packaging model: model/API input cost and developer tooling; customer still needs to construct, govern and operate the solution.

Acceptance signal: API/service-level technical consumption, not buyer acceptance of an externally assigned Job result.

Sources:

- https://developers.sber.ru/docs/ru/gigachat/tariffs/legal-tariffs
- https://developers.sber.ru/docs/ru/gigachain/tutorials/agent-gigachat-mcp
- https://developers.sber.ru/docs/ru/gigachat/guides/functions/overview

## 5. RPA and enterprise AI platforms

### PIX RPA

Observed facts:

- PIX RPA positions software robots and AI agents as digital employees for routine business processes.
- The platform includes Studio/Robot/Master/Runner and AI-agent orchestration, with workflow-controlled agents and detailed action logs.
- Public examples explicitly include document classification/comparison, orders, finance/accounting, IT operations and procurement/logistics.
- PIX reports `230+` deployments and `150+` implementation partners on its current public site; these are vendor claims, not independently verified market-share evidence.

Packaging model: software platform + implementation ecosystem.

Acceptance signal: process logs, customer implementation/project acceptance; no public per-Job marketplace settlement mechanism observed in this sample.

Sources:

- https://pix.ru/products/pix-rpa/
- https://pix.ru/partnership/

### Naumen Erudite

Observed facts:

- Naumen Erudite is positioned as a platform for AI assistants and autonomous AI agents in customer service and sales.
- Public packaging is demo/contact-led; no comparable per-task public price was observed in the sampled source.

Packaging model: enterprise software/platform deployment.

Source:

- https://www.naumen.ru/products/erudite/

## 6. AI implementation studios / custom development

This category is especially important because it represents the buyer alternative identified in the Work hypothesis: commission a custom AI solution rather than buy the repeated outcome.

### OfficeForge

Observed facts:

- Public offer: implementation of department-level AI agents, including customer-server deployment and access/logging controls.
- Open hourly rates were observed at `2,500–3,500 RUB/hour` depending on work type.
- The commercial unit is engineering/integration time and project deliverables, not an independently tradable repeated machine Job.

Source:

- https://officeforge.ru/services/ai-agents

### Rippa Digital

Observed facts:

- Public package: pilot `from 150,000 RUB` for one agent/one task over two weeks; full implementation `from 450,000 RUB`; support `from 25,000 RUB/month`.
- The described process includes task analysis, pilot, integration, acceptance report and ongoing support.

Packaging model: custom agent development / implementation project.

Source:

- https://rippa.ru/ru/services/ai-agents

Additional current examples of the same substitute category include Promolytica, Nord Clan, MotifAI, EORA and other Russian integrators. They are useful for later pricing/sample expansion but are not required to interpret this first map.

## 7. Observed structural comparison

| Substitute mechanism | What the buyer primarily purchases | Who/what performs work | Acceptance / proof signal | Price unit visible in public sample | Main friction relative to Work hypothesis |
|---|---|---|---|---|---|
| Kwork / FL.ru / Workzilla | bounded freelance task/result | human freelancer | buyer confirmation, dispute/revision/safe-deal rules | per service/task | executor is human; machine provenance/capability history is not the unit |
| YouDo Business | access to/manage external human workforce | human contractor | contractor/project administration | platform/month + payment/service economics | solves workforce/legal ops, not autonomous machine execution |
| Yandex AI Studio / GigaChat | AI/model capability and tooling | customer's/integrator's software/agent | API/workflow/technical controls | tokens/cloud usage | buyer still builds/operates the solution |
| PIX / Naumen | enterprise automation platform | robots/agents within deployed solution | implementation/process controls and logs | quote/license/project | upfront implementation/platform commitment |
| AI studios/integrators | custom AI automation project | integrator-built agent/system | project/pilot acceptance | hours / pilot / implementation | buyer funds development before repeated outcome is proven |
| **Arvectum Work hypothesis** | **defined accepted work result + evidence** | **Human / AI / Software / Hybrid Executor** | **Job-specific frozen Acceptance + Evidence** | **per Job/result initially** | **must prove that buyers actually prefer and pay for this transaction form** |

## 8. Preliminary interpretation — hypotheses, not findings of product-market fit

### H-M1 — existing marketplaces validate transactional primitives, not machine-work demand

The sampled freelance platforms show that Russian buyers already understand task posting, assignment, result review, revision/dispute and protected payout. That reduces conceptual novelty for the transaction flow. It does **not** prove willingness to buy the same flow from an autonomous Executor.

### H-M2 — custom AI implementation is a real substitute cost anchor

Public AI-studio/integrator pricing demonstrates that a buyer can currently pay tens or hundreds of thousands of RUB to implement an agent. Work should test whether some buyers would rather pay repeatedly for a bounded accepted outcome without owning the implementation.

### H-M3 — Russian AI infrastructure reduces execution-supply risk but increases the build-vs-buy alternative

Yandex AI Studio, GigaChat, PIX and similar systems make autonomous/agentic execution increasingly accessible. This helps potential Executors but also lets capable buyers build internally. Work must therefore compete on transaction cost, verification, procurement/contract simplicity and economics — not merely access to an LLM/agent.

### H-M4 — B2B contractor/payment infrastructure is adjacent, not equivalent

YouDo Business shows market demand for Russian contractor onboarding, documents and RUB/SBP payout operations. It may be relevant as a benchmark for Principal/settlement ergonomics, but it does not establish the legal or product model for machine Executors.

## 9. Gaps for AW-010-B / AW-010-C

This map is not enough to pass AW-010. Next evidence must add:

- 30+ concrete public paid task/deal/substitute examples across job families;
- more comparable price points for J-01…J-07;
- observable acceptance/revision mechanisms for document extraction, data cleanup, monitoring and report-generation work;
- buyer-side evidence from AW-020 showing whether implementation alternatives are actually perceived as too slow/expensive;
- current-law/payment re-verification for any real transaction;
- explicit counterexamples where managed service/custom automation is clearly preferable to per-result machine work.

## 10. AW-010-A result

`COMPLETE AS MARKET MAP / NOT AW-010 GO`.

The public market contains strong substitutes around human freelance work, contractor administration, AI tooling and custom automation. The unproven question remains whether Russian buyers will purchase a separately priced, evidence-backed machine-executed result often enough to support a distinct transaction layer.
