# Building BlackBox

## Developing an AI workspace through experimentation, iteration, and agentic workflows

BlackBox was developed over approximately four months between February and May 2026. There was no dedicated software team, detailed specification, or fixed roadmap. The project began as a series of technical experiments and gradually developed into a working system as new possibilities became visible.

This mode of development was exploratory by necessity. Rather than defining a final product in advance, the work focused on identifying where AI could provide practical value within an architectural environment. Each successful experiment created the conditions for another question, and the scope of the project expanded through use rather than through formal planning.

The process therefore became as important as the prototype itself. BlackBox was not only an investigation into AI-assisted organisational memory; it was also a test of whether an architect, working without a conventional software team, could develop a bespoke digital environment through AI-assisted planning and coding.

---

![FIGURE 09 — Development Timeline](assets/diagrams/Timeline.png)

*The evolution of BlackBox: from early experiments with local language models to an AI-assisted workspace.*

---

## Building Without a Software Team

The first stage focused on establishing a local AI environment. Ollama was installed on an available workstation, allowing different open-source Large Language Models to be downloaded and tested. OpenWebUI followed shortly afterwards and provided a practical interface through which these models could be evaluated in everyday use.

At this point, the broader structure of BlackBox did not yet exist. The initial objective was simply to understand the capabilities and limitations of local AI systems. Questions concerning image archives, documentation, semantic search, and collaborative ideation emerged later, as the consequences of the first experiments became clearer.

Development proceeded through a sequence of small steps. Each working component suggested another possible application:

- Could visual references be organised through AI?
- Could office documentation become accessible through conversation?
- Could different applications be connected into a unified environment?
- Could AI assist not only with retrieval, but also with curation?

These questions were not resolved through a single design decision. They accumulated gradually, and the relationship between them only became apparent as the prototype developed. What began as a local language-model test eventually became a wider software ecosystem.

This incremental process resembled architectural design more closely than conventional software procurement. The system was not specified in full and then implemented. It was tested, observed, adjusted, and extended as new requirements emerged.

---

## ChatGPT and Planning

One of the more consequential aspects of the project was that AI became involved before any software was written.

ChatGPT was used extensively as a planning and discussion partner. Architectural objectives were translated into technical requirements, alternative technologies were compared, and implementation strategies were developed through conversation. Questions that initially appeared vague could be broken into smaller and more testable tasks before development began.

This was particularly important because many of the technical subjects were unfamiliar. Building BlackBox required engagement with databases, APIs, authentication, containers, local model hosting, and software integration. AI-assisted dialogue reduced the threshold for entering these areas by allowing technical research and project planning to happen together.

The process did not remove the need for judgement. Suggestions still had to be evaluated, assumptions checked, and technical directions selected. Its value lay in accelerating the movement from an architectural intention to a workable technical plan.

In retrospect, a substantial proportion of the project consisted not of coding, but of defining problems clearly enough for coding to become possible. The quality of the implementation often depended on the quality of the conversation that preceded it.

---

## Codex and Implementation

Once an implementation strategy had been established, development increasingly shifted towards Codex.

Rather than attempting to generate large quantities of software in a single step, the work was divided into small, manageable tasks. Individual features were implemented, tested, reviewed, and only then incorporated into the wider system. This became increasingly important as BlackBox began to combine multiple applications, databases, APIs, authentication systems, and AI services.

Large changes often produced unreliable results. They could introduce unexpected behaviour, solve the wrong problem, or make it difficult to identify where an error had occurred. Development therefore proceeded through micro-iterations: define a task, generate an implementation, test the result, review its consequences, and either retain or revise it before continuing.

This workflow altered the relationship between architectural practice and software development. Complex integrations that would previously have required specialist programming knowledge became achievable through a combination of clear problem definition, AI-assisted implementation, and careful testing.

