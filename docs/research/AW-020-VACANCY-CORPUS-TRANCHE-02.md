# AW-020 — Vacancy corpus tranche 02

Status: `Public-source evidence / current-vacancy tranche`
Date: `2026-09-17`

Purpose: expand AW-020-C1 with vacancy-level evidence while keeping **current** and **archived** vacancies separate.

A vacancy is evidence that an employer is paying or actively budgeting for a function. It is **not** evidence that the employer will buy Arvectum Work.

## 1. Inclusion rules

Count toward the current-corpus target only records that are:

- a concrete vacancy page, not a search/category page;
- publicly accessible;
- not marked archived at observation time;
- relevant to recurring digital/operational work;
- specific enough to extract at least one atomic duty.

Archived 2026 vacancies are retained only as **persistence evidence** for the function. They do not count toward the `>=100 current vacancies` target.

## 2. Current active sample — September 2026

| ID | Source | Vacancy | Salary shown | Atomic recurring functions | Cluster |
|---|---|---|---:|---|---|
| C035 | hh.ru | Оператор 1С — ТАЙМЫР ИНВЕСТ | 165k net | maintain nomenclature; process requests; create/update supplier orders; check receiving; control shipment/receipt/movements | orders + master data |
| C036 | hh.ru | Оператор 1С / Ассистент бренд-менеджера | 120k | order processing in 1C; track order-to-shipment; EDO; payment/shipment control | order-to-document |
| C037 | hh.ru | Оператор по документообороту — Лемана ПРО Склады | 84.5–88.5k gross | WMS receiving/placement; launch picking; receiving/shipping docs; UPD; reporting | warehouse document flow |
| C038 | hh.ru | Оператор обработки заказов на складе — ЗУБР МСК | 80–120k | primary docs; receipt/move/write-off in warehouse system; shipping docs; reports | warehouse document flow |
| C039 | hh.ru | Оператор 1С — PARLY | 80–120k net | Excel↔1C data transfer; requests; order documentation; execution monitoring | order/data processing |
| C040 | hh.ru | Менеджер по документообороту с сетями DIY | 90–100k gross | retail-chain orders; portal registrations; pallet labels; EDI/EDO cycle; TORG-2; KSF/UKD; reconciliations | retail EDI/EDO |
| C041 | hh.ru | Оператор 1С — Max Christmas | 100k | primary docs; receipts/shipments/corrections; invoices/UPD/acts; EDO status; discrepancy checks; reports; reference data | primary docs + reconciliation |
| C042 | hh.ru | Специалист по маркировке «Честный знак» | 120–130k gross | product cards; code issuance/turnover/write-off; exception tickets; marked-goods receiving/shipping; 1C docs; GTIN/EAN13; reports | marking/catalog data |
| C043 | hh.ru | Администратор / оператор ПК / базы данных | 60–70k | create records/order cards; control acceptance; verify payout requisites; prepare payout data | structured data operations |
| C044 | hh.ru | Менеджер службы клиентского сервиса | 100k | sales document flow; contracts/specifications; closing docs; shipment docs/certificates; order status | sales document operations |
| C045 | hh.ru | Специалист операционного отдела | 90k net | prepare forms; publish documents; create electronic media; maintain document flow | document operations |
| C046 | hh.ru | Специалист учебного центра | 90k | registries; personal files; system data; statistics/reports; incoming/outgoing docs | registry/reporting |
| C047 | hh.ru | Эксперт цифровых проектов | 218–272k gross | product-card content; product DB corrections; supplier content intake; site data freshness; tender-doc support | catalog/content operations |
| C048 | hh.ru | Ассистент отдела маркетинга | 90k | Excel/Bitrix/1C databases; contracts/closing docs; shipping/publication reports | mixed document/data ops |
| C049 | hh.ru | Lead Shopper / руководитель группы по документообороту | salary unknown | 1C purchase-order/contract checks; Diadok admin; reports; supplier document control | procurement document flow |
| C050 | hh.ru | Ведущий специалист отдела закупок ОЦО | salary unknown | check technical/procurement docs; prepare notices/materials; internal document flow | procurement subflow |
| C051 | hh.ru | Помощник руководителя / ведущий специалист | salary unknown | contract cards in 1C; template contracts; approval status; correspondence; reports | contract/document routing |

## 3. Archived 2026 persistence sample — NOT counted as current

The separate archived sample shows that the same functions have recurred throughout 2026 across unrelated employers. Examples observed include:

