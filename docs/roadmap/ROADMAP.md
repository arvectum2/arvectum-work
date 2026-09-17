# Arvectum Work — Discovery Roadmap

Status: `Proposed 0.1.0`
Date: `2026-09-17`
Phase: `Discovery`
Canonical repository: `arvectum2/arvectum-work`

## 1. Governing rule

The roadmap exists to answer one question:

**Can machine work in Russia produce real, repeatable, economically attractive paid transactions before we invest in a marketplace?**

No stage may be passed on architecture or internal demos alone.

`Technical PASS ≠ Business PASS`.

## 2. Current sequence

`AW-000 → AW-010 → AW-020 → AW-030 → AW-040 → AW-050 → AW-060`

Only after explicit `AW-060 GO` may `AW-100 — Marketplace MVP` be admitted.

---

## AW-000 — Product hypothesis and discovery baseline

Status: `Current`

### Objective
Create a coherent product baseline and eliminate the former Arvectum Exchange / Company-repo ambiguity.

### Deliverables
- Product Vision;
- Hypothesis Register;
- Company/Product/OS ownership boundary;
- discovery roadmap;
- customer discovery plan;
- initial machine-work job taxonomy;
- first Worker experiment design;
- official-source legal/payment baseline;
- cross-review.

### Evidence gate
PASS only if:
- Arvectum Work has a dedicated canonical repo and product-owned baseline;
- Company retains only portfolio/investment authority and footprint;
- no marketplace build is authorized;
- no OS capability/Product Contract is inferred without OS governance;
- legal/payment/procurement claims are either officially sourced or explicitly marked unknown/to-be-verified.

### Decision
- `GO`: baseline is coherent and reversible; start market discovery.
- `PIVOT`: boundaries or thesis need material rewrite before interviews.
- `STOP`: no coherent product thesis remains after reconciliation.

---

## AW-010 — Russian market and competitors

### Objective
Understand substitutes, current buyer behavior and where machine-work transactions might be differentiated in Russia.

### Work
- map Russian freelance/B2B service marketplaces, AI automation studios, agent platforms and managed-service substitutes;
- collect public examples of task pricing and acceptance mechanisms;
- identify payment/data/local-execution constraints that materially affect buying;
- distinguish evidence from hypotheses.

### Required evidence
- competitor/substitute map with source dates;
- 30+ public task/deal examples across candidate categories;
- observed pricing/packaging/acceptance patterns;
- explicit list of unresolved legal/payment questions.

### Gate
- `GO`: at least 2 plausible wedges have observable paid demand and no known fatal blocker.
- `PIVOT`: demand exists but not for the initial job families or buyer segment.
- `STOP`: no meaningful paid substitute market or no plausible differentiated wedge.

---

## AW-020 — Buyer/problem discovery

### Objective
Prove that specific Russian buyers have recurring work they would pay to receive as a result rather than as an AI implementation project.

### Target evidence
Minimum discovery set before stage decision:
- `15–20` structured buyer/problem interviews across at least `3` buyer archetypes;
- `25+` concrete recent tasks supplied or reconstructed from buyers;
- price/budget or current cost evidence for at least `10` tasks;
- explicit current workaround and pain for each interview;
- at least `5` buyers who can state a plausible paid pilot condition;
- at least `2` buyers willing to provide a real bounded task for the next experiment.

Counts are discovery targets, not substitutes for evidence quality.

### Buyer PASS signal
At least one segment shows all of:
- recurring task frequency;
- material cost/latency/pain today;
- outcome can be specified;
- buyer can identify who accepts the result;
- buyer can describe a plausible budget/payment route;
- at least one real pilot opportunity is actionable.

### Gate
- `GO`: one buyer segment + one job family show credible willingness to pay and real pilot access.
- `PIVOT`: pain exists but buyer, job or packaging must change.
- `STOP`: interest remains informational/AI-curiosity with no paid outcome demand.

---

## AW-030 — Machine-work task taxonomy and acceptance

### Objective
Prove that one or more paid job families can be specified, executed and accepted repeatably.

### Work
For each shortlisted job family define:
- inputs and prohibited inputs;
- output contract;
- acceptance criteria;
- evidence requirements;
- failure/revision rules;
- expected execution/verification cost;
- data/security class;
- human judgment dependency;
- cancellation/dispute conditions.

### Required evidence
For the leading job family:
- at least `20` representative tasks or benchmark cases;
- pre-declared acceptance criteria frozen before execution;
- measured first-pass acceptance and revision rate;
- acceptance false-positive/false-negative analysis where testable;
- bounded failure modes;
- estimate of revenue minus execution/verification/rework cost.

