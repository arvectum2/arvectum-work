# Arvectum Work — Discovery Roadmap

Status: `Proposed 0.2.0`
Date: `2026-09-17`
Phase: `Discovery`
Canonical repository: `arvectum2/arvectum-work`

## 1. Governing question

The roadmap exists to answer one question:

**Can Arvectum Work profitably take over a recurring stream of digital work for Russian companies and charge for accepted results, while being economically preferable to the relevant alternatives?**

Relevant alternatives MUST include:

- employee/manual work;
- employee + ChatGPT or another modern general-purpose AI;
- ordinary outsourcing;
- SaaS/RPA/specialized automation;
- customer's own AI agent/automation.

No stage may be passed on architecture, synthetic demos or internal benchmarks alone.

`Technical PASS ≠ Business PASS`.

## 2. Product direction under test

Arvectum Work is testing **machine work as a service**.

The customer should be able to transfer a recurring or bursty digital work stream and buy:

`volume + result + quality + deadline + price per accepted unit/batch`

The customer should not need to operate prompts/models/retries as the normal production process.

Work may initially operate as a managed/semi-manual service. Marketplace mechanisms are a later hypothesis, not a prerequisite for proving the business.

## 3. Current sequence

`AW-000 → AW-010 → AW-020 → AW-030 → AW-040 → AW-050 → AW-060`

Only after explicit `AW-060 GO` may a post-Discovery product build be admitted.

The first admitted product build MUST follow evidence:

- if value comes from managed execution and operating visibility, build the minimum managed Work product;
- if multiple buyers/executors create proven routing, capacity or price-discovery value, marketplace mechanisms may be added later.

---

## AW-000 — Product hypothesis and discovery baseline

Status: `Complete for baseline / superseded in part by Product Decision 001`

### Objective
Create a coherent product baseline, ownership boundary and evidence discipline before investing in software.

### Deliverables
- Product Vision;
- Hypothesis Register;
- Company/Product/OS ownership boundary;
- discovery roadmap;
- customer discovery plan;
- initial work taxonomy;
- first Worker experiment design;
- official-source legal/payment baseline;
- cross-review.

### Evidence gate
PASS only if:
- Arvectum Work has a dedicated canonical repo and product-owned baseline;
- Company retains portfolio/investment authority and footprint;
- no marketplace build is authorized;
- no OS capability/Product Contract is inferred without OS governance;
- legal/payment/procurement claims are officially sourced or explicitly unknown/to-be-verified.

---

## AW-010 — Russian market and substitutes

Status: `Public-evidence baseline complete / business validation not proven`

### Objective
Understand how Russian companies currently buy or perform comparable digital work and establish substitute baselines.

### Work
- map freelance/B2B service marketplaces, outsourcing, AI automation studios, agent platforms, SaaS/RPA and managed-service substitutes;
- collect public examples of task/process pricing and acceptance mechanisms;
- identify payment/data/local-execution constraints;
- distinguish buying a result from buying automation of a result;
- explicitly include employee + general-purpose AI and own automation as substitutes in later economics.

### Required evidence
- competitor/substitute map with source dates;
- 30+ public task/deal/service examples;
- observed pricing/packaging/acceptance patterns;
- explicit unresolved legal/payment questions.

### Gate
AW-010 public research can identify plausible wedges but cannot prove buyer demand for Work.

---

## AW-020 — Buyer/work-stream discovery

Status: `Current`

### Objective
Find real Russian business processes where transferring the **ongoing digital work stream** may be more valuable than assigning employees to operate AI or investing immediately in owned automation.

### Pre-interview requirement
Before the first real interview, maintain a concrete interviewable concept pack containing:

- a one-page Work concept;
- at least one clearly synthetic end-to-end example;
- a low-fidelity interface prototype that looks like management of a work stream, not a chat window;
- a direct comparison against `employee + ChatGPT` and `own agent/automation`;
- explicit labels that synthetic materials are not customer evidence.

The prototype exists to make discussion concrete; it must not lead the respondent before their recent real process is reconstructed.

### What every interview should reconstruct
At least one recent real work stream/process with:

