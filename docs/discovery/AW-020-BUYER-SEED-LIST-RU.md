# AW-020-A — Buyer discovery seed list (RU)

Status: `Recruitment aid / public-source research`
Observed: `2026-09-17`
Task: `AW-020-A-BUYER-SEED-LIST`

## 1. Назначение и границы

Это privacy-safe список организаций и **функций**, которые подходят для human-led customer discovery Arvectum Work.

Список не означает, что перечисленные организации испытывают заявленную проблему, заинтересованы в продукте или готовы платить. Основание включения — только публично наблюдаемые business processes, в которых встречаются повторяемые документы, данные, сверки, каталоги, отчёты или закупочные операции.

В public repo намеренно не копируются личные телефоны, персональные e-mail и ФИО сотрудников, даже если они опубликованы на корпоративных сайтах.

## 2. Archetype A — SME / professional-services operations

| Организация | Публично наблюдаемый контекст | Функции для discovery | Какие недавние задачи стоит реконструировать | Почему полезно интервьюировать | Источник |
|---|---|---|---|---|---|
| Моё дело | Бухгалтерский аутсорсинг и онлайн-бухгалтерия; учет, налоги, кадры, счета, интеграции, работа с контрагентами и управленческий учет | operations / accounting service delivery / back office / product operations | сбор и нормализация первички; сверки; подготовка отчетности; обработка документов; recurring client reporting | Высокая доля повторяемых документных/данных процессов; можно проверить, где machine result реально отделим от экспертной ответственности | https://www.moedelo.org/ |
| Кнопка | Сервис ведения бухгалтерии с собственной автоматизацией; обслуживает предпринимателей по России; публично описывает бухгалтерский учет, отчетность, кадры и консультации | service operations / accounting ops / automation/product ops | классификация и проверка документов; подготовка типовых отчетов; reconciliation; контроль исключений; клиентские запросы | Полезный контрпример: организация уже автоматизирует внутренний труд — можно проверить, где выгоднее capability, а где purchase of result | https://knopka.com/contacts ; https://blog.knopka.com/buhobsluzhivanie/outsourcing-buhgalterii/ |
| 1C-WiseAdvice | Бухгалтерский аутсорсинг; 500+ специалистов; публично описывает 100+ контрольных точек, собственную автоматизацию и аутсорсинг рутинных участков | accounting operations / quality control / automation / client delivery | массовая обработка документов; контрольные проверки; payroll/data preparation; исключения и сверки; регулярная отчетность | Особенно полезно проверить economics verification: компания сочетает людей, автоматизацию и многоуровневый контроль | https://1c-wiseadvice.ru/ ; https://1c-wiseadvice.ru/glavnomu-buhgalteru/accounting_section/ |
| СберРешения | Аутсорсинг бухгалтерского и налогового учета; подготовка обязательной и управленческой отчетности, работа с данными клиента | finance operations / accounting delivery / reporting / shared services | сбор/проверка данных; отчетные пакеты; структурирование документов; регулярные сверки; exception handling | Позволяет проверить требования крупных professional-services операций к качеству, конфиденциальности и human responsibility | https://sber-solutions.ru/services/finance/ |

### Что проверять в Archetype A

- Где заканчивается механическая обработка и начинается профессиональная ответственность.
- Сколько стоит проверка исключений относительно самого execution.
- Есть ли задачи, которые сегодня выгодно отдавать отдельным внешним исполнителям, а не автоматизировать внутри.
- Может ли `Result + Evidence` встроиться в существующий сервисный процесс без передачи клиентского ownership цифровому исполнителю.

## 3. Archetype B — suppliers / contractors serving business customers

| Организация | Публично наблюдаемый контекст | Функции для discovery | Какие недавние задачи стоит реконструировать | Почему полезно интервьюировать | Источник |
|---|---|---|---|---|---|
| ЭТМ | Федеральный комплексный B2B-поставщик инженерных систем; цифровые закупки iPRO; работа с каталогами, заказами, договорными лимитами и поставками | commercial operations / sales ops / product data / tender & specification desk / supply operations | подбор позиций и аналогов; разбор спецификаций; прайс/каталог reconciliation; подготовка КП; контроль заказов/поставок | Близко к исходному опыту Arvectum: много структурированных товарных данных и повторяемой коммерческой работы | https://holding.etm.ru/ ; https://promo.etm.ru/ |
| Русский Свет | Крупный дистрибьютор электротехники; 650+ производителей, B2B-портал, логистические центры | sales operations / catalog & pricing / procurement support / customer operations | подбор продукции; аналоги; прайс-листы; проверка наличия/сроков; коммерческие предложения; документы | Можно проверить, насколько формализуемы реальные supplier-side tasks и где возникают дорогостоящие исключения | https://russvet.ru/ |
| ВсеИнструменты.ру | B2B-продажи для компаний и ИП; личный кабинет юрлица, документы, ЭДО, отсрочка, персональный менеджер | B2B sales ops / order ops / catalog data / customer support / document ops | комплектация заявки; поиск аналогов; сведение корзин/спецификаций; документы по заказам; повторные заказы | Массовый ассортимент + юридические лица создают хороший контекст для проверки bounded catalog/specification jobs | https://www.vseinstrumenti.ru/b2b/ ; https://www.vseinstrumenti.ru/publication/lichnyj-kabinet-dlya-yurlits-vozmozhnosti-i-funktsii-6969/ |
| Эlevel | Электротехническая инжиниринговая компания; комплексные поставки, e.way, оптимизация смет и подбор аналогов для строительно-монтажных организаций | commercial engineering / tender support / specification desk / sales ops | разбор проекта/сметы; подбор аналогов; спецификация; запрос цены/наличия; формирование счета/КП | Полезно проверить границу между machine-executable normalization и инженерным judgment | https://pro.elevel.ru/builders |

