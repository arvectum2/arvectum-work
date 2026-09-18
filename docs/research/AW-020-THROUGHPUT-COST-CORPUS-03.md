# AW-020 — Throughput / cost evidence corpus 03

Status: `Public-source calibration / mixed current + recent historical evidence`  
Date: `2026-09-18`

Purpose: test whether catalog/master-data work now has a defensible numeric throughput denominator and identify the strongest substitute signal for the `buy Work vs own automation` comparison.

## 1. Evidence table

| Evidence | Status at observation | Numeric throughput / scale | Compensation | What it supports | Limitation |
|---|---|---:|---:|---|---|
| Kadrout 39101 — “Наполнять карточки на маркетплейсах” | current public page dated 2026-09-07; no archive marker observed | “в день можно 10 карточек делать” | page shows 800–3200 RUB and says “1 проверенная категория товаров = 800 рублей” | current public evidence that a bounded card-check/fill workflow is expressed with a daily numeric volume | compensation unit is internally ambiguous (`category` vs `card`), employer is not identified, Kadrout disclaims responsibility for off-platform cooperation; do **not** derive RUB/card or monthly salary-equivalent |
| ПравЖизнь — technical content manager, AI-first | published 2026-07-01; mirrors say original hh window ended 2026-08-30, so recent historical / expired rather than current | target: 25 collections × 1500 cards in 2 months = **37,500 cards / 2 months**; 1500+ cards per collection; 100+ collections in pipeline | salary not stated | exceptionally strong substitute/process signal: an employer explicitly describes a Python + Flask + Excel + AI production pipeline for mass card generation/validation/upload | target/plan, not observed accepted throughput; no salary; original vacancy window expired; do not treat as current salary+throughput pair |
| Kadrout 31467 / Workzilla 339322 — specialist for WB cards | March 2026 / Workzilla copy currently archived | 80–150 cards/month; text also says 10–15/day | 80–250 RUB/card, average 150 RUB | historical per-unit market calibration for a checklist-driven card workflow | timing arithmetic is internally inconsistent; duplicated wording across Kadrout/Workzilla suggests syndication; Workzilla marks archive |
| Mark Formelle 136890934 | archived | ~600 cards/month | 110–140k RUB/month net | recent historical role-level salary + throughput calibration | archived; whole-role salary is not card process cost or Work price |

## 2. Derived quantities that are safe to compute

### 2.1 ПравЖизнь target scale

The listing states:

`25 collections × 1500 cards / 2 months`

Arithmetic only:

- target cards: `25 × 1500 = 37,500`;
- nominal target average: `37,500 / 2 = 18,750 cards/month`.

This is a **pipeline target**, not measured throughput of one worker and not accepted-result evidence.

The same listing describes:
- an existing `Python + Flask + Excel-generator`;
- a four-stage `content → photo → files → upload` pipeline;
- structured fields and uploads into 1C / WB / Ozon / Yandex Market;
- validation for duplicate articles, field correctness and marketplace requirements;
- AI as a core production tool rather than optional assistance.

That makes it directly relevant to the mandatory owned-automation substitute for Arvectum Work.

### 2.2 Why no current RUB/card estimate is promoted

Kadrout 39101 is current enough to provide a daily volume phrase, but its compensation wording mixes:
- `1 checked category = 800 RUB`;
- `10 cards/day`;
- header range `800–3200 RUB`.

The unit mapping is not explicit. Any conversion to RUB/card would require an assumption not present in the source.

Therefore no current card unit-cost estimate is promoted from this record.

## 3. Evidence-quality finding: syndication risk

The older Kadrout card-specialist page and the archived Workzilla page reproduce materially identical:
- duties;
- `80–150 cards/month`;
- `10–15/day`;
- `80–250 RUB/card`, average `150 RUB`.

They must be treated as one underlying market observation or an unknown syndicated lineage, **not two independent confirmations**.

This reinforces the corpus rule already adopted for Dream Job/hh.ru: public source-surface diversity does not imply data independence.

## 4. Discovery implication

Catalog/master-data becomes more strategically interesting but also more exposed to the `own automation` substitute.

The evidence now supports:

1. **bounded unit exists** — a product-card check/fill/update can be specified and counted;
2. **numeric volume exists in current public work** — up to 10 cards/day is stated on a September 2026 public page;
3. **mass automation is already an explicit employer strategy** — the ПравЖизнь role is built around AI + scripts + structured pipelines at tens-of-thousands-of-cards target scale;
4. therefore Arvectum Work cannot win merely by “using AI to create cards”. It must offer a lower-friction accepted-result service where the buyer avoids owning/operating the pipeline.

This is exactly the product comparison required by Product Decision 001:

`employee + AI` vs `buy Arvectum Work` vs `own automation`.

## 5. Gate conclusion

The strict missing evidence remains:

**No clean current exact-status employee salary + numeric catalog-card throughput pair is established.**

What is now established:
- current numeric catalog-work volume evidence: **yes, weak/low-confidence gig source**;
- recent historical salary + throughput calibration: **yes**;
- recent explicit AI-first owned-automation scale target: **yes, strong substitute/process signal**;
- current clean salary + throughput pair: **no**;
- buyer willingness to pay Arvectum Work: **no evidence**.

Do not convert this artifact into Work pricing.

## 6. Next evidence action

For AW-020-C1:
- continue exact current vacancy quantity toward 100 without over-concentrating on one syndicated source;
- prefer direct employer pages, current hh/Zarplata/Rabota/Svoe records and other exact sources;
- keep searching for a current **salary + explicit cards/day or cards/month** pair;
- carry ПравЖизнь into the top-candidate owned-automation crossover model as a concrete substitute example.

No outreach, application, customer contact, commercial commitment, spend or deployment occurred.
