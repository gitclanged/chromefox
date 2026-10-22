---
name: explain
description: Teach the owner a concept, file, decision or part of the project in plain language, anchored in this repository. Use when the owner asks what something is, how parts connect, or why something is done a certain way.
argument-hint: "[topic, file, ADR or patch ID]"
---

# Explain: $ARGUMENTS

The owner is not a programmer and wants to understand well enough to make architecture
decisions.

1. Find where this topic lives in the repo (docs, ADRs, specs, patches, scripts) and read it.
2. Explain in this order, under 400 words unless asked for more:
   - **One-sentence answer.**
   - **Analogy** to something everyday, then the precise version.
   - **Where it lives** in this project (folder, file, layer in docs/ARCHITECTURE.md).
   - **How it connects:** what depends on it and what it depends on. A small Mermaid diagram
     if relationships matter.
   - **Why it's done this way** here, citing the ADR or source; alternatives in one line each.
   - **What could go wrong** and how we'd notice.
3. Offer two or three check-your-understanding questions.
4. If a term isn't in `docs/GLOSSARY.md`, add it (on the current branch, or note it for the
   next one if on `main`).
5. If you find the docs are wrong or unclear about this topic, say so and propose the fix.
