# AW-020 — Machine-work boundary reconciliation for legacy counted records

Status: `Discovery evidence / acceptance-criteria reconciliation`  
Date: `2026-09-19`

Purpose: satisfy the AW-020-C1 requirement that every counted vacancy separates a plausible machine-executable recurring flow from human judgment, communication, authority and accountability.

## 1. Method

Tranches 06–10 already record `machine-work slice` and `residual human / accountability` per row.

The first 33 counted records predate that explicit table schema. This artifact reconciles those legacy records without changing their original source evidence.

Important distinction:

- **machine slice** below is a conservative product boundary derived from the observed atomic duties;
- **residual human** is an exclusion boundary, not a claim that the source page used those exact words;
- this artifact does not assert that any whole role is automatable.

## 2. Tranche 02 — C035–C051

| Record | Observed role shorthand | Candidate machine-work slice | Keep with human / Principal |
|---|---|---|---|
| C035 | Оператор 1С — ТАЙМЫР ИНВЕСТ | nomenclature updates; request/order entry; receipt/shipment/movement status checks | supplier exceptions, inventory decisions, business accountability |
| C036 | Оператор 1С / ассистент бренд-менеджера | order entry/status; invoices/docs; EDO status; payment/shipment status data | commercial decisions, actual payment authority, supplier/customer communication |
| C037 | Оператор документооборота — Лемана ПРО Склады | WMS event/data handling; receiving/shipping docs; UPD; standard reports | physical warehouse custody, discrepancy decisions, operational accountability |
| C038 | Оператор обработки заказов — ЗУБР МСК | primary docs; warehouse-system receipt/move/writeoff records; shipping docs/reports | physical inventory, exceptions, shipment authority |
| C039 | Оператор 1С — PARLY | Excel↔1C transfer; request/order docs; status monitoring | ambiguous source corrections, commercial communication |
| C040 | Менеджер документооборота с DIY-сетями | chain-order data; portal/EDI/EDO docs; labels; TORG-2/KSF/UKD prep; reconciliations | claims/negotiation, approval/signing, retailer relationship |
| C041 | Оператор 1С — Max Christmas | primary docs; receipts/shipments/corrections; invoice/UPD/act prep; EDO status; reference data | discrepancy judgment, inventory/accounting accountability |
| C042 | Специалист по маркировке «Честный знак» | product-card data; code/request preparation; 1C/marking reconciliation; exception queue | regulated submissions/turnover actions, legal interpretation, final compliance authority |
| C043 | Администратор / оператор БД | create records/order cards; validate requisites; payout-data preparation | payout authorization, applicant/customer communication, fraud/judgment |
| C044 | Менеджер клиентского сервиса | sales docs; contract/specification templates; closing/shipment docs; order status | customer negotiation, terms/commitments, commercial accountability |
| C045 | Специалист операционного отдела | forms; standard publishing/preparation; document register/flow | approval, ambiguous content, external communication |
| C046 | Специалист учебного центра | registries; personal-file data; system updates; statistics/reports; document register | decisions about people, official certification/approval, sensitive-data responsibility |
| C047 | Эксперт цифровых проектов | product-card intake/checks; DB corrections; supplier-content normalization; freshness monitoring | product/marketing judgment, supplier coordination, tender/commercial decisions |
| C048 | Ассистент маркетинга | Excel/Bitrix/1C data; contract/closing-doc prep; shipment/publication reports | marketing choices, counterpart communication, approvals |
| C049 | Lead Shopper / документооборот закупок | 1C PO/contract checklist; Diadok status; reports; supplier-doc completeness | supplier/commercial decisions, contract approval/signing, negotiation |
| C050 | Ведущий специалист закупок ОЦО | checklist validation; notices/material preparation from approved inputs; registers/status | procurement strategy, legal/compliance judgment, participation/submission authority |
| C051 | Помощник руководителя / ведущий специалист | contract cards; approved-template contracts; approval status; correspondence/registers | contract terms, legal judgment, approvals and external commitments |

## 3. Tranche 04 — V001–V008

