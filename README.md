# image-lora-kb

Private text-to-image LoRA knowledge base for Graydient: Illustrious/NoobAI, SDXL, Pony, Anima, Krea2, MOSS. Companion to `video-lora-kb`.

- `SKILL.md` — goal chooser + recipes (load this).
- `families/<family>/<category>.md` — complete tables.
- `data/loras.jsonl`, `candidates.jsonl`, `excluded.jsonl`, `unclassified.jsonl`, `inventory_summary.md`, `accessibility_report.md`, `graydient_ingest_queue.md`.
- `scripts/` — `list_graydient.py` (HF listing), `civit_lookup.py` (hash/model lookup), `harvest.py` (candidates), `build_kb.py`, `render_kb.py`, `check_new.py` (weekly monitor), `export_pack.py`.

Metadata only: nothing here downloads weights; no tokens are stored.

## Counts

| family | on Graydient | HF only | candidates |
|---|---:|---:|---:|
| illustrious | 2412 | 14 | 4373 |
| sdxl | 102 | 0 | 1582 |
| pony | 248 | 7 | 1279 |
| anima | 3413 | 0 | 1436 |
| krea2 | 3768 | 3 | 1883 |
| moss | 585 | 0 | 746 |

## Weekly routine

```
cd /workspace/image-lora-kb && python3 scripts/check_new.py
```

See `proposals/`.
