# AW-020 — Top candidate update after vacancy tranche 03

Status: `Discovery update / not a commercial decision`
Date: `2026-09-17`

This note refines, but does not replace, the synthetic economics in `AW-020-TOP3-SYNTHETIC-COMMERCIAL-SCENARIOS.md`.

## 1. Candidate-set change

Earlier scenario C combined generic product/catalog work with regulated marking operations.

The vacancy evidence supports splitting them:

- **C1 — unregulated catalog / master-data validation**: preferred early candidate;
- **C2 — regulated marking / «Честный знак» operations**: later specialization or narrowly scoped data-preparation subflow.

Reason: both share structured data, but the latter adds regulatory interpretation, external-system actions and potentially consequential reporting/authority boundaries.

## 2. C1 — unregulated catalog/master-data validation

Observed atomic work:

`row/card/feed → normalize attributes → map to canonical nomenclature → detect duplicate/error → enrich permitted missing facts → produce accepted row/update proposal → exception`

Evidence:

- current/recent vacancy evidence shows roughly 80–140k+ RUB/month salary anchors for master-data, catalog and adjacent structured-data roles, subject to exact-page status verification before current-corpus counting;
- one **archived** hh.ru vacancy for product-card moderation directly states a workload of up to **40,000 rows/day**. Exact-page verification confirms the number belongs to the duties, but the vacancy is archived from 2025-10-06.

The historical high-volume record strengthens the hypothesis that catalog/master-data work can be sold as measurable processing capacity rather than a seat/job title, but it does **not** prove current 2026 workload demand.

### Commercial unit to test

Possible unit:

`accepted row/card` or `accepted batch of N records`.

Candidate service metrics:

- records received;
- records accepted cleanly;
- exception rate;
- field-level accuracy;
- throughput / records per hour;
- provenance coverage;
- customer verification sample size;
- price per accepted record/batch.

### Important caveat

The existing synthetic scenario used `25,000 records/month` only as a modeling assumption. The historical `40,000 rows/day` evidence does **not** validate that assumed customer volume or the synthetic `2.2 RUB/record` price. It only proves that real employers have operated very large row-level workloads in this function class.

At sufficiently high stable volumes, owned automation may become economically preferable very quickly. That makes C1 useful for testing the **Work → owned automation** crossover, provided current workload evidence can also be found.

## 3. C2 — regulated marking

Keep only low-consequence, bounded subflows in early Work exploration, such as:

- product-card preparation;
- structured field validation;
- code/request data preparation;
- reconciliation between permitted source data and 1C/EDO records;
- exception detection;
- draft reporting data.

Do not include by default:

- legal/regulatory interpretation;
- final statutory reporting approval;
- consequential external-system submission without explicit authority;
- actions that make Work the customer's compliance decision-maker.

## 4. Updated top-three Discovery candidates

1. **Order-to-document / 1C + EDO operations** — broadest repeated pattern across employers.
2. **Unregulated catalog/master-data validation** — clean per-record commercial unit, current/recent salary/function evidence and strong historical high-volume evidence; current workload-volume evidence is still missing.
3. **Warehouse/shipping document closure** — good acceptance boundary, but integration and coupling to physical operations are material risks.

Regulated marking remains a useful adjacent specialization but not the default first wedge.

## 5. What would change the ordering

Promote a candidate when current evidence shows:

- clear unit of work;
- repeated high volume;
- role-level budget anchor;
- low customer-side verification burden;
- low consequence of a single error;
- limited privileged access;
- plausible Work price below employee+AI residual cost;
- owned automation not already obviously superior at likely customer scale.

Demote when:

- most value comes from human judgment/communication;
- customer must supervise nearly every unit;
- integration/setup cost is comparable to building owned automation;
- liability/regulation makes external machine execution unattractive;
- employee + general AI already removes nearly all operational labor.


## 6. Update after throughput-cost corpus 03 — 2026-09-18

New public evidence sharpens candidate 2 without changing the current top-three set.

### Current numeric volume signal

Kadrout vacancy `39101`, dated 2026-09-07, states that the card-check/fill workflow can handle `10 cards/day`.

This is a current numeric throughput phrase, but the compensation text is internally ambiguous: the page says `1 checked category = 800 RUB` while separately referring to `10 cards/day`. The record therefore **does not** establish a clean RUB/card or employee salary+throughput pair.

### Owned-automation substitute becomes concrete

A recent ПравЖизнь technical-content vacancy (published 2026-07-01; original hh window mirrored as ending 2026-08-30) describes an existing `Python + Flask + Excel-generator` plus AI pipeline and a target of:

`25 collections × 1500 cards / 2 months = 37,500 cards / 2 months`

The same description says:
- the role writes little manually and automates heavily;
- the pipeline covers content → photo → files → upload;
- structured data is loaded into 1C / WB / Ozon / Yandex Market;
- validation includes duplicate articles, field correctness and marketplace requirements;
- 100+ collections are already in the pipeline.

This is recent historical process/substitute evidence, **not** current accepted throughput, salary evidence or customer proof.

### Implication for candidate 2

Candidate 2 remains attractive because its unit is clean and measurable. But its competitive bar is now higher:

> Arvectum Work must beat the buyer's option of operating an AI-first catalog pipeline, not merely beat manual catalog labor.

The candidate is strongest where:
- the buyer has recurring or bursty batches but does not want to own the pipeline;
- schemas/sources vary enough that managed execution has value;
- Work can provide acceptance/evidence/provenance and bounded exceptions;
- switching/setup cost stays materially below owned automation.

At very high stable volume, current evidence increases the probability that owned automation is the rational endpoint.

### Ordering

No ordering change is justified yet:

1. Order-to-document / 1C + EDO operations;
2. Unregulated catalog/master-data validation;
3. Warehouse/shipping document closure.

Reason: catalog/master-data now has stronger throughput and substitute evidence, but still lacks a clean **current employee salary + numeric processing rate** pair and has not yet been tested against real buyer willingness to outsource.
