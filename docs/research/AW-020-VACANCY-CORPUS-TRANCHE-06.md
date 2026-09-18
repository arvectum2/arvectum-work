# AW-020 — Vacancy corpus tranche 06

Status: `Public-source evidence / exact-page verified / third strict source`  
Date: `2026-09-18`

Purpose: expand AW-020-C1 with concrete current Rabota.ru detail pages and establish a third strict public vacancy source.

## 1. Verification rule

A Rabota.ru record in this tranche counts as `current at observation time` only when:

- the exact numeric vacancy detail page loads with HTTP 200;
- page metadata exposes a concrete vacancy title/employer and recent `datePosted` / visible placement date;
- the visible page does not contain an exact closure/archive phrase such as `Вакансия закрыта`, `Вакансия снята с публикации` or `Вакансия в архиве`;
- recurring duties are concrete and relevant to document/data/1C/EDO work;
- the record is not a duplicate of an already-counted vacancy.

Salary counts only when the exact detail page/metadata exposes an amount or range.

Observation date: `2026-09-18`.

## 2. Exact-page verified current records — Rabota.ru

| ID | Rabota.ru vacancy | Employer | Published | Salary shown | Exact-page recurring duties | Cluster |
|---|---|---|---|---:|---|---|
| R001 | `54284497` — Менеджер по документообороту | ООО «МИЛШПЕД» | 2026-08-29 | from 75k RUB/month | receive/check supplier primary docs; check/sort/scan/archive shipping docs; assemble customer document sets; create/maintain orders in 1C and control data/document status | document operations / 1C |
| R002 | `54337858` — Делопроизводитель | Центральный НИИ организации и информатизации здравоохранения Минздрава РФ | 2026-09-01 | up to 97k RUB/month | 1C:Документооборот; МЭДО; incoming/outgoing correspondence; electronic document flow; scanning/routing; document registers | document operations / EDO |
| R003 | `54380209` — Бухгалтер первички | Блумика | 2026-08-26 | from 90k RUB/month | full cycle of primary-document receipt/check/posting in 1C; counterparty reconciliation; marketplace closing-document control; TMC accounting | primary docs / 1C |
| R004 | `54409297` — Бухгалтер / Помощник бухгалтера на первичную документацию | Джейкет, сервис размещения объявлений | 2026-09-15 | 80–95k RUB/month | primary documents; ЭДО/СБИС; 1C:Комплексная Автоматизация | primary docs / 1C / EDO |

Exact pages:

- https://www.rabota.ru/vacancy/54284497/
- https://www.rabota.ru/vacancy/54337858/
- https://www.rabota.ru/vacancy/54380209/
- https://www.rabota.ru/vacancy/54409297/

## 3. Explicitly rejected Rabota.ru candidates

The same search pass found several apparently fresh search results whose exact pages were already closed.

These do **not** count:

| Vacancy | Search-page appearance | Exact-page result |
|---|---|---|
| `54357180` — Специалист по документообороту / Помощник бухгалтера | 80k RUB, relevant document role | `Вакансия снята с публикации` / `Вакансия в архиве` |
| `54296498` — Оператор 1С | 40–42k RUB | `Вакансия закрыта` / `Вакансия в архиве` |
| `54342074` — Специалист по сопровождению сделок и товарному учёту | from 100k RUB, 1C/МойСклад/ЭДО | `Вакансия снята с публикации` / `Вакансия в архиве` |

This again confirms that search-result freshness is insufficient for the current-vacancy gate.

## 4. Evidence-quality note

Rabota.ru exposes useful structured metadata including salary bounds, employer name and, for current indexed records, `datePosted`.

For current classification, the canonical rule remains stricter than metadata descriptions such as `свежая вакансия`:

> visible exact closure/archive wording overrides search snippets or generic fresh-vacancy metadata.

R002 had one automated extraction pass that inconsistently inferred an archive flag despite the exact direct-quote pass finding no archive/closure phrase and the page remaining indexed with its placement date. The corpus therefore relies on literal page evidence, not the extractor's inferred boolean.

## 5. What this tranche adds

New strict evidence:

- **4** current concrete Rabota.ru detail-page records;
- **4** salary-bearing records;
- a third strict public source: **Rabota.ru**.

The recurring work again converges on the same transaction-shaped stream:

`input document/order → validate → register/post in 1C or document system → assemble/send/route → reconcile/status → exception/correction`

This cross-source recurrence strengthens the case for benchmarking `one accepted realization/document package` rather than a whole job title.

## 6. Updated conservative gate state

Starting state after tranche 05:

- current relevant vacancies: `33/100`;
- reliable salary anchors: `27/50`;
- recurring function clusters: `8/8`;
- strict current concrete sources: `2`.

Tranche 06 adds:

- `+4` current vacancies;
- `+4` salary anchors;
- `+1` strict current public source.

Updated state:

| Gate | Required | Counted after tranche 06 | Remaining |
|---|---:|---:|---:|
| Current relevant vacancies | 100 | **37** | **63** |
| Reliable salary anchors | 50 | **31** | **19** |
| Recurring function clusters | 8 | **8** | **0** |
| Strict current concrete public sources | >=5 where accessible | **3: hh.ru + Zarplata.ru + Rabota.ru** | **2 additional source surfaces if accessible** |

## 7. Business implication

The third strict source reduces the risk that the order/document pattern is an artifact of one platform's taxonomy.

However it still proves only that Russian employers pay people for recurring document/data work.

It does not prove:

- buyers will externalize the stream;
- the stream is machine-executable at acceptable accuracy;
- customer verification cost is low enough;
- Arvectum Work beats employee + AI;
- Work beats owned 1C/EDO automation;
- a profitable transaction price exists.

Those remain later Discovery gates.

## 8. Next AUTO target

1. attempt a fourth strict source from Работа России / trudvsem or another accessible independent job surface;
2. continue exact current records toward `100 / 50`;
3. prioritize salary-bearing exact records until the salary gate closes;
4. separately continue searching for current numeric throughput in catalog/master-data;
5. never convert salary into unit price without a defensible throughput denominator.

No outreach, employer contact, application, commercial offer, deployment, spend or customer evidence occurred.
