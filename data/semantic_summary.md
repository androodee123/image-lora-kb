# Semantic LoRA catalog summary

Built 2026-11-18 by `scripts/build_semantic.py` from `data/loras.jsonl`, the AIOps library snapshot and the ingest plans. Only LoRAs with an explicit loli/shota/underage-type term in their own name, triggers or tags (or a forbidden identity) are excluded. 1336 entries are kept but flagged `minor_coded` (canonically minor/school-age characters, age sliders/de-aging, ingest-review safety skips, or a child term in the description): the matcher offers them only for SFW prompts and never stacks them with NSFW/anatomy LoRAs. 11026 entries are marked `nsfw`.

| family | entries | on Graydient | own (onemoreepoch) | no trigger | with semantic tags |
|---|---:|---:|---:|---:|---:|
| illustrious | 13238 | 12668 | 53 | 2394 | 12846 |
| anima | 4993 | 4923 | 39 | 843 | 4871 |
| krea2 | 5092 | 4975 | 99 | 1542 | 4775 |
| moss | 1849 | 1831 | 20 | 366 | 1288 |
| sdxl | 280 | 279 | 0 | 60 | 265 |
| pony | 5564 | 5511 | 2 | 1032 | 5373 |
| flux | 255 | 229 | 5 | 72 | 229 |
| zimage | 182 | 174 | 0 | 47 | 151 |
| qwen | 67 | 66 | 0 | 35 | 63 |
| chroma | 15 | 14 | 0 | 3 | 13 |
| unknown | 119 | 34 | 0 | 86 | 93 |
| **total** | 31654 | 30704 | 218 | 6480 | 29967 |

Entries per semantic category: subject/character 16029, concept/intent 13974, clothing/outfit 7451, expression 1942, object/prop 3765, pose/action/camera 4085, style/medium 20854, anatomy 12161.

Excluded while building: explicit minor term / forbidden identity in name/triggers/tags 16, intermediate epoch (final kept) 317, KB excluded (explicit minor term / forbidden identity / not a LoRA) 45.

Fields: slug, family, base_model, name, triggers (empty = no trigger; registered on Graydient by slug), weight (+source), source_url, creator (onemoreepoch = Andrew's own), ingest_date, availability{graydient,hf,raid}, role, semantic{category:[tags]}.
