# Building BlackBox

The development of BlackBox took place over approximately four months, from February to May 2026. The process did not begin with a complete technical roadmap. The concept evolved gradually as different technologies were explored and the understanding of the project became more precise.

The initial stage focused on establishing a local AI environment. Ollama and several Large Language Models were installed on a Mac workstation. OpenWebUI was subsequently introduced to provide a user interface through which these models could be tested and evaluated.

During this period, ChatGPT became a central development partner. The conversations were used to understand technical concepts, explore possible directions, compare software solutions, and translate broad ideas into concrete tasks.

As the concept developed, additional components were added to the ecosystem. PhotoPrism was introduced as an image archive, tldraw as a collaborative environment, BookStack as a documentation system, and Heimdall as a unified entry point to all applications.

The development workflow changed substantially with the introduction of Codex.

Early stages of the project involved discussing ideas with ChatGPT and manually implementing solutions. Later, these discussions were converted into structured development milestones that were passed to Codex, which carried out the implementation work.

The process became an iterative cycle:

Idea → Discussion → Development Plan → AI Implementation → Testing → Revision

This introduced a different relationship between professional expertise and software development. The architect remained responsible for defining the problem, evaluating the results, and deciding the direction of the project. AI tools accelerated implementation by writing scripts, configuring software environments, and assisting with technical integration.

A significant part of the later development focused on transforming a collection of individual applications into a coherent system.

The backend was organised through Docker containers, structured project folders, and Git version control. The frontend was refined through the development of a consistent Heimdall interface that allowed users to access the ecosystem through the office network.

One of the more technically demanding components was the connection between OpenWebUI and PhotoPrism. This required the development of custom scripts that allowed the AI interface to search the image archive directly.

Additional experimentation focused on AI-assisted image classification. New images added to PhotoPrism could be analysed by local language models and assigned custom architectural categories.

The project also explored more formal infrastructure, including centralised user management through Zitadel and the creation of a complete user guide within BookStack.

By the end of the development period, BlackBox existed as a working prototype consisting of multiple interconnected applications available through the office LAN.

The development process itself became one of the most interesting outcomes of the experiment.

BlackBox demonstrated how agentic coding changes the relationship between domain experts and software creation. A professional with detailed knowledge of a particular field can now participate directly in building specialised digital tools without following the traditional path of becoming a software engineer.

For architecture, this opens a possibility for more bespoke digital workflows. Offices are no longer entirely dependent on commercial software companies to identify and solve their specific needs. They can increasingly prototype, test, and develop their own tools.