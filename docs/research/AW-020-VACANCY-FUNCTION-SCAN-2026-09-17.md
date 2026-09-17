# AW-020 — Vacancy Function Scan / paid-work demand proxy

Status: `Discovery evidence / public-source proxy`
Date: `2026-09-17`
Scope: Russia-first, initial Moscow-heavy sample

## 1. Why this exists

Arvectum Work should not begin by asking companies whether they "like AI". A job vacancy is stronger public evidence that a company already allocates money to a recurring function.

This scan uses current vacancy postings as a **proxy for existing labor budget and operational pain**. It does **not** prove that an employer would outsource the function to Arvectum Work, accept autonomous execution, or pay the proposed price.

The analytical unit is not the job title. It is the **atomic recurring function inside the vacancy**.

Example:

`Бухгалтер на первичную документацию` is too broad to call automatable as a whole.

But the recurring slice:

`receive UПД/ТОРГ-12 → validate required fields → reconcile against system data → enter/prepare import → flag exceptions`

may be a candidate Work stream.

## 2. Source and interpretation rules

Initial sources checked on 2026-09-17:

- hh.ru current vacancy/search pages;
- Rabota.ru current/search pages;
- Zarplata.ru current/search pages where available.

Search-result counts are noisy: they can include adjacent roles and duplicated/cross-listed positions. They are directional evidence only.

Salary shown in a vacancy is a **conservative lower-bound cost anchor**, not the employer's full cost. Employer taxes, benefits, recruiting, management, equipment, vacancy downtime and training are not added here unless separately evidenced.

## 3. Initial observed function clusters

### F-01 — Primary documents / 1C reconciliation

Observed public signals:

- hh.ru search for `бухгалтер первичной документации` showed roughly 2,000 Moscow vacancies in the current index snapshot;
- examples observed at 100–130k RUB net, 125–140k RUB gross, 150k RUB net and other ranges;
- recurring duties include receiving, validating and entering UПД, ТОРГ-12, ТТН, acts, invoices and reconciliation data into 1C/ЭДО.

Representative current examples:

- `Бухгалтер на первичную документацию`, 100–130k RUB net: receive/check/enter primary documents into 1C;
- `Бухгалтер на первичную документацию`, 125–140k RUB gross: collect/systematize primary documents, check records, create invoices/UПД;
- `Оператор 1С / менеджер документооборота`, 90–100k RUB net: prepare UПД/ТТН, receipts/issues/transfers, check marketplace supplies;
- logistics document specialist, ~80–100k RUB net: reconcile `1C ↔ primary documents ↔ electronic transport waybill`.

Candidate Work stream:

`Incoming primary-document stream → validation → reconciliation → normalized import/output → exception queue`

Potential automation path:

1. ingest PDF/XML/XLSX/ЭДО export;
2. classify document type;
3. extract identifiers, dates, parties, amounts, VAT, item lines;
4. validate required fields and arithmetic;
5. reconcile against order/contract/1C export;
6. prepare import or structured posting proposal;
7. route mismatches/ambiguous cases to exception queue;
8. preserve evidence for every material field.

What must remain human or separately governed initially:

- accounting-policy judgment;
- consequential posting where rules are ambiguous;
- dispute/claim decisions;
- final professional responsibility where required.

Initial fit: **very strong**.

### F-02 — Logistics document closure / transport document reconciliation

Observed public signals:

- current hh.ru examples at roughly 80–100k RUB net;
- recurring duties include closing every trip with correct documents, checking 1C against source documents and electronic transport records, maintaining registers and missing-document control.

Candidate Work stream:

`Completed trip → collect document pack → reconcile identifiers/amounts/statuses → detect missing/inconsistent documents → close clean cases → exception queue`

Potential automation path:

- monitor source folders/exports;
- match trip/order/document IDs;
- compare 1C/TMS/ЭТрН fields;
- generate completeness status;
- chase only via explicitly authorized channels later; initial Work can stop at exception creation;
- produce daily closure register.

Initial fit: **very strong**, because acceptance is largely deterministic and volume can be high.

### F-03 — Product/catalog data validation and normalization

Observed public signals:

- current hh.ru examples around 80–85k RUB gross for checking price lists/product data;
- duties explicitly include checking prices, descriptions and attributes, finding mistakes/duplicates, updating internal tables/systems and keeping the product base current;
- content-card roles were also observed around 50–60k RUB net for templated creation/filling of product cards.

Candidate Work stream:

`Supplier/catalog feed → normalization → duplicate detection → attribute validation → change set → exception queue`

Potential automation path:

1. ingest supplier Excel/CSV/XML/site data;
2. normalize units/brands/articles/categories;
3. deduplicate;
4. compare against current master data;
5. flag impossible/ambiguous values;
6. produce accepted update package and provenance.

Initial fit: **very strong** for validation/normalization; **medium** for creative descriptions because quality becomes subjective.

### F-04 — Order processing / operator 1C

Observed public signals:

- current hh.ru examples around 80–90k and 90–120k RUB net;
- current Rabota.ru listings/searches show operator 1C roles from about 60–80k upward, with some higher ranges;
- duties include receiving and processing orders, creating UПД/shipping documents, entering orders, supplier orders and reports.

Candidate Work stream:

`Structured incoming order → validate → enter/prepare system transaction → generate documents → exception queue`

Potential automation path:

- ingest e-mail/form/EDI order;
- extract customer/items/quantity/delivery terms;
- validate master data, availability and price rules;
- create proposed 1C order/import;
- generate invoice/UПД draft when rules allow;
- route pricing/availability/contract exceptions.

Constraint:

Many operator vacancies mix deterministic order processing with phone calls, negotiation and customer service. Work should target the deterministic slice first, not claim full role replacement.

Initial fit: **strong for the transaction-processing slice**.

