# AW-020 — Top candidate update after vacancy tranche 03

Status: `Discovery update / not a commercial decision`
Date: `2026-09-17`

This note refines, but does not replace, the synthetic economics in `AW-020-TOP3-SYNTHETIC-COMMERCIAL-SCENARIOS.md`.

## 1. Candidate-set change

Earlier scenario C combined generic product/catalog work with regulated marking operations.

The vacancy evidence now supports splitting them:

- **C1 — unregulated catalog / master-data validation**: preferred early candidate;
- **C2 — regulated marking / «Честный знак» operations**: later specialization or narrowly scoped data-preparation subflow.

Reason: both share structured data, but the latter adds regulatory interpretation, external-system actions and potentially consequential reporting/authority boundaries.

## 2. C1 — unregulated catalog/master-data validation

Observed atomic work:

`row/card/feed → normalize attributes → map to canonical nomenclature → detect duplicate/error → enrich permitted missing facts → produce accepted row/update proposal → exception`

New evidence:

- current vacancies show 80–140k+ RUB/month salary anchors for master-data, catalog and adjacent structured-data roles;
- one current vacancy explicitly states **40,000 rows/day** for product-card moderation.

This strengthens the hypothesis that catalog/master-data work can be sold as measurable processing capacity rather than a seat/job title.

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

The existing synthetic scenario used `25,000 records/month` only as a modeling assumption. The new `40,000 rows/day` evidence does **not** validate that assumed customer volume or the synthetic `2.2 RUB/record` price. It only proves that real employers can have very large row-level workloads.

At such high stable volumes, owned automation may become economically preferable very quickly. That makes C1 especially useful for testing the **Work → owned automation** crossover.

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
2. **Unregulated catalog/master-data validation** — strongest explicit high-volume evidence and a clean per-record commercial unit.
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
