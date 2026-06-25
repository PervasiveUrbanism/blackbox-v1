# The BlackBox Experiment

## A conversational interface to architectural knowledge

BlackBox began with a practical question: how might artificial intelligence become genuinely useful within the everyday work of an architectural practice?

At the time, much of the public discussion surrounding AI focused on generation. New tools appeared almost weekly, promising to produce floor plans, renderings, masterplans, or conceptual images from increasingly simple prompts. While technically impressive, these demonstrations often overlooked a fundamental aspect of architectural practice. Architects spend a considerable amount of time engaging with existing knowledge: previous projects, technical standards, reference images, competition submissions, design narratives, and the many informal lessons accumulated through work.

BlackBox approached the question from a different direction. Rather than asking how AI could generate architecture, the project investigated whether it could provide a conversational interface to the knowledge that already existed within a practice. Project documentation, technical standards, visual references, sketches, and AI conversations all have different characteristics and therefore benefit from different tools. The objective was not to replace those tools with a single application, but to connect them through a shared interface.

The resulting prototype was conceived as a modular ecosystem of specialised applications. Each component retained responsibility for the form of knowledge it managed best, while the conversational layer created a common point of access. This made it possible to ask a question without first knowing where the relevant information had been stored.

One of the first surprises was the maturity of the open-source ecosystem surrounding artificial intelligence. Many of the technologies required to assemble such a system were already available free of charge, actively maintained, and capable of running on standard office hardware. Rather than depending on a single commercial platform, BlackBox could therefore be built as a flexible environment tailored to the needs of an architectural practice.

---

![FIGURE 03 — Technical BlackBox Ecosystem Diagram](assets/diagrams/Stack.png)

*OpenWebUI as the central interface connecting AI models with documentation, image archives, and collaborative environments.*

---

## A Modular AI Architecture

The decision to adopt a modular architecture was not simply a technical preference. It reflected the expectation that artificial intelligence would continue to evolve rapidly. Language models improve, new applications appear, and commercial services frequently change their capabilities and pricing. A system built around a single model or provider therefore risks becoming obsolete within a relatively short period.

BlackBox instead separated the conversational interface, the language models, the documentation platform, the image archive, and the supporting infrastructure into independent components. Each could evolve or be replaced without requiring the remainder of the system to be redesigned. This architectural decision proved more important than the selection of any individual software package.

### Ollama: decoupling the language model

