# Arvectum Work — Hypothesis Register

Status: `Proposed 0.1.0 / Discovery`
Date: `2026-09-17`
Canonical repository: `arvectum2/arvectum-work`

## 1. Primary product hypothesis

Российским компаниям может быть выгоднее покупать **формализованный, проверяемый результат работы автономного цифрового исполнителя**, чем каждый раз заказывать разработку отдельного AI-решения или нанимать человека для той же повторяемой задачи.

The hypothesis is not proven until real paid transactions and repeat demand exist.

## 2. Testable hypotheses

| ID | Hypothesis | Required evidence | Falsification signal |
|---|---|---|---|
| `H-01` | Есть buyer demand на outcome, а не только на разработку/лицензию AI | интервью + paid/contractual intent + реальные задачи | buyers готовы обсуждать AI, но не покупать отдельный result |
| `H-02` | Существуют повторяемые machine-executable job families | корпус задач с повторяющимися входами/выходами/ценой | задачи слишком уникальны или требуют постоянного human judgment |
| `H-03` | Acceptance можно формализовать достаточно надёжно | benchmark/tests/schema/human rubric с измеримой согласованностью | высокий false accept/reject, критерии меняются после результата |
| `H-04` | Автономный Executor способен давать положительную contribution economics | execution + verification + rework + payment cost < realized revenue | human intervention/rework съедают маржу |
| `H-05` | Заказчик реально платит за выполненную machine work | минимум одна завершённая оплаченная end-to-end transaction | только бесплатные pilots / verbal interest |
| `H-06` | Российский legal/payment/tax contour не блокирует выбранную модель сделки | актуальная проверка по официальным источникам + применимый договорный/расчётный путь | модель требует запрещённой/неприемлемой роли, лицензирования или недоступного payment path |
| `H-07` | Russia-first constraints создают differentiation | buyer evidence о ценности RUB/local/self-hosted/data sovereignty | buyers не воспринимают эти свойства как material buying criteria |
| `H-08` | Marketplace-like matching eventually adds value over managed service | multiple buyers + multiple executors + repeated matching friction | value создаёт только managed execution by Arvectum |

## 3. Important sequencing

`H-08` не нужно доказывать раньше `H-01…H-06`.

На Discovery допустимо, что Arvectum вручную:

- находит Job;
- выбирает Executor;
- формирует Assignment;
- проверяет Result;
- выставляет счёт/получает оплату допустимым существующим способом;
- ведёт evidence ledger в репозитории или иной разрешённой системе.

Manual orchestration is not product failure at this stage. It is a cheaper way to test whether the transaction deserves software.

## 4. Economic model to measure

For every live experiment capture:

`revenue`
`GMV` where meaningful
`worker payout`
`execution cost`
`verification cost`
`payment cost`
`rework cost`
`owner intervention cost/time`
`contribution margin`
`time-to-result`
`acceptance rate`
`revision rate`
`dispute rate`
`repeat purchase`

Unknown values MUST remain `unknown`; they must not be rewritten as zero.

## 5. Trust hypothesis

The primary trust mechanism should be evidence of execution, not marketing claims about an agent.

Candidate evidence:

- benchmark result;
- execution history;
- acceptance rate;
- latency;
- revision/failure/dispute rate;
- proven capability on a declared job family;
- provenance of Result and Acceptance.

## 6. Technology sovereignty hypothesis

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

## 7. Decision rule

The project advances because evidence reduces uncertainty, not because implementation volume increases.

A stage may return:

- `GO` — evidence supports the next bounded test;
- `PIVOT` — demand exists but segment/job/acceptance/economics/model must change;
- `STOP` — core assumptions fail or downside dominates plausible upside.
