#!/usr/bin/env python3
"""CivitAI public-API metadata lookup by file SHA256 (the HF LFS hash) and by model id.

Metadata only. No weights, no media downloads, no tokens. Resumable caches:
  data/raw/civitai_byhash.jsonl   one row per sha256 (found or not)
  data/raw/civitai_models.jsonl   one row per modelId (description, tags, stats)

Usage:
  python3 scripts/civit_lookup.py byhash [--limit N]
  python3 scripts/civit_lookup.py models
"""
from __future__ import annotations
import argparse, json, sys, threading, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
UA = "image-lora-kb/civit_lookup (metadata only; never downloads weights)"
LOCK = threading.Lock()
DEADLINE = 0.0  # epoch seconds; 0 = none

def get(url, retries=6):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            last = e
            time.sleep(2 + i * 3)
        except Exception as e:
            last = e
            time.sleep(1 + i * 2)
    raise RuntimeError(f"GET failed {url}: {last}")

def slim_version(d):
    imgs = []
    for im in (d.get("images") or [])[:6]:
        meta = im.get("meta") or {}
        imgs.append({
            "url": im.get("url"), "nsfwLevel": im.get("nsfwLevel"), "type": im.get("type"),
            "prompt": (meta.get("prompt") or "")[:1500], "negativePrompt": (meta.get("negativePrompt") or "")[:600],
            "steps": meta.get("steps"), "cfgScale": meta.get("cfgScale"), "sampler": meta.get("sampler"),
            "Model": meta.get("Model"), "resources": meta.get("resources"),
        })
    m = d.get("model") or {}
    st = d.get("stats") or {}
    return {
        "found": True, "versionId": d.get("id"), "modelId": d.get("modelId"), "versionName": d.get("name"),
        "baseModel": d.get("baseModel"), "baseModelType": d.get("baseModelType"),
        "trainedWords": d.get("trainedWords") or [], "publishedAt": d.get("publishedAt"),
        "versionDescription": (d.get("description") or "")[:1500],
        "downloadCount": st.get("downloadCount"), "thumbsUpCount": st.get("thumbsUpCount"),
        "modelName": m.get("name"), "type": m.get("type"), "nsfw": m.get("nsfw"), "poi": m.get("poi"),
        "images": imgs,
        "files": [{"name": f.get("name"), "sizeKB": f.get("sizeKB")} for f in (d.get("files") or [])][:3],
    }

def load_done(path, key):
    done = set()
    if path.exists():
        for ln in path.read_text().splitlines():
            if ln.strip():
                try:
                    done.add(json.loads(ln)[key])
                except Exception:
                    pass
    return done

def all_hashes():
    seen = {}
    for f in sorted((RAW / "hf").glob("*.jsonl")):
        for ln in f.read_text().splitlines():
            if not ln.strip():
                continue
            r = json.loads(ln)
            if r["path"].endswith((".safetensors", ".sft")) and r.get("sha256"):
                seen.setdefault(r["sha256"], r["path"])
    return seen

def run_byhash(limit=None, workers=5):
    out = RAW / "civitai_byhash.jsonl"
    done = load_done(out, "sha256")
    todo = [h for h in all_hashes() if h not in done]
    if limit:
        todo = todo[:limit]
    print(f"byhash: {len(todo)} to fetch ({len(done)} cached)", file=sys.stderr)
    n = [0]
    def work(h):
        if DEADLINE and time.time() > DEADLINE:
            return
        try:
            d = get(f"https://civitai.com/api/v1/model-versions/by-hash/{h}")
            row = {"sha256": h, **(slim_version(d) if d else {"found": False})}
        except Exception as e:
            print("ERR", h[:10], e, file=sys.stderr)
            return
        with LOCK:
            with out.open("a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n[0] += 1
            if n[0] % 250 == 0:
                print(f"  {n[0]}/{len(todo)}", file=sys.stderr)
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(work, todo))

def run_models(workers=5):
    out = RAW / "civitai_models.jsonl"
    done = load_done(out, "modelId")
    ids = set()
    for ln in (RAW / "civitai_byhash.jsonl").read_text().splitlines():
        try:
            r = json.loads(ln)
        except Exception:
            continue
        if r.get("found") and r.get("modelId") and is_scope(r.get("baseModel")):
            ids.add(r["modelId"])
    todo = sorted(ids - done)
    print(f"models: {len(todo)} to fetch ({len(done)} cached)", file=sys.stderr)
    n = [0]
    def work(mid):
        if DEADLINE and time.time() > DEADLINE:
            return
        try:
            d = get(f"https://civitai.com/api/v1/models/{mid}")
        except Exception as e:
            print("ERR", mid, e, file=sys.stderr); return
        if d is None:
            row = {"modelId": mid, "found": False}
        else:
            st = d.get("stats") or {}
            row = {"modelId": mid, "found": True, "name": d.get("name"), "type": d.get("type"),
                   "nsfw": d.get("nsfw"), "poi": d.get("poi"), "tags": d.get("tags") or [],
                   "description": (d.get("description") or "")[:4000],
                   "creator": (d.get("creator") or {}).get("username"),
                   "downloadCount": st.get("downloadCount"), "thumbsUpCount": st.get("thumbsUpCount"),
                   "versions": [{"id": v.get("id"), "name": v.get("name"), "baseModel": v.get("baseModel"),
                                 "trainedWords": v.get("trainedWords") or [], "downloadCount": (v.get("stats") or {}).get("downloadCount")}
                                for v in (d.get("modelVersions") or [])][:12]}
        with LOCK:
            with out.open("a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n[0] += 1
            if n[0] % 250 == 0:
                print(f"  {n[0]}/{len(todo)}", file=sys.stderr)
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(work, todo))

SCOPE_BASES = ("illustrious", "noobai", "anima", "krea", "moss")
def is_scope(b):
    b = (b or "").lower()
    return any(s in b for s in SCOPE_BASES)

def pending():
    done_h = load_done(RAW / "civitai_byhash.jsonl", "sha256")
    h = [x for x in all_hashes() if x not in done_h]
    ids = set()
    for ln in (RAW / "civitai_byhash.jsonl").read_text().splitlines() if (RAW / "civitai_byhash.jsonl").exists() else []:
        try:
            r = json.loads(ln)
        except Exception:
            continue
        if r.get("found") and r.get("modelId") and is_scope(r.get("baseModel")):
            ids.add(r["modelId"])
    done_m = load_done(RAW / "civitai_models.jsonl", "modelId")
    return {"byhash_pending": len(h), "models_pending": len(ids - done_m)}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["byhash", "models", "pending"])
    ap.add_argument("--limit", type=int)
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--deadline", type=float, default=0, help="epoch seconds after which no new requests start")
    a = ap.parse_args()
    DEADLINE = a.deadline
    if a.cmd == "pending":
        print(json.dumps(pending()))
    else:
        run_byhash(a.limit, a.workers) if a.cmd == "byhash" else run_models(a.workers)
