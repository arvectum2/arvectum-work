# Arvectum Work — Hypothesis Register

Status: `Proposed 0.2.0 / Discovery`
Date: `2026-09-17`
Canonical repository: `arvectum2/arvectum-work`

## 1. Primary product hypothesis

Российским компаниям может быть выгоднее **передать Arvectum Work поток повторяемой цифровой работы и платить за принятые результаты**, чем:

- выполнять этот поток сотрудниками вручную;
- оставлять сотрудника оператором ChatGPT/другой универсальной модели;
- отдавать процесс обычному аутсорсеру;
- каждый раз внедрять отдельное AI-решение;
- владеть собственной автоматизацией до того, как объём и стабильность процесса это экономически оправдают.

Arvectum Work проверяет модель **machine work as a service**: заказчик покупает выполненную работу с измеримыми сроком, качеством и ценой за принятую единицу/пакет, а не модель, промпт, лицензию или внутренний AI-проект.

Гипотеза не считается доказанной до реальных платных транзакций и повторного спроса.

## 2. Testable hypotheses

| ID | Hypothesis | Required evidence | Falsification signal |
|---|---|---|---|
| `H-01` | Есть спрос на внешний поток выполненной цифровой работы, а не только на разработку/лицензию AI | интервью + реальные процессы + paid/contractual intent + пилот | buyers готовы обсуждать AI, но не отдавать наружу сам рабочий поток |
| `H-02` | Существуют повторяемые machine-executable work streams | процессы с повторяющимися единицами, входами/выходами, объёмом и ценой | работа слишком редкая, уникальная или требует постоянного human judgment |
| `H-03` | Acceptance можно формализовать достаточно надёжно и дёшево | benchmark/tests/schema/human rubric с измеримой согласованностью | высокий false accept/reject или стоимость проверки съедает выгоду |
| `H-04` | Автономный Executor способен давать положительную contribution economics | execution + verification + rework + payment + owner intervention cost < realized revenue | human intervention/rework/verification съедают маржу |
| `H-05` | Заказчик реально платит за выполненную machine work | минимум одна завершённая оплаченная end-to-end transaction | только бесплатные pilots / verbal interest |
| `H-06` | Российский legal/payment/tax contour не блокирует выбранную модель сделки | актуальная проверка по официальным источникам + применимый договорный/расчётный путь | модель требует запрещённой/неприемлемой роли, лицензирования или недоступного payment path |
| `H-07` | Russia-first constraints создают differentiation | buyer evidence о ценности RUB/local/self-hosted/data sovereignty | buyers не воспринимают эти свойства как material buying criteria |
| `H-08` | Marketplace-like matching eventually adds value over managed service | multiple buyers + multiple executors + repeated matching/capacity friction | ценность создаёт только managed execution by Arvectum |
| `H-09` | Work экономит не prompt-writing, а операционную нагрузку вокруг массового AI-enabled процесса | сравнение employee + ChatGPT против Work на времени, пропускной способности, исключениях и полной стоимости | сотрудник с современной моделью закрывает единицу работы за несколько минут без существенного контроля; Work не улучшает полную экономику |
| `H-10` | Для части процессов покупать работу временно выгоднее, чем владеть собственной автоматизацией | build-vs-buy расчёт на реальном объёме, вариативности, сопровождении и сроке окупаемости | собственный агент/автоматизация очевидно дешевле и проще уже при текущем объёме клиента |
| `H-11` | Work может стать каналом квалификации процессов, которые позже экономически созревают для собственной автоматизации клиента | фактическая история объёма/качества/затрат позволяет определить точку перехода | Work не даёт достаточно данных или клиенты не рассматривают переход к собственной системе |

## 3. Two mandatory substitution tests

### 3.1 Employee + general-purpose AI test

Для каждого перспективного рабочего потока нужно ответить:

> Что остаётся делать сотруднику, если дать ему современный ChatGPT/аналог сегодня?

Измерять:

- время на одну единицу;
- число ручных итераций;
- время проверки;
- перенос данных между системами;
- обработку исключений;
- ежедневный/месячный объём;
- потребность в операторе процесса.

Если после применения универсального AI остаточная операционная нагрузка мала, такой процесс не должен становиться ведущим wedge Arvectum Work.

### 3.2 Buy work vs own automation test

Для каждого перспективного потока сравнивать как минимум:

- текущую полную стоимость ручного/AI-assisted процесса;
- ожидаемую полную стоимость Arvectum Work;
- стоимость создания и владения собственной автоматизацией клиента.

Own-automation cost должен учитывать не только разработку, но и применимые расходы на инфраструктуру, интеграции, поддержку, обновления, контроль качества и внутреннего владельца процесса.

Если собственная автоматизация становится устойчиво выгоднее, Work должен показывать это как экономическую границу продукта, а не искусственно удерживать клиента на per-unit оплате.

Возможный следующий продукт/решение определяется Arvectum Company отдельно; потенциально это система с собственными AI-исполнителями на базе Arvectum OS. Work не владеет OS и не переносит в неё свои доменные semantics.

## 4. Important sequencing

`H-08` и `H-11` не нужно доказывать раньше `H-01…H-06` и базовой экономики `H-09/H-10`.

На Discovery допустимо, что Arvectum вручную или полуавтоматически:

- принимает рабочий поток;
- разбивает его на единицы/пакеты;
- выбирает Executor;
- формирует Assignment;
- проверяет Result;
- обрабатывает исключения;
- выставляет счёт/получает оплату допустимым существующим способом;
- ведёт evidence ledger в репозитории или иной разрешённой системе.

Manual orchestration is not product failure at this stage. It is a cheaper way to test whether the operating model deserves software.

## 5. Economic model to measure

For every live experiment capture:

`revenue`
`GMV` where meaningful
`units/batches received`
`units/batches accepted`
`worker payout`
`execution cost`
`verification cost`
`payment cost`
`rework cost`
`owner intervention cost/time`
`customer operator time avoided`
`contribution margin`
`cost per accepted unit/batch`
`time-to-result`
`throughput`
`acceptance rate`
`revision rate`
`exception rate`
`dispute rate`
`repeat purchase`
`volume variability`
`estimated own-automation break-even` where enough evidence exists

Unknown values MUST remain `unknown`; they must not be rewritten as zero.

## 6. Trust hypothesis

The primary trust mechanism should be evidence of execution and operating history, not marketing claims about an agent.

Candidate evidence:

- benchmark result;
- execution history;
- acceptance rate;
- latency;
- throughput;
- exception/revision/failure/dispute rate;
- proven capability on a declared work stream;
- provenance of Result and Acceptance;
- measured operator intervention.

## 7. Technology sovereignty hypothesis

External dependencies are acceptable only when their role is explicit and a replacement path exists proportionate to risk.

Discovery should record for each material dependency:

- jurisdiction;
- sanctions/access risk from Russia;
- data locality and telemetry;
- license;
- self-hosting option;
- replacement path;
- provenance/IP concerns.

No external vendor should own Organizational Authority or the only copy of canonical history.

## 8. Decision rule

The project advances because evidence reduces uncertainty, not because implementation volume increases.

A stage may return:

- `GO` — evidence supports the next bounded test;
- `PIVOT` — demand exists but segment/process/acceptance/economics/model must change;
- `STOP` — core assumptions fail or downside dominates plausible upside.
