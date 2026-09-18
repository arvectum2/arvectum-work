# AW-020 — Current vacancy corpus ledger

Status: `Canonical conservative gate ledger`  
Date: `2026-09-18`

Purpose: maintain one deduplicated counter for the formal AW-020-C1 gates after the source-quality rules became stricter.

## 1. Counting rule

A record counts toward `>=100 relevant current vacancies` only when the canonical research artifact already classifies it as a concrete current vacancy rather than:

- a category/search page observation;
- a provisional current/recent candidate awaiting exact-page status verification;
- an archived vacancy;
- a duplicate re-verification of an already-counted vacancy;
- source-level corroboration without a concrete vacancy record.

A record counts toward `>=50 reliable salary anchors` only if the same counted current vacancy exposes a salary amount/range.

This ledger is intentionally conservative. It can undercount older observations rather than inflate the gate.

## 2. Counted current records

### 2.1 Tranche 02 — C035–C051

Canonical source:
`docs/research/AW-020-VACANCY-CORPUS-TRANCHE-02.md`

The artifact explicitly labels these 17 rows as:

`Current active sample — September 2026`

Counted current vacancies: **17**

Salary-bearing:
- C035
- C036
- C037
- C038
- C039
- C040
- C041
- C042
- C043
- C044
- C045
- C046
- C047
- C048

Salary anchors: **14**

Salary unknown:
- C049
- C050
- C051

### 2.2 Tranche 04 — exact-page verified C052–C059 equivalents

Canonical source:
`docs/research/AW-020-VACANCY-CORPUS-TRANCHE-04.md`

Tranche 04 exact-page verifies the eight provisional roles introduced as C052–C059 in tranche 03. They are counted **once**, here, not again from tranche 03.

| hh.ru vacancy | Employer / role shorthand | Salary? |
|---|---|---|
| 137357096 | Мартфарм — Оператор 1С (документооборот) | yes |
| 136893634 | Сфера Эстетики — Оператор 1С / сопровождение заказов | yes |
| 137035900 | Торговый Дом МАФ — ввод данных в 1С | yes |
| 137110041 | Ситилаб — НСИ / каталог | yes |
| 137320977 | ЛБТ — маркировка | yes |
| 136588879 | АНАЛИТИКА — маркировка | no |
| 137062000 | Наос Восток — Честный знак | no |
| 136979178 | Лотте КФ Рус — младший специалист по маркировке | yes |

Counted current vacancies: **8**

Salary anchors: **6**

### 2.3 Throughput-cost corpus 02

Canonical source:
`docs/research/AW-020-THROUGHPUT-COST-CORPUS-02.md`

New unique current records:

| hh.ru vacancy | Employer | Salary | Numeric throughput |
|---|---|---:|---|
| 136761302 | Пионер | 90–110k RUB/month | 15–20 realizations/day |
| 136775615 | РуссКом | from 100k RUB/month | up to 50 signed primary-document sets/day |

Counted current vacancies: **2**

Salary anchors: **2**

### 2.4 Tranche 05 — exact-page verified Zarplata.ru records

Canonical source:
`docs/research/AW-020-VACANCY-CORPUS-TRANCHE-05.md`

New unique current records from the second strict public source:

| Zarplata.ru vacancy | Employer | Salary? |
|---|---|---|
| 137395562 | Блю Вэйл / Aivel | yes |
| 136531527 | АКД | yes |
| 137165696 | Крона | yes |
| 137010548 | Organic People | yes |
| 136971852 | MEDIA GLOB | yes |
| 137486192 | Руссторг | no |

Counted current vacancies: **6**

Salary anchors: **5**

### 2.5 Tranche 06 — exact-page verified Rabota.ru records

Canonical source:
`docs/research/AW-020-VACANCY-CORPUS-TRANCHE-06.md`

New unique current records from the third strict public source:

