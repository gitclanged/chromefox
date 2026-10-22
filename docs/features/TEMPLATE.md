# Feature: <name>

- **Status:** Draft | Approved | In progress | Shipped | Removed
- **Owner decision needed:** yes/no (link to OPEN-QUESTIONS row)
- **Roadmap tasks:** P?-??
- **Pref switch:** `chromefox.<feature>.enabled` (default: true/false)
- **Patch series:** `patches/0?00-<series>/` (or "none — configuration only")

## Problem

What the user experiences today and why it's a problem. One paragraph.

## Goals

- Measurable outcome 1
- Measurable outcome 2

## Non-goals

- What this feature deliberately does not do.

## Design

Which layer (policy / pref / extension / frontend / engine) and why higher layers are not
enough. Components, data, UI. Reference upstream files with Searchfox links for the pinned
version — never from memory.

## Security and privacy

What data does this touch? What new attack surface does it add? What happens if it fails?

## Maintenance cost

Which upstream files does it depend on? How likely are they to change between ESR versions?

## Testing

- Verification level (see `docs/QUALITY.md`).
- Manual test steps a non-programmer can follow.
- Automated tests, if any.

## Results

Filled in as work happens: what was verified, on which version, with links to PRs and data.

## Open questions

- …
