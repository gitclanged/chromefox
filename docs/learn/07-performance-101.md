# Lesson 07 — Performance 101

## "Faster" is several different things

| What people feel | What we measure |
| --- | --- |
| "It opens instantly" | Cold and warm startup time |
| "Pages feel snappy" | Speedometer (responsiveness), page-load times |
| "Heavy web apps run well" | JetStream (JavaScript/WebAssembly) |
| "Scrolling is smooth" | MotionMark (graphics), frame timing |
| "My laptop stays cool, battery lasts" | Idle CPU wakeups, memory, network at idle |

A change can help one and hurt another. Honest reporting shows both.

## Why single runs lie

Benchmarks vary from run to run: other programs, CPU temperature, power settings, caches.
A 3% "improvement" from one run of each is often noise. Our method (`perf/README.md`):

- Same machine, same session, same OS state, power plugged in.
- Stock Firefox ESR of the same version as the baseline.
- Many runs (e.g. 10+), alternating builds, report the **median** and the **spread**.
- If the ranges overlap a lot, the honest conclusion is "no measurable difference".

## Where browser speed actually comes from

Mostly from the engine, which Mozilla's engineers tune constantly, and from **how it's
compiled**. Mozilla uses PGO (optimize for the code paths real browsing uses) and LTO
(optimize across the whole program). If we build *without* those, we're slower than stock
Firefox before we change anything. That's why our first performance task is simply matching
stock.

Our realistic wins: doing less in the background (no telemetry, studies, sponsored fetches,
AI models), sensible defaults, and possibly CPU-specific builds.

## Red flags in other projects' claims

- No method, machine or run count stated.
- Compared against a different version of Firefox.
- One benchmark shown, others omitted.
- "Tweaks" that disable security features (process isolation, sandboxing, safe browsing).

## Check your understanding

1. Build A scores 101, build B scores 99, each run once. What can you conclude?
2. Why must the baseline be the *same* Firefox version?
3. Why might our first build be slower than stock Firefox?
4. Name two improvements we can honestly expect, and one we shouldn't promise.
