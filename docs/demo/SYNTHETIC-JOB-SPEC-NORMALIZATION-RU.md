# Arvectum Work — синтетический demo Job

Status: `SYNTHETIC DEMO / NOT CUSTOMER EVIDENCE`
Date: `2026-09-17`
Scenario: `J-02 Document extraction + J-03 reconciliation`

> Все компании, документы, цифры и результаты ниже вымышлены. Это демонстрационный кейс для интервью. Он не является клиентским кейсом, продажей, подтверждением спроса или unit economics.

## 1. Ситуация

Вымышленная компания **ООО «ДемоСнаб»** регулярно получает коммерческие предложения от нескольких поставщиков электротехнического оборудования.

Менеджеру нужно собрать предложения в единую таблицу перед внутренним сравнением.

Последний пакет:

- 6 PDF/XLSX файлов;
- 87 товарных строк;
- разные названия одной и той же продукции;
- разные единицы измерения;
- часть цен указана с НДС, часть без НДС;
- по ряду позиций есть аналоги;
- в двух документах срок поставки указан только в примечании.

Сегодня сотрудник обычно вручную переносит это в Excel и затем второй сотрудник выборочно перепроверяет.

## 2. Что размещается как Job

### Job ID

`DEMO-JOB-001`

### Название

**Нормализовать 6 коммерческих предложений поставщиков в единую сравнительную таблицу.**

### Input

Заказчик передаёт:

- `supplier-a.pdf`
- `supplier-b.xlsx`
- `supplier-c.pdf`
- `supplier-d.pdf`
- `supplier-e.xlsx`
- `supplier-f.pdf`

Плюс schema:

| Field | Required |
|---|---:|
| requested_item_id | yes |
| supplier | yes |
| supplier_item_name | yes |
| manufacturer | if stated |
| article | if stated |
| quantity | yes |
| unit | yes |
| unit_price_net | yes or ambiguity flag |
| vat_rate | yes or ambiguity flag |
| total_price_gross | yes or computable |
| delivery_days | yes or ambiguity flag |
| is_analog | yes |
| source_ref | yes |
| confidence | yes |
| exception | if applicable |

### Result

Заказчик должен получить:

1. `normalized_offers.xlsx` — единая таблица;
2. `exceptions.csv` — всё, что нельзя определить уверенно;
3. `evidence.csv` — источник каждого существенного значения;
4. `execution-summary.md` — что было сделано и какие ограничения обнаружены.

### Deadline

`4 часа с момента Assignment`

### Synthetic price

`9 000 ₽ за принятый Result`

Цена — **только иллюстрация механики**, не предложение рынку.

## 3. Acceptance фиксируется ДО исполнения

Результат принимается, если:

1. присутствуют все 87 исходных строк либо для пропуска есть явная причина;
2. `requested_item_id`, supplier, name, quantity, unit и source_ref заполнены для 100% обработанных строк;
3. ни одно отсутствующее в источнике значение не выдумано;
4. неоднозначные НДС/срок/артикул помечены `AMBIGUOUS`;
5. каждая цена имеет source_ref;
6. арифметика total_price проверяется автоматически;
7. случайная выборка 20 строк имеет не менее 19 полностью корректных строк;
8. все аналоги отделены от точных совпадений;
9. формат файлов открывается и соответствует schema.

### Rework rule

Если не выполнены пункты 1–9 — одна ограниченная доработка в пределах исходного Job.

Если проблема вызвана отсутствием данных в источнике и она корректно вынесена в exception — это **не ошибка Executor**.

## 4. Assignment

Платформа выбирает доступного Executor, чья capability соответствует:

- PDF/XLSX parsing;
- Russian commercial documents;
- structured extraction;
- table normalization;
- provenance/evidence output.

В demo Assignment получает:

`Executor: Local Worker / Mac mini / isolated execution`

Юридический Principal исполнителя в реальной сделке был бы отдельной договорной стороной. В demo он не моделируется как реальная компания.

## 5. Что делает Executor

Условный execution pipeline:

1. fingerprint входных файлов;
2. извлечение таблиц/текста;
3. нормализация единиц и денежных полей;
4. сопоставление строк с requested_item_id;
5. вычисление derived totals только там, где входные поля однозначны;
6. flag всех ambiguities;
7. формирование evidence references;
8. deterministic schema checks;
9. формирование Result package.

Важно: покупатель не обязан покупать этот pipeline или владеть им. Он покупает принятый Result.

## 6. Фрагмент Result

