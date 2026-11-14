#!/usr/bin/env python3
"""Harvest CivitAI *metadata* for text-to-image LoRA candidates (Illustrious/NoobAI, Anima,
Krea 2, MOSS Image, SDXL, Pony). NEVER downloads weights or media.

Writes data/raw/civitai_candidates.jsonl (slim, one row per model, versions merged).
Resumable via data/raw/harvest_state.json (cursor per family+sort).

Usage:
  python3 scripts/harvest.py                 # full default harvest
  python3 scripts/harvest.py --newest-only   # weekly: newest pages only (used by check_new.py)
"""
from __future__ import annotations
import argparse, json, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = RAW / "civitai_candidates.jsonl"
STATE = RAW / "harvest_state.json"
API = "https://civitai.com/api/v1/models"
UA = "image-lora-kb/harvest.py (metadata only; never download weights)"

# family -> {civitai baseModel string: {sort: max_pages}}
PLAN = {
    "illustrious": {"Illustrious": {"Most Downloaded": 25, "Highest Rated": 8, "Newest": 10},
                    "NoobAI": {"Most Downloaded": 10, "Highest Rated": 4, "Newest": 5}},
    "anima":       {"Anima": {"Most Downloaded": 15, "Highest Rated": 5, "Newest": 10}},
    "krea2":       {"Krea 2": {"Most Downloaded": 15, "Highest Rated": 5, "Newest": 10},
                    "Flux.1 Krea": {"Most Downloaded": 4, "Newest": 2}},
    "moss":        {"MOSS Image": {"Most Downloaded": 10, "Highest Rated": 3, "Newest": 5}},
    "sdxl":        {"SDXL 1.0": {"Most Downloaded": 15, "Highest Rated": 5, "Newest": 3}},
    "pony":        {"Pony": {"Most Downloaded": 15, "Highest Rated": 5, "Newest": 3},
                    "Pony V7": {"Most Downloaded": 2, "Newest": 2}},
}

def get(url, retries=6):
    last = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last = e
            time.sleep(3 + i * 4)
        except Exception as e:
            last = e
            time.sleep(2 + i * 2)
    raise RuntimeError(f"GET failed {url}: {last}")

def slim(it, family):
    vers = []
    for v in (it.get("modelVersions") or []):
        imgs = []
        for im in (v.get("images") or [])[:3]:
            meta = im.get("meta") or {}
            imgs.append({"url": im.get("url"), "nsfwLevel": im.get("nsfwLevel"),
                         "prompt": (meta.get("prompt") or "")[:1200], "negativePrompt": (meta.get("negativePrompt") or "")[:400],
                         "steps": meta.get("steps"), "cfgScale": meta.get("cfgScale"), "sampler": meta.get("sampler")})
        vers.append({"id": v.get("id"), "name": v.get("name"), "baseModel": v.get("baseModel"),
                     "trainedWords": v.get("trainedWords") or [], "publishedAt": v.get("publishedAt"),
                     "downloadCount": (v.get("stats") or {}).get("downloadCount"),
                     "sha256": [((f.get("hashes") or {}).get("SHA256") or "").lower() for f in (v.get("files") or []) if (f.get("hashes") or {}).get("SHA256")],
                     "images": imgs})
    st = it.get("stats") or {}
    return {"id": it["id"], "family_hint": family, "name": it.get("name"), "type": it.get("type"), "nsfw": it.get("nsfw"),
            "poi": it.get("poi"), "tags": it.get("tags") or [], "creator": (it.get("creator") or {}).get("username"),
            "downloadCount": st.get("downloadCount"), "thumbsUpCount": st.get("thumbsUpCount"),
            "description": (it.get("description") or "")[:2000], "versions": vers[:6]}

