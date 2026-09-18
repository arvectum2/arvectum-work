# AW-020 — Vacancy corpus tranche 05

Status: `Public-source evidence / exact-page verified / second strict source`  
Date: `2026-09-18`

Purpose: expand AW-020-C1 beyond hh.ru by promoting concrete current Zarplata.ru detail pages into the strict current-vacancy ledger.

## 1. Verification rule

A Zarplata.ru record in this tranche counts as `current at observation time` only when:

- the exact vacancy detail page loads successfully with HTTP 200;
- metadata describes a vacancy rather than an archive page;
- a literal search for archive wording such as `в архиве` / `вакансия в архиве` returns no match;
- the page exposes a publication date in September 2026;
- the page contains concrete recurring duties relevant to document/data/1C/EDO work.

Salary counts as a reliable salary anchor only when the exact vacancy page exposes an amount/range.

Observation date: `2026-09-18`.

## 2. Exact-page verified current records — Zarplata.ru

| ID | Vacancy | Employer | Published | Salary shown | Exact-page recurring duties | Cluster |
|---|---|---|---|---:|---|---|
| Z001 | `137395562` — Бухгалтер по первичной документации (удаленно) | ООО «Блю Вэйл» / Aivel | 2026-09-15 | 70k RUB/month net | receive/check primary docs; validate mandatory requisites; identify discrepancies; create nomenclature/counterparty cards and reflect receipts in 1C; reconciliations/EDO-related work | primary docs / 1C / validation |
| Z002 | `136531527` — Помощник бухгалтера | ООО «АКД» | 2026-09-17 | 40–65k RUB/month | input acts/invoices into 1C; bank-statement allocation; reconciliations; EDO | primary docs / 1C |
| Z003 | `137165696` — Бухгалтер | ООО «Крона» | 2026-09-15 | 80–100k RUB/month | accounting in 1C:UNF; receive/send documents through EDO; process primary documents | primary docs / EDO |
| Z004 | `137010548` — Бухгалтер, участок поставщиков и первички | Organic People | 2026-09-04 | 60–80k RUB/month | supplier settlements; collect primary docs; EDO; control closing documents; document cleanup/corrections | supplier docs / EDO |
| Z005 | `136971852` — Специалист по отчётности и документообороту | MEDIA GLOB | 2026-09-03 | from 50k RUB/month | receive/check/sign/scan/archive contracts; prepare acts; collect receipts/acts; maintain archives; structure grant-report documents | document operations |
| Z006 | `137486192` — Бухгалтер на первичную документацию | ООО «Руссторг» | 2026-09-17 | not shown | receive/control/process primary docs; supplier/customer reconciliations; create primary documents in 1C UNF; prepare UPD/account/MX forms for EDO; control returned originals/EDO | primary docs / 1C / EDO |

Exact pages:

- https://zarplata.ru/vacancy/137395562
- https://zarplata.ru/vacancy/136531527
- https://zarplata.ru/vacancy/137165696
- https://zarplata.ru/vacancy/137010548
- https://zarplata.ru/vacancy/136971852
- https://zarplata.ru/vacancy/137486192

## 3. Evidence quality notes

### 3.1 Source independence

Zarplata.ru shares parts of its platform infrastructure with hh.ru, but these are distinct public vacancy surfaces/domains and the AW-020 gate is defined as public-source coverage rather than independent corporate ownership.

Therefore this tranche counts Zarplata.ru as a second concrete public source, while preserving the limitation that platform infrastructure is related.

### 3.2 Archive-status discipline

No selected detail page contained explicit archive wording when re-scraped on 2026-09-18.

This is stronger than treating a category listing as current, but still only establishes status **at observation time**.

### 3.3 Salary qualifiers

The corpus uses salary amounts/ranges as displayed on the source page. Where net/gross qualification was clearly visible in the exact-page extraction it is retained; where the compact extraction did not preserve the tax qualifier, the ledger relies only on the numeric salary as a role-level budget anchor rather than normalizing it to employer cost.

No salary value in this tranche is treated as fully loaded employer cost or Work pricing.

## 4. What this tranche adds

New strict evidence:

- **6** current concrete vacancy records;
- **5** salary-bearing current records;
- strict current concrete-source coverage expands from **hh.ru only** to **hh.ru + Zarplata.ru**.

The records independently reinforce the same recurring operational pattern already seen on hh.ru:

`document arrives → validate required fields/requisites → reflect in 1C/ERP → EDO / status / reconciliation → exception or correction`

This strengthens evidence that the pattern is not an artifact of one hh.ru search category.

## 5. Notable strategic signal: Aivel / Блю Вэйл

Z001 is especially useful as a substitute signal.

The employer explicitly describes itself as building a technology-led accounting outsourcing model with its own AI platform and AI agents, while still recruiting a human primary-document accountant.

That supports two opposing interpretations that must both remain live:

1. the document stream is real, repeated and important enough to justify dedicated labor;
2. AI-enabled incumbents may already be compressing the same labor, making `employee + automation` / managed AI accounting a strong substitute for Arvectum Work.

Therefore Z001 is **not** evidence that Work has an advantage. It is evidence that the competitive baseline may already include AI-assisted managed accounting.

## 6. Updated conservative gate state

Starting canonical ledger before this tranche:

- current relevant vacancies: `27/100`;
- reliable salary anchors: `22/50`;
- recurring function clusters: `8/8`;
- strict current concrete sources: `1`.

Tranche 05 adds:

- `+6` current vacancies;
- `+5` salary anchors;
- `+1` strict current concrete public source.

Updated state:

| Gate | Required | Counted after tranche 05 | Remaining |
|---|---:|---:|---:|
| Current relevant vacancies | 100 | **33** | **67** |
| Reliable salary anchors | 50 | **27** | **23** |
| Recurring function clusters | 8 | **8** | **0** |
| Strict current concrete public sources | >=5 where accessible | **2** | **3 source surfaces still needed if accessible** |

## 7. Next AUTO target

Continue the promotion pipeline:

`candidate observation → detail page → current/archive check → dedupe → salary → atomic duties → ledger increment`

Priority order:

1. extract concrete current Rabota.ru detail pages to establish a third strict source if accessible;
2. continue exact current Zarplata.ru/hh.ru records toward `100 / 50`;
3. seek numeric throughput in catalog/master-data rather than confusing catalog size with processing rate;
4. preserve the current salary+throughput Pioner anchor as calibration, not pricing;
5. keep searching for direct-employer/process evidence where public vacancies omit throughput.

No outreach, employer contact, application, commercial offer, deployment, spend or customer evidence occurred.
