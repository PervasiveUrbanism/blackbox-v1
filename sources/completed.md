# Completed Milestones Archive

Last updated: 2026-04-23

## Milestone 7 - PhotoPrism Structured Bridge

### Goal

- reconnect and stabilise the PhotoPrism bridge so structured search requests return real results predictably

### What was implemented

- deterministic mapping from structured query fields into PhotoPrism search requests
- fallback chain for query construction
- bridge logging for original query, structured query, final PhotoPrism query, and result count
- runtime validation against live PhotoPrism data

### Key technical decisions

- keep the bridge simple and transparent
- avoid embeddings or semantic search at this stage
- use the existing PhotoPrism API rather than changing PhotoPrism itself

### Current status

- validated

### Known limitations

- result quality still depends on current PhotoPrism captions and labels
- the bridge is deterministic, but not semantic

## Milestone 7.5 - Public URL Alignment

### Goal

- align PhotoPrism result links with the actual LAN access model

### What was implemented

- updated the public result URL base used by the bridge
- validated that returned links use the LAN-facing address instead of the old machine-specific hostname

### Key technical decisions

- keep the bridge logic unchanged
- treat this as a URL consistency cleanup, not a routing redesign

### Current status

- validated

### Known limitations

- HTTPS trust behaviour for LAN clients is still constrained by the local certificate model

## Milestone 8 - Canvas Multiplayer Fix

### Goal

- make the tldraw-based BlackBox Canvas work as a real shared board over LAN

### What was implemented

- fixed room/session handling so live clients are tracked by connection identity instead of collapsing same-user sessions
- validated same-board collaboration across multiple sessions
- preserved the existing board UI and persistence model

### Key technical decisions

- keep the custom BlackBox Canvas service instead of replacing it
- repair multiplayer behaviour with minimal architectural change
- continue using snapshot-based sync over WebSockets

### Current status

- validated

### Known limitations

- multiplayer is real, but still based on a custom single-node sync service
- concurrent editing can still behave like last-write-wins at the document level

## Milestone 8.1 - Canvas Integration Into Repo

### Goal

- bring the working Canvas service under the main repo so the milestone becomes reproducible

### What was implemented

- integrated the BlackBox Canvas service into `services/blackbox-canvas`
- updated Compose to build and run the service from the repo
- aligned runtime paths and documentation with the repo-owned service

### Key technical decisions

- preserve the current implementation exactly rather than redesigning it
- keep port `8787` and the existing access pattern unchanged

### Current status

- validated

### Known limitations

- the service is reproducible from the repo, but it still uses a custom anonymous collaboration model rather than shared authenticated identity

## Milestone 9.6 - User Provisioning Automation

### Goal

- automate approved-user onboarding across ZITADEL and PhotoPrism so onboarding is repeatable and avoids guest-only PhotoPrism access

### What was implemented

- added [scripts/provision_user.py](/Users/blackbox/blackbox-core/scripts/provision_user.py) as the admin provisioning entrypoint
- the script creates or reuses a ZITADEL human user with a verified email and initial password
- the script creates or aligns the matching PhotoPrism OIDC user explicitly instead of relying on auto-registration

### Key technical decisions

- reuse the live ZITADEL bootstrap PAT and management API that already work in this stack
- keep PhotoPrism auto-registration disabled
- provision approved users as PhotoPrism `admin` accounts because the current PhotoPrism edition does not provide a reliable automated regular-user role path here

### Current status

- validated

### Known limitations

- first login still reaches the ZITADEL MFA setup prompt, so onboarding is not fully hands-off beyond account creation
- the current PhotoPrism access model is practical rather than ideal because it depends on the `admin` role for reliable library visibility

## Milestone 9.6B - User Documentation Consolidation In BookStack

### Goal

- consolidate the scattered staff-facing BlackBox documentation into one clear BookStack book

### What was implemented

- created `BlackBox User Guide` as the new primary BookStack book
- added staff-facing pages for access, onboarding, OpenWebUI, Canvas, PhotoPrism, BookStack, troubleshooting, and current limitations
- preserved the older BlackBox books by renaming them as archived instead of deleting them

### Key technical decisions

- keep the final guide simple and user-facing rather than technical
- preserve older source material safely as archived reference content
- leave unrelated BookStack content such as `competition playbook` alone

### Current status

- validated

### Known limitations

- the guide reflects the current live system, so it will need updating as authentication and app behavior change
- some legacy archived material is still useful background, but it is no longer the primary source for staff

## Milestone 9.7 - OpenWebUI As The Primary Interface

### Goal

- make OpenWebUI feel like the main BlackBox interface for AI help and image search rather than just another tool in the stack

### What was implemented

- updated the live OpenWebUI model metadata so the main `BlackBox` model describes OpenWebUI as the primary user-facing interface
- updated the live `PhotoPrism Assistant (llama3.1:8b)` system prompt to keep image-search behavior strict, tool-first, and table-oriented
- added domain-relevant starter prompts for both the main `BlackBox` model and the PhotoPrism assistant

### Key technical decisions

- keep this as a runtime UX and prompt step rather than a backend redesign
- preserve the existing bridge result format and search logic
- keep Heimdall as the launcher while steering users toward OpenWebUI for normal interaction

### Current status

- validated

### Known limitations

- the OpenWebUI behavior change currently lives in the runtime database rather than tracked app code
- direct PhotoPrism access is still needed for deeper browsing or account troubleshooting

## Milestone 9.7A - OpenWebUI Strict Renderer Mode

### Goal

- suppress conversational drift so the PhotoPrism assistant behaves like a deterministic renderer of bridge results

### What was implemented

- tightened the live PhotoPrism assistant prompt so tool-backed image queries return only the markdown table or the exact no-results line
- replaced generic starter prompts with architectural prompts that match the real archive workflow
- validated the tool-enabled OpenWebUI chat path to confirm commentary and reasoning leakage were suppressed

### Key technical decisions

- keep the assistant silent around valid tool output rather than trying to make it more conversational
- preserve renderer mode even when future retrieval features are added

### Current status

- validated

### Known limitations

- the prompt/runtime behavior still lives in OpenWebUI's live database rather than tracked application code

## Milestone 9.7B - Temporal Query Support And User Readiness

### Goal

- add deterministic recency-aware retrieval while finishing the staff-facing onboarding, PhotoPrism, and Heimdall polish needed for internal alpha use

### What was implemented

- added deterministic temporal parsing for `latest`, `recent`, `today`, `yesterday`, `this week`, `last week`, `this month`, and `last month`
- added quantity-aware recency requests such as `latest 4 images`
- made combined recency + keyword searches return newest-first results while preserving deterministic metadata matching
- extended the live `BlackBox User Guide` with clearer access, login, onboarding, troubleshooting, and PhotoPrism AI/search pages
- changed the live Heimdall browser tab title from `Heimdall` to `BlackBox`

### Key technical decisions

- keep recency support deterministic and metadata-based
- document the real PhotoPrism indexing and AI metadata behavior honestly instead of implying background automation that does not exist
- treat Heimdall branding as a live config concern rather than a major dashboard redesign

### Current status

- validated

### Known limitations

- recency is now date-aware, but retrieval is still metadata-based rather than embeddings-based
- Heimdall branding is currently controlled by the live bind-mounted config at `/Users/blackbox/heimdall-config/www/.env`
