#!/usr/bin/env python3
"""Build the T2I LoRA KB data from metadata caches. Never downloads weights.

Inputs  (data/raw/): hf/*.jsonl (all Octavian123 repos), civitai_byhash.jsonl, civitai_models.jsonl,
                     civitai_candidates.jsonl, legacy_enriched.jsonl (ai-ops-portal 2026-09-09 enrichment)
Outputs (data/):     inventory.jsonl (every weight file + classification), loras.jsonl (available),
                     excluded.jsonl, candidates.jsonl, inventory_summary.md, accessibility_report.md,
                     graydient_ingest_queue.{md,txt}, graydient_slugs.json
"""
from __future__ import annotations
import html, json, math, re, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from t2i_lora import *  # noqa

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
WEIGHT_EXT = (".safetensors", ".sft")

def jl(path):
    if not path.exists():
        return []
    out = []
    for l in path.read_text().split("\n"):
        if l.strip():
            try:
                out.append(json.loads(l))
            except Exception:
                pass  # tolerate a truncated line from an interrupted fetch
    return out

def strip_html(s: str) -> str:
    s = re.sub(r"<(br|/p|/li|/h\d)[^>]*>", "\n", s or "", flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", s)).strip()

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())

def load_inputs():
    hf = []
    for f in sorted((RAW / "hf").glob("*.jsonl")):
        hf += jl(f)
    byhash = {r["sha256"]: r for r in jl(RAW / "civitai_byhash.jsonl")}
    models = {r["modelId"]: r for r in jl(RAW / "civitai_models.jsonl") if r.get("found")}
    legacy = {}
    legacy_rows = jl(RAW / "legacy_enriched.jsonl")
    if not legacy_rows and (DATA / "legacy_enriched.jsonl.gz").exists():
        import gzip
        legacy_rows = [json.loads(l) for l in gzip.open(DATA / "legacy_enriched.jsonl.gz", "rt").read().split("\n") if l.strip()]
    for r in legacy_rows:
        legacy[r["slug"]] = r
        legacy.setdefault(norm(r["slug"]), r)
    return hf, byhash, models, legacy

