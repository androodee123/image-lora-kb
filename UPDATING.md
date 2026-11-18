# Updating image-lora-kb

One command refreshes everything and publishes it:

```bash
cd /workspace/image-lora-kb && bash scripts/update.sh
```

It is idempotent: with nothing new it changes nothing and exits 0. The **last stdout line is one JSON summary** (counts per family, changes, runtime, commit SHA, repo visibility); progress goes to stderr.

## Flags

| flag | effect |
|---|---|
| `--dry-run` | do everything, print the summary, **do not commit/push**, and restore the working tree |
| `--no-civitai` | HF/Graydient rematch only (no CivitAI requests; new files fall back to name-based classification until the next full run) |
| `--no-push` | commit locally, do not push |
| `--max-minutes N` | runtime budget (default 30; lookups and paging stop before the budget) |
| `--pages N` | CivitAI "Newest" pages per baseModel (default 3) |
| `--allow-dirty` | do not abort on uncommitted changes (the tree is then never auto-restored) |

## What it does (in order)

1. `git pull --rebase` (aborts if the tree is dirty).
2. **Re-list every `Octavian123` HF repo** (`scripts/list_graydient.py`, read-only metadata incl. file SHA256). `civit`, `civit2` and `private` are Graydient; files in any other repo are flagged *in HF repo X, not on Graydient (needs adding)*. New and removed weight files are recorded in the proposal.
3. **CivitAI lookups for new files** (`scripts/civit_lookup.py`): base model, trained words and example-image metadata by file hash, then model descriptions. Cached and incremental; only new files cost requests. Triggers, strengths and example prompts are copied only when the source states them (never invented). If the time budget runs out before lookups finish, nothing is committed (status `partial`) and the next run resumes from the cache.
4. **New CivitAI LoRAs as candidates** (`scripts/harvest.py --merge-newest`): newest pages for Illustrious/NoobAI, Anima, Krea 2, MOSS Image, SDXL and Pony, merged into the candidate cache. A full multi-sort refresh (download counts etc.) runs automatically when the last one is older than 30 days. Minor-coded names/tags and forbidden identities go to `data/excluded.jsonl`.
5. **Rebuild** (`build_kb.py`, `render_kb.py`, `export_pack.py`): `data/loras.jsonl`, `candidates.jsonl`, `excluded.jsonl`, `unclassified.jsonl`, `inventory_summary.md`, `accessibility_report.md`, `graydient_ingest_queue.*`, `SKILL.md` (with an auto "Live inventory" block), `families/`, README, and the export pack (`/workspace/share-image/`). A candidate whose file is now on Graydient moves to available automatically.
6. **Proposals and changelog**: `proposals/YYYY-MM-DD.md` and a `CHANGELOG.md` entry (moved / added / became on Graydient / removed, new HF files, new candidates). Written only when something changed.
7. **Secret scan** of staged changes (HF/GitHub/CivitAI tokens, bearer tokens, private keys, the Graydient login config key and login URLs, weight files). Any hit aborts the commit.
8. **Commit and push to `main`** only if something changed. GitHub account `androodee123` only; `GITHUB_TOKEN`/`GH_TOKEN` are unset.

## Proposed vs applied

- **Applied automatically:** catalogs, SKILL.md, family pages, README, reports, the ingest queue, the export pack. All metadata; the repo never holds weights.
- **Proposed only:** adding anything to Graydient. The ingest queue and *Suggest ingest* lines are proposals; a LoRA found only in another HF repo is flagged "needs adding". Ingesting (civit-to-graydient, `ingest.py`) stays a manual step Andrew asks for; these scripts never download weights and never ingest.
- Recommendations use only LoRAs registered on Graydient.

## Weekly routine

The weekly routine (Mondays) runs `bash scripts/update.sh` from this repo and reports the JSON summary line. Run it by hand any time. `scripts/check_new.py` remains a read-only preview.

## Keeping forks and other AIs in sync

- Raw skill on main: `https://raw.githubusercontent.com/androodee123/image-lora-kb/main/SKILL.md`
- Clones: `git pull`.
- Chat attachments: `python3 scripts/export_pack.py --out <dir>`.

## Requirements and caches

Python 3 with `huggingface_hub` (credentials from the machine's normal HF login; none are stored in the repo) and `gh` logged in as `androodee123`. Raw caches live in `data/raw/` (gitignored except the HF listings). On a fresh clone the first run warms the caches and may report `partial` a few times (about 13k hash lookups). `data/legacy_enriched.jsonl.gz` is a committed fallback for older enrichment.

## Semantic catalog and prompt matcher

`scripts/update.sh` now also runs `scripts/build_semantic.py --flag-kb` right after the catalog rebuild, then `scripts/matcher_examples.py`:

1. **Minor-coded flags:** nothing is removed for being minor-coded. Rows in `data/loras.jsonl` / `data/candidates.jsonl` that are canonically minor/school-age characters (named individually in `scripts/semantic.py`, no franchise rules), age-slider/de-aging LoRAs, ingest-review safety skips (`data/local/safety_skips.json`), or that say child/minor in their own text get `minor_coded: true` plus `minor_reason`. Only an explicit loli/shota/underage/preteen/toddler term in a LoRA's own name, triggers or tags, or a forbidden identity, moves it to `data/excluded.jsonl`. `scripts/suggest.py` never offers `minor_coded` LoRAs for NSFW prompts (explicit/nudity wording or NSFW/anatomy LoRAs already in the stack) and never stacks them with NSFW or anatomy LoRAs.
2. **`data/semantic_catalog.jsonl`:** one row per LoRA we have on Graydient (plus HF/RAID-only ones, flagged), merged from `data/loras.jsonl`, the AIOps library snapshot and the ingest-plan snapshot. Fields: slug, family, base_model, name, triggers (empty = no trigger; registered by slug), weight + source, source_url, CivitAI ids, creator (`onemoreepoch` = Andrew's own), ingest_date (plan date or AIOps `ingested_at`; approximate), availability {graydient, hf, raid}, role, and `semantic` tags in subject / concept / clothing / expression / object / pose / style / anatomy (+ motion for video), derived from names, triggers, CivitAI tags and descriptions. Summary: `data/semantic_summary.md`.
3. **`guides/prompt-matching.md`:** worked `scripts/suggest.py` examples regenerated on the current catalog.

`scripts/check_new.py` rebuilds the same catalog and adds a *Semantic tags* section to the proposal (new and untagged LoRAs, snapshot ages). New CivitAI proposals carry their semantic tags too.

### Refreshing the local snapshots (`data/local/`)

The AIOps LoRA library and the civit-to-graydient plan files live on the home Mac, so the weekly box run reuses the committed snapshots. Refresh them (read-only; sanitized: no RAID paths, download URLs, logins or tokens) when `check_new.py` says they are older than a week, or after a big ingest:

```bash
# on the home Mac, from a checkout of this repo
python3 scripts/export_local_meta.py \
  --aiops-db ~/AI/ai-ops-portal/data/catalog-index.sqlite \
  --plans '/Users/AndrewD/downloadtemp/civit-ingest-*/plan.json' \
  --out data/local
# safety skips come from the ingest review files (box: /workspace/ingest-batches)
python3 scripts/export_local_meta.py --batches /workspace/ingest-batches --out data/local
```

Then `python3 scripts/build_semantic.py --flag-kb && python3 scripts/matcher_examples.py`, or just run `bash scripts/update.sh`. The SQLite DB is opened with `mode=ro`; nothing is downloaded or ingested.
