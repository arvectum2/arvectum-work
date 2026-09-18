# AW-020 — Throughput + cost corpus 01

Status: `Public-source evidence / partial / no current unit-cost proof yet`  
Date: `2026-09-18`

Purpose: test whether public Russian vacancy evidence can support a defensible **cost-per-unit** baseline for candidate Arvectum Work streams by finding records where a single role exposes both:

1. a salary/cost anchor; and
2. an explicit workload volume with a time period.

This artifact is deliberately stricter than the broader vacancy corpus. A role with salary but no throughput does not produce a unit-cost anchor. A role with throughput but archived status does not count as current demand.

## 1. Evidence rule

A record can support a **current throughput-cost anchor** only if all of the following are observable:

- role and employer;
- salary amount and whether it is gross/net where stated;
- explicit numeric workload;
- explicit workload period (day/week/month);
- the workload belongs to the same role as the salary;
- current status is independently supportable at observation time;
- the unit is relevant to a digital work stream rather than physical warehouse/production throughput.

Derived ratios are labelled only as salary-equivalent ratios. They are **not** treated as fully loaded process cost, Work price, buyer WTP, or automatable savings.

## 2. Candidate T001 — marketplace product cards

### Observable source evidence

hh.ru vacancy id: `136890934`  
Employer: Марк Формэль  
Role: Контент-менеджер  
Publication date reproduced by third-party mirror: `2026-09-02`  
Salary: `110,000–140,000 RUB/month net`  
Explicit workload: `approximately 600 product cards/month`

The same vacancy describes additional duties beyond initial card creation, including media upload, SEO/attributes, rich content, brand-zone banners, and rework of older cards.

Sources:

- exact vacancy URL discovered in indexed public search: https://hh.ru/vacancy/136890934
- archived-status mirror: https://dreamjob.ru/employers/205182/vakansii/136890934
- second public reproduction of duties: https://moscow.cataloxy.ru/rabota/vacancy1128650517_kontent-menedzher.htm

### Status correction

The strongest mirror explicitly labels the vacancy **archived**.

Therefore T001 is **historical/recent workload evidence only** and MUST NOT count toward the current-vacancy target.

### Derived salary-equivalent ratio

Using the stated role salary and stated monthly card volume:

- lower bound: `110,000 / 600 ≈ 183 RUB/card`;
- upper bound: `140,000 / 600 ≈ 233 RUB/card`.

Interpretation boundary:

> `183–233 RUB/card` is only the net-salary-equivalent ratio of this whole role divided by the stated creation volume.

It is **not** the employer's real cost per accepted card because:

- salary is stated net, not employer fully-loaded cost;
- the employee performs multiple duties beyond creating new cards;
- some work may involve judgment, SEO, creative formatting and rework;
- acceptance/error rate is unknown;
- customer-side management and tooling costs are unknown.

This record is still useful because it demonstrates that a buyer-side role can be expressed simultaneously in salary and monthly digital throughput.

## 3. Candidate T002 — short-form video throughput

Employer: Stellar Beauty Clinic  
Role: SMM specialist / Visual Content Creator  
Salary visible in current hh.ru search results: `from 75,000 RUB/month gross`  
Explicit workload: `5–15 Reels / Shorts / Clips per day`

Sources:

- public role reproduction: https://h.careers/job/c6edf2d4-5a4c-4a51-9f3c-481db44654cc
- hh.ru search surface observed 2026-09-18: https://hh.ru/vacancies/kontent_menedzher/chastichnaya_zanyatost

### Classification

T002 is retained as **throughput-pattern evidence**, not as a primary Arvectum Work unit-cost anchor.

Reasons:

- the output is creative audiovisual work rather than a deterministic data/document stream;
- quality is heavily subjective;
- exact vacancy archive/current status was not independently verified from the exact hh page;
- daily working-day denominator is not stated.

It shows that public vacancies sometimes publish explicit digital production quotas, but it does not justify pricing a machine-work stream.

