#!/usr/bin/env python3
"""Render SKILL.md, families/*, guides, README and accessibility_report.md from data/*.jsonl.
Primary picks use ONLY Graydient-registered LoRAs. HF-repo-only LoRAs are listed flagged (needs adding to Graydient).
Candidates appear only as capped 'Suggest ingest' lines. Never invents triggers/strengths."""
from __future__ import annotations
import json, re, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from t2i_lora import FAMILIES, FAMILY_LABEL, CATEGORIES
from recipes import RECIPES

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def jl(p):
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []

def esc(s):
    return (s or "").replace("|", "/").replace("\n", " ").strip()

def trig(l):
    t = [x.strip() for x in (l.get("trigger_words") or []) if x and x.strip()]
    return ", ".join(f"`{esc(x)[:70]}`" for x in t[:4]) if t else "trigger not stated"

def strength(l):
    return f"strength `{l['strength']}` (stated)" if l.get("strength") else "strength not stated"

def link(l):
    return f"[source]({l['source_url']})" if l.get("source_url") else "no source link"

def line(l, flagged=False, example=False):
    tag = "" if not flagged else " **[HF repo only - needs adding to Graydient]**"
    unv = "" if l.get("reliability") in ("verified", "name-only") else f" _({l.get('reliability')})_"
    dl = f" · {l['downloads']:,} dl" if l.get("downloads") else ""
    d = esc(l.get("description"))[:100]
    s = f"- `{l['slug']}`{tag}{unv} — {trig(l)} · {strength(l)}{dl} · {d + ' · ' if d else ''}{link(l)}"
    ex = l.get("example") or {}
    if example and ex.get("prompt"):
        s += f"\n  - example prompt (from source{', ' + ex['sampler'] if ex.get('sampler') else ''}{', steps ' + str(ex['steps']) if ex.get('steps') else ''}): `{esc(ex['prompt'])[:170]}`" + (f" · [example image]({ex['image_url']})" if ex.get("image_url") else "")
    return s

def cline(c):
    why = f" — **{c['suggest_reason']}**" if c.get("suggest_reason") else ""
    return f"- Suggest ingest: [{esc(c['name'])[:70]}]({c['source_url']}) ({c['family']}, {c['downloads']:,} dl) — {trig(c)} · {strength(c)}{why}"

def match(l, rx, cats, text_fn=None):
    if cats and l["category"] not in cats:
        return 0
    name = (l["slug"] + " " + (l.get("name") or "")).lower()
    return 2 if rx.search(name) else 0

def recipe_block(RECIPES, pools, hfonly, sugg, top_n, examples):
    S = []
    for i, (rid, title, rxs, cats, note) in enumerate(RECIPES, 1):
        rx = re.compile(rxs, re.I)
        S += [f"### {i}. {title}", ""]
        if note:
            S += [note, ""]
        any_pick = False
        for f in FAMILIES:
            scored = [(match(l, rx, cats), l) for l in pools[f]]
            picks = sorted([x for x in scored if x[0]], key=lambda x: (-x[0], -(x[1].get("downloads") or 0), x[1]["slug"]))[:top_n]
            hf = sorted([l for l in hfonly[f] if match(l, rx, cats)], key=lambda l: -(l.get("downloads") or 0))[:2]
            if not picks and not hf:
                continue
            any_pick = True
            S.append(f"**{FAMILY_LABEL[f]}**")
            for n, (_, l) in enumerate(picks):
                S.append(line(l, example=(examples and n == 0)))
            for l in hf:
                S.append(line(l, flagged=True))
            S.append("")
        rc = sorted([c for c in sugg if (not cats or c["category"] in cats) and rx.search((c["name"] + " " + " ".join(c.get("trigger_words") or [])).lower())], key=lambda c: -c["ingest_priority"])
        seen_f, picks_c = Counter(), []
        for c in rc:
            if seen_f[c["family"]] < 2 and len(picks_c) < 3:
                picks_c.append(c); seen_f[c["family"]] += 1
        if picks_c:
            S += [cline(c) for c in picks_c] + [""]
        if not any_pick and not picks_c:
            S += ["_No Graydient LoRA and no qualifying candidate matched this goal. Describe it in the prompt text instead of a LoRA._", ""]
    return S

