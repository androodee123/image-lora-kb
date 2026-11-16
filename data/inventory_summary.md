# Inventory summary (T2I LoRAs)

Source: read-only Hugging Face listings of every repo under `Octavian123` (22 repos; weight files seen: **14504**), matched to CivitAI by file SHA256.

Availability: **on Graydient** = file in `Octavian123/civit`, `civit2` or `private` (or identical sha to such a file). **HF repo only** = file only in another Octavian123 repo (flag: needs adding to Graydient).

| family | on Graydient (slugs) | on Graydient, distinct files (excl. duplicate shas) | of which verified by CivitAI hash | other HF repo only | candidates (not available) |
|---|---:|---:|---:|---:|---:|
| illustrious | 2916 | 2868 | 2769 | 14 | 4819 |
| sdxl | 120 | 119 | 118 | 0 | 1610 |
| pony | 513 | 507 | 485 | 7 | 1323 |
| anima | 3790 | 3717 | 3599 | 0 | 1769 |
| krea2 | 3903 | 3855 | 3590 | 3 | 2113 |
| moss | 647 | 645 | 574 | 0 | 834 |
| **total** | **11889** | **11711** | **11135** | **24** | **12468** |

## Row reliability (all families)

| reliability | rows | meaning |
|---|---:|---|
| verified | 11299 | file hash matched on CivitAI; family/triggers from source |
| name-only | 481 | no CivitAI hash match; family from file-name token or legacy 2026-09-09 enrichment |
| family-guess | 25 | family guessed from `-xl` suffix (no hash match); treated as Illustrious, unverified |
| epoch-only | 84 | only an intermediate training-epoch file exists (mostly Andrew's own trained LoRAs in `private`/`mcb`); concept slug unverified |
| manual-unverified | 24 | slugs from the owner's minekrea / kromoss skills; no matching HF file name, so 'on Graydient' is inferred |
| duplicate (same sha as another slug) | 178 | extra names for an identical file; ignored by recipes |

Note: `Octavian123/private` holds training-epoch files, and the matching Graydient concept slugs often differ from the file names, so 'on Graydient' is inferred for that repo.

Unclassifiable files (no family determinable): **194** (see `data/unclassified.jsonl`).

## Excluded (data/excluded.jsonl)

| reason | count |
|---|---:|
| intermediate epoch | 1457 |
| out of scope family | 806 |
| candidate rejected: minor-coded term | 87 |
| checkpoint, not a LoRA | 83 |
| minors/forbidden identity (inventory) | 73 |
| not a plain weight file (zip/partial download) | 4 |
| zero-byte placeholder | 1 |

## Weight files per HF repo

| repo | weight files | on Graydient |
|---|---:|---|
| Octavian123/civit | 10169 | yes |
| Octavian123/civit2 | 3622 | yes |
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