def classify_files(hf, byhash, legacy):
    """Return (rows, excluded) one row per distinct slug (merged across repos)."""
    rows, excluded = {}, []
    ignored = Counter()
    # 1. per-file facts
    files = []
    for r in hf:
        p = r["path"]
        if not p.lower().endswith(WEIGHT_EXT):
            if p.lower().endswith((".zip", ".download.zip")) or ".safetensors" in p.lower():
                excluded.append({"slug": Path(p).name, "repo": r["repo"], "path": p, "reason": "not a plain weight file (zip/partial download)", "family": None})
            else:
                ignored[Path(p).suffix or "(none)"] += 1
            continue
        stem = re.sub(r"\.(safetensors|sft)$", "", Path(p).name, flags=re.I)
        files.append({**r, "stem": stem, "on_graydient": r["repo"] in GRAYDIENT_REPOS})
    # trailing "-NN" numeric epochs in the user's own (non-Graydient) repos
    prefix_count = Counter()
    for f in files:
        m = re.match(r"^(.*?)[-_ ](\d{1,2})$", f["stem"])
        if m and not f["on_graydient"]:
            prefix_count[(f["repo"], m.group(1).lower())] += 1
    # epoch groups (only for files NOT found on CivitAI by hash)
    groups = defaultdict(list)
    for f in files:
        civ = byhash.get(f.get("sha256") or "", {})
        f["civ"] = civ if civ.get("found") else None
        g, ep = epoch_group(f["stem"])
        m = re.match(r"^(.*?)[-_ ](\d{1,2})$", f["stem"])
        if g is None and m and not f["on_graydient"] and prefix_count[(f["repo"], m.group(1).lower())] >= 2:
            g, ep = m.group(1), int(m.group(2))
        f["epoch_group"], f["epoch"] = (g, ep) if (g and not f["civ"]) else (None, None)
        if f["epoch_group"] is not None:
            groups[(f["repo"] if not f["on_graydient"] else "GRAYDIENT", f["epoch_group"].lower())].append(f)
    plain_stems = {(("GRAYDIENT" if f["on_graydient"] else f["repo"]), f["stem"].lower()) for f in files if f["epoch_group"] is None}
    keep, dropped_ep = [], set()
    for f in files:
        if f["epoch_group"] is None:
            keep.append(f); continue
        key = ("GRAYDIENT" if f["on_graydient"] else f["repo"], f["epoch_group"].lower())
        members = groups[key]
        top = max(members, key=lambda x: x["epoch"])
        if key in plain_stems or any(k[1] == key[1] for k in plain_stems if k[0] == key[0]):
            excluded.append({"slug": f["stem"], "repo": f["repo"], "path": f["path"], "reason": "intermediate training epoch (final file exists)", "family": None}); continue
        if f is top:
            f["epoch_only"] = True
            f["epoch_variants"] = len(members)
            keep.append(f)
        else:
            excluded.append({"slug": f["stem"], "repo": f["repo"], "path": f["path"], "reason": f"intermediate training epoch (kept highest epoch {top['stem']})", "family": None})
    # 2. classify each kept file
    for f in keep:
        stem, civ = f["stem"], f["civ"]
        leg = legacy.get(stem) or legacy.get(norm(stem))
        fam, fam_src, oos = None, None, None
        if civ:
            fam = family_from_base(civ.get("baseModel"))
            fam_src = "civitai-hash"
            if not fam:
                oos = civ.get("baseModel") or "unknown base"
        if not fam and not oos:
            nfam, noos = family_from_name(stem + " " + (f["path"].split("/")[0] if "/" in f["path"] else ""))
            if nfam:
                fam, fam_src = nfam, "filename"
            elif noos:
                oos = noos
        if not fam and not oos and leg and leg.get("family"):
            fam, fam_src = leg["family"], "legacy-enrichment"
        if not fam and not oos and re.search(r"(?:^|[-_ ])xl(?:[-_ ]|$)", stem.lower()):
            fam, fam_src = "illustrious", "filename (-xl suffix convention = Illustrious on Graydient; UNVERIFIED, no CivitAI hash match)"
        # repo hints (small user repos): file-name tokens failed; use repo-level name for sdxl/ill
        f["family"], f["family_source"], f["oos"] = fam, fam_src, oos
        if f["size"] == 0:
            excluded.append({"slug": stem, "repo": f["repo"], "path": f["path"], "reason": "zero-byte placeholder", "family": fam}); continue
        if f["repo"] == "Octavian123/base" or (f["size"] or 0) > 1_500_000_000:
            excluded.append({"slug": stem, "repo": f["repo"], "path": f["path"], "reason": "checkpoint, not a LoRA", "family": fam}); continue
        if f["repo"] in ("Octavian123/video",) or (oos and oos.lower() not in ("unknown base",)) :
            excluded.append({"slug": stem, "repo": f["repo"], "path": f["path"], "reason": f"out of scope (base/family: {oos or 'video'})", "family": None}); continue
        mr = minor_reason(stem, (civ or {}).get("modelName") or "", " ".join((civ or {}).get("trainedWords") or []), (leg or {}).get("name") or "", (leg or {}).get("description", "")[:600] if not civ else "")
        if mr:
            excluded.append({"slug": stem, "repo": f["repo"], "path": f["path"], "reason": mr, "family": fam}); continue
        slug = stem
        row = rows.setdefault(slug.lower() if f["on_graydient"] else f"{f['repo']}::{slug}".lower(), {
            "slug": slug, "family": fam, "family_source": fam_src, "files": [], "civ": civ, "leg": leg,
            "epoch_only": f.get("epoch_only", False), "epoch_variants": f.get("epoch_variants", 1)})
        row["files"].append({"repo": f["repo"], "path": f["path"], "size": f["size"], "sha256": f.get("sha256"), "on_graydient": f["on_graydient"]})
        if civ and not row["civ"]:
            row["civ"] = civ
    return rows, excluded, ignored, len(files)

