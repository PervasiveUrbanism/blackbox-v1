# Current System State

Last updated: 2026-05-06

## Running Services

- ZITADEL
- Heimdall
- BookStack
- PhotoPrism
- PhotoPrism Bridge
- OpenWebUI
- BlackBox Canvas
- Memos
- Excalidraw
- Excalidraw Room

## Ports And Access Model

- Heimdall: `http://192.168.36.27:8080`
- OpenWebUI: `http://192.168.36.27:3000`
- Memos: `http://192.168.36.27:5230`
- Excalidraw: `http://192.168.36.27:5001`
- Excalidraw Room: `http://192.168.36.27:5002`
- BlackBox Canvas: `http://192.168.36.27:8787`
- ZITADEL: `https://auth.local:8443`
- BookStack: `http://192.168.36.27:6875`
- PhotoPrism: `https://192.168.36.27:2342`
- PhotoPrism Bridge: `http://127.0.0.1:8011`

Practical access model:

- LAN-ready without auth caveats: Heimdall, OpenWebUI, Memos, Excalidraw, BlackBox Canvas
- LAN-ready with auth caveat: BookStack, PhotoPrism
- auth exception: ZITADEL remains on `auth.local`
- BookStack itself now loads on the LAN URL and posts OIDC login with:
  - redirect target: `https://auth.local:8443`
  - callback URI: `http://192.168.36.27:6875/oidc/callback`

## Identity Model

- ZITADEL is the central identity provider
- BookStack uses ZITADEL via OIDC
- PhotoPrism uses ZITADEL via OIDC
- OpenWebUI is not yet integrated with ZITADEL
- BlackBox Canvas is currently anonymous multiplayer and does not use real auth

Important exceptions:

- PhotoPrism OIDC auto-registration is disabled to avoid accidental guest-only user creation
- approved-user provisioning is now handled by [scripts/provision_user.py](/Users/blackbox/blackbox-core/scripts/provision_user.py)
- the current practical PhotoPrism onboarding model provisions approved users as PhotoPrism `admin` accounts so they can reliably see the library
- first login still reaches the ZITADEL MFA setup prompt, so onboarding is automated up to the point of interactive first sign-in
- Canvas collaborator identity is local browser metadata, not authenticated user identity
- BookStack and PhotoPrism now use LAN IP public URLs, but their sign-in flow still depends on `auth.local`
- LAN clients that need BookStack or PhotoPrism sign-in should resolve `auth.local` to `192.168.36.27` and trust the BlackBox local CA to avoid certificate warnings
- the current Windows onboarding helper for that setup is [scripts/client-onboarding/windows_auth_local_onboarding.py](/Users/blackbox/blackbox-core/scripts/client-onboarding/windows_auth_local_onboarding.py)
- the BookStack guide now also covers:
  - access and login expectations
  - admin provisioning
  - first-login troubleshooting
  - PhotoPrism AI/search behavior
  - LAN client onboarding and Windows setup

## BookStack Documentation

- the primary staff-facing BookStack book is now `BlackBox User Guide`
- the onboarding guide lives in the page `First-time onboarding guide`
- older books were kept but marked as archived:
  - `Archived - BlackBook Doc`
  - `Archived - BlackBox Reference`
  - `Archived - BlackBox User Examples`
- `competition playbook` remains separate and was not changed by this consolidation

## Canvas (BlackBox Canvas / tldraw)

Access URLs:

- local: `http://127.0.0.1:8787`
- LAN: `http://192.168.36.27:8787`

Identity model:

- anonymous sessions only
- no ZITADEL integration
- no authenticated account model
- browser-local identity persisted in local storage as `blackbox-canvas-user`

How users are distinguished:

- frontend identity contains a generated `id`, `name`, and `color`
- backend presence uses a per-connection `connectionId`
- visible collaborator names are lightweight guest labels such as `Guest 101`

Multiplayer behaviour:

- two or more sessions can join the same board
- presence reflects multiple live collaborators
- edits sync in real time via WebSockets
- the previous same-session overwrite problem is resolved

What this does not include:

- accounts
- permissions
- ownership model
- authoritative user attribution

Step 9 decision:

- Canvas remains anonymous multiplayer for now
- no ZITADEL integration will be added in Step 9

## What Works

- shared authentication for BookStack and PhotoPrism
- PhotoPrism bridge and structured search
- bridge-side deterministic retrieval across title, filename, captions, keywords, labels, location text, and selected metadata
- bridge-side term normalization now also handles a small set of architectural near-equivalents more consistently during metadata matching
- natural-language image-search phrases are normalized deterministically before bridge retrieval
- direct bridge keyword queries now fetch PhotoPrism detail payloads, so raw bridge calls and assistant-driven searches agree on attached metadata matches
- zero-result bridge queries now retry once with a small deterministic synonym expansion set for controlled near-miss recall
- the expansion dictionary is maintained in [services/photoprism-bridge/query_expansions.py](/Users/blackbox/blackbox-core/services/photoprism-bridge/query_expansions.py)
- recency-oriented phrases are now parsed deterministically, including:
  - `latest`
  - `recent`
  - `today`
  - `yesterday`
  - `this week`
  - `last week`
  - `this month`
  - `last month`
