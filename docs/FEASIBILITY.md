# Feasibility assessment

Written 2026-10-19. Facts about Firefox, Gemini and other projects were checked against the
sources listed at the bottom on that date; re-check anything time-sensitive before relying
on it.

## The short answer

**Most of this is feasible. One part is a research project, and one goal needs reframing.**

| Goal | Feasible for one owner + Claude Code? | Rough effort | Why |
| --- | --- | --- | --- |
| No AI features | **Yes, easily** | Days | Firefox now ships an enterprise policy (`AIControls`) that blocks all AI features and locks the setting. Mostly configuration, not code. |
| Less bloat (telemetry, studies, sponsored content, nags) | **Yes** | Weeks | Most of it is policies and default prefs. A few UI leftovers need small frontend patches. |
| uBlock Origin built in | **Yes, easily** | Days | Enterprise policy installs it from Mozilla's add-on site on first run and keeps it updated. |
| Your own branded build from source | **Yes, with effort** | 1–2 months to a repeatable pipeline | Needs a capable build machine and patience; builds take hours. |
| Signed, auto-updating releases | **Hard, mostly money and operations** | Months, ongoing | Code-signing certificates, an update server, per-platform packaging. |
| Keeping up with Firefox security fixes | **Feasible only with discipline** | Every ESR update, forever | This is the real cost of a browser fork. See "The hidden cost". |
| Compat for Chrome-only sites, stages 1–2 | **Yes** | 1–3 months | User-agent rules per site, then an "open in Chromium window" companion. |
| A true Chromium-engine **tab inside** the Firefox window | **Research-grade; low odds** | 6–12+ months, may fail | Nobody ships this inside Gecko. See "The compat tab". |
| "Most performant Firefox fork" | **Partly** | Ongoing | You can be measurably leaner than stock Firefox. Large engine speedups are unlikely: Mozilla already ships highly optimized builds. |
| "Most performant Chromium fork" | **Not a meaningful target here** | — | This project embeds a Chromium runtime for compatibility; it does not fork Chromium. See "Performance". |

## What a professional in your position would do first

1. **Not fork yet.** Prove the value with configuration on stock Firefox ESR (Phase 0).
   If policies alone deliver "no AI, no bloat, uBlock built in", the fork's job shrinks to
   branding, packaging and the compat tab — far less to maintain.
2. **Pick one platform** to ship first: the one you use daily. Build infrastructure is easiest
   on Linux; the compat tab is easiest on Windows (see below).
3. **Base on ESR, not the rapid-release channel.** Mozilla moved the rapid channel to a
   two-week cadence starting with Firefox 155 in September 2026. Rebasing patches every two
   weeks is not sustainable for one person. ESR 153 (released July 21, 2026) is supported for
   at least 15 months and only receives security and stability fixes between major versions.
4. **Measure the compat problem before solving it.** Keep a list of real sites that fail and
   why. Most "requires Chrome" messages are user-agent sniffing, fixable with a rule. The
   expensive solutions are only justified by the sites that remain.
5. **Write the maintenance plan before the features.** Decide who ships a security update
   on a holiday weekend, and how fast.

## The hidden cost: keeping up with Firefox

Every patch we carry must be re-applied to every future Firefox release. Mozilla's security
fixes arrive on a schedule and sometimes in emergencies. The project's credibility rests on
shipping them quickly. Our design choices all serve this:

- **ESR base** — fewer, smaller upstream changes between our releases.
- **Patch-set repository** (not a fork of Firefox's git history) — every change is a small,
  named file we can re-apply and reason about. LibreWolf and Zen work this way.
- **Least-intrusive layer first** — a policy or pref survives Firefox updates far better
  than a code patch.
- **Automation** — CI checks that patches still apply to the pinned version and, later, to
  the next one, so breakage is found before release day.
- **Gemini upstream reports** — before each ESR update, Gemini reads the release notes and
  the upstream changes to files we patch, and predicts conflicts.

Once a year a new ESR major version (the next after 153) means a bigger rebase. Plan a few
weeks for it.

## The compat tab

You want sites that "require Chrome" to work. There are four very different ways to do it,
and the plan uses them in order ([ADR-0004](adr/0004-compat-tab-staged.md)):

| Stage | What it is | Difficulty | Covers |
| --- | --- | --- | --- |
| 1. Site rules | Tell specific sites we are Chrome (user-agent override) and apply known fixes | Low | Most sites that only *sniff* for Chrome |
| 2. Companion window | A button: "Open this page in a Chromium window". Launches an installed Chromium-family browser in a separate app window and profile, or (Windows) a small WebView2 shell | Medium | Sites that truly need Blink-only features (some WebUSB/WebHID/WebSerial tools, some web apps) |
| 3. Embedded tab (research) | A real tab in our window whose content area is drawn by Chromium (WebView2 on Windows, CEF elsewhere) | Very high | Same sites as stage 2, without a second window |
| 4. Fork Chromium | Build Chromium ourselves | Out of scope | — |

Why stage 3 is so hard:

- Firefox's tabs are built around Gecko content processes. A Chromium tab means placing a
  native child window over the content area and keeping it in sync with resizing, scrolling,
  full screen, pop-ups, focus, keyboard shortcuts, menus, drag-and-drop, printing,
  downloads, accessibility and high-DPI screens — for every platform.
- It is a **second browser** with its own cookies, logins, history, permissions and
  extensions. uBlock Origin would **not** run inside it.
- If you bundle Chromium (CEF), you must also ship Chromium's security fixes, which arrive
  even more often than Firefox's. On Windows, the WebView2 runtime is updated by Microsoft,
  which is the main reason stage 3 should start on Windows if it is attempted at all.
- There is a precedent outside Firefox (a WebKit-based macOS browser that embeds CEF in
  tabs), and Microsoft Edge's IE mode shows the idea is workable inside one company's
  browser. There is no known precedent inside Gecko.

The plan time-boxes stage 3 to a four-week prototype after stages 1–2 ship, with a written
go/no-go decision.

## Performance

**What is realistic:**

- **Leaner than stock Firefox.** No telemetry uploads, no studies, no sponsored-content
  fetches, no AI models downloading or running, fewer background tasks. These show up as
  lower idle CPU and network use, less memory and sometimes faster startup — and they can
  be measured honestly.
- **CPU-tuned builds.** Compiling for newer CPU instruction sets (x86-64-v3, i.e. AVX2) can
  help some workloads, at the cost of not running on older CPUs. Must be measured; often a
  few percent at most.
- **Careful defaults.** Some preferences trade memory for speed. Every change must be
  benchmarked, not copied from "tweak lists" online.

**What is not realistic:**

- Beating Mozilla's engine work by large margins. Mozilla's official builds already use
  profile-guided optimization (PGO) and link-time optimization (LTO). Forks that advertise
  big gains usually measure noise or ship unsafe settings.
- A "most performant Chromium". In stages 2–3 we use a Chromium runtime someone else builds
  (Microsoft's WebView2, or prebuilt CEF). Building Chromium yourself needs roughly 16–64 GB
  of RAM, 100–150 GB of disk and hours per build on a fast machine. The right goal for the
  compat tab is: **costs nothing when unused, starts fast when used.**

The performance program and its rules are in [features/performance.md](features/performance.md)
and [ADR-0006](adr/0006-performance-claims-need-data.md).

## Can Claude Code do all of it?

Mostly yes, with these limits in mind:

- **Slow feedback.** A C++ change in Gecko means a rebuild; the first full build takes hours
  and incremental ones still take minutes. Frontend-only changes can use Mozilla's "artifact
  builds" (download prebuilt engine parts), which are fast. Prefer frontend work.
- **Huge codebase.** Firefox is far larger than any context window, including Gemini's
  1M tokens. Agents must search it (Mozilla's Searchfox, `grep` in the source tree), not
  "load" it. Never assume an API exists; find it in the source for our pinned version.
- **You cannot check code by reading it**, so the project checks it by process: small
  patches, a registry, automated checks, tests, a reviewer agent that did not write the
  change, and a separate auditor (Gemini). This is why the docs are so prescriptive.
- **Security judgment.** Agents must stop and ask before touching security-sensitive code
  (AGENTS.md rule 2.7).

## Money and machines

| Item | Needed when | Approximate cost |
| --- | --- | --- |
| Build machine: 8+ cores, 16–32 GB RAM, 100+ GB free SSD | Phase 1 | Use what you have if it meets this; otherwise a desktop or a cloud VM billed by the hour |
| GitHub (private repo, Actions for checks) | Phase 0 | Free tier is enough for checks; full Firefox builds need bigger runners or your machine |
| Claude subscription or API usage | Throughout | Depends on plan |
| Gemini 4 Argon | Weekly audits | $2 / $10 per million input / output tokens until Nov 30, 2026 (introductory), then higher. A full-repo audit is well under 1M tokens early on |
| Windows code-signing certificate | Before public Windows release | Hundreds of USD per year; without it users see SmartScreen warnings |
| Apple Developer Program | Before public macOS release | 99 USD per year; required for notarization |
| Domain + simple website | Phase 6 | Small |

Mozilla's own minimum for building is 8 GB+ RAM recommended and 30–40 GB free disk; the
higher numbers above are for optimized release builds and keeping more than one tree.

## Legal and licensing

*Not legal advice — confirm with a lawyer before a public release.*

- **Firefox** is MPL-2.0: you may modify and redistribute it; changes to MPL-licensed files
  must be published under MPL-2.0. Publishing this repository satisfies that.
- **Firefox trademarks** (name and logos) may not be used for a modified build. Source builds
  are unbranded by default; we add our own branding.
- **"Chrome" is a Google trademark** for a browser. A product named "Chromefox" invites a
  complaint. Treat the name as a codename until you choose a public one
  ([ADR-0005](adr/0005-naming-and-trademarks.md)).
- **uBlock Origin** is GPL-3.0. Shipping it as a separate, unmodified extension installed
  from Mozilla's add-on site keeps the licenses separate. Merging its code into the browser
  would not — that is one reason Waterfox chose a different engine.
- **WebView2 / CEF** for the compat tab have their own licenses and redistribution terms;
  review them in Phase 4.

## A note on Waterfox's ad blocker

Waterfox's new built-in blocker is not proprietary: it is built on Brave's open-source
`adblock-rust` library (MPL-2.0) and runs inside the browser rather than as an extension.
Waterfox chose it partly because uBlock Origin's GPL-3.0 license complicates deep
integration, and it allows text ads on its search partner's page by default to fund the
project. Your preference for uBlock Origin is a reasonable product choice; just know the
trade-off is "extension we don't control the code of" versus "engine we'd have to maintain".

## Sources

- Mozilla two-week release cadence and Firefox 153 ESR: https://www.theregister.com/a/5274423
- Firefox ESR 153 release date and ESR 140 end of life: https://endoflife.ai/article-firefox-esr-eol
- Firefox AI kill switch (Firefox 148): https://www.techspot.com/news/111453-firefox-148-rolls-out-promised-ai-kill-switch.html
- `AIControls` policy reference: https://firefox-admin-docs.mozilla.org/reference/policies/aicontrols/
- `GenerativeAI` policy reference: https://firefox-admin-docs.mozilla.org/reference/policies/generativeai/
- `ExtensionSettings` policy reference: https://firefox-admin-docs.mozilla.org/reference/policies/extensionsettings/
- Firefox source on GitHub: https://www.phoronix.com/news/Firefox-On-GitHub
- Building Firefox (requirements, artifact builds): https://searchfox.org/firefox-main/source/docs/setup/linux_build.md
- CEF build requirements: https://bitbucket.org/chromiumembedded/cef/wiki/MasterBuildQuickStart
- Chromium build requirements: https://chromium.googlesource.com/chromium/src/+/b05a42bd3d0e84d55392ae984a69946e56203c71/docs/windows_build_instructions.md
- LibreWolf source structure: https://codeberg.org/librewolf/source
- Zen's Surfer build tool: https://github.com/zen-browser/surfer
- Waterfox ad blocking: https://www.waterfox.com/support/waterfox-ad-blocking/ and https://alternativeto.net/news/2026/4/waterfox-to-integrate-brave-adblock-engine-with-search-ads-enabled-by-default
- Gemini 4 Argon model page: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Gemini 4 Argon pricing: https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud
