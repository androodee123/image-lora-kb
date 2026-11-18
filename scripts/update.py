#!/usr/bin/env python3
"""One idempotent entry point to update image-lora-kb (T2I LoRAs: Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS).

  bash scripts/update.sh [--dry-run] [--no-civitai] [--max-minutes 30] [--pages 3] [--allow-dirty] [--no-push]

Steps: pull -> re-list EVERY Octavian123 HF repo (Graydient = civit/civit2/private) -> CivitAI hash/model lookup
for new files (cached, incremental) -> pull newest CivitAI LoRAs into the candidate cache (monthly full refresh)
-> rebuild catalogs/families/SKILL/accessibility/ingest queue/export pack (candidates now on Graydient move to
available) -> proposals + CHANGELOG -> secret scan -> commit + push only if something changed -> ONE JSON line.

Metadata only. Never downloads weights, never runs ingest.py, never ingests to Graydient.
"""
from __future__ import annotations
import argparse, json, shutil, sys, time
from datetime import datetime, date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import update_lib as U
from t2i_lora import FAMILIES, FAMILY_LABEL

ROOT = Path(__file__).resolve().parents[1]
DATA, RAW = ROOT / "data", ROOT / "data" / "raw"
REPO = "androodee123/image-lora-kb"
PY = sys.executable
GRAYDIENT_PREFIX = ("Octavian123/civit/", "Octavian123/civit2/", "Octavian123/private/")
EXPORT_DIR = "/workspace/share-image"

def jl(p):
    out = []
    if p.exists():
        for l in p.read_text().split("\n"):
            if l.strip():
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

def snapshot():
    avail = {r["slug"].lower() + "|" + str(r.get("hf_files") and r["hf_files"][0]["repo"] or ""): r for r in jl(DATA / "loras.jsonl")}
    cand = {r["civitai_model_id"]: r for r in jl(DATA / "candidates.jsonl")}
    return avail, cand

def counts(avail):
    c = {}
    for f in FAMILIES:
        rows = [r for r in avail.values() if r["family"] == f and not r.get("duplicate_of")]
        c[f] = {"on_graydient": sum(1 for r in rows if r["graydient"]), "hf_only": sum(1 for r in rows if not r["graydient"])}
    return c

def desc(r):
    trig = ", ".join(r.get("trigger_words") or []) or "trigger not stated"
    return f"`{r.get('slug') or r.get('name')}` ({r['family']}/{r.get('category', '?')}) — {trig}" + (f" — {r['source_url']}" if r.get("source_url") else "")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="run everything, print the summary, do not commit/push, restore the tree")
    ap.add_argument("--no-civitai", action="store_true", help="HF/Graydient rematch only (no CivitAI requests)")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--allow-dirty", action="store_true")
    ap.add_argument("--max-minutes", type=float, default=30.0)
    ap.add_argument("--pages", type=int, default=3, help="CivitAI 'Newest' pages per baseModel (cap)")
    a = ap.parse_args()
    U.sanitize_env()
    clock = U.Clock(a.max_minutes)
    today = datetime.now().strftime("%Y-%m-%d")
    summary = {"repo": REPO, "date": today, "mode": "dry-run" if a.dry_run else "apply", "status": "error", "warnings": []}
    with U.Lock(ROOT):
        clean_start = not U.dirty(ROOT)
        summary["_clean_start"] = clean_start
        try:
            run(a, clock, summary, today)
        except SystemExit as e:
            summary["status"] = "aborted"; summary["error"] = str(e)
            if clean_start:
                U.restore_tree(ROOT)
        except Exception as e:
            summary["status"] = "error"; summary["error"] = f"{type(e).__name__}: {e}"[:400]
            U.log(summary["error"])
            if clean_start:
                U.restore_tree(ROOT)
    summary.pop("_clean_start", None)
    summary["runtime_s"] = round(time.time() - clock.t0, 1)
    summary["steps_s"] = clock.steps
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["status"] in ("pushed", "no-change", "dry-run-ok", "committed-not-pushed") else 1

def run(a, clock, summary, today):
    ok, detail = U.check_gh_account(ROOT, need_push=not (a.dry_run or a.no_push))
    if not ok:
        raise SystemExit(f"github account check failed: {detail}")
    U.ensure_git_identity(ROOT)
    if not summary["_clean_start"] and not a.allow_dirty:
        raise SystemExit("working tree not clean; commit/stash first (or --allow-dirty)")
    with clock.step("git pull --rebase"):
        r = U.sh(["git", "pull", "--rebase"], ROOT, check=False)
        if r.returncode != 0:
            U.sh(["git", "rebase", "--abort"], ROOT, check=False)
            raise SystemExit("git pull --rebase failed: " + (r.stderr or "")[-300:])
    before_avail, before_cand = snapshot()
    before_paths = hf_paths()

    with clock.step("list all Octavian123 HF repos"):
        r = U.sh([PY, "scripts/list_graydient.py"], ROOT, check=False)
        if r.returncode != 0:
            raise SystemExit("HF listing failed (no changes kept): " + (r.stderr or "")[-250:])
    after_paths = hf_paths()
    new_files, gone_files = sorted(after_paths - before_paths), sorted(before_paths - after_paths)
    summary["hf_weight_files"] = len(after_paths)
    summary["hf_files_added"] = len(new_files); summary["hf_files_removed"] = len(gone_files)

    if not a.no_civitai:
        with clock.step("civitai: hash lookup for new files"):
            U.sh([PY, "scripts/civit_lookup.py", "byhash", "--workers", "6", "--deadline", str(clock.deadline - 900)], ROOT, check=False)
        with clock.step("civitai: model details for new in-scope models"):
            U.sh([PY, "scripts/civit_lookup.py", "models", "--workers", "6", "--deadline", str(clock.deadline - 600)], ROOT, check=False)
        pend = json.loads(U.sh([PY, "scripts/civit_lookup.py", "pending"], ROOT).stdout.strip().split("\n")[-1])
        summary["lookups_pending"] = pend
        if pend["byhash_pending"] or pend["models_pending"]:
            summary["warnings"].append("CivitAI lookups incomplete (time budget or API errors); nothing committed. Re-run to continue; caches keep progress.")
            summary["status"] = "partial"
            U.restore_tree(ROOT) if summary["_clean_start"] else None
            return
        with clock.step("civitai: merge newest LoRAs into candidate cache"):
            stamp = RAW / "harvest_full.stamp"
            full_due = (not stamp.exists()) or (date.today() - date.fromisoformat(stamp.read_text().strip() or "2000-01-01")).days >= 30
            if full_due:
                r = U.sh([PY, "scripts/harvest.py", "--full", "--deadline", str(clock.deadline - 500)], ROOT, check=False)
                if r.returncode == 0 and time.time() < clock.deadline - 500:
                    stamp.write_text(today)
                else:
                    summary["warnings"].append("monthly full harvest incomplete; will retry next run")
                summary["full_harvest"] = True
            r = U.sh([PY, "scripts/harvest.py", "--merge-newest", str(a.pages), "--deadline", str(clock.deadline - 400)], ROOT, check=False)
            if r.returncode == 0 and r.stdout.strip():
                j = json.loads(r.stdout.strip().split("\n")[-1])
                summary["civitai_candidate_models_total"] = j["models_total"]; summary["civitai_new_models_seen"] = j["models_added"]
            else:
                summary["warnings"].append("newest merge failed: " + (r.stderr or "")[-200:])

    with clock.step("rebuild catalog"):
        r = U.sh([PY, "scripts/build_kb.py"], ROOT, check=False)
        if r.returncode != 0:
            raise SystemExit("build_kb failed: " + (r.stderr or "")[-300:])
    with clock.step("adults-only prune + semantic catalog (prompt matcher)"):
        # moves safety-skipped / minor-coded rows to excluded.jsonl, then tags every Graydient LoRA for scripts/suggest.py
        r = U.sh([PY, "scripts/build_semantic.py", "--prune-kb"], ROOT, check=False)
        if r.returncode != 0:
            raise SystemExit("build_semantic failed: " + (r.stderr or "")[-300:])
        for line in r.stdout.strip().split("\n"):
            if line.startswith("{"):
                summary.setdefault("semantic", {}).update(json.loads(line))
        r = U.sh([PY, "scripts/matcher_examples.py"], ROOT, check=False)
        if r.returncode != 0:
            summary["warnings"].append("matcher_examples failed: " + (r.stderr or "")[-200:])
    after_avail, after_cand = snapshot()
    after_mids = {r.get("civitai_model_id") for r in after_avail.values() if r.get("civitai_model_id")}
    before_mids = {r.get("civitai_model_id") for r in before_avail.values() if r.get("civitai_model_id")}
    moved = [after_cand_row for mid, after_cand_row in before_cand.items() if mid in after_mids and mid not in before_mids]
    moved_rows = [r for r in after_avail.values() if r.get("civitai_model_id") in {m["civitai_model_id"] for m in moved}]
    added = [r for k, r in after_avail.items() if k not in before_avail and r not in moved_rows]
    removed = [r for k, r in before_avail.items() if k not in after_avail]
    became = [r for k, r in after_avail.items() if k in before_avail and r["graydient"] and not before_avail[k]["graydient"]]
    new_cand = [r for k, r in after_cand.items() if k not in before_cand and k not in after_mids]
    summary["counts"] = counts(after_avail)
    summary["counts"]["candidates"] = {f: sum(1 for r in after_cand.values() if r["family"] == f) for f in FAMILIES}
    summary["counts"]["unclassified"] = len(jl(DATA / "unclassified.jsonl"))
    summary["counts"]["excluded"] = len(jl(DATA / "excluded.jsonl"))
    summary["changes"] = {"candidates_moved_to_available": len(moved_rows), "added_available": len(added), "removed_available": len(removed),
                          "became_on_graydient": len(became), "new_candidates": len(new_cand)}

    with clock.step("render SKILL / families / README"):
        U.sh([PY, "scripts/render_kb.py"], ROOT)
        recent = update_recent(today, moved_rows + added + became, new_cand)
        U.patch_markers(ROOT / "SKILL.md", skill_block(summary["counts"], recent, today), "## How to look up any LoRA")
    with clock.step("export pack"):
        out = EXPORT_DIR if Path(EXPORT_DIR).parent.exists() else str(ROOT / "dist")
        r = U.sh([PY, "scripts/export_pack.py", "--out", out], ROOT, check=False)
        if r.returncode != 0:
            summary["warnings"].append("export_pack failed: " + (r.stderr or "")[-200:])
        summary["export_dir"] = out

    reverted = U.revert_cosmetic(ROOT) if summary["_clean_start"] else []
    if reverted:
        U.log("reverted timestamp-only diffs:", reverted)
    changed = U.dirty(ROOT)
    meaningful = any(summary["changes"].values()) or new_files or gone_files
    if changed and not meaningful and summary["_clean_start"]:
        U.log("only live download-count drift; not committing (stats refresh with the next real change)")
        U.restore_tree(ROOT)
        summary["warnings"].append("stats-only drift ignored")
        changed = U.dirty(ROOT)
    if changed:
        write_reports(today, summary, moved_rows, added, removed, became, new_cand, new_files, gone_files)
    summary["files_changed"] = len([l for l in changed.split("\n") if l.strip()])
    if a.dry_run:
        summary["diffstat"] = U.sh(["git", "diff", "--stat", "--no-color"], ROOT).stdout.strip().split("\n")[-1:]
        if summary["_clean_start"]:
            U.restore_tree(ROOT)
        summary["status"] = "dry-run-ok"
        return
    if not changed:
        summary["status"] = "no-change"; summary["commit"] = U.sh(["git", "rev-parse", "HEAD"], ROOT).stdout.strip()
        return
    ch = summary["changes"]; tot = summary["counts"]
    g = sum(v["on_graydient"] for k, v in tot.items() if k in FAMILIES)
    cn = sum(tot["candidates"].values())
    msg = (f"Auto-update {today}: {ch['candidates_moved_to_available']} moved to available, {ch['added_available']} added, {ch['became_on_graydient']} became on Graydient, "
           f"{ch['new_candidates']} new candidates; {g} on Graydient / {cn} candidates")
    with clock.step("commit + push"):
        res = U.commit_and_push(ROOT, msg, push=not a.no_push)
    summary["status"] = res["status"]; summary["commit"] = res["sha"]
    if res["hits"]:
        summary["secret_scan_hits"] = [f"{k}:{f}" for k, f in res["hits"]]
    if res["status"] == "pushed":
        summary["visibility"] = U.visibility(ROOT, REPO)
    if res["status"] == "aborted-secret-scan":
        raise SystemExit("secret scan hit; nothing committed: " + ", ".join(summary["secret_scan_hits"]))

