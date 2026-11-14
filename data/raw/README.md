Raw caches (not committed except hf/ listings). Rebuild:
  python3 scripts/list_graydient.py          # HF listings of every Octavian123 repo (read-only metadata)
  python3 scripts/civit_lookup.py byhash     # CivitAI lookup by file sha256
  python3 scripts/civit_lookup.py models     # model-level description/tags
  python3 scripts/harvest.py                 # candidate harvest
legacy_enriched.jsonl (ai-ops-portal enrichment, 2026-09-09) is a fallback source; copy it back from the box mirror /workspace/lora-inventory-2026-09-09/*-enriched.jsonl if rebuilding.
