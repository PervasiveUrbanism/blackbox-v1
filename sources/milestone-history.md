# BlackBox Milestone History

Last updated: 2026-06-15

## Purpose

This file is the compact chronological record of the main BlackBox milestones completed so far.
It is intended as a readable history of what was done, why it was done, and what the practical outcome was.

## Milestone 4 - PhotoPrism OIDC Integration

- Goal:
  connect PhotoPrism to ZITADEL for shared login
- Main outcome:
  PhotoPrism authentication was moved onto the shared OIDC path
- Practical result:
  PhotoPrism can use ZITADEL-based sign-in instead of remaining fully isolated

## Milestone 5 - Direct Ollama Tagging and Captioning in PhotoPrism

- Goal:
  enable direct AI-generated captions and labels inside PhotoPrism
- Main outcome:
  PhotoPrism was configured to use Ollama vision models for captions and labels
- Practical result:
  the image library gained AI-generated metadata that could later support search
- Later refinement:
  the active model settled on `gemma3:4b`, with architecture-focused prompts for both captions and labels

## Milestone 6 - OpenWebUI PhotoPrism Query Interpreter

- Goal:
  make OpenWebUI capable of turning natural image-search requests into structured PhotoPrism queries
- Main outcome:
  an OpenWebUI-side query-interpreter path was introduced for PhotoPrism searches
- Practical result:
  OpenWebUI became a usable front end for archive search instead of requiring direct PhotoPrism use

## Milestone 7 - PhotoPrism Bridge Validation

- Goal:
  reconnect and stabilise the PhotoPrism bridge so structured search requests return real results predictably
- Main outcome:
  deterministic bridge behavior was validated against live PhotoPrism data
- Practical result:
  the bridge became the stable retrieval layer between OpenWebUI and PhotoPrism

## Milestone 7.5 - PhotoPrism Public URL Alignment

- Goal:
  align bridge output links with the actual LAN access model
- Main outcome:
  returned PhotoPrism links were changed to the LAN-facing public URL model
- Practical result:
  result links became usable for real users instead of pointing to stale or machine-specific addresses

## Milestone 8 - tldraw Multiplayer Over LAN

- Goal:
  make BlackBox Canvas work as a true shared whiteboard over LAN
- Main outcome:
  multiplayer session handling was fixed so live sessions no longer collapsed into each other
- Practical result:
  multiple people could join the same board and see synchronized edits

## Milestone 8.1 - Consolidate BlackBox Canvas Into Main Repo

- Goal:
  bring the working Canvas service into the main repo so it became reproducible
- Main outcome:
  the service was integrated into `services/blackbox-canvas`
- Practical result:
  the canvas runtime could be rebuilt from the repo instead of depending on an external sibling project

## Milestone 8.2 - Canvas Identity Investigation and Project Maintenance

- Goal:
  clarify what Canvas multiplayer means and establish better in-repo project tracking
- Main outcome:
  Canvas was documented as anonymous multiplayer rather than authenticated collaboration
- Practical result:
  missing visible login identity was confirmed as expected behavior, not a bug
- Additional outcome:
  repo-side project tracking and maintenance expectations were introduced

## Milestone 9.0 - Archive Previous Work and Establish Project Documentation

- Goal:
  formalize prior milestones and create a stable project documentation structure in the repo
- Main outcome:
  the `docs/project/` structure became the canonical project-tracking location
- Practical result:
  roadmap, completed work, current state, and next steps gained a clear home in the repo

## Milestone 9.1 - Canvas Investigation and Documentation

- Goal:
  inspect and document the real behavior of the Canvas service
- Main outcome:
  the service was documented as anonymous session-based multiplayer with lightweight presence
- Practical result:
  the team now has a clear explanation of what Canvas does and does not provide

## Milestone 9.2 - OpenWebUI Result UX

- Goal:
  make PhotoPrism search results usable inside OpenWebUI
- Main outcome:
  result output was changed from raw JSON/plain text into a compact markdown table with thumbnails and links
- Practical result:
  users could browse image results inside OpenWebUI without needing to interpret API output

## Milestone 9.3 - OpenWebUI Delivery Fixes

- Goal:
  make the search experience faster and more reliable
- Main outcome:
  the PhotoPrism assistant model was switched to a faster local model and thumbnail delivery was stabilized
- Practical result:
  search became faster, thumbnail rendering improved, and result links became more consistent

### Milestone 9.3D - Search-Field Coverage Audit and Retrieval Fix

- Goal:
  confirm which metadata fields were actually being searched and widen coverage where needed
- Main outcome:
  retrieval was broadened across attached metadata such as title, filename, caption, keywords, labels, location, and selected metadata fields
- Practical result:
  search became more deterministic and explainable

### Milestone 9.3E - Natural-Language Query Normalization Fix

- Goal:
  stop natural-language filler phrasing from degrading search terms
- Main outcome:
  common image-search filler phrases were stripped and simple singular/plural normalization was added
- Practical result:
  queries like `show me images with facade` resolved more reliably to the useful search term

