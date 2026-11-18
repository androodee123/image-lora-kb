# Inventory summary (T2I LoRAs)

Source: read-only Hugging Face listings of every repo under `Octavian123` (22 repos; weight files seen: **18026**), matched to CivitAI by file SHA256.

Availability: **on Graydient** = file in `Octavian123/civit`, `civit2` or `private` (or identical sha to such a file). **HF repo only** = file only in another Octavian123 repo (flag: needs adding to Graydient).

| family | on Graydient (slugs) | on Graydient, distinct files (excl. duplicate shas) | of which verified by CivitAI hash | other HF repo only | candidates (not available) |
|---|---:|---:|---:|---:|---:|
| illustrious | 4307 | 4247 | 4108 | 14 | 5016 |
| sdxl | 277 | 276 | 275 | 0 | 1638 |
| pony | 1016 | 1003 | 980 | 7 | 1373 |
| anima | 4196 | 4114 | 3993 | 0 | 1977 |
| krea2 | 4333 | 4280 | 4012 | 3 | 2235 |
| moss | 810 | 808 | 736 | 0 | 914 |
| **total** | **14939** | **14728** | **14104** | **24** | **13153** |

## Row reliability (all families)

| reliability | rows | meaning |
|---|---:|---|
| verified | 14300 | file hash matched on CivitAI; family/triggers from source |
| name-only | 529 | no CivitAI hash match; family from file-name token or legacy 2026-09-09 enrichment |
| family-guess | 25 | family guessed from `-xl` suffix (no hash match); treated as Illustrious, unverified |
| epoch-only | 85 | only an intermediate training-epoch file exists (mostly Andrew's own trained LoRAs in `private`/`mcb`); concept slug unverified |
| manual-unverified | 24 | slugs from the owner's minekrea / kromoss skills; no matching HF file name, so 'on Graydient' is inferred |
| duplicate (same sha as another slug) | 211 | extra names for an identical file; ignored by recipes |

Note: `Octavian123/private` holds training-epoch files, and the matching Graydient concept slugs often differ from the file names, so 'on Graydient' is inferred for that repo.

Unclassifiable files (no family determinable): **194** (see `data/unclassified.jsonl`).

## Excluded (data/excluded.jsonl)

| reason | count |
|---|---:|
| intermediate epoch | 1504 |
| out of scope family | 1218 |
| candidate rejected: minor-coded term | 91 |
| checkpoint, not a LoRA | 89 |
| minors/forbidden identity (inventory) | 80 |
| not a plain weight file (zip/partial download) | 4 |
| zero-byte placeholder | 1 |

## Weight files per HF repo

| repo | weight files | on Graydient |
|---|---:|---|
| Octavian123/civit | 10169 | yes |
| Octavian123/civit2 | 7144 | yes |
| Octavian123/private | 530 | yes |
| Octavian123/mcb | 116 | no |
| Octavian123/mine | 27 | no |
| Octavian123/video | 8 | no |
| Octavian123/pixai | 5 | no |
| Octavian123/base | 4 | no |
| Octavian123/cockrings | 4 | no |
| Octavian123/mariehotline | 3 | no |
| Octavian123/alana | 2 | no |
| Octavian123/gillianscully | 2 | no |
| Octavian123/kerisable | 2 | no |
| Octavian123/roxyraye | 2 | no |
| Octavian123/beegcl1tor1s | 1 | no |
| Octavian123/bigclit | 1 | no |
| Octavian123/bikini | 1 | no |
| Octavian123/condomrealism | 1 | no |
| Octavian123/maricax-xl | 1 | no |
| Octavian123/milla | 1 | no |
| Octavian123/roxy | 1 | no |
| Octavian123/roxyrayeanal | 1 | no |

Ignored non-weight files (txt/readme/etc): 1101
