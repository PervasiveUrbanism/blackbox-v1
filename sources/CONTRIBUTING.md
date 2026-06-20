# Project Documentation And Maintenance Rules

Last updated: 2026-04-22

## Documentation Is Required Work

Documentation is a first-class part of the BlackBox system.

Every milestone should update documentation, not just implementation files.

## Required Project File Updates

Every milestone must review and update, when affected:

- `docs/project/completed.md`
- `docs/project/roadmap.md`
- `docs/project/next-steps.md`
- `docs/project/current-state.md`

## Git Discipline

- run `git status` before starting work
- keep milestone diffs focused
- do not leave accidental junk or debug artifacts in the worktree
- commit only at logical checkpoints
- do not perform destructive Git actions unless explicitly requested

## Runtime vs Repo Differences

- document live-runtime changes that are not fully represented in tracked files
- call out when the running system depends on ignored local env files, local certs, or existing container state
- do not pretend the repo owns behaviour that it does not actually reproduce

## Writing Guidance

- prefer markdown over ad hoc scratch notes
- summarise outcomes rather than pasting raw logs
- keep milestone sections readable and review-friendly
- keep milestone numbering consistent with `docs/project/roadmap.md`
