# Observations

By May 2026, BlackBox existed as a functioning prototype consisting of multiple interconnected applications accessible through the office network.

The experiment demonstrated that an AI-assisted workspace could be assembled using open-source applications, locally hosted AI models, and custom integrations. The central idea of connecting different forms of office knowledge through a conversational interface proved technically possible.

At the same time, the transition from a working prototype to a practical everyday office tool revealed a different set of challenges.

## The Difference Between a Prototype and an Office Tool

One of the most important observations was that technical feasibility does not automatically result in practical adoption.

BlackBox successfully connected image archives, documentation platforms, AI models, and collaborative environments. However, a successful office tool requires more than functionality. It must integrate naturally into existing workflows, provide immediate benefits, and require minimal effort from its users.

During the development process, the scale of the ecosystem gradually increased. Additional applications, user management systems, integrations, and custom workflows were introduced.

Looking back, a more incremental approach may have been more suitable. Instead of building a complete ecosystem, individual tools could have been introduced, tested with users, and expanded only once their value had been demonstrated.

This was an important lesson. The complexity of a system should be justified by the usefulness it provides.

## Local AI and Performance

The original intention of BlackBox was to investigate a fully local AI environment.

This decision was motivated by concerns regarding confidentiality and by the desire to experiment without recurring costs. These remain relevant considerations for architectural practices, particularly when working with confidential competition material or private clients.

The practical experience, however, showed clear limitations.

Local models could successfully perform many of the required tasks, including image classification, text generation, and information retrieval. However, response times were often considerably slower than commercial AI services.

This became particularly visible in more complex workflows.

For example, searching the PhotoPrism archive through OpenWebUI involved several stages. The system needed to interpret the user's request, formulate a search, query the image database, and return matching references. The workflow was functional, but the delay interrupted the natural conversational experience expected from AI systems.

The reliability of image retrieval was also dependent on the maturity of the indexing strategy. BlackBox V1 relied primarily on AI-generated descriptions and architectural labels. A later stage involving image embeddings was planned but not implemented within the timeframe of the project.

These observations suggested that a practical office system may benefit from a hybrid approach. Local models offer control over data and privacy, while commercial cloud services currently provide advantages in speed and capability.

## Infrastructure and Maintenance

Another observation concerned the amount of work required beyond the AI models themselves.

Installing and running a language model was only a small part of creating a usable office environment.

A functioning system required user management, network configuration, documentation, software maintenance, backups, and reliable communication between multiple applications.

As development progressed, a growing amount of time was spent maintaining the ecosystem rather than adding new features.

This highlighted a broader challenge: introducing AI into professional practice is not only a question of intelligence or model quality. It also requires robust infrastructure and long-term maintenance.

## Agentic Development as an Unexpected Outcome

One of the most interesting outcomes of BlackBox was not a feature of the final platform but the way in which it was developed.

AI-assisted development made it possible to move from an architectural problem to a functioning digital experiment within a relatively short period of time.

The importance of this observation was not that AI can write software. The more relevant insight was that architects can now investigate highly specific digital problems that previously would have been difficult to address through commercial software or traditional development processes.

The experience of BlackBox demonstrated this through concrete examples: the creation of a visual archive with AI-assisted indexing, the exploration of conversational access to office knowledge, and the integration of multiple specialised tools into a single environment.

Many of these experiments would have been difficult to justify as independent software projects.

The methods developed during BlackBox have continued beyond the project itself and have influenced later AI-assisted workflows in architectural practice.