- unit of work;
- weekly/monthly volume;
- peaks/variability;
- current people/hours involved;
- current cost or credible cost anchor;
- current use of ChatGPT/other AI;
- residual operator time after AI;
- input/output systems;
- exception rate or exception types;
- acceptance owner and quality rule;
- latency/deadline;
- data/security constraints;
- current outsourcing/SaaS/automation alternatives;
- condition for a small paid pilot;
- condition at which owned automation would be preferable.

### Target evidence
Minimum discovery set before stage decision:
- `15–20` structured interviews across at least `3` buyer archetypes;
- `25+` concrete recent work streams/tasks reconstructed from buyers;
- cost or budget anchors for at least `10`;
- quantified volume/frequency for at least `10`;
- explicit `employee + AI` substitute comparison for at least `10` where applicable;
- at least `5` buyers able to state a plausible paid-pilot condition;
- at least `2` buyers willing to provide a real bounded batch/stream for an experiment.

### Buyer PASS signal
At least one segment/process shows all of:
- material recurring or bursty volume;
- meaningful operator cost after considering modern general-purpose AI;
- result and exception handling can be bounded;
- buyer identifies who accepts the work;
- buyer can describe a plausible budget/payment route;
- at least one real paid-pilot opportunity is actionable;
- there is a credible economic window where Work can be preferable to both employee + AI and immediate owned automation.

### Gate
- `GO`: one buyer segment + one work stream show credible willingness to pay, measurable residual operational burden and real pilot access.
- `PIVOT`: pain exists but process, buyer, packaging or operating model must change.
- `STOP`: modern employee + AI already makes the remaining burden immaterial, buyers will not transfer the process, or owned automation is obviously superior for all credible targets.

---

## AW-030 — Work-stream contract, acceptance and substitution economics

### Objective
Prove that the leading work stream can be executed and accepted repeatedly and that Work has a credible economic advantage over the relevant alternatives.

### Work
For the leading work stream define:
- unit/batch boundary;
- inputs and prohibited inputs;
- output contract;
- acceptance criteria;
- evidence requirements;
- exception taxonomy;
- failure/revision rules;
- expected execution/verification cost;
- data/security class;
- human judgment dependency;
- cancellation/dispute conditions;
- throughput and latency target.

### Mandatory comparison
Benchmark the same representative workload against, where applicable:

1. current manual process;
2. competent employee using a modern general-purpose AI;
3. Arvectum Work execution;
4. credible own-automation scenario.

The comparison must use total relevant cost/time, not only model inference cost.

### Required evidence
For the leading work stream:
- at least `20` representative batches/tasks or a sufficiently large unit-level sample;
- pre-declared acceptance criteria frozen before execution;
- measured first-pass acceptance and revision rate;
- measured exception rate;
- throughput/time-to-result;
- verification cost;
- owner intervention;
- `employee + AI` residual operator baseline;
- preliminary `buy Work vs own automation` break-even model;
- expected contribution margin per accepted unit/batch.

### Gate
- `GO`: acceptance is reliable, expected contribution margin is positive, and Work shows a credible advantage for a real customer window after the employee+AI and own-automation tests.
- `PIVOT`: demand exists but scope, exception handling, pricing or execution architecture must narrow/change.
- `STOP`: Work adds little over employee + AI, verification/operator burden destroys economics, or own automation dominates at the target customer's realistic volume.

---

## AW-040 — First real external work-stream experiment

### Objective
Use the existing 24/7 Mac mini/local execution contour as an experimental Worker on a **real external batch or short work stream**, not merely a synthetic one-off demo.

### Required contour
`Real Customer → Work Stream/Batch → Assignment → Executor → Result + Evidence + Exceptions → Acceptance`

Settlement may occur in AW-040 if the customer is ready, but AW-040 PASS does not require funds to have cleared; AW-050 does.

### Required evidence
- real external customer and real workload;
- real observed volume context, even if pilot batch is small;
- price agreed before execution, or a pre-agreed paid-pilot condition;
- frozen Result/Acceptance contract;
- execution log and provenance;
- measured throughput/latency;
- compute/runtime cost;
- verification cost;
- exception/rework rate;
- owner intervention;
- customer acceptance/rejection evidence;
- comparison with customer's current employee/manual/AI-assisted process;
- no hidden manual completion presented as autonomous execution.

