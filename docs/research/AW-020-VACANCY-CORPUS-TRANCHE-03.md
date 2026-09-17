# AW-020 — Vacancy corpus tranche 03

Status: `Public-source evidence / current-vacancy tranche`
Date: `2026-09-17`

Purpose: strengthen AW-020-C1 with vacancy-level evidence for the leading work-stream candidates and improve source-quality rules.

A vacancy remains a proxy for **existing paid labor demand**, not evidence that the employer would buy Arvectum Work.

## 1. Source-quality correction

Automated extraction of an `is_archive` boolean proved unreliable on some hh.ru pages. From this tranche onward, archive status is accepted only when the page title, metadata or visible page text explicitly says that the vacancy is archived.

Rules:

- explicit `вакансия в архиве` / `в архиве с ...` => archived;
- absence of explicit archive wording in search extraction is **not sufficient** to prove a vacancy is current; high-value records should be verified on the exact page before being counted as current;
- search/category pages never count as individual vacancy records;
- CAPTCHA/blocked pages do not support exact extracted duties or salary unless the public search snippet itself explicitly contains them;
- aggregator counts are directional only.

## 2. New current/recent exact records

The following exact vacancy pages add evidence to the leading clusters. Records remain provisional as `current/recent` until exact-page status verification is complete; records with explicit archive wording are excluded from the current target and retained as persistence evidence.

| ID | Source | Vacancy | Salary shown | Key atomic work | Status basis |
|---|---|---|---:|---|---|
| C052 | hh.ru | Оператор 1С (документооборот) — Мартфарм | 60–70k net | template documents; send/return control; standard correspondence; status tracking | current/recent candidate; exact-page archive verification pending |
| C053 | hh.ru | Оператор 1С / сопровождение заказов — Сфера Эстетики | 80k | receive orders; enter in 1C; invoice; shipping docs; marking; delivery/status control | current/recent candidate; exact-page archive verification pending |
| C054 | hh.ru | Оператор по вводу данных в 1С — Торговый Дом МАФ | 70–80k | primary docs; inventory moves/writeoffs; registries; accompanying docs | current/recent candidate; exact-page archive verification pending |
| C055 | hh.ru | Специалист по НСИ / сопровождению ИС — Ситилаб | 140k gross | maintain dictionaries; map customer nomenclature to unified catalog; update reference data | current/recent candidate; exact-page archive verification pending |
| C056 | hh.ru | Специалист по маркировке «Честный знак» — ЛБТ | 80k | product cards; code lifecycle; 1C records; exception handling | current/recent candidate; exact-page archive verification pending |
| C057 | hh.ru | Специалист по маркировке — АНАЛИТИКА | salary unknown | goods movement; EDO; reporting; exception/support flow | current/recent candidate; exact-page archive verification pending |
| C058 | hh.ru | Специалист по работе с «Честным знаком» — Наос Восток | salary unknown | code order/accounting; docs; EDO; 1C exchange; errors; reports | current/recent candidate; exact-page archive verification pending |
| C059 | hh.ru | Младший специалист по маркировке — Лотте КФ Рус | 80–90k | product cards; codes; national catalog; coordination | current/recent candidate; exact-page archive verification pending |

### Archived workload record — C060

hh.ru vacancy `130253648`, **Модератор карточек товаров — Честный знак.рф**, was re-checked directly on the exact page after this tranche was first written.

The page explicitly states that the vacancy is archived from `2025-10-06`, so it **MUST NOT** count toward the current-vacancy target.

The same exact page nevertheless contains a valuable historical workload statement in the duties: processing up to **40,000 rows per day in Excel**.

Therefore C060 is retained only as **historical workload/persistence evidence** for high-volume product-card moderation.

## 3. Critical workload evidence

### 3.1 Historical product-card moderation: `40,000 rows/day`

The archived hh.ru vacancy `130253648` directly states work with up to **40,000 rows per day**. Exact-page verification confirms that this number belongs to the duties of the role, but the vacancy itself is archived.

This remains unusually useful Discovery evidence because it demonstrates that employers have operated product-card/data-review processes at very large row-level scale.

The function is approximately:

`row/card arrives → validate against rules → enrich missing public facts where allowed → accept/correct/flag → return structured row`

This is relevant to Arvectum Work because:

- unit of work is countable;
- throughput is explicit;
- work is highly repetitive;
- quality rules can potentially be frozen;
- exceptions can be separated;
- the customer can potentially buy processing capacity instead of a seat.

This does **not** prove current 2026 demand at that employer, that all 40,000 rows are machine-executable, what accuracy is required, or what a buyer would pay per row.

### 3.2 Retail/EDI shipping persistence: `30–50 shipments`

