# Glossary

Plain-language definitions. Agents add a term here the first time it comes up in a session
(AGENTS.md section 6). Keep entries to one to three sentences; link to a lesson for more.

| Term | Meaning |
| --- | --- |
| **ADR** | Architecture Decision Record. A short document recording a hard-to-reverse decision, the options considered, and why. Lives in `docs/adr/`. |
| **AMO** | addons.mozilla.org, Mozilla's extension store. Extensions there are signed by Mozilla. |
| **Artifact build** | A Firefox build that downloads the already-compiled engine from Mozilla and only builds the frontend. Minutes instead of hours; only usable when we haven't changed C++/Rust code. |
| **Autoconfig** | A Firefox mechanism for setting and locking prefs from a file in the install folder. An alternative to policies for prefs that have no policy. |
| **Bisect** | Finding which commit introduced a bug by testing commits in a binary-search order. Only works well when commits are small and each one builds. |
| **Blink** | The page-rendering engine inside Chrome, Edge and other Chromium browsers. |
| **Branch** | A separate line of work in git. We do each task on its own branch and merge it into `main` by pull request. |
| **CEF** | Chromium Embedded Framework: Chromium packaged so other apps can show web pages with it. Large and frequently updated. |
| **chrome** (Mozilla meaning) | The browser's own interface — tabs, menus, toolbars — as opposed to web content. `chrome://` URLs are browser UI pages. Not related to Google Chrome; that's why our feature is called "compat tab". |
| **Chromium** | The open-source project behind Chrome, Edge, Brave, Opera, Vivaldi. |
| **CI** | Continuous Integration: automatic checks that run on every push or pull request. Ours runs in GitHub Actions. |
| **Commit** | A saved snapshot of changes in git, with a message explaining it. |
| **Compat tab** | Our feature for sites that only work in a Chromium-engine browser. Built in stages; see `docs/features/compat-tab.md`. |
| **Content process** | A separate program Firefox runs web pages in, so one site can't easily read another's data or crash the browser. |
| **Conventional Commits** | A commit message format: `type(scope): summary`, e.g. `fix(prefs): …`. |
| **Distribution folder** | `distribution/` inside the installed browser; Firefox reads `policies.json` and bundled extensions from it. |
| **Enterprise policy** | An officially supported rule (in `policies.json`) that configures and can lock Firefox settings. Our first choice for changes. |
| **ESR** | Extended Support Release: a Firefox version that gets security fixes for over a year without new features. We build on ESR 153. |
| **Extension (WebExtension)** | An add-on built with the standard browser-extension API, like uBlock Origin. |
| **Frontend** | The browser's interface code (JavaScript, HTML, CSS). |
| **Gecko** | Firefox's engine: turns HTML/CSS/JavaScript into what you see. |
| **Git / GitHub** | Git records the history of files; GitHub hosts the repository and runs CI and pull requests. |
| **Git ignore list (`.gitignore`)** | A file listing paths Git leaves out when you add files (it can still be overridden on purpose with `git add -f`). Ours keeps Firefox's source, build output, installers and secrets out of the repository. |
| **Hook (Claude Code)** | A script Claude Code runs automatically at certain moments (session start, before a command, when finishing). Used to enforce rules. |
| **Line endings (LF / CRLF)** | The invisible character(s) that end each line of text. Linux and macOS use LF; Windows traditionally uses CRLF. `.gitattributes` (Git's per-file-type rules) stores our text files as LF and keeps patch files exactly as written, because a patch whose line endings were changed can fail to apply. |
| **LTO** | Link-Time Optimization: a compiler technique that optimizes across the whole program. Mozilla's release builds use it. |
| **mach** | Mozilla's build command: `./mach build`, `./mach run`, `./mach package`, `./mach test`. |
| **MAR** | Mozilla ARchive: the signed update file format Firefox's updater installs. |
| **mozconfig** | The file of options telling `mach` how to build (optimization, branding, features). |
| **MPL-2.0** | Mozilla Public License 2.0, Firefox's license. Modified MPL files must stay MPL and be published. |
| **Native messaging** | A standard way for a browser extension to talk to a small program installed on the computer. Used by the compat-tab companion. |
| **omni.ja** | A zip file in the Firefox install that holds most of the frontend code. |
| **Parent process** | The main Firefox program that runs the UI and coordinates content processes. |
| **Patch** | A file describing line-by-line changes to source code. Our changes to Firefox are patches in `patches/`. |
| **PGO** | Profile-Guided Optimization: build once, run typical workloads to record what code is hot, rebuild optimized for that. Mozilla's release builds use it. |
| **Pref** | A Firefox preference (see `about:config`). Has a default value that can be overridden. |
| **Profile** | The folder holding one user's bookmarks, history, settings and extensions. |
| **Pull request (PR)** | A proposal to merge a branch into `main`, with a description, checks and review. |
| **Rapid Release** | Firefox's main channel. Moved to a two-week release cycle in September 2026. We don't track it. |
| **Rebase (of patches)** | Updating our patches so they apply to a newer Firefox version. |
| **Searchfox** | Mozilla's searchable website for the Firefox source code: searchfox.org. Agents use it to confirm that a file, pref or function really exists. |
| **Skill (Claude Code)** | A saved procedure Claude follows when you type `/name`. Ours are in `.claude/skills/`. |
| **SpiderMonkey** | Firefox's JavaScript engine. |
| **Subagent (Claude Code)** | A helper Claude starts in a fresh context for a focused job, e.g. our `reviewer`. |
| **Tag** | A permanent name for one commit in git, used for releases (`v153.4.0-cfx.1`). |
| **Tarball** | A single compressed archive file holding a whole folder tree, e.g. `firefox-153.4.0esr.source.tar.xz`, which is Firefox's source code. Downloaded into `work/`, never committed. |
| **Telemetry** | Usage data a program sends home. Disabled in this project. |
| **Upstream** | The original project we build on — Mozilla Firefox. "Upstream changes" means changes Mozilla made. |
| **User agent** | The text a browser sends to websites to identify itself. Many "Chrome only" sites just check this. |
| **WebRender** | Firefox's GPU-based graphics system. |
| **WebView2** | Microsoft's Chromium-based web view for Windows apps, kept up to date by Microsoft. Key to the compat tab on Windows. |
| **x86-64-v3** | A CPU feature level (roughly 2015+ Intel/AMD with AVX2). Building for it can be faster but won't run on older CPUs. |