At the foundation of the system sat [Ollama](https://ollama.com), an open-source framework for running Large Language Models locally.

Ollama made it possible to download, manage, and switch between different models without changing the surrounding software environment. During development, several models were tested for tasks ranging from general language assistance to image description and classification.

Its significance extended beyond local execution. More importantly, Ollama separated the model itself from the applications that depended on it. The wider system communicated with Ollama rather than with a particular model, allowing the underlying AI engine to be exchanged while the broader ecosystem remained unchanged.

In this sense, Ollama acted as an abstraction layer between the applications and the AI models. This reduced dependence on any single provider and allowed BlackBox to evolve alongside a rapidly changing AI landscape.

### OpenWebUI: separating the interface from the model

While Ollama provides the infrastructure for running language models, interaction normally takes place through the command line. This is suitable for experimentation, but unlikely to support routine office use.

[OpenWebUI](https://openwebui.com) was therefore introduced as the primary user interface. It provided a familiar conversational environment while remaining independent of the underlying model. The same interface could connect to locally hosted models running through Ollama or to commercial services such as OpenAI and Anthropic, depending on the task.

This separation between interface and model became one of the central principles of BlackBox. Users could work within a consistent environment while the underlying intelligence changed according to performance, privacy, cost, or availability. The system was therefore designed around continuity of access rather than loyalty to a particular AI service.

---

## The Software Ecosystem

The prototype combined a number of specialised applications:

- [**Ollama**](https://ollama.com) — local execution and management of Large Language Models.
- [**OpenWebUI**](https://openwebui.com) — conversational interface connecting users, models, and external systems.
- [**BookStack**](https://www.bookstackapp.com/) — structured documentation platform for standards, workflows, and office knowledge.
- [**PhotoPrism**](https://www.photoprism.app/) — image archive with AI-assisted descriptions and semantic search.
- [**tldraw**](https://tldraw.dev/quick-start) — collaborative visual workspace and experimental ideation environment.
- [**Heimdall**](https://heimdall.site/) — dashboard providing a single point of access to all applications.

Each application maintained a distinct role. AI did not replace their specialised functions; it provided a common method of navigating between them. Heimdall acted as the practical entry point into the environment, while OpenWebUI formed its conversational centre.

---

![FIGURE 04 — Heimdall Dashboard](assets/screenshots/BB_Homescreen.png)

*The Heimdall dashboard acting as a central entry point into the BlackBox environment.*

---

## Visual References and Architectural Knowledge

Images play a fundamental role in architectural practice. Architects collect visual references continuously throughout a project, including precedent buildings, interiors, material samples, landscape references, furniture, construction details, textures, lifestyle imagery, photography, and CGI references.

A significant amount of time is often spent assembling these collections, particularly during competitions and early-stage concept design. The difficulty is rarely finding images in the first instance. It is rediscovering the right image when it becomes relevant months or years later.

Conventional image collections rely on folders, filenames, and manually assigned keywords. In practice, architectural archives often evolve in a less structured way. Images are gathered rapidly during design work, copied between projects, downloaded from websites, stored on personal drives, and reused in presentations. Over time, collections can grow into thousands of files distributed across multiple locations with only limited organisation.

Expecting architects to describe and curate every image in detail is rarely realistic. At best, a lightweight folder structure and a small number of keywords may be maintained. The time required to organise a large archive often exceeds the time available during project work.

This suggested a role for AI that extended beyond retrieval. Rather than expecting users to classify every image manually, BlackBox investigated whether AI could assist with the curation process itself. Images could enter the archive with minimal organisation, while AI generated descriptions, labels, and metadata that made them easier to search later.

The ambition was not to replace human judgement. Architects would continue to decide which references were worth collecting and how they related to a project. AI would instead undertake part of the repetitive labour involved in describing and indexing large quantities of visual material. In this way, the archive could remain simple to contribute to while acquiring a richer descriptive layer over time.

---

## PhotoPrism and AI-Assisted Image Analysis

[PhotoPrism](https://www.photoprism.app/) was selected as the image management platform because it combined a robust archive with support for metadata, automation, and AI-assisted workflows.

When a new image was uploaded, a custom workflow automatically triggered an AI analysis. A locally hosted model received the image together with a prompt developed specifically for architectural references.

The prompt became an important part of the experiment. A generic image caption might identify a building, a chair, or a landscape, but this would provide limited value to an architect searching for spatial ideas. The model was therefore instructed to interpret images through an architectural lens, identifying spatial characteristics, typologies, material qualities, atmosphere, programme, landscape conditions, and broader design themes.

Considerable effort was invested in refining this prompt. It gradually became a form of organisational knowledge in its own right: a reusable method for directing a general-purpose model towards a particular architectural mode of interpretation.

The analysis produced two outputs:

- a written architectural description;
- a set of architectural labels.

These AI-generated fields existed alongside manually assigned keywords. The two systems served different purposes.

Human keywords remained under deliberate control and represented a stable office taxonomy. They reflected decisions about how projects, references, materials, and themes should be categorised. AI-generated descriptions and labels were more fluid, introducing interpretations, associations, and observations that would have been difficult to maintain manually across thousands of images.

The intention was not to replace one form of classification with the other. Human judgement provided structure and consistency; AI provided scale and interpretive breadth. Their combination became one of the more consequential design decisions within BlackBox.

---

![FIGURE 05 — PhotoPrism AI Labelling](assets/screenshots/PP_AI_Details.png)

![FIGURE 05a — PhotoPrism AI Description](assets/screenshots/PP_AI_Labels.png)

*Example of AI-generated descriptions and architectural labels automatically assigned after image upload.*

---

## Conversational Access to Images

A custom integration connected OpenWebUI with the PhotoPrism archive. This allowed architects to retrieve references through natural language rather than by navigating folders or predefined categories.

The more interesting possibility was the retrieval of images through abstract architectural concepts. A request could take the form:

> Show me examples of projects that explore the idea of a void.

Rather than looking for a literal filename or a fixed keyword, the system attempted to interpret the conceptual intent of the request and match it against the descriptions and labels generated during image analysis. OpenWebUI formulated the search, queried the PhotoPrism database, and returned relevant references within the conversation.

This changed the role of metadata. Descriptions were no longer simply records attached to images; they became the linguistic layer through which visual material could participate in a design discussion.

---

![FIGURE 06 — PhotoPrism Labels](assets/screenshots/BB_PP_Search.png)

*Natural language search of the PhotoPrism archive through OpenWebUI.*

---

The retrieval process relied primarily on textual descriptions and AI-generated labels. A future development stage was planned around image embeddings, allowing visual and semantic relationships to be explored beyond explicit descriptions.

---

## Documentation and Organisational Knowledge

Visual references represent only one part of the knowledge accumulated within a practice. Technical standards, workflows, onboarding guides, lessons learned, software instructions, and project procedures are equally important, but they are often dispersed across folders, emails, shared drives, and the memories of individual staff members.

The BlackBox prototype therefore required a documentation platform that could support two audiences at once. It needed to remain straightforward enough for staff to read and update as part of everyday work, while also imposing sufficient structure for information to be searched and retrieved by AI.

[BookStack](https://www.bookstackapp.com/) was selected because its structure closely resembled an office wiki. Documentation could be organised into books, chapters, and pages, creating a clear hierarchy without requiring specialist technical knowledge. Workflows, standards, onboarding material, software instructions, and lessons learned could be maintained within a shared environment rather than remaining as isolated documents.

Its collaborative editing model was equally important. Organisational memory cannot remain useful if it is treated as a finished archive. Procedures change, software develops, projects produce new lessons, and responsibilities move between people. BookStack allowed documentation to evolve through continued contribution rather than periodic replacement.

This was the principal reason for its inclusion in BlackBox. The objective was not simply to store information, but to create a living body of office knowledge that could be refined by staff and accessed through AI-assisted retrieval. BookStack provided the human-readable structure from which a conversational organisational memory could begin to emerge.

---

![FIGURE 07 — BookStack Documentation](assets/screenshots/BS_Screen.png)

*Structured office documentation including workflows, standards, technical guides, and user instructions.*

---

## Towards AI-Assisted Ideation

The project also explored [tldraw](https://tldraw.dev/quick-start) as a collaborative visual environment. Unlike the other components, this part of the prototype remained largely experimental.

The ambition was not simply to add a digital whiteboard. It was to investigate whether the knowledge retrieved from different parts of BlackBox could enter a more visual form of architectural thinking. References from PhotoPrism, documentation from BookStack, and conversations developed in OpenWebUI could potentially be assembled within a shared workspace for concept development and early-stage ideation.

The idea was related to emerging AI-assisted whiteboard environments such as Miro AI, but with an important distinction. The material available to the system would be drawn from office-specific archives rather than generic online sources. In principle, the ideation environment could therefore reflect the references, terminology, methods, and accumulated experience of the practice using it.

Although this component remained exploratory, it indicated a possible extension of the wider argument. AI could support not only the retrieval of organisational knowledge, but also the arrangement and development of that knowledge during design.

---

![FIGURE 08 — Drawing Canvas](assets/screenshots/BB_Canvas.png)

*Experimental collaborative environment for sketches, references, diagrams, and future AI-assisted ideation.*

---

By combining these components, BlackBox became a prototype for a conversational organisational memory. Its purpose was less to generate architecture than to create new ways of accessing knowledge that already existed within the practice.

The experiment therefore tested a broader proposition: that conversational interfaces, AI-assisted indexing, and modular software ecosystems could make office knowledge more accessible, searchable, and useful without requiring it to be consolidated into a single application. The software formed the technical evidence, but the underlying question concerned the relationship between architectural practice and the knowledge it continuously produces.