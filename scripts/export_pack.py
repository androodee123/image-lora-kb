#!/usr/bin/env python3
"""Build the share pack (default /workspace/share-image/): consolidated prompt-ready skill md, HOW-TO-USE.md,
catalog json/csv, candidates csv, and zips. Metadata only; never invents triggers/strengths; never downloads weights.
Usage: python3 scripts/export_pack.py [--out /workspace/share-image]"""
from __future__ import annotations
import argparse, csv, json, shutil, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIP_DT = (2026, 11, 14, 0, 0, 0)

def jl(p):
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()]

def zipdir(zpath, items):
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, path in items:
            zi = zipfile.ZipInfo(arc, ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, Path(path).read_bytes() if not isinstance(path, bytes) else path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/workspace/share-image")
    out = Path(ap.parse_args().out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    loras = [l for l in jl(ROOT / "data/loras.jsonl") if not l.get("duplicate_of")]
    cands = jl(ROOT / "data/candidates.jsonl")
    skill = (ROOT / "SKILL.md").read_text()
    stacks = (ROOT / "guides/andrew-proven-stacks.md").read_text()
    patterns = (ROOT / "guides/prompt-patterns.md").read_text()
    summary = (ROOT / "data/inventory_summary.md").read_text()
    consolidated = skill + "\n\n---\n\n" + stacks + "\n\n---\n\n" + patterns + "\n"
    (out / "image-lora-skill.md").write_text(consolidated)
    cols = ["slug", "family", "category", "nsfw", "availability", "reliability", "trigger_words", "strength", "downloads", "source_url", "description"]
    cat = [{"slug": l["slug"], "family": l["family"], "category": l["category"], "nsfw": l["nsfw"], "availability": l["availability"],
            "reliability": l["reliability"], "trigger_words": l["trigger_words"], "strength": l["strength"] or None, "downloads": l["downloads"],
            "source_url": l["source_url"], "description": (l.get("description") or "")[:200],
            "example_prompt": ((l.get("example") or {}).get("prompt") or "")[:400] or None, "example_image_url": (l.get("example") or {}).get("image_url")} for l in loras]
    (out / "catalog.json").write_text(json.dumps(cat, ensure_ascii=False))
    with (out / "catalog.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for c in cat:
            w.writerow([c[k] if k != "trigger_words" else " | ".join(c[k]) for k in cols])
    ccols = ["name", "family", "category", "nsfw", "downloads", "ingest_priority", "suggest_ingest", "suggest_reason", "trigger_words", "strength", "source_url", "other_version_on_graydient", "compat_note"]
    with (out / "candidates.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(ccols)
        for c in cands:
            w.writerow([(" | ".join(c[k]) if k == "trigger_words" else c.get(k)) for k in ccols])
    (out / "inventory_summary.md").write_text(summary)
    (out / "HOW-TO-USE.md").write_text("""# How to use the image LoRA KB (share pack)

**What it is:** a goal-based chooser for text-to-image LoRAs on Graydient (Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS). Adults-only.

## Quick start (any AI)
1. Give the AI `image-lora-skill.md` as a file / project knowledge / system prompt.
2. Optionally give `catalog.json` (or `catalog.csv`) so it can look up any LoRA by slug, family, category.
3. Ask: "Pick LoRAs for <goal> on <family> and write the Graydient command."

## Rules the AI follows
- Recommend only LoRAs *on Graydient*. Other-HF-repo LoRAs are flagged "needs adding".
- Never invents triggers/strengths: unknown fields say "not stated".
- "Suggest ingest" lines are proposals only (max 3 per recipe). Nothing auto-downloads or ingests.

## Files
- `image-lora-skill.md` - consolidated skill (recipes + stacking + Andrew's proven stacks).
- `catalog.json` / `catalog.csv` - every available LoRA (non-duplicate): slug, family, category, triggers, strength, source link, example prompt.
- `candidates.csv` - CivitAI LoRAs not yet available, ranked by `ingest_priority`.
- `inventory_summary.md` - per-family counts and exclusions.
- `image-lora-kb-skill.zip` - Claude Agent Skill layout (SKILL.md + reference/).
- `image-lora-kb-share-pack.zip` - everything above.

The private GitHub repo `androodee123/image-lora-kb` is the live source; this pack is a snapshot.
""")
    skill_items = [("image-lora-kb/SKILL.md", ROOT / "SKILL.md"), ("image-lora-kb/reference/andrew-proven-stacks.md", ROOT / "guides/andrew-proven-stacks.md"),
                   ("image-lora-kb/reference/prompt-patterns.md", ROOT / "guides/prompt-patterns.md"), ("image-lora-kb/reference/recipes-detailed.md", ROOT / "guides/recipes-detailed.md"),
                   ("image-lora-kb/reference/catalog.json", out / "catalog.json")]
    for fam in sorted((ROOT / "families").iterdir()):
        for p in sorted(fam.glob("*.md")):
            skill_items.append((f"image-lora-kb/reference/families/{fam.name}/{p.name}", p))
    zipdir(out / "image-lora-kb-skill.zip", skill_items)
    share_items = [(p.name, p) for p in out.iterdir() if p.suffix != ".zip"] + [("image-lora-kb-skill.zip", out / "image-lora-kb-skill.zip")]
    zipdir(out / "image-lora-kb-share-pack.zip", share_items)
    for p in sorted(out.iterdir()):
        print(f"{p.stat().st_size:>10}  {p}")

if __name__ == "__main__":
    main()