### Gate
- `GO`: Worker handles a real workload with acceptable quality and plausible better total economics for the tested customer window.
- `PIVOT`: customer demand is real but process/executor/scope/pricing needs change.
- `STOP`: execution is unreliable or no better than the customer's realistic substitute.

---

## AW-050 — First real paid end-to-end transaction

### Objective
Prove the complete economic loop with real money for accepted machine work.

### Required contour
`Customer Principal → paid workload → Assignment → Execution → Result + Evidence + Exceptions → Acceptance → lawful Settlement → revenue/economic evidence`

### Mandatory evidence
- identifiable real customer Principal;
- agreed unit/batch price and scope before completion;
- valid contractual/commercial basis;
- actual accepted Result;
- real payment/settlement evidence recorded privacy-safely;
- volume delivered and accepted;
- revenue;
- worker payout if any;
- execution/verification/payment/rework costs;
- owner intervention time;
- contribution margin;
- cost per accepted unit/batch;
- customer comparison against its prior process;
- explicit answer to whether customer would buy the same/similar work again.

### PASS criteria
All of:
1. Result accepted;
2. real payment received/settled to the appropriate Principal;
3. no material legal/payment exception silently assumed;
4. economics measured with unknowns remaining unknown;
5. no fabricated autonomy: owner/manual work counted;
6. buyer indicates repeat or starts/commits to a credible recurring continuation;
7. Work has not merely shifted equivalent operator burden back onto the customer.

---

## AW-060 — Go / Pivot / Stop

### Objective
Decide whether Arvectum Work deserves continued investment and what operating/product model is justified.

### Evidence package
Review at minimum:
- buyer interviews and reconstructed work streams;
- paid transaction evidence;
- repeat purchase/continuation evidence or absence;
- employee + ChatGPT substitution results;
- buy-Work vs own-automation break-even analysis;
- acceptance/revision/exception/dispute data;
- throughput/latency;
- Worker execution economics;
- owner intervention rate;
- acquisition/sales effort;
- legal/payment/tax/procurement constraints validated for the actual model;
- technology-sovereignty dependencies;
- whether multiple buyers/executors create genuine matching/capacity value.

### `GO` criteria
A GO recommendation requires evidence of:
- real paid demand, not only interviews;
- at least one repeatable work stream;
- reliable acceptance and bounded exceptions;
- positive or credibly improvable contribution economics;
- at least one completed paid transaction and credible recurring/repeat path;
- a demonstrated customer window where Work is preferable to employee + modern general-purpose AI;
- a demonstrated customer window where buying work is preferable to owning automation today;
- no known fatal legal/payment/data blocker;
- clarity on whether the next product should remain managed service or needs software/marketplace mechanisms.

### `PIVOT` criteria
Use PIVOT when a real business exists but one or more materially changes:
- buyer segment;
- work stream;
- acceptance/exception model;
- managed-service vs software/marketplace model;
- pricing model;
- execution architecture;
- payment/contract packaging.

### `STOP` criteria
Use STOP when evidence shows no credible route to repeatable paid demand with acceptable economics/risk, including if Work consistently loses to employee + AI or immediate owned automation for realistic buyers.

### Owner gate
`AW-060 Continue / Pivot / Stop` is a Company portfolio/investment decision.

---

## AW-100 — Managed Work MVP

Status: `NOT ADMITTED`.

May be created only after explicit `AW-060 GO` and separate scope/budget/architecture authority.

Purpose if admitted: productize the minimum customer/operations surface needed to receive work streams, show volume/status/quality/cost/exceptions, preserve evidence and support lawful acceptance/settlement without forcing marketplace complexity.

This stage is not automatically a public marketplace.

---

## AW-200 — Marketplace / multi-executor layer

Status: `NOT ADMITTED`.

May be considered only after evidence shows that multiple executors and buyers create material value from routing, capacity, price/quality competition or liquidity that cannot be captured efficiently by the managed Work model.

Do not build a broad marketplace merely because the long-term thesis is tradable machine work.
