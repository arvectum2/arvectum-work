# AW-020 — Customer Discovery Plan: Russia

Status: `Proposed 0.1.0`
Date: `2026-09-17`
Owner: `Arvectum Work`

## 1. Purpose

Customer discovery must test whether Russian buyers have recurring, bounded work they will pay to receive as an accepted result.

The interviews are not intended to validate enthusiasm for AI. They must reconstruct actual recent work, current cost, acceptance, buying authority and payment/procurement friction.

## 2. Initial buyer archetypes

Interview at least three archetypes before selecting the first wedge:

1. **SME / professional-services operations** — companies with recurring research, document, data and reporting tasks and short buying paths.
2. **Suppliers / contractors serving large Russian business** — repeated catalog, specification, commercial-research and document-processing work.
3. **Large-enterprise functional teams** — procurement, sales operations, finance operations, legal operations, analytics or back office where local/self-hosted execution and data sovereignty may matter.
4. **Public-sector / 223-FZ-adjacent buyers** may be interviewed for problem evidence, but no procurement applicability or route is assumed before exact current legal review.

The first paid transaction SHOULD prefer a buyer with a simple lawful commercial path rather than optimize for public-procurement complexity.

## 3. Recruitment target

Discovery target before AW-020 decision:

- `15–20` structured interviews;
- at least `3` buyer archetypes;
- `25+` concrete recent tasks;
- at least `10` tasks with a credible current cost, budget or price anchor;
- at least `5` buyers able to state conditions under which they would pay for a pilot;
- at least `2` buyers willing to provide a real bounded task.

These counts are stopping heuristics, not proof by volume.

## 4. Interview protocol

Do not lead with “Would you use an AI marketplace?”.

Use a recent-task reconstruction:

1. “Расскажите о последней задаче этого типа, которую реально выполняли.”
2. What triggered it?
3. Who requested it and who performed it?
4. What inputs were available?
5. What exact output was needed?
6. Who decided it was good enough?
7. What caused revisions or rejection?
8. How long did it take end-to-end?
9. What did it cost in money and employee/contractor time?
10. How often does the same class of work recur?
11. What data, system access or confidentiality was involved?
12. Why was the current method chosen?
13. What failure would make outsourcing unacceptable?
14. If an external executor returned the same accepted result with evidence, how would the company normally buy/pay for it?
15. Who can approve a bounded paid pilot and what must be true first?

Only after the concrete history is understood explain the Work concept and ask for objections.

## 5. Evidence record per interview

Store a privacy-safe record containing:

- interview ID and date;
- buyer archetype and company-size band;
- interviewee role/function, without unnecessary personal data;
- concrete task examples;
- current workaround;
- frequency;
- current cost/budget evidence quality;
- acceptance owner and criteria;
- data/security constraints;
- payment/procurement route as described by buyer;
- willingness-to-pay signal strength;
- pilot availability;
- direct objections;
- assumptions invalidated.

Do not publish confidential customer names, private documents, exact sensitive commercial terms or personal data in the public repository.

## 6. Signal quality ladder

From weakest to strongest:

`opinion → stated pain → recent concrete task → current spend/cost → pilot commitment → priced pilot → accepted paid result → repeat purchase`

Discovery decisions MUST prefer stronger signals over interview count.

## 7. What counts as willingness to pay

Strong signals include:

- buyer already pays employees/contractors/software for the outcome;
- buyer provides a real task and accepts a price before execution;
- buyer authorizes a paid pilot subject to explicit acceptance criteria;
- buyer explains an existing lawful payment path and the person/function that can approve it.

Weak signals include:

- “interesting idea”;
- generic desire to use AI;
- free pilot only with no purchasing path;
- hypothetical budget with no authority;
- requests to build a custom agent before defining the result.

## 8. Discovery questions to falsify the thesis

Actively look for:

- tasks where context transfer costs more than execution;
- outputs whose acceptance is political/subjective rather than testable;
- buyer policies that prohibit external/autonomous execution;
- very low task frequency;
- budgets below verification and support cost;
- mandatory human responsibility that removes autonomous economic advantage;
- buying cycles too heavy for the transaction value;
- data access that makes local execution necessary but operationally impractical.

## 9. First-pilot selection rubric

A pilot candidate should score well qualitatively on:

- real recent demand;
- repeat frequency;
- objective acceptance;
- low data sensitivity;
- low system-access privilege;
- short time-to-result;
- visible current cost;
- simple payment path;
- limited downside if wrong;
- Mac-mini execution feasibility.

No weighted score is a substitute for judgment; the purpose is to expose trade-offs.

## 10. AW-020 handoff

AW-020 may move to AW-030 only when one buyer segment and one job family have:

- repeated concrete demand;
- identifiable acceptance;
- credible price/current-cost evidence;
- a real pilot path.

Otherwise the result is `PIVOT` or `STOP`, not “build more product”.
