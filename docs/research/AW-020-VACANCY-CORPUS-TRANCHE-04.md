# AW-020 — Vacancy corpus tranche 04

Status: `Public-source evidence / exact-page verified`
Date: `2026-09-17`

Purpose: convert selected hh.ru search observations into higher-confidence current evidence by checking the exact vacancy pages directly.

## 1. Verification rule

A record in this tranche counts as `current at observation time` only when:

- the exact vacancy page loads successfully;
- page metadata/title describes a normal vacancy rather than an archive page;
- no explicit archive wording is present;
- publication date is visible and current to September 2026;
- duties are extracted from the exact page, not only from a search snippet.

This still does not prove that the vacancy remains open after the observation date or that the employer would buy Arvectum Work.

## 2. Exact-page verified current records

| ID | hh.ru vacancy | Employer | Published | Salary shown | Exact-page recurring duties | Discovery cluster |
|---|---|---|---|---:|---|---|
| V001 | `137357096` — Оператор 1С (документооборот) | Мартфарм | 2026-09-15 | 60–70k RUB/month | template contract addenda; customer correspondence; template claims/information letters; signed-document return tracking; contract-termination support | document routing / contract operations |
| V002 | `136893634` — Оператор 1С / операционист по сопровождению заказов | Сфера Эстетики | 2026-09-02 | from 80k RUB/month | receive sales orders; create invoices in 1C; prepare shipping/supporting docs; marking-system work; delivery and shipment status control; inventory control | order-to-document |
| V003 | `137035900` — Оператор по вводу данных в 1С | Торговый Дом МАФ | 2026-09-16 | 70–80k RUB/month | primary docs in 1C; material movement/accounting/write-off; document registers; accompanying documents; document-flow maintenance | primary docs / 1C |
| V004 | `137110041` — Специалист по ведению нормативно-справочной информации и сопровождению ИС | Ситилаб | 2026-09-08 | 140k RUB/month | maintain production dictionaries; map services to a unified catalog; prepare specifications for new services / system changes; maintain service catalog; map service parameters | master data / catalog |
| V005 | `137320977` — Специалист по маркировке «Честный знак» | ЛБТ | 2026-09-14 | from 80k RUB/month | control full goods lifecycle in marking system; create/edit cards in marking system and 1C; code order/aggregation/turnover operations; interdepartmental coordination; residual-goods marking | regulated marking |
| V006 | `136588879` — Специалист по маркировке «Честный знак» | АНАЛИТИКА | 2026-09-15 | salary not shown | goods-movement accounting; EDO for UPD/write-off acts; mandatory reporting; problem resolution; support/vendor coordination; process adaptation to legal requirements | regulated marking |
| V007 | `137062000` — Специалист по работе с системой «Честный знак» | Наос Восток | 2026-09-16 | salary not shown | order/account for marking codes; process code-movement documents; EDO transfer control; 1C↔marking-system data checks; error resolution; reporting; legislation monitoring | regulated marking |
| V008 | `136979178` — Младший специалист по маркировке | Лотте КФ Рус | 2026-09-16 | 80–90k RUB/month net | product cards; code ordering and usage control; national catalog; invoices/administrative steps; external/internal coordination; legislation analysis | regulated marking |

## 3. Interpretation

### 3.1 Order-to-document remains commercially legible

V002 exposes a clean digital slice even though the whole job also contains physical work:

`order from sales → record/invoice in 1C → shipping/supporting documents → shipment/delivery status → exception`

Physical picking/packing and discretionary customer interaction should be excluded from an early Work service. The remaining digital slice is a plausible measurable work stream.

### 3.2 Master data is supported by a high salary anchor

V004 is particularly useful because the salary is `140k RUB/month` and the duties are largely structured catalog/reference-data work rather than a generic content role.

Potential Work slice:

`source record → map to canonical catalog → validate required attributes → propose/update mapping → exception`

The important missing variable remains throughput: the vacancy does not state records/day or records/month.

### 3.3 Regulated marking is real demand but a poor first full-function wedge

V005–V008 confirm current September 2026 demand for marking work, but the roles repeatedly combine:

- structured data work;
- external-system actions;
- cross-department coordination;
- legislation monitoring / compliance interpretation;
- reports and regulated operations.

Therefore the early Work boundary should isolate low-consequence data/document preparation and reconciliation rather than offer end-to-end replacement of a marking specialist.

## 4. Current salary anchors from this verified tranche

Verified salary-bearing records:

- 60–70k;
- 80k+;
- 70–80k;
- 140k;
- 80k+;
- 80–90k net.

These are role-level labor budget anchors. They are **not** the price ceiling for Work and must not be treated as fully automatable savings.

For economics, the relevant quantity is:

`role cost × share of time attributable to the bounded stream`

plus/minus employer overhead and residual human verification/exception handling.

## 5. What this tranche changes

Confidence increases that three candidate classes have real current paid labor behind them:

1. order/document processing in 1C/ERP;
2. primary/document operations and status control;
3. master/catalog/reference-data maintenance.

Current marking vacancies also confirm an adjacent market, but simultaneously strengthen the case for **not** choosing regulated marking as the first broad Work offer.

## 6. What this tranche does not prove

It does not prove:

- current workload volume;
- willingness to outsource;
- willingness to pay Arvectum Work;
- machine-executable share of each role;
- employee+AI residual cost;
- required integration effort;
- customer-side verification cost;
- Work pricing or unit economics.

## 7. Next evidence target

Continue AW-020-C1 with two priorities:

1. collect more exact-page verified current vacancies and reliable salary anchors;
2. search specifically for vacancies that disclose **workload volume** — orders, documents, rows, cards, shipments or counterparties per day/month.

The corpus target remains `>=100 current relevant vacancies` and `>=50 reliable salary anchors`; this tranche does not claim completion.
