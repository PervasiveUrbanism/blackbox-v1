# The BlackBox Experiment - What did I build?

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
