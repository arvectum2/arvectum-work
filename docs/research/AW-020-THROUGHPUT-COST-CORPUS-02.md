# AW-020 — Throughput + cost corpus 02

Status: `Public-source evidence / first current deterministic throughput anchors`  
Date: `2026-09-18`

Purpose: continue the stricter throughput-cost layer after corpus 01 and identify **current** salary + numeric throughput pairs for the leading deterministic Arvectum Work candidates.

## 1. What changed

Corpus 01 concluded that no clean current salary + throughput pair had yet been established for the leading deterministic streams.

This pass changes that conclusion for **order-to-document / primary-document processing**.

Two hh.ru vacancies pass the current-status rule at observation time:

1. exact vacancy page returns HTTP 200;
2. metadata title contains no archive wording;
3. publication date is visible;
4. salary and workload belong to the same role;
5. workload unit is a document/realization flow rather than physical warehouse throughput.

A third apparently strong example was rejected from current evidence because exact-page metadata explicitly marks it archived.

## 2. T003 — Пионер: primary documents / realizations

hh.ru vacancy: `136761302`  
Employer: ООО «Пионер»  
Role: Бухгалтер на первичную документацию  
Publication date: `2026-08-31`  
Exact-page status at observation: `HTTP 200; no archive wording in title/metadata`  
Salary: `90,000–110,000 RUB/month`  
Schedule: `5/2`  
Explicit workload: `15–20 realizations/day`

Observed work:

- reflect primary documents in 1C:UT / 1C:EDO;
- form UPD;
- process `15–20 realizations/day`;
- upload payment orders into 1C:UT;
- perform related document/accounting operations.

Source:
https://hh.ru/vacancy/136761302

### 2.1 Why this is material

This is the first current public pair in the corpus that directly connects:

`monthly human salary ↔ bounded digital document-flow throughput`

The unit is not an abstract “employee”. It is close to a Work-compatible operational unit:

`realization request/data → validate → create/update realization → form UPD → record/send/status → exception`

### 2.2 Salary-equivalent calibration

September 2026 contains 22 Monday–Friday weekdays. If the published `5/2` schedule is used only as a **nominal calibration assumption**, the stated daily volume corresponds to:

- `15 × 22 = 330 realizations/month`;
- `20 × 22 = 440 realizations/month`.

Dividing the stated monthly salary by that nominal volume gives a whole-role salary-equivalent range of approximately:

- `90,000 / 440 ≈ 205 RUB per realization`;
- `110,000 / 330 ≈ 333 RUB per realization`.

Therefore the public vacancy supports a rough **205–333 RUB/realization salary-equivalent calibration** under the stated nominal schedule.

This is **not** a Work price or employer process cost. It over-allocates the whole salary to the realization stream and excludes employer payroll burden, software, management, exception handling and other role duties.

The economically useful conclusion is narrower:

> a current employer is publicly budgeting roughly a six-figure monthly salary for a role whose core description includes a measured 15–20 realization/day digital document stream.

## 3. T004 — РуссКом: returned primary-document sets

hh.ru vacancy: `136775615`  
Employer: Группа компаний «РуссКом»  
Role: Бухгалтер  
Publication date: `2026-08-31`  
Exact-page status at observation: `HTTP 200; no archive wording in title/metadata`  
Salary: `from 100,000 RUB/month`  
Schedule: `5/2`  
Explicit workload: `up to 50 signed primary-document sets/day`

Observed work includes control of returned signed customer primary documents, archive/dispatch operations and broader accounting duties.

Source:
https://hh.ru/vacancy/136775615

### 3.1 Interpretation

This is a second current salary + throughput pair, but it is weaker for direct automation economics than T003:

- `up to 50` is a ceiling, not an average;
- the role contains substantial accounting duties outside document-return control;
- the flow may mix electronic and physical originals;
- final legal/accounting accountability remains human.

At the stated ceiling, a nominal 22-weekday month would be `up to 1,100 sets/month`. Using only the published salary floor would yield roughly `91 RUB/set` at that ceiling, but that number is **not a representative unit cost** and MUST NOT be used as pricing evidence.