An archived 2026 hh.ru vacancy for a retail-chain 1C operator states an average shipping volume of `30–50` units/shipments in its operating description while requiring UПД, ТТН, pallet sheets, Mercury, EDI/Diadok and return/claim handling.

Because the time period attached to `30–50` is not sufficiently explicit in the public text, **do not convert this to monthly volume**. It is retained only as evidence that these roles can be tied to measurable operational throughput.

## 4. Independent source corroboration

### `Работа России` / trudvsem.ru

Public search indexing on 2026-09-17 exposed recent vacancy cards including:

- `Оператор 1С по работе с интернет-магазинами` in Moscow, search snippet showing `80,000 RUB`;
- `Оператор по оформлению ЭПД`, with 1C / Excel requirements;
- primary-document accounting roles mentioning reconciliations, missing-document collection and 1C uploads;
- warehouse roles requiring 1C tracking and incoming/outgoing documents.

Direct card scraping was blocked by the source, so these records are source-level corroboration rather than full structured rows for the salary target unless the amount is explicitly present in the indexed snippet.

### SuperJob limitation

Current exact-card automation encountered CAPTCHA and unreliable extraction. SuperJob remains an observed market source from tranche 01, but no new exact records are added from CAPTCHA pages.

This is preferable to fabricating a five-source corpus.

## 5. Updated work-stream interpretation

### A — Order-to-document / 1C + EDO

Still a strong broad candidate.

Repeated duties:

`order/request → validate → create/update 1C/ERP record → invoice/UPD/shipping docs → EDO/status monitoring → exception`

Observed salary anchors in the collected vacancy evidence commonly appear in roughly the `60–100k+ RUB/month` range for narrow operational roles, with higher values when procurement/commercial judgment is mixed in.

Main risk: system access and integration cost can erase the apparent labor saving.

### B — Warehouse/shipping document closure

Still strong because the acceptance boundary is often clearer:

`physical/system event → receiving/shipping record → standard documents → reconciliation → close/exception`

The best first pilot should avoid physical picking/packing and take only the digital document subflow.

### C1 — Unregulated catalog/master-data operations

**Still promising, but the high-volume clue is historical rather than current.**

Examples include:

- nomenclature maintenance;
- mapping client/supplier nomenclature to a canonical catalog;
- duplicate/error detection;
- product-attribute validation;
- card moderation;
- reference-data updates.

The archived `40,000 rows/day` record demonstrates that this class of work can reach industrial scale. Current/recent salary and function evidence from other records still supports the cluster, but a current 2026 workload-volume example remains to be found.

### C2 — Regulated marking operations

Separate from generic catalog data.

Vacancies around «Честный знак» often include:

- product-card work;
- code ordering and lifecycle operations;
- EDO/1C exchange;
- discrepancy resolution;
- reporting;
- monitoring changing legislation;
- regulated submissions and external-system actions.

The data-normalization/checking portions may be strong Work candidates. Consequential regulated actions, legal interpretation and final responsibility are a higher-risk layer and should not be part of the first pilot by default.

## 6. Revised Discovery priority

The leading candidate set remains:

1. **Order-to-document operations** — broadest repeated labor pattern.
2. **Unregulated catalog/master-data validation** — clean per-record commercial unit and evidence of potentially very high historical volume; current workload-volume evidence still needed.
3. **Warehouse/shipping document closure** — strong deterministic acceptance, but integration/physical-process coupling must be tested.

`Честный знак`/regulated marking remains a later specialization or narrowed data-preparation subflow rather than the default form of candidate 2.

This is still a Discovery ordering, not a final product ranking.

## 7. Commercial implication

The vacancy scan supports a more precise selling proposition:

> Arvectum Work should not offer «an employee replacement». It should offer a measured processing capacity for a bounded stream: for example, N accepted orders/documents/rows per month, with declared error/exception handling and price per accepted unit or batch.

The economically relevant comparison is therefore:

`current fully-loaded process cost per accepted unit`

versus

`employee + AI residual cost per accepted unit`

versus

`Work price + customer exception/verification cost`

versus

`owned automation amortization + support + residual human cost`.

Salary is only one input into the first term.

## 8. What remains before AW-020-C1 completion

Do **not** close the task yet.

Still required:

- verify exact-page active/archive status before counting high-value hh.ru records as current;
- continue exact current-vacancy collection toward the explicit `>=100` criterion;
- continue salary anchors toward `>=50` reliable records;
- preserve at least five-source market coverage with explicit accessibility limits;
- seek current workload-volume evidence, especially orders/documents/rows per day or month;
- deduplicate exact URLs/employer-role duplicates;
- refine commercial scenarios using the **automatable slice**, never the full salary as the assumed savings;
- only after the corpus is sufficient, narrow focused buyer validation to the leading streams.
