# AW-020 — Top-3 synthetic commercial scenarios

Status: `Discovery modeling / synthetic / not an offer`
Date: `2026-09-17`

> All prices, volumes, setup costs and payback periods below are synthetic modeling assumptions. They are not current Arvectum commercial terms, customer quotes or validated unit economics.

## Purpose

Turn the vacancy-function scan into something commercially testable.

For each candidate compare:

1. employee/current operation;
2. employee + general-purpose AI;
3. Arvectum Work as paid recurring machine-work stream;
4. owned automation / agent as the high-volume alternative.

The goal is not to make Work win every comparison. The goal is to identify the customer-volume window where each option is rational.

---

## Scenario A — Primary documents / 1C reconciliation

### Observed labor pattern

Public vacancies commonly ask people to:

- receive UПД, ТОРГ-12, ТТН, acts and invoices;
- check completeness/correctness;
- reconcile against orders/system records;
- enter or prepare data for 1C;
- maintain missing-document / discrepancy lists.

Observed vacancy salary examples in the initial scan frequently fall around `80–150k RUB/month`, depending on scope and seniority.

### Synthetic customer

Wholesale company processes `8,000` primary documents per month.

Current operation:

- `2 FTE` operators/accounting assistants;
- synthetic salary anchor: `110k RUB/month` each;
- total salary-only anchor: `220k RUB/month`;
- senior accountant handles exceptions/final judgment.

### Option 1 — employee + ChatGPT

Assumption:

General-purpose AI helps with reading/classification, but employees still perform uploads, reconciliation, entry, checking and exception handling.

Synthetic outcome:

- operator load falls from 2.0 to `1.4 FTE` equivalent;
- salary-only comparable cost: `154k RUB/month`;
- licensing/other cost omitted unless observed later.

This option wins if the process is small, highly variable or too integrated for external execution.

### Option 2 — Arvectum Work

Productized stream:

`incoming documents → classify → extract → validate → reconcile → import-ready output → exception queue`

Synthetic service terms for modeling:

- `15 RUB` per accepted clean document;
- `8,000 × 15 = 120k RUB/month` Work charge;
- customer handles only exceptions/final accounting judgment;
- assume residual customer handling equivalent to `20k RUB/month` of internal time;
- synthetic total customer-side cost: `140k RUB/month`.

This would be roughly `36%` below the 220k salary-only baseline and about `9%` below the synthetic employee+AI baseline.

That second comparison is the important one: if Work cannot materially beat employee+AI after residual handling, this wedge is weak.

### Option 3 — owned agent / automation

Synthetic high-volume alternative:

- one-time build/integration: `450k RUB`;
- ongoing infrastructure/support: `30k RUB/month`;
- residual internal exception/judgment cost: `20k RUB/month`;
- steady-state monthly cost after build: `50k RUB`.

Compared with synthetic Work total `140k`, monthly delta is `90k`, so the one-time 450k investment would pay back in roughly `5 months` if volume/process stability holds.

### Commercial interpretation

At stable 8,000 documents/month, owned automation may be more rational than Work.

At lower, variable or seasonal volume, Work may be preferable because the customer avoids the one-time investment and support burden.

### What to test

- actual documents/month;
- operator time per document;
- employee+AI residual time;
- exception rate;
- 1C integration constraints;
- acceptable cost per accepted document;
- customer's own acceptable automation payback period.

---

## Scenario B — Logistics document closure / trip reconciliation

### Observed labor pattern

Vacancies ask staff to:

- close completed trips with correct document packs;
- reconcile `1C ↔ primary docs ↔ ЭТрН/TMS`;
- control missing documents;
- maintain registers and status;
- identify discrepancies before closing.

Public salary examples in the initial scan are commonly around `80–100k RUB/month` for these document-focused logistics roles.

### Synthetic customer

Transport/logistics company closes `3,000` trips per month.

Current operation:

- `2 FTE` document specialists;
- synthetic salary anchor: `95k RUB/month` each;
- salary-only baseline: `190k RUB/month`.

### Option 1 — employee + ChatGPT

ChatGPT may help interpret scans or draft summaries, but much of the workload is system reconciliation and status control.

Synthetic result:

- load falls to `1.5 FTE` equivalent;
- salary-only comparable cost: `142.5k RUB/month`.

