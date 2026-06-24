# Building BlackBox

## Developing an AI workspace through experimentation, iteration, and agentic workflows

The development of BlackBox took place over approximately four months between February and May 2026.

Unlike a conventional software project, there was no dedicated development team, detailed specification, or predefined roadmap. The project emerged through a series of experiments that gradually evolved into a working system. New ideas appeared as technologies were tested, and the direction of the project changed several times as new opportunities emerged.

Rather than beginning with a fixed vision of the final product, the process focused on understanding what was possible and identifying where AI could provide practical value within an architectural environment.

---

![FIGURE 09 — Development Timeline](assets/diagrams/Timeline.png)

*The evolution of BlackBox: from early experiments with local language models to an AI-assisted workspace.*

---

## Building Without a Software Team

The first stage focused on establishing a local AI environment.

Ollama was installed on an available workstation, allowing different open-source Large Language Models to be downloaded and tested locally. OpenWebUI followed shortly afterwards and became the primary interface through which these models could be evaluated through everyday use.

At this stage the objective was simply to explore the capabilities of local AI systems. The broader vision of BlackBox had not yet emerged. Questions about image archives, documentation systems, semantic search, and collaborative ideation only appeared later as the possibilities of the technology became clearer.

The development process therefore moved in small steps. Each successful experiment suggested a new direction of investigation.

Questions gradually accumulated:

- Could visual references be organised through AI?
- Could office documentation become accessible through conversation?
- Could different applications be connected into a unified environment?
- Could AI assist not only with retrieval, but also with curation?

Over time, these individual experiments began to form a coherent system.

---

## ChatGPT and Planning

One of the more unexpected aspects of the project was that AI became involved long before any software was written.

ChatGPT was used extensively as a discussion partner throughout the development process. Ideas were explored through conversation, alternative technologies were compared, and implementation strategies were developed before coding began.

Many development tasks were broken down into a sequence of smaller steps. Architectural objectives were translated into technical requirements, possible approaches were evaluated, and implementation plans were refined through discussion.

This proved particularly valuable because many of the questions being explored were unfamiliar. Rather than spending weeks researching every technical topic independently, it became possible to learn through dialogue while simultaneously moving the project forward.

In retrospect, a significant proportion of the project consisted not of coding, but of planning, questioning, and refining ideas through conversation.

---

## Codex and Implementation

Once a strategy had been established, implementation increasingly shifted towards Codex.

Rather than writing large quantities of code manually, development tasks were divided into small and manageable steps. Individual features were implemented one at a time, tested, reviewed, and only then incorporated into the wider system.

This incremental approach became essential as the complexity of BlackBox increased. The project combined multiple applications, databases, APIs, authentication systems, and AI services. Attempting to implement large changes in a single step often produced unreliable results.

Development therefore proceeded through a sequence of micro-iterations.

A feature would first be discussed and planned. The implementation would then be generated through Codex. The result would be tested, reviewed, and either accepted or revised before the next stage began.

The process was surprisingly effective. Complex integrations that would previously have required significant programming knowledge became achievable through a combination of clear problem definition, careful planning, and iterative testing.

---

![FIGURE 10 — Codex Development Interface](assets/screenshots/Codex.png)

*Using Codex to implement and refine individual components of the BlackBox environment.*

---

## Git, Testing, and Rollback

Version control became an essential part of the workflow.

Git was used to record development milestones and provide the ability to revert changes whenever experiments failed. Although AI-assisted coding accelerated development considerably, it did not eliminate mistakes. Some implementations worked immediately, while others introduced unexpected behaviour or solved the wrong problem entirely.

Several development branches had to be abandoned and rolled back after testing revealed unintended consequences.

The ability to return to a known working state provided the confidence to continue experimenting without risking the stability of the wider system.

In practice, Git and AI-assisted development proved highly complementary. AI increased the speed of implementation, while version control provided the safety net required to manage uncertainty.

The result was a workflow that encouraged experimentation while maintaining a reliable path back to a stable configuration.

---

![FIGURE 11 — Agentic Development Workflow](assets/diagrams/Development.png)

*Architectural problem → discussion with AI → technical roadmap → implementation → testing → revision.*

---

## Unexpected Challenges

Not all challenges were related to AI.

As the number of applications increased, a consistent approach to user management became necessary. Different systems required authentication, permissions, and user separation. What initially appeared to be a straightforward administrative task gradually became one of the more technically demanding aspects of the project.

Zitadel was introduced as an identity and access management system intended to provide single sign-on and centralised user management across the environment.

While conceptually simple, integrating authentication across multiple open-source applications proved considerably more complex than expected. A significant amount of development time was spent configuring, testing, and debugging user-management workflows.

Although largely invisible to end users, this infrastructure became essential. Without reliable authentication and user separation, the system could not realistically function as a shared office environment.

The experience highlighted an important lesson: building useful AI workflows is often easier than integrating them into a robust and maintainable system.

---

## Development as Research

One of the most interesting outcomes of BlackBox was that the development process itself became a form of research.

Many of the project's most useful observations emerged through implementation rather than theoretical discussion. Questions about model quality, software integration, maintenance requirements, usability, and long-term viability only became apparent once the system was operating.

The project therefore produced two forms of knowledge simultaneously. On one level it generated a working prototype. On another, it revealed practical insights into the opportunities and limitations of building AI-assisted tools within an architectural environment.

In this sense, the prototype was not simply the outcome of the investigation. It was also the method through which the investigation was conducted.

Several of the conclusions discussed in the following chapters emerged directly from the experience of building, testing, revising, and occasionally abandoning parts of the system.

The process reinforced a simple observation: some questions can only be answered by making something and seeing what happens.