def build_lora_row(r, models):
    civ, leg = r["civ"], r["leg"] or {}
    files = r["files"]
    on_g = any(x["on_graydient"] for x in files)
    mid = (civ or {}).get("modelId") or leg.get("model_id")
    vid = (civ or {}).get("versionId") or leg.get("model_version_id")
    m = models.get(mid, {})
    name = (civ or {}).get("modelName") or m.get("name") or leg.get("name") or r["slug"]
    tags = m.get("tags") or leg.get("tags") or []
    desc_full = strip_html(m.get("description") or "") or strip_html((civ or {}).get("versionDescription") or "") or leg.get("description") or ""
    trig = list((civ or {}).get("trainedWords") or [])
    trig_src = "civitai version trainedWords" if trig else ""
    if not trig and leg.get("trained_words"):
        trig, trig_src = list(leg["trained_words"]), "ai-ops-portal enrichment (CivitAI trainedWords, 2026-09-09)"
    if not trig and leg.get("trigger"):
        trig, trig_src = [leg["trigger"]], "ai-ops-portal enrichment (2026-09-09)"
    strength = extract_strength((civ or {}).get("versionDescription"), strip_html(m.get("description") or ""), leg.get("description"))
    ex = None
    for im in (civ or {}).get("images") or []:
        if im.get("prompt"):
            ex = {"prompt": im["prompt"], "negative": im.get("negativePrompt") or "", "steps": im.get("steps"), "cfg": im.get("cfgScale"),
                  "sampler": im.get("sampler"), "image_url": im.get("url"), "source": "CivitAI example image metadata"}
            break
    if not ex:
        for im in (civ or {}).get("images") or []:
            if im.get("url"):
                ex = {"prompt": "", "image_url": im["url"], "source": "CivitAI example image (no prompt metadata)"}
                break
    if (not ex or not ex.get("prompt")) and leg.get("example_prompts"):
        ex = {"prompt": leg["example_prompts"][0], "image_url": (ex or {}).get("image_url"), "source": f"ai-ops-portal enrichment ({leg.get('prompt_source') or leg.get('fetch_source') or 'CivitAI'})"}
    url = f"https://civitai.com/models/{mid}" + (f"?modelVersionId={vid}" if vid else "") if mid else (leg.get("source_url") or "")
    fam = r["family"]
    cat = categorize(name + " " + r["slug"], tags, desc_full)
    nsfw = bool((civ or {}).get("nsfw")) or (m.get("nsfw") is True) or cat == "nsfw-act" or "nsfw" in [t.lower() for t in tags]
    if on_g:
        avail = "on Graydient"
        needs_add = False
    else:
        repos = sorted({x["repo"].split("/")[1] for x in files})
        avail = f"in HF repo {', '.join(repos)}, not on Graydient"
        needs_add = True
    return {
        "slug": r["slug"], "family": fam, "category": cat, "nsfw": nsfw, "availability": avail,
        "graydient": on_g, "needs_graydient_add": needs_add,
        "graydient_status": "on Graydient" if on_g else "needs adding to Graydient (file only in HF repo; ingest needs local-file/HF-URL path)",
        "hf_files": [{"repo": x["repo"], "path": x["path"], "size": x["size"]} for x in files],
        "name": name, "source_url": url, "civitai_model_id": mid, "civitai_version_id": vid,
        "civitai_version_name": (civ or {}).get("versionName"), "base_model": (civ or {}).get("baseModel"),
        "creator": m.get("creator"), "tags": tags[:12], "poi": (civ or {}).get("poi") or m.get("poi"),
        "downloads": (civ or {}).get("downloadCount") or m.get("downloadCount"), "thumbs_up": (civ or {}).get("thumbsUpCount") or m.get("thumbsUpCount"),
        "published_at": (civ or {}).get("publishedAt"),
        "trigger_words": trig, "trigger_source": trig_src or "unknown (not stated by source)",
        "strength": strength, "strength_source": "stated in source description" if strength else "unknown (not stated by source)",
        "description": (desc_full[:420] + ("…" if len(desc_full) > 420 else "")) if desc_full else "",
        "example": ex, "family_source": r["family_source"], "epoch_only": r["epoch_only"],
        "_sha": files[0].get("sha256"), "source_confirmed": bool(civ), "metadata_source": "civitai-hash" if civ else ("legacy-enrichment" if leg else "filename-only"),
    }

