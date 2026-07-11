#!/usr/bin/env python3
"""Check data.json for the failure modes that actually bite as the tree grows:
dangling references, nodes you can't reach, arguments nobody cites."""

import json
import sys

d = json.load(open("data.json"))
nodes, args = d["nodes"], d["arguments"]

problems = []

for nid, n in nodes.items():
    for ref in n.get("children", []) + n.get("seeAlso", []):
        if ref not in nodes:
            problems.append(f"{nid}: points at a node that doesn't exist -> {ref}")
    for ref in n.get("for", []) + n.get("against", []):
        if ref not in args:
            problems.append(f"{nid}: cites an argument that doesn't exist -> {ref}")

# Anything you can't walk to from the root is invisible to users.
reached, stack = set(), ["root"]
while stack:
    cur = stack.pop()
    if cur in reached or cur not in nodes:
        continue
    reached.add(cur)
    stack += nodes[cur].get("children", [])

orphans = set(nodes) - reached
cited = {a for n in nodes.values() for a in n.get("for", []) + n.get("against", [])}
unused = set(args) - cited

print(f"{len(nodes)} nodes, {len(args)} arguments")
if orphans:
    print(f"unreachable from root: {', '.join(sorted(orphans))}")
if unused:
    print(f"arguments never cited: {', '.join(sorted(unused))}")
for p in problems:
    print(f"BROKEN  {p}")

if problems:
    sys.exit(1)
print("ok" if not (orphans or unused) else "no broken refs, but see above")
