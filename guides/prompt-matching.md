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
| 1 | `<Jewel Bikini - Krea 2 v1.0 - MisterMR_Jewel_Bikini_Krea2:0.7>` | clothing | words: bikini; concept/intent: beach, lighting; clothing/outfit: swimwear | Jewel bikini | 0.7 (default) |
| 2 | `<bikini-extremly-highcut-krea2:0.7>` | clothing | words: bikini; clothing/outfit: swimwear; outfit match | bik80s, Bikini, thong | 0.7 (default) |
| 3 | `<nude-private-leaked-selfie-aesthetic-krea2:1.0>` | style | words: amateur, phone, selfie; concept/intent: realism enhancement, lighting; object/prop: phone | — (slug only) | 1.0 (source) |
| 4 | `<real-skin-pores-freckles-uneven-tone-by-se-krea2:1.0>` | identity | words: freckles, phone, selfie; concept/intent: realism enhancement; object/prop: phone | r3alsk1n | 1.0 (source) |
| 5 | `<freckles-face-krea2:0.4>` | style | words: freckles; anatomy: face, skin | — (slug only) | 0.4 (source) |
| 6 | `<ms-smile-slider-kr2-krea2:0.7>` | utility | expression: smile | — (slug only) | 0.7 (default) |

Stacking notes: Two or more style LoRAs fight each other: keep one, or halve both weights. Speed/slider LoRAs: speed ones only on the matching turbo/few-step workflow; sliders are signed (negative weight reverses). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Andrew's own style LoRA (Anima)

```bash
python3 scripts/suggest.py "kiwinestyle comic pin-up, curvy woman with lavender hair in a cowboy hat and pink coat, speech bubble, screentones" --base anima
```

Prompt reads as: subject: woman, bbw, cowgirl western; concept: text and logos; clothing: jacket coat, headwear; expression: talking; style: vintage retro, comic, glamour; anatomy: hair, body type

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<mcgoth-costume-anima:0.7>` | clothing | words: hat; clothing/outfit: headwear; outfit match | hat, visor cap, black shorts | 0.7 (default) |
| 2 | `<kiwinestyle_anima_v1:0.7>` (own) | style | words: kiwinestyle; concept/intent: text and logos; style/medium: vintage retro, comic, glamour | kiwinestyle | 0.7 (default) |
| 3 | `<deuza-style-anima-2:0.8>` | style | words: pin, woman; subject/character: woman, bbw, cowgirl western; style/medium: vintage retro, glamour | deuzapinxl, pin-up, traditional media | 0.8 (source) |
| 4 | `<zamn-meme-anima:0.7>` | concept | words: bubble, speech; concept/intent: text and logos; expression: talking | zamn meme, speech bubble, text: zamn | 0.7 (default) |
| 5 | `<sis-begs-for-more-style-anima:0.7>` | style | subject/character: bbw; anatomy: hair, body type | sbfm7_s | 0.7 (default) |
| 6 | `<boo-di-ogog-artist-style-anima:0.7>` | style | expression: talking | 0g0g | 0.7 (default) |

Stacking notes: Two or more style LoRAs fight each other: keep one, or halve both weights. Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Fantasy character, tag prompt (Pony)

```bash
python3 scripts/suggest.py "score_9, score_8_up, 1girl, dark elf, silver hair, bikini armor, holding sword, from below, angry, fantasy forest" --base pony
```

Prompt reads as: subject: woman, elf; concept: fantasy, outdoors; clothing: swimwear, armor; expression: angry; object: weapon; pose: from below; style: dark gothic; anatomy: hair

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<costumebikini-top-01-request-pony:0.7>` | clothing | words: bikini; clothing/outfit: swimwear; outfit match | bikini | 0.7 (default) |
| 2 | `<elf-drow-xl:0.7>` | concept | words: elf, fantasy; subject/character: elf; concept/intent: fantasy | — (slug only) | 0.7 (default) |
| 3 | `<bousou-rampage-xl:0.7>` | concept | words: angry; expression: angry | bousou, angry, rampage | 0.7 (default) |
| 4 | `<under-lighting-xl:0.7>` | concept | words: below; pose/action/camera: from below | Light_from_below | 0.7 (default) |
| 5 | `<airgenasi-fantasy-xl:0.7>` | concept | words: fantasy; concept/intent: fantasy | AirGenasi | 0.7 (default) |
| 6 | `<changeling-xl:0.7>` | concept | words: dark, hair; style/medium: dark gothic; anatomy: hair | Changeling, gray skin, white eyes | 0.7 (default) |

Stacking notes: Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Latex + pose + expression (Illustrious/NoobAI)

```bash
python3 scripts/suggest.py "1girl, black latex catsuit, high heels, kneeling, looking at viewer, smirk, neon lights, night city" --base illustrious --intent "glossy fetish fashion look"
```