def main():
    loras = jl(DATA / "loras.jsonl")
    cands = jl(DATA / "candidates.jsonl")
    pools = {f: [l for l in loras if l["family"] == f and l["graydient"] and l.get("recipe_eligible")] for f in FAMILIES}
    hfonly = {f: [l for l in loras if l["family"] == f and not l["graydient"] and not l.get("duplicate_of")] for f in FAMILIES}
    sugg = [c for c in cands if c.get("suggest_ingest")]
    today = datetime.now().strftime("%Y-%m-%d")
    counts = {f: (len([l for l in loras if l['family'] == f and l['graydient'] and not l.get('duplicate_of')]), len(hfonly[f]), len([c for c in cands if c['family'] == f])) for f in FAMILIES}

    # ---------------- families/<fam>/ ----------------
    fam_dir = ROOT / "families"
    for f in FAMILIES:
        d = fam_dir / f
        d.mkdir(parents=True, exist_ok=True)
        rows = [l for l in loras if l["family"] == f and not l.get("duplicate_of")]
        by_cat = defaultdict(list)
        for l in rows:
            by_cat[l["category"]].append(l)
        idx = [f"# {FAMILY_LABEL[f]} — text-to-image LoRAs", "",
               f"On Graydient: **{counts[f][0]}** distinct LoRAs · HF repo only (needs adding to Graydient): **{counts[f][1]}** · ingest candidates: **{counts[f][2]}**", "",
               "Per-category pages (sorted: Graydient first, then by CivitAI downloads). Complete data: `data/loras.jsonl` (filter `family == " + f + "`).", "",
               "| category | on Graydient | HF only | page |", "|---|---:|---:|---|"]
        for cat in CATEGORIES:
            rs = by_cat.get(cat, [])
            if not rs:
                continue
            idx.append(f"| {cat} | {sum(1 for r in rs if r['graydient'])} | {sum(1 for r in rs if not r['graydient'])} | [{cat}.md]({cat}.md) |")
            pg = [f"# {FAMILY_LABEL[f]} — {cat}", "", f"{len(rs)} LoRAs. `[HF repo only]` = file exists in another Octavian123 HF repo but is not on Graydient yet.", ""]
            cs = [c for c in sugg if c["family"] == f and c["category"] == cat][:3]
            if cs:
                pg += ["**Suggest ingest (max 3, nothing auto-downloads):**", ""] + [cline(c) for c in cs] + [""]
            rs.sort(key=lambda r: (not r["graydient"], r.get("reliability") not in ("verified",), -(r.get("downloads") or 0), r["slug"]))
            pg.append("| slug | triggers | strength | dl | what | source |")
            pg.append("|---|---|---|---:|---|---|")
            for r in rs:
                fl = "" if r["graydient"] else " **[HF only]**"
                pg.append(f"| `{r['slug']}`{fl} | {esc(', '.join(r.get('trigger_words') or []))[:80] or 'not stated'} | {r.get('strength') or 'not stated'} | {r.get('downloads') or ''} | {esc(r.get('description'))[:110]} | {('[link](' + r['source_url'] + ')') if r.get('source_url') else ''} |")
            (d / f"{cat}.md").write_text("\n".join(pg) + "\n")
        hf = hfonly[f]
        if hf:
            idx += ["", "## In another HF repo, not on Graydient (flag: needs adding)", ""] + [f"- `{l['slug']}` ({l['category']}; repo `{l['hf_files'][0]['repo']}`; {l['reliability']})" for l in hf]
        (d / "README.md").write_text("\n".join(idx) + "\n")

    # ---------------- SKILL.md ----------------
    S = ["---", "name: image-lora-kb",
         "description: >-", "  Choose and stack text-to-image LoRAs for Illustrious/NoobAI, SDXL, Pony, Anima, Krea2 (detailed-krea2) and MOSS (kromoss)",
         "  on Graydient. Goal-based chooser with recipes. Prefer LoRAs registered on Graydient; flag other HF-repo LoRAs; suggest ingesting strong CivitAI/HF",
         "  LoRAs only under the suggest-ingest rule. Never invent triggers or strengths. Adults only.", "---", "",
         "# Skill: choose text-to-image LoRAs (Illustrious · SDXL · Pony · Anima · Krea2 · MOSS)", "",
         f"Snapshot {today}. Adults-only (18+) concepts; describe NSFW factually. No minor-coded LoRAs are in this KB.", "",
         "## Inventory at a glance", "", "| family | on Graydient | HF repo only (needs adding) | ingest candidates |", "|---|---:|---:|---:|"]
    for f in FAMILIES:
        S.append(f"| {FAMILY_LABEL[f]} | {counts[f][0]} | {counts[f][1]} | {counts[f][2]} |")
    S += ["", "**Recommend only LoRAs registered on Graydient** (files in HF `Octavian123/civit`, `civit2`, `private`). LoRAs found only in other Octavian123 HF repos are listed *flagged* as needing to be added to Graydient. Candidates (CivitAI/HF, not available) appear only as capped *Suggest ingest* lines.", "",
          "**Never invent a trigger or a strength.** If a pick says `trigger not stated` or `strength not stated`, say so and tune on a short test render. Workflow defaults (e.g. 0.7 on detailed-krea2) are workflow rules, not per-file data.", "",
          "### Suggest-ingest rule", "",
          "1. **Gap fill:** the family+category has no Graydient LoRA and the candidate has ≥ 2,000 downloads.",
          "2. **High-value upgrade:** candidate has ≥ 2,000 downloads and ≥ 2× the downloads of the best available LoRA in the same family+category; or it is an official utility pack (turbo/lightning/distill/hyper) with no available equivalent.",
          "3. **Cap:** at most 3 suggestions per recipe, each with link + any source-stated trigger/strength. Nothing auto-downloads or auto-ingests; ingest runs only when Andrew asks (civit-to-graydient pipeline).", "",
          "## How to look up any LoRA", "",
          "- Full data: `data/loras.jsonl` (fields: slug, family, category, nsfw, availability, trigger_words, strength, description, example{prompt,image_url}, source_url, downloads, reliability).",
          "- Search: `rg -i '\"slug\": \"[^\"]*keyword' data/loras.jsonl` or `jq -c 'select(.family==\"krea2\" and (.slug|test(\"latex\")))' data/loras.jsonl`.",
          "- Per-category tables: `families/<family>/<category>.md`. Candidates: `data/candidates.jsonl`. Ingest proposals: `data/graydient_ingest_queue.md`.",
          "- `reliability`: `verified` (CivitAI hash match) > `name-only` > `family-guess` / `epoch-only` / `manual-unverified` (weaker; recipes skip these).", "",
          "## How to stack, per family", "",
          "General: one **identity** LoRA per person, at most one **style/look**, at most one **detail/realism** enhancer, then anatomy/pose/act helpers only for what the image needs. Write the LoRA as `<slug:weight>` and put source triggers in the prompt text. Add LoRAs one at a time and test.", "",
          "### Krea2 (workflow `detailed-krea2`)",
          "- Command shape (from the owner's minekrea skill): `/workflow /run:detailed-krea2 /size:1536x1920 /images:1 <lora-a:0.7> <lora-b:0.7> trigger words, natural-language scene`. Tall 1536x1920 for one person, wide 1920x1536 for two or more or rooms.",
          "- Bracket order: identities → anatomy assists → concepts → style/look. Write slugs ONLY inside `<>`; then write every trigger tag after the brackets in the same order.",
          "- Prose paragraph (2–4 sentences), concrete English, one motivated light source. No SDXL tag soup (`masterpiece`, `1girl`, `8k`).",
          "- Workflow default weight 0.7 unless the catalog line states a strength.", "",
          "### MOSS (workflow `kromoss`)",
          "- Command shape from Andrew's benchmark: `/workflow /run:kromoss /size:1536x1536 /steps:40 /guidance:3.5 /images:2`, tag-style prompt with `score_9, best quality ...`, negatives in `[[ ... ]]`, LoRAs as `<slug-moss:weight>`. Highest weight on the identity LoRA (0.8 in the benchmark), helpers 0.1–0.4. See `guides/andrew-proven-stacks.md`.", "",
          "### Illustrious / NoobAI, SDXL, Pony, Anima",
          "- The owner's skills do not record workflow slugs for these families; use the workflow Andrew names. Prompt styles (rules of thumb, not per-file data): Illustrious/NoobAI and Anima are danbooru-tag friendly; Pony wants its `score_9, score_8_up, score_7_up` prefix and Pony-trained LoRAs; plain SDXL LoRAs use natural-language or tag prompts. **Do not mix families:** an Illustrious LoRA on a Pony base (or vice versa) may degrade; match each LoRA's family to the checkpoint.", "",
          "### Conflicts worth remembering", "",
          "- Two style/look LoRAs at full strength fight each other; halve both or pick one.",
          "- Two identity LoRAs in one image are only OK when the image has two different people.",
          "- Turbo/lightning/distill LoRAs belong on matching fast workflows only.",
          "- Realism enhancers and anime style LoRAs rarely agree; choose the lane first.", "",
          "---", "", "## Goal recipes", "",
          "Each recipe lists, per family, the 2 most-downloaded **verified Graydient** matches, then flagged HF-only matches, then up to 3 *Suggest ingest* lines. Deeper lists with source-stated example prompts: `guides/recipes-detailed.md`.", ""]
    S += recipe_block(RECIPES, pools, hfonly, sugg, 2, False)
    S += ["---", "", "## Andrew's proven stacks", "", "See `guides/andrew-proven-stacks.md` (detailed-krea2 identity/anatomy stack; kromoss benchmark stack).", "",
          "## Keeping this current", "", "Weekly: `python3 scripts/check_new.py` (proposals only; writes `proposals/YYYY-MM-DD.md`). After Andrew ingests anything, rerun `scripts/list_graydient.py`, `scripts/civit_lookup.py byhash`, `scripts/build_kb.py`, `scripts/render_kb.py`.", ""]
    (ROOT / "guides").mkdir(exist_ok=True)
    (ROOT / "SKILL.md").write_text("\n".join(S))
    D = ["# Detailed goal recipes (top 3 per family, with source-stated example prompts)", "",
         "Same structure as SKILL.md recipes but deeper. Verified Graydient picks first; HF-only flagged; max 3 Suggest-ingest lines.", ""]
    D += recipe_block(RECIPES, pools, hfonly, sugg, 3, True)
    (ROOT / "guides" / "recipes-detailed.md").write_text("\n".join(D))

    # ---------------- guides ----------------
    g = ROOT / "guides"
    g.mkdir(exist_ok=True)
    (g / "andrew-proven-stacks.md").write_text("""# Andrew's proven stacks (from his own skills; adults only)

## detailed-krea2 (minekrea rules)
`/workflow /run:detailed-krea2 /size:1536x1920 /images:1 <identity:0.7> <anatomy-assist:0.7> <concept:0.7> <style:0.7> triggers..., natural-language scene`

- Size: 1536x1920 for one person; 1920x1536 for two or more people, rooms, wide scenes. Never 1024x1024 unless asked.
- Bracket order: identities, anatomy assists, concepts, style/look. Slugs only inside `<>`; triggers after all brackets in the same order.
- Weight 0.7 unless the catalog line states a strength (minekrea: nude "me" penis LoRA `mypeniserect-krea2` is always 0.4; Cyber-shot uses 1.2).
- Anatomy assists named by minekrea: visible penis -> `<penis-krea2:0.7>` trigger `p3n15`; penetration -> `<penetration-control-v2-krea2:1.2>`; semen -> `<real-cum-4k-krea2:1.0>`; nude marie -> `<marie-pussyassist-krea2>`.
- Prose paragraph in order: camera/composition, who, action, clothing, place, light last. Put readable text in "quotes". No `/seed`, `/steps`, `/guidance` unless asked.

## kromoss still (benchmark run Andrew marked HIGHLY successful, Nov 2026)
`/workflow /run:kromoss /size:1536x1536 /steps:40 /guidance:3.5 /images:2` + tag prompt (`(uncensored, explicit full body photo), score_9, best quality pinup photography, ...`) + `[[censorship, emoji, watermark, website, bad anatomy, worst quality]]` + LoRAs `<mcbcore-moss:0.8> <condom-moss:0.4> <andrdpna-moss:0.4> <suze-moss:0.1> <face-moss:0.4>`.
Keep the identity LoRA highest; name condom details explicitly (transparent latex, glossy, tip state); full body in frame, eye-level.
""")
    (g / "prompt-patterns.md").write_text("""# Prompt patterns (rules of thumb; not per-LoRA data)

- Put the LoRA's source trigger words in the prompt text; the `<slug:weight>` tag alone often does nothing for concept LoRAs.
- Start at the source-stated strength; if none is stated, start at the workflow default and adjust by 0.1–0.2.
- Style LoRAs: describe the subject in plain terms and let the LoRA own the look.
- Concept/act LoRAs: describe who does what; name the camera angle explicitly.
- One change per test render.
- People are adults (18+). Write woman/man, never girl/boy, in adult scenes.
""")

    # ---------------- README + accessibility report ----------------
    R = ["# image-lora-kb", "", "Private text-to-image LoRA knowledge base for Graydient: Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS. Companion to `video-lora-kb`.", "",
         "- `SKILL.md` — goal chooser + recipes (load this).", "- `families/<family>/<category>.md` — complete tables.", "- `data/loras.jsonl`, `candidates.jsonl`, `excluded.jsonl`, `unclassified.jsonl`, `inventory_summary.md`, `accessibility_report.md`, `graydient_ingest_queue.md`.",
         "- `scripts/` — `list_graydient.py` (HF listing), `civit_lookup.py` (hash/model lookup), `harvest.py` (candidates), `build_kb.py`, `render_kb.py`, `check_new.py` (weekly monitor), `export_pack.py`.", "",
         "Metadata only: nothing here downloads weights; no tokens are stored.", "", "## Counts", "", "| family | on Graydient | HF only | candidates |", "|---|---:|---:|---:|"]
    for f in FAMILIES:
        R.append(f"| {f} | {counts[f][0]} | {counts[f][1]} | {counts[f][2]} |")
    R += ["", "## Weekly routine", "", "```", "cd /workspace/image-lora-kb && python3 scripts/check_new.py", "```", "", "See `proposals/`."]
    (ROOT / "README.md").write_text("\n".join(R) + "\n")
    rel = Counter(l["reliability"] for l in loras)
    A = ["# Accessibility report", "", "Graydient availability = file in `Octavian123/civit`, `civit2` or `private` (identical sha counts). Other `Octavian123/*` repos = **HF only, needs adding to Graydient**.", "",
         f"- Available rows: {len(loras)} (Graydient {sum(1 for l in loras if l['graydient'])}, HF-only {sum(1 for l in loras if not l['graydient'])})", f"- Reliability: {dict(rel)}", "",
         "## HF-only LoRAs (needs adding to Graydient)", ""]
    for l in loras:
        if not l["graydient"] and not l.get("duplicate_of"):
            A.append(f"- `{l['slug']}` — {l['family']}/{l['category']} — {l['hf_files'][0]['repo']}/{l['hf_files'][0]['path']} ({l['reliability']})")
    (DATA / "accessibility_report.md").write_text("\n".join(A) + "\n")
    print("rendered; SKILL.md bytes:", (ROOT / "SKILL.md").stat().st_size, file=sys.stderr)

if __name__ == "__main__":
    main()
