# The Alien Key

An interactive argument map of what could be true about alien life — and why you might believe it.

Not a dichotomous key in the taxonomic sense (those identify a specimen). This is a **branching map of hypotheses**: each node is a claim, its children are the ways that claim could be true, and each carries evidence for and against.

## Structure

Two files do all the work:

- **`data.json`** — all content. Nodes (the claims) and arguments (the evidence), kept separate.
- **`index.html`** — the entire app. Vanilla JS, no build step, no dependencies.

### The content model

```jsonc
{
  "arguments": {
    "fermi": { "title": "The Fermi Paradox", "body": "..." }
  },
  "nodes": {
    "exist": {
      "label":    "Aliens exist",        // short — used in nav and buttons
      "claim":    "Life beyond Earth…",  // the full statement
      "summary":  "…",                   // a paragraph of framing
      "children": ["advanced", "not-advanced"],
      "for":      ["exoplanets", "drake"],   // argument IDs, not prose
      "against":  ["fermi", "rare-earth"],
      "seeAlso":  ["filter-ahead"]           // sideways links, not children
    }
  }
}
```

Three decisions worth preserving:

1. **Arguments are referenced by ID, never inlined.** The Fermi paradox appears under five nodes and the zoo hypothesis under three — but each is written exactly once. Sharpen the wording in one place, it sharpens everywhere.
2. **Nodes take any number of children.** "Hostile / indifferent / benevolent" is three-way. Nothing in the code assumes two.
3. **`seeAlso` is a separate relation from `children`.** It's really a graph; this keeps it navigable as a tree without lying about that.

## Extending it

Only ever touch `data.json`. Add a node, give it a claim and summary, list argument IDs under `for` and `against`, wire it into some parent's `children`. Reload. The interface is entirely derived.

Then check your work:

```bash
python3 validate.py
```

Catches dangling references, unreachable nodes, and unused arguments — the failure modes you'll actually hit as this grows.

## Running locally

```bash
python3 -m http.server 8000
```

`data.json` is fetched over HTTP, so `file://` won't work.

## Deployment

Deployed on [Railway](https://railway.app) from a `Dockerfile` (Caddy serving static files). Pushes to `main` redeploy automatically.
