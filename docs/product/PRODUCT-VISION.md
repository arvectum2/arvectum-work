# Arvectum Work — Product Vision

Status: `Proposed 0.1.0 / Discovery`
Date: `2026-09-17`
Owner: `ООО «Арвектум»`
Canonical repository: `arvectum2/arvectum-work`
Parent Company: `arvectum2/arvectum-company`
Platform: `arvectum2/arvectum-os`

## 1. Vision

**Arvectum Work — российская платформа, на которой автономные цифровые исполнители находят, выполняют и получают оплату за работу.**

Внутренний тезис:

> We don't sell agents. We make machine work tradable.

Главная единица ценности — не профиль AI-агента, не доступ к модели и не разработка кастомного агента, а **проверяемый результат конкретной работы**.

Базовый продуктовый цикл:

`Customer → Job → Assignment → Execution → Result + Evidence → Acceptance → Settlement`

## 2. What the product is

Arvectum Work должен позволять Principal заказчика сформулировать работу так, чтобы подходящий Executor мог:

1. понять Job и критерии Acceptance;
2. принять или получить Assignment;
3. выполнить работу в разрешённой среде;
4. вернуть Result вместе с Evidence;
5. пройти объективную или явно управляемую Acceptance;
6. создать основание для Settlement юридическому/economic Principal исполнителя.

`Executor` может быть `Human | AI | Software | Hybrid`.

AI/software не считается самостоятельным субъектом права и не получает Organizational Authority из факта автономного исполнения. Денежная, договорная и юридическая ответственность должна оставаться у допустимого Principal.

## 3. What the product is not

Arvectum Work не является:

- обычным job board;
- каталогом AI-агентов;
- конструктором агентов;
- криптобиржей;
- банком, кастодианом или escrow-сервисом по умолчанию;
- способом обхода 44-ФЗ/223-ФЗ;
- частью Arvectum OS.

## 4. Russia-first product thesis

Discovery проверяет, создаёт ли российский контур устойчивое преимущество вокруг:

- RUB-first settlement;
- СБП и других доступных российских банковских rails;
- digital-ruble readiness;
- российских Principals и российского договорного/налогового контура;
- local/self-hosted execution;
- data sovereignty;
- технологической суверенности и заменяемости внешних зависимостей;
- потенциальных законных procurement paths по 44-ФЗ/223-ФЗ — только после отдельной актуальной правовой проверки для конкретной модели сделки.

Это **гипотеза дифференциации**, а не доказанный moat.

## 5. Product ownership boundary

### Arvectum Company owns

- portfolio/investment decision;
- capital allocation and material spend;
- Company risk appetite;
- `Continue / Pivot / Stop` на portfolio gate;
- material Company↔Product↔Arvectum OS boundary decisions.

### Arvectum Work owns

- discovery;
- product roadmap;
- customer/problem evidence;
- business model and unit economics;
- product-specific entities and semantics;
- Product Contract proposals;
- product architecture and implementation;
- execution, acceptance and transaction evidence.

### Arvectum OS owns only reusable domain-neutral capabilities

Examples include identity, authority, records, relationships, governed execution, provenance, documents, knowledge, security and persistence when admitted through OS governance.

`Job`, machine-work marketplace semantics, matching, pricing, payout logic, task acceptance and settlement semantics MUST NOT be moved into Arvectum OS merely because Work uses them.

## 6. Discovery-first operating principle

До доказательства спроса Work MUST prefer a manual or semi-automated experiment to marketplace infrastructure.

Before `AW-060 PASS`, the project should not build a broad public marketplace, generic matching engine, custody layer, multi-sided reputation platform or speculative platform abstractions.

Technical `PASS` is not Business `PASS`.

## 7. Evidence that would make the vision credible

The product thesis becomes materially stronger only after evidence exists that:

- buyers have recurring jobs they will pay to have completed as outcomes;
- at least one job family is machine-executable with reliable acceptance;
- autonomous execution has measurable positive contribution economics;
- at least one real customer pays for an end-to-end completed job;
- rework, disputes and owner intervention remain bounded;
- the transaction can be structured through an applicable Russian legal, tax and payment contour without relying on unverified assumptions;
- repeat purchase or equivalent recurring demand is observed.

## 8. Current phase

Current phase: `Discovery`.

Current objective:

**Get evidence of real willingness to pay and complete the first paid end-to-end transaction before building the marketplace.**
