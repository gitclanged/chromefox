# Lesson 06 — Reading a patch

You don't need to understand every line of code to review a patch well. You need to see
**where** it changes things, **how much**, and whether that matches **what it claims**.

## Anatomy of a patch

```diff
diff --git a/browser/components/example/Example.sys.mjs b/browser/components/example/Example.sys.mjs
--- a/browser/components/example/Example.sys.mjs
+++ b/browser/components/example/Example.sys.mjs
@@ -42,7 +42,10 @@ export const Example = {
   init() {
     this.loadSettings();
-    this.showPromotion();
+    // Chromefox: promotions are disabled (CFX-0203, docs/features/debloat.md).
+    if (!Services.prefs.getBoolPref("chromefox.debloat.hidePromotions", true)) {
+      this.showPromotion();
+    }
   },
```

| Part | Meaning |
| --- | --- |
| `diff --git a/… b/…` | Which file is changed (`a/` = before, `b/` = after) |
| `@@ -42,7 +42,10 @@` | Around line 42: 7 lines before became 10 lines after |
| Lines starting with ` ` (space) | Context — unchanged lines shown so you can see where you are |
| Lines starting with `-` | Removed |
| Lines starting with `+` | Added |

This example (illustrative, not real Firefox code) shows good habits: a comment naming the
patch ID and spec, and a `chromefox.*` pref so the change can be switched off.

## Questions to ask about any patch

1. **Which folder?** `browser/` (UI) is normal. `netwerk/`, `security/`, `ipc/`, `dom/`,
   `js/` are engine or red-zone areas — expect an ADR.
2. **How big?** Count `+` and `-` lines. Our target is under ~300 changed lines per patch.
3. **Does it match the registry row and the spec?** Same files? Same purpose?
4. **Is there a pref switch?**
5. **Is anything removed that might matter?** A `-` line that deletes a security check is a
   stop sign.
6. **Would this survive an update?** Changes to big, busy files conflict more often.

## Asking for help

Ask Claude: "Walk me through patch CFX-0203 hunk by hunk in plain language, then tell me
the riskiest line." Then ask Gemini the same about the same patch and compare.

## Check your understanding

1. In the example, how many lines were added and removed?
2. Why does the comment include the patch ID?
3. A patch touches `security/manager/`. What should happen before it's merged?
