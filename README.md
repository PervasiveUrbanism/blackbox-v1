# BlackBox V1

## AI, Organisational Memory and Architectural Practice

BlackBox V1 was an experimental investigation into how artificial intelligence could support the knowledge, culture, and everyday workflows of an architectural practice.

Developed between February and May 2026, the project explored a simple question:

> How do we preserve what we learn?

Architectural offices continuously generate knowledge. Every competition submission, fee proposal, design narrative, technical detail, material selection, graphic standard, consultant relationship, and internal discussion contributes to the collective experience of a practice.

However, this knowledge is often difficult to access. It becomes distributed across project folders, documents, image libraries, emails, and individual memory. While this information exists, it does not always participate in future decision-making.

BlackBox explored whether Large Language Models (LLMs) could provide a new interface between architects and this accumulated body of knowledge.

The objective was not to automate design or replace architectural judgement. The project investigated whether AI could support architects by retrieving previous experience, providing relevant context, accelerating repetitive tasks, and making organisational knowledge available at the moment it becomes useful.

This idea becomes particularly relevant when considering the nature of general-purpose AI systems.

A commercial or open-source LLM has broad knowledge of architecture, construction, history, technology, and language. However, it does not understand the specific culture of an individual architectural practice. It does not know the language of previous competition submissions, preferred references, established graphic approaches, successful technical solutions, or the internal reasoning behind past decisions.

The identity of an office is built through thousands of individual decisions accumulated over many years. Large international practices such as Zaha Hadid Architects or Foster + Partners are recognised not only because of individual projects, but because they have developed distinct methods of thinking, communicating, and presenting architecture.

BlackBox explored whether a general AI model could be provided with this missing context through access to an office's own organisational memory. The model itself would remain general, but its responses could be informed by the specific knowledge, language, and references of the practice.

The technical prototype combined a number of open-source applications including OpenWebUI, Ollama, BookStack, PhotoPrism, tldraw, and Heimdall within a locally hosted environment.

Local AI was initially selected for two reasons. The first was privacy. Architectural practices frequently work under confidentiality agreements, and sensitive project information cannot always be transferred to external AI services. The second was economic. A local model offered the possibility of experimentation without continuous usage costs.

The development successfully demonstrated that an AI-assisted workspace could be created by connecting specialised applications through a conversational interface. The project also revealed practical limitations, particularly regarding the performance of local models, the complexity of infrastructure, and the challenge of introducing new digital systems into established office workflows.

An unexpected outcome of BlackBox was the role of agentic software development. The project was developed through continuous collaboration between architectural expertise and AI coding tools. Discussions with ChatGPT helped formulate ideas, identify technical directions, and structure development tasks, while Codex was used to implement software integrations, scripts, and configurations.

The experience demonstrated a different relationship between domain experts and software development. Rather than waiting for commercial software providers to identify specific needs, architects can increasingly participate directly in the creation of their own digital tools and workflows.

BlackBox did not result in a final product. It was a case study that investigated both the opportunities and the limitations of introducing AI into architectural practice.

The broader conclusion of the project is that AI may not become most useful when acting as an autonomous designer. Its more immediate role may be as an assistant that helps practices retrieve knowledge, maintain continuity, communicate more effectively, and build upon their accumulated experience.

---

## Repository Structure

### publication

The main case study documenting the motivations, development, observations, and conclusions of the BlackBox experiment.

### assets

Diagrams, screenshots, and visual material used throughout the publication.

### sources

Original development documents, milestone records, user guides, and technical documentation produced during the project.

### notes

Additional reflections, quotations, and working material developed during the preparation of the publication.

---

## Main Themes

- AI in architectural practice
- Organisational memory and knowledge retrieval
- Office culture and design continuity
- Local and private AI infrastructure
- Agentic software development
- Human-AI collaboration

---

## Acknowledgement

BlackBox V1 was itself developed using AI-assisted workflows. The process of building the prototype became part of the research, demonstrating how AI can support not only architectural work but also the creation of new digital tools for architectural practice.