### F-05 — Tender/procurement document operations

Observed public signals:

- hh.ru career page currently reports a broad salary range of ~56–133k RUB for tender specialists;
- current vacancy examples include 170k, 180k and 200k+ RUB offers for experienced tender work;
- Zarplata.ru showed current/near-current examples from ~90k to 200k+ RUB depending on responsibility and experience.

Candidate Work streams:

- monitoring selected sources for relevant opportunities;
- extracting deadlines/requirements/quantities;
- building a requirement matrix;
- comparing a supplier's declared capability to the specification;
- preparing a document checklist;
- tracking missing documents/clarifications.

Not an early Work scope:

- legal conclusion;
- final bid/no-bid decision;
- signing or submitting bids;
- ЕИС/ЭТП actions without explicit authority;
- commercial pricing decisions.

Initial fit: **medium-to-strong**, but higher consequence and verification cost make it later than document/data reconciliation.

### F-06 — General document routing / registers / status control

Observed public signals:

- hh.ru examples around 85–110k RUB net/gross for document specialists;
- one current public-sector letters role around 130–150k RUB net;
- duties include registering incoming/outgoing correspondence, categorizing/routing requests, maintaining registers and monitoring deadlines.

Candidate Work stream:

`Incoming document/request → classify → extract metadata → route → update register/status → SLA alert`

Initial fit: **strong technically**, but internal-system integration and confidentiality can dominate economics.

### F-07 — Data/registry operator

Observed public signals:

- current hh.ru operator-database search showed roughly 180 Moscow vacancies;
- examples include 75–80k RUB net for customer-order/document/report operations and ~76k RUB for daily register/database maintenance;
- another data-processing role around 60k RUB net explicitly asks to verify incoming data by rules and detect discrepancies.

Candidate Work stream:

`Incoming records → validation → normalization → database/import update → exception queue`

Initial fit: **very strong technically**, but the lower salary floor means Work must be extremely cheap at scale.

### F-08 — Product-card/content operations

Observed public signal:

- current hh.ru example: 50–60k RUB net for templated product-card creation, names, descriptions, attributes, package data and prices.

Candidate Work stream:

`New SKU/supplier data → card draft → attribute normalization → completeness check → publish-ready package`

Initial fit: **medium**. High automation potential, but the observable human salary is lower and subjective copy quality can increase verification cost.

## 4. Current wedge ranking for further public evidence

This is a research prioritization, not a commercial winner decision.

### Tier A — investigate first

1. **Primary documents / 1C reconciliation**
2. **Logistics document closure / transport reconciliation**
3. **Product/catalog data validation**
4. **Structured order processing / 1C transaction preparation**

Why:

- recurring volume;
- observable salaries around the 80–150k RUB band in many examples;
- structured inputs/outputs;
- acceptance can often be deterministic;
- exception handling can be separated from clean-path execution;
- strong potential for price-per-unit Work service.

### Tier B — investigate after Tier A

5. Tender/procurement document operations
6. General document routing and registers
7. Data/registry operator functions

### Tier C — opportunistic

8. Product-card/content operations

## 5. Commercial modeling rule

Do **not** model the pitch as:

`employee salary = 100k → Work = 50k → 50k saved`

That is too simplistic.

For each vacancy/function decompose:

`role = automatable recurring flow + human exceptions + judgment/communication + accountability`

Then compare:

`current monthly role cost attributable to flow`

against

`Work price + customer's residual exception/acceptance cost`

and against

`owned automation amortization + operation/support + residual human cost`.

### Initial discovery hurdle

For a Work candidate to remain interesting, the model should aim for at least one realistic volume band where:

- Work total cost is materially lower than the current flow cost after modern employee+AI use;
- customer residual work is bounded;
- Work contribution margin remains positive;
- owned automation does not already dominate at the customer's current volume.

A useful **hypothesis to test**, not a price commitment:

- customer savings target: `>= 30%` versus the current comparable flow cost;
- for an observable 100k RUB/month role where ~70% of the job is the target flow, Work should likely cost well below 70k RUB/month after residual customer handling; a 40–50k RUB Work price is plausible only if measured volume/quality economics support it.

## 6. Buy Work vs owned-agent handoff

Arvectum Work should not try to retain a customer when owned automation is clearly better.

For each candidate stream estimate a crossover:

`annual Work spend` vs `one-time owned automation + annual support/infra + residual human handling`.

If the process is stable and an owned solution can credibly pay back within the customer's acceptable period, Work should surface that as a handoff signal to Arvectum Company rather than hide it.

Discovery hypothesis for modeling only: test payback windows around `6–12 months`, then replace with real buyer thresholds when evidence exists.

Arvectum Work does not own the design or sale of the separate owned-agent/Arvectum OS product.

## 7. Next public-evidence work

Before outbound interviews, expand this into a vacancy corpus:

- >=100 relevant current vacancies;
- >=5 source/job portals where accessible;
- capture title, salary/range, location/remote, employer type, duties, systems, volume clues and human-only duties;
- atomize duties into recurring functions;
- cluster functions independent of job title;
- estimate automation share as a hypothesis with explicit uncertainty;
- identify the top 3 work-stream candidates;
- draft a synthetic Work offer and an owned-automation alternative for each top candidate;
- monitor changes over time instead of relying on a single snapshot.

## 8. Evidence boundary

Vacancies prove that employers are actively recruiting for functions at observable salary levels.

They do **not** prove:

- the workload is large enough for Work;
- the advertised salary is the full employer cost;
- the whole role is automatable;
- the employer will outsource it;
- the employer accepts machine execution;
- Work can deliver the function at 50% of salary;
- an owned agent will pay back in a specific number of months.

Those remain hypotheses to test with workload benchmarks, pilots and eventually buyers.