- primary documents + 1C + acts of reconciliation;
- order entry + invoices + EDO;
- receiving/shipping + WMS/1C;
- product nomenclature and reference-data upkeep;
- document checks and discrepancy correction;
- client/supplier document status control.

Salary anchors in the archived sample commonly fall around `65–130k RUB/month` for operational 1C/document roles, with some broader/higher bands when the role mixes commercial judgment, procurement, management or regulated accounting.

Archived examples are useful for **function persistence**, not current market-size counts.

## 4. Eight recurring function clusters now supported

### F1 — Primary documents + EDO

Typical atomic work:

`receive document → identify type → validate required fields → register/post in system → send/receive through EDO → monitor status → archive → escalate exception`

Common artifacts: UPD, invoices, acts, TORG-12, TTN, correction documents.

### F2 — Order processing in 1C/ERP

`receive request/order → validate customer/supplier/data → create/update order → produce invoice/order docs → monitor status → hand off exception`

### F3 — Warehouse/shipping document closure

`receive/ship event → verify system record → create/validate shipment documents → update WMS/1C → close or flag mismatch`

### F4 — Reconciliation and corrections

`compare source A vs source B → detect mismatch → apply allowed deterministic correction → prepare reconciliation/correction document → escalate ambiguous case`

### F5 — Master data / nomenclature

`create/update counterparty, product, contract or reference record → validate required attributes → deduplicate → maintain current state`

### F6 — Catalog/product-card/marking data

`receive supplier/source data → normalize attributes → create/update product card → validate codes/classification → publish/transfer → handle rejected records`

Marking flows can carry higher regulatory/system-access risk and require a narrower pilot boundary.

### F7 — Logistics / retail EDI-EDO cycle

`receive chain order → confirm → plan/record shipment → issue notices/docs → receive acceptance signal → reconcile discrepancies → correction/closing docs`

### F8 — Procurement/commercial document subflows

Suitable subflows are extraction, checklist validation, preparation from approved templates, register/status control and reporting.

Buyer/participation decisions, legal conclusions, bid submission and consequential approval remain outside the early Work boundary.

## 5. Main observation

The vacancy market repeatedly pays people not merely to "use 1C" but to perform a common operational pattern:

`structured event/document arrives → data is checked and transferred across systems → standard document/result is produced → status is monitored → mismatch becomes an exception`

That pattern is more promising for Work than the job title itself.

## 6. Strongest candidate work streams after tranche 02

### Candidate A — Order-to-document operations

Includes order intake, 1C/ERP entry, invoices/UPD, EDO status and deterministic status monitoring.

Why promising:
- appears in many unrelated roles;
- recurring/high-volume by nature;
- output state can often be checked;
- customer can retain only exception handling.

Key unknown: actual monthly order/document volume per employer.

### Candidate B — Warehouse/shipping document closure

Includes WMS/1C events, receiving/shipping docs, UPD, discrepancy checks and closure status.

Why promising:
- exceptionally clear input/output events;
- close to deterministic acceptance;
- vacancies explicitly pay 80–120k/month for this work.

Key unknown: access/security/integration cost versus remote managed execution.

### Candidate C — Product/master data + marking

Includes nomenclature, product-card attributes, reference data, code/catalog updates and exception queues.

Why promising:
- structured records;
- repeatable validation rules;
- current salary anchors include 120–130k for marking roles and materially higher mixed digital/catalog roles.

Key unknown: regulatory accountability and system permissions.

## 7. Why primary accounting is not automatically the first wedge

Primary-document vacancies are numerous, but some roles include tax/accounting responsibility, judgment, payment operations or statutory reporting. Work should first isolate low-consequence deterministic subflows rather than claim replacement of an accountant.

## 8. Why tender roles are not the first wedge

Tender/procurement roles can have high salary anchors, but many responsibilities involve strategy, supplier judgment, legal/compliance interpretation and consequential decisions.

Work may eventually service document extraction/checking/monitoring subflows, but the whole role is a poor first replacement claim.

## 9. Evidence still missing before AW-020-C1 completion

Do **not** close AW-020-C1 yet.

Still required:

- expand the number of current concrete vacancy records toward `>=100`;
- broaden exact vacancy-level evidence across at least five sources where accessible;
- reach `>=50` current salary/cost anchors;
- obtain workload-volume clues where vacancies disclose them;
- refine top-three economics using only the automatable functional slice, not whole-role salary;
- preserve archived records separately from current-market records.