def merge_newest(pages: int, delay: float, deadline: float = 0):
    """Incremental: fetch the newest `pages` pages per baseModel and MERGE into civitai_candidates.jsonl."""
    models = {}
    for ln in OUT.read_text().split("\n") if OUT.exists() else []:
        try:
            r = json.loads(ln); models[r["id"]] = r
        except Exception:
            pass
    added = 0
    for family, bases in PLAN.items():
        for bm in bases:
            cursor = None
            for _ in range(pages):
                if deadline and time.time() > deadline:
                    print("deadline reached", file=sys.stderr); break
                params = [("limit", 100), ("nsfw", "true"), ("sort", "Newest"), ("types", "LORA"), ("types", "LoCon"), ("types", "DoRA"), ("baseModels", bm)]
                if cursor:
                    params.append(("cursor", cursor))
                d = get(API + "?" + urllib.parse.urlencode(params))
                for it in d.get("items") or []:
                    r = slim(it, family)
                    old = models.get(r["id"])
                    if old:
                        have = {v["id"] for v in old["versions"]}
                        old["versions"] += [v for v in r["versions"] if v["id"] not in have]
                        old["downloadCount"] = max(old.get("downloadCount") or 0, r["downloadCount"] or 0)
                        old["thumbsUpCount"] = max(old.get("thumbsUpCount") or 0, r["thumbsUpCount"] or 0)
                    else:
                        models[r["id"]] = r; added += 1
                cursor = (d.get("metadata") or {}).get("nextCursor")
                time.sleep(delay)
                if not (d.get("items") and cursor):
                    break
    OUT.write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in models.values()) + "\n")
    print(json.dumps({"models_total": len(models), "models_added": added}))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merge-newest", type=int, metavar="PAGES", help="incremental: newest PAGES per baseModel merged into the candidate cache")
    ap.add_argument("--full", action="store_true", help="re-run the full multi-sort harvest (resets paging state; merges into existing cache)")
    ap.add_argument("--deadline", type=float, default=0)
    ap.add_argument("--newest-only", action="store_true")
    ap.add_argument("--delay", type=float, default=0.6)
    a = ap.parse_args()
    if a.merge_newest:
        merge_newest(a.merge_newest, a.delay, a.deadline)
        return
    if a.full and STATE.exists():
        STATE.unlink()
    state = json.loads(STATE.read_text()) if STATE.exists() and not a.newest_only else {}
    models = {}
    if OUT.exists() and not a.newest_only:
        for ln in OUT.read_text().split("\n"):
            r = json.loads(ln); models[r["id"]] = r
    for family, bases in PLAN.items():
        for bm, sorts in bases.items():
            for sort, maxp in sorts.items():
                if a.newest_only and sort != "Newest":
                    continue
                key = f"{family}|{bm}|{sort}"
                if state.get(key) == "done":
                    continue
                cursor = state.get(key + "|cursor")
                pages = state.get(key + "|pages", 0)
                while pages < (2 if a.newest_only else maxp) and not (a.deadline and time.time() > a.deadline):
                    params = [("limit", 100), ("nsfw", "true"), ("sort", sort), ("types", "LORA"), ("types", "LoCon"), ("types", "DoRA"), ("baseModels", bm)]
                    if cursor:
                        params.append(("cursor", cursor))
                    d = get(API + "?" + urllib.parse.urlencode(params))
                    for it in d.get("items") or []:
                        r = slim(it, family)
                        old = models.get(r["id"])
                        if old:  # union versions
                            have = {v["id"] for v in old["versions"]}
                            old["versions"] += [v for v in r["versions"] if v["id"] not in have]
                            old["downloadCount"] = max(old.get("downloadCount") or 0, r["downloadCount"] or 0)
                        else:
                            models[r["id"]] = r
                    pages += 1
                    cursor = (d.get("metadata") or {}).get("nextCursor")
                    state[key + "|cursor"], state[key + "|pages"] = cursor, pages
                    time.sleep(a.delay)
                    if not (d.get("items") and cursor):
                        break
                state[key] = "done"
                print(f"{key}: pages={pages} total_models={len(models)}", file=sys.stderr)
                if not a.newest_only:
                    STATE.write_text(json.dumps(state))
                    OUT.write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in models.values()) + "\n")
    out = OUT if not a.newest_only else RAW / "civitai_newest.jsonl"
    out.write_text("\n".join(json.dumps(m, ensure_ascii=False) for m in models.values()) + "\n")
    print(f"wrote {len(models)} models -> {out}", file=sys.stderr)

if __name__ == "__main__":
    main()
