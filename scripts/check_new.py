#!/usr/bin/env python3
"""Weekly monitor: propose new T2I LoRAs and KB updates. NEVER downloads weights, NEVER ingests.

1. New on Graydient / HF: re-lists every Octavian123 HF repo (read-only metadata) and diffs against the
   previous listing in data/raw/hf -> files added/removed (KB needs `build_kb.py` + `render_kb.py`).
2. New on CivitAI: harvests the newest pages for Illustrious/NoobAI, Anima, Krea 2, MOSS Image, SDXL, Pony and
   proposes LoRAs that are in neither data/loras.jsonl nor data/candidates.jsonl (ranked by early traction).
   Minor-coded names/tags and forbidden identities are skipped.
Writes proposals/YYYY-MM-DD.md. Exit code 0 always when the report is written.

Usage:  python3 scripts/check_new.py [--no-hf] [--no-civitai] [--min-downloads 50]
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from t2i_lora import family_from_base, minor_reason, categorize, FAMILY_LABEL

ROOT = Path(__file__).resolve().parents[1]
RAW, DATA, PROP = ROOT / "data" / "raw", ROOT / "data", ROOT / "proposals"

def jl(p):
    out = []
    if p.exists():
        for l in p.read_text().split("\n"):
            try:
                out.append(json.loads(l))
            except Exception:
                pass
    return out

def hf_paths():
    s = set()
    for f in (RAW / "hf").glob("*.jsonl"):
        for r in jl(f):
            if r["path"].lower().endswith((".safetensors", ".sft")):
                s.add(f"{r['repo']}/{r['path']}")
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-hf", action="store_true")
    ap.add_argument("--no-civitai", action="store_true")
    ap.add_argument("--min-downloads", type=int, default=50)
    a = ap.parse_args()
    today = datetime.now().strftime("%Y-%m-%d")
    PROP.mkdir(exist_ok=True)
    L = [f"# T2I LoRA KB proposals — {today}", "", "Proposals only. Nothing was downloaded or ingested. Andrew decides; ingest runs only when he asks (civit-to-graydient).", ""]

    # 1. HF / Graydient diff
    if not a.no_hf:
        before = hf_paths()
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "list_graydient.py")], capture_output=True, text=True)
        after = hf_paths()
        if r.returncode != 0 or not after:
            L += ["## HF listing", "", f"Could not re-list HF repos (exit {r.returncode}); skipped. {r.stderr.strip()[-200:]}", ""]
        else:
            added, removed = sorted(after - before), sorted(before - after)
            L += ["## New or removed weight files in Octavian123 HF repos", "", f"{len(added)} added, {len(removed)} removed since the last snapshot.", ""]
            by_repo = defaultdict(list)
            for p in added:
                by_repo[p.rsplit("/", 1)[0] if p.count("/") > 1 else p].append(p)
            for p in added[:200]:
                gr = p.startswith(("Octavian123/civit/", "Octavian123/civit2/", "Octavian123/private/"))
                L.append(f"- `{p}` — {'on Graydient repo' if gr else 'other HF repo, NOT on Graydient (needs adding)'}")
            for p in removed[:50]:
                L.append(f"- removed: `{p}`")
            if added or removed:
                L += ["", "Action: `python3 scripts/civit_lookup.py byhash && python3 scripts/build_kb.py && python3 scripts/render_kb.py` (then review the diff and push).", ""]

    # 2. CivitAI newest
    if not a.no_civitai:
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "harvest.py"), "--newest-only"], capture_output=True, text=True)
        newest = jl(RAW / "civitai_newest.jsonl")
        known = {x.get("civitai_model_id") for x in jl(DATA / "loras.jsonl")} | {x.get("civitai_model_id") for x in jl(DATA / "candidates.jsonl")}
        hfsha = set()
        for f in (RAW / "hf").glob("*.jsonl"):
            hfsha |= {x.get("sha256") for x in jl(f) if x.get("sha256")}
        new = []
        for c in newest:
            if c["id"] in known:
                continue
            fam = next((family_from_base(v.get("baseModel")) for v in c.get("versions", []) if family_from_base(v.get("baseModel"))), None)
            if not fam or {h for v in c["versions"] for h in v.get("sha256", [])} & hfsha:
                continue
            tw = next((v.get("trainedWords") for v in c["versions"] if v.get("trainedWords")), [])
            if minor_reason(c["name"], " ".join(c.get("tags") or []), " ".join(tw or [])):
                continue
            if (c.get("downloadCount") or 0) < a.min_downloads:
                continue
            new.append((fam, c, tw))
        new.sort(key=lambda x: -(x[1].get("downloadCount") or 0))
        L += ["## New CivitAI LoRAs not yet in the KB", "", f"{len(new)} new models (>= {a.min_downloads} downloads) from the newest pages.", ""]
        per = Counter()
        for fam, c, tw in new:
            if per[fam] >= 15:
                continue
            per[fam] += 1
            cat = categorize(c["name"], c.get("tags"))
            L.append(f"- [{c['name'][:80]}](https://civitai.com/models/{c['id']}) — {FAMILY_LABEL[fam]} · {cat} · {c.get('downloadCount') or 0} dl · triggers: {', '.join(tw[:4]) if tw else 'not stated'}" + (" · real-person likeness (POI)" if c.get("poi") else ""))
        L += ["", "To fold these into the KB as candidates run `python3 scripts/harvest.py && python3 scripts/build_kb.py && python3 scripts/render_kb.py`.", ""]
    out = PROP / f"{today}.md"
    out.write_text("\n".join(L) + "\n")
    print(out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
