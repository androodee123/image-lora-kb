# Semantic LoRA catalog summary

Built 2026-11-18 by `scripts/build_semantic.py` from `data/loras.jsonl`, the AIOps library snapshot and the ingest plans. Adults only: safety-skipped CivitAI ids and minor/school-coded names are excluded.

| family | entries | on Graydient | own (onemoreepoch) | no trigger | with semantic tags |
|---|---:|---:|---:|---:|---:|
| illustrious | 12058 | 11505 | 53 | 2338 | 11671 |
| anima | 4687 | 4618 | 39 | 830 | 4567 |
| krea2 | 4890 | 4773 | 99 | 1503 | 4576 |
| moss | 1814 | 1796 | 20 | 355 | 1266 |
| sdxl | 270 | 269 | 0 | 57 | 256 |
| pony | 5423 | 5371 | 2 | 1009 | 5237 |
| flux | 245 | 219 | 5 | 65 | 219 |
| zimage | 181 | 173 | 0 | 46 | 150 |
| qwen | 67 | 66 | 0 | 35 | 63 |
| chroma | 15 | 14 | 0 | 3 | 13 |
| unknown | 114 | 33 | 0 | 82 | 88 |
| **total** | 29764 | 28837 | 218 | 6323 | 28106 |

Entries per semantic category: subject/character 14379, concept/intent 13061, clothing/outfit 6182, expression 1777, object/prop 3405, pose/action/camera 3943, style/medium 19542, anatomy 10795.

Excluded while building: minor-coded character/franchise 457, safety-skip id 1081, minor/school-coded text 294, intermediate epoch (final kept) 317, KB excluded (minor-coded / not a LoRA) 106.

Fields: slug, family, base_model, name, triggers (empty = no trigger; registered on Graydient by slug), weight (+source), source_url, creator (onemoreepoch = Andrew's own), ingest_date, availability{graydient,hf,raid}, role, semantic{category:[tags]}.
