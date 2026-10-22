# Lesson 02 — Inside Firefox

## The big parts

| Part | What it does | Language | Do we change it? |
| --- | --- | --- | --- |
| **Gecko** (layout, styling) | Turns HTML and CSS into positioned boxes | C++ and Rust | Almost never |
| **SpiderMonkey** | Runs JavaScript | C++ | No |
| **WebRender** | Draws pages using the GPU | Rust | No |
| **Networking** (Necko) | Connections, caching, HTTP, TLS | C++ | No — red zone |
| **Toolkit** | Shared pieces: preferences, extensions, updates, policies | JS and C++ | Configure, rarely patch |
| **Browser frontend** (`browser/`) | Tabs, address bar, menus, settings pages, new tab | JavaScript, HTML, CSS | Yes — small patches |
| **WebExtensions runtime** | Runs add-ons like uBlock Origin | JS and C++ | No — we just use it |

The source tree is enormous — tens of millions of lines. No person or AI reads all of it.
Engineers navigate it with **Searchfox** (searchfox.org), Mozilla's code search, which is why
our agents must cite a Searchfox link or a file path in our pinned source whenever they
claim something about Firefox.

## How Firefox is configured

From most official to most invasive:

1. **Enterprise policies** — a JSON file (`policies.json`) in the install's `distribution/`
   folder. Designed for companies to turn things off and lock settings. Mozilla supports and
   documents every policy. This is where most of our "no AI, no bloat, uBlock built in" lives.
2. **Preferences ("prefs")** — thousands of named settings you can see at `about:config`.
   Firefox ships defaults; we can override defaults. Prefs can be renamed or removed by
   Mozilla, so each of ours must be re-checked on updates.
3. **Code** — the frontend and engine themselves. Changing them means a patch.

## How Firefox is built

- **`mach`** is the command you use for everything: `./mach bootstrap` installs the tools,
  `./mach build` compiles, `./mach run` starts the result, `./mach package` makes an
  installable archive, `./mach test` runs tests.
- **`mozconfig`** is a small file of build options: optimization level, which branding to use,
  which features to include.
- A first full build takes hours. Later builds reuse work and are faster. If only frontend
  files changed, an **artifact build** downloads Mozilla's pre-compiled engine and builds in
  minutes — a big reason we prefer frontend patches.

## How Firefox is released

- **Rapid release:** new version every two weeks (since September 2026).
- **ESR:** one version a year, supported for more than a year with only security and
  stability fixes. **We use ESR 153.**
- **Security advisories:** Mozilla publishes what each release fixes. Our job is to ship
  those fixes quickly (see `SECURITY.md`).

## Where this shows up in our project

| Concept | Our repo |
| --- | --- |
| Policies | `prefs/policies.json`, `prefs/README.md` |
| Prefs | `prefs/`, AGENTS.md rule 2.4 |
| mozconfig, mach | `docs/runbooks/build-locally.md` (Phase 1) |
| ESR | `docs/adr/0002-esr-base.md` |

## Check your understanding

1. You want to hide a menu item. Which three layers would you try, in which order?
2. Why is an artifact build only possible for some changes?
3. What's the risk of relying on a pref that has no policy?
4. Why do agents need Searchfox if they "know" Firefox?