HARD_RE = re.compile(r"\b(loli(?!ta)\w*|shota(?!ro)\w*|underage|under[- ]age|preteen|pre[- ]teen)\b", re.I)

def main():
    hf, byhash, models, legacy = load_inputs()
    rows, excluded, ignored, nfiles = classify_files(hf, byhash, legacy)
    loras, unclassified = [], []
    g_sha = {f["sha256"] for r in rows.values() for f in r["files"] if f["on_graydient"] and f["sha256"]}
    for r in rows.values():
        if not any(f["on_graydient"] for f in r["files"]) and any(f["sha256"] in g_sha for f in r["files"] if f["sha256"]):
            for f in r["files"]:
                f["on_graydient"] = True  # identical file already on Graydient under another name
                f["same_file_as_graydient"] = True
        civ = r["civ"] or {}
        m = models.get(civ.get("modelId"), {})
        hard = HARD_RE.search(strip_html(m.get("description") or "")[:1500]) if m else None
        mr = minor_reason(" ".join(m.get("tags") or []))  # description-only terms are flagged (minor_coded), not excluded
        if mr:
            excluded.append({"slug": r["slug"], "repo": r["files"][0]["repo"], "path": r["files"][0]["path"], "reason": mr, "family": r["family"]})
            continue
        if not r["family"]:
            unclassified.append({"slug": r["slug"], "reason": "family could not be determined (no CivitAI hash match, no family token in name, no legacy record)",
                                 "repos": sorted({f["repo"] for f in r["files"]}), "path": r["files"][0]["path"]})
            continue
        loras.append(build_lora_row(r, models))
    have = {l["slug"].lower() for l in loras}
    for mrow in json.loads((DATA / "manual_concepts.json").read_text()) if (DATA / "manual_concepts.json").exists() else []:
        if mrow["slug"].lower() in have:
            for l in loras:
                if l["slug"].lower() == mrow["slug"].lower():
                    l["trigger_words"] = l["trigger_words"] or mrow["trigger_words"]
            continue
        loras.append({"slug": mrow["slug"], "family": mrow["family"], "category": mrow["category"], "nsfw": True, "availability": "on Graydient",
            "graydient": True, "needs_graydient_add": False, "graydient_status": "on Graydient (private concept; listed in owner skill catalog, file name differs from slug)",
            "hf_files": [], "name": mrow["slug"], "source_url": "", "civitai_model_id": None, "civitai_version_id": None, "civitai_version_name": None,
            "base_model": None, "creator": "Andrew (private)", "tags": ["private"], "poi": None, "downloads": None, "thumbs_up": None, "published_at": None,
            "trigger_words": mrow["trigger_words"], "trigger_source": mrow["source"], "strength": mrow["strength"],
            "strength_source": mrow["strength_note"] if mrow["strength"] else "unknown (not stated by source)", "description": "Andrew's private LoRA (identity/style/anatomy helper).",
            "example": None, "family_source": "owner skill catalog", "epoch_only": False, "source_confirmed": False, "metadata_source": "owner-skill-catalog", "private": True})
    loras.sort(key=lambda x: (x["family"], x["category"], -(x["downloads"] or 0), x["slug"]))
    annotate(loras)
    (DATA / "loras.jsonl").write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in loras) + "\n")
    (DATA / "unclassified.jsonl").write_text("\n".join(json.dumps(u, ensure_ascii=False) for u in unclassified) + "\n")
    for e in excluded:
        e.setdefault("family", None)
    (DATA / "excluded.jsonl").write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in excluded) + "\n")
    cand_counts = build_candidates(loras, byhash, models, excluded)
    (DATA / "excluded.jsonl").write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in excluded) + "\n")
    write_summary(loras, excluded, unclassified, ignored, nfiles, hf, cand_counts)
    print(f"loras={len(loras)} excluded={len(excluded)} unclassified={len(unclassified)} files={nfiles}", file=sys.stderr)

