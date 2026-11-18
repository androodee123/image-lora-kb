# image-lora-kb

Private text-to-image LoRA knowledge base for Graydient: Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS. Companion to `video-lora-kb`.

- `SKILL.md` — goal chooser + recipes (load this).
- `scripts/suggest.py` + `data/semantic_catalog.jsonl` — prompt → LoRA matcher over every LoRA on Graydient (subject, intent, clothing, expression, object, pose, style, anatomy tags; worked examples in `guides/prompt-matching.md`).
- `families/<family>/<category>.md` — complete tables.
- `data/loras.jsonl`, `candidates.jsonl`, `excluded.jsonl`, `unclassified.jsonl`, `inventory_summary.md`, `accessibility_report.md`, `graydient_ingest_queue.md`.
- `UPDATING.md`, `CHANGELOG.md` — how updates work; `scripts/update.sh` is the single entry point.
- `scripts/` — `update.sh`/`update.py`, `list_graydient.py` (HF listing), `civit_lookup.py` (hash/model lookup), `harvest.py` (candidates), `build_kb.py`, `render_kb.py`, `check_new.py` (weekly monitor), `export_pack.py`.

Metadata only: nothing here downloads weights; no tokens are stored.

## Counts

| family | on Graydient | HF only | candidates |
|---|---:|---:|---:|
| illustrious | 4280 | 14 | 5056 |
| sdxl | 279 | 0 | 1653 |
| pony | 1010 | 7 | 1380 |
| anima | 4129 | 0 | 1991 |
| krea2 | 4297 | 3 | 2244 |
| moss | 812 | 0 | 918 |

## Updating

```
cd /workspace/image-lora-kb && bash scripts/update.sh
```

Idempotent: rematches Graydient availability, pulls new CivitAI LoRAs, rebuilds the catalog, commits and pushes only if something changed. Flags, weekly routine and the proposed-vs-applied policy: [UPDATING.md](UPDATING.md). History: [CHANGELOG.md](CHANGELOG.md), `proposals/`.
