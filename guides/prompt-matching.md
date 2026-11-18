# Prompt → LoRA matching (worked examples)

Generated 2026-11-18 by `scripts/matcher_examples.py` from `data/semantic_catalog.jsonl` (real slugs; rerun after the weekly update). Reproduce any example with the command shown.

Read each pick's *why* before adding it: the matcher ranks by shared words and semantic tags, not by looking at images. Triggers are copied from the source; an empty trigger means the LoRA is registered on Graydient by slug only. Weights marked *default* are workflow defaults, not source-stated values.

## Photoreal phone selfie (Krea2, detailed-krea2)

```bash
python3 scripts/suggest.py "photoreal amateur phone selfie of a tanned woman in a red bikini on a beach at golden hour, freckles, smiling" --base krea2
```

Prompt reads as: subject: woman; concept: beach, realism enhancement, lighting; clothing: swimwear; expression: smile; object: phone; pose: selfie; style: photoreal, amateur; anatomy: face, skin

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<nude-private-leaked-selfie-aesthetic-krea2:1.0>` | style | words: amateur, phone, selfie; concept/intent: realism enhancement, lighting; object/prop: phone | — (slug only) | 1.0 (source) |
| 2 | `<real-skin-pores-freckles-uneven-tone-by-se-krea2:1.0>` | identity | words: freckles, phone, selfie; concept/intent: realism enhancement; object/prop: phone | r3alsk1n | 1.0 (source) |
| 3 | `<Tan-Lines-Krea2_epoch_10:0.9>` | detail | words: beach, bikini; subject/character: woman; concept/intent: beach, realism enhancement | tan_linesV1 | 0.9 (source) |
| 4 | `<satin-string-bikini-panties-krea2:0.9>` | style | words: bikini; clothing/outfit: swimwear; anatomy: skin | satin_string_bikini_panties | 0.9 (source) |
| 5 | `<style-punkeydoodles8-i-cast-fireball-krea2:0.7>` | style | words: freckles; anatomy: face, skin | digital illustration with rough lines, vibrant expression of, freckles | 0.7 (default) |
| 6 | `<ms-smile-slider-kr2-krea2:0.7>` | utility | expression: smile | — (slug only) | 0.7 (default) |

Stacking notes: Two or more style LoRAs fight each other: keep one, or halve both weights. Speed/slider LoRAs: speed ones only on the matching turbo/few-step workflow; sliders are signed (negative weight reverses). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Andrew's own style LoRA (Anima)

```bash
python3 scripts/suggest.py "kiwinestyle comic pin-up, curvy woman with lavender hair in a cowboy hat and pink coat, speech bubble, screentones" --base anima
```

Prompt reads as: subject: woman, bbw, cowgirl western; concept: text and logos; clothing: jacket coat, headwear; expression: talking; style: vintage retro, comic, glamour; anatomy: hair, body type

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<kiwinestyle_anima_v1:0.7>` (own) | style | words: kiwinestyle; concept/intent: text and logos; style/medium: vintage retro, comic, glamour | kiwinestyle | 0.7 (default) |
| 2 | `<deuza-style-anima-2:0.8>` | style | words: pin, woman; subject/character: woman, bbw, cowgirl western; style/medium: vintage retro, glamour | deuzapinxl, pin-up, traditional media | 0.8 (source) |
| 3 | `<zamn-meme-anima:0.7>` | concept | words: bubble, speech; concept/intent: text and logos; expression: talking | zamn meme, speech bubble, text: zamn | 0.7 (default) |
| 4 | `<patchouli-knowledge-cosplay-clothing-anima:1.0>` | clothing | words: hair, hat, pin, pink; clothing/outfit: jacket coat, headwear; anatomy: hair | patchouli knowledge (cosplay), blue bow, bow | 1.0 (source) |
| 5 | `<sis-begs-for-more-style-anima:0.7>` | style | subject/character: bbw; anatomy: hair, body type | sbfm7_s | 0.7 (default) |
| 6 | `<boo-di-ogog-artist-style-anima:0.7>` | style | expression: talking | 0g0g | 0.7 (default) |

Stacking notes: Two or more style LoRAs fight each other: keep one, or halve both weights. Realism and anime/comic style LoRAs rarely agree: choose one lane. Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Fantasy character, tag prompt (Pony)

```bash
python3 scripts/suggest.py "score_9, score_8_up, 1girl, dark elf, silver hair, bikini armor, holding sword, from below, angry, fantasy forest" --base pony
```

