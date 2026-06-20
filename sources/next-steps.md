# Next Steps

Last updated: 2026-05-06

## Step 9 Priority List

### 9.0 Project tracking

- keep project docs current and milestone numbering stable

### 9.1 Canvas investigation

- clarify collaboration identity expectations and decide whether lightweight display names are needed

### 9.2 OpenWebUI result UX

- improve result presentation, especially structured image-search results

### 9.3 Delivery and retrieval stability

- keep result delivery, thumbnail rendering, and retrieval coverage stable before any search expansion

### 9.4 Query expansion

- deterministic query expansion is now in place; observe recall/precision in everyday use before broadening the synonym set any further
- maintain the dictionary only in [services/photoprism-bridge/query_expansions.py](/Users/blackbox/blackbox-core/services/photoprism-bridge/query_expansions.py) and only after a real failed search

### 9.6 User provisioning automation

- the admin provisioning script is now in place; validate it in everyday use and keep the PhotoPrism admin-role caveat explicit until the product role model improves
- keep the single-hostname auth exception (`auth.local`) documented until a fuller DNS or reverse-proxy strategy replaces it
- keep the BookStack LAN guidance explicit: the app URL is LAN-safe, but OIDC still depends on `auth.local`

### 9.7 OpenWebUI as primary interface

- completed as a runtime UX and prompt pass
- strict renderer mode is now the intended behavior for the PhotoPrism assistant; preserve that deterministic output style unless a later milestone deliberately redesigns the rendering layer
- deterministic recency support is now in place for supported temporal phrases such as `latest`, `recent`, `today`, `this week`, and `this month`
- keep the `BlackBox User Guide` aligned with any future OpenWebUI or access-flow changes
- keep the PhotoPrism AI/search documentation aligned with the real indexing and metadata-generation behavior
- the current LAN alpha onboarding helper is [scripts/client-onboarding/windows_auth_local_onboarding.py](/Users/blackbox/blackbox-core/scripts/client-onboarding/windows_auth_local_onboarding.py); keep the `auth.local` hostname requirement explicit until shared DNS or a different auth entrypoint replaces it

### 10.1 Basic AI interaction in Canvas

- begin the Step 10 work by exploring a simple request/response AI pattern inside Canvas without building a full agent system

## Immediate Order

1. commit the current intentional Step 9 stabilization work at a clean checkpoint
2. use the system in internal alpha mode and capture real failed searches before changing the expansion dictionary again
3. keep the OpenWebUI renderer behavior stable before considering any broader AI search features
4. move to Step 10 only after the current access, onboarding, and search workflow feels reliable in everyday use