### Milestone 9.3F - Bridge Retrieval Fix for Attached Metadata

- Goal:
  ensure direct bridge queries truly search attached metadata instead of relying on too-narrow candidate behavior
- Main outcome:
  direct bridge keyword retrieval was fixed to fetch and match richer PhotoPrism detail payloads
- Practical result:
  direct bridge queries and OpenWebUI queries began agreeing more consistently on real metadata hits

## Milestone 9.4 - Controlled Query Expansion

- Goal:
  improve recall with a small deterministic synonym layer without moving into embeddings or semantic search
- Main outcome:
  a controlled expansion dictionary was added and later moved into `services/photoprism-bridge/query_expansions.py`
- Practical result:
  near-equivalent architectural terms such as `elevation` and `facade` began matching more reliably

## Milestone 9.5 - LAN Access Unification

- Goal:
  make the core services understandable and usable across the LAN
- Main outcome:
  the practical access model was clarified around `192.168.36.27`, with `auth.local` retained as the one auth hostname exception
- Practical result:
  Heimdall, OpenWebUI, Canvas, BookStack, and PhotoPrism gained a clearer LAN-safe usage pattern

## Milestone 9.6 - User Provisioning Automation

- Goal:
  automate onboarding of approved users
- Main outcome:
  `scripts/provision_user.py` was added to create or align users across ZITADEL and PhotoPrism
- Practical result:
  onboarding became scriptable and more repeatable, while avoiding accidental guest-only PhotoPrism access

## Milestone 9.6B - User Documentation Consolidation in BookStack

- Goal:
  consolidate user-facing documentation into one clear guide
- Main outcome:
  `BlackBox User Guide` became the primary staff-facing BookStack book
- Practical result:
  access notes, onboarding, OpenWebUI, Canvas, PhotoPrism, troubleshooting, and limitations were centralized for staff

## Milestone 9.7 - OpenWebUI as the Primary Interface

- Goal:
  make OpenWebUI feel like the main way users interact with BlackBox
- Main outcome:
  runtime prompt and profile work positioned OpenWebUI as the primary interface, with PhotoPrism as backend infrastructure
- Practical result:
  users could treat OpenWebUI as the main search and interaction surface instead of hopping between tools

### Milestone 9.7A - OpenWebUI Strict Renderer Mode

- Goal:
  suppress conversational drift in the PhotoPrism assistant
- Main outcome:
  the assistant was tightened into a strict renderer for tool-backed image results
- Practical result:
  result tables became more stable, with less commentary, contradiction, or reasoning leakage

### Milestone 9.7B - Temporal Retrieval, Onboarding Completion, and Heimdall Branding

- Goal:
  add recency-aware retrieval and complete key user-facing documentation and polish
- Main outcome:
  deterministic temporal query handling was added, onboarding docs were expanded, and Heimdall branding was improved
- Practical result:
  queries like `latest images` became supported, and the platform became more ready for internal alpha use

### Milestone 9.7C - BookStack LAN Access

- Goal:
  verify and stabilize BookStack LAN access
- Main outcome:
  BookStack itself was confirmed LAN-safe, while `auth.local` was documented as the remaining shared auth dependency
- Practical result:
  the actual LAN failure point became clearer and easier to troubleshoot

### Milestone 9.7D - LAN Client Onboarding and Local Network Access

- Goal:
  reduce friction for new client machines on the local network
- Main outcome:
  LAN onboarding guidance and a Windows helper for the `auth.local` hosts-file step were added
- Practical result:
  LAN alpha onboarding became more repeatable for non-host machines

## Additional Recent Platform Work

These items were practical follow-on improvements rather than separately archived numbered milestones:

- PhotoPrism AI caption and label generation was switched from manual runs to `auto`
- architecture-focused caption and label prompts were tuned and validated on representative images
- a full-library caption and label regeneration run was started against the existing archive
- the `BlackBox User Guide` PhotoPrism pages were refined to explain:
  - the active AI model
  - caption rules
  - label rules
  - what can still be set manually
- a new BookStack book, `Rhino & Revit`, was created with:
  - placeholder Rhino/Revit guide pages
  - a structured `Upcoming Revit Training` chapter
  - one page per Revit training day
  - supporting pages for teaching notes, pace options, and budget planning
- Heimdall branding was further revised to use the Mossessian logo and a more office-specific landing-page layout

## Not Yet Started

The following roadmap phases are still future work:

- Step 10 - AI in Canvas
- Step 11 - Embeddings and semantic search

## Related Files

- [completed.md](/Users/blackbox/blackbox-core/docs/project/completed.md)
- [roadmap.md](/Users/blackbox/blackbox-core/docs/project/roadmap.md)
- [current-state.md](/Users/blackbox/blackbox-core/docs/project/current-state.md)
- [next-steps.md](/Users/blackbox/blackbox-core/docs/project/next-steps.md)
- [blackbox-status.md](/Users/blackbox/blackbox-core/docs/blackbox-status.md)