The useful evidence is that document-closure work is explicitly countable at tens of sets per workday and sits inside a paid current role.

## 4. T005 — Царь-Макет: rejected from current evidence

hh.ru vacancy: `135538575`  
Employer: ЧУ «Музей Царь-Макет Страны»  
Role: Бухгалтер  
Salary: `100,000–120,000 RUB/month`  
Explicit workload:

- supplier primary documents: `10/day`;
- buyer primary documents: `4–6/day`.

Exact-page metadata explicitly says:

`вакансия в архиве c 11 сентября 2026`

Therefore T005 is **historical/recent calibration only** and does not count toward the current-vacancy target.

Source:
https://hh.ru/vacancy/135538575

This rejection validates the exact-page rule: a fresh-looking search result can still be archived.

## 5. What the new anchors do and do not prove

### They do support

- current paid labor demand for document-processing streams;
- explicit digital throughput at `15–20 realizations/day`;
- explicit document-closure throughput of up to `50 sets/day`;
- the ability to define a per-realization or per-document-set Work unit;
- a public salary-equivalent order-of-magnitude baseline for later benchmarking.

### They do not support

- buyer willingness to outsource;
- willingness to pay Arvectum Work;
- full automatable share of either role;
- required accuracy/SLA;
- exception rate;
- current employee use of ChatGPT/AI;
- fully loaded employer cost;
- Work execution/verification cost;
- customer residual verification cost;
- a commercial price.

## 6. Business implication

The evidence now makes the leading candidate more concrete.

Instead of selling:

> “AI accountant” or “agent for 1C”

the first Work benchmark can be framed as a bounded processing stream such as:

> **Process N realization packages from validated source data into a structured 1C/EDO-ready result with UPD, evidence, exception list and acceptance checks.**

Possible unit:

`one accepted realization package`

Potential acceptance evidence:

- required fields complete;
- source-to-result trace;
- arithmetic/requisite validation;
- UPD generated according to frozen template/rules;
- no unsupported values invented;
- exception flagged instead of silently resolved;
- status/evidence record attached.

This is materially closer to the Arvectum Work thesis than whole-role replacement.

## 7. Employee + ChatGPT test

The current public anchor does not by itself prove Work beats an employee using ChatGPT.

For this stream, buyer validation must specifically measure:

1. how much of 15–20 realizations/day is already accelerated by 1C rules, OCR, templates or general-purpose AI;
2. how many minutes of human attention remain per realization;
3. what share goes to exception handling, communication and accountability;
4. whether a third-party Work service reduces that residual burden enough to justify transaction price and integration cost.

If an employee + existing software can handle the stream cheaply with little management burden, Work loses.

## 8. Owned-automation crossover test

T003 also gives a better denominator for the owned-automation alternative.

A buyer with a stable `~330–440 realizations/month` nominal stream may rationally prefer its own 1C automation if:

- schema/process is stable;
- integration is easy;
- exceptions are low;
- volume persists long enough to amortize implementation/support.

Work remains plausible where:

- volume is variable or bursty;
- process changes;
- automation backlog is expensive;
- evidence/verification/exception handling matter;
- buyer does not want to own another narrow automation.

This remains a hypothesis until real buyer/process data exists.

## 9. AW-020-C1 implication

AW-020-C1 remains **ACTIVE**.

New evidence state:

- at least one strong current deterministic salary + throughput pair now exists for the leading `order-to-document` candidate (T003);
- a second current pair supports document-closure throughput but has weaker unit-economics interpretability (T004);
- exact-page archive verification continues to reject false-current records (T005);
- no equivalent current salary + throughput pair has yet been established for unregulated catalog/master-data.

Next public-source priority:

1. continue exact current vacancy and salary collection toward the explicit corpus gates;
2. seek another independent current order/document throughput pair;
3. seek current numeric throughput for catalog/master-data;
4. preserve current-vs-archived separation;
5. do not turn salary-equivalent ratios into Work pricing.

No outreach, employer contact, application, commercial offer, pricing commitment, deployment or spend occurred.