| Record | Observed role | Candidate machine-work slice | Keep with human / Principal |
|---|---|---|---|
| V001 / hh 137357096 | Мартфарм — Оператор 1С (документооборот) | template addenda/letters; signed-doc return tracking; document status/registers | claim/termination decisions, legal/commercial wording approval |
| V002 / hh 136893634 | Сфера Эстетики — Оператор 1С / заказы | sales-order entry; invoices; shipping docs; status control | physical shipment, customer exceptions, regulated marking actions |
| V003 / hh 137035900 | ТД МАФ — ввод данных в 1С | primary-doc entry; material movement/writeoff records; registers; accompanying docs | inventory/accounting judgment and exception resolution |
| V004 / hh 137110041 | Ситилаб — НСИ / каталог | dictionary/catalog mapping; required-field checks; service-record proposals | semantic/service-policy decisions, system-change approval |
| V005 / hh 137320977 | ЛБТ — маркировка | card/code data prep; 1C↔marking reconciliation; exception detection | regulated code lifecycle actions, compliance responsibility |
| V006 / hh 136588879 | АНАЛИТИКА — маркировка | goods-movement/EDO data prep; reconciliation; draft reporting data | statutory reporting, legislation interpretation, external-system authority |
| V007 / hh 137062000 | Наос Восток — Честный знак | code-request data; movement-doc prep; 1C↔system checks; error queue | regulated submission/actions, legislation monitoring, compliance decisions |
| V008 / hh 136979178 | Лотте КФ Рус — маркировка | product-card/code data; national-catalog data prep; invoice/admin records | regulatory interpretation, external coordination, final marking authority |

## 4. Throughput-cost corpus 02

| Record | Observed role | Candidate machine-work slice | Keep with human / Principal |
|---|---|---|---|
| T003 / hh 136761302 | Пионер — первичные документы | realization data → validate → 1C realization → UPD → EDO/status; 15–20 realizations/day evidence | accounting judgment, exception approval, payment authority |
| T004 / hh 136775615 | РуссКом — document closure | returned signed-document-set tracking; completeness/status; primary-doc register | supplier/customer escalation, acceptance of ambiguous docs, accounting responsibility |

## 5. Tranche 05 — Zarplata.ru

| Record | Observed role | Candidate machine-work slice | Keep with human / Principal |
|---|---|---|---|
| Z001 / 137395562 | Блю Вэйл / Aivel — первичка | primary-doc validation; requisites; discrepancy detection; 1C nomenclature/counterparty cards; receipt reflection; reconciliations | accounting interpretation, client communication, final responsibility |
| Z002 / 136531527 | АКД — помощник бухгалтера | acts/invoices → 1C; bank-statement allocation prep; reconciliations; EDO status | actual payment authority, accounting exceptions |
| Z003 / 137165696 | Крона — бухгалтер | 1C UNF document processing; EDO send/receive prep; primary-doc status | signing/authorization, tax/accounting judgment |
| Z004 / 137010548 | Organic People — поставщики/первичка | supplier-doc collection/status; EDO; closing-doc control; corrections queue | supplier dispute/communication, accounting close decisions |
| Z005 / 136971852 | MEDIA GLOB — отчётность/документооборот | receive/check/scan/archive contracts; act preparation; receipts/acts collection; structured grant-report pack | contract approval/signing, grant-compliance judgment |
| Z006 / 137486192 | Руссторг — первичная документация | primary-doc processing; reconciliations; 1C UNF docs; UPD/account/MX form prep; EDO/original status | accounting judgment, signing and counterparty escalation |

## 6. Reconciliation result

Legacy counted records reconciled here: **33 / 33**.

Together with the explicit per-row boundaries already present in tranches 06–10:

- counted current corpus: **100 / 100 records**;
- records with an explicit machine-work vs residual-human boundary: **100 / 100**.

This does not establish machine feasibility. It establishes a disciplined **candidate boundary** for later benchmark and buyer validation.

## 7. Standing early-product exclusion

Across the corpus, the following are not part of the default autonomous Work slice:

- payment release / bank authorization;
- УКЭП/ЭП signing;
- final tax/statutory reporting;
- legal or regulatory interpretation;
- final procurement participation/submission;
- final regulated marking/Mercury/other consequential external-system action;
- physical custody/inventory decisions;
- non-template commercial negotiation or commitment;
- acceptance of ambiguous exceptions where the Principal must exercise judgment.

Those may only enter a later Job when authority, acceptance and liability boundaries are explicit.

No customer evidence, willingness-to-pay evidence, revenue or legal approval is created by this reconciliation.