def annotate(loras):
    """duplicate_of (same sha under several slugs) + reliability flag."""
    by_sha = defaultdict(list)
    for l in loras:
        sha = next((f.get("sha256") for f in [] ), None)
    # sha is stored per hf file in build_lora_row via _sha
    for l in loras:
        if l.get("_sha"):
            by_sha[l["_sha"]].append(l)
    for sha, grp in by_sha.items():
        grp.sort(key=lambda x: (not x["graydient"], x.get("epoch_only", False), len(x["slug"]), x["slug"]))
        for dup in grp[1:]:
            dup["duplicate_of"] = grp[0]["slug"]
    for l in loras:
        if l.get("private") and l["metadata_source"] == "owner-skill-catalog":
            l["reliability"] = "manual-unverified"
        elif l.get("epoch_only"):
            l["reliability"] = "epoch-only"
        elif "UNVERIFIED" in (l.get("family_source") or ""):
            l["reliability"] = "family-guess"
        elif l["source_confirmed"]:
            l["reliability"] = "verified"
        else:
            l["reliability"] = "name-only"
        l["recipe_eligible"] = l["reliability"] in ("verified", "name-only") and not l.get("duplicate_of") and bool(l["trigger_words"] or l["reliability"] == "verified")
        l.pop("_sha", None)