### Gate
- `GO`: acceptance is reliable enough for a real paid attempt and expected contribution margin is positive before owner-time sensitivity.
- `PIVOT`: task demand exists but acceptance or scope must be narrowed.
- `STOP`: result quality cannot be judged predictably enough for a transaction.

---

## AW-040 — First autonomous Worker experiment

### Objective
Use the existing 24/7 Mac mini with local LLM as an experimental Worker on a real external Job.

### Required contour
`Real Customer → Job → Assignment → Mac mini Executor → Result + Evidence → Acceptance`

Settlement may occur in AW-040 if the customer is ready, but AW-040 PASS does not require funds to have cleared; AW-050 does.

### Required evidence
- real external customer and real job;
- price agreed before execution, or a pre-agreed paid-pilot condition;
- frozen Job/Acceptance contract before worker sees the final acceptance result;
- execution log and Result provenance;
- measured latency, compute/runtime cost, verification cost, rework and owner intervention;
- customer acceptance/rejection evidence;
- no hidden manual completion presented as autonomous execution.

### Gate
- `GO`: Worker completes a real job with acceptable quality and plausible positive economics.
- `PIVOT`: customer demand is real but executor/job scope needs change.
- `STOP`: autonomous execution is uneconomic or unreliable for the tested family.

---

## AW-050 — First real paid end-to-end transaction

### Objective
Prove the complete economic loop with real money.

### Required contour
`Customer Principal → paid Job → Assignment → Execution → Result + Evidence → Acceptance → lawful Settlement → revenue/economic evidence`

### Mandatory evidence
- identifiable real customer Principal;
- agreed price and scope before completion;
- valid contractual/commercial basis appropriate to the transaction;
- actual accepted Result;
- payment/settlement evidence recorded in a privacy-safe way;
- revenue, worker payout if any, execution, verification, payment and rework costs;
- owner intervention time;
- contribution margin;
- post-transaction buyer feedback;
- explicit answer to whether buyer would purchase the same/similar result again.

### PASS criteria
All of:
1. Result accepted;
2. real payment received/settled to the appropriate Principal;
3. no material legal/payment exception was silently assumed;
4. transaction economics are measured, with unknowns remaining unknown;
5. no fabricated autonomy: owner/manual work is counted;
6. buyer indicates repeat or a credible condition for repeat.

### Gate
- `GO`: one paid loop exists; proceed to viability review and seek repeat evidence.
- `PIVOT`: payment happened but economics/job/segment/model is weak.
- `STOP`: a lawful payable transaction cannot be completed on the selected model or economics are structurally negative.

---

## AW-060 — Go / Pivot / Stop

### Objective
Decide whether Arvectum Work deserves continued investment and whether marketplace software is justified.

### Evidence package
Review at minimum:
- buyer interviews and task corpus;
- paid transaction evidence;
- repeat purchase evidence or absence;
- acceptance/revision/dispute data;
- Worker execution economics;
- owner intervention rate;
- acquisition path and sales effort;
- legal/payment/tax/procurement constraints validated for the actual model;
- technology-sovereignty dependencies;
- whether multiple buyers/executors create genuine matching/liquidity value.

### `GO` criteria
A GO recommendation requires evidence of:
- real paid demand, not only interviews;
- at least one repeatable job family;
- reliable acceptance;
- positive or credibly improvable contribution economics;
- at least one completed paid transaction and a credible repeat path;
- no known fatal legal/payment/data blocker for the selected operating model;
- a reason software/marketplace mechanisms would reduce transaction cost or increase liquidity versus a managed service.

### `PIVOT` criteria
Use PIVOT when a real business exists but one or more of these changes materially:
- buyer segment;
- job family;
- acceptance model;
- managed-service vs marketplace model;
- pricing/take-rate model;
- execution architecture;
- payment/contract packaging.

### `STOP` criteria
Use STOP when evidence shows no credible route to repeatable paid demand with acceptable risk/economics, or when the product would require disproportionate legal/financial/operational complexity relative to the opportunity.

### Owner gate
`AW-060 Continue / Pivot / Stop` is a Company portfolio/investment decision.

Marketplace MVP admission is not automatic from technical success.

---

## AW-100 — Marketplace MVP

Status: `NOT ADMITTED`.

May be created only after explicit `AW-060 GO` and separate scope/budget/architecture authority.
