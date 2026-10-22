# Lesson 03 — How a fork works

## Pin, patch, build

Our repository is a **recipe**, not a copy of Firefox:

1. **Pin.** `upstream/firefox.toml` names one exact Firefox release, e.g. `153.4.0esr`,
   with a checksum so we know the download wasn't tampered with.
2. **Patch.** `patches/` holds small files, each describing a few changed lines in Firefox's
   source. They are numbered and applied in order.
3. **Configure.** `prefs/` and `branding/` are copied into the source tree.
4. **Build.** `mach` compiles the result.

Think of it as: *Firefox 153.4 + these 23 named changes + this configuration = our browser*.

## What happens when Mozilla releases an update

Say Mozilla releases `153.5.0esr` with security fixes:

1. We change the pin to `153.5.0esr`.
2. We try to apply our patches to the new source.
3. Most apply cleanly, because ESR updates are small.
4. If one fails, it's because Mozilla changed the same lines we change. We **rebase** that
   patch: look at what Mozilla changed, re-do our small change on top of it.
5. Build, test, release.

Once a year, the next ESR major arrives with a year of changes, and many patches need
rebasing. That's a planned project of a few weeks.

**Every patch is a recurring cost.** A 10-line patch in a stable file costs almost nothing
per update; a 500-line patch spread across busy files can cost days. This is why the rules
push toward policies, prefs and small patches.

## Why not just fork Firefox's git history?

You could copy all of Firefox into your own repository and edit files directly. It feels
simpler at first. But then your changes are mixed into millions of lines, every update is a
giant merge, and nobody (human or AI) can answer "what exactly did we change, and why?"
In the patch-set model, the answer is always: `patches/REGISTRY.md`. See ADR-0001.

## Why ESR and not the newest Firefox?

Rapid release now ships every two weeks. Each one can break our patches. With one owner,
that's a treadmill. ESR changes only for security and stability between yearly majors. We
trade newest features for sustainability. See ADR-0002.

## The registry

`patches/REGISTRY.md` is a table with one row per patch: ID, file, feature, layer, which
Firefox files it touches, risk, and **why it exists**. A script checks that every patch file
is listed and every row points to a real file. When you review a pull request that adds a
patch, read its registry row first — if the "why" doesn't convince you, ask.

## Check your understanding

1. What two things change when we update to a new Firefox ESR dot release?
2. A patch fails to apply after an update. What does that tell you?
3. Why does the registry ask which layer a patch is in?
4. Two patches each change the same Firefox file. What risk does that create?