## 4. Negative evidence from leading Work clusters

A targeted pass over current/recent vacancy search results found many salary-bearing digital operational roles but usually **no explicit throughput denominator**.

Examples observed on hh.ru search surfaces:

| Role | Salary signal | Digital work signal | Why rejected for unit-cost calculation |
|---|---:|---|---|
| Бухгалтер на первичную документацию / оператор 1С — Автомиг | 100–140k net/month | primary docs, reconciliations, archive | no documents/day or month |
| Оператор 1С / ассистент отдела продаж — Сити-Эл | from 170k gross/month | 1C primary documents, reconciliations | no orders/documents throughput |
| Оператор 1С — ЭКЗО | 60–80k net/month | receipts/sales docs, EDI/EDO, document packages | no package/order count |
| Оператор 1С (Управление торговлей) — Ветсовет | 80–100k net/month | orders, realizations, returns, counterparty cards | no transactions/day or month |
| content / marketplace roles | many salary anchors | product-card creation/update | usually "large volume" without numeric period |

Representative current search surfaces observed 2026-09-18:

- https://hh.ru/vacancies/operator-na-pervichnuyu-dokumentatsiyu/za_sutki
- https://hh.ru/vacancies/spetsialist-po-podgotovke-dokumentov/polniy_den
- https://hh.ru/vacancies/deloproizvoditel-dokumentoved
- https://hh.ru/vacancies/kontent-menedzher-internet-magazina
- https://hh.ru/vacancies/dizajner-kartochek-dlya-marketpleysov/ot_pryamih_rabotodateley

This is not absence of throughput in the real process. It is evidence that **vacancy text is a poor public source for the denominator required by unit economics**.

## 5. What this changes

### 5.1 Public vacancies are strong for role-cost and function evidence

The broader AW-020 corpus remains useful for:

- proving that companies currently pay humans for repeated 1C/document/catalog work;
- identifying recurring atomic functions;
- locating salary budget anchors;
- narrowing the leading streams.

### 5.2 Public vacancies are weak for real unit economics

For the leading candidates, the missing fields are usually:

- orders/documents/rows per day or month;
- peak vs normal volume;
- accepted vs rejected output;
- rework rate;
- time spent on exceptions;
- share of role time attributable to the bounded stream;
- current ChatGPT/AI usage and residual human work;
- fully loaded employer process cost.

Therefore:

> **Do not infer Work price per unit from salary alone.**

The economically relevant denominator must come from real process evidence, not title-level vacancy data.

### 5.3 Historical T001 still gives an order-of-magnitude clue

The archived Mark Formelle record suggests that a human-operated marketplace-card role can be tied to hundreds of cards per month while carrying a six-figure monthly salary.

That is useful for selecting a benchmark, but not enough to claim a current market price.

## 6. Implication for AW-020-C1

This pass does **not** close AW-020-C1.

It adds a new evidence rule:

- salary anchors continue to count toward the role-cost corpus when current and reliable;
- workload-volume observations are stored separately;
- a cost-per-unit benchmark requires both values on the same defensible process record;
- archived salary+volume pairs remain historical calibration only;
- physical warehouse throughput must not be substituted for digital machine-work throughput.

Current conclusion:

> **No clean current, exact-status-verified salary + throughput pair for the three leading deterministic Work streams was established in this pass.**

That negative result is important. It prevents false precision in the synthetic commercial models.

## 7. Next evidence target

Continue AW-020-C1 with two parallel public-source tracks:

1. keep expanding current exact vacancy + salary records toward the corpus acceptance gate;
2. specifically search direct employer career pages, operational case studies, SLA/process descriptions and role postings that disclose numeric digital throughput.

When buyer validation is later authorized, the interview kit must ask the missing denominator directly:

`monthly accepted units + peak units + current process cost + residual human verification + exception rate`.

No outreach, employer contact, vacancy application, commercial offer or pricing commitment occurred in this pass.