- quantity requests such as `latest 4 images` are now respected
- combined recency + keyword requests such as `latest facade images` preserve deterministic metadata matching and return newest-first results
- OpenWebUI as the main general interface
- one consolidated BookStack user guide for staff onboarding and day-to-day use
- Heimdall now reflects the LAN-safe app URLs for BookStack and PhotoPrism
- LAN access via Heimdall for the main services
- BlackBox Canvas shared board collaboration

## What Is Still Fragile

- PhotoPrism user-role behaviour is constrained by the current PhotoPrism edition
- user provisioning is now scriptable, but first login still requires the person to complete or skip the ZITADEL MFA setup prompt interactively
- label coverage in PhotoPrism is still weak; the current library has no usable non-null labels for runtime proof of label-only retrieval
- query normalization is intentionally shallow and rule-based
- query expansion is now limited to a tiny deterministic synonym map and still depends on real attached metadata being present
- some narrow misses can still happen if the relevant photo falls outside the current PhotoPrism candidate fetch window before local bridge matching runs
- retrieval is now deterministic across attached metadata, but broader query expansion is still intentionally out of scope
- PhotoPrism indexing and AI metadata generation currently behave as follows:
  - import path: `/photoprism/import`
  - auto import: disabled
  - auto index: every 300 seconds
  - caption and label generation are configured through `/etc/photoprism/vision.yml`
  - caption and label generation now run automatically through Ollama during the PhotoPrism AI pipeline
  - users can still edit metadata manually inside PhotoPrism; AI-generated captions and labels are not the only source of metadata
  - current active AI model: `gemma3:4b`
  - `gemma4:latest` is the preferred quality-first upgrade target from the PhotoPrism docs, but it still requires a newer Ollama version than the currently available local runtime
  - current caption prompt requires one factual sentence that starts with the main building, space, or object and focuses on visible materials, spatial condition, and lighting
  - current caption prompt explicitly avoids speculation, design interpretation, meta-language, and filler phrasing
  - current label prompt requires raw JSON label objects with `name`, `confidence`, and `topicality`
  - current label prompt returns at most 5 single-word singular labels and favors architectural nouns, materials, spatial elements, and site terms
  - the main manual metadata fields staff should correct when needed are titles, keywords, and other normal PhotoPrism metadata edits available in the UI
  - prompt bake-off result: the current architectural caption and label prompts performed best on representative sample images and remain the active defaults
- ZITADEL is still not a raw-IP service; `auth.local` remains the single hostname exception in the access model
- Canvas has working presence, but only anonymous/local identity
- some runtime behaviour still depends on live local state that is not fully owned by tracked files
- the current worktree contains intentional but mixed in-progress changes outside this documentation pass

## LAN Client Onboarding

- raw LAN IP services:
  - Heimdall `http://192.168.36.27:8080`
  - OpenWebUI `http://192.168.36.27:3000`
  - BlackBox Canvas `http://192.168.36.27:8787`
  - BookStack `http://192.168.36.27:6875`
  - PhotoPrism `https://192.168.36.27:2342`
- auth hostname exception:
  - ZITADEL `https://auth.local:8443`
- current alpha rule:
  - LAN clients that need BookStack or PhotoPrism sign-in should add `192.168.36.27 auth.local`
  - Windows clients can do that with [scripts/client-onboarding/windows_auth_local_onboarding.py](/Users/blackbox/blackbox-core/scripts/client-onboarding/windows_auth_local_onboarding.py)
  - trusting the BlackBox local CA is still optional but recommended if certificate warnings should be avoided

## OpenWebUI Role

- OpenWebUI is now the primary user-facing interface for BlackBox
- Heimdall remains the launcher and fallback entrypoint
- the live OpenWebUI runtime now frames:
  - OpenWebUI as the main place users should start
  - PhotoPrism as the backend image archive
  - Canvas as the parallel creative board
  - BookStack as the documentation system
- the active `PhotoPrism Assistant (llama3.1:8b)` now runs in strict renderer mode:
  - when tool output exists, it should render only the markdown table or the exact no-results line
  - conversational framing is intentionally suppressed to keep image-search output stable and trustworthy
- current starter prompts for the PhotoPrism assistant are:
  - `Search facade references`
  - `Explore concrete buildings`
  - `Find timber interiors`
  - `Search structural precedents`
  - `Show latest uploaded images`
- current known limitation:
  - recency is now supported for a defined set of temporal phrases, but the system is still metadata-based rather than embeddings-based
  - broader semantic image search is still future work

## Heimdall Branding

- Heimdall remains the launcher and fallback entrypoint
- the live browser tab title now shows `BlackBox`
- the current live branding source is `/Users/blackbox/heimdall-config/www/.env` via `APP_NAME`