Prompt reads as: subject: woman; concept: outdoors, lighting; clothing: latex, heels; expression: seductive, eye contact; pose: kneeling; style: neon cyberpunk, glamour

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<black-latex-suit-ill:1.05>` | clothing | words: black, latex; clothing/outfit: latex; outfit match | — (slug only) | 1.05 (source) |
| 2 | `<city-worlds15-xl:0.7>` | concept | words: city; concept/intent: outdoors; style/medium: neon cyberpunk | citybkg | 0.7 (default) |
| 3 | `<bss-styles-pony-xl:0.7>` | concept | words: lights, neon; subject/character: woman; concept/intent: lighting | NEOST, neon lights | 0.7 (default) |
| 4 | `<hand-on-own-hip-xl:0.7>` | concept | words: looking, viewer; expression: eye contact | hand on own hip on side, looking at viewer | 0.7 (default) |
| 5 | `<Soviet Gothic Architecture Buildings NoobAI AD - v1.0 - Soviet_Gothic_Architecture_Buildings_NoobAI_AD:0.75>` | style | words: city; concept/intent: outdoors | Soviet_Gothic, city, building | 0.75 (source) |
| 6 | `<kneeling-upright-xl:0.7>` | concept | words: kneeling; pose/action/camera: kneeling; adds: sex | kneeling upright sex from behind | 0.7 (default) |

Stacking notes: Mixed families in one stack: keep every LoRA in the checkpoint's family (illustrious, pony). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Outfit-first: plugsuit-style bodysuit, adult original character (Illustrious/NoobAI)

```bash
python3 scripts/suggest.py "adult woman, mature female, white and red plugsuit, form-fitting bodysuit, standing in a sci-fi hangar, anime" --base illustrious --intent "get the plugsuit outfit without a character LoRA"
```

Prompt reads as: subject: woman, mature; concept: sci-fi; clothing: bodysuit, costume; pose: standing; style: anime

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<ribbon-bodysuit-xl:0.7>` | clothing | words: anime, bodysuit; clothing/outfit: bodysuit, costume; style/medium: anime | (color) bodysuit, clothing cutout | 0.7 (default) |
| 2 | `<hikaru-saikou-xl:0.7>` | concept | words: anime, female, mature; subject/character: woman, mature; style/medium: anime | c-hikaru, mature female, black hair | 0.7 (default) |
| 3 | `<retro-sci-fi-90-s-anime-style-illustriousx-anima-6:0.7>` | style | words: anime, fi, sci; concept/intent: sci-fi; style/medium: anime | retro_scifi_90s, retro_artstyle, retro | 0.7 (default) |
| 4 | `<roman-futurism-buildings-ad-ill:1.15>` | concept | words: fi, sci; concept/intent: sci-fi | AncRomFut, buildings | 1.15 (source) |
| 5 | `<standing-over-defeated-foe-ill:0.7>` | pose | words: standing; pose/action/camera: standing | — (slug only) | 0.7 (default) |
| 6 | `<prince-albert-piercing-pa-piercing-penis-p-ill:0.7>` | anatomy | words: without | penis, papiercing, papiercing_without_ball | 0.7 (default) |

Stacking notes: Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

## Noir boudoir (MOSS, kromoss)

```bash
python3 scripts/suggest.py "score_9, best quality, woman in a black corset and fishnet stockings sitting on a velvet chair, low-key lighting, film noir" --base moss
```

Prompt reads as: subject: woman; concept: detail enhancement, lighting; clothing: corset, stockings; object: chair; pose: sitting; style: dark gothic

| # | LoRA | role | why it matches | trigger | weight |
|---:|---|---|---|---|---|
| 1 | `<base-getting-dressed-stepping-into-clothin-moss:0.4>` | clothing | clothing/outfit: stockings; outfit match | st3pp1ng-1nt0 She is getting dressed stepping into her clothing | 0.4 (default) |
| 2 | `<ink-noir-graphic-novel-woodcut-style-moss:0.9>` | style | words: black, noir; concept/intent: lighting; style/medium: dark gothic | inknoire | 0.9 (source) |
| 3 | `<direct-flash-film-point-and-shoot-flash-sn-xl:0.4>` | utility | words: film; concept/intent: detail enhancement, lighting; style/medium: dark gothic | — (slug only) | 0.4 (default) |
| 4 | `<velvet-sensual-bunny-nikke-moss:0.8>` | identity | words: velvet; name match | Velvet_Bunny | 0.8 (default) |
| 5 | `<octopuss-style-moss:0.75>` | utility | pose/action/camera: sitting | @octopuss | 0.75 (source) |
| 6 | `<mcb-red-stool-moss:0.4>` | concept | object/prop: chair | mcbredstool | 0.4 (default) |

Stacking notes: Speed/slider LoRAs: speed ones only on the matching turbo/few-step workflow; sliders are signed (negative weight reverses). Large stack: add LoRAs one at a time and keep helpers at 0.2–0.5.

