# Feature: uBlock Origin built in

- **Status:** Draft (policy written, not yet tested)
- **Owner decision needed:** yes — OPEN-QUESTIONS #2 (install mode)
- **Roadmap tasks:** P0-03, P1-06
- **Patch series:** `patches/0400-ublock/` (expected to stay empty)
- **Decision record:** [ADR-0003](../adr/0003-ublock-via-policy.md)

## Goals

- On first launch, uBlock Origin is installed, enabled and visible in the toolbar.
- It stays updated through addons.mozilla.org without any action from us.
- Default uBO filter lists, unchanged. We don't curate lists.

## Design

`ExtensionSettings` policy in `prefs/policies.json`:

```json
"uBlock0@raymondhill.net": {
  "installation_mode": "normal_installed",
  "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi",
  "default_area": "navbar"
}
```

- `normal_installed`: installed automatically; the user can disable it.
- `force_installed` (alternative): the user cannot remove it.
- `default_area: "navbar"` puts the uBO button on the toolbar instead of the overflow menu.

## Limits users must be told about

- uBlock Origin does **not** filter pages opened in the compat tab's Chromium window.
- First install needs network access to addons.mozilla.org. Offline first run is a possible
  later improvement (bundle the `.xpi`, see ADR-0003 option 2).

## Testing

1. Fresh profile with the policy: within a minute of first launch, `about:addons` shows uBO
   enabled; the toolbar shows its icon.
2. Visit a known ad-heavy page; the uBO badge shows blocked requests.
3. With `normal_installed`: user can disable it. With `force_installed`: "Remove" is absent.
4. `about:policies` shows no errors for `ExtensionSettings`.

## Results

_Not yet tested._