def update_recent(today, newly, new_cands):
    p = DATA / "recent_additions.json"
    cur = json.loads(p.read_text()) if p.exists() else {"available": [], "candidates": []}
    def pack(r, ev):
        return {"date": today, "event": ev, "family": r["family"], "slug": r.get("slug") or r.get("name"), "category": r.get("category"),
                "triggers": (r.get("trigger_words") or [])[:4], "url": r.get("source_url") or ""}
    if newly:
        cur["available"] = ([pack(r, "available") for r in newly[:60]] + cur["available"])[:150]
    if new_cands:
        cur["candidates"] = ([pack(r, "candidate") for r in sorted(new_cands, key=lambda r: -(r.get("ingest_priority") or 0))[:15]] + cur["candidates"])[:60]
    p.write_text(json.dumps(cur, indent=1, ensure_ascii=False))
    return cur

def skill_block(c, recent, today):
    g = {f: c[f]["on_graydient"] for f in FAMILIES}
    L = [f"## Live inventory (auto-updated by `scripts/update.py`, {today})", "",
         "On Graydient: " + " · ".join(f"{f} **{g[f]}**" for f in FAMILIES) + f". Ingest candidates: " + " · ".join(f"{f} {c['candidates'][f]}" for f in FAMILIES) + ".", ""]
    if recent["available"]:
        L += ["**Recently available (newest first, max 20):**", ""]
        for r in recent["available"][:20]:
            L.append(f"- {r['date']} `{r['slug']}` ({r['family']}/{r.get('category')}) — {', '.join(r['triggers']) or 'trigger not stated'}" + (f" — {r['url']}" if r["url"] else ""))
        L.append("")
    if recent["candidates"]:
        L += ["**Newest ingest candidates from the weekly update (proposals only; max 10):**", ""]
        for r in recent["candidates"][:10]:
            L.append(f"- {r['date']} {r['slug'][:70]} ({r['family']}/{r.get('category')}) — {', '.join(r['triggers']) or 'trigger not stated'}" + (f" — {r['url']}" if r["url"] else ""))
        L.append("")
    return "\n".join(L)