| requested_item_id | supplier | supplier_item_name | qty | unit | unit_price_net | VAT | delivery_days | analog | confidence | source_ref |
|---|---|---|---:|---|---:|---:|---:|---|---|---|
| RQ-001 | Поставщик А | Автоматический выключатель AX-16 16A | 20 | шт | 1 240.00 | 20% | 7 | no | high | DOC-A:p2:r4 |
| RQ-001 | Поставщик В | Выключатель модульный BX16 | 20 | шт | 1 190.00 | 20% | 14 | yes | medium | DOC-B:sheet1:r18 |
| RQ-002 | Поставщик А | Контактор KM-25 | 8 | шт | 3 870.00 | 20% | 5 | no | high | DOC-A:p2:r9 |
| RQ-002 | Поставщик Г | Контактор C25-230 | 8 | шт | 3 610.00 | AMBIGUOUS | 12 | yes | medium | DOC-D:p4:r3 |
| RQ-003 | Поставщик Е | Кабель ВВГнг-LS 3×2.5 | 400 | м | 78.40 | 20% | AMBIGUOUS | no | high | DOC-E:sheet2:r27 |
| RQ-004 | Поставщик F | Светильник LED 36W IP65 | 30 | шт | 2 480.00 | 20% | 21 | no | high | DOC-F:p3:r11 |

## 7. Фрагмент Evidence

| Result field | Value | Evidence |
|---|---|---|
| RQ-001 / supplier A / unit_price_net | 1 240.00 | `DOC-A`, page 2, row 4: price column explicitly states 1 240.00 without VAT |
| RQ-001 / supplier B / analog | yes | article differs from requested article; document labels product as «аналог» |
| RQ-002 / supplier D / VAT | AMBIGUOUS | source contains price but does not state whether VAT is included |
| RQ-003 / supplier E / delivery_days | AMBIGUOUS | document says «со склада/под заказ» without numeric term |

В реальной реализации Evidence может хранить hash/fingerprint, source coordinates, before/after artifacts или иные provenance records.

## 8. Exception report

| Row | Exception | Suggested buyer action |
|---|---|---|
| RQ-002 / supplier D | VAT basis not stated | ask supplier / do not compare gross total yet |
| RQ-003 / supplier E | delivery term not numeric | clarify delivery date |
| RQ-011 / supplier C | article unreadable in scan | manual verification of source page |
| RQ-014 / supplier F | unit is «упак.», request uses «шт» | require conversion factor |

Ключевой принцип: **лучше явный exception, чем правдоподобно выдуманное значение.**

## 9. Acceptance

После получения Result заказчик видит:

- `87 / 87` source rows accounted for;
- `83` rows normalized without exception;
- `4` rows require clarification;
- schema checks: PASS;
- arithmetic checks: PASS;
- sample verification: `20 / 20` correct in synthetic demo;
- acceptance decision: `ACCEPTED`.

Если бы sample verification дал, например, `17 / 20`, Result ушёл бы на rework согласно заранее установленному правилу.

## 10. Synthetic settlement

После Acceptance возникает расчётная часть.

Иллюстративная экономика одного Job:

| Metric | Synthetic value |
|---|---:|
| GMV / customer price | 9 000 ₽ |
| Executor Principal payout | 5 000 ₽ |
| Platform revenue | 4 000 ₽ |
| machine execution cost | 250 ₽ |
| verification cost | 800 ₽ |
| payment/closing-doc cost | 150 ₽ |
| rework reserve | 300 ₽ |
| synthetic contribution margin | 2 500 ₽ |

Это **не прогноз и не целевой take rate**. Таблица нужна, чтобы на интервью задать вопросы: какая цена кажется невозможной, сколько реально стоит текущий способ, сколько проверки понадобится и кто должен получать экономическую ценность.

## 11. Что в этом кейсе является продуктом

Не Mac mini.

Не LLM.

Не парсер PDF.

Не «агент закупщика».

Продуктовая единица:

> **Job с заранее фиксированным Result, Evidence, Acceptance и основанием для Settlement.**

Исполнитель может со временем меняться, а контрактуемая единица работы остаётся понятной заказчику.

## 12. Как использовать demo на интервью

Показывать этот кейс **после** разбора хотя бы одной реальной задачи респондента.

Затем спросить:

- «У вас бывает работа, похожая по структуре?»
- «Что здесь слишком искусственно?»
- «Какие поля нельзя было бы доверить такому исполнителю?»
- «Какой Evidence вам реально нужен?»
- «20 из 20 sample check — лишняя проверка или разумная?»
- «Кто у вас принимает такой файл?»
- «Если бы это стоило 9 000 ₽, с чем вы сравнивали бы цену: временем сотрудника, подрядчиком, SaaS или проектом автоматизации?»
- «Что пришлось бы изменить, чтобы вы дали реальный пакет документов для пилота?»

Цель demo — не убедить респондента, а заставить обсуждать **конкретную транзакцию и конкретную работу**.