Prompt reads as: subject: woman, elf; concept: fantasy, outdoors; clothing: swimwear, armor; expression: angry; object: weapon; pose: from below; style: dark gothic; anatomy: hair

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<elf-drow-xl:0.7>` | concept | words: elf, fantasy; subject/character: elf; concept/intent: fantasy | — (slug only) | 0.7 (default) |
| 2 | `<bousou-rampage-xl:0.7>` | concept | words: angry; expression: angry | bousou, angry, rampage | 0.7 (default) |
| 3 | `<gpt-anime-sword-and-fantasy-beautiful-game-ill:0.7>` | style | words: fantasy, sword; concept/intent: fantasy; clothing/outfit: armor | Fantasy_style_112 | 0.7 (default) |
| 4 | `<under-lighting-xl:0.7>` | concept | words: below; pose/action/camera: from below | Light_from_below | 0.7 (default) |
| 5 | `<airgenasi-fantasy-xl:0.7>` | concept | words: fantasy; concept/intent: fantasy | AirGenasi | 0.7 (default) |
| 6 | `<changeling-xl:0.7>` | concept | words: dark, hair; style/medium: dark gothic; anatomy: hair | Changeling, gray skin, white eyes | 0.7 (default) |

Stacking notes: Realism and anime/comic style LoRAs rarely agree: choose one lane. Mixed families in one stack: keep every LoRA in the checkpoint's family (pony, illustrious). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Latex + pose + expression (Illustrious/NoobAI)

```bash
python3 scripts/suggest.py "1girl, black latex catsuit, high heels, kneeling, looking at viewer, smirk, neon lights, night city" --base illustrious --intent "glossy fetish fashion look"
```

Prompt reads as: subject: woman; concept: outdoors, lighting; clothing: latex, heels; expression: seductive, eye contact; pose: kneeling; style: neon cyberpunk, glamour

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<duplex-house-duplex-camper-ill:2.0>` | style | words: city, lights, neon, night; concept/intent: outdoors, lighting; style/medium: neon cyberpunk | duplex house, interior layout, tv | 2.0 (source) |
| 2 | `<datch-roll-city-14-ill-xl:0.7>` | concept | words: 1girl, city, heels; subject/character: woman; concept/intent: outdoors | Datch Roll City 14, 1girl, solo | 0.7 (default) |
| 3 | `<city-worlds15-xl:0.7>` | concept | words: city; concept/intent: outdoors; style/medium: neon cyberpunk | citybkg | 0.7 (default) |
| 4 | `<black-latex-suit-ill:1.05>` | clothing | words: black, latex; clothing/outfit: latex | — (slug only) | 1.05 (source) |
| 5 | `<hand-on-own-hip-xl:0.7>` | concept | words: looking, viewer; expression: eye contact | hand on own hip on side, looking at viewer | 0.7 (default) |
| 6 | `<kneeling-upright-xl:0.7>` | concept | words: kneeling; pose/action/camera: kneeling; adds: sex | kneeling upright sex from behind | 0.7 (default) |

Stacking notes: Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Medical cross-section anatomy (MOSS, kromoss)

```bash
python3 scripts/suggest.py "anatomical cross-section illustration of the female pelvis, labeled medical diagram, clean white background" --base moss
```

Prompt reads as: subject: woman; concept: medical, background; pose: cross-section; style: illustration; anatomy: internal anatomy

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<picturd-style-z-image-turbo-moss:1.0>` | utility | words: illustration; subject/character: woman; concept/intent: medical | Illustration | 1.0 (source) |
| 2 | `<c-section-scar-moss:0.4>` | concept | words: section | cs3ct10n, c-section scar on lower abdomen. | 0.4 (default) |
| 3 | `<friendly-sketch-moss:1.0>` | utility | words: illustration; concept/intent: medical; style/medium: illustration | friendlysketch | 1.0 (source) |
| 4 | `<wide-hips-thigh-gap-moss:0.4>` | anatomy | words: pelvis; anatomy: internal anatomy; adds: bbw | wide pelvis, thigh gap | 0.4 (default) |
| 5 | `<fourth-wall-interior-a-dollhouse-cutaway-b-moss:0.4>` | concept | concept/intent: background; pose/action/camera: cross-section; adds: sex | — (slug only) | 0.4 (default) |
| 6 | `<stiletto-gladiator-moss:1.0>` | clothing | words: cross; adds: bbw | gldstiletto, knee-high gladiator sandals, stiletto heel | 1.0 (source) |

Stacking notes: Speed/slider LoRAs: speed ones only on the matching turbo/few-step workflow; sliders are signed (negative weight reverses). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