### Что проверять в Archetype B

- Какие спецификации и коммерческие запросы реально повторяются каждую неделю.
- Сколько времени уходит на поиск/сверку/нормализацию до экспертного решения.
- Можно ли заранее формализовать `Acceptance`: полнота строк, source evidence, match confidence, ambiguity flags.
- Покупается ли такая работа отдельно или экономически рациональнее держать ее внутри CRM/ERP/catalog automation.

## 4. Archetype C — large-enterprise functional teams

| Организация | Публично наблюдаемый контекст | Функции для discovery | Какие недавние задачи стоит реконструировать | Почему полезно интервьюировать | Источник |
|---|---|---|---|---|---|
| СИБУР | Закупки МТР/услуг через SAP SRM и 7Rights; квалификация поставщиков, формализованные предложения, широкий перечень категорий; актуальный план закупок 2026 | procurement operations / category management / supplier onboarding / back office / finance or document ops | supplier qualification data; procurement document triage; comparison tables; category research; recurring reports; non-consequential document preparation | Сильный контекст для проверки data sovereignty, formal acceptance и тяжелого buying path — без предположения, что Work уже подходит под закупочную процедуру | https://sibur.ru/ru/procurement/procedure/ ; https://www.sibur.ru/ru/procurement/start/ ; https://www.sibur.ru/ru/procurement/procurement/ |
| Норникель | 40+ агрегированных закупочных категорий; единая SAP SRM; квалификация поставщиков; формализованные критерии и электронный документооборот | procurement operations / supplier management / sourcing analytics / document operations | supplier questionnaire processing; document completeness; tender-data normalization; comparison prep; reporting; shipment-data checks | Позволяет проверить ценность verifiable machine work в крупном формализованном procurement process при высоких требованиях к governance | https://nornickel.ru/suppliers/ ; https://nornickel.ru/suppliers/purchasing-policy/ |
| Ростелеком | Крупный закупочный контур; в 2026 запущена совместная с Росэлторгом платформа подготовки поставщиков; публично раскрывает масштаб закупочной деятельности | procurement operations / supplier enablement / contract/document support / analytics | разбор закупочной документации; supplier-data preparation; recurring reporting; qualification/support content; document QA | Подходит для проверки, какие вспомогательные procurement tasks можно покупать как результат, не пересекаясь с принятием закупочного решения | https://www.company.rt.ru/press/news/d479539/ |
| X5 | Регулярные закупки товаров, работ и услуг; supplier portals, EDI/data services, Partner НКЗ; более 50 категорий закупок для собственных нужд на публичной странице | procurement operations / supplier operations / category analytics / contract/document ops | supplier onboarding; document packs; category data; tender preparation support; reconciliation/reporting | Масштабный коммерческий procurement-контур позволяет проверить repeatability и требования к integration/closing documents без 44-ФЗ предпосылки | https://www.x5.ru/ru/partners/purchases-for-own-needs/ ; https://www.x5.ru/ru/suppliers/noncommercial-purchase/ |

### Что проверять в Archetype C

- Есть ли вспомогательные задачи, которые можно отделить от decision authority и закупочного решения.
- Насколько тяжелый vendor onboarding делает маленький Job экономически бессмысленным.
- Может ли простой B2B service contract / existing supplier route быть реалистичнее нового marketplace procurement path.
- Какие данные обязаны оставаться в российском/локальном контуре.
- Где Evidence действительно снижает verification cost, а где только добавляет еще один слой контроля.

## 5. Prioritization for the first five interviews

Это **не рейтинг компаний** и не вывод о спросе. Для первого человеческого recruitment batch разумно добиться разнообразия контекста:

- 2 интервью из Archetype A — service/back-office operations;
- 2 интервью из Archetype B — supplier/commercial operations;
- 1 интервью из Archetype C — large-enterprise functional team, если доступ к респонденту реалистичен.

Если доступ к крупной компании требует длинного согласования, не ждать его: первый paid pilot по canonical discovery plan должен предпочитать простой законный коммерческий путь.

## 6. Recruitment target functions, not named people

Искать респондентов по функциям:

- операционный директор / head of operations;
- руководитель бухгалтерского/финансового аутсорсинга;
- руководитель back office / shared services;
- руководитель коммерческих операций / sales operations;
- руководитель тендерного/спецификационного отдела;
- category/procurement operations manager;
- руководитель product/catalog data operations;
- руководитель аналитики или process automation, если он владеет реальным operational workload.

Не ограничиваться IT/AI-функциями: они часто знают технологию, но не владеют бюджетом и болью конкретной работы.

## 7. Recruitment evidence rule

Организация переходит из seed-list в реальный AW-020 evidence только после **реального интервью**, в котором восстановлена хотя бы одна недавняя задача согласно `AW-020-INTERVIEW-KIT-RU.md`.

До этого:
- наличие организации в списке = `0` buyer-demand evidence;
- публично наблюдаемая автоматизация = только контекст;
- публичный procurement/catalog process = только основание задать вопросы;
- никакая строка списка не является разрешением на autonomous outreach.
