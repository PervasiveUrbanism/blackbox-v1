# Observations - What surprised me?

## What the prototype revealed

By the time the first working version of BlackBox was operational, many of the original technical questions had already been answered. Local language models could run successfully, documentation systems could be connected, images could be analysed automatically, and individual applications could exchange information.

Surprisingly, these technical achievements were not the most interesting outcome of the project.

As the system gradually took shape, it became clear that the prototype was revealing just as much about architectural practice as it was about artificial intelligence. Assumptions I had held at the beginning of the project were repeatedly challenged, often in unexpected ways.

One of the first surprises was the maturity of the open-source AI ecosystem.

When the project began, I expected local AI to involve significant technical compromises and a fragmented collection of unfinished software. Instead, I discovered an impressive ecosystem of applications that could be combined into a coherent working environment. Ollama, OpenWebUI, BookStack, PhotoPrism, Heimdall, Docker, n8n and many other projects demonstrated that sophisticated AI environments were no longer reserved for large technology companies. They could be assembled on an ordinary workstation using freely available software.

Equally important was the modular nature of these tools. None of them attempted to solve every problem. Each application focused on a particular task, yet together they formed an ecosystem that was remarkably flexible. This gradually changed the way I thought about software development. Rather than searching for one comprehensive application, it became possible to think in terms of small, specialised components connected through well-defined interfaces.

The second surprise concerned the process of development itself.

Before BlackBox, I would have assumed that building a system like this required years of software engineering experience. Instead, artificial intelligence fundamentally changed the relationship between architect and programmer.

Development became conversational.

Ideas were first discussed with ChatGPT, where broader strategies, technical alternatives and implementation approaches could be explored without writing a single line of code. As these discussions matured, they were broken down into smaller development tasks before being implemented with Codex.

The work rarely happened in large leaps. Features were developed one step at a time, committed to Git, tested, evaluated and refined before the next step began. On several occasions Git rollback became just as valuable as the implementation itself, allowing unsuccessful experiments to be abandoned without hesitation.

This iterative workflow felt surprisingly familiar. It resembled the way architects develop projects: exploring alternatives, testing ideas, reviewing the outcome and gradually refining the solution rather than attempting to solve everything in a single move.

Another observation emerged from an entirely different direction.

At the beginning of the project, prompts appeared to be temporary instructions written for a single conversation with an AI model. Over time, however, I realised that carefully developed prompts represented valuable intellectual work in their own right.

Considerable experimentation was often required before an AI consistently produced useful architectural descriptions, meaningful image labels or reliable search results. Once refined, these prompts became reusable assets that could benefit other members of the practice.

In many respects they began to resemble Grasshopper definitions, Dynamo scripts, Revit families or carefully developed office templates. They represented knowledge that had been accumulated through experimentation and was worth preserving rather than recreating.

The experiments with PhotoPrism produced another unexpected insight.

Initially, I imagined that AI might eventually replace manual image organisation. Instead, the project demonstrated that human judgement and AI interpretation complemented one another remarkably well.

Architects remained responsible for selecting meaningful references and providing a lightweight organisational structure. AI then contributed detailed descriptions, semantic labels and architectural observations that would have been impractical to create manually across thousands of images.

Neither approach proved sufficient on its own.

Together they created a richer and considerably more useful archive than either manual organisation or automated tagging could have achieved independently.

Perhaps the most significant observation only became clear towards the end of the project.

I originally believed I was building a single AI application.

Looking back, I realise that BlackBox gradually became something quite different.

Every successful experiment suggested another possibility. Semantic image search led naturally to conversational retrieval. Documentation suggested AI-assisted onboarding. Prompt engineering became a form of organisational knowledge. AI-assisted software development revealed opportunities for creating bespoke digital tools that would previously have been unrealistic for a small practice.

The prototype slowly transformed into an environment for experimentation.

Rather than providing one definitive solution, BlackBox became a place where new ideas could be explored, connected and evaluated. Each component hinted at several more that could be developed in the future.

In retrospect, this may have been the project's most valuable outcome.

The software itself will continue to evolve, and individual technologies will inevitably be replaced. The more enduring contribution was the realisation that AI is not a single application to be adopted, but a growing ecosystem of possibilities that architects can actively shape through experimentation.

That shift in perspective became one of the most important observations of the entire project.