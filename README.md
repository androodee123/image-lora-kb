# image-lora-kb

Private text-to-image LoRA knowledge base for Graydient: Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS. Companion to `video-lora-kb`.

- `SKILL.md` — goal chooser + recipes (load this).
- `families/<family>/<category>.md` — complete tables.
- `data/loras.jsonl`, `candidates.jsonl`, `excluded.jsonl`, `unclassified.jsonl`, `inventory_summary.md`, `accessibility_report.md`, `graydient_ingest_queue.md`.
- `UPDATING.md`, `CHANGELOG.md` — how updates work; `scripts/update.sh` is the single entry point.
- `scripts/` — `update.sh`/`update.py`, `list_graydient.py` (HF listing), `civit_lookup.py` (hash/model lookup), `harvest.py` (candidates), `build_kb.py`, `render_kb.py`, `check_new.py` (weekly monitor), `export_pack.py`.

Metadata only: nothing here downloads weights; no tokens are stored.

## Counts

| family | on Graydient | HF only | candidates |
|---|---:|---:|---:|
| illustrious | 2868 | 14 | 4819 |
| sdxl | 119 | 0 | 1610 |
| pony | 507 | 7 | 1323 |
| anima | 3717 | 0 | 1769 |
| krea2 | 3855 | 3 | 2113 |
| moss | 645 | 0 | 834 |

## Updating

```
cd /workspace/image-lora-kb && bash scripts/update.sh
```

Idempotent: rematches Graydient availability, pulls new CivitAI LoRAs, rebuilds the catalog, commits and pushes only if something changed. Flags, weekly routine and the proposed-vs-applied policy: [UPDATING.md](UPDATING.md). History: [CHANGELOG.md](CHANGELOG.md), `proposals/`.
