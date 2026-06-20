# BlackBox User Guide

Primary staff guide for accessing and using the current BlackBox system.

# What is BlackBox?

[![Homescreen.png](http://192.168.36.27:6875/uploads/images/gallery/2026-05/scaled-1680-/homescreen.png)](http://192.168.36.27:6875/uploads/images/gallery/2026-05/homescreen.png)

BlackBox is an experimental digital workspace developed specifically for Mossessian Architecture.

Inspired by Michel Mossessian's design philosophy, BlackBox explores how artificial intelligence, visual knowledge systems, and collaborative digital tools can support architectural research, creative exploration, and design ideation.

The project investigates how Large Language Models (LLMs), image archives, and office knowledge can be combined to help architects discover information, explore references, develop ideas, and navigate complex design challenges through both text and images.

BlackBox is not intended to replace architectural judgement, creativity, or design authorship. Instead, it aims to augment the design process by providing new ways to access knowledge, uncover connections, and support exploration.

At its core, BlackBox is an experiment in how digital tools can help architects think.

---

# A Tool for Exploration and Ideation

Architecture rarely follows a predictable path.

Projects emerge through research, discussion, sketching, modelling, testing, observation, and the gradual refinement of ideas. Designers constantly move between technical requirements, visual references, precedents, materials, narratives, and spatial concepts.

Much of this process is exploratory.

BlackBox has been created to support this way of working.

Rather than focusing solely on productivity or automation, BlackBox is designed as a platform for investigation, learning, and discovery. It provides tools that help architects search for information, explore visual references, organise knowledge, and develop ideas through conversation.

Using BlackBox, staff can:

* explore architectural topics through natural language
* discover precedents and design references
* search image collections and visual archives
* investigate materials, construction methods, and technologies
* access office documentation and shared knowledge
* organise and discuss ideas collaboratively
* combine text-based and image-based research workflows

The intention is not to provide definitive answers. Instead, BlackBox encourages exploration by helping users discover information, identify patterns, and uncover connections that may influence the design process.

---

# Why the Name "BlackBox"?

The name **BlackBox** is directly inspired by Michel Mossessian's design philosophy.

In architecture, the relationship between information and design is rarely straightforward. A project brief, a site visit, a conversation, a sketch, a precedent image, or a technical constraint can all contribute to the development of an idea. Yet the process by which these inputs become architecture is often difficult to explain.

Design thinking does not operate as a simple sequence of steps.

It involves intuition, experimentation, reflection, discussion, testing, and discovery. The internal process through which information is transformed into architectural ideas can often appear as a "black box" — a space where ideas emerge through exploration rather than through a fixed formula.

BlackBox seeks to bring aspects of this exploratory process into a digital environment.

Rather than treating artificial intelligence as a tool for generating immediate answers, the platform explores how AI can support curiosity, investigation, and creative thinking. It aims to help architects navigate large amounts of information, discover relevant references, and develop new lines of enquiry during the design process.

In this sense, BlackBox is not simply an AI platform.

It is an experiment in how large language models, visual archives, office knowledge, and collaborative tools can be combined to support the way architects research, think, and create.

The ambition is not to automate design.

The ambition is to build a digital environment that reflects and supports the exploratory culture of Mossessian Architecture.

---

# The BlackBox Platform

BlackBox consists of several connected applications, each serving a different role within the wider system.

## OpenWebUI

OpenWebUI provides access to AI assistants and research tools.

It can be used to:

* explore design ideas
* conduct research
* ask architectural and technical questions
* analyse documents
* search connected knowledge sources
* investigate precedents and references

The goal is to create a conversational interface to knowledge, allowing information to be explored through natural language rather than traditional search alone.

---

## PhotoPrism

PhotoPrism is the visual knowledge archive.

It stores and organises:

* precedent images
* project photography
* reference material
* visual research collections

As BlackBox develops, PhotoPrism will become an increasingly important source of visual knowledge that can be searched through both conventional and AI-assisted methods.

---

## BookStack

BookStack is the documentation and knowledge platform.

It contains:

* office guides
* workflows
* software instructions
* technical notes
* project knowledge
* internal documentation

BookStack serves as the primary repository for structured information within BlackBox.

---

## BlackBox Canvas

BlackBox Canvas is a collaborative digital whiteboard.

It provides a shared space for:

* brainstorming
* workshops
* design discussions
* concept development
* visual organisation of ideas

Multiple users can work together in real time, making it a useful tool for collaborative exploration and design thinking.

---

## Heimdall

Heimdall acts as the main entry point into the BlackBox ecosystem.

From Heimdall, users can access all available BlackBox applications through a single dashboard.

---

# What You Can Do Today

Today, BlackBox allows staff to:

* access all applications through Heimdall
* use AI assistants within OpenWebUI
* search and retrieve visual references from the image archive
* access office documentation and guides
* collaborate on shared canvases across the office network
* experiment with AI-assisted research and ideation workflows

While the platform is already useful for research and knowledge discovery, many capabilities are still being actively developed.

---

# An Ongoing Experiment

BlackBox should currently be viewed as a research and development initiative.

The platform is continuously evolving as new technologies, workflows, and ideas are tested. Some features are experimental and may change over time as we learn more about how AI and digital knowledge systems can support architectural practice.

The project relies on participation, feedback, and experimentation from across the practice.

Its success will not be defined solely by technology, but by its ability to support curiosity, knowledge sharing, creative exploration, and the development of architectural ideas.

BlackBox is ultimately an exploration into how digital tools can help architects think, learn, and design more effectively.

# How to access BlackBox

# How to access BlackBox

BlackBox works best when you start from Heimdall and use OpenWebUI as the main working interface.

## Main links

1. Heimdall: [http://192.168.36.27:8080](http://192.168.36.27:8080)
2. OpenWebUI: [http://192.168.36.27:3000](http://192.168.36.27:3000)
3. BlackBox Canvas: [http://192.168.36.27:8787](http://192.168.36.27:8787)
4. BookStack: [http://192.168.36.27:6875](http://192.168.36.27:6875)
5. PhotoPrism: [https://192.168.36.27:2342](https://192.168.36.27:2342)
6. ZITADEL sign-in: [https://auth.local:8443](https://auth.local:8443)

## Login model

- Heimdall is the launcher only and has no login.
- OpenWebUI currently uses its own login/access model.
- BookStack uses ZITADEL login.
- PhotoPrism uses ZITADEL login and approved users must be provisioned correctly.
- BlackBox Canvas is anonymous multiplayer and does not use ZITADEL yet.

## LAN note

BookStack and PhotoPrism open on the LAN IP, but their sign-in still redirects to `https://auth.local:8443`. That means a new client machine must resolve `auth.local` to `192.168.36.27`.

# Ollama and Large Language Models (LLMs)

## What is Ollama?

Ollama is the software that allows BlackBox to run Artificial Intelligence models locally on the office server.

Think of Ollama as a runtime or hosting framework for Large Language Models (LLMs). It is responsible for loading AI models into memory, managing their execution, and making them available to applications such as OpenWebUI.

Without Ollama, the AI models themselves cannot run.

In the BlackBox ecosystem, Ollama acts as the layer between the AI models and the applications that use them.

---

## Why Do We Use Ollama?

One of the key principles behind BlackBox is flexibility.

The tools built on top of BlackBox should not depend on a single AI model or a specific AI provider.

Instead, the underlying model can be changed as requirements evolve.

This means that:

- new models can be tested easily
- better models can be adopted when they become available
- specialised models can be used for specific tasks
- the system remains independent from any single vendor

Applications such as OpenWebUI communicate with Ollama rather than directly with a particular model.

As a result, changing the AI model usually requires little or no change to the user-facing tools.

---

## Local Models and Cloud Models

Large Language Models can be run in two different ways.

### Local Models

A model is downloaded and runs directly on the BlackBox server.

Advantages:

- data remains inside the office network
- no usage fees
- greater privacy
- works without relying on external AI providers

Disadvantages:

- limited by available hardware
- generally slower than large cloud-based systems
- may not match the capabilities of the most advanced commercial models

---

### Cloud Models

A model runs on servers operated by an external provider.

Examples include:

- OpenAI
- Anthropic
- Google
- Mistral AI

Advantages:

- access to very large and capable models
- frequent updates
- high performance

Disadvantages:

- usage costs
- information is sent outside the local environment
- dependence on third-party services

---

## BlackBox Is Model-Agnostic

An important design principle of BlackBox is that the platform should not depend on any specific Large Language Model.

The tools and workflows are designed so that the underlying AI engine can be replaced when necessary.

For example, OpenWebUI can be connected to:

- local Ollama models
- OpenAI models
- Anthropic Claude models
- Google Gemini models
- future AI systems that may become available

This means the long-term value of BlackBox comes from its workflows, integrations, and knowledge systems rather than from any single AI model.

As AI technology evolves, the underlying models can evolve with it.

---

## How Ollama Runs

Ollama runs as a background service on the BlackBox Mac Studio.

It can also be accessed directly through the macOS Terminal.

For example, opening a Terminal window and entering:

```bash
ollama list

```

displays all models currently installed on the system.

Example:

```bash
NAME
gemma3:4b
qwen3:30b
glm-4
llama3.1:8b
llama3.1:70b
mistral
phi3
gpt-oss:20b

```

Each model has different strengths, capabilities, and hardware requirements.

Some are optimised for speed, others for reasoning, coding, knowledge retrieval, or general conversation.

---

## Common Models Used in BlackBox

### Llama

Developed by Meta.

Llama is one of the most widely used open-source model families and forms the basis for many other AI systems.

Strengths:

- strong general-purpose performance
- large ecosystem
- good reasoning abilities
- widely supported

Common versions:

- Llama 3.1 8B
- Llama 3.1 70B

---

### Qwen

Developed by Alibaba.

Qwen has become one of the strongest open-weight model families and often performs exceptionally well on reasoning and technical tasks.

Strengths:

- excellent reasoning
- strong coding capabilities
- good instruction following
- highly competitive with commercial models

Example:

- Qwen3 30B

---

### Gemma

Developed by Google.

Gemma is designed to provide strong performance while remaining efficient enough to run on modest hardware.

Strengths:

- lightweight
- fast
- efficient
- suitable for everyday tasks

Example:

- Gemma 3 4B

---

### Mistral

Developed by Mistral AI.

Mistral models are known for efficiency and strong overall performance.

Strengths:

- fast responses
- good general knowledge
- efficient resource usage

---

### Phi

Developed by Microsoft.

Phi models are compact models designed for efficiency and reasoning.

Strengths:

- small footprint
- good reasoning relative to size
- fast execution

Example:

- Phi-3

---

### GPT-OSS

An open-weight model family inspired by GPT-style architectures.

Strengths:

- strong conversational abilities
- good instruction following
- suitable for experimentation

---

## Commercial Models

BlackBox is not limited to local models.

If required, the platform can also connect to commercial AI providers.

### OpenAI

Examples:

- GPT-5
- GPT-4o

Strengths:

- state-of-the-art reasoning
- strong language understanding
- broad capabilities

---

### Anthropic Claude

Examples:

- Claude Sonnet
- Claude Opus

Strengths:

- excellent writing quality
- long-context understanding
- strong document analysis

---

### Google Gemini

Examples:

- Gemini Pro
- Gemini Ultra

Strengths:

- multimodal capabilities
- integration with Google's AI ecosystem

---

## Looking Ahead

The AI industry is evolving rapidly.

New models appear regularly, and today's leading model may not remain the strongest option tomorrow.

For this reason, BlackBox has been designed around a flexible architecture where models can be replaced, upgraded, or combined as needed.

The objective is not to commit to a particular AI model.

The objective is to build a platform that can take advantage of the best available models—whether they run locally on the BlackBox server or in the cloud—while continuing to support the research, exploration, and design workflows of Mossessian Architecture.

# First-time onboarding guide

# First-time onboarding guide

## Step 1: Connect to the office network

Make sure you are on the same office LAN as the BlackBox host.

## Step 2: Open Heimdall

Go to [http://192.168.36.27:8080](http://192.168.36.27:8080).

## Step 3: Open OpenWebUI

Open [http://192.168.36.27:3000](http://192.168.36.27:3000). This is the main user interface for BlackBox.

## Step 4: Try the PhotoPrism Assistant

Start with simple prompts such as:

1. `show me facade images`
2. `show me latest images`
3. `find timber interiors`
4. `show me tension images`

Each result row shows a thumbnail, an **Open** link, and a **Download** link.

## Step 5: Open BookStack

Open [http://192.168.36.27:6875](http://192.168.36.27:6875) for guides and reference notes.

## Step 6: Open BlackBox Canvas

Open [http://192.168.36.27:8787](http://192.168.36.27:8787) to use the shared board.

## Step 7: Sign in through ZITADEL when redirected

BookStack and PhotoPrism use ZITADEL. If you are redirected, sign in with your approved BlackBox account.

## Step 8: If something fails

- if `auth.local` does not load, see **Troubleshooting**
- if you see a certificate warning, your machine may not trust the BlackBox local certificate yet
- if PhotoPrism opens but the library looks empty, contact the admin instead of trying to self-register again

# LAN onboarding

# LAN onboarding

Use these steps when setting up a new office laptop or desktop for BlackBox.

## Step by step

1. Connect the machine to the office LAN.
2. Open Heimdall at [http://192.168.36.27:8080](http://192.168.36.27:8080).
3. If BookStack or PhotoPrism sign-in is needed, make sure `auth.local` resolves to `192.168.36.27`.
4. On Windows, run the BlackBox onboarding helper from an elevated Command Prompt or PowerShell window.
5. After setup, test BookStack, PhotoPrism, and the direct ZITADEL page.

## Why auth.local exists

ZITADEL still uses `https://auth.local:8443` as the shared sign-in address. BookStack and PhotoPrism both redirect there during login, so this hostname must work on each client machine.

## Certificate note

The BlackBox local CA signs the internal HTTPS certificates used by ZITADEL and PhotoPrism. If the browser shows a certificate warning, the hostname is usually still correct, but the client machine does not yet trust the local CA.

# Windows setup

# Windows setup

This is the easiest current setup path for a Windows office machine.

<span style="color:rgb(224,62,45);">\[edit: explain why it is nessesary\]</span>

## Run the helper

<span style="color:rgb(224,62,45);">\[edit: explain where the script is saved\]</span>

<span style="color:rgb(224,62,45);">\[edit: explain to copy the script onto the windows machine\]</span>

1. Open Command Prompt or PowerShell as Administrator. \[explain how to do it\]
2. Go to the BlackBox repo copy or shared script location. \[explain how to change directory\]
3. Run:<span style="color:rgb(224,62,45);"> \[edit: explain to run python script on local cmd in admin mode, you would type something like "python windows\_auth\_local\_onboarding.py\]</span>

```
python scripts/client-onboarding/windows_auth_local_onboarding.py
```

## What the script does

- checks for administrator privileges
- adds `192.168.36.27 auth.local` to the Windows hosts file
- avoids duplicate entries
- flushes the DNS cache unless told not to

## Validate afterward

1. Open Heimdall: [http://192.168.36.27:8080](http://192.168.36.27:8080)
2. Open OpenWebUI: [http://192.168.36.27:3000](http://192.168.36.27:3000)
3. Open BookStack: [http://192.168.36.27:6875](http://192.168.36.27:6875)
4. Open PhotoPrism: [https://192.168.36.27:2342](https://192.168.36.27:2342)
5. Open ZITADEL directly: [https://auth.local:8443](https://auth.local:8443)

# How to create new users

# How to create new users

This page is for the BlackBox admin.

Use this process when a new approved staff member needs access.

## Information you need first

1. email address
2. first name
3. last name
4. initial password

## Where to run the script

Repo root:

`/Users/blackbox/blackbox-core`

Script:

`scripts/provision_user.py`

## Step 1: Open a terminal on the BlackBox host

Go to the repo root:

```bash
cd /Users/blackbox/blackbox-core
```

## Step 2: Run the provisioning command

```bash
python3 scripts/provision_user.py \
  --email new.user@example.com \
  --first-name New \
  --last-name User \
  --password 'Replace-Me-2026!'
```

## Step 3: What the script does

The script will:

- create or reuse the ZITADEL human user
- verify and activate that user for the current local setup
- create or align the matching PhotoPrism OIDC user
- print the final access details and caveats

## Step 4: What to send to the user

Give them:

1. their email address
2. their initial password
3. Heimdall: [http://192.168.36.27:8080](http://192.168.36.27:8080)
4. OpenWebUI: [http://192.168.36.27:3000](http://192.168.36.27:3000)
5. BookStack: [http://192.168.36.27:6875](http://192.168.36.27:6875)
6. Canvas: [http://192.168.36.27:8787](http://192.168.36.27:8787)

## Step 5: Remaining manual first-login steps

Tell the user that:

- BookStack and PhotoPrism sign-in use ZITADEL
- the first sign-in may show the ZITADEL MFA setup or skip screen
- some machines need `auth.local` to resolve to `192.168.36.27`
- some machines may show certificate warnings until the BlackBox local certificate is trusted

## Step 6: Avoid duplicate accounts

- rerun the script before creating anything manually
- avoid creating multiple user accounts for one person with different email addresses unless there is a real reason
- if PhotoPrism looks empty after login, check the existing account instead of creating another one

## Current caveat

This is an admin-only workflow, not self-service signup.

Approved users are currently provisioned with the practical PhotoPrism admin-access model because the current PhotoPrism edition does not yet provide a reliable automated standard-user path without guest-only access issues.

# Using OpenWebUI

# Using OpenWebUI

Open OpenWebUI at [http://192.168.36.27:3000](http://192.168.36.27:3000).

## What it is for

OpenWebUI is the main AI interface for BlackBox.

Use it to:

- search the image archive
- review examples and precedents
- open or download images returned by the system
- ask basic usage questions about the BlackBox tools

## Good search prompts

- `show me facade images`
- `show me latest images`
- `find concrete references`
- `show me timber interiors`
- `show me latest facade images`

## What the result table means

Each result row shows:

- a thumbnail preview
- the image name
- an **Open** link to PhotoPrism
- a **Download** link

## Important behavior note

The PhotoPrism Assistant is intentionally in strict renderer mode.

That means:

- if results exist, it should show only the result table
- if no results exist, it should show only a simple no-results message
- it should not add commentary around valid tool output

## Known limitations

- search is deterministic metadata retrieval, not semantic AI search yet
- very abstract words may still return no results
- OpenWebUI itself does not currently use ZITADEL sign-in

# Using BlackBox Canvas

# Using BlackBox Canvas

Open Canvas at [http://192.168.36.27:8787](http://192.168.36.27:8787).

## How to share a board

1. Open the board URL
2. Share the same board link with a colleague
3. Work on the same board at the same time

## What anonymous multiplayer means

Canvas is currently shared live over the LAN, but it does not yet use individual user accounts.

If you see `2 collaborators`, that means two live browser sessions are connected to the same board.

## Current limitations

- no named account ownership yet
- no ZITADEL login yet
- collaborator names are temporary session labels rather than office identities

# Using PhotoPrism

# Using PhotoPrism

PhotoPrism is mainly the backend image library for BlackBox.

Direct URL: [https://192.168.36.27:2342](https://192.168.36.27:2342)

## What staff should know

- most people should start in OpenWebUI, not in PhotoPrism directly
- direct PhotoPrism access is mainly for approved users who need to browse the library itself
- PhotoPrism sign-in uses ZITADEL
- PhotoPrism now generates captions and labels automatically through Ollama
- the current AI model for both captions and labels is `gemma3:4b` through Ollama
- staff can still manually correct titles, keywords, and other standard metadata fields in the PhotoPrism interface

## Access note

If you can sign in but do not see the expected library, contact the BlackBox admin. User provisioning is controlled centrally to avoid guest or empty-library access problems.

## More detail

For the current AI and search architecture, including the exact caption and label rules, see **PhotoPrism AI &amp; Search System** in this guide.

# PhotoPrism AI & Search System

## What this system does today

The current PhotoPrism search stack supports metadata search, natural-language retrieval through OpenWebUI, keyword matching, caption matching where captions exist, deterministic query expansion for a small set of architectural terms, and thumbnail plus open/download links.

This is **not** embeddings-based semantic search yet.

## Architecture

- PhotoPrism stores the image library.
- PhotoPrism itself can generate AI captions and AI labels for images.
- OpenWebUI does **not** search PhotoPrism directly.
- The PhotoPrism bridge sits between OpenWebUI and PhotoPrism and handles retrieval.

The bridge currently normalizes queries, parses temporal requests such as `latest`, `recent`, `today`, and `this month`, expands a small deterministic synonym dictionary, searches attached metadata deterministically, builds the markdown result table used in OpenWebUI, and proxies thumbnails while returning open/download links.

Relevant code paths:

- `services/photoprism-bridge/server.py`
- `services/photoprism-bridge/query_expansions.py`

## What metadata currently drives retrieval

Search currently depends mainly on attached metadata such as:

- title
- filename
- keywords
- captions
- labels
- location text
- selected metadata fields such as color or camera text

## How the AI caption model works

PhotoPrism currently uses the local Ollama model `gemma3:4b` for caption generation. In the current setup the caption model runs in **auto** mode, so when PhotoPrism processes an image it can generate a caption automatically.

The active caption prompt is deliberately strict. It tells the model to:

- create **one factual sentence**
- begin with the primary building, space, or object
- describe the main architectural subject
- include visible materials
- include spatial condition when clearly visible
- include lighting when clearly visible
- use plain descriptive language
- avoid speculation
- avoid design interpretation
- avoid meta-language and filler words

In other words, the caption model is meant to produce short descriptive text for retrieval, not a design critique and not a conversational explanation.

## How the AI label model works

PhotoPrism also uses the local Ollama model `gemma3:4b` for label generation. The label model also runs in **auto** mode.

The active label prompt is more structured than the caption prompt. It tells the model to:

- return a simple machine-readable list of label entries
- for each label, include the label name plus two internal score fields used by PhotoPrism
- return **at most 5 labels**
- prefer architectural nouns, materials, spatial elements, and site terms
- use single-word nouns in canonical singular form
- prefer visible terms such as `facade`, `window`, `concrete`, `timber`, `stair`, `corridor`, `column`, `roof`, `street`, `plaza`, or `interior` when appropriate
- avoid repeating the same label twice
- avoid extra fields or extra explanatory text

This makes the labels easier to store, inspect, and use in deterministic search.

## What is done by AI and what can be set manually

**Done automatically by AI in the current setup:**

- captions
- labels

**What staff or admins can set or correct manually in PhotoPrism:**

- title
- keywords
- other standard metadata edits available in the PhotoPrism interface

The practical rule is simple: AI creates the first-pass captions and labels, while people should correct or strengthen search quality manually through titles, keywords, and normal metadata editing when needed.

Search uses both AI-generated metadata and manually maintained metadata.

## Indexing and processing

Current indexing behavior:

- import path: `/photoprism/import`
- auto import: disabled
- auto index: every 300 seconds
- index schedule: no separate cron schedule configured

Practical meaning:

- new files must be placed into the library/import workflow intentionally
- once indexed, metadata becomes searchable on the next automatic index cycle
- AI caption and label generation now run automatically as part of the configured vision pipeline
- existing files can also be regenerated with a manual vision run when needed

## Current limitations

- retrieval is metadata-based only
- embeddings are not implemented yet
- caption quality depends on the source image and the AI output quality
- some searches still depend heavily on metadata quality
- `auth.local` and certificate trust still matter for some sign-in flows
- the OpenWebUI PhotoPrism Assistant intentionally behaves as a strict renderer, not a conversational explainer

## Short glossary

- **Caption:** the short sentence the AI writes to describe what is visible in the image.
- **Label:** a short keyword the AI adds, such as `facade`, `concrete`, or `stair`.
- **Machine-readable list:** a structured format that PhotoPrism can store and process reliably without extra prose around it.
- **Confidence:** PhotoPrism's internal score for how strongly the model believes a label is present.
- **Topicality:** PhotoPrism's internal score for how central that label is to the image rather than just a minor detail.
- **Deterministic search:** a search process that follows fixed matching rules instead of inventing or guessing results.

## Future direction

Planned future work may include embeddings, semantic retrieval, deeper AI-assisted tagging, deeper Canvas integration, and more unified authentication across apps.

# Using BookStack

# Using BookStack

BookStack is the central documentation platform for the BlackBox system.

It is used to organise and maintain:

* staff guides
* onboarding instructions
* technical setup notes
* workflow documentation
* office standards
* archived project information

The purpose of the system is to create a shared and searchable office knowledge base that can grow over time.

---

# How Documentation is Organised

BookStack uses a simple hierarchy:

## Books

Large topics or systems.

Examples:

* BlackBox User Guide
* IT & Infrastructure
* BIM Standards
* AI Workflows

## Chapters

Sections within a book used to group related topics.

Examples:

* Onboarding
* User Management
* AI Systems
* Maintenance

## Pages

Individual documents or instructions.

Examples:

* How to Access BlackBox
* Installing Rhino Plugins
* PhotoPrism Search Guide

---

# Recommended Starting Points

New users should begin with the following pages:

1. **How to Access BlackBox**
   System URLs, login methods, and basic overview.

2. **First-Time Onboarding Guide**
   Device setup and initial configuration.

3. **How to Create New Users**
   User accounts, permissions, and roles.

4. **PhotoPrism AI & Search System**
   AI-assisted image search and tagging workflows.

---

# Multi-User Setup

BookStack is configured as a shared multi-user documentation system.

Each staff member receives their own account and login credentials.

## Authentication

Authentication is handled through the BlackBox single sign-on system using OpenID Connect (OIDC).

This means:

* users log in with a shared office identity system
* passwords are not managed directly inside BookStack
* user access can be centrally controlled
* permissions remain consistent across connected applications

---

# User Roles

Depending on permissions, users may be able to:

* read documentation
* create pages
* edit pages
* upload files and images
* manage books and chapters
* administer users and permissions

Typical roles include:

| Role   | Permissions                |
| ------ | -------------------------- |
| Viewer | Read-only access           |
| Editor | Create and edit content    |
| Admin  | Full system administration |

---

# Editing Documentation

BookStack supports collaborative editing, but pages are not edited in true real-time like Google Docs.

## Important

* only one user should actively edit a page at a time
* simultaneous edits may overwrite changes
* save regularly during editing
* larger edits are best coordinated between team members

For collaborative drafting, it is recommended to:

* split content into smaller pages
* use clear page ownership where possible
* avoid multiple people editing the same paragraph simultaneously

---

# Markdown Syntax Guide

BookStack supports Markdown formatting.

Markdown is a lightweight writing syntax used to structure documents quickly and clearly.

---

# Headings

Use `#` symbols for headings.

```md
# Main Heading
## Sub Heading
### Smaller Heading
```

Example:

# Main Heading

## Sub Heading

### Smaller Heading

---

# Bold and Italic Text

```md
**Bold text**

*Italic text*
```

Example:

**Bold text**
*Italic text*

---

# Lists

## Bullet Lists

```md
- Item One
- Item Two
- Item Three
```

## Numbered Lists

```md
1. First Item
2. Second Item
3. Third Item
```

---

# Links

```md
[OpenAI](https://openai.com)
```

---

# Images

```md
![Description](image.png)
```

Images can also be uploaded directly through the BookStack editor.

---

# Code Blocks

Use triple backticks for code blocks.

````md
```python
print("Hello World")
```
````

Example:

```python
print("Hello World")
```

---

# Tables

```md
| Name | Role |
|---|---|
| Anna | Admin |
| Mark | Editor |
```

Example:

| Name | Role   |
| ---- | ------ |
| Anna | Admin  |
| Mark | Editor |

---

# Tips for Writing Good Documentation

Good documentation should be:

* clear
* short
* structured
* searchable
* easy to maintain

## Recommended Practices

* use descriptive page titles
* keep sections short
* add screenshots where useful
* avoid duplicate pages
* update outdated information
* explain technical terms when needed

The goal is to allow another team member to complete a task independently using the documentation alone.

---

# General Principles

The BlackBox documentation system is intended to become a long-term internal knowledge base.

Documentation should prioritise:

* clarity over complexity
* practical information over theory
* maintainability over excessive detail
* consistency across all pages

Well-structured documentation reduces onboarding time, improves continuity between projects, and helps preserve office knowledge over time.

# Troubleshooting

# Troubleshooting

## Login problems

- If BookStack or PhotoPrism redirects to `https://auth.local:8443` and the page does not load, the client machine probably does not resolve `auth.local` yet.
- Required hosts-file line: `192.168.36.27 auth.local`
- On Windows, use the onboarding helper instead of editing the file manually if possible.

## Certificate warning

- The warning usually means the machine does not trust the BlackBox local CA yet.
- For internal alpha testing, confirm the URL is correct before proceeding.

## Empty PhotoPrism library

- If PhotoPrism login works but the library looks empty, the user account may not have been provisioned correctly yet.
- Ask an admin to re-check the approved-user provisioning flow.

## Canvas not syncing

- Make sure both people are on the same board URL.
- Refresh both sessions if collaborator count looks wrong.

# Current limitations

# Current limitations

The system is usable today, but a few limits still matter:

1. not all apps use ZITADEL yet
2. BlackBox Canvas is anonymous for now
3. some HTTPS or certificate warnings may still appear on some machines
4. PhotoPrism user roles are constrained by the current PhotoPrism edition
5. some apps still depend on the special login hostname `auth.local`
6. PhotoPrism retrieval is still metadata-based, not embeddings-based
7. the PhotoPrism assistant intentionally behaves as a renderer rather than a conversational search explainer

These limits are known and already tracked in the BlackBox roadmap.