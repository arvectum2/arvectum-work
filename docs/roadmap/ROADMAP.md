# Arvectum Work — Discovery Roadmap

Status: `Proposed 0.3.0`
Date: `2026-09-17`
Phase: `Discovery`
Canonical repository: `arvectum2/arvectum-work`

## 1. Governing question

**Can Arvectum Work profitably take over a recurring stream of digital work for Russian companies and charge for accepted results, while being economically preferable to the relevant alternatives?**

Relevant alternatives MUST include:

- employee/manual work;
- employee + ChatGPT or another modern general-purpose AI;
- ordinary outsourcing;
- SaaS/RPA/specialized automation;
- customer's own AI agent/automation.

No stage may pass on architecture, synthetic demos, vacancy counts or internal benchmarks alone.

`Technical PASS ≠ Business PASS`.

## 2. Product direction under test

Arvectum Work tests **machine work as a service**.

The customer transfers a recurring or bursty digital work stream and buys:

`volume + result + quality + deadline + price per accepted unit/batch`

The customer should not need to operate prompts/models/retries as the normal production process.

The initial operating model may be managed/semi-manual. Marketplace mechanisms are later hypotheses.

## 3. Current sequence

`AW-000 → AW-010 → AW-020 → AW-030 → AW-040 → AW-050 → AW-060`

Current AW-020 sub-sequence:

`concept/prototype → vacancy-function corpus → top-3 work-stream hypotheses → focused buyer validation → benchmark/pilot`

Broad generic buyer interviews are deferred until the vacancy/function corpus narrows the target.

---

## AW-000 — Product hypothesis and discovery baseline

Status: `Complete for baseline / superseded in part by Product Decisions 001–002`

Purpose: establish product/governance/evidence boundaries before building software.

No marketplace build, public launch, spend, payment-provider commitment or OS capability change is inferred from this stage.

---

## AW-010 — Russian market and substitutes

Status: `Public-evidence baseline complete / business validation not proven`

Completed public research includes:

- human freelance/service substitutes;
- B2B/managed service substitutes;
- AI/agent/automation substitutes;
- 30+ public task/service examples;
- observed pricing/packaging/acceptance patterns;
- official-source legal/payment baseline.

AW-010 proves only that adjacent paid markets exist. It does not prove demand for Work.

---

## AW-020 — Buyer/work-stream discovery

Status: `Current`

### Objective

Find recurring Russian business functions where an employer already bears material labor cost and where Work may take over a bounded digital work stream more cheaply than the realistic alternatives.

### AW-020-A/B/C0 — completed preparation

Completed:

- buyer archetype seed list;
- interview/evidence kit;
- one-page product concept;
- synthetic end-to-end example;
- work-stream interface prototype;
- employee+AI / Work / owned-automation comparison surface.

### AW-020-C1 — vacancy/function market scan — CURRENT

Before broad outbound interviews, build a public vacancy corpus as a proxy for existing labor budget.

Analyze **atomic duties, not titles**.

For each vacancy/function capture where publicly observable:

- portal/source/date;
- title and employer context;
- salary/range;
- location/remote;
- recurring duties;
- systems used: 1C, ЭДО, CRM, Excel, marketplace cabinets, etc.;
- volume/recurrence clues;
- structured input/output;
- human-only communication/judgment/accountability;
- candidate machine-work slice;
- acceptance/evidence path;
- likely exception classes.

### Vacancy corpus target

Before selecting focused buyer targets:

- `>=100` relevant current vacancies;
- `>=5` job/source portals where accessible, with source freshness recorded;
- `>=8` recurring function clusters independent of job title;
- salary/cost anchors for at least `50` records;
- explicit automation-scope hypothesis for every included record;
- top `3` candidate work streams selected for deeper evidence;
- synthetic Work offer + owned-automation alternative for each top candidate.

Vacancy counts are noisy and do not equal demand for Work.

### Current early candidates

Initial public scan currently prioritizes as hypotheses:

1. primary documents / 1C reconciliation;
2. logistics document closure / transport-document reconciliation;
3. product/catalog data validation and normalization;
4. structured order processing / 1C transaction preparation.

Tender/procurement document operations remain promising but higher consequence and are not the default first wedge.

### Economics rule

Never infer:

`100k vacancy salary → Work can sell for 50k`.

Decompose the role:

`automatable recurring flow + exceptions + judgment/communication + accountability`.

Compare:

`current attributable monthly flow cost`

vs

`Work price + customer residual exception/acceptance cost`

