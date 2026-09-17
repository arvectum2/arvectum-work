# AW-040 — First Mac mini Worker Paid-Job Experiment

Status: `Proposed 0.1.0 / Discovery`
Date: `2026-09-17`
Owner: `Arvectum Work`
Worker host: existing 24/7 Arvectum Mac mini with local LLM

## 1. Experiment question

Can the existing Mac mini act as a bounded autonomous Worker that completes a real externally sourced paid Job with pre-declared Acceptance, measurable evidence and plausible positive unit economics?

The experiment tests the Worker and transaction hypothesis. It does not test a marketplace UI, matching engine or public platform.

## 2. Default Job hypothesis

Default family: `J-02 — Document extraction and normalization`.

Example paid Job:

> Given a bounded pack of documents supplied by a real customer, return a CSV/JSON/XLSX table containing a pre-declared field schema, a per-field source reference, an ambiguity/error report and the requested final artifact.

AW-020 customer evidence may replace J-02 before execution if another family has materially stronger paid demand.

## 3. Parties and roles

- **Customer Principal** — the person/legal entity with authority to order and accept the work.
- **Arvectum Principal** — the legal/economic party contracting/invoicing/receiving settlement where applicable.
- **Executor** — Mac mini + declared local runtime/tools.
- **Owner/operator** — may configure, supervise and verify within the declared experiment, but all intervention must be measured and disclosed in the evidence.

The Mac mini is an Executor, not the contractual/economic Principal.

## 4. Pre-execution Job Contract

Before execution starts, freeze a small experiment record with:

- Job ID;
- customer type and privacy-safe identity reference;
- input artifact manifest;
- allowed data boundary;
- output schema and format;
- Acceptance criteria;
- deadline / maximum latency;
- agreed price or paid-pilot condition;
- revision rule;
- cancellation rule;
- verification method;
- prohibited actions and systems;
- settlement basis/path to be used if accepted.

Acceptance criteria MUST be frozen before the Worker sees acceptance feedback.

## 5. Suggested first Acceptance design

For J-02:

1. `100%` of required records are present or explicitly flagged as unreadable/missing.
2. Required schema validates.
3. Every non-derived material value has a source page/section/reference where feasible.
4. A frozen verification sample is checked against source truth.
5. No invented value is allowed where the source is ambiguous; ambiguity must be explicit.
6. Customer-specific formatting/checklist requirements are satisfied.
7. Any quality threshold is agreed before execution and reported exactly, not retuned afterward.

The exact threshold must be chosen from the real Job and buyer risk, not invented now.

## 6. Execution contour

`Intake → eligibility/risk check → Assignment → isolated work directory → local execution → deterministic/schema checks → evidence pack → verification → customer delivery → Acceptance/Revision → Settlement`

No broad Worker autonomy is implied outside the Job.

## 7. Allowed initial Worker capabilities

Only what the Job requires, preferably:

- read the admitted input files;
- local model inference;
- deterministic local parsing/transformation;
- generate structured output and evidence;
- run schema/consistency checks;
- write only to the isolated Job workspace.

Network access should be disabled unless the exact Job requires approved public-source retrieval.

## 8. Prohibited actions in first experiment

- bank/payment execution by the Worker;
- customer production-system mutation;
- EIS/ETP action or procurement submission;
- signing contracts/documents;
- external communications in customer/Company name without separate authority;
- new paid vendor commitments;
- unrestricted secrets/credentials;
- silent human replacement of failed autonomous work;
- acceptance-criterion changes after output is observed to make the run pass.

## 9. Evidence to capture

### Commercial
- agreed price;
- actual revenue/payment status;
- whether the buyer would repeat;
- acquisition channel and sales effort.

### Execution
- start/end timestamps;
- runtime/model/tool versions;
- compute/runtime estimate;
- number of attempts;
- first-pass result;
- final accepted result;
- failures/retries.

### Quality
- acceptance result;
- verification sample result;
- revision count;
- failure/exception count;
- customer corrections.

### Economics
- Worker execution cost;
- verification cost;
- payment cost;
- rework cost;
- human/Owner intervention minutes;
- worker payout if applicable;
- contribution margin.

### Governance
- source/input provenance;
- exact Acceptance contract;
- authority/data boundary;
- settlement evidence recorded without exposing bank/private data in the public repo.

## 10. Intervention accounting

Every human intervention after Assignment must be classified:

- `setup`;
- `execution rescue`;
- `quality verification`;
- `customer communication`;
- `commercial/payment administration`;
- `other`.

Do not count an outcome as autonomous if a human materially completed or rewrote the work. A hybrid result may still be commercially useful, but it must be labeled honestly.

## 11. Economic calculation

For the Job calculate:

`Contribution margin = realized revenue - worker payout - execution cost - verification cost - payment cost - rework cost`

Owner/human time is tracked separately and also used in a sensitivity view because unpaid Owner time is not economically free.

Unknown cost remains `unknown` until measured.

## 12. AW-040 PASS

PASS requires:

- real external Job;
- price or paid-pilot condition agreed before execution;
- frozen Acceptance;
- Mac mini performs the material execution;
- Result is accepted or reaches acceptance after measured bounded revision;
- evidence is complete enough to reconstruct the run;
- execution economics are plausibly positive before hidden Owner labor.

AW-040 does not require payment to have cleared. If it clears, preserve it as early AW-050 evidence.

## 13. AW-050 handoff

The preferred next action after a successful Worker run is not “add more features”.

It is:

1. obtain/confirm Acceptance;
2. complete the lawful agreed Settlement;
3. measure the whole transaction;
4. ask for a repeat Job;
5. record the evidence for AW-050.