CAND_CAP = {}
def build_candidates(loras, byhash, models, excluded):
    cands_raw = jl(RAW / "civitai_candidates.jsonl")
    avail_sha, avail_mid = set(), {}
    for l in loras:
        for f in l["hf_files"]:
            pass
    sha_rows = {}
    for r in jl(RAW / "civitai_byhash.jsonl"):
        if r.get("found"):
            sha_rows[r["sha256"]] = r
    for l in loras:
        for f in l["hf_files"]:
            pass
    # available sha / model ids come from the hf listing via byhash
    hf_sha = set()
    for fpath in (RAW / "hf").glob("*.jsonl"):
        for r in jl(fpath):
            if r.get("sha256") and r["path"].lower().endswith(WEIGHT_EXT):
                hf_sha.add(r["sha256"])
    g_mid = {l["civitai_model_id"] for l in loras if l.get("civitai_model_id") and l["graydient"]}
    o_mid = {l["civitai_model_id"] for l in loras if l.get("civitai_model_id") and not l["graydient"]}
    # best available downloads per family+category (Graydient, verified, non-duplicate)
    best = defaultdict(int)
    have_util_kw = defaultdict(set)
    for l in loras:
        if l["graydient"] and not l.get("duplicate_of") and l["downloads"]:
            best[(l["family"], l["category"])] = max(best[(l["family"], l["category"])], l["downloads"])
        if l["graydient"] and l["category"] == "utility":
            for kw in ("turbo", "lightning", "distill", "hyper", "lightx2v", "accelerat"):
                if kw in (l["slug"] + " " + l["name"]).lower():
                    have_util_kw[l["family"]].add(kw)
    cnt_cat = Counter((l["family"], l["category"]) for l in loras if l["graydient"] and not l.get("duplicate_of"))
    out = []
    for c in cands_raw:
        vers = c.get("versions") or []
        fam = None
        base = None
        for v in vers:
            fam = family_from_base(v.get("baseModel")); base = v.get("baseModel")
            if fam:
                break
        if not fam:
            continue
        shas = {h for v in vers for h in v.get("sha256", [])}
        if shas & hf_sha:
            continue  # exact file already available
        tw = []
        for v in vers:
            if family_from_base(v.get("baseModel")) == fam:
                tw = v.get("trainedWords") or []
                if tw:
                    break
        mr = minor_reason(c["name"], " ".join(c.get("tags") or []), " ".join(tw))
        hard = HARD_RE.search(strip_html(c.get("description") or "")[:1500])
        if mr:
            excluded.append({"slug": f"civitai:{c['id']}", "repo": "candidate", "path": c["name"], "reason": mr, "family": fam})
            continue
        cat = categorize(c["name"], c.get("tags"), strip_html(c.get("description") or ""))
        dl = c.get("downloadCount") or 0
        desc = strip_html(c.get("description") or "")
        ex = None
        for v in vers:
            for im in v.get("images") or []:
                if im.get("prompt"):
                    ex = {"prompt": im["prompt"], "negative": im.get("negativePrompt") or "", "steps": im.get("steps"), "cfg": im.get("cfgScale"), "sampler": im.get("sampler"), "image_url": im.get("url"), "source": "CivitAI example image metadata"}
                    break
            if ex:
                break
        compat = "Flux.1 Krea base - verify compatibility with detailed-krea2 before ingest" if base and base.lower().startswith("flux.1") else ""
        row = {"civitai_model_id": c["id"], "name": c["name"], "family": fam, "category": cat, "nsfw": bool(c.get("nsfw")) or cat == "nsfw-act",
               "base_model": base, "source_url": f"https://civitai.com/models/{c['id']}", "creator": c.get("creator"), "downloads": dl,
               "thumbs_up": c.get("thumbsUpCount"), "published_at": next((v.get("publishedAt") for v in vers if v.get("publishedAt")), None),
               "trigger_words": tw, "trigger_source": "civitai version trainedWords" if tw else "unknown (not stated by source)",
               "strength": extract_strength(desc), "description": desc[:300], "example": ex, "poi": c.get("poi"), "compat_note": compat,
               "other_version_on_graydient": c["id"] in g_mid, "other_version_in_hf_repo": c["id"] in o_mid}
        b = best[(fam, cat)]
        reason = ""
        if not row["other_version_on_graydient"] and not row["other_version_in_hf_repo"] and not compat and dl >= 2000:
            if cnt_cat[(fam, cat)] == 0:
                reason = "no Graydient LoRA in this family+category"
            elif b and dl >= 2 * b:
                reason = f"downloads {dl} >= 2x best available ({b}) in same family+category"
            elif cat == "utility":
                for kw in ("turbo", "lightning", "distill", "hyper", "accelerat"):
                    if kw in row["name"].lower() and kw not in have_util_kw[fam]:
                        reason = f"utility ({kw}) with no available equivalent"; break
        row["suggest_ingest"] = bool(reason)
        row["suggest_reason"] = reason
        row["ingest_priority"] = round(math.log10(dl + 1) * 10 + (8 if reason else 0) - (6 if row["other_version_on_graydient"] else 0) - (4 if c.get("poi") else 0) - (5 if compat else 0), 1)
        out.append(row)
    out.sort(key=lambda r: -r["ingest_priority"])
    (DATA / "candidates.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n")
    cnt = Counter(r["family"] for r in out)
    # ingest queue
    q = [r for r in out if r["suggest_ingest"]][:300]
    (DATA / "graydient_ingest_queue.txt").write_text("\n".join(r["source_url"] for r in q) + "\n")
    md = ["# Graydient ingest queue (proposals only; nothing is downloaded or ingested automatically)", "",
          "Top candidates that meet the suggest-ingest rule, by `ingest_priority`. Andrew decides; ingest runs only when he asks.", "",
          "| prio | family | category | name | downloads | trigger | reason | link |", "|---:|---|---|---|---:|---|---|---|"]
    for r in q[:120]:
        md.append(f"| {r['ingest_priority']} | {r['family']} | {r['category']} | {r['name'][:60].replace('|','/')} | {r['downloads']} | {', '.join(r['trigger_words'])[:60].replace('|','/') or 'unknown'} | {r['suggest_reason']} | {r['source_url']} |")
    (DATA / "graydient_ingest_queue.md").write_text("\n".join(md) + "\n")
    return dict(cnt)

