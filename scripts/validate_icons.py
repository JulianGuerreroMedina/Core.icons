#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "style_icons.css"
MANIFEST = ROOT / "manifest.json"

errors = []
css_text = CSS.read_text(encoding="utf-8")
refs = [p.strip().strip("\"'") for p in re.findall(r"url\(([^)]+)\)", css_text)]
for ref in refs:
    if not (ROOT / ref).exists():
        errors.append(f"Missing asset referenced by CSS: {ref}")

class_names = re.findall(r"\.([a-zA-Z0-9_-]+)\s*\{", css_text)
seen = set()
for name in class_names:
    if name in seen:
        errors.append(f"Duplicate class in CSS: {name}")
    seen.add(name)

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
for item in manifest.get("items", []):
    asset = item.get("asset", "")
    if not (ROOT / asset).exists():
        errors.append(f"Manifest points to missing asset: {asset}")

if errors:
    print("Validation failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print(f"OK: {len(refs)} CSS refs, {len(seen)} unique classes, {len(manifest.get('items', []))} manifest entries")
