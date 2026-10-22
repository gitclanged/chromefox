# Contributing

Thanks for helping. This project is maintained by a non-programmer owner working with AI
coding agents, so the process is deliberately explicit. Humans follow the same rules as the
agents — read [AGENTS.md](AGENTS.md) sections 2–5; they apply to you too.

## Before you write code

1. Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) to see where your change belongs.
2. Check [docs/STATUS.md](docs/STATUS.md) and open issues so you do not duplicate work.
3. For a new feature, open an issue with the **Feature** template. Non-trivial features need
   a spec in `docs/features/` before code is reviewed.

## Making a change

1. Fork, then branch from `main`: `git switch -c feat/<topic>`.
2. Keep the change to one purpose. Prefer the least-intrusive layer (policy → pref →
   frontend patch → C++ patch).
3. If you add or change a patch, update [patches/REGISTRY.md](patches/REGISTRY.md).
4. Run the repository checks:

   ```bash
   python3 scripts/check_registry.py
   python3 scripts/check_links.py
   ```

5. Commit using Conventional Commits, e.g. `fix(prefs): keep translations available`.
6. Open a pull request and fill in the template, including **how you verified it**.

## What reviewers look for

The checklist in [docs/QUALITY.md](docs/QUALITY.md). The most common reasons a pull request
is sent back: missing registry entry, docs not updated, a patch touching more than it needs
to, or a performance claim without measurements.

## Reporting a site that only works in Chrome

Use the **Site compatibility** issue template. Include the URL, what breaks, and whether
switching the user agent fixes it. These reports drive the compat-tab rules list.

## Security issues

Do not open a public issue. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the Mozilla Public License 2.0 (see [LICENSE](LICENSE)),
the same license as Firefox.
