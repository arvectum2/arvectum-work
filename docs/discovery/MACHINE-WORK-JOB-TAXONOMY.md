# AW-030 — Initial Machine-Executable Paid Job Taxonomy

Status: `Proposed 0.1.0 / Discovery`
Date: `2026-09-17`
Owner: `Arvectum Work`

## 1. Selection principle

The first job families are not a marketplace catalog. They are bounded hypotheses chosen because they can be tested manually, priced as outcomes and accepted with evidence before a marketplace exists.

A good early Job has:

- explicit inputs;
- bounded output schema/artifact;
- pre-declared Acceptance;
- low-cost verification;
- limited privileged access;
- measurable execution/rework cost;
- enough recurrence to support repeat purchase.

## 2. Candidate job families

### J-01 — Structured public-web commercial research

Example outcome:

`Find suppliers/products matching declared constraints and return a normalized CSV/JSON dataset with source evidence.`

Possible Acceptance:
- required fields populated;
- source URL/evidence for every record;
- deduplication rules;
- sample verification of factual fields;
- freshness cutoff declared before execution.

Why test early:
- common B2B task pattern;
- can use public data;
- result is structured and auditable;
- low customer-system privilege.

Risks:
- website terms/access restrictions;
- dynamic data/freshness;
- source reliability;
- anti-bot constraints.

### J-02 — Document extraction and normalization

Example outcome:

`Extract defined fields/tables from a bounded set of supplied documents into a declared schema.`

Possible Acceptance:
- schema validation;
- benchmark truth for a sample;
- field-level accuracy thresholds;
- explicit unreadable/ambiguous flags rather than invented values.

Why test early:
- objectively benchmarkable;
- local execution may create data-sovereignty value;
- easy to measure error/rework economics.

Risks:
- confidential data;
- scan quality/OCR dependency;
- ambiguous source documents.

### J-03 — Data cleanup, reconciliation and enrichment

Example outcome:

`Normalize a CSV/XLSX dataset, remove duplicates, reconcile identifiers and return a validated dataset plus exception report.`

Possible Acceptance:
- deterministic schema/type checks;
- declared duplicate rules;
- reconciliation coverage;
- exception count and unresolved records;
- no silent deletion.

Why test early:
- measurable before/after state;
- low-latency execution;
- repeatable operations use case.

Risks:
- ambiguous merge rules;
- hidden source-of-truth issues;
- sensitive business data.

### J-04 — Bounded code bug fix or transformation

Example outcome:

`Fix one declared defect or implement a narrow transformation in an isolated repository so frozen automated tests pass.`

Possible Acceptance:
- exact-head test suite;
- declared changed-path boundary;
- no prohibited dependency/security changes;
- diff review and reproducible build.

Why test:
- unusually strong machine-checkable Acceptance;
- execution evidence is straightforward.

Risks:
- IP/private-code exposure;
- test gaming;
- hidden architectural context;
- security-sensitive changes.

### J-05 — Public procurement/tender document triage and structured extraction

Example outcome:

`From publicly available procurement documents, extract declared dates, requirements, quantities, qualification fields and source references into a structured brief.`

Possible Acceptance:
- every extracted field linked to source location;
- required-field completeness;
- contradiction/uncertainty flags;
- spot-check against source.

Boundary:
This is information extraction, **not** a procurement participation decision, legal conclusion, bid submission, EIS/ETP action or claim of 44-FZ/223-FZ compliance.

Why test:
- domain familiarity;
- structured recurring documents;
- provenance can be strong.

Risks:
- legal/business consequences if extraction is wrong;
- changing document versions;
- temptation to expand into prohibited decision/submission scope.

### J-06 — Website/catalog change monitoring

Example outcome:

`Check a declared set of public pages on schedule and return only material changes with before/after evidence.`

Possible Acceptance:
- coverage of declared URLs;
- reproducible timestamps;
- before/after artifacts or hashes;
- false-positive sampling;
- change taxonomy fixed in advance.

Why test:
- recurring by nature;
- strong repeat-purchase potential;
- can become a clear evidence-driven service before productization.

Risks:
- access blocking;
- page-layout churn;
- false positives;
- source retention requirements.

### J-07 — Evidence-backed report generation from supplied sources

Example outcome:

`Generate a bounded analytical brief from an approved source pack with every material factual statement traceable to a source.`

Possible Acceptance:
- required sections/checklist;
- citation/source coverage;
- factual consistency checks;
- length/format requirements;
- explicit unsupported/unknown statements.

Why test:
- frequent knowledge-work pattern;
- local LLM is usable;
- evidence requirement differentiates it from generic text generation.

Risks:
- subjective quality;
- factual synthesis errors;
- acceptance may become too human-intensive.

## 3. Initial preference for first paid experiment

Current default candidate: **J-02 — Document extraction and normalization**, with **J-01** as a strong alternative.

Reason:

- bounded input/output;
- pre-declared field-level Acceptance;
- easy local execution;
- easy measurement of first-pass quality and rework;
- does not require building marketplace infrastructure;
- can be sold as a concrete result.

This preference is a Discovery hypothesis. AW-020 buyer evidence may replace it.

## 4. Excluded early job classes

Do not prioritize for the first paid transaction:

- unrestricted autonomous purchasing;
- bank/payment actions;
- legal representation or legal conclusions relied on without qualified review;
- EIS/ETP procurement submission;
- external communications in the customer's name without explicit authority;
- high-consequence cybersecurity changes;
- tasks requiring broad production credentials;
- open-ended “do whatever is needed” assignments;
- work whose Acceptance can only be decided after seeing the result with no frozen criteria.

## 5. Promotion rule

A Job family becomes `validated` only from real evidence:

`buyer demand + real tasks + frozen Acceptance + execution history + economics + paid acceptance`.

Internal benchmark success alone leaves it `experimental`.
