# AW-000 — Official-source legal/payment baseline

Status: `Research baseline / not legal advice`
Verified: `2026-09-17`
Owner: `Arvectum Work`

## 1. Purpose

This file records only the minimum official-source facts needed to prevent product discovery from turning assumptions into claims.

It does **not** establish that any particular Arvectum Work transaction is legally, tax, banking or procurement compliant. The exact transaction model must be checked again before execution.

## 2. Digital ruble

Official source:

- Bank of Russia, Board decision dated `2026-08-28`, operations and bank enablement from `2026-09-01`:
  `https://cbr.ru/rbr/dir_decisions/rsd_2026-08-28_45_02/`
- Bank of Russia FAQ:
  `https://www.cbr.ru/faq/dr/`
- Bank of Russia operator-platform tariffs:
  `https://www.cbr.ru/PSystem/dr/doc_dr/tarif/dr_t-1/`

Observed official facts relevant to discovery:

- from `2026-09-01`, the Bank of Russia decision includes operations with digital rubles for resident legal entities within the defined platform rules;
- rollout obligations for credit institutions are phased;
- the Bank of Russia publishes operator-platform tariffs and current usage rules.

Product implication:

`digital-ruble readiness` is a legitimate discovery item, but Arvectum Work MUST NOT assume universal bank/customer availability, a particular tariff, automatic merchant readiness or legal suitability for its exact settlement model.

Before any real use, verify the customer's bank, Arvectum's bank, transaction type, current tariffs/rules and required agreements at that date.

## 3. Faster Payments System / СБП

Official source:

- Bank of Russia tariffs effective `2026-05-01`:
  `https://www.cbr.ru/PSystem/payment_system/2026-04-01/`
- corresponding Board decision dated `2026-03-27`:
  `https://cbr.ru/rbr/dir_decisions/rsd_2026-03-27_45_01`

Observed official fact relevant to discovery:

The current Bank of Russia SBP tariff schedule explicitly contains transfer categories including legal entity / individual entrepreneur to legal entity / individual entrepreneur, as well as other C2B/B2C categories.

Product implication:

SBP can be researched as a possible RUB rail. This does not establish the commercial terms, API availability, limits, fraud controls, KYC/AML obligations or suitability of a specific bank/provider arrangement for Arvectum Work.

For AW-050, use an existing lawful bank/payment path where possible rather than integrating a new provider merely to prove the transaction.

## 4. 44-FZ / 223-FZ public procurement

Official source for the base 44-FZ:

- Federal Law `05.04.2013 № 44-ФЗ`, Official Internet Portal of Legal Information:
  `https://publication.pravo.gov.ru/Document/View/0001201304080023`

Official legal-information portal:

- `https://pravo.gov.ru/`

Relevant baseline only:

- 44-FZ is the federal contract-system framework for procurement of goods, works and services for state and municipal needs;
- 223-FZ is the framework for procurement of goods, works and services by covered categories of legal entities.

Arvectum Work does **not** infer from those titles that a marketplace, autonomous Executor, software license, development project or result-based service automatically fits a particular procurement path.

For every future public-procurement hypothesis distinguish at least:

1. development of an agent/software solution;
2. purchase/license/right to use ready software or capability;
3. service for performance of a defined task/result;
4. another goods/works/services classification supported by the actual subject and current law.

Any claim about a lawful 44-FZ/223-FZ route requires an exact current-law review, customer/procurement context and applicable procurement documentation. Arvectum Work must never be positioned as a mechanism to bypass procurement law.

## 5. Settlement role boundary

Discovery baseline:

- default domestic currency is RUB;
- ordinary Russian banking/SBP are preferred for the earliest experiment if already available and lawful;
- digital ruble is a readiness/research path, not a requirement for AW-050;
- crypto/digital assets are not the default domestic rail;
- Arvectum Work does not assume a bank, custodian, escrow or payment-agent role.

If the future business model requires holding customer money, split settlement, escrow/custody, regulated payment intermediation or a new financial-service role, the project must stop that path for separate legal/regulatory and Company risk review before implementation or commitments.

## 6. Tax and contract boundary

No universal tax/contract conclusion is recorded at AW-000.

For the first paid transaction the project must document, with appropriate professional/official verification where necessary:

- who is the contracting Principal;
- what exactly is being sold/provided;
- price and acceptance basis;
- invoicing/payment basis appropriate to the parties;
- applicable tax/accounting treatment;
- data/IP/confidentiality terms proportionate to the actual Job.

The simplest existing lawful B2B service contour is preferred over inventing platform-specific financial mechanics.

## 7. Re-verification rule

Legal/payment/procurement facts are time-sensitive.

Before AW-040/AW-050 external execution, re-check the official sources current on that date and record the exact source/date used for the transaction decision.