| Rabota.ru vacancy | Employer / listing | Salary? |
|---|---|---|
| 53732012 | ООО «ИМТЭК» — Оператор 1С | yes |
| 53653417 | ООО «Альфатранснефть» — Бухгалтер-оператор | yes |
| 53722270 | Brainbox — Контент-менеджер | yes |
| 51555925 | ИП Рузавин А. Г. — Контент-менеджер | yes |
| 46879339 | ИП Степанов М. В. — Оператор ПК / контент-менеджер | yes |
| 54245470 | ООО «ГУДТРАНС» — Оператор ПК | yes |
| 54260476 | ООО «АЗАЛИЯ» — Оператор ПК | yes |
| 54370668 | ООО «ТАНИО» — Оператор ПК | yes |
| 54396705 | ООО «МА Рейн» via Jobers — Оператор ввода данных | yes |
| 54404206 | РА ВНТА — Оператор базы данных | yes |
| 54202752 | ИП Пантелеев А. Р. — Менеджер по маркетплейсам | yes |
| 54315352 | ИП Садаков С. Н. — Менеджер-аналитик маркетплейсов | yes |
| 52115774 | ИП Гулянский И. Ю. — Менеджер по маркетплейсам | yes |
| 54256140 | «Генацвале на Арбате» — Бухгалтер-калькулятор | yes |

Counted current vacancies: **14**

Salary anchors: **14**

Important: tranche 06 explicitly decomposes every record into a machine-work slice and residual human/accountability slice. R012's `300+ SKU` is scope evidence only and is not treated as processing throughput.

## 3. Explicit exclusions from the current counter

### Tranche 01

`docs/research/AW-020-VACANCY-CORPUS-TRANCHE-01.md` contains 34 useful public observations across hh.ru, Rabota.ru, Zarplata.ru and SuperJob, but its own method states that records can be vacancy/search-index observations.

Because later source-quality rules require concrete current records, tranche 01 is retained for function/source coverage and salary-market context but **does not automatically add 34 to the current-vacancy gate**.

Individual tranche-01 observations may be promoted later only after concrete-page/current verification.

### Tranche 03 provisional records

C052–C059 are not added separately because tranche 04 is the exact-page re-verification of those same eight roles.

### Archived workload records

Excluded from the current gate:

- hh.ru 130253648 — 40,000 rows/day, archived from 2025-10-06;
- hh.ru 136890934 — ~600 product cards/month, archived;
- hh.ru 135538575 — 10 supplier + 4–6 buyer documents/day, archived from 2026-09-11.

They remain historical throughput/persistence calibration only.

## 4. Conservative gate state

As of 2026-09-18:

| Gate | Required | Conservatively counted | Remaining |
|---|---:|---:|---:|
| Current relevant vacancies | 100 | **47** | **53** |
| Reliable salary anchors on counted current vacancies | 50 | **41** | **9** |
| Recurring function clusters | 8 | **8** | **0** |
| Current concrete-source coverage | >=5 public sources where accessible | **3 strict sources: hh.ru + Zarplata.ru + Rabota.ru** | **2 additional source surfaces if accessible** |

Important distinction:

- broader public-source coverage already exists across hh.ru, Rabota.ru, Zarplata.ru, SuperJob and Работа России/trudvsem;
- strict **current concrete counted records** now exist on hh.ru, Zarplata.ru and Rabota.ru;
- SuperJob and Работа России/trudvsem still require promotion to concrete current detail-page evidence where technically accessible.

Do not claim the five-source current-record gate complete from source-level corroboration alone.

## 5. What this means for the next AUTO work

The fastest honest path is not another broad search-summary document. It is a promotion pipeline:

`candidate observation → exact/concrete vacancy → current/archive check → dedupe → salary extraction → atomic duties → ledger increment`

Priorities:

1. close the remaining salary-anchor gap (9 records) without weakening source-quality rules;
2. continue exact current Rabota.ru, Zarplata.ru and hh.ru records toward 100 current vacancies;
3. attempt a fourth strict source, prioritizing Работа России/trudvsem exact records where technically accessible;
4. keep current throughput anchors separate from salary-only records and do not treat portfolio size as throughput;
5. never count an archived or provisional record toward the gate.

## 6. Evidence boundary

The ledger measures public paid-labor evidence only.

It does not establish:
- buyer willingness to outsource;
- willingness to pay Arvectum Work;
- machine-executable share;
- acceptance rate;
- Work contribution margin;
- repeat purchase.

No employer contact, application, outreach, commercial offer, deployment, spend or customer evidence occurred.
