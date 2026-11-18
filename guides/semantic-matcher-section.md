## Match a prompt to LoRAs (semantic matcher)

Use this whenever someone hands you a draft prompt, a render to improve, or an intent ("make it look like a 90s anime cel", "she should be kneeling in latex"). It searches **every LoRA we have on Graydient** (Andrew's own `onemoreepoch` ones included) — not just the recipe picks below.

1. **Read the prompt context.** Note the base/workflow (Illustrious/NoobAI, Anima, Krea2 `detailed-krea2`, MOSS `kromoss`, SDXL, Pony), the LoRAs already in it (`<slug:w>`), and what the user is trying to get closer to: subject/character, concept/intent, clothing/outfit, expression, object/prop, pose/action/camera, style/medium, anatomy.
2. **Run the matcher** (instant, offline):
   ```bash
   python3 scripts/suggest.py "<draft prompt>" --base krea2 [--intent "<goal in words>"] [--top 12] [--own] [--include-unavailable] [--json]
   ```
   It parses the prompt into those categories, scores each catalog LoRA on rare shared words (name, slug, source triggers) and shared semantic tags, and prefers on-Graydient, own (`OWN (onemoreepoch)`) and verified ones. Versions/epochs of one LoRA collapse to the best one (`+N other versions`). Each pick shows **why it matched**, the **trigger** (or *no trigger — registered by slug*), the **weight** (source-stated, or a labelled workflow default), creator, availability and the CivitAI link, then *Best per category*, *Stacking notes* and a *Proposed addition*.
3. **Or consult the catalog directly:** `data/semantic_catalog.jsonl` (one row per Graydient slug: `slug, family, base_model, name, triggers, no_trigger, weight, weight_source, source_url, creator, own, ingest_date, availability{graydient,hf,raid}, role, semantic{subject,concept,clothing,expression,object,pose,style,anatomy}`), e.g. `jq -c 'select(.family=="anima" and (.semantic.clothing//[]|index("latex")))' data/semantic_catalog.jsonl`. Counts: `data/semantic_summary.md`.
4. **Propose additions, don't dump the list.** Pick at most one identity per person, one style, one detail/realism helper, then only the clothing/pose/expression/object/anatomy helpers the image needs. Skip picks whose *why* says `adds: …` (content the prompt didn't ask for) unless the user wants it, and skip identity LoRAs without a `name match`. Keep every LoRA in the checkpoint's family. Write them in the family syntax below — `<slug:weight>` blocks first, then the source triggers in the prompt text in the same order; no-trigger LoRAs go in by slug only. **Never invent a trigger or a strength.**
5. Explain each addition in one line (what it should fix), and suggest testing one LoRA at a time.
6. **Minor-coded LoRAs are SFW-only.** Entries flagged `minor_coded` (named minor/school-age characters, age sliders/de-aging) stay in the catalog for SFW renders; for NSFW prompts the matcher hides them, and never stack one with an NSFW or anatomy LoRA.
7. **Outfit-first.** When the prompt names a garment (bodysuit/plugsuit, latex, uniform…), clothing-only LoRAs for it rank first (`outfit match`). An NSFW prompt that names a minor-coded character gets no suggestions and no outfit substitute.

Worked examples with real slugs: `guides/prompt-matching.md`. The catalog is rebuilt weekly by `scripts/update.sh` (`scripts/build_semantic.py`), and `scripts/check_new.py` reports new/untagged LoRAs.
