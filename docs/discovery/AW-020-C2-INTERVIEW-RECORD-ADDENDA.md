# AW-020-C2 — Stream-specific interview record addenda

Status: `Operational template / privacy-safe`  
Date: `2026-09-23`

Use together with `AW-020-INTERVIEW-KIT-RU.md`.

Do not record personal contact details in the public repository.

## Common header

- Interview ID:
- Date:
- Stream: A / B / C
- Organization class:
- Respondent function:
- Recruitment route class:
- Recent real process confirmed: yes / no
- Evidence quality: usable / insufficient

## Stream A — Order-to-document / 1C + EDO

Capture explicitly:

- unit: realization / UPD / invoice / act / document set / other;
- normal units/day and units/month;
- peak volume;
- source system and target system;
- operator minutes/unit before AI;
- operator minutes/unit with current AI/automation;
- EDO/1C actions still manual;
- % missing/incorrect documents;
- % exceptions needing accountant/manager;
- acceptance rule and acceptance owner;
- authority-bearing steps excluded from external execution;
- integration/access burden;
- current cost/time anchor;
- paid external service already used: yes/no;
- own-automation threshold;
- pilot-safe batch, if any.

## Stream B — Catalog / master data

Capture explicitly:

- unit: row / SKU / card / service mapping / batch;
- records/day and records/month;
- number of source schemas;
- % exact-match / ambiguous-match / new-item cases;
- duplicate/error rate;
- fields that require domain judgment;
- current LLM/AI/RPA pipeline;
- human minutes per clean record and per exception;
- acceptance method: schema / sample / deterministic checks / expert review;
- provenance requirements;
- data-locality constraints;
- frequency of schema/rule changes;
- build-vs-buy threshold;
- pilot-safe batch, if any.

## Stream C — Warehouse / shipping document closure

Capture explicitly:

- unit: shipment / trip / receiving event / document pack;
- normal/peak units per period;
- systems: 1C / WMS / TMS / EDO / ЭТрН / other;
- document completeness rate;
- mismatch/missing-document rate;
- % cases requiring calls/messages to warehouse/carrier/supplier;
- digital steps separable from physical custody;
- signing/approval authority;
- close/acceptance rule;
- latency/SLA;
- operator minutes/unit;
- current automation;
- external-access restrictions;
- integration cost/complexity;
- own-automation threshold;
- pilot-safe batch, if any.

## Minimum usable interview gate

A record is usable only when it contains one recent real process plus:

- unit/input/output;
- actual or explicitly unknown volume;
- current method and AI use;
- residual human work;
- acceptance owner;
- exception evidence;
- time/cost anchor or explicit unknown;
- buying path or explicit unknown;
- own-automation threshold or explicit unknown.

Pure opinion about AI = insufficient evidence.