The significance of this shift extends beyond BlackBox. Small architectural practices often identify the need for highly specific digital tools but lack the resources to commission custom software. Agentic coding lowers that threshold. It does not eliminate technical complexity, but it allows practitioners to engage with software development directly enough to test ideas that might otherwise remain unrealised.

---

![FIGURE 10 — Codex Development Interface](assets/screenshots/Codex.png)

*Using Codex to implement and refine individual components of the BlackBox environment.*

---

## Git, Testing, and Rollback

The speed of AI-assisted implementation made version control essential.

Git was used to record development milestones and to provide a reliable path back whenever an experiment failed. AI-assisted coding accelerated the production of new features, but it did not eliminate mistakes. Some implementations worked immediately; others introduced unintended behaviour, created dependencies that were difficult to maintain, or addressed the wrong interpretation of the problem.

Several branches of development were abandoned after testing revealed consequences that were not visible during implementation. In these cases, rollback was not a sign of failure but part of the research process. Returning to a known working state made it possible to test alternatives without destabilising the wider system.

Git and agentic development therefore proved highly complementary. AI increased the speed and range of experimentation, while version control created the discipline required to manage that experimentation safely. Together they supported a workflow in which uncertainty could be explored without losing control of the project.

This balance is particularly important for small practices. Faster implementation is only useful if the resulting system remains understandable, reversible, and maintainable. Agentic coding creates new possibilities, but those possibilities still require a robust development method.

---

![FIGURE 11 — Agentic Development Workflow](assets/diagrams/Development.png)

*Architectural problem → discussion with AI → technical roadmap → implementation → testing → revision.*

---

## Unexpected Challenges

Not all of the difficult work concerned artificial intelligence.

As the number of applications increased, a consistent approach to user management became necessary. Each system had its own requirements for authentication, permissions, and user separation. What initially appeared to be an administrative detail gradually became one of the more technically demanding parts of the project.

Zitadel was introduced as an identity and access-management system intended to provide single sign-on and centralised user administration across the BlackBox environment. The principle was straightforward, but implementation across several open-source applications proved considerably more complex than expected. A significant amount of development time was spent configuring, testing, and debugging authentication workflows.

This infrastructure remained largely invisible to the user, yet it was essential to the credibility of the prototype. Without dependable authentication and user separation, BlackBox could not function as a shared office environment.

The experience exposed an important distinction between a technical demonstration and an operational tool. Creating an isolated AI workflow may be relatively straightforward. Integrating that workflow into a secure, maintainable, multi-user environment requires a different level of effort.

This also revealed a limitation of agentic coding. AI can help produce integrations quickly, but the surrounding responsibilities of deployment, access control, testing, maintenance, and support do not disappear. For small businesses, the opportunity to build bespoke software is therefore accompanied by a need to understand the infrastructure on which that software depends.


---
![FIGURE 12 — Zitadel](assets/screenshots/Zitadel.png)

*User management in Zitadel*

---


## Development as Research

The development process became a form of research in its own right.

Many of the project's more useful observations emerged through implementation rather than theoretical discussion. Questions concerning model quality, software interoperability, authentication, maintenance, usability, and long-term viability only became visible once the system was operating.

BlackBox therefore generated two forms of knowledge simultaneously. On one level, it produced a working prototype. On another, it revealed the practical conditions under which AI-assisted tools might be developed and sustained within an architectural practice.

The prototype was consequently not only the outcome of the investigation; it was also the method through which the investigation was conducted. Building, testing, revising, and occasionally abandoning parts of the system created the evidence from which the later observations and conclusions emerged.

This distinction matters because the third proposition of BlackBox concerns more than the availability of coding tools. Agentic development may allow small practices to create bespoke software, but the process remains iterative, uncertain, and dependent on critical judgement. The accessibility of implementation does not remove the need for research; it changes who is able to conduct it.

Several conclusions discussed in the following chapters emerged directly from this process. Some questions could only be answered by making the system, placing it in use, and observing where the initial assumptions held or failed.