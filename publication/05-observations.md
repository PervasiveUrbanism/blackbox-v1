# Observations

## What worked, what proved difficult, and what changed along the way

The purpose of BlackBox was never to validate a predefined theory about artificial intelligence. The project emerged through experimentation, and many of the more interesting observations only became apparent during development.

Some confirmed initial expectations. Others challenged assumptions that seemed reasonable at the beginning of the project.

The following observations emerged directly from the process of building and testing the system.

---

## Open Source AI Is More Mature Than Expected

One of the most surprising discoveries was the maturity of the open-source ecosystem surrounding artificial intelligence.

At the beginning of the project, it would have been reasonable to assume that creating an AI-assisted workspace required a substantial budget and a dependence on commercial platforms. The reality was rather different.

The core components of BlackBox—including Ollama, OpenWebUI, BookStack, PhotoPrism, Heimdall, and tldraw—were all available as open-source software and could be deployed on standard hardware.

This did not mean that deployment was effortless. Installation, configuration, maintenance, and integration still required considerable work. Nevertheless, the quality and capability of the available tools exceeded expectations.

One of the outcomes of the project was a greater appreciation for the open-source communities that maintain these systems. BlackBox would not have been possible without them.

---

## The Real Challenge Was Not AI

At the beginning of the project, most attention was focused on AI models themselves.

Questions about model quality, prompting techniques, and local versus cloud-based systems appeared central to the success of the project.

Over time, a different picture emerged.

The most difficult challenges were often unrelated to AI. Authentication, user management, software integration, data structures, maintenance, and workflow design frequently required more effort than the AI components themselves.

The experience suggested that AI is often the most visible part of a system, but not necessarily the most complex.

Creating a reliable environment in which AI can operate effectively remains a significant design challenge in its own right.

---

## Human Judgement Remains Central

Several parts of BlackBox relied on AI-generated descriptions, labels, classifications, and search results.

Yet throughout the project it became clear that human judgement remained essential.

Architects decided which images were worth collecting. They defined keywords, selected references, evaluated results, and determined whether a particular response was useful or irrelevant.

The relationship that emerged was therefore not one of replacement but of collaboration.

In many cases, AI performed tasks that benefited from scale: analysing images, generating descriptions, searching archives, or processing information. Human users provided context, priorities, and judgement.

One of the more interesting design decisions within BlackBox reflected this relationship directly. Human-controlled keywords coexisted with AI-generated labels. The two systems served different purposes and complemented one another rather than competing.

---

## Small Problems Become Interesting Again

Architectural offices contain many small problems that rarely attract commercial software development.

How can previous competition narratives be searched?

How should successful AI prompts be shared between colleagues?

How can a large image archive remain useful over time?

How can internal documentation become easier to access?

Individually, these questions are often too specific to justify dedicated software development. As a result, they are frequently solved through improvised workflows or not addressed at all.

AI-assisted development changes this equation.

Throughout the project it became possible to investigate highly specific problems that would previously have required a dedicated software team. The combination of conversational planning, AI-assisted coding, and iterative testing significantly lowered the threshold for experimentation.

This observation may ultimately prove more important than any particular software component used within BlackBox.

---

## The Questions Became More Interesting Than the Answers

Perhaps the most unexpected observation emerged towards the end of the project.

Each successful experiment tended to generate additional questions.

The integration of image archives led to questions about embeddings and semantic similarity. Documentation systems suggested new approaches to knowledge retrieval. Collaborative environments raised questions about AI-assisted ideation and design support.

As the system grew, it became increasingly clear that BlackBox was not moving towards a single final product.

Instead, it was becoming a framework through which different aspects of AI-assisted architectural practice could be explored.

This observation would later influence how the project itself was understood. BlackBox was less a completed system than a collection of connected investigations, each opening further areas of inquiry.

The value of the project therefore resided not only in the prototype that was produced, but also in the questions that emerged through the process of building it.