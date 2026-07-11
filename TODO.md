# TODO

Parked work for The Alien Key. Nothing here is started.

## 1. Type is too small

Body text is hard to read on the live site. Bump the base size and re-check the whole scale, not just one rule — the argument bodies, card summaries, and the `peek` line under each branch are the worst offenders, and the JetBrains Mono labels are smaller still.

Currently: 16px base, argument bodies and card text at 13.5–14.5px, mono labels at 10.5–11.5px. That mono floor is almost certainly the real problem.

Touch the `:root` scale and the component rules together so the hierarchy survives the change. Check on a real display at a real viewing distance, not a zoomed browser.

## 2. Link out on the hard concepts

Arguments like the Fermi paradox, the Great Filter, the Drake equation, the Rare Earth hypothesis, and the dark forest deserve a "read more" pointer for anyone who wants the real background.

Schema change: add an optional `links` array to each entry in `arguments`, then render them at the bottom of the expanded argument body.

```jsonc
"fermi": {
  "title": "The Fermi Paradox",
  "body": "…",
  "links": [
    { "label": "Stanford Encyclopedia of Philosophy", "url": "https://…" },
    { "label": "SETI Institute", "url": "https://…" }
  ]
}
```

Prefer durable, high-quality sources — SEP, university pages, the original papers (Hart 1975, Hanson 1998, Ward & Brownlee 2000) — over listicles and blogspam. Wikipedia is acceptable as a secondary link but shouldn't be the only one.

Then extend `validate.py` to check that every link has both a label and a URL.

## 3. Remove every em dash

Currently **49** of them: 40 in `data.json`, 6 in `README.md`, 3 in `index.html`.

Not a find-and-replace job. An em dash usually holds a sentence together, so removing one means recasting the clause — into a period, a colon, a comma, or parentheses depending on what the dash was doing. A blind swap to a hyphen or a comma will produce a lot of limp, comma-spliced prose.

Do it by hand, file by file, reading the result aloud. Re-run `python3 validate.py` afterward to confirm the JSON still parses.
