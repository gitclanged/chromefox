# Security policy

## How security works for a Firefox-based browser

Almost all security fixes come from Mozilla. Our main security duty is to **ship Mozilla's
ESR security updates quickly** — the target is within 72 hours of Mozilla's release, and
within 24 hours when Mozilla marks a fix as critical or actively exploited. The procedure is
in [docs/runbooks/security-release.md](docs/runbooks/security-release.md).

If the project cannot meet that target for a sustained period, it must say so publicly on the
README and the download page. A browser that silently lags on security fixes is worse than
no browser.

## Reporting a vulnerability

- **In Firefox itself:** report to Mozilla: https://www.mozilla.org/security/bug-bounty/
- **In our patches, prefs, compat tab or build:** open a private
  [GitHub security advisory](https://docs.github.com/en/code-security/security-advisories)
  on this repository. Do not open a public issue.

## Supported versions

Only the latest release is supported. There are no long-term branches of this project.
