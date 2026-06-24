# The BlackBox Experiment

## Building a conversational interface between architects and organisational knowledge

The BlackBox project explored whether an architectural office could create its own AI-assisted workspace by combining existing open-source applications, local AI models, and custom software integrations.

One of the first surprises during the development of the project was the maturity of the open-source ecosystem surrounding artificial intelligence. Many of the tools that formed the foundation of BlackBox were available free of charge and could be installed on standard office hardware. Rather than depending on a single commercial platform, the project was able to combine specialised applications into a modular environment tailored to the needs of an architectural practice.

The objective was not to develop a single application that performed every task. Instead, the project treated the office as an ecosystem of different forms of knowledge. Project documentation, technical standards, visual references, sketches, and AI conversations all have different characteristics and therefore benefit from different tools.

The BlackBox environment was organised around a central conversational interface through which these different sources of knowledge could be accessed.

---

![FIGURE 03 — Technical BlackBox Ecosystem Diagram](assets/diagrams/Stack.png)

*OpenWebUI as the central interface connecting AI models with documentation, image archives, and collaborative environments.*

---

## Ollama and the Language Models

At the foundation of the system sat Ollama, an open-source framework for running Large Language Models locally.

Ollama made it possible to download, manage, and switch between different models without changing the surrounding software environment. During development, various models were tested for different tasks, ranging from general language assistance to image description and classification.

This separation between the model and the surrounding applications proved important. The objective was never to build a system dependent on a particular AI provider. As models continue to evolve, the underlying AI engine can be replaced while the broader ecosystem remains unchanged.

In this sense, Ollama acted as an abstraction layer between the applications and the AI models themselves.

---

## Why OpenWebUI?

While Ollama provides the infrastructure for running AI models, interaction with these models normally takes place through the command line.

For experimentation this is perfectly acceptable, but it is unlikely to be suitable for everyday office use.

OpenWebUI was therefore introduced as the primary user interface. It provided a familiar conversational environment while remaining independent of the underlying model.

This proved particularly valuable because OpenWebUI could connect not only to locally hosted models running through Ollama, but also to commercial services such as OpenAI or Anthropic. The interface remained the same while the underlying model could be changed depending on the task.

This modular approach became one of the central principles of BlackBox. Individual components could evolve independently without requiring changes to the entire system.

---

## The Software Ecosystem

The main components of the system were:

- [**Ollama** ](https://ollama.com)— local execution and management of Large Language Models.
- [**OpenWebUI**](https://openwebui.com)— conversational interface connecting users, models, and external systems.
- [**BookStack**](https://www.bookstackapp.com/) — structured documentation platform for standards, workflows, and office knowledge.
- [**PhotoPrism**](https://www.photoprism.app/) — image archive with AI-assisted descriptions and semantic search.
- [**tldraw**](https://tldraw.dev/quick-start)— collaborative visual workspace and experimental ideation environment.
- [**Heimdall**](https://heimdall.site/)— dashboard providing a single point of access to all applications.

The intention was that each application maintained its own specialised role while AI provided a common method of navigating between them.

---

![FIGURE 04 — Heimdall Dashboard](assets/screenshots/BB_Homescreen.png)

*The Heimdall dashboard acting as a central entry point into the BlackBox environment.*

---

## Visual References and Architectural Knowledge

Images play a fundamental role in architectural practice.

Architects collect visual references continuously throughout a project. These may include precedent buildings, interiors, material samples, landscape references, furniture, construction details, textures, lifestyle imagery, photography, and CGI references.

A significant amount of time is often spent assembling these collections, particularly during competition work and early-stage concept design. The challenge is rarely finding images; it is finding the right image at the right moment.

Traditionally, image collections are organised through folders, filenames, and manually assigned keywords. While effective in theory, visual archives in architectural practice often evolve in a much less structured way.

Images are collected rapidly during design work, copied between projects, downloaded from websites, stored on personal drives, and reused in presentations. Over time, collections can grow into thousands of images distributed across multiple locations with only limited organisation.

Expecting architects to carefully curate and describe every image is rarely realistic. At best, a lightweight folder structure and a handful of keywords may be maintained. The effort required to organise a large image collection often exceeds the time available.

This suggested a role for AI that extended beyond retrieval.

Rather than expecting users to manually classify every image, BlackBox explored whether AI could assist in the curation process itself. Images could be uploaded with minimal organisation while AI generated descriptions, labels, and metadata that made the collection easier to search and navigate later.

The ambition was not to replace human judgement. Architects would still decide which images were worth collecting and how they related to a project. AI would instead perform part of the labour involved in describing and indexing large collections of visual material.

BlackBox therefore investigated whether AI could introduce an additional descriptive layer to architectural references while preserving a simple workflow for the people contributing to the archive.

---

## PhotoPrism and AI-Assisted Image Analysis

PhotoPrism was selected as the image management platform because it combined a robust image archive with support for metadata, automation, and AI-assisted workflows.

When a new image was uploaded, a custom workflow automatically triggered an AI analysis.

A locally hosted model received the image together with a carefully developed prompt designed specifically for architectural references.

The prompt itself became an important part of the experiment. Rather than asking the AI to simply describe an image, it was instructed to analyse the image from an architectural perspective.

The prompt encouraged the model to identify spatial characteristics, architectural typologies, material qualities, atmosphere, programme, landscape conditions, and broader design themes. The objective was to create descriptions that would be meaningful to architects rather than generic image captions.

Considerable effort went into refining this prompt. In many ways it represented a form of organisational knowledge itself: a carefully developed method for interpreting visual references through a particular architectural lens.

The output consisted of two elements:

- a written architectural description;
- a set of architectural labels.

These AI-generated fields existed alongside manually assigned keywords.

Human keywords and AI-generated labels served different purposes within the system.

Keywords remained under human control and represented a stable office taxonomy. They reflected deliberate decisions about how projects, references, materials, or themes should be categorised.

AI-generated descriptions and labels were more fluid. They introduced interpretations, associations, and observations that would have been difficult to maintain manually across thousands of images.

The intention was not to replace one system with the other, but to combine them. Human judgement provided structure and consistency; AI provided scale and flexibility.

This relationship between human classification and AI interpretation became one of the more interesting design decisions within BlackBox.

---

![FIGURE 05 — PhotoPrism AI Labelling](assets/screenshots/PP_AI_Details.png)

![FIGURE 05a — PhotoPrism AI Description](assets/screenshots/PP_AI_Labels.png)

*Example of AI-generated descriptions and architectural labels automatically assigned after image upload.*

---

## Conversational Access to Images

A custom integration connected OpenWebUI with the PhotoPrism archive.

This allowed architects to retrieve images through natural language rather than folders or predefined categories.

One of the more interesting aspects of this approach was the ability to search for abstract architectural concepts.

For example:

> Show me examples of projects that explore the idea of a void.

Rather than searching for a specific building type or keyword, the system attempted to interpret the conceptual intent of the request and match it against the AI-generated descriptions and labels stored within the archive.

OpenWebUI would formulate a search, query the PhotoPrism database, and return relevant references directly within the conversation.

---

![FIGURE 06 — PhotoPrism Labels](assets/screenshots/BB_PP_Search.png)

*Natural language search of the PhotoPrism archive through OpenWebUI.*

---

The retrieval process relied primarily on textual descriptions and AI-generated labels. A future development stage was planned around image embeddings, allowing visual and semantic relationships to be explored beyond explicit descriptions.

---

## Documentation and Organisational Knowledge

Not all office knowledge exists as images.

Technical standards, workflows, onboarding guides, lessons learned, software instructions, and project procedures are often equally important.

BookStack was selected because it combined a simple editing experience with a structure that closely resembled an office wiki.

Documentation could be organised into books, chapters, and pages, creating a hierarchy that remained understandable for both humans and AI systems. Workflows, standards, onboarding guides, software instructions, and lessons learned could be maintained within a shared environment rather than becoming isolated documents distributed across folders.

The platform also supported collaborative editing, making it possible for documentation to evolve over time rather than becoming a static archive.

This was particularly important because the ambition was not simply to store information. The longer-term vision was that BookStack could become a living organisational memory: a place where office knowledge was continuously refined by staff while simultaneously becoming accessible through AI-assisted retrieval.

---

![FIGURE 07 — BookStack Documentation](assets/screenshots/BS_Screen.png)

*Structured office documentation including workflows, standards, technical guides, and user instructions.*

---

## Towards AI-Assisted Ideation

The project also explored tldraw as a collaborative visual environment.

Unlike the other applications, this component remained largely experimental. The ambition was not simply to create a digital whiteboard, but to investigate whether future AI systems could participate in more visual forms of architectural thinking.

One possible workflow involved retrieving references from PhotoPrism, combining them with relevant knowledge from BookStack, and developing concepts through conversations taking place in OpenWebUI. These elements could then be assembled within a shared visual workspace for concept development and early-stage ideation.

The idea was not entirely dissimilar to emerging AI-assisted whiteboard environments such as Miro AI. The difference was that the knowledge available to the system would be drawn from office-specific archives rather than generic online sources.

Although this part of the project remained exploratory, it pointed towards a possible future in which AI is not only used for retrieval and search, but also participates in the creation and organisation of design ideas.

---

![FIGURE 08 — Drawing Canvas](assets/screenshots/BB_Canvas.png)

*Experimental collaborative environment for sketches, references, diagrams, and future AI-assisted ideation.*

---

By combining these different components, BlackBox became a prototype of an AI-assisted organisational memory system.

The project was less concerned with generating architecture than with creating new ways of accessing knowledge that already existed within the practice. The experiment explored whether conversational interfaces, AI-assisted indexing, and modular software ecosystems could make that knowledge more accessible, searchable, and useful within everyday work.