### Option 2 — Arvectum Work

Stream:

`completed trip → collect/match documents → reconcile fields/statuses → clean close recommendation/output → exception queue`

Synthetic modeling:

- `35 RUB` per accepted trip closure;
- `3,000 × 35 = 105k RUB/month` Work charge;
- residual customer exception handling: `15k RUB/month`;
- total synthetic cost: `120k RUB/month`.

This is about `37%` below the 190k salary-only baseline and ~`16%` below the employee+AI baseline.

### Option 3 — owned automation

Synthetic alternative:

- one-time integration/build: `400k RUB`;
- support/infra: `25k RUB/month`;
- residual customer handling: `15k RUB/month`;
- steady-state cost: `40k RUB/month`.

Compared with Work total `120k`, monthly delta is `80k`; synthetic payback is about `5 months`.

### Commercial interpretation

This function looks attractive for Work when:

- volume is meaningful but not fully stable;
- TMS/1C integration for owned automation is expensive;
- customer needs quick start;
- peaks matter;
- exception rate remains low enough.

It may graduate to owned automation rapidly once the process becomes stable and high-volume.

---

## Scenario C — Product/catalog data validation and normalization

### Observed labor pattern

Current public vacancies include work such as:

- check price lists and product data;
- compare prices/descriptions/attributes;
- detect errors and duplicates;
- update internal tables/systems;
- create/fill product cards from templates.

Observed salary examples include roughly `80–85k RUB/month` for validation/data work and `50–60k RUB/month` for templated product-card work.

### Synthetic customer

Distributor receives `25,000` changed supplier/product records per month.

Current operation:

- `1.5 FTE` data/content operators;
- synthetic salary anchor: `85k RUB/month`;
- salary-only baseline: `127.5k RUB/month`.

### Option 1 — employee + ChatGPT

General-purpose AI can normalize descriptions and attributes, but employee still needs batch handling, master-data comparison, deduplication and exception resolution.

Synthetic result:

- load falls to `1.0 FTE`;
- salary-only comparable cost: `85k RUB/month`.

### Option 2 — Arvectum Work

Stream:

`supplier feed → normalize → match → deduplicate → validate → proposed update set + exceptions + provenance`

Synthetic modeling:

- `2.2 RUB` per accepted processed record;
- `25,000 × 2.2 = 55k RUB/month`;
- residual customer exception/master-data decisions: `10k RUB/month`;
- total customer-side cost: `65k RUB/month`.

This is ~`49%` below salary-only baseline and ~`24%` below the synthetic employee+AI baseline.

### Option 3 — owned automation

Synthetic alternative:

- one-time build/integration: `300k RUB`;
- support/infra: `20k RUB/month`;
- residual customer handling: `10k RUB/month`;
- steady-state: `30k RUB/month`.

Compared with Work total `65k`, monthly delta is `35k`; payback is roughly `9 months`.

At `50,000+` records/month, a per-unit Work price would rise unless volume discounting occurs, and owned automation could cross over much sooner.

### Commercial interpretation

This may be a strong first Work wedge because:

- low consequence relative to accounting/tender decisions;
- deterministic validation is possible;
- provenance can be explicit;
- scale is naturally measured per record;
- customer can keep final master-data authority.

---

## Cross-scenario commercial logic

### Work should be sold when

- recurring/bursty workload already consumes material paid labor;
- employee + modern AI still leaves operational burden;
- customer does not yet want to own/operate automation;
- volume is large enough for Work economics but below/around the owned-automation crossover;
- exceptions are bounded and measurable.

### Owned automation should be proposed when

- volume is high and stable;
- process is stable;
- integrations are durable;
- annual Work spend materially exceeds owned-operation cost;
- customer accepts the capital/integration/support burden;
- payback fits the customer's threshold.

### This creates a product ladder

For Work Discovery purposes:

`human process → employee + AI → Arvectum Work → handoff candidate for owned automation`

Work should not intentionally lock a customer into per-unit pricing after owned automation becomes economically rational.

## Immediate evidence priority

The next vacancy-corpus passes should seek real volume clues for these three scenarios:

1. monthly document count / number of counterparties / number of warehouses;
2. trips/shipments per day/month;
3. SKU/catalog record counts and supplier feed frequency.

Without volume, salary alone is insufficient to calculate a credible Work price.
