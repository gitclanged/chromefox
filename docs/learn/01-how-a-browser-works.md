# Lesson 01 — How a browser works

## The journey of a page

When you type `example.com` and press Enter:

1. **Find the server.** The browser asks DNS ("the internet's phone book") for the server's
   address.
2. **Connect securely.** It opens a connection and performs a TLS handshake: the server proves
   its identity with a certificate, and both sides agree on encryption keys.
3. **Ask for the page.** It sends an HTTP request. Part of that request is the
   **user agent** — a line of text saying which browser you are. (Remember this; the compat
   tab's first stage is about it.)
4. **Receive HTML.** The server sends back HTML: the page's structure.
5. **Fetch everything else.** HTML points to CSS (styling), JavaScript (behavior), images and
   fonts. The browser fetches those too. This is where ad blockers work: uBlock Origin
   looks at each of these requests and cancels the ones that match its filter lists.
6. **Build the page.** The **engine** parses HTML into a tree (the DOM), applies CSS, runs
   JavaScript, works out where everything goes (layout), and draws pixels (painting and
   compositing, usually on the GPU).
7. **Keep it alive.** JavaScript keeps running, responding to your clicks and fetching more
   data.

## Engine vs browser

- The **engine** does steps 4–7: turning web code into pixels. Firefox's engine is **Gecko**.
  Chrome, Edge, Brave and Opera all use **Blink** (from the Chromium project). Safari uses
  WebKit.
- The **browser** is the engine plus everything around it: tabs, address bar, bookmarks,
  history, settings, extensions, updates. Mozilla calls this surrounding UI the **chrome**
  (that's a decades-old term, unrelated to Google Chrome).

When a site "only works in Chrome", the cause is either that it checks the user agent and
refuses others, or that it depends on something Blink does that Gecko doesn't. Those two
causes need very different fixes — that's why the compat tab is built in stages.

## Why browsers are split into processes

A modern browser is several programs working together. Web pages run in separate
**content processes**, so a malicious or crashing page can't easily read another site's data
or take down the whole browser. The **parent process** runs the UI. Speed and memory
measurements must take all of them into account.

## Where this shows up in our project

| Concept | Our repo |
| --- | --- |
| User agent | `docs/features/compat-tab.md` stage 1 |
| Request filtering | uBlock Origin, `docs/features/ublock-origin.md` |
| Engine vs UI | `docs/ARCHITECTURE.md` §2 layers |
| Processes | `docs/ARCHITECTURE.md` "Processes"; `docs/features/performance.md` |

## Check your understanding

1. In which step does uBlock Origin do its work?
2. Why might pretending to be Chrome fix one site but not another?
3. If you changed how Firefox draws text, which layer would you be changing — engine or UI?
4. Why is a bug in a content process less dangerous than one in the parent process?
