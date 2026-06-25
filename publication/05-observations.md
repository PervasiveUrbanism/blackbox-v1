# Observations

## What worked, what proved difficult, and what changed along the way

BlackBox was not developed to confirm a predefined theory about artificial intelligence. It began as an open-ended investigation, and many of its more useful observations only became visible through the process of building, testing, and revising the system.

Some findings confirmed the initial expectations. Others challenged assumptions that had seemed entirely reasonable at the outset. In several cases, the most important lesson was not related to the performance of an AI model at all, but to the conditions required for AI to become useful within a real working environment.

The observations that follow therefore concern more than the prototype itself. They describe a broader set of practical questions about open-source software, infrastructure, human judgement, bespoke tool development, and the changing role of architects in relation to software.

---

## Open-Source AI Is More Mature Than Expected

One of the earliest assumptions was that building an AI-assisted workspace would require a substantial budget, specialist developers, and dependence on commercial platforms. The reality proved more nuanced.

The core components of BlackBox—including Ollama, OpenWebUI, BookStack, PhotoPrism, Heimdall, and tldraw—were all available as open-source software and could be deployed on standard office hardware. Each addressed a different part of the problem, and together they provided much of the foundation required to construct a functioning prototype.

This did not mean that deployment was effortless. Installation, configuration, integration, maintenance, and user management still required considerable time and technical attention. Open source reduced the cost of access, but it did not remove the work involved in assembling reliable systems.

Nevertheless, the quality and range of the available tools exceeded the initial expectations. The significance of this lies not only in cost. Open-source software also made it possible to inspect, adapt, combine, and replace individual components in ways that would have been difficult within a closed commercial platform.

For small architectural practices, this creates a new kind of opportunity. Rather than waiting for a single software provider to deliver a complete solution, practices can assemble environments around their own priorities. The result may be less polished than a commercial product, but it can respond more precisely to the specific forms of knowledge and workflow that already exist within the office.

BlackBox depended heavily on the communities maintaining these systems. Their contribution was not peripheral to the project; it was one of the conditions that made the experiment possible.

---

## The Real Challenge Was Not AI

At the beginning of the project, most attention was directed towards the models themselves. Questions concerning output quality, prompting, local execution, and the relative value of open and commercial systems appeared likely to determine whether BlackBox would succeed.

As development progressed, a different picture emerged.

The most demanding problems were often found in the surrounding infrastructure. Authentication, user management, software integration, data structures, permissions, maintenance, and workflow design frequently required more effort than the AI components they were intended to support.

This distinction is easy to overlook because the model is the most visible part of the system. It produces the response, generates the description, or returns the search result. Yet that visible interaction depends on a much larger technical environment operating correctly behind it.

A useful AI system therefore cannot be evaluated only through the quality of its outputs. It must also be judged by whether people can access it reliably, whether data remains organised, whether permissions are appropriate, whether integrations can be maintained, and whether the workflow fits the conditions of everyday practice.

The development of BlackBox suggested that the integration of AI is as much an organisational and infrastructural challenge as a computational one. The model may provide the intelligence, but the wider system determines whether that intelligence can be used.

---

## Human Judgement Remains Central

Several components of BlackBox relied on AI-generated descriptions, labels, classifications, and search results. These processes demonstrated the value of automation, particularly where large quantities of information had to be analysed or indexed.

At the same time, the experiments repeatedly confirmed that human judgement remained essential.

Architects decided which images were worth collecting, which references were relevant, how keywords should be defined, whether a generated description was useful, and whether a search result supported the design question being asked. AI could increase the scale and speed of interpretation, but it could not determine the priorities of the practice using it.

The relationship that emerged was therefore not one of replacement. It was a division of responsibility.

AI performed tasks that benefited from scale: analysing images, generating descriptions, searching archives, and processing information across large collections. Human users supplied context, intention, critical judgement, and the ability to recognise when an apparently plausible result was inappropriate.

The coexistence of human-controlled keywords and AI-generated labels within PhotoPrism made this relationship visible. Human keywords provided a stable and deliberate taxonomy. AI-generated labels introduced additional interpretations and associations that would have been difficult to produce manually at scale.

Neither system was sufficient on its own. Human classification offered consistency but was labour-intensive and necessarily selective. Automated interpretation offered breadth but remained variable and dependent on evaluation. Their combination produced a richer archive than either approach could have achieved independently.

This suggests a more useful way of framing AI in architectural practice. Its value may lie less in autonomous decision-making than in extending the capacity of practitioners to organise, interpret, and retrieve material while leaving responsibility for meaning and relevance with the human user.

---

## Small Problems Become Worth Investigating

Architectural practices contain many recurring problems that are too specific to attract commercial software development.

How can previous competition narratives be searched? How should successful AI prompts be shared between colleagues? How can a large image archive remain useful over time? How can internal documentation become easier to access?

Individually, these questions may appear minor. They rarely justify the cost of commissioning a dedicated software system, yet collectively they consume time, reduce continuity, and contribute to the gradual loss of organisational knowledge.

In most offices, they are addressed through improvised workflows: folders, spreadsheets, naming conventions, shared drives, or the memory of a particular colleague. These solutions may work temporarily, but they are difficult to scale and often depend on individual habits rather than shared systems.

AI-assisted development changes the threshold at which such problems become worth investigating.

Throughout BlackBox, conversational planning, agentic coding, and iterative testing made it possible to explore highly specific workflows without a conventional software team. The objective was not to create a polished commercial product for each problem. It was to test whether a useful internal tool could be produced with a level of effort proportionate to the issue it addressed.

This shifts the economics of bespoke software. A problem no longer needs to affect thousands of users before it becomes viable to develop a response. A small office can investigate a narrow requirement because the cost of prototyping has fallen substantially.

The consequence may be a more diverse software landscape in which practices build tools around their own methods rather than adapting every workflow to the assumptions embedded within generic applications.

This observation may prove more consequential than any individual component of BlackBox. The project demonstrated not only that bespoke tools could be built, but that problems previously considered too small for software development could become legitimate subjects of experimentation.

---

## The Questions Became More Interesting Than the Answers

Towards the end of the development period, it became increasingly difficult to describe BlackBox as a single product moving towards completion.

Each successful experiment generated further questions. The integration of image archives led to investigations into embeddings, semantic similarity, and the difference between object recognition and architectural interpretation. Documentation systems raised questions about conversational retrieval, authorship, and the maintenance of office knowledge. Collaborative environments suggested possible forms of AI-assisted ideation and visual organisation.

The prototype therefore expanded through consequences rather than through a fixed feature list. Solving one problem exposed another layer of the same problem, while connecting two components often created an entirely new direction of inquiry.

This pattern changed the way the project was understood. BlackBox gradually became less a product than a framework for investigating different aspects of AI-assisted architectural practice. Its components remained connected, but each also developed into a research question in its own right.

The image archive was not only an archive; it became an investigation into architectural metadata and semantic retrieval. The documentation platform was not only a wiki; it became a test of whether organisational knowledge could support contextual AI. The coding process was not only implementation; it became evidence that architects could engage directly in bespoke software development.

This explains why the project never reached a conventional endpoint. A finished product would have required the scope to close, yet the principal value of the prototype lay in its ability to reveal further areas of inquiry.

BlackBox should therefore be understood as a connected set of investigations rather than a completed system. The software demonstrated what could be built, but the questions emerging from its development proved more transferable than the prototype itself.

That distinction matters for the chapters that follow. The conclusions of the project do not depend on whether BlackBox continues in its original form. They arise from what the process revealed about organisational memory, contextual AI, and the changing accessibility of bespoke software development within architectural practice.