def write_reports(today, summary, moved, added, removed, became, new_cand, new_files, gone_files):
    ch, c = summary["changes"], summary["counts"]
    lines = [f"# Update {today}", "", "Applied automatically by `scripts/update.py`. " + ", ".join(f"{f}: {c[f]['on_graydient']} on Graydient / {c[f]['hf_only']} HF-only / {c['candidates'][f]} candidates" for f in FAMILIES) + ".", ""]
    sections = [("Candidates now on Graydient (moved to available)", moved), ("Newly available", added), ("HF-only LoRAs that are now on Graydient", became), ("Removed", removed)]
    for title, rows in sections:
        if rows:
            lines += [f"## {title} ({len(rows)})", ""] + U.fmt_items([desc(r) for r in rows]) + [""]
    if new_files or gone_files:
        lines += [f"## Weight files in Octavian123 HF repos: {len(new_files)} added, {len(gone_files)} removed", ""]
        lines += U.fmt_items([f"`{p}` — {'on Graydient repo' if p.startswith(GRAYDIENT_PREFIX) else 'other HF repo, NOT on Graydient (needs adding)'}" for p in new_files], 40)
        lines += U.fmt_items([f"removed `{p}`" for p in gone_files], 20) + [""]
    top = sorted(new_cand, key=lambda r: -(r.get("ingest_priority") or 0))
    if top:
        lines += [f"## New ingest candidates ({len(new_cand)}) — proposals only", "", "Nothing is downloaded or ingested. Ingest runs only when Andrew asks (civit-to-graydient).", ""]
        lines += U.fmt_items([f"[{r['name'][:70]}]({r['source_url']}) ({r['family']}/{r['category']}, {int(r.get('downloads') or 0):,} dl, priority {r.get('ingest_priority')})" + (f" — **suggest ingest: {r['suggest_reason']}**" if r.get("suggest_ingest") else "") for r in top], 40) + [""]
    if len(lines) <= 4:
        lines += ["Only metadata refreshed (rankings, download stats); no new, moved or removed LoRAs.", ""]
    (ROOT / "proposals").mkdir(exist_ok=True)
    (ROOT / "proposals" / f"{today}.md").write_text("\n".join(lines))
    entry = [f"## {today}", "", f"Moved candidate→available {ch['candidates_moved_to_available']}, added {ch['added_available']}, became on Graydient {ch['became_on_graydient']}, removed {ch['removed_available']}, new candidates {ch['new_candidates']}; HF files +{len(new_files)}/-{len(gone_files)}."]
    for title, rows in sections[:3]:
        if rows:
            entry += ["", f"{title}:"] + U.fmt_items([desc(r) for r in rows], 15)
    U.changelog_prepend(ROOT, "\n".join(entry))

if __name__ == "__main__":
    sys.exit(main())
