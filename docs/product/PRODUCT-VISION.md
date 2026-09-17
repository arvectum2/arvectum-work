# Arvectum Work — Product Vision

Status: `Proposed 0.2.0 / Discovery`
Date: `2026-09-17`
Owner: `ООО «Арвектум»`
Canonical repository: `arvectum2/arvectum-work`
Parent Company: `arvectum2/arvectum-company`
Platform: `arvectum2/arvectum-os`

## 1. Vision

**Arvectum Work — российская платформа/сервис, через который компании передают поток повторяемой цифровой работы автономным цифровым исполнителям и платят за принятые результаты.**

Внутренний тезис:

> We don't sell agents. We make machine work tradable.

Коммерческая формулировка Discovery:

> **Не покупайте AI и не управляйте AI. Покупайте выполненную цифровую работу.**

Главная единица ценности — не профиль AI-агента, не доступ к модели, не prompt и не проект внедрения. Это **измеримый объём выполненной работы с согласованными результатом, качеством, сроком и ценой за принятую единицу/пакет**.

Базовый цикл сохраняется:

`Customer → Work Stream/Job → Assignment → Execution → Result + Evidence + Exceptions → Acceptance → Settlement`

## 2. What the customer buys

Заказчик должен иметь возможность передать Work повторяемый или переменный цифровой процесс и договориться о понятной экономической единице, например:

- рублей за принятый документ;
- рублей за нормализованную строку;
- рублей за принятый пакет;
- фиксированной цене за ограниченный объём/период при заранее заданном качестве и сроке.

Заказчик не должен в нормальном производственном сценарии управлять моделями, промптами, повторами, маршрутизацией и технической кухней исполнения.

Arvectum Work отвечает за продуктовый контур, в котором можно:

1. определить единицу/пакет работы и границы потока;
2. назначить подходящего Executor;
3. выполнить работу в разрешённой среде;
4. вернуть Result вместе с Evidence и отдельными Exceptions;
5. провести Acceptance по заранее известным правилам;
6. измерить объём, качество, latency, стоимость и вмешательство людей;
7. создать основание для Settlement между допустимыми Principals.

`Executor` может быть `Human | AI | Software | Hybrid`.

AI/software не считается самостоятельным субъектом права. Денежная, договорная и юридическая ответственность остаётся у допустимого Principal.

## 3. Core customer value hypothesis

Work должен экономить не время на написание prompt, а **операционную стоимость выполнения потока**.

Целевой сценарий:

- у компании есть повторяемая цифровая нагрузка;
- даже с современным ChatGPT/аналогом остаётся операторская работа, проверка, перенос данных, обработка исключений и контроль объёма;
- заказчик не хочет или пока не может экономически оправдать собственную автоматизацию;
- Work принимает поток и возвращает готовые принятые результаты по измеримой цене.

Если сотрудник + современная универсальная модель закрывают процесс за пренебрежимо малое время без заметной операторской нагрузки, Work не должен искусственно создавать там продукт.

## 4. Buy work vs own automation

Work — альтернатива владению автоматизацией, а не универсальная замена ей.

Для части клиентов собственный AI-агент/автоматизация со временем будет выгоднее.

Work должен уметь измерять и показывать экономическую границу:

`покупать выполненную работу` vs `владеть средством её выполнения`.

Если процесс клиента становится большим, стабильным и предсказуемым, переход к собственной системе может быть рациональным.

Возможный следующий продукт/решение определяется Arvectum Company отдельно; потенциально это система с собственными AI-исполнителями на базе Arvectum OS. Arvectum Work не владеет OS и не переносит туда свои доменные/marketplace semantics.

## 5. What the product is not

Arvectum Work не является:

- обычным job board;
- каталогом AI-агентов;
- конструктором агентов;
- «ещё одним ChatGPT для бизнеса»;
- обязательной заменой собственной автоматизации;
- криптобиржей;
- банком, кастодианом или escrow-сервисом по умолчанию;
- способом обхода 44-ФЗ/223-ФЗ;
- частью Arvectum OS.

## 6. Russia-first product thesis

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

## 7. Product ownership boundary

### Arvectum Company owns

- portfolio/investment decision;
- capital allocation and material spend;
- Company risk appetite;
- `Continue / Pivot / Stop` на portfolio gate;
- material Company↔Product↔Arvectum OS boundary decisions;
- решение о предложении клиенту другого продукта, если владение собственной автоматизацией становится экономически рациональнее Work.

### Arvectum Work owns

- discovery;
- product roadmap;
- customer/process evidence;
- business model and unit economics;
- work-stream/job-specific entities and semantics;
- Product Contract proposals;
- product architecture and implementation;
- execution, acceptance and transaction evidence;
- build-vs-buy evidence по своим клиентским потокам.

### Arvectum OS owns only reusable domain-neutral capabilities

Examples include identity, authority, records, relationships, governed execution, provenance, documents, knowledge, security and persistence when admitted through OS governance.

`Job`, work-stream commercial semantics, matching, pricing, payout logic, acceptance and settlement semantics MUST NOT be moved into Arvectum OS merely because Work uses them.

## 8. Discovery-first operating principle

До доказательства спроса Work MUST prefer manual/semi-automated managed execution to marketplace infrastructure.

Before `AW-060 PASS`, the project should not build a broad public marketplace, generic matching engine, custody layer, multi-sided reputation platform or speculative platform abstractions.

После `AW-060 GO` продукт также не обязан сразу становиться marketplace: сначала должен быть построен тот минимальный operating/product layer, который подтверждён реальными транзакциями.

Technical `PASS` is not Business `PASS`.

## 9. Evidence that would make the vision credible

The product thesis becomes materially stronger only after evidence exists that:

- buyers have recurring/bursty digital work streams they will transfer and pay to have completed;
- employee + general-purpose AI still leaves material operational burden for the selected process;
- at least one work stream is machine-executable with reliable, affordable acceptance;
- autonomous execution has measurable positive contribution economics;
- at least one real customer pays for accepted work;
- rework, exceptions, disputes and owner intervention remain bounded;
- Work is economically preferable to relevant substitutes for a real customer window;
- the transaction can be structured through an applicable Russian legal, tax and payment contour;
- repeat purchase/continuation is observed;
- build-vs-buy data can identify when own automation becomes the better customer choice.

## 10. Current phase

Current phase: `Discovery`.

Current objective:

**Find one real recurring work stream where Arvectum Work beats the customer's practical alternatives, execute it, get paid for accepted work and observe repeat/continuation before building product infrastructure.**
