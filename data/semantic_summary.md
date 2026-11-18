# Semantic LoRA catalog summary

Built 2026-11-18 by `scripts/build_semantic.py` from `data/loras.jsonl`, the AIOps library snapshot and the ingest plans. Adults only: safety-skipped CivitAI ids and minor/school-coded names are excluded.

| family | entries | on Graydient | own (onemoreepoch) | no trigger | with semantic tags |
|---|---:|---:|---:|---:|---:|
| illustrious | 12031 | 11477 | 53 | 2332 | 11644 |
| anima | 4683 | 4614 | 39 | 829 | 4563 |
| krea2 | 4887 | 4770 | 99 | 1503 | 4573 |
| moss | 1814 | 1796 | 20 | 355 | 1266 |
| sdxl | 270 | 269 | 0 | 57 | 256 |
| pony | 5416 | 5364 | 2 | 1010 | 5227 |
| flux | 245 | 219 | 5 | 65 | 219 |
| zimage | 181 | 173 | 0 | 46 | 150 |
| qwen | 67 | 66 | 0 | 35 | 63 |
| chroma | 15 | 14 | 0 | 3 | 13 |
| unknown | 114 | 33 | 0 | 82 | 88 |
| **total** | 29723 | 28795 | 218 | 6317 | 28062 |

Entries per semantic category: subject/character 14343, concept/intent 13059, clothing/outfit 6177, expression 1777, object/prop 3405, pose/action/camera 3941, style/medium 19504, anatomy 10780.

Excluded while building: KB excluded (minor-coded / not a LoRA) 609, minor/school-coded text 94, minor-coded character/franchise 203, safety-skip id 1074, intermediate epoch (final kept) 317.

Fields: slug, family, base_model, name, triggers (empty = no trigger; registered on Graydient by slug), weight (+source), source_url, creator (onemoreepoch = Andrew's own), ingest_date, availability{graydient,hf,raid}, role, semantic{category:[tags]}.