def write_summary(loras, excluded, unclassified, ignored, nfiles, hf, cand_counts=None):
    cand_counts = cand_counts or {}
    def cnt(pred):
        c = Counter()
        for l in loras:
            if pred(l):
                c[l["family"]] += 1
        return c
    g_rows = cnt(lambda l: l["graydient"])
    g_dist = cnt(lambda l: l["graydient"] and not l.get("duplicate_of"))
    g_ver = cnt(lambda l: l["graydient"] and not l.get("duplicate_of") and l["reliability"] == "verified")
    o_rows = cnt(lambda l: not l["graydient"])
    exc_by = Counter()
    for e in excluded:
        r = e["reason"]
        if e.get("repo") == "candidate":
            key = "candidate rejected: minor-coded term"
        elif r.startswith("possible minor") or r.startswith("forbidden identity"):
            key = "minors/forbidden identity (inventory)"
        elif r.startswith("intermediate"):
            key = "intermediate epoch"
        elif r.startswith("out of scope"):
            key = "out of scope family"
        else:
            key = r
        exc_by[key] += 1
    repos = Counter(r["repo"] for r in hf if r["path"].lower().endswith(WEIGHT_EXT))
    L = ["# Inventory summary (T2I LoRAs)", "",
         f"Source: read-only Hugging Face listings of every repo under `Octavian123` (22 repos; weight files seen: **{nfiles}**), matched to CivitAI by file SHA256.", "",
         "Availability: **on Graydient** = file in `Octavian123/civit`, `civit2` or `private` (or identical sha to such a file). **HF repo only** = file only in another Octavian123 repo (flag: needs adding to Graydient).", "",
         "| family | on Graydient (slugs) | on Graydient, distinct files (excl. duplicate shas) | of which verified by CivitAI hash | other HF repo only | candidates (not available) |", "|---|---:|---:|---:|---:|---:|"]
    for f in FAMILIES:
        L.append(f"| {f} | {g_rows[f]} | {g_dist[f]} | {g_ver[f]} | {o_rows[f]} | {cand_counts.get(f, 'pending')} |")
    L.append(f"| **total** | **{sum(g_rows.values())}** | **{sum(g_dist.values())}** | **{sum(g_ver.values())}** | **{sum(o_rows.values())}** | **{sum(cand_counts.values()) if cand_counts else 'pending'}** |")
    rel = Counter(l["reliability"] for l in loras)
    L += ["", "## Row reliability (all families)", "", "| reliability | rows | meaning |", "|---|---:|---|",
          f"| verified | {rel['verified']} | file hash matched on CivitAI; family/triggers from source |",
          f"| name-only | {rel['name-only']} | no CivitAI hash match; family from file-name token or legacy 2026-09-09 enrichment |",
          f"| family-guess | {rel['family-guess']} | family guessed from `-xl` suffix (no hash match); treated as Illustrious, unverified |",
          f"| epoch-only | {rel['epoch-only']} | only an intermediate training-epoch file exists (mostly Andrew's own trained LoRAs in `private`/`mcb`); concept slug unverified |",
          f"| manual-unverified | {rel['manual-unverified']} | slugs from the owner's minekrea / kromoss skills; no matching HF file name, so 'on Graydient' is inferred |",
          f"| duplicate (same sha as another slug) | {sum(1 for l in loras if l.get('duplicate_of'))} | extra names for an identical file; ignored by recipes |", "",
          "Note: `Octavian123/private` holds training-epoch files, and the matching Graydient concept slugs often differ from the file names, so 'on Graydient' is inferred for that repo.", "",
          f"Unclassifiable files (no family determinable): **{len(unclassified)}** (see `data/unclassified.jsonl`).", "",
          "## Excluded (data/excluded.jsonl)", "", "| reason | count |", "|---|---:|"]
    for k, v in exc_by.most_common():
        L.append(f"| {k} | {v} |")
    L += ["", "## Weight files per HF repo", "", "| repo | weight files | on Graydient |", "|---|---:|---|"]
    for k, v in repos.most_common():
        L.append(f"| {k} | {v} | {'yes' if k in GRAYDIENT_REPOS else 'no'} |")
    L += ["", f"Ignored non-weight files (txt/readme/etc): {sum(ignored.values())}", ""]
    (DATA / "inventory_summary.md").write_text("\n".join(L))

if __name__ == "__main__":
    main()