vs

`owned automation amortization/support + residual human cost`.

Vacancy salary is a conservative lower-bound cost anchor, not full employer cost.

### Substitute tests

A candidate remains interesting only if there is a realistic volume band where:

- employee + modern general-purpose AI still leaves material operator burden;
- Work can materially reduce total customer cost/time;
- Work retains positive contribution margin;
- owned automation does not already dominate at the customer's current volume.

Initial pricing research hypothesis: look for cases where Work can create at least ~30% customer savings after residual handling. This is **not** a price promise.

### Owned-automation crossover

For stable high-volume work estimate:

`annual Work spend`

against

`one-time owned automation + annual support/infra + residual human handling`.

If owned automation is clearly better, Work should surface a handoff signal to Arvectum Company rather than hide it. Work does not own the separate Arvectum OS/owned-agent product.

### AW-020-C2 — focused buyer validation

Status: `Deferred until C1 narrows targets`.

After the corpus selects top work streams, resume human validation with employers/functions that actually exhibit those duties.

Focused interviews should reconstruct:

- real unit of work;
- monthly/weekly volume and peaks;
- current people/hours/cost;
- current ChatGPT/AI use;
- residual operator burden;
- exception rate;
- acceptance owner/rules;
- latency/deadline;
- data/security constraints;
- willingness to transfer the process;
- paid-pilot condition;
- own-automation crossover threshold.

### AW-020 gate

`GO` requires at least one work stream with:

- observable existing paid labor demand;
- material recurring/bursty volume;
- meaningful residual human cost after employee+AI;
- bounded result/exception/acceptance model;
- credible focused buyer evidence or pilot access;
- an economic window where Work can beat both current operation and premature owned automation.

`PIVOT` if the paid function exists but scope/segment/packaging changes.

`STOP` if modern employee+AI eliminates most cost, external execution is unacceptable, or owned automation dominates at realistic volumes.

---

## AW-030 — Work-stream contract, acceptance and substitution economics

Objective: benchmark the leading work stream and prove repeatable acceptance plus credible economics.

Mandatory comparison where applicable:

1. current manual process;
2. competent employee + modern general-purpose AI;
3. Arvectum Work execution;
4. credible own-automation scenario.

Required evidence includes:

- representative workload/batches;
- frozen acceptance criteria;
- first-pass acceptance/revision/exception rates;
- throughput and latency;
- verification and owner-intervention cost;
- employee+AI residual baseline;
- buy-Work vs owned-automation break-even model;
- contribution margin per accepted unit/batch.

`GO` only if Work has a credible customer window after both substitution tests.

---

## AW-040 — First real external work-stream experiment

Use a real external batch/short stream, not a synthetic one-off.

Required contour:

`Real Customer → Work Stream/Batch → Assignment → Executor → Result + Evidence + Exceptions → Acceptance`

Measure volume context, throughput, compute/runtime, verification, exception/rework, owner intervention and comparison with the customer's existing process.

No hidden manual completion may be presented as autonomous execution.

---

## AW-050 — First real paid end-to-end transaction

Prove:

`Customer Principal → paid workload → Execution → accepted Result → lawful Settlement → measured economics`

Mandatory evidence:

- real price/scope before completion;
- accepted volume;
- real payment;
- revenue and all material costs;
- customer residual handling;
- cost per accepted unit/batch;
- contribution margin;
- repeat/continuation signal.

---

## AW-060 — Go / Pivot / Stop

Owner/Company decision based on:

- vacancy/function corpus;
- focused buyer evidence;
- paid transaction and repeat evidence;
- employee+AI substitution results;
- buy-Work vs own-automation analysis;
- acceptance/exception/throughput data;
- execution economics and owner intervention;
- legal/payment/data constraints;
- acquisition effort;
- evidence for or against multi-executor routing value.

`GO` requires a demonstrated customer window where Work is paid, repeatable, margin-positive and preferable to employee+AI and immediate owned automation.

---

## AW-100 — Managed Work MVP

Status: `NOT ADMITTED`.

Only after explicit `AW-060 GO` and separate authority.

If admitted, productize the minimum surface to receive work streams, show volume/status/quality/cost/exceptions, preserve evidence and support acceptance/settlement.

Not automatically a public marketplace.

---

## AW-200 — Marketplace / multi-executor layer

Status: `NOT ADMITTED`.

Consider only if multiple executors/buyers create proven routing, capacity, price/quality competition or liquidity value beyond the managed model.
