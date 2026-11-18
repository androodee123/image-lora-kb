---
name: image-lora-kb
description: >-
  Choose and stack text-to-image LoRAs for Illustrious/NoobAI, SDXL, Pony, Anima, Krea2 (detailed-krea2) and MOSS (kromoss)
  on Graydient. Goal-based chooser with recipes. Prefer LoRAs registered on Graydient; flag other HF-repo LoRAs; suggest ingesting strong CivitAI/HF
  LoRAs only under the suggest-ingest rule. Prompt matcher (scripts/suggest.py + data/semantic_catalog.jsonl) finds LoRAs from every
  Graydient LoRA that move a draft prompt closer to its subject, intent, clothing, expression, object, pose and style. Never invent triggers or strengths. Minor-coded LoRAs are SFW-only.
---

# Skill: choose text-to-image LoRAs (Illustrious · SDXL · Pony · Anima · Krea2 · MOSS)

Snapshot 2026-11-18. Describe NSFW factually, adults (18+) only. LoRAs flagged `minor_coded` (minor/school-age characters, age sliders) are for SFW renders only and never go in an NSFW stack.

## Inventory at a glance

| family | on Graydient | HF repo only (needs adding) | ingest candidates |
|---|---:|---:|---:|
| Illustrious / NoobAI (Illustrious-XL based) | 4280 | 14 | 5056 |
| SDXL | 279 | 0 | 1653 |
| Pony (Pony Diffusion XL) | 1010 | 7 | 1380 |
| Anima | 4129 | 0 | 1991 |
| Krea2 (detailed-krea2) | 4297 | 3 | 2244 |
| MOSS (Moss Image / kromoss) | 812 | 0 | 918 |

**Recommend only LoRAs registered on Graydient** (files in HF `Octavian123/civit`, `civit2`, `private`). LoRAs found only in other Octavian123 HF repos are listed *flagged* as needing to be added to Graydient. Candidates (CivitAI/HF, not available) appear only as capped *Suggest ingest* lines.

**Never invent a trigger or a strength.** If a pick says `trigger not stated` or `strength not stated`, say so and tune on a short test render. Workflow defaults (e.g. 0.7 on detailed-krea2) are workflow rules, not per-file data.

### Suggest-ingest rule

1. **Gap fill:** the family+category has no Graydient LoRA and the candidate has ≥ 2,000 downloads.
2. **High-value upgrade:** candidate has ≥ 2,000 downloads and ≥ 2× the downloads of the best available LoRA in the same family+category; or it is an official utility pack (turbo/lightning/distill/hyper) with no available equivalent.
3. **Cap:** at most 3 suggestions per recipe, each with link + any source-stated trigger/strength. Nothing auto-downloads or auto-ingests; ingest runs only when Andrew asks (civit-to-graydient pipeline).

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

Worked examples with real slugs: `guides/prompt-matching.md`. The catalog is rebuilt weekly by `scripts/update.sh` (`scripts/build_semantic.py`), and `scripts/check_new.py` reports new/untagged LoRAs.

<!-- AUTO-UPDATE:START -->
## Live inventory (auto-updated by `scripts/update.py`, 2026-11-18)

On Graydient: illustrious **4280** · sdxl **279** · pony **1010** · anima **4129** · krea2 **4297** · moss **812**. Ingest candidates: illustrious 5056 · sdxl 1653 · pony 1380 · anima 1991 · krea2 2244 · moss 918.

**Recently available (newest first, max 20):**

- 2026-11-18 `ass-ripple-original-anima` (anima/anatomy) — trigger not stated — https://civitai.com/models/2880606?modelVersionId=3255745
- 2026-11-18 `anya-alstreim-code-geass-lelouch-of-the-re-anima` (anima/anatomy) — Anya_Anima, 1girl, pink hair, long hair, medium hair, twintails, ponytail, sidelocks, blunt bangs, pink eyes, lips, hairband, breasts, small breasts, midriff, red cape, cape, crop top, sleeveless shirt, shirt, sleeveless, open clothes, buttons, white shorts, short shorts, shorts, belt, belt buckle, buckle, black gloves, elbow gloves, gloves, kneehighs, socks, knee boots, ankle boots, high heel boots, boots, black footwear, high heels, bare shoulders, breasts, small breasts, midriff, tattoo, jewelry, earrings, crop top, black shirt, sleeveless shirt, shirt, sleeveless, white skirt, miniskirt, pleated skirt, skirt, underwear, panties, highleg panties, pink panties, purple panties, highleg, panty straps, black belt, belt, buckle, thigh strap, thigh belt, black gloves, elbow gloves, gloves, asymmetrical gloves, single glove, single elbow glove, latex gloves, pink thighhighs, purple thighhighs, thighhighs, thighhighs under boots, zettai ryouiki, high heel boots, knee boots, thigh boots, boots, black footwear, high heels, breasts, small breasts, midriff, black leotard, multicolored leotard, highleg leotard, leotard, highleg, clothing cutout, center opening, turtleneck, latex, white jacket, shrug (clothing), long sleeves, black gloves, gloves, pink thighhighs, thighhighs, thigh boots, high heel boots, boots, pink footwear, high heels, cropped jacket, jacket, open jacket, open clothes, shrug (clothing) — https://civitai.com/models/1615827?modelVersionId=3398415
- 2026-11-18 `anya-alstreim2-xl` (anima/anatomy) — Anya_Anima, 1girl, pink hair, long hair, medium hair, twintails, ponytail, sidelocks, blunt bangs, pink eyes, lips, hairband, breasts, small breasts, midriff, red cape, cape, crop top, sleeveless shirt, shirt, sleeveless, open clothes, buttons, white shorts, short shorts, shorts, belt, belt buckle, buckle, black gloves, elbow gloves, gloves, kneehighs, socks, knee boots, ankle boots, high heel boots, boots, black footwear, high heels, bare shoulders, breasts, small breasts, midriff, tattoo, jewelry, earrings, crop top, black shirt, sleeveless shirt, shirt, sleeveless, white skirt, miniskirt, pleated skirt, skirt, underwear, panties, highleg panties, pink panties, purple panties, highleg, panty straps, black belt, belt, buckle, thigh strap, thigh belt, black gloves, elbow gloves, gloves, asymmetrical gloves, single glove, single elbow glove, latex gloves, pink thighhighs, purple thighhighs, thighhighs, thighhighs under boots, zettai ryouiki, high heel boots, knee boots, thigh boots, boots, black footwear, high heels, breasts, small breasts, midriff, black leotard, multicolored leotard, highleg leotard, leotard, highleg, clothing cutout, center opening, turtleneck, latex, white jacket, shrug (clothing), long sleeves, black gloves, gloves, pink thighhighs, thighhighs, thigh boots, high heel boots, boots, pink footwear, high heels, cropped jacket, jacket, open jacket, open clothes, shrug (clothing) — https://civitai.com/models/1615827?modelVersionId=3398415
- 2026-11-18 `mao-hakawa-asuka-saki-hentai-renzu-futari-anima` (anima/anatomy) — Mao Hakawa, red hair, long hair, pink eyes, hairclip, hoop earrings, short red dress, star print, spaghetti straps, red rope, shibari, breast bondage, thigh strap, Asuka, short hair, brown hair, green eyes, freckles, stud earrings — https://civitai.com/models/2901846?modelVersionId=3281495
- 2026-11-18 `c-c-code-geass-lelouch-of-the-rebellion-anima` (anima/anatomy) — C.C_Anima, See Model Info for outfit — https://civitai.com/models/1834731?modelVersionId=3474299
- 2026-11-18 `sailor-uranus-sailor-moon-anima` (anima/anatomy) — sailoruranus_pb82,, blonde hair, short hair, parted bangs, blue eyes, golden tiara,   earrings, blue choker,  makeup, small breasts,, sailor senshi uniform, white leotard, blue sailor collar, brooch, jewelry, covered navel, blue skirt, miniskirt, pleated skirt, yellow bow, ribbon, back bow, bow, elbow gloves, white gloves, black boots, short  boots, high heels,, holding saber, — https://civitai.com/models/2313377?modelVersionId=3458251
- 2026-11-18 `ubette-goth-futa-oc-anima` (anima/anatomy) — ubette — https://civitai.com/models/3046233?modelVersionId=3463199
- 2026-11-18 `draco-malfoid-malfoy-redteneri-genderswap-anima` (anima/character) — femdraco, 1girl, blonde hair, long hair, asymmetrical bangs, parted hair, hair intakes, hair behind ear, light-blue eyes, ringed eyes, pale skin, black hoop earrings, small breasts, hogwarts school uniform, black robe, grey sweater, collared shirt, green necktie, black pleated skirt, pantyhose, black loafers — https://civitai.com/models/2967285?modelVersionId=3362156
- 2026-11-18 `kugisaki-nobara-jujutsu-kaisen-2nd-season-anima` (anima/character) — kugisaki nobara, jujutsu kaisen — https://civitai.com/models/1266763?modelVersionId=2963822
- 2026-11-18 `sailor-venus-anima` (anima/character) — sailor venus,(solo:1.4),blonde hair,blue eyes,tiara,red hair bow,half updo,long hair,yellow back bow,brooch,blue bow,(no symbol orange choker:1.4),(sleeveless:1.4),jewelry,leotard,orange sailor collar,orange skirt,sailor senshi uniform,elbow gloves,white gloves,, (super sailor venus:1.4),(solo:1.4),blonde hair,blue eyes,tiara,red hair bow,half updo,long hair,yellow back bow,heart brooch,blue bow,star orange choker,elbow gloves,jewelry,leotard,orange sailor collar,orange skirt,sailor senshi uniform,white gloves,, aino minako,blonde hair,long hair,blue eyes,medium breasts,earrings,school uniform,blue skirt,hair bow,white shirt,blue sailor collar,serafuku,shirt,long sleeves,pleated skirt,red bowtie,bowtie, — https://civitai.com/models/1001281?modelVersionId=3276532
- 2026-11-18 `Meiko Shiraki 白木芽衣子 Prison School 監獄学園 - AnimaBaseV1 - Anima - Meiko-Shiraki-Prison-School-AnimaBaseV1-StrangestArt` (anima/character) — shiraki_meiko, 1girl, hair bun, grey hair, brown eyes, glasses, large breasts, Meiko_uniform, jacket, white button-up shirt, open shirt, black skirt, black thighhighs,, Meiko_crop_top,  yellow tank top, crop top, pink shorts, dolphin shorts,, Meiko_Prison, striped crop top, striped pants, navel — https://civitai.com/models/2836819?modelVersionId=3201804
- 2026-11-18 `euphoria-nemu-manaka-anima` (anima/character) — <lora:NemuManaka-Anima-v1-08:0.9>, ChopioNemu, brown hair, short hair with long locks, french braid, single hair bun, blunt bangs, purple eyes, looking at viewer, source_anime,, outfit_1, collar, black serafuku, black sailor collar, black shirt, grey neckerchief, breast pocket, long sleeves, black pleated skirt, black thighhighs,, white bra, white panties,, outfit_2, bdsm, collar, bondage outfit, o-ring body harness, black thighhighs, — https://civitai.com/models/2711043?modelVersionId=3045547
- 2026-11-18 `atelier-yumia-anima` (anima/character) — atelier yumia anima — https://civitai.com/models/1392646?modelVersionId=3247839
- 2026-11-18 `leona-morimoto-hentai-discipline-record-of-anima` (anima/character) — Leona Morimoto, 1girl, blonde hair, long hair, twin drills, blue eyes, half updo, hair bow, white bow, purple school uniform, two-tone jacket, necktie, pleated skirt, purple thighhighs, yellow trim, red armband, o-ring top, bondage outfit, red panties, elbow gloves, red gloves, highleg panties, latex, thigh boots, chastity bra, chastity belt, black collar, padlock, padlock on chastity belt, orange cloak — https://civitai.com/models/1738464?modelVersionId=3378238
- 2026-11-18 `malfoid-harry-potter-fanfic-anima` (anima/character) — malfoid, blonde hair, long hair, green eyes, earrings, school uniform, collared shirt, green necktie, striped necktie, sweater, pleated skirt, thighhighs, cloak, — https://civitai.com/models/3011024?modelVersionId=3417144
- 2026-11-18 `hatsune-miku-rabbit-hole-vocaloid-anima` (anima/character) — rabbithole bunny, blue eyes, pink pupils, blue hair, pink hair, two-tone hair, hair intakes, twintails, ahoge, x hair ornament, white fake rabbit ears, teardrop facial mark, detached collar, red bowtie, heart cutout, playboy bunny, pink ribbon, red nails, fishnet pantyhose, pink single thigh strap, black high heels,, rabbithole hoodie, blue eyes, pink pupils, blue hair, pink hair, two-tone hair, medium hair, surgical mask around neck, the price tag is attached to the hem of the hoodie., hood up, black hoodie, red nails, no print, no animal ears, bandaid on leg, garter straps, fishnet thighhighs, black high heels, — https://civitai.com/models/2986359?modelVersionId=3385819
- 2026-11-18 `furinji-miu-kenichi-the-mightiest-disciple-anima` (anima/character) — furinji miu, blonde hair, long hair, blue eyes, fair skin, large breasts, curvy, parted bangs, mole, mole under eye, jacket, cropped jacket, open jacket, rolled up sleeves, purple unitard, high collar, bike shorts, tight clothes,, dougi, white jacket, wide sleeves, purple bodysuit, high collar, red belt, shorts, school uniform, white shirt, collared shirt, button up, red ribbon, ribbon tie, pleated skirt, miniskirt, yellow trim — https://civitai.com/models/3039695?modelVersionId=3454744
- 2026-11-18 `kasugano-sakura-street-fighter-alpha2-zero-anima` (anima/character) — (kasugano_sakura), (brown eyes, brown hair, short hair, large breasts, bursting breasts), (hachimaki, high neck sports bra, high neck, sailor shirt, sports bra under sailor shirt, sailor collar, neckerchief, puffy short sleeves, midriff peek, mma gloves, red gloves, pleated skirt, miniskirt), (socks, high tops), (wind lift, red buruma peek), (forehead:1.3), (red high neck sports bra, sleeveless, midriff, buruma), (barefoot) — https://civitai.com/models/2073054?modelVersionId=3405036
- 2026-11-18 `shifty-nikke-anima` (anima/character) — shifty, blue eyes, blue hair, two side up, long hair, hair ornament, animal ear headphones, headset, medium breasts, sailor collar, button badge, serafuku, blue neckerchief, grey shirt, short sleeves, wrist cuffs, breast pockets, impossible clothes, pouch, white dress, covered navel, bare legs, white footwear, sneakers, socks — https://civitai.com/models/2844483?modelVersionId=3211418
- 2026-11-18 `haramura-nodoka-saki-anima` (anima/character) — haramura_nodoka, blue eyes, pink hair, long hair, hair bow, kiyosumi school uniform, serafuku, shirt overhang, midriff, blue skirt, petticoat, white thighhighs, — https://civitai.com/models/3014157?modelVersionId=3421220

**Newest ingest candidates from the weekly update (proposals only; max 10):**

- 2026-11-18 Age Slider LoRA | PonyXL SDXL (pony/utility) — trigger not stated — https://civitai.com/models/402667
- 2026-11-18 NSFW: flat chested (sdxl/quality-detail) — flat chested — https://civitai.com/models/155622
- 2026-11-18 THE PONYDEX (POKEMON) - [PONY XL | INDIGO XL] (pony/character) — Abra — https://civitai.com/models/561630
- 2026-11-18 Age Slider LoRA | Illustrious XL (illustrious/utility) — trigger not stated — https://civitai.com/models/1025710
- 2026-11-18 BArtstyle | Blue Archive Art Style LoRA | Anime Flat Color | 蔚蓝档案画风模型  (krea2/style) — azure youth anime art style — https://civitai.com/models/29215
- 2026-11-18 Age Slider (pony/utility) — trigger not stated — https://civitai.com/models/468265
- 2026-11-18 Tifa Lockhart (Final Fantasy 7) (Outfit Collection 23 Outfits) (illustrious/clothing) — tfff7lckhrt, brown eyes, black hair, long hair, swept bangs, silver earring, jewelry, white tank top, black undershirt, midriff, bare shoulders, toned, black gloves, elbow pad, red arm guard, single arm guard, elbow gloves, fingerless gloves, belt, black skirt, miniskirt, suspender skirt, black thighhighs, zettai ryouiki, suspenders, navel, — https://civitai.com/models/1242549
- 2026-11-18 [PonyXL + 1.5] Pokemon - Lillie (pony/character) — 1lillie1, blonde hair, long hair, green eyes, 2default2, twin braids, white sunhat, white dress, sleeveless dress, kneehighs, blue footwear, 3anniversary3, twin braids, blue dress, purple dress, white gloves, elbow gloves, blue footwear, 4ponytail4, ponytail, white shirt, white skirt, pink backpack, white socks, white footwear — https://civitai.com/models/56025
- 2026-11-18 (SDXL/Pony/SD1.5)  Sono Bisque Doll wa Koi wo Suru - Marin Kitagawa (pony/character) — Kitagawa Marin — https://civitai.com/models/362837
- 2026-11-18 Marin Kitagawa (My Dress-Up Darling) - All cosplays, appearances, and  (illustrious/clothing) — mar1n, 1girl, blonde hair, long hair, multicolored hair, red eyes | pink nails, nail polish, fingernails, jewelry, earrings, ear piercing, necklace, choker, barbell piercing, bracelet, Shizuku Kuroe, cosplay, leash, wig, purple eyes, solo, purple hair, thighhighs, apron, frills, black thighhighs, dress, indoors, wide sleeves, chain leash, makeup, black dress, smile, lipstick, nail polish, necktie, detached collar, hair ornament, breasts, flower, frilled dress, black headwear, bonnet, red rose, hairband, Black Lobelia, long hair, cleavage, black gloves, collarbone, leotard, corset,  cosplay, highleg, epaulettes, dress, heterochromia, blue eyes, cleavage, red eyes, hat, choker, large breasts, black headwear, black choker, grey hair, peaked cap, military hat, coat, hair between eyes, jacket, collarbone, white hair, Prisoner Veronica, sharp teeth, breasts, white hair, dark-skinned female, dark skin, collar, teeth, hair over one eye, yellow eyes, belt bra, large breasts, ahoge, short hair, buckle, collarbone, bare shoulders, belt, partially nude, underboob — https://civitai.com/models/975648
<!-- AUTO-UPDATE:END -->

## How to look up any LoRA

- Full data: `data/loras.jsonl` (fields: slug, family, category, nsfw, availability, trigger_words, strength, description, example{prompt,image_url}, source_url, downloads, reliability).
- Search: `rg -i '"slug": "[^"]*keyword' data/loras.jsonl` or `jq -c 'select(.family=="krea2" and (.slug|test("latex")))' data/loras.jsonl`.
- Per-category tables: `families/<family>/<category>.md`. Candidates: `data/candidates.jsonl`. Ingest proposals: `data/graydient_ingest_queue.md`.
- `reliability`: `verified` (CivitAI hash match) > `name-only` > `family-guess` / `epoch-only` / `manual-unverified` (weaker; recipes skip these).

## How to stack, per family

General: one **identity** LoRA per person, at most one **style/look**, at most one **detail/realism** enhancer, then anatomy/pose/act helpers only for what the image needs. Write the LoRA as `<slug:weight>` and put source triggers in the prompt text. Add LoRAs one at a time and test.

### Krea2 (workflow `detailed-krea2`)
- Command shape (from the owner's minekrea skill): `/workflow /run:detailed-krea2 /size:1536x1920 /images:1 <lora-a:0.7> <lora-b:0.7> trigger words, natural-language scene`. Tall 1536x1920 for one person, wide 1920x1536 for two or more or rooms.
- Bracket order: identities → anatomy assists → concepts → style/look. Write slugs ONLY inside `<>`; then write every trigger tag after the brackets in the same order.
- Prose paragraph (2–4 sentences), concrete English, one motivated light source. No SDXL tag soup (`masterpiece`, `1girl`, `8k`).
- Workflow default weight 0.7 unless the catalog line states a strength.

### MOSS (workflow `kromoss`)
- Command shape from Andrew's benchmark: `/workflow /run:kromoss /size:1536x1536 /steps:40 /guidance:3.5 /images:2`, tag-style prompt with `score_9, best quality ...`, negatives in `[[ ... ]]`, LoRAs as `<slug-moss:weight>`. Highest weight on the identity LoRA (0.8 in the benchmark), helpers 0.1–0.4. See `guides/andrew-proven-stacks.md`.

### Illustrious / NoobAI, SDXL, Pony, Anima
- The owner's skills do not record workflow slugs for these families; use the workflow Andrew names. Prompt styles (rules of thumb, not per-file data): Illustrious/NoobAI and Anima are danbooru-tag friendly; Pony wants its `score_9, score_8_up, score_7_up` prefix and Pony-trained LoRAs; plain SDXL LoRAs use natural-language or tag prompts. **Do not mix families:** an Illustrious LoRA on a Pony base (or vice versa) may degrade; match each LoRA's family to the checkpoint.

### Conflicts worth remembering

- Two style/look LoRAs at full strength fight each other; halve both or pick one.
- Two identity LoRAs in one image are only OK when the image has two different people.
- Turbo/lightning/distill LoRAs belong on matching fast workflows only.
- Realism enhancers and anime style LoRAs rarely agree; choose the lane first.

---

## Goal recipes

Each recipe lists, per family, the 2 most-downloaded **verified Graydient** matches, then flagged HF-only matches, then up to 3 *Suggest ingest* lines. Deeper lists with source-stated example prompts: `guides/recipes-detailed.md`.

### 1. Photoreal skin, realism and detail

Pick one realism/detail LoRA first; extra ones fight each other.

**Illustrious / NoobAI (Illustrious-XL based)**
- `trendcraft-style-detailer-xl` — `trendcraft-style-detailer-xl` · strength `1` (stated) · 22,266 dl · 💖 Support & Share the Magic!  Love this detailer? Like, add to collection, and tag this resource in  · [source](https://civitai.com/models/1350877?modelVersionId=1809575)
- `add-micro-details-concept-ill-2` — `addmicrodetails` · strength not stated · 17,180 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=2832991)

**SDXL**
- `trendcraft-the-peoples-style-detailer-base-xl` — trigger not stated · strength not stated · 1,779 dl · Image sources include only Illustrious and NoobAI models. No realistic content. No X or higher rated · [source](https://civitai.com/models/1390819?modelVersionId=1768080)
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)

**Pony (Pony Diffusion XL)**
- `penis-real-diffusion-realistic-pony` — `penisQuiron` · strength `0.7 - 1.3` (stated) · 6,585 dl · 👑 Penis Real Diffusion - Illustrious - LORA 👑 realistic ⚙️🔧Model base: Illustrious This LORA is capa · [source](https://civitai.com/models/696766?modelVersionId=936819)
- `amateur-style-diffusion-pony` — `amateurQuironStyle`, `amateurQuiron`, `flash photo`, `webcam photo` · strength `0.7 - 1` (stated) · 4,157 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=833676)

**Anima**
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)
- `realskin-slider-anima` — `realskin slider anima` · strength not stated · 6,621 dl · -1：更平滑、更二次元的皮肤质感  0：接近底模原始效果 +1：更真实的皮肤纹理、材质和光影表现 -1 = flat anime skin  0 = base +1 = realistic skin  · [source](https://civitai.com/models/2682590?modelVersionId=3068784)

**Krea2 (detailed-krea2)**
- `krea2_nud3` — trigger not stated · strength `0.7 - 1` (stated) · 24,860 dl · New KREA 2 Version Faceless dataset (doesn't influence face), can be used with character lora easily · [source](https://civitai.com/models/2174081?modelVersionId=3066702)
- `realism-enhancer-krea2` — trigger not stated · strength not stated · 16,530 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2727284?modelVersionId=3065628)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
- `amateur-nudes-flux-wan-2-2-zit-zib-krea2` — `Amateur nudes - FLUX, Wan 2.2, ZIT, (ZIB), Krea2` · strength not stated · 3,474 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3417654)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1779) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**

### 2. Phone / selfie / amateur-photo look

Pairs with a plain, believable scene description; avoid stacking with cinematic looks.

**Illustrious / NoobAI (Illustrious-XL based)**
- `amateur-style-diffusion-ill` — `amateurQuironn 1girl` · strength `0.7 - 1` (stated) · 4,992 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=1484586)
- `phone-exposure-juxtaposition-ill` — `phoneExposureQuiron`, `juxtaposition`, `Phone Exposure` · strength `0.7 - 1.3` (stated) · 1,770 dl · 👑 Phone Exposure juxtaposition - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustriou · [source](https://civitai.com/models/1657471?modelVersionId=1876047)

**SDXL**
- `amateur-amateur-professional-photography-xl` — trigger not stated · strength not stated · 283 dl · [source](https://civitai.com/models/2973823?modelVersionId=3370283)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)

**Pony (Pony Diffusion XL)**
- `amateur-style-diffusion-pony` — `amateurQuironStyle`, `amateurQuiron`, `flash photo`, `webcam photo` · strength `0.7 - 1` (stated) · 4,157 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=833676)
- `trans-girl-selfie-pony` — `tgselfie` · strength not stated · 401 dl · [source](https://civitai.com/models/2006272?modelVersionId=2270821)

**Anima**
- `ILANIMA Irrumatio selfie NSFW Concept - ANIMA - NSFW_selfie_epoch_3` — `1girl, solo focus, selfie, reaching towards viewer, looking at viewer,`, `deepthroat,`, `clothed female nude male` · strength `0.7-0.9` (stated) · 907 dl · Like my model? Review, like, and post an image! Hope you have a nice day! Thanks! Just because why n · [source](https://civitai.com/models/2253084?modelVersionId=3249951)
- `ccdishwasher-style-anima` — trigger not stated · strength `0.8` (stated) · 318 dl · Model Introduction The dishwasher-style model boasts an extremely high level of accuracy. ANIMA V3:  · [source](https://civitai.com/models/2711269?modelVersionId=3434763)

**Krea2 (detailed-krea2)**
- `Amateur nudes - FLUX Wan 2.2 ZIT ZIB Krea2 - v1.0 Krea2 - Amateur_Nudes_v1_Krea2` — trigger not stated · strength not stated · 4,385 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3245545)
- `better-amateur-anal-xl` — `NM_amtanal,` · strength not stated · 2,454 dl · A Lora of Better amateur anal trigger tag: NM_AmtAnal, You can support my work by following the link · [source](https://civitai.com/models/963175?modelVersionId=3365704)

**MOSS (Moss Image / kromoss)**
- `amateur-nudes-flux-wan-2-2-zit-zib-krea2` — `Amateur nudes - FLUX, Wan 2.2, ZIT, (ZIB), Krea2` · strength not stated · 3,474 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3417654)
- `phone-photography-2000-2025-moss` — `This is a candid photograph taken with a smartphone of` · strength not stated · 2,706 dl · Stop prompting from scratch, explore 11,000+ Prompts for free 👉 PromptDexter.com LoRAs for simulatin · [source](https://civitai.com/models/2537408?modelVersionId=3426517)

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [Amateur style - slider](https://civitai.com/models/1410317) (pony, 50,928 dl) — trigger not stated · strength not stated — **downloads 50928 >= 2x best available (5757) in same family+category**
- Suggest ingest: [LEAKCORE (LEAKED NUDES STYLE, Realism, Amateur)](https://civitai.com/models/1439962) (sdxl, 48,422 dl) — `amateur photo`, `film grain`, `face out of frame`, `taking a mirror selfie` · strength `0.7-1.1` (stated) — **downloads 48422 >= 2x best available (3670) in same family+category**

### 3. Cinematic film still look

Pick one look. Do not mix with digicam/amateur LoRAs.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-neo-noir-illustriousxl-zimageturbo-f-ill` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,477 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2078295)
- `Kei Yuri Dirty Pair The Movie ダーティペア - v1.0 - mai_dirty_pair` — `mai_dirty_pair,1980s_\(style\),kei_\(dirty_pair\),dark-skinned_female,`, `mai_dirty_pair,1980s_\(style\),yuri_\(dirty_pair\),long_hair,blue_hair` · strength `0.8` (stated) · 622 dl · Character Set from anime movie "Dirty Pair: The Movie ダーティペア the Movie". This model offers a mini-si · [source](https://civitai.com/models/2840732?modelVersionId=3206701)

**Pony (Pony Diffusion XL)**
- `arena-1989-movie-style-pony` — `ar3na1989` · strength not stated · 167 dl · [source](https://civitai.com/models/2105155?modelVersionId=2381613)

**Anima**
- `Retro_Neo_Noir_Anima` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,301 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2803271)
- `Retro_Synth_Noir_Anima_step00002300` — `retro_synth_noir, retro, retro_artstyle, film_grain,` · strength `0.7` (stated) · 1,394 dl · Anima version: weight between [0.7,1], best at 1 trigger words : retro_synth_noir, retro, retro_arts · [source](https://civitai.com/models/2038668?modelVersionId=2841795)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `70s-horror-movie-krea2` — `ArsMovieStill, movie still from a 1970s horror movie,` · strength not stated · 1,464 dl · This LoRA is designed to capture the specific atmosphere of 70s horror movies. The trigger words are · [source](https://civitai.com/models/863136?modelVersionId=3187148)

**MOSS (Moss Image / kromoss)**
- `direct-flash-film-point-and-shoot-flash-sn-xl` — trigger not stated · strength not stated · 2,456 dl · Color film snapshots shot with a cheap point-and-shoot and its on-camera flash: the nearest face and · [source](https://civitai.com/models/3013030?modelVersionId=3419791)
- `tjfilm-style-moss` — `vifilm` · strength `1` (stated) · 497 dl · TJFilmStyle is a style LoRA I specifically trained to simulate real film photography, featuring the  · [source](https://civitai.com/models/2840370?modelVersionId=3454092)

- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**
- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [Cinematic Shot ✨](https://civitai.com/models/432586) (krea2, 62,180 dl) — `zy_cinematic` · strength not stated — **downloads 62180 >= 2x best available (11215) in same family+category**

### 4. Anime / manga / illustration style

One style LoRA at a time; add a second only at a lower strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
- `figure-anime-xl` — `fig`, `nendo`, `figma` · strength not stated · 7,822 dl · Attempt at anime figure style,  trigger word is "fig"  for nendoroid style is "nendo" Intento de est · [source](https://civitai.com/models/631010?modelVersionId=1284415)

**SDXL**
- `anime-figure-xl` — `anifigurestyle` · strength `0.5 to 0.7` (stated) · 792 dl · Trained with SDXL base model, using this lora with other XL models will produce uncontrolled results · [source](https://civitai.com/models/429926?modelVersionId=508307)

**Pony (Pony Diffusion XL)**
- `Prison School anime style PDXL - PSV1F - Prison_School_anime_style_Pony_r2` — `score_9_up, score_8_up, score_7_up,` · strength not stated · 1,686 dl · [source](https://civitai.com/models/525298?modelVersionId=583646)
- `uno-makoto-marumiya-pony-xl` — trigger not stated · strength not stated · 1,603 dl · [source](https://civitai.com/models/347454?modelVersionId=388734)

**Anima**
- `90s_anime_melancholy_Anima-step00003300` — `90s_melancholy, retro,` · strength `0.8` (stated) · 3,887 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : 90s_melancholy, retro, Anima vers · [source](https://civitai.com/models/1738546?modelVersionId=2820017)
- `90s anime aesthetic Anima-step00001600` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle,` · strength `0.8` (stated) · 3,164 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=2795022)

**Krea2 (detailed-krea2)**
- `Line Art Anime Flat - Krea.v2 - K2_Anime_Flat_V20_nnegret` — `线条动漫` · strength `0.6` (stated) · 2,496 dl · 交流群：173273201 最新的V3主要加强了线条风格，以及对tag形式的提示词支持更好了 使用技巧 1. 最佳参数组合 参数推荐值： LoRA Weight 0.6 ~ 0.9（默认 0.6） C · [source](https://civitai.com/models/2741033?modelVersionId=3103017)
- `clusterfuck-western-illustration-comic-sty-krea2` — `Illustration` · strength not stated · 1,863 dl · First of all, I don't know what I'm doing really. I just trial and errored my way through dozens of  · [source](https://civitai.com/models/154425?modelVersionId=3084476)

**MOSS (Moss Image / kromoss)**
- `anime-flat-style-moss` — trigger not stated · strength not stated · 2,919 dl · This LoRA is designed to generate vibrant, clean anime artwork featuring bold, flat colors with mini · [source](https://civitai.com/models/1952560?modelVersionId=3413292)
- `cel-animation-art-style-moss` — trigger not stated · strength not stated · 1,743 dl · Cel-Animation Art Style No trigger words are required, and the default strength is recommended. It w · [source](https://civitai.com/models/3012746?modelVersionId=3419395)

- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (24024) in same family+category**
- Suggest ingest: [MeMaXL Flat Anime Style - Noob/Illustrious/Pony/XL](https://civitai.com/models/269772) (illustrious, 63,089 dl) — `memaxl6_a`, `memaxl6_b`, `memaxl6_c`, `memaxl6_d` · strength not stated — **downloads 63089 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Vector illustration](https://civitai.com/models/60132) (sdxl, 36,693 dl) — `color icon` · strength `0.65-0.9` (stated) — **downloads 36693 >= 2x best available (3670) in same family+category**

### 5. Retro / decade looks (70s-2000s, VHS, airbrush)

Name the decade in the prompt text as well as the trigger.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
- `90s-anime-aesthetic-illustriousxl-zimagetu-ill` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle` · strength `0.8` (stated) · 5,666 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=1532976)

**Pony (Pony Diffusion XL)**
- `80s-vintage-porn-magazine-style-v1-pony` — `80spm, vintage porn, 80s era, 1980s photo` · strength not stated · 2,061 dl · [source](https://civitai.com/models/1007808?modelVersionId=1129515)
- `FTRXSRFQS8A10TW5FTQ3PVKD10` — `R3troF4nt4sy, fantasy art, painting,` · strength not stated · 90 dl · This should help you make a retro fantasy look to your babes. · [source](https://civitai.com/models/2564814?modelVersionId=2881983)

**Anima**
- `90s anime aesthetic Anima-step00001600` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle,` · strength `0.8` (stated) · 3,164 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=2795022)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-5` — `retro_scifi_90s_anime_style, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 2,778 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=2808683)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `Private Magazine Style - Private Magazine 2000s - Private_Magazine_2000s_v1` — `privatemag` · strength `1.5` (stated) · 2,563 dl · Private Magazine 1970s NEW! Tested raising the lora weight to 1.5 and found out it helps a lot if th · [source](https://civitai.com/models/2833524?modelVersionId=3266535)

**MOSS (Moss Image / kromoss)**
- `retro-vintage-photo-moss-z-image-base-xl` — trigger not stated · strength `2` (stated) · 1,203 dl · I spent some serious time digging through the Internet Archive to put this together. This LoRA is tr · [source](https://civitai.com/models/2380695?modelVersionId=3419437)
- `retro-vintage-comics-style-xl` — trigger not stated · strength not stated · 603 dl · This LoRA is trained to reproduce a vintage illustrated comic style, with a focus of detailed line a · [source](https://civitai.com/models/1082272?modelVersionId=3418240)

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [2000s Analog Core](https://civitai.com/models/1134895) (krea2, 40,517 dl) — trigger not stated · strength `0.9` (stated) — **downloads 40517 >= 2x best available (11215) in same family+category**
- Suggest ingest: [Retro Big Naturals - Photorealistic Natural Boobs](https://civitai.com/models/86483) (sdxl, 28,943 dl) — `retrobigguns` · strength not stated — **downloads 28943 >= 2x best available (1779) in same family+category**

### 6. Comic, cartoon and western animation

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-comic-random-generator-full-color-i-ill` — `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view:1.1, Frame, Text, speech bubb` · strength not stated · 24,024 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/585589?modelVersionId=2166652)
- `hentai-comic-random-generator-hard-core-il-ill` — `fcomichardcore, (comic:1.25),(Multi view, Frame, Text, speech bubble, ` · strength not stated · 16,026 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=2166991)

**SDXL**
- `sano-comic-xl` — `1girl, aika, blonde hair, medium hair, hair down, hair in ponytail, br` · strength not stated · 32 dl · [source](https://civitai.com/models/3055031?modelVersionId=3474989)
- `dizzycartoonstyle-e10-xl` — `dizzycartoonstyle` · strength not stated · 19 dl · [source](https://civitai.com/models/2950113?modelVersionId=3341094)

**Pony (Pony Diffusion XL)**
- `hentai-comic-random-generator-hard-core-il-pony` — `(comic:1.25),(Multi view, Frame, Text, speech bubble, frame, heart, tr` · strength not stated · 27,500 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=657169)
- `hentai-comic-random-generator-grayscale-as-pony` — `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, ` · strength not stated · 8,508 dl · [source](https://civitai.com/models/601268?modelVersionId=672051)

**Anima**
- `hentai-comic-random-generator-full-color-i-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text`, `1boy, erection, penis, hetero, sex, rough sex, epic sex, head grab, cu`, `2boys, mmf threesome, erection, penis, multiple penises, testicles, cu` · strength not stated · 10,402 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/585589?modelVersionId=3008158)
- `hentai-comic-random-generator-hard-core-il-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text` · strength not stated · 7,151 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=3014282)

**Krea2 (detailed-krea2)**
- `clusterfuck-western-illustration-comic-sty-krea2` — `Illustration` · strength not stated · 1,863 dl · First of all, I don't know what I'm doing really. I just trial and errored my way through dozens of  · [source](https://civitai.com/models/154425?modelVersionId=3084476)
- `dc-sci-fi-krea2` — `DCSC1F1.` · strength not stated · 1,567 dl · v1 krea2raw Trigger = DCS1F1. v1 krea2raw Trained @10,000 Steps, Rank 64, Captioned with GPT4.1, Dat · [source](https://civitai.com/models/2976222?modelVersionId=3373246)

**MOSS (Moss Image / kromoss)**
- `retro-vintage-comics-style-xl` — trigger not stated · strength not stated · 603 dl · This LoRA is trained to reproduce a vintage illustrated comic style, with a focus of detailed line a · [source](https://civitai.com/models/1082272?modelVersionId=3418240)
- `ag-vassago-flat-cartoon-style-moss` — `V4SS4G0X` · strength `0.6-0.8` (stated) · 337 dl · Ars Goetia is series of loras made on a whim, on variety of images, made from mix of Midjourney, Tum · [source](https://civitai.com/models/2853357?modelVersionId=3431233)

- Suggest ingest: [Eldritch Comics (comic book style illustration)](https://civitai.com/models/262880) (sdxl, 17,999 dl) — `comic book` · strength not stated — **downloads 17999 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Wizard's Vintage Comic Book Cover](https://civitai.com/models/210095) (sdxl, 17,473 dl) — `Vintage comic book with title text: "xyz"`, `vintage comic book` · strength not stated — **downloads 17473 >= 2x best available (3670) in same family+category**

### 7. Painting, watercolor, oil, sketch, ink

**Illustrious / NoobAI (Illustrious-XL based)**
- `public-bdsm-on-black-toilet-real-anime-cos-ill` — `public bdsm, bdsm, restrained, bondage, shibari, black toilet, black r`, `realistic, photorealistic,`, `spread legs, spread_pussy, close up pussy, detailed pussy, detailed an`, `pov, pov penis, vaginal, deep insertion, Grabing ass, spread mons,` · strength not stated · 2,665 dl · This model generates a cosplayer engaged in public bondage play on top of a black toilet bowl. Can b · [source](https://civitai.com/models/2375147?modelVersionId=2671098)
- `japanese-style-toilet-girl-il-ill` — `((jptoilet)) , ((Thighs buried in wall)), solo, anus, pussy, ((from ab` · strength not stated · 2,304 dl · The learning materials are available here. Please feel free to use them. https://mega.nz/folder/Q0gn · [source](https://civitai.com/models/1899949?modelVersionId=2242138)

**SDXL**
- `Ink Splatter Abstract Art Style SDXL LoRA - v1.0 - art_ink_splatter_abstract_v1` — trigger not stated · strength not stated · 41 dl · [source](https://civitai.com/models/2870349?modelVersionId=3243001)

**Pony (Pony Diffusion XL)**
- `hash sketch - v 8.26 noobai - Desenho_de_Rachurado` — trigger not stated · strength not stated · 17 dl · [source](https://civitai.com/models/2242730?modelVersionId=2524719)

**Anima**
- `Anime Oil Touch - v1.0 - 123.1` — trigger not stated · strength not stated · 695 dl · 默认lora强度为1即可。 · [source](https://civitai.com/models/2884752?modelVersionId=3260812)
- `kok-takenawa-style-pastel-anime-illustrati-anima` — `@koktakenawa`, `anime illustration, clean lineart, pastel colors,` · strength `1.0` (stated) · 360 dl · A style LoRA trained on 158 images of the artist kok/takenawa for anime illustrations with light lin · [source](https://civitai.com/models/2976007?modelVersionId=3372990)

**Krea2 (detailed-krea2)**
- `krea2_ta86_inkriot_V2` — `ta86_inkriot`, `graphic cel shading`, `bold black outlines` · strength `2` (stated) · 4,844 dl · ta86_inkriot Graphic Cel Shaded Chaos and Hand-Inked Worldmorph-like Aesthetics. You all can guess w · [source](https://civitai.com/models/2827717?modelVersionId=3190465)
- `fantasy-graphite-sketch-krea2` — `@fantasysketcheight` · strength `0.5 to 0.7` (stated) · 863 dl · So, yeah, descriptions are in model descriptions. V1 Just a simple sketch lora for Pony. I wanted a  · [source](https://civitai.com/models/580163?modelVersionId=3188163)

**MOSS (Moss Image / kromoss)**
- `friendly-sketch-moss` — `friendlysketch` · strength `0.8 to 1.2` (stated) · 599 dl · Apply a friendly, warm style to your Moss-Image illustrations. (See the Krea 2 version or the Anima  · [source](https://civitai.com/models/3013132?modelVersionId=3419935)
- `hd-digital-painting-moss` — `digital painting` · strength not stated · 405 dl · A sharp digital painting style that doesn't look plastic! · [source](https://civitai.com/models/3034351?modelVersionId=3447679)

- Suggest ingest: [zyd232's Ink Style](https://civitai.com/models/73305) (sdxl, 30,128 dl) — `zydink`, `ink sketch` · strength `0.6 to 1.2` (stated) — **downloads 30128 >= 2x best available (3670) in same family+category**
- Suggest ingest: [ClassipeintXL (oil paint / oil painting style)](https://civitai.com/models/127139) (sdxl, 25,007 dl) — `oil painting` · strength not stated — **downloads 25007 >= 2x best available (3670) in same family+category**

### 8. 3D render / CG / game-art look

**Illustrious / NoobAI (Illustrious-XL based)**
- `queen-s-blade-gamebook-defeats-concept-il-ill` — `qbdefeat, simple background, white background, number Text,  trembling`, `1boy, pov hand, Tearing other clothes, grabbing other clothes, grabbin` · strength not stated · 3,424 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=2166233)
- `sinisistar-2-game-emulator-cg-style-2-ill` — `sinistar2, 1 girl, solo focus ,  (gameplay mechanics , fake screenshot`, `sinistar2, 1 girl, solo focus ,  (gameplay mechanics , fake screenshot`, `gangbang, group sex, 2+male, 2+penis, double penetration, veins penis,`, `monster gangbang, group sex, 2+monsters, 2+penis, double penetration, ` · strength not stated · 2,673 dl · ⚠️Please do not submit gory images to CivitAI.⚠️ Plese Set CFG Scale = 4.5 Landscape 1216x832 (Game  · [source](https://civitai.com/models/1992673?modelVersionId=2255524)

**SDXL**
- `soren3d-soren-jones-art-style-il-sd-xl` — `soren3d, 3d,` · strength not stated · 45 dl · Recreates the art style of Soren3D, or Soren Jones. Have fun! · [source](https://civitai.com/models/1458929?modelVersionId=1649912)

**Pony (Pony Diffusion XL)**
- `queen-s-blade-gamebook-defeats-concept-il-pony` — `(nipple), (pussy), (QB_Defeat:1.25), simple background, white backgrou` · strength not stated · 4,049 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=927214)
- `black-lilith-style-taimanin-asagi-cg-pony` — `bl-tai1` · strength not stated · 173 dl · Recreates the Black Lilith style for the CGs, have fun! · [source](https://civitai.com/models/1295024?modelVersionId=1461538)

**Anima**
- `queen-s-blade-gamebook-defeats-concept-il-anima` — `qb defeat, qbdefeat, simple background, white background, number Text,`, `1boy, pov hand, Tearing other clothes, grabbing other clothes, grabbin` · strength not stated · 1,626 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=3051558)
- `MogudanOldStyle_AnimaBaseV10_byKonan` — trigger not stated · strength `0.8-1` (stated) · 977 dl · Trained on Anima with 103 pictures. Best result with weight between : 0.8-1. Reviews are really appr · [source](https://civitai.com/models/2658734?modelVersionId=2985451)

**Krea2 (detailed-krea2)**
- `krea2 sex 淫模 - CG - krea cowgirl` — `kreacowgirl, 1girl, 1boy, hetero, long hair, ass, black hair, anus, gi` · strength `0.6–0.7` (stated) · 4,986 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3158775)
- `pure-pixar-3d-krea2` — `KR2Pix` · strength not stated · 1,981 dl · This is a style LoRA that blends Pixar and realistic aesthetics. Use the following sentences or term · [source](https://civitai.com/models/2977241?modelVersionId=3374517)

**MOSS (Moss Image / kromoss)**
- `stylr-blender3d-nai5-moss` — `@blender` · strength not stated · 1,508 dl · Moss&Anima-V2.0 触发词：@blender, 辅助提示词：dreamy smooth polished body rendering, wet oily skin look, anime · [source](https://civitai.com/models/3028260?modelVersionId=3441491)
- `3dcg-master-ultimate-stylized-cg-skin-glos-v3-moss` — `style_3dcg_master` · strength `1.0` (stated) · 964 dl · # 🌟 3DCG Master: Stylized Anime 3D & Skin Gloss LoRA > 🔥 Latest Version: V3 (Pure Anime 3D & Style B · [source](https://civitai.com/models/3018834?modelVersionId=3431432)

- Suggest ingest: [3D rendering style](https://civitai.com/models/73756) (sdxl, 177,723 dl) — `3DMM` · strength `2` (stated) — **downloads 177723 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Pixel Art XL](https://civitai.com/models/120096) (sdxl, 120,889 dl) — trigger not stated · strength not stated — **downloads 120889 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Illustrious  Pixel Art XL & 1.5 By creativehotia](https://civitai.com/models/43820) (illustrious, 55,968 dl) — `pixel` · strength `1` (stated) — **downloads 55968 >= 2x best available (24024) in same family+category**

### 9. Fantasy, sci-fi, cyberpunk, horror worlds

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
- `dark-fantasy-90-s-anime-style-illustriousx-ill` — `dark_fantasy_style, dark fantasy, retro,` · strength `0.8` (stated) · 5,191 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : dark_fantasy_style, dark fantasy,  · [source](https://civitai.com/models/1108959?modelVersionId=1245970)

**SDXL**
- `raven-mercer-a-gothic-beauty-with-a-danger-xl` — `cfRavenWoman` · strength not stated · 24 dl · [source](https://civitai.com/models/3047362?modelVersionId=3464623)

**Pony (Pony Diffusion XL)**
- `karin-cecil-vongielen-space-pirate-sara-uc-pony` — `vongielentwin`, `black hair`, `long hair`, `red eyes` · strength not stated · 302 dl · Base version, trained here on Civitai 6 Epochs, 99 uncropped pictures, 0.3 threshhold, 20 tags, 3 re · [source](https://civitai.com/models/1191236?modelVersionId=1341210)
- `sara-scorpion-pirat-sala-uchuu-kaizoku-sar-pony` — `Sara_Scorpion`, `blonde hair, blue eyes, long hair, side-swept bangs, earrings,`, `dark blue coat, long coat, open coat, red inner coat, high collar, sho`, `visual novel style, game cg,` · strength not stated · 180 dl · First version of the 50th Lora. · [source](https://civitai.com/models/2486705?modelVersionId=2795758)

**Anima**
- `moriimee-gothic-niji-journey-style-anima` — `realistic` · strength `0.8-1` (stated) · 3,603 dl · Trained on Anima with 36 pictures. Best result with weight between : 0.8-1. Prompts : realistic Insp · [source](https://civitai.com/models/2485109?modelVersionId=2945538)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-5` — `retro_scifi_90s_anime_style, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 2,778 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=2808683)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-2` — `retro_scifi_90s, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 1,803 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=3346833)

**MOSS (Moss Image / kromoss)**
- `80s-fantasy-movie-moss` — `ArsMovieStill, 80s Fantasy Movie Still` · strength not stated · 483 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3413429)
- `cyberpunk-realism-moss` — trigger not stated · strength not stated · 387 dl · This should create some cyperpunk style for ANIMA · [source](https://civitai.com/models/2628831?modelVersionId=3430753)

- Suggest ingest: [Velvet's Mythic Fantasy Styles / Flux + Pony + illustrious + ZiT + Ani](https://civitai.com/models/599757) (illustrious, 250,565 dl) — `C0lorL1nes` · strength not stated — **downloads 250565 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Popyay's Epic Fantasy Style / Pony & SDXL](https://civitai.com/models/470073) (sdxl, 55,842 dl) — trigger not stated · strength not stated — **downloads 55842 >= 2x best available (3670) in same family+category**
- Suggest ingest: [MGE Monster Girls](https://civitai.com/models/556479) (illustrious, 36,393 dl) — trigger not stated · strength not stated — **downloads 36393 >= 2x best available (9653) in same family+category**

### 10. A specific character or identity

Search `data/loras.jsonl` by the character name (`rg -i name`). Use ONE identity LoRA per person. Adults only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `defeated-waifu-imminent-penetration-concep-ill` — `defeatedwaifu`, `humiliation`, `slave`, `imminent penetration` · strength not stated · 13,616 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/934757?modelVersionId=1335609)
- `miniature-mini-girl-and-penis-diffusion-ill` — `MinigirlPenisQuiron`, `minigirl` · strength `0.7 - 2.5` (stated) · 4,089 dl · 👑 Miniature Mini Girl and Penis Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 T · [source](https://civitai.com/models/1421294?modelVersionId=1606496)
- `Coochies_Manager_-_Art_of_Jaguar_v1.0` **[HF repo only - needs adding to Graydient]** — `c00chiesManager, 1girl, white hair, short hair, grey eyes, huge breast`, `white shirt, pencil skirt, necktie, garter straps, thighhighs, side sl` · strength `1.5` (stated) · 95 dl · Diner manager from art of Jaguar. Sometimes you might need to crank up the strength to 1.5 to get re · [source](https://civitai.com/models/2018495?modelVersionId=2284476)

**SDXL**
- `pornmaster-age-differencesize-differencesu-xl` — trigger not stated · strength not stated · 4,715 dl · SDXL模型使用自然语言效果更好。 SDXL models work better using natural language. -- SDXL-V1基于PornMaster-Pro-SDXL-V1 · [source](https://civitai.com/models/279071?modelVersionId=1067539)
- `age-difference-old-woman-young-man-xl` — trigger not stated · strength not stated · 438 dl · [source](https://civitai.com/models/2699607?modelVersionId=3031574)

**Pony (Pony Diffusion XL)**
- `defeated-waifu-imminent-penetration-concep-pony` — `defeatedwaifu`, `humiliation`, `slave`, `imminent penetration` · strength not stated · 7,066 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/934757?modelVersionId=1046362)
- `taimanin-rpgx-character-collection-concept-pony` — `taimanincc, 1 girl, Solo Focus, character profile title text, Simple b` · strength not stated · 2,837 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=618819)

**Anima**
- `draco-malfoid-malfoy-redteneri-genderswap-anima` — `femdraco, 1girl, blonde hair, long hair, asymmetrical bangs, parted ha`, `hogwarts school uniform, black robe, grey sweater, collared shirt, gre` · strength not stated · 3,480 dl · Based on Redteneri's Genderswap Draco Prompts: femdraco, 1girl, pale blonde hair, long hair, asymmet · [source](https://civitai.com/models/2967285?modelVersionId=3362156)
- `taimanin-rpgx-character-collection-concept-anima` — `1girl, white background, character name, character profile, multi-fram`, `((TITLE TEXT:2,"***Character Name***", ***Character Name***))` · strength not stated · 1,535 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=3051237)

**Krea2 (detailed-krea2)**
- `alt-girl-e-girl-krea2` — trigger not stated · strength not stated · 9,378 dl · Trigger word AltGirl · [source](https://civitai.com/models/2274840?modelVersionId=3198266)
- `realisitc-good-girl-krea2` — `rggl` · strength `1-1.25` (stated) · 5,505 dl · (0, 0.25, 0.5, 0.75, 1, 1.25 in lora strength) Hello friends! Let the beautiful girls out! Things To · [source](https://civitai.com/models/2898581?modelVersionId=3277262)

**MOSS (Moss Image / kromoss)**
- `luisap-nsfw-tweak-moss` — trigger not stated · strength not stated · 2,092 dl · There no exactly a important use of this lora it's just some custom selection of data that give a su · [source](https://civitai.com/models/3016687?modelVersionId=3424542)
- `malfoid-genderbent-draco-malfoy-meme-chara-moss` — `M4lfoid` · strength not stated · 1,454 dl · Krea 2 and MOSS character LoRA for Malfoid (Genderbent Draco Malfoy). How to use Trigger word: M4lfo · [source](https://civitai.com/models/3021116?modelVersionId=3435645)

- Suggest ingest: [NSFW MASTER](https://civitai.com/models/667086) (krea2, 236,423 dl) — trigger not stated · strength `0.8` (stated) — **downloads 236423 >= 2x best available (9378) in same family+category**
- Suggest ingest: [All Disney Princess XL LoRA Model from Ralph Breaks the Internet](https://civitai.com/models/212532) (illustrious, 209,305 dl) — trigger not stated · strength not stated — **downloads 209305 >= 2x best available (13616) in same family+category**
- Suggest ingest: [NiceGirls UltraReal](https://civitai.com/models/1862761) (anima, 161,022 dl) — trigger not stated · strength `0.6-0.8` (stated) — **downloads 161022 >= 2x best available (3480) in same family+category**

### 11. Lighting and atmosphere

Describe a single motivated light source in prose too.

**Illustrious / NoobAI (Illustrious-XL based)**
- `maya-ibuki-neon-genesis-evangelion-ill` — `Maya_Ibuki`, `hat, uniform, black hair, beret, boots, black footwear, black eyes, mi`, `1girl, uniform, brown hair, short hair, pantyhose, military uniform, b` · strength not stated · 1,222 dl · Maya Ibuki from EVA Tragger word: Maya_Ibuki Outfit 1: 1girl, uniform, brown hair, short hair, panty · [source](https://civitai.com/models/1613043?modelVersionId=1825441)
- `digitaldelights-impossible-downward-dog-ill` — `<Lora:DigitalDelights-impossible-downward-dog:1>, top-down bottom-up, ` · strength not stated · 1,130 dl · Name is self explanatory it's a yoga pose named dog down taking it to the extreme XD · [source](https://civitai.com/models/2143059?modelVersionId=2423989)

**Anima**
- `vixon-s-styles-gothic-neon-anima` — `g0thic n30n, neon lights, glowing` · strength not stated · 5,773 dl · the OG dataset now brought to anima! Hey guys! Hope you love using this new LoRA as much as I loved  · [source](https://civitai.com/models/888231?modelVersionId=3022620)
- `vixon-s-styles-gothic-neon-anima-2` — `cityscape`, `@g0thic, neon, glowing, neon lights, gothic` · strength not stated · 2,355 dl · the OG dataset now brought to anima! Hey guys! Hope you love using this new LoRA as much as I loved  · [source](https://civitai.com/models/888231?modelVersionId=2934771)

**Krea2 (detailed-krea2)**
- `neon-vhs-dreams-krea2` — trigger not stated · strength `0.8–1.0` (stated) · 1,189 dl · ☕ Like my work? Feel free to support me on Ko-fi: https://ko-fi.com/granddyser Thanks! 🙏 Neon VHS Dr · [source](https://civitai.com/models/2987989?modelVersionId=3387832)
- `fleshlight_000006750` — `fleshlight` · strength not stated · 992 dl · Man masturbating with a fleshlight. Training captions include the following (but does not always wor · [source](https://civitai.com/models/2766256?modelVersionId=3113736)

**MOSS (Moss Image / kromoss)**
- `realistic-night-outdoor-photo-real-streetl-moss` — trigger not stated · strength not stated · 363 dl · Photos taken outdoors at night: bus stops, street food stalls, canal railings, parking lots, rooftop · [source](https://civitai.com/models/3048122?modelVersionId=3465868)
- `amish-barn-straw-hats-suspenders-light-thr-moss` — trigger not stated · strength not stated · 187 dl · An Amish farm in Pennsylvania: weathered wide-plank barns, hay, wooden gates, gravel yards, buggies  · [source](https://civitai.com/models/3034848?modelVersionId=3448284)

- Suggest ingest: [S1 Dramatic Lighting](https://civitai.com/models/661736) (illustrious, 63,463 dl) — `s1_dram` · strength not stated — **downloads 63463 >= 2x best available (3749) in same family+category**
- Suggest ingest: [Smooth Lighting Enhancer (NoobAI/Illustrious)](https://civitai.com/models/1204179) (illustrious, 24,842 dl) — trigger not stated · strength `0.5` (stated) — **downloads 24842 >= 2x best available (3749) in same family+category**
- Suggest ingest: [Luke's Neon Clothing and Accessories (Illustrious + Flux + Pony + 1.5 ](https://civitai.com/models/422657) (sdxl, 22,996 dl) — `glowing-neon-colour-clothing`, `blue, green, pink, orange, red, yellow, purple`, `skirt, jacket, shirt, tank top, shorts, hijab, pants, thighhighs, biki` · strength `0.5-0.7` (stated) — **no Graydient LoRA in this family+category**

### 12. Detail / aesthetic / stabilizer enhancers

Use at most one; start low and raise only if the image gets soft.

**Illustrious / NoobAI (Illustrious-XL based)**
- `add-micro-details-concept-ill-2` — `addmicrodetails` · strength not stated · 17,180 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=2832991)
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)

**SDXL**
- `trendcraft-the-peoples-style-detailer-base-xl` — trigger not stated · strength not stated · 1,779 dl · Image sources include only Illustrious and NoobAI models. No realistic content. No X or higher rated · [source](https://civitai.com/models/1390819?modelVersionId=1768080)
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)

**Pony (Pony Diffusion XL)**
- `trendcraft-the-peoples-style-detailer-xl-b-pony` — trigger not stated · strength not stated · 2,847 dl · V2.0 new tagging method used · [source](https://civitai.com/models/1378661?modelVersionId=1557746)
- `add-micro-details-concept-pony-3` — `addmicrodetails` · strength not stated · 2,703 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=1961984)

**Anima**
- `hentai-studio-quality-illustriousxl-zimage-anima` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 12,234 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=2814440)
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)

**Krea2 (detailed-krea2)**
- `realism-enhancer-krea2` — trigger not stated · strength not stated · 16,530 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2727284?modelVersionId=3065628)
- `Emotions V1` — `Detailed Emotions and Expressions` · strength not stated · 10,258 dl · LEAVE A TIP IF YOU LIKE IT, I AM OUT OF BUZZ!! What it does: - Detailed and mostly accurate emotions · [source](https://civitai.com/models/2829908?modelVersionId=3193133)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
- `pornmaster-moss-detail-slider-xl` — trigger not stated · strength not stated · 4,239 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -6 to +8 使用正面lora權重時增加增細節，使用負面lora權重時降低細節。 LoRA  · [source](https://civitai.com/models/3010274?modelVersionId=3416145)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**
- Suggest ingest: [Stabilizer IL/NAI/CK](https://civitai.com/models/971952) (illustrious, 161,491 dl) — trigger not stated · strength not stated — **downloads 161491 >= 2x best available (17180) in same family+category**

### 13. Turbo, distill and speed LoRAs

Only on a matching fast/turbo workflow; never stack with a full-step look at high strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)
- `hyper-huge-gape-xl` — `HyperAGapeQuiron`, `extreme anal gape`, `extreme gape` · strength `0.7 - 1.5` (stated) · 4,602 dl · 👑 Hyper A Gape Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 This LORA is capab · [source](https://civitai.com/models/109087?modelVersionId=1632779)

**SDXL**
- `hyperpregnant-hyperpregnancy-il-sd-xl` — `hyperpregnant, huge belly` · strength not stated · 110 dl · Makes characters extremely pregnant, have fun! · [source](https://civitai.com/models/1703222?modelVersionId=1927565)

**Pony (Pony Diffusion XL)**
- `hyper-huge-gape-diffusion-sd1-5-pony` — `hugeAnusGapeQuiron`, `anal gape`, `hyper anus gape`, `gaping` · strength `0.7 - 1.5` (stated) · 5,757 dl · 👑 Hyper A Gape Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 This LORA is capab · [source](https://civitai.com/models/109087?modelVersionId=1006302)
- `Kissing Fetish Hyperlips Kissing Concept LoRA - v1.0 - Kissing_Fetish__Hyperlips_Kissing_Concept_LoRA-000039` — `Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy,` · strength not stated · 1,183 dl · [source](https://civitai.com/models/1162938?modelVersionId=1308166)

**Anima**
- `hentai-studio-quality-illustriousxl-zimage-anima` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 12,234 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=2814440)
- `2-9b-turbo-remapped-anima` — trigger not stated · strength not stated · 3,853 dl · Turbo LoRA for Anima-2.9 if you're having problems with the OG lora. It's just a temporary solution  · [source](https://civitai.com/models/2857451?modelVersionId=3227488)

**Krea2 (detailed-krea2)**
- `hyperdetailed-colored-pencil-krea2` — `ArsMJStyle, Colored pencil hyperdetailed realism,` · strength `1.2` (stated) · 3,656 dl · A LoRA inspired by one of my favourite styles of hyperdetailed colored pencil illustrations. This st · [source](https://civitai.com/models/1155749?modelVersionId=3113897)
- `god-tier-tits-zimage-turbo-flux-ill-krea2` — `GodTierTits` · strength `1.0` (stated) · 2,021 dl · Krea2 added using v1.1 dataset! ZiT added using v1.1 dataset! This one can handle strengths up to th · [source](https://civitai.com/models/961829?modelVersionId=3312813)

**MOSS (Moss Image / kromoss)**
- `turbo-loras-moss` — trigger not stated · strength not stated · 11,500 dl · I'll be uploading different Moss Image Turbo LoRAs I use here and crediting the original creators. I · [source](https://civitai.com/models/3006599?modelVersionId=3414934)
- `hentai-studio-quality-illustriousxl-zimage-moss` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 2,393 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=3420914)

- Suggest ingest: [Anima Turbo LoRA](https://civitai.com/models/2560840) (anima, 82,342 dl) — trigger not stated · strength `1` (stated) — **downloads 82342 >= 2x best available (13445) in same family+category**
- Suggest ingest: [LCM-LoRA Weights - Stable Diffusion Acceleration Module](https://civitai.com/models/195519) (sdxl, 78,879 dl) — trigger not stated · strength not stated — **downloads 78879 >= 2x best available (369) in same family+category**
- Suggest ingest: [SDXL Lightning LoRAs](https://civitai.com/models/350450) (sdxl, 72,507 dl) — trigger not stated · strength not stated — **downloads 72507 >= 2x best available (369) in same family+category**

### 14. Sliders (weight, size, expression, realism)

Sliders usually accept negative strengths; the source page states the range. Age sliders are excluded from this KB.

**Illustrious / NoobAI (Illustrious-XL based)**
- `large_areolae_addift` — `large areolae` · strength not stated · 10,181 dl · Areolae size slider · [source](https://civitai.com/models/1384966?modelVersionId=1565020)
- `long_nipples_addift_v2` — `long nipples` · strength not stated · 6,613 dl · Nipple length slider · [source](https://civitai.com/models/1384979?modelVersionId=1771546)

**SDXL**
- `thick-xl-thin-thick-body-build-slider-xl` — trigger not stated · strength not stated · 369 dl · [source](https://civitai.com/models/2893137?modelVersionId=3271132)
- `bewbs-breast-size-slider-xl` — trigger not stated · strength not stated · 265 dl · [source](https://civitai.com/models/2947454?modelVersionId=3337780)

**Pony (Pony Diffusion XL)**
- `abs-slider-pony` — trigger not stated · strength `0 to 2` (stated) · 867 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2513137?modelVersionId=2879098)
- `muscle-slider-pony` — trigger not stated · strength `0 to 2` (stated) · 589 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2518673?modelVersionId=2881011)

**Anima**
- `Breasts slider - Anima - Breasts_Size_SliderAnima6` — trigger not stated · strength not stated · 13,445 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2100839?modelVersionId=2974098)
- `Mature slider - Anima - MatureFemaleSliderAnima` — trigger not stated · strength not stated · 11,760 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2118055?modelVersionId=2979797)

**Krea2 (detailed-krea2)**
- `penis-size-krea2` — `penis-size-krea2` · strength not stated · 21,904 dl · https://wallofthieves.com/  Krea 2 - V2 V2 is here, and it is MUCH better then V1. Improvements: - M · [source](https://civitai.com/models/2687793?modelVersionId=3154138)
- `pornmaster-age-slider-krea2` — `pornmaster age slider krea2` · strength not stated · 16,394 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師-Krea2 V1: 權重-9 to +9 lora權重:+9 to -? 如果要增強老年人的效果可以寫上:皮膚有許多皺紋。 · [source](https://civitai.com/models/2772293?modelVersionId=3121449)

**MOSS (Moss Image / kromoss)**
- `pornmaster-moss-realism-slider-xl` — trigger not stated · strength `2` (stated) · 5,479 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -2 to +4.5 使用正面lora權重時增加增真實感，使用負面lora權重時增加2d感。 L · [source](https://civitai.com/models/3010059?modelVersionId=3415845)
- `pornmaster-moss-detail-slider-xl` — trigger not stated · strength not stated · 4,239 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -6 to +8 使用正面lora權重時增加增細節，使用負面lora權重時降低細節。 LoRA  · [source](https://civitai.com/models/3010274?modelVersionId=3416145)

- Suggest ingest: [Penis Size Slider - Pony/Illustrious](https://civitai.com/models/465379) (illustrious, 123,867 dl) — `Futanari` · strength not stated — **downloads 123867 >= 2x best available (12347) in same family+category**
- Suggest ingest: [Breast Size Slider - Pony / Illustrious](https://civitai.com/models/481016) (illustrious, 104,242 dl) — trigger not stated · strength not stated — **downloads 104242 >= 2x best available (12347) in same family+category**
- Suggest ingest: [extremely detailed (no trigger) - sliders.ntcai.xyz](https://civitai.com/models/229213) (sdxl, 102,055 dl) — `extremely detailed` · strength not stated — **downloads 102055 >= 2x best available (369) in same family+category**

### 15. Breasts, nipples and chest anatomy

Use an anatomy LoRA only if the base model draws the area poorly.

**Illustrious / NoobAI (Illustrious-XL based)**
- `grabbing-breasts-ill` — `grabbing breasts` · strength not stated · 10,744 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=1389783)
- `breasts-squeeze-xl-ill` — `breasts squeeze, breasts, cleavage` · strength not stated · 3,341 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/849396?modelVersionId=961201)
- `marie-breast-helper_epoch_12-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `flat-chest-xl` — `flat body` · strength `1.0` (stated) · 605 dl · Updated dataset  Tags - flatties, flat-chest, flat, chest, petite, nipples, solo, 1girl, nude, navel · [source](https://civitai.com/models/2240675?modelVersionId=3145094)
- `huge-sag-breasts-xl` — trigger not stated · strength not stated · 223 dl · [source](https://civitai.com/models/2939810?modelVersionId=3328196)

**Pony (Pony Diffusion XL)**
- `grabbing-breasts-pony` — `grabbing breasts` · strength not stated · 7,694 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=705069)
- `small-saggy-breasts-pony` — trigger not stated · strength not stated · 3,700 dl · [source](https://civitai.com/models/704319?modelVersionId=947120)

**Anima**
- `nipple-anima-2` — `nipples` · strength `0.6–0.8` (stated) · 7,807 dl · [MOSS] The usage is the same as Anima. Forge Neo: The effect of Adetailer is a bit weak. Turbo: It m · [source](https://civitai.com/models/2385403?modelVersionId=3036905)
- `grabbing-breasts-anima` — `grabbing breasts` · strength not stated · 3,829 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=2933804)

**Krea2 (detailed-krea2)**
- `breasts-helper-v1-krea2` — `HMBreasts` · strength `0.9` (stated) · 7,142 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2740401?modelVersionId=3081828)
- `ski-slope-breasts-mh3-ani-kr2-zit-f1d-pny-krea2` — `SteepSlopeTiddies` · strength `1.10` (stated) · 6,701 dl · Moss XXL / MH3 XXL / Ani XXL / Krea2 XXL / ZiT XXL / ZiT 1.2 / F1D XXL / F1D 1.2 / PNY 1.2 / ILL 1.2 · [source](https://civitai.com/models/942483?modelVersionId=3112303)

**MOSS (Moss Image / kromoss)**
- `tiny-tits-small-breasts-v0297-krea2` — `tyneetitpn` · strength `1.15` (stated) · 10,662 dl · MOSS Small breasts puffy nipples Best strength for me was around 1.15.  Trigger: tyneetitspn Some sa · [source](https://civitai.com/models/2733121?modelVersionId=3440297)
- `moss-natural-breasts-xl` — trigger not stated · strength `0.8–1.0` (stated) · 2,420 dl · Natural Breasts — for MOSS Image A small, focused LoRA for natural breast shape on MOSS-Image. It do · [source](https://civitai.com/models/3010783?modelVersionId=3416833)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [Sagging Breasts](https://civitai.com/models/139131) (illustrious, 89,056 dl) — `sagging breasts`, `breasts apart` · strength `1.0` (stated) — **downloads 89056 >= 2x best available (10931) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**

### 16. Penis, scrotum and futa anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `penis-size-difference-ill` — `PSDER, penis size difference, penis, (2boys:1.7), 1girl,  small penis,` · strength `0.6-1.0` (stated) · 8,863 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=1245271)
- `Small Penis - Feminization - SPH - Illustrious - cute_v1.5` — `cute_penis` · strength not stated · 7,251 dl · Twice the gurls and even daintier bits! I've updated the first concept model I created. I incorporat · [source](https://civitai.com/models/1514972?modelVersionId=1738881)

**SDXL**
- `futanari-pegging-male-hassaku-v1-xl` — `Futa_Pegging_Male`, `futa on male, futa pegging male, anal sex,` · strength not stated · 2,769 dl · [source](https://civitai.com/models/790941?modelVersionId=884496)
- `all-in-one-lying-on-back-female-male-futa-xl` — trigger not stated · strength not stated · 2,306 dl · [source](https://civitai.com/models/810132?modelVersionId=905931)

**Pony (Pony Diffusion XL)**
- `ponyillustrious-futa-xl` — `futa with female, 1futa, breasts, 2girls`, `sex,`, `fellatio,`, `vaginal,` · strength not stated · 5,919 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1107758?modelVersionId=1254269)
- `hentai-futanari-girls-sex-random-generator-pony` — `(2 girls:1.1),(2 penises:1.1), futanari, futa, (futa with futa:1.1), y` · strength not stated · 4,188 dl · [source](https://civitai.com/models/589732?modelVersionId=658463)

**Anima**
- `concept-wet-penis-saliva-pussy-juice-anal-anima` — `pussy juice on penis`, `saliva on penis`, `anal fluid on penis` · strength not stated · 2,764 dl · This is an experimental initial release. This LoRA focuses specifically on coating the penis with va · [source](https://civitai.com/models/2627734?modelVersionId=3222610)
- `penis-size-difference-anima` — `penis size difference` · strength `0.6-1.0` (stated) · 2,479 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=3027209)

**Krea2 (detailed-krea2)**
- `femboy-shemale-flaccid-or-small-penis-krea2` — `femboy shemale flaccid or small penis krea2` · strength `1.0` (stated) · 5,728 dl · v Krea 2 Krea version 2 works without any bypass LoRAs or similar censorship modifications. It uses  · [source](https://civitai.com/models/2054525?modelVersionId=3096065)
- `hmcockface-cock-on-face-krea2` — `HMCockFace` · strength `0.9` (stated) · 4,173 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2753674?modelVersionId=3098191)

**MOSS (Moss Image / kromoss)**
- `flaccid-vtx-flaccid-uncut-penis-moss` — `flaccid penis` · strength not stated · 1,143 dl · Not sure if I like MOSS over Krea 2 for photorealism, but it's really fast and can do a wider variet · [source](https://civitai.com/models/3008280?modelVersionId=3413532)
- `f-ing-dick-moss` — trigger not stated · strength not stated · 1,058 dl · Note: You can significantly improve the quality by using a BBOX (Bounding Box) to show the model whe · [source](https://civitai.com/models/3014843?modelVersionId=3422079)

- Suggest ingest: [Nipples XL](https://civitai.com/models/171014) (sdxl, 73,706 dl) — `oval nipples`, `puffy nipples`, `dark nipples`, `ghost nipples` · strength not stated — **downloads 73706 >= 2x best available (1707) in same family+category**
- Suggest ingest: [[PonyXL/ILXL] Pull out Penis Cumtrail](https://civitai.com/models/467896) (illustrious, 40,651 dl) — `cum string, cumtrail, solo focus`, `cumtrail vagina to penis, , after sex, pulling out penis, cum on penis`, `cumtrail mouth to penis, , pulling out penis, after oral, after ferrat`, `cumtrail breast to penis, , pulling out penis, after paizuri, cum on b` · strength not stated — **downloads 40651 >= 2x best available (10931) in same family+category**
- Suggest ingest: [Penis Worship](https://civitai.com/models/514556) (illustrious, 39,536 dl) — `penis worship`, `heart-shaped pupils`, `penis on face`, `penis on head` · strength `0.4 - 0.6` (stated) — **downloads 39536 >= 2x best available (10931) in same family+category**

### 17. Vulva, vagina and anus anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `mating-press-wide-spread-focus-right-befor-ill` — `mating press`, `focus` · strength `1` (stated) · 13,255 dl · 💖 Support & Share the Magic!  Love these tools? Like, add to collection, and tag this resource in yo · [source](https://civitai.com/models/1280616?modelVersionId=1444772)
- `pussy-juice-ill` — `pussy juice` · strength not stated · 10,931 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=1135306)
- `Marie-PussyPlayground_2_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `Marie-PussyPlayground_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `gaping-assholes-all-fours-sdxl1-0-concept-xl` — `GapingAssholesAllFourQuiron pose`, `all fours`, `from behind`, `spread ass` · strength not stated · 7,022 dl · 👑 Gaping Assholes All Fours LORA 👑 SDXL1.0 v5.1p 🔧Model base: SDXL1.0 📝🌟 Trigger: (GapingAssholesAll · [source](https://civitai.com/models/130866?modelVersionId=143716)
- `all-in-one-lying-on-back-female-male-futa-xl` — trigger not stated · strength not stated · 2,306 dl · [source](https://civitai.com/models/810132?modelVersionId=905931)

**Pony (Pony Diffusion XL)**
- `hentai-pussy-inspection-2shot-il-2-pony` — `solo, multiple views, close-up, looking at viewer, cowboy shot, nude, `, `(Multiple layers),solo, full body, cowboy shot, standing, sweat, oily ` · strength not stated · 11,319 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=639693)
- `pussy-juice-pony` — `pussy juice` · strength not stated · 9,912 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=601324)
- `Marie-pussyplayground_v3_epoch_12-pony` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `mcb-pussy-helper_epoch_10-pony` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Anima**
- `pussy-juice-anima` — `pussy juice` · strength not stated · 4,376 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=2981405)
- `hentai-pussy-inspection-2shot-il-2-anima` — `hpi2, 1 girl, full body, cowboy shot, Clothed girl and nude girl, Cove` · strength not stated · 4,203 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=3055825)

**Krea2 (detailed-krea2)**
- `krea2filterbypass-krea2` — trigger not stated · strength `1.0` (stated) · 32,481 dl · Since people can't read. Strength can be used at 1.0 all the way up to 40000.0 If you use poorly qua · [source](https://civitai.com/models/2728234?modelVersionId=3067151)
- `anal-helper-krea2` — `anal-helper-krea2` · strength not stated · 17,728 dl · https://wallofthieves.com/  Anal Helper LoRA (Not a slider) I have found it frustrating that most Lo · [source](https://civitai.com/models/2759414?modelVersionId=3105253)
- `marie-pussyassist-krea2-v1e12` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**MOSS (Moss Image / kromoss)**
- `anal-assistant-for-moss` — trigger not stated · strength not stated · 1,617 dl · This should aid with all things Anal · [source](https://civitai.com/models/3037721?modelVersionId=3452026)
- `better-pussy-moss` — trigger not stated · strength not stated · 1,113 dl · Moss knows anatomy pretty well out of the box but i find it likes to make multiple labia lips, or st · [source](https://civitai.com/models/3039119?modelVersionId=3453860)

- Suggest ingest: [Labiaplasty Innie Pussy Adjuster [KR2 K9B ZImage SDXL Qwen Chroma SD1]](https://civitai.com/models/112299) (krea2, 176,773 dl) — trigger not stated · strength not stated — **downloads 176773 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Lily](https://civitai.com/models/86788) (sdxl, 99,961 dl) — `pussy_front`, `pussy_rear`, `toys_front`, `toys_rear` · strength not stated — **downloads 99961 >= 2x best available (1707) in same family+category**
- Suggest ingest: [Real Pussy - Peach](https://civitai.com/models/99174) (sdxl, 87,846 dl) — `pussy_scale1`, `pussy_scale2`, `pussy_scale3` · strength not stated — **downloads 87846 >= 2x best available (1707) in same family+category**

### 18. Hands, feet, face and small anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-pussy-inspection-gaping-pussy-opene-ill` — `(gaping pussy opened in fingers),(Put fingers in Vagina), (spread Vagi`, `(close-up clitoris), (close-up layers:1.2),(Multiple layers:1.2), (mul` · strength not stated · 5,194 dl · Inspection out Your WIFE's PUSSY!! Width:832 Height:1216 is best Width:1216 Height:832 is best SAMPL · [source](https://civitai.com/models/870724?modelVersionId=2165255)
- `two-finger-handjob-crotch-pov-pinching-han-ill` — `tf handjob, crotch pov, penis, male pov,`, `1girl,`, `blowjob, fellatio,`, `ejaculation,` · strength not stated · 3,951 dl · Version 1, kind of sucks. Version 2, actually functional this time. Recommend you use hand negative. · [source](https://civitai.com/models/853056?modelVersionId=1444623)

**SDXL**
- `cumface-xl` — `facial`, `cumface` · strength not stated · 1,094 dl · [source](https://civitai.com/models/1382629?modelVersionId=1562351)
- `push-head-down-face-against-floor-il-sd-xl` — `Face in pillow`, `push head down, hand on another's head` · strength not stated · 488 dl · [source](https://civitai.com/models/1726270?modelVersionId=1953666)

**Pony (Pony Diffusion XL)**
- `hentai-pussy-inspection-gaping-pussy-opene-pony` — `(dilation Vagina),(Put fingers in Vagina), (spread Vagina wide), (Perf` · strength not stated · 5,112 dl · Inspection out Your WIFE's PUSSY!! Width:832 Height:1216 is best Width:1216 Height:832 is best SAMPL · [source](https://civitai.com/models/870724?modelVersionId=974577)
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
- `MCB_hands_pony_epoch_10` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Anima**
- `lips-size-slider-anima` — trigger not stated · strength `0 to 2` (stated) · 3,339 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2533131?modelVersionId=3044145)
- `_feet_epoch_10` — `@feet, feet, toes, soles, tonails, whatever else` · strength not stated · 2,756 dl · Enjoy and share results! Suggestion Box (Higher chance of getting what you want if you attach an ima · [source](https://civitai.com/models/1293552?modelVersionId=3103124)

**Krea2 (detailed-krea2)**
- `hmcockface-cock-on-face-krea2` — `HMCockFace` · strength `0.9` (stated) · 4,173 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2753674?modelVersionId=3098191)
- `krea2 sex 淫模 - FJ - krea2 footjob` — `krea2fotjob, footjob, 1girl, fishnets, feet, hetero, penis, 1boy, pant` · strength `0.6–0.7` (stated) · 3,299 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3187149)

**MOSS (Moss Image / kromoss)**
- `door-peephole-view-fisheye-visitor-at-the-moss` — trigger not stated · strength not stated · 729 dl · Looking out through an electronic door peephole: a high fisheye angle with the visitor in the center · [source](https://civitai.com/models/3019310?modelVersionId=3427972)
- `feet-moss` — trigger not stated · strength `0.7` (stated) · 543 dl · A bare-feet concept LoRA for MOSS-Image. Trigger word: feet Trained on 300 real studio photographs ( · [source](https://civitai.com/models/3022702?modelVersionId=3432393)

- Suggest ingest: [Hands XL + SD 1.5 + F1D + Pony + Illustrious + zit + ZIB](https://civitai.com/models/200255) (illustrious, 314,114 dl) — `detailed` · strength not stated — **downloads 314114 >= 2x best available (10931) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Detailed Perfection style (Hands + Feet + Face + Body + All in one) XL](https://civitai.com/models/411088) (illustrious, 139,148 dl) — `detailed` · strength not stated — **downloads 139148 >= 2x best available (17180) in same family+category**

### 19. Body type, muscle, curves, tan lines

**Illustrious / NoobAI (Illustrious-XL based)**
- `small-but-hung-xl` — `small but hung`, `size difference` · strength not stated · 2,869 dl · v1.1 More refined (i hope), test it out! That said, use whichever fits for u and give feedback if ab · [source](https://civitai.com/models/1991612?modelVersionId=2263536)
- `bottom_up_spread_epoch_10` — `bottom_up_spread, 1girl, solo,  lying,  looking at viewer, on back, sp`, `hip lift,` · strength not stated · 1,359 dl · lora for a sexy posing. A girl spreads legs and lifts her hip. · [source](https://civitai.com/models/2631708?modelVersionId=2954783)

**SDXL**
- `muscle-mommy-female-bodybuilder-fbb-flux-i-xl` — `Muscl3-m0mmy` · strength not stated · 179 dl · Create your own sexy muscle mommy, have fun! · [source](https://civitai.com/models/1262213?modelVersionId=1423389)

**Pony (Pony Diffusion XL)**
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
- `futa-self-cock-worship-pony` — `Self-Licking, Self-Worship,`, `Licking cock` · strength not stated · 1,558 dl · Beta · [source](https://civitai.com/models/1250501?modelVersionId=1409664)

**Anima**
- `Concept Body bridge - v0.0.0 - body_bridge_v0.0.0_0600_cosine-0025` — `body bridge`, `on back`, `arm support`, `tiptoes` · strength not stated · 1,741 dl · I found it difficult to achieve a pose where the body bends into a bridge-like shape, curving like a · [source](https://civitai.com/models/2875579?modelVersionId=3249483)
- `body-writing-erotic-anima` — `body writing,` · strength `1` (stated) · 1,571 dl · Recommended weight： 1 Trigger prompts ： body writing,  Tried making an anima version with a "Body Wr · [source](https://civitai.com/models/2951684?modelVersionId=3343038)

**Krea2 (detailed-krea2)**
- `Krea2 milf body - V1 - milfbodyhms_v1` — `(fupa:1.2)`, `rounded pubic mound`, `saggy buttocks`, `rounded lower abdomen` · strength not stated · 4,091 dl · try the following: (fupa:1.2) - increase strength for a more distended lower abdomen. I've come to l · [source](https://civitai.com/models/2784421?modelVersionId=3137009)
- `z-female-body-retouched-krea2` — trigger not stated · strength `2.0` (stated) · 2,990 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3186931)

**MOSS (Moss Image / kromoss)**
- `z-female-body-retouched-xl` — trigger not stated · strength `0.6-1.0` (stated) · 1,346 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3413047)
- `thick-inner-labia-moss` — `th1ck-l4b1a	Her pussy has thick inner labia` · strength not stated · 769 dl · try: th1ck-l4b1a Her pussy has thick protruding inner labia, shown curly wrinkled and saggy Yes, I k · [source](https://civitai.com/models/3032886?modelVersionId=3445800)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [BFS - Best Face Swap](https://civitai.com/models/2027766) (krea2, 110,251 dl) — `body_swap: replace the person with the reference person.` · strength not stated — **downloads 110251 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Cameltoe](https://civitai.com/models/137423) (sdxl, 63,670 dl) — `cameltoe_body`, `cameltoe_hips`, `cameltoe_pussy` · strength not stated — **downloads 63670 >= 2x best available (1707) in same family+category**

### 20. Lingerie, latex, bodysuits, corsets

**Illustrious / NoobAI (Illustrious-XL based)**
- `cat-lingerie-ill` — trigger not stated · strength `0.7` (stated) · 3,088 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2711788)
- `thin-bodysuit-ill` — `th1nbodysu1t`, `highleg` · strength `0.8` (stated) · 2,149 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=1417556)

**SDXL**
- `thin-bodysuit-xl` — `th1nbodysu1t` · strength `0.8` (stated) · 1,359 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=388278)
- `thong-upskirt-xl` — trigger not stated · strength not stated · 178 dl · [source](https://civitai.com/models/2898091?modelVersionId=3276640)

**Pony (Pony Diffusion XL)**
- `costumefishnet-bodysuit-request-pony` — `fishnet bodysuit` · strength not stated · 4,406 dl · [source](https://civitai.com/models/815349?modelVersionId=911750)
- `costumelatex-outfit-request-pony` — `latex shrug (clothing), latex legwear, reverse outfit` · strength not stated · 2,153 dl · [source](https://civitai.com/models/815828?modelVersionId=912285)

**Anima**
- `cat-lingerie-anima` — `cat lingerie`, `cat ear legwear` · strength `0.7` (stated) · 1,777 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2939201)
- `jav-race-queen-with-highleg-leotard-anima` — `jav fstu 033 032,  1girl, solo,  race queen, clothes writing, highleg `, `holding parasol,  Holding umbrella,`, `2boys, multiple boys,  taking picture, recording, camera boys, boys ar`, `2boys, mmf threesome, hetero, fingering, grabbing, group sex, leotard ` · strength `0.85 - 1` (stated) · 728 dl · This LORA was created to see if it could learn JAV and produce hentai anime. 📋Source material for tr · [source](https://civitai.com/models/2861588?modelVersionId=3232553)

**Krea2 (detailed-krea2)**
- `thin-bodysuit-krea2` — `th1nbodysu1t` · strength `0.8` (stated) · 2,025 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=3154439)
- `thong-madness-krea2` — trigger not stated · strength not stated · 1,988 dl · Most krea2 models i use struggle to make tiny or string panties or thongs so i made this model to tr · [source](https://civitai.com/models/2995179?modelVersionId=3396864)

**MOSS (Moss Image / kromoss)**
- `micro-bikini-thong-pull-for-moss` — trigger not stated · strength `0.5` (stated) · 843 dl · This model generates a low cut sling style micro bikini. This model also does well with getting the  · [source](https://civitai.com/models/3022730?modelVersionId=3432428)
- `base-candid-adjusting-panties-moss` — `4dju5t1ng-p4nt135	She is adjusting her panties.` · strength not stated · 277 dl · generates mid-action shots of a woman adjusting her underwear try: 4dju5t1ng-p4nt135 She is adjustin · [source](https://civitai.com/models/3048896?modelVersionId=3466869)

- Suggest ingest: [クロッチずらし/panties aside(XL,Pony)](https://civitai.com/models/471385) (illustrious, 33,017 dl) — `panties aside, panties, pussy`, `anus` · strength not stated — **downloads 33017 >= 2x best available (6777) in same family+category**
- Suggest ingest: [セクシーランジェリー/babydoll,sexy lingerie(SD,ILL,pony)](https://civitai.com/models/522201) (illustrious, 25,785 dl) — `babydoll` · strength not stated — **downloads 25785 >= 2x best available (6777) in same family+category**
- Suggest ingest: [No Bra SDXL](https://civitai.com/models/137296) (sdxl, 17,694 dl) — `no bra`, `covered nipples` · strength not stated — **downloads 17694 >= 2x best available (1359) in same family+category**

### 21. Stockings, thigh-highs, heels and shoes

**Illustrious / NoobAI (Illustrious-XL based)**
- `costumeblack-bodystocking-request-ill` — `bodystocking` · strength not stated · 2,400 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=1244147)
- `bow-accent-kitten-heels-ill` — `highheels, bow,` · strength not stated · 1,318 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/256493?modelVersionId=1506248)

**SDXL**
- `lace-pantyhose-hooked-on-heel-meme-il-sd-xl` — `Pantyhose_hooked_on_heel, full body, from side, lying, on stomach, fee` · strength not stated · 49 dl · Creates the meme/viral pose where the character's high heel shoe is hooked on lace pantyhose. Very s · [source](https://civitai.com/models/2212567?modelVersionId=2491084)

**Pony (Pony Diffusion XL)**
- `costumeblack-bodystocking-request-pony` — `bodystocking` · strength not stated · 1,210 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=908485)
- `futa-presenting-in-pantyhose-pony` — trigger not stated · strength not stated · 813 dl · [source](https://civitai.com/models/1098370?modelVersionId=1233809)

**Anima**
- `costumeopaque-pantyhose-commission-anima` — `pantyhose, (color) pantyhose` · strength not stated · 698 dl · TAGS: pantyhose, (color) pantyhose ISSUES: sometimes control top or other seams appears · [source](https://civitai.com/models/2730158?modelVersionId=3069195)
- `costumeembroidered-thigh-highs-commission-anima` — `embroidered legwear, thighhighs, (color) thighhighs` · strength not stated · 672 dl · TAGS: embroidered legwear, thighhighs, (color) thighhighs commissions https://ko-fi.com/aiadoreyou · [source](https://civitai.com/models/2700511?modelVersionId=3032608)

**Krea2 (detailed-krea2)**
- `suspender-stockings-krea2` — `suspender_stockings` · strength not stated · 2,211 dl · A lora for a one-piece garment integrating stockings and garter belt. Keywords include fishnet, torn · [source](https://civitai.com/models/2087323?modelVersionId=3200743)
- `glossy-pantyhose-flux-krea2` — `glossy pantyhose flux krea2` · strength not stated · 1,631 dl · You can use it for glossy or shiny pantyhose. Testet on white, black, tan and brown. · [source](https://civitai.com/models/1443102?modelVersionId=3247385)

**MOSS (Moss Image / kromoss)**
- `heel-grabbers-base-moss` — trigger not stated · strength not stated · 190 dl · Its nice to see you again OBVIOUS PERSON OF TASTE! I spent some time making something your 1girl is  · [source](https://civitai.com/models/3047057?modelVersionId=3464228)
- `10-inches-pleaser-heels-moss` — `101ph`, `[Infinity997,Beyond008,Beyond009,Beyond010LG,Beyond010LG],`, `10 inch platform heels, [color,clear] massive extreme platform soles, `, `[color,clear] [criss-cross,slender thin woven interlaced multi-strap,p` · strength not stated · 166 dl · My Character LoRA Gallery (1000+ Downloadable Character LoRAs & 500+ Runnable Online) Moss Image: St · [source](https://civitai.com/models/1777689?modelVersionId=3451681)

- Suggest ingest: [Tifa Lockhart (Final Fantasy 7) (Outfit Collection 23 Outfits)](https://civitai.com/models/1242549) (illustrious, 25,090 dl) — `tfff7lckhrt, brown eyes, black hair, long hair, swept bangs, silver ea` · strength not stated — **downloads 25090 >= 2x best available (6777) in same family+category**
- Suggest ingest: [pantyhose](https://civitai.com/models/26760) (sdxl, 24,942 dl) — `panntyhose`, `black pantyhose`, `white pantyhose` · strength `0.5` (stated) — **downloads 24942 >= 2x best available (1359) in same family+category**
- Suggest ingest: [Erza Scarlet (All Armors & Outfits) (61 Outfits) / Illustrious](https://civitai.com/models/902174) (illustrious, 21,556 dl) — `erz_bwaitress, brown eyes, red hair, long hair, hair over one eye, fak` · strength `0.8 - 1` (stated) — **downloads 21556 >= 2x best available (6777) in same family+category**

### 22. Swimwear and beach

**Illustrious / NoobAI (Illustrious-XL based)**
- `x micro bikini_illustrious_V2.1` — `x micro bikini` · strength not stated · 4,944 dl · pony;The strength of Lora is recommended to be around 1.0. XL;The strength of Lora is recommended to · [source](https://civitai.com/models/518864?modelVersionId=2651990)
- `competitive-swimsuit-sd-xl-ill` — `competitive swimsuit` · strength not stated · 2,523 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2715085)

**SDXL**
- `condom-bikini-condoms-tied-to-bikini-il-sd-xl` — `c0ndom_bikini, tied condom, used condoms, condoms tied to bikini` · strength not stated · 135 dl · Lets your favorite character wear a condom bikini, or bikini with used condoms tied on it. Have fun! · [source](https://civitai.com/models/1584792?modelVersionId=1793388)
- `penis-under-another-s-bikini-penis-under-a-xl` — `Penis under another's clothes, bikini` · strength not stated · 82 dl · Have him stick his dick right under her bikini, the best spot! Have fun! · [source](https://civitai.com/models/2024170?modelVersionId=2290925)

**Pony (Pony Diffusion XL)**
- `competitive-swimsuit-sd-xl-ill-pony` — `competitive swimsuit` · strength not stated · 4,591 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=614384)
- `costumecross-swimsuit-request-pony` — `cross swimsuit`, `areola slip, skin indention` · strength not stated · 1,967 dl · [source](https://civitai.com/models/830254?modelVersionId=928606)

**Anima**
- `maid-bikini-anima` — `maid bikini, maid headdress, frills, wrist cuffs,bare shoulders` · strength not stated · 2,193 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/668558?modelVersionId=3055885)
- `competitive-swimsuit-sd-xl-ill-anima` — `competitive swimsuit` · strength not stated · 1,812 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2944201)

**Krea2 (detailed-krea2)**
- `micro-bikini-krea2` — `Micr0Bikini` · strength not stated · 2,315 dl · Generates images of women with micro bikinis. I recommend upscaling after generating, not all images · [source](https://civitai.com/models/2317614?modelVersionId=3136903)
- `Tan-Lines-Krea2_epoch_10` — trigger not stated · strength `0.6 – 1.2` (stated) · 2,112 dl · Bikini Tan Lines LoRA A clean, detailed skin LoRA that adds realistic bikini tan lines to female cha · [source](https://civitai.com/models/2840638?modelVersionId=3206585)

**MOSS (Moss Image / kromoss)**
- `micro-bikini-thong-pull-for-moss` — trigger not stated · strength `0.5` (stated) · 843 dl · This model generates a low cut sling style micro bikini. This model also does well with getting the  · [source](https://civitai.com/models/3022730?modelVersionId=3432428)
- `4472-swimsuit-party-xl` — `@ruanyi4472,areola slip,long sleeves,o-ring,revealing clothes,purple d` · strength not stated · 281 dl · Hello everyone! Whenever a new model is released, I just have to try training it and really put it t · [source](https://civitai.com/models/3010194?modelVersionId=3416032)

- Suggest ingest: [Slingshot swimsuit [SD1.5/Pony/Illustrious/Anima]](https://civitai.com/models/7957) (illustrious, 133,438 dl) — `slingshot swimsuit` · strength not stated — **downloads 133438 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,308 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36308 >= 2x best available (9653) in same family+category**
- Suggest ingest: [SDXL_Sexy underwear](https://civitai.com/models/124782) (sdxl, 10,105 dl) — `bikini`, `underwear`, `Lace` · strength `0.6-1.5` (stated) — **downloads 10105 >= 2x best available (1359) in same family+category**

### 23. Costumes, uniforms and cosplay (adult characters)

All characters must be adults.

**Illustrious / NoobAI (Illustrious-XL based)**
- `costumeblack-bodystocking-request-ill` — `bodystocking` · strength not stated · 2,400 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=1244147)
- `body-paint-cosplay-event-peint-clothes-cos-ill` — `((paint clothes)), ((bodypaint)), paint_cosplay_event, 1girl, breasts,` · strength not stated · 2,321 dl · Generate a scene from a cosplay event in Tokyo. According to recent regulations, it's OK as long as  · [source](https://civitai.com/models/2017293?modelVersionId=2283114)

**SDXL**
- `80s-aerobic-outfit-xl` — `a3robic`, `80s aerobic outfit` · strength not stated · 479 dl · [source](https://civitai.com/models/517542?modelVersionId=575094)
- `outfit-futa-xl` — trigger not stated · strength not stated · 185 dl · V1 · [source](https://civitai.com/models/663022?modelVersionId=741974)

**Pony (Pony Diffusion XL)**
- `costumefishnet-bodysuit-request-pony` — `fishnet bodysuit` · strength not stated · 4,406 dl · [source](https://civitai.com/models/815349?modelVersionId=911750)
- `costumeskimpy-gal-request-pony` — `front-tied shirt, micro bikini, areola slip, miniskirt, pleated skirt` · strength not stated · 2,214 dl · [source](https://civitai.com/models/815009?modelVersionId=911347)

**Anima**
- `maid-bikini-anima` — `maid bikini, maid headdress, frills, wrist cuffs,bare shoulders` · strength not stated · 2,193 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/668558?modelVersionId=3055885)
- `bondage-outfit-xl-ill-anima` — `bondage outfit, thighhighs, gloves, latex, dominatrix,skirt,o-ring` · strength not stated · 1,557 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/572670?modelVersionId=3086911)

**Krea2 (detailed-krea2)**
- `bondage-outfit-v3-krea2` — `bondage outfit, fluxbondage, 1girl, breasts, solo, nipples, twintails,` · strength `0.8` (stated) · 2,775 dl · Krea2 bondage outfit v3 （Slim harness） Lora type:Krea2 triger：bondage outfit, fluxbondage, prompt：bo · [source](https://civitai.com/models/2053543?modelVersionId=3192079)
- `krea2 thong floss outfit` — `zithong, thong floss outfit, 1girl, breasts, solo, nipples, realistic,` · strength `0.8` (stated) · 1,606 dl · Krea2 thong_floss_outfit Lora type:Krea2 triger：zithong, thong floss outfit, prompt：zithong, thong f · [source](https://civitai.com/models/2217869?modelVersionId=3190414)

**MOSS (Moss Image / kromoss)**
- `team-rocket-cosplay-pokemon-ani-il-moss-xl` — `t34mr0ck3t,`, `t34mr0ck3t,  team rocket uniform, white jacket, cropped jacket, white ` · strength not stated · 253 dl · Prepare for trouble! 🚀 Follow me on X/Twitter for exclusive content: https://x.com/Citron_Legacy 😁 P · [source](https://civitai.com/models/371976?modelVersionId=3416558)
- `maid-classic-moss` — `maid,maid apron,maid headdres` · strength not stated · 221 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/703211?modelVersionId=3456338)

- Suggest ingest: [Undressing SD1/XL/PONY/FLUX](https://civitai.com/models/505266) (sdxl, 55,860 dl) — `undressing` · strength `1.3` (stated) — **downloads 55860 >= 2x best available (1359) in same family+category**
- Suggest ingest: [Slavekini, aka Slave Leia Outfit - Clothing [Krea2, Anima, IL, Pony, S](https://civitai.com/models/7913) (illustrious, 30,714 dl) — `slave leia outfit`, `or`, `slavekini, pelvic curtain , collar, armlet , hair ornament, braid` · strength `.8-1.0` (stated) — **downloads 30714 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Undressing LoRA [SD1.5 & SDXL1.0]](https://civitai.com/models/242034) (sdxl, 26,132 dl) — `undressing` · strength not stated — **downloads 26132 >= 2x best available (1359) in same family+category**

### 24. Accessories and gear (collars, chastity, piercings, condoms, plugs)

**Illustrious / NoobAI (Illustrious-XL based)**
- `harness-sd-xl-ill` — `harness, bdsm, o-ring`, `bound` · strength not stated · 6,777 dl · The strength of Lora is recommended to be around 0.8 · [source](https://civitai.com/models/583686?modelVersionId=1131895)
- `chastity-cage-metal-flat-v1-ill` — `flat chastity cage`, `precum drip`, `testicles`, `ejaculation, ejaculating while penetrated, cum` · strength not stated · 5,868 dl · flat chastity cage lora best used with inpainting check my specialized loras! pov lora https://civit · [source](https://civitai.com/models/1689514?modelVersionId=2429438)

**SDXL**
- `condom-bikini-condoms-tied-to-bikini-il-sd-xl` — `c0ndom_bikini, tied condom, used condoms, condoms tied to bikini` · strength not stated · 135 dl · Lets your favorite character wear a condom bikini, or bikini with used condoms tied on it. Have fun! · [source](https://civitai.com/models/1584792?modelVersionId=1793388)
- `condoms-in-stomach-il-sd-xl` — `c0ndoms_in_st0mach, condoms in stomach, x-ray` · strength not stated · 86 dl · Leaves condoms in her stomach, very few pics of this (and I love making rare concepts), have fun! · [source](https://civitai.com/models/1445083?modelVersionId=1633717)

**Pony (Pony Diffusion XL)**
- `genital-piercing-xl-pony` — `pussy piercing, clitoris piercing`, `pussy`, `spread puusy` · strength not stated · 3,287 dl · [source](https://civitai.com/models/459565?modelVersionId=511474)
- `clitoris-jewelry-xl-ill-pony` — `clitoris jewelry` · strength not stated · 2,800 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/576831?modelVersionId=643187)

**Anima**
- `[Anima][Concept]flat_chastity_cage-10` — `flat chastity cage`, `pov, pov chastity`, `chastity strap`, `chastity ring` · strength `1.0` (stated) · 2,533 dl · Anima Version Update: Flat Chastity Cage for Anima model. Not perfect but works well with other lora · [source](https://civitai.com/models/1037793?modelVersionId=3020542)
- `harness-sd-xl-anima` — `harness,o-ring` · strength not stated · 2,154 dl · The strength of Lora is recommended to be around 0.8 · [source](https://civitai.com/models/583686?modelVersionId=3064972)

**Krea2 (detailed-krea2)**
- `used-condom-krea2` — `usedc0nd0m.` · strength not stated · 4,476 dl · About this version The used condom Lora for Krea2 is here. The preview image includes a workflow, wh · [source](https://civitai.com/models/2780495?modelVersionId=3131462)
- `nipple-piercing-zit-il-flux-krea2` — `pierced nipples,` · strength `0.7` (stated) · 3,716 dl · Just an attempt to create a different lora, if it turns out good, I'll create more. I accept suggest · [source](https://civitai.com/models/1096396?modelVersionId=3182058)

**MOSS (Moss Image / kromoss)**
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)
- `barbell-nipple-piercings-ultra-hd-moss` — `nipple piercings` · strength not stated · 532 dl · Barbell Nipple Piercings Trained with at 1024x1024 with hand cropped patches from 20MP images High d · [source](https://civitai.com/models/2357066?modelVersionId=3451406)

- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,308 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36308 >= 2x best available (9653) in same family+category**
- Suggest ingest: [乳首責め/nipple pull](https://civitai.com/models/627113) (illustrious, 33,549 dl) — `nipple pull,holding,1girl,nipples,1boy,nipple piercing,chain,` · strength not stated — **downloads 33549 >= 2x best available (10931) in same family+category**
- Suggest ingest: [Milking Machines](https://civitai.com/models/419704) (pony, 16,179 dl) — `milking machine,suction device,milk machine,harness,object insertion,s` · strength not stated — **downloads 16179 >= 2x best available (7814) in same family+category**

### 25. POV and camera angle / framing

Camera/framing LoRAs go early in the stack; keep strength moderate.

**Illustrious / NoobAI (Illustrious-XL based)**
- `CuckNTR POV Pony LoRa - 3.0 Illustrious - NTR_POV` — trigger not stated · strength not stated · 9,704 dl · Important tags (tag: cuck pov,netorare,femdom) Make person hold a cellphone with porn on it (tags: p · [source](https://civitai.com/models/339447?modelVersionId=1255291)
- `toilet-spy-multiple-views-2koma-concept-ve-ill` — `knees together feet apart`, `tile wall`, `toilet use`, `toilet seat` · strength not stated · 5,016 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/1941768?modelVersionId=2197702)

**SDXL**
- `female-masturbation-from-above-xl` — trigger not stated · strength `0.6` (stated) · 895 dl · Try a strength between 0.6 and 1.0. I recommend negative promts like: "maleformed hands, malformed f · [source](https://civitai.com/models/2718384?modelVersionId=3054666)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)

**Pony (Pony Diffusion XL)**
- `tg-rear-shot-trans-girls-from-behind-pony` — `TGRearShot` · strength not stated · 265 dl · This is mostly to generate a better rear angle of trans women. I've had decent luck with at 0.6 to 1 · [source](https://civitai.com/models/2015785?modelVersionId=2281365)
- `wide-shot-long-shot-zoom-out-pony` — `Wide shot` · strength not stated · 131 dl · Don't like how all your images are so close to the character? The wide shot view is zoomed out so yo · [source](https://civitai.com/models/2623769?modelVersionId=2946007)

**Anima**
- `fpov-anima` — `female pov looking down her breasts` · strength not stated · 6,246 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/427349?modelVersionId=2948925)
- `fpcview_v0.0.0-step00000600` — `fpcview`, `from above, wide shot, dutch angle`, `head out of frame, straight-on`, `The character stands near the edge of the frame while a large empty sp` · strength not stated · 2,133 dl · v0.0.0 (Initial Release) The purpose of this LoRA is to break the AI's deeply hardcoded composition  · [source](https://civitai.com/models/2782139?modelVersionId=3133505)

**Krea2 (detailed-krea2)**
- `_Krea2__Taking_selfie_from_3rd-person_view_epoch_6` — `th1rd-p3rson-self1e third-person view of`, `viewed from a three-quarters angle`, `she is sitting and reclining back spreading her thighs {and feet up cu`, `she is standing and reaching carefully between her leg holding a smart` · strength not stated · 1,779 dl · Give it a go. It generates images of [women] taking selfies. Not a selfie image as such, as it's fro · [source](https://civitai.com/models/2818090?modelVersionId=3178646)
- `fpov-female-point-of-view-for-krea2` — `From a top-down view`, `From a first-person perspective` · strength `1` (stated) · 1,728 dl · V1 (alone): This is the main version. This LoRa is the result of 2 years of testing on Flux, but I w · [source](https://civitai.com/models/2918304?modelVersionId=3301630)

**MOSS (Moss Image / kromoss)**
- `home-cctv-hd-clear-home-dorm-security-came-moss` — trigger not stated · strength not stated · 1,552 dl · Description Clear colour home-security stills: a camera mounted high in a room corner looks down acr · [source](https://civitai.com/models/3015044?modelVersionId=3422347)
- `bodycam-view-vlogger-chest-cam-pov-moss` — trigger not stated · strength not stated · 666 dl · A chest-mounted action camera POV: a low, chest-height wide-angle frame facing the person who is tal · [source](https://civitai.com/models/3021452?modelVersionId=3430758)

- Suggest ingest: [Upright straddle sex front view](https://civitai.com/models/82128) (sdxl, 59,134 dl) — `1boy, sex, hetero, upright straddle, straddling, girl on top` · strength `1.0` (stated) — **downloads 59134 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Cowgirl Position Sex Non-POV / Third Person](https://civitai.com/models/145887) (sdxl, 47,903 dl) — `1boy, sex, cowgirl position, girl on top, straddling` · strength not stated — **downloads 47903 >= 2x best available (7022) in same family+category**

### 26. Poses and body positions

**Illustrious / NoobAI (Illustrious-XL based)**
- `pose_femdom_pegging_nipple_tweak - v1.0 - pose_pegging_nipple_tweak` — `pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1b` · strength not stated · 3,470 dl · pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1boy, hetero, ejaculation, ejacu · [source](https://civitai.com/models/1295786?modelVersionId=1462424)
- `jack-o-pose-sex-solo-ill` — `jko, jack-o' challenge,`, `top-down bottom-up,`, `rom behind,`, `1girl, solo,` · strength not stated · 3,062 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1373437?modelVersionId=1551797)

**SDXL**
- `gaping-assholes-all-fours-sdxl1-0-concept-xl` — `GapingAssholesAllFourQuiron pose`, `all fours`, `from behind`, `spread ass` · strength not stated · 7,022 dl · 👑 Gaping Assholes All Fours LORA 👑 SDXL1.0 v5.1p 🔧Model base: SDXL1.0 📝🌟 Trigger: (GapingAssholesAll · [source](https://civitai.com/models/130866?modelVersionId=143716)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)

**Pony (Pony Diffusion XL)**
- `assuplyingdown-pony` — `auok`, `assuponknees` · strength not stated · 2,790 dl · This is my first LORA, trained off only 11 images, so it's probably rubbish, but it seems to do what · [source](https://civitai.com/models/300336?modelVersionId=441302)
- `jack-o-pose-sex-solo-pony` — `jko, jack-o' challenge,`, `top-down bottom-up,`, `rom behind,`, `1girl, solo,` · strength not stated · 627 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1373437?modelVersionId=1619238)

**Anima**
- `folded-pose-anima` — `folded`, `legs up`, `knees together`, `legs together` · strength not stated · 3,918 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/623820?modelVersionId=2923111)
- `butt-to-butt-copulation-human-pose-anima` — `butt to butt copulation`, `all fours` · strength not stated · 1,816 dl · 神秘小姿势 trigger word: butt to butt copulation better with: all fours, testicles, x-ray, ass ripple opt · [source](https://civitai.com/models/2727765?modelVersionId=3066227)

**Krea2 (detailed-krea2)**
- `krea2 sex 淫模 - carry - krea2 standing and carry` — `zitstanding, stand_and_carry, 1girl, 1boy, hetero, penis, sex, nude, a` · strength `0.6–0.7` (stated) · 5,912 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170121)
- `krea2 sex 淫模 - Leg - standing_on_one_leg_sex_epoch_10` — trigger not stated · strength `0.6–0.7` (stated) · 3,697 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3249142)

**MOSS (Moss Image / kromoss)**
- `ek-s-aio-pose-nsfw-moss` — `many!! see description!` · strength not stated · 1,672 dl · This lora is for MOSS image This is a ALL IN ONE Pose set I worked on for a while Its purpose Is to  · [source](https://civitai.com/models/3020392?modelVersionId=3429378)
- `blowbowpose-moss` — `blowbowpose` · strength not stated · 743 dl · The keyword for this model is "blowbowpose" To prompt this model you need to know a few bonus things · [source](https://civitai.com/models/2987554?modelVersionId=3428844)

- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Reverse upright straddle / sitting on lap](https://civitai.com/models/114292) (pony, 41,344 dl) — `reverse upright straddle`, `legs together`, `spread legs` · strength not stated — **downloads 41344 >= 2x best available (8495) in same family+category**

### 27. Oral (blowjob, deepthroat, cunnilingus)

**Illustrious / NoobAI (Illustrious-XL based)**
- `fellatio-and-masturbation-ill` — `fellatio and masturbation, fellatio, female masturbation, 1boy, penis` · strength not stated · 11,460 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=1134882)
- `jav-hard-irrumatio-deepthroat-generator-ill` — `JAV_MISS572,  1girl, hetero, solo focus, tears, crying, saliva, snot, `, `bukkake, facial, excessive cum ,  close-up mouth , vomiting,` · strength `0.85 - 1` (stated) · 8,090 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/728512?modelVersionId=2115883)

**SDXL**
- `blowjob-top-of-head-pov-sdxl1-0-xl` — `blowjobtopofheadpovQuiron` · strength not stated · 6,789 dl · 👑 Blowjob Top of Head POV - Lora 👑 SDXL1.0 ⚙️🔧Model base: SDXL1.0 ______________ 📝🌟 Trigger: blowjob · [source](https://civitai.com/models/125648?modelVersionId=1312598)
- `blowjob-top-of-head-pov-sdxl1-0-xl-2` — `BlowjobTopofHeadPOVQuiron pose`, `a woman with a penis in her mouth`, `oral` · strength not stated · 1,075 dl · 👑 Blowjob Top of Head POV Lora SDXL1.0👑  v3 🔧Model base: SDXL1.0 _____________ 📝🌟 Trigger: BlowjobTo · [source](https://civitai.com/models/125648?modelVersionId=137273)

**Pony (Pony Diffusion XL)**
- `fellatio-and-masturbation-pony` — `fellatio and masturbation`, `fellatio`, `female masturbation`, `fingering` · strength not stated · 11,628 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=616692)
- `jav-hard-irrumatio-deepthroat-generator-pony` — `JAV_MISS572,  1girl, hetero, solo focus, tears, crying, saliva, snot, ` · strength `0.85 - 1` (stated) · 11,159 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/728512?modelVersionId=814646)

**Anima**
- `fellatio-and-masturbation-anima` — `fellatio and masturbation, 1girl, 1boy, penis,pussy` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=3000440)
- `deeper-penetration-deepthroat-and-somethin-anima` — `deep penetration`, `deepthroat`, `object insertion` · strength not stated · 2,412 dl · I trained this Lokr to solve the issue of not penetrate deep enough. However, I was too ambitious an · [source](https://civitai.com/models/2708641?modelVersionId=3042522)

**Krea2 (detailed-krea2)**
- `how-much-cum-yes-bukkake-gokkun-cum-overfl-krea2` — `cum,`, `semen,`, `sperm,`, `gokkun` · strength `0.8-0.9` (stated) · 8,807 dl · Join my Discord: https://discord.gg/tMbPUdkP27 Excellent cum texture, put that shit on everything! I · [source](https://civitai.com/models/2512358?modelVersionId=3221218)
- `krea2 sex 淫模 - BJ - kreablowjob` — `kreablowjob, 1girl, realistic, hetero, breasts, 1boy, penis, nipples, ` · strength `0.6–0.7` (stated) · 4,514 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3158893)

**MOSS (Moss Image / kromoss)**
- `cum-xl` — trigger not stated · strength not stated · 2,247 dl · Commonly used vocabulary in captioning: - Fluid states (use one or two): glossy · thick white · visc · [source](https://civitai.com/models/3012757?modelVersionId=3419412)
- `pov-blowjob-moss` — `Highly explicit, high-angle, close-up photo of a nude woman. She is pe` · strength not stated · 1,272 dl · Basic Prompt: Highly explicit, high-angle, close-up photo of a nude woman. She is performing oral se · [source](https://civitai.com/models/2514609?modelVersionId=3434597)

- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Pov Blowjob + Titjob + Handjob [updated]](https://civitai.com/models/446163) (illustrious, 40,457 dl) — `pov, 1girl, 1boy,`, `fellatio,`, `paizuri,`, `handjob,` · strength not stated — **downloads 40457 >= 2x best available (9704) in same family+category**
- Suggest ingest: [deep_penetration concept slider (for pony XL)](https://civitai.com/models/287556) (pony, 34,682 dl) — `vaginal`, `anal`, `deepthroat` · strength not stated — **downloads 34682 >= 2x best available (14402) in same family+category**

### 28. Sex positions (cowgirl, missionary, doggy, etc.)

Use ONE position LoRA per image.

**Illustrious / NoobAI (Illustrious-XL based)**
- `fucked-silly-xl` — `extreme sex` · strength `1` (stated) · 38,542 dl · 💖 Support & Share the Magic!  Love these tools? Like, add to collection, and tag this resource in yo · [source](https://civitai.com/models/1273929?modelVersionId=1613410)
- `xxx-gangbang-group-sex-generator-evil-ange-ill` — `1girl, solo forcas, nude, 4+boys, Gangbang, Group Sex, Multiple Boys, ` · strength `0.9-0.6` (stated) · 14,416 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=2110029)

**SDXL**
- `sex-machine-sdxl` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 1,976 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=930213)
- `trash-can-sex-garbage-can-sex-stuck-in-gar-xl` — `tr4sh-can-s3x, trash can, in container, stuck, lower body, ass, anus, ` · strength not stated · 344 dl · Your favorite character is stuck in a trash can. What's a guy to do 🤣. Have fun! · [source](https://civitai.com/models/1535973?modelVersionId=1737933)

**Pony (Pony Diffusion XL)**
- `xxx-gangbang-group-sex-generator-evil-ange-pony` — `1girl, solo forcas, nude, Simple background,  depth of field, indoors,` · strength `0.9-0.6` (stated) · 14,402 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=732074)
- `hentai-gangbang-group-sex-after-sex-xl-spr-pony` — `group sex, after sex, hetero,6+boys,6+penises,veiny penis, 1girl, solo` · strength not stated · 8,000 dl · [source](https://civitai.com/models/581936?modelVersionId=649130)

**Anima**
- `sex-machine-xl-ill-anima` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 4,153 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=2952118)
- `human-onahole-fantasy-sex-concept-collecti-anima` — `HBGV2, giant, holding person, size difference,` · strength not stated · 3,219 dl · I BARELY HAD ANY DICKS INSIDE ME Real description:  Held By Giant - it gets the same effect, seeming · [source](https://civitai.com/models/1319951?modelVersionId=2987156)

**Krea2 (detailed-krea2)**
- `K_gangbanghelper` — `prompt anything with:`, `gangbang, double penetration, gets double penetrated, anal sex, vagina`, `She is on her back.`, `she is kneeling.` · strength `0.7-1.0` (stated) · 6,569 dl · Krea2 This is a All holes filled-lora. She will have the tendency to always have a penis in her mout · [source](https://civitai.com/models/2240240?modelVersionId=3159235)
- `krea2 sex 淫模 - carry - krea2 standing and carry` — `zitstanding, stand_and_carry, 1girl, 1boy, hetero, penis, sex, nude, a` · strength `0.6–0.7` (stated) · 5,912 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170121)

**MOSS (Moss Image / kromoss)**
- `pantyhose-sex-moss` — trigger not stated · strength not stated · 329 dl · Guidance 2.5 Steps 25 Sampler er_sde Seed 2 · [source](https://civitai.com/models/3022457?modelVersionId=3432090)
- `ek-s-mecha-suit-sex-machine-moss` — `sex machine mecha suit` · strength not stated · 279 dl · edit: added extracted loras. r16 seems to be quite fine. and it is just 75 mega not over one giga bi · [source](https://civitai.com/models/3041593?modelVersionId=3457246)

- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**
- Suggest ingest: [Mating press](https://civitai.com/models/90532) (pony, 61,812 dl) — `mating press` · strength not stated — **downloads 61812 >= 2x best available (8495) in same family+category**
- Suggest ingest: [Upright straddle sex front view](https://civitai.com/models/82128) (sdxl, 59,134 dl) — `1boy, sex, hetero, upright straddle, straddling, girl on top` · strength `1.0` (stated) — **downloads 59134 >= 2x best available (7022) in same family+category**

### 29. Cum, fluids and aftermath

**Illustrious / NoobAI (Illustrious-XL based)**
- `facial-cumshot-225-xl` — `cumshot, facial, masturbation, ejaculation,`, `pov, pov hands` · strength not stated · 5,489 dl · 🔥 Facial cumshot LoRa for Illustrious 🔥 Hey everyone! This model focuses on creating images with a g · [source](https://civitai.com/models/1164568?modelVersionId=1310077)
- `doggystyle-view-from-behind-creampie-ill` — `facefocus_doggy,sex from behind,cumshot, cum drip, cum in pussy,lookin`, `arms behind back, restrained,` · strength `0.8` (stated) · 5,246 dl · lora for a doggystyle sex from behind view. A girl is force to look at her pussy and ejaculation. st · [source](https://civitai.com/models/1662410?modelVersionId=1881604)
- `MCB Lubed ill v2-15` **[HF repo only - needs adding to Graydient]** — trigger not stated · strength not stated · no source link

**SDXL**
- `pornmaster-projectile-cumejaculationcumsho-xl` — `projectile cum, penis,` · strength not stated · 4,139 dl · SDXL-V1培訓字幕excel檔案下載。 SDXL-V1 training subtitle excel file download. -- 培训图片包含男同性恋，要生成女性图片正面提示词放入女性聚 · [source](https://civitai.com/models/950655?modelVersionId=1064347)
- `cumshot-xl` — trigger not stated · strength not stated · 455 dl · [source](https://civitai.com/models/1538069?modelVersionId=1740302)

**Pony (Pony Diffusion XL)**
- `hentai-falling-into-the-toilet-girl-3-shot-pony` — `((3girls)), multiple views, multiple frame, (covered nipples),(covered` · strength not stated · 4,294 dl · This's LORA who turns cheeky girls into cum toilets.. Due to its structure, it is effective to gener · [source](https://civitai.com/models/677434?modelVersionId=758325)
- `cumshots-meme-for-ponyxl-pony` — `cumshots meme` · strength not stated · 2,221 dl · Initial Version · [source](https://civitai.com/models/491746?modelVersionId=546832)
- `MCB Lubed pony v1-14` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `MCB Lubed pony v2-10` **[HF repo only - needs adding to Graydient]** — trigger not stated · strength not stated · no source link

**Anima**
- `female-ejaculation-krea2-2` — `female ejaculation, pussy` · strength not stated · 3,114 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/558452?modelVersionId=2980272)
- `huge-facial-bukkake-ponyxl-xl-anima` — `huge facial bukkake ponyxl xl anima` · strength not stated · 2,247 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=3171504)

**Krea2 (detailed-krea2)**
- `realcumk4` — `cum on face`, `cum covered face`, `cum in mouth` · strength not stated · 16,673 dl · I'm back. realcum krea2 alpha This is the first version for testing the concept with the krea2 model · [source](https://civitai.com/models/326320?modelVersionId=3208030)
- `oiled-skin-krea2` — trigger not stated · strength `1.0` (stated) · 8,842 dl · Krea 2 Turbo Info: Use the trigger phrase "OiledSkin" for best results. Keep strength at 1.0 for max · [source](https://civitai.com/models/87685?modelVersionId=3096878)
- `MCB Lubed krea2 v1-08` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**MOSS (Moss Image / kromoss)**
- `cum-xl` — trigger not stated · strength not stated · 2,247 dl · Commonly used vocabulary in captioning: - Fluid states (use one or two): glossy · thick white · visc · [source](https://civitai.com/models/3012757?modelVersionId=3419412)
- `cum-on-face-moss` — `semen on her face`, `semen dripping from her chin` · strength `0.8-0.6` (stated) · 1,212 dl · Probably the only cumshot lora you will ever need. 💦💦 Weight: 0.8-0.6 Trigger words: semen on her fa · [source](https://civitai.com/models/146522?modelVersionId=3434966)

- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Bukkake / excessive cum](https://civitai.com/models/109745) (pony, 105,734 dl) — `excessive cum` · strength not stated — **downloads 105734 >= 2x best available (14402) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**

### 30. Solo, masturbation and fingering

**Illustrious / NoobAI (Illustrious-XL based)**
- `fellatio-and-masturbation-ill` — `fellatio and masturbation, fellatio, female masturbation, 1boy, penis` · strength not stated · 11,460 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=1134882)
- `fingering-ill` — `fingering` · strength not stated · 6,896 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/551963?modelVersionId=2101849)

**SDXL**
- `femdom handjob SDXL - SDXL v1.0 - femdom handjob SDXL_epoch_19` — trigger not stated · strength `0.6` (stated) · 403 dl · Try a strength between 0.6 and 1.0. · [source](https://civitai.com/models/2570715?modelVersionId=2888449)
- `step-sis-backside-anal-fingering-simulator-xl` — `finger_ass` · strength not stated · 260 dl · [source](https://civitai.com/models/3009204?modelVersionId=3414763)

**Pony (Pony Diffusion XL)**
- `fellatio-and-masturbation-pony` — `fellatio and masturbation`, `fellatio`, `female masturbation`, `fingering` · strength not stated · 11,628 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=616692)
- `fingering-pony` — `fingering` · strength not stated · 6,541 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/551963?modelVersionId=614217)

**Anima**
- `masturbation-with-dildo-object-insertion-anima` — `female masturbation, object insertion, dildo grab`, `vaginal object insertion, vaginal`, `anal object insertion, anal` · strength `0.8-1.0` (stated) · 4,019 dl · A girl and her trusty friend. If you have any request or would like a commission, feel free to comme · [source](https://civitai.com/models/218726?modelVersionId=3057069)
- `fellatio-and-masturbation-anima` — `fellatio and masturbation, 1girl, 1boy, penis,pussy` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=3000440)

**Krea2 (detailed-krea2)**
- `fingering-krea2` — `fingering-krea2` · strength `0.6–0.85` (stated) · 6,754 dl · V1:  krea2_fingering_v0.1 — Krea 2 concept LoRA that improves fingering (vaginal/anal). No trigger w · [source](https://civitai.com/models/2813245?modelVersionId=3172724)
- `krea2 sex 淫模 - mast - krea2 masturbation` — `zitmast, female masturbation, 1girl, solo, realistic, spread legs, fem` · strength `0.6–0.7` (stated) · 4,792 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170098)

**MOSS (Moss Image / kromoss)**
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)
- `base-pov-fingering-moss` — `p0v-f1ng3r1ng    pov view of a female viewer reaching hand between leg` · strength not stated · 323 dl · try: p0v-f1ng3r1ng pov view of a female viewer reaching hand between legs and fingering pussy slick  · [source](https://civitai.com/models/3050006?modelVersionId=3468343)

- Suggest ingest: [Multiple Boys - Concept](https://civitai.com/models/1431750) (illustrious, 23,068 dl) — `<lora:multiple-boys-v9-illustriousxl-lora-nochekaiser:1>, multiple boy` · strength `1.0` (stated) — **downloads 23068 >= 2x best available (9653) in same family+category**
- Suggest ingest: [SDXL dildo](https://civitai.com/models/138380) (sdxl, 19,591 dl) — `dildo`, `sex toy`, `vaginal object insertion`, `anal object insertion` · strength `0.2` (stated) — **downloads 19591 >= 2x best available (2431) in same family+category**
- Suggest ingest: [SexToy - Dildo](https://civitai.com/models/263021) (sdxl, 9,436 dl) — `See tag discription` · strength not stated — **downloads 9436 >= 2x best available (2431) in same family+category**

### 31. BDSM, bondage and restraints

Consensual adult scenes only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `jav-hard-core-bdsm-generator-m-drag-m-ill` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 11,673 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=2106832)
- `jav-hard-bdsm-generator-bondage-wall-il-xl-ill` — `1girl, legs up, m legs, licking, slave, spread legs, wide spread legs,`, `(oral), ((cunnilingus)), perfect hands, spread_pussy, male profile, to`, `Hands holding dildo, hands holding vibrator, Foreign object vaginal in`, `(pov), (sex),  large insertion, large penis, thick penis,` · strength not stated · 9,242 dl · This LORA was created to see if it could learn JAV and produce hentai anime. Width:832 Height:1216 i · [source](https://civitai.com/models/903161?modelVersionId=2117424)

**SDXL**
- `bondage-bdsm-xl` — `rope`, `black tape gag`, `bondage` · strength not stated · 21,468 dl · Training lora need more buzz, give me support! Please leave a review if you like this lora！ ver. “花と · [source](https://civitai.com/models/136849?modelVersionId=150991)
- `femdom handjob SDXL - SDXL v1.0 - femdom handjob SDXL_epoch_19` — trigger not stated · strength `0.6` (stated) · 403 dl · Try a strength between 0.6 and 1.0. · [source](https://civitai.com/models/2570715?modelVersionId=2888449)

**Pony (Pony Diffusion XL)**
- `jav-hard-core-bdsm-generator-m-drag-m-pony` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 12,530 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=721539)
- `jav-hard-bdsm-generator-bondage-wall-il-xl-pony` — `1girl, legs up, m legs, licking, slave, spread legs, wide spread legs,`, `(oral), ((cunnilingus)), perfect hands, spread_pussy, male profile, to`, `Hands holding dildo, hands holding vibrator, Foreign object vaginal in`, `(pov), (sex),  large insertion, large penis, thick penis,` · strength not stated · 9,515 dl · This LORA was created to see if it could learn JAV and produce hentai anime. Width:832 Height:1216 i · [source](https://civitai.com/models/903161?modelVersionId=1015638)

**Anima**
- `jav-hard-core-bdsm-generator-m-drag-m-anima` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 2,743 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=3229257)
- `shibari-sd-xl-ill-anima` — `shibari` · strength not stated · 2,613 dl · The strength of Lora is recommended to be around 0.4. · [source](https://civitai.com/models/591433?modelVersionId=2944205)

**Krea2 (detailed-krea2)**
- `arms-tied-around-legs-doggystyle-bdsm-bond-krea2` — `bd5m, top-down bottom up, tied up, arms tied to legs, anal sex, anal p`, `Image is shot from side, side view,` · strength `0.7-1.0` (stated) · 3,628 dl · Based on a few training pics, works best with horizontal layouts. Krea 2 Strength: 0.7-1.0 Have fun! · [source](https://civitai.com/models/2358990?modelVersionId=3220184)
- `bondage-outfit-v3-krea2` — `bondage outfit, fluxbondage, 1girl, breasts, solo, nipples, twintails,` · strength `0.8` (stated) · 2,775 dl · Krea2 bondage outfit v3 （Slim harness） Lora type:Krea2 triger：bondage outfit, fluxbondage, prompt：bo · [source](https://civitai.com/models/2053543?modelVersionId=3192079)

**MOSS (Moss Image / kromoss)**
- `bondage-gags-megapack-aio-moss` — trigger not stated · strength not stated · 1,878 dl · See example prompts in images. Trained on 10,750 steps 430 images. All images posted with SFT model, · [source](https://civitai.com/models/3009470?modelVersionId=3415104)
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)

- Suggest ingest: [Bondage Suspension](https://civitai.com/models/8762) (illustrious, 92,975 dl) — `suspension` · strength not stated — **downloads 92975 >= 2x best available (38542) in same family+category**
- Suggest ingest: [Erza Scarlet (All Armors & Outfits) (61 Outfits) / Illustrious](https://civitai.com/models/902174) (illustrious, 21,556 dl) — `erz_bwaitress, brown eyes, red hair, long hair, hair over one eye, fak` · strength `0.8 - 1` (stated) — **downloads 21556 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Slave Restraints](https://civitai.com/models/151223) (sdxl, 17,090 dl) — `slave_restraints outfit` · strength not stated — **downloads 17090 >= 2x best available (1359) in same family+category**

### 32. Multiple partners, gangbang, threesome

**Illustrious / NoobAI (Illustrious-XL based)**
- `xxx-gangbang-group-sex-generator-evil-ange-ill` — `1girl, solo forcas, nude, 4+boys, Gangbang, Group Sex, Multiple Boys, ` · strength `0.9-0.6` (stated) · 14,416 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=2110029)
- `spitroast-foot-xl` — `prone bone`, `on stomach`, `defeat`, `humiliation` · strength not stated · 6,956 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/1336016?modelVersionId=1508669)
- `suze-group_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `straining-expression-il-sd-flux-xl` — `str4in, clenched teeth, sweating, blushing, drool, eyes rolling up` · strength not stated · 240 dl · [source](https://civitai.com/models/1246430?modelVersionId=1405076)
- `double-dildo-deepthroat-il-z-sd-xl` — `Double_dildo_deepthroat` · strength not stated · 129 dl · Have two characters deepthroat a double dildo together. Have fun! · [source](https://civitai.com/models/2356803?modelVersionId=2650703)

**Pony (Pony Diffusion XL)**
- `xxx-gangbang-group-sex-generator-evil-ange-pony` — `1girl, solo forcas, nude, Simple background,  depth of field, indoors,` · strength `0.9-0.6` (stated) · 14,402 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=732074)
- `hentai-gangbang-group-sex-after-sex-xl-spr-pony` — `group sex, after sex, hetero,6+boys,6+penises,veiny penis, 1girl, solo` · strength not stated · 8,000 dl · [source](https://civitai.com/models/581936?modelVersionId=649130)

**Anima**
- `group-sex-with-a-large-number-of-boys-anima` — `groupsex_ani,` · strength `0.8` (stated) · 2,457 dl · lora for a group sex with a large number of boys. strength ~0.8. It is better to use landscape form  · [source](https://civitai.com/models/1932245?modelVersionId=3312976)
- `multiple penetration_anima_V1.0` — `multiple boys, multiple penetration, group sex, gangbang, 1girl, anal,` · strength `1.0` (stated) · 1,946 dl · A strength of around 1.0 for Lola is recommended. · [source](https://civitai.com/models/1370965?modelVersionId=2958545)

**Krea2 (detailed-krea2)**
- `K_gangbanghelper` — `prompt anything with:`, `gangbang, double penetration, gets double penetrated, anal sex, vagina`, `She is on her back.`, `she is kneeling.` · strength `0.7-1.0` (stated) · 6,569 dl · Krea2 This is a All holes filled-lora. She will have the tendency to always have a penis in her mout · [source](https://civitai.com/models/2240240?modelVersionId=3159235)
- `k_doggystyledp` — `d0ggy,, double penetration, doggystyle, vaginal sex, anal sex, double `, `the girl has sex in doggystyle position and get double penetrated by t` · strength `0.7-1.0` (stated) · 3,896 dl · This is double Penetration in Doggystyle, many think the cowgirl DP is Doggy-version. But no.. Krea  · [source](https://civitai.com/models/2213833?modelVersionId=3156267)
- `mcbbedridden-krea2-000010.TA_trained` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**MOSS (Moss Image / kromoss)**
- `trio-for-threesomes-moss` — trigger not stated · strength not stated · 305 dl · Trio is a Krea 2 LoRA trained on 153 captioned images of threesomes.  Start your prompt with one of  · [source](https://civitai.com/models/3040250?modelVersionId=3475732)

- Suggest ingest: [Multiple insertion / penetration](https://civitai.com/models/89125) (pony, 36,633 dl) — `multiple penetrations`, `multiple insertions`, `anal object insertion`, `vaginal object insertion` · strength not stated — **downloads 36633 >= 2x best available (14402) in same family+category**
- Suggest ingest: [Fondled](https://civitai.com/models/705447) (illustrious, 30,962 dl) — `1girl surrounded by males, girl sandwiched by boys, group, multiple bo`, `groping,`, `breast grab,`, `fingering,` · strength `0.5-0.8` (stated) — **downloads 30962 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Mtu Virus](https://civitai.com/models/57573) (illustrious, 29,967 dl) — `mtu virus`, `multiple views` · strength not stated — **downloads 29967 >= 2x best available (9653) in same family+category**

### 33. Backgrounds, rooms and environments

**Illustrious / NoobAI (Illustrious-XL based)**
- `backgroundpurple-nightclub-ill` — `nightclub` · strength not stated · 3,749 dl · The 'nightclub' tag works in regular Illustrious, but I wanted something slightly more defined and p · [source](https://civitai.com/models/1232013?modelVersionId=1388252)
- `jav-1girl-1boy-hetero-bathroom-pov-sex-gen-ill` — `1girl, nude, solo focus, looking at viewer, wet body,  1boy, pov sex, ` · strength not stated · 3,470 dl · This LoRa has learned JAV of Japanese style bathroom POV SEX. ❤In Japan, if you rent a private bathr · [source](https://civitai.com/models/2089710?modelVersionId=2364345)

**SDXL**
- `atomicpunk-interior-buildings-ad-xl` — `AtoPunInt`, `interior` · strength not stated · 47 dl · [source](https://civitai.com/models/2949992?modelVersionId=3340943)
- `miami-beach-hotel-interior-background-ad-xl` — `MiaBeaHotInt`, `interior` · strength not stated · 35 dl · [source](https://civitai.com/models/2819289?modelVersionId=3180166)

**Pony (Pony Diffusion XL)**
- `milf-city-sexy-milfs-mature-moms-and-couga-pony` — `MilfCity` · strength not stated · 629 dl · I wanted a good MILF lora that could do both elegant and trashy older women. Have fun. Be responsibl · [source](https://civitai.com/models/1983105?modelVersionId=2244787)
- `miami-beach-hotel-bedroom-background-ad-pony` — `MiaBeaHotBed`, `hotel bedroom`, `interior` · strength not stated · 77 dl · [source](https://civitai.com/models/2819331?modelVersionId=3180223)

**Anima**
- `japanese-school-hallway-background-ad-anima` — `JapHal` · strength `0.8 to 1.25` (stated) · 328 dl · This is an Anima lora for Japanese School Hallway backgrounds. The samples largely came from anime l · [source](https://civitai.com/models/2976615?modelVersionId=3373714)
- `meeting-room-anima` — `m33t1ng`, `indoors, long table, window, chairs, ceiling light, cityscape` · strength not stated · 305 dl · Creates a meeting room / board room background Trigger: m33t1ng Additional: indoors, long table, win · [source](https://civitai.com/models/2956232?modelVersionId=3348667)

**Krea2 (detailed-krea2)**
- `Nightmare_Grunge_Krea_2_Version_epoch_9` — trigger not stated · strength `0.5 to 1` (stated) · 1,769 dl · Many models are very "clean" and "bright"- grunge, dirt, darkness and atmospheric horror details are · [source](https://civitai.com/models/2804228?modelVersionId=3161763)
- `cuckold-scene-concept-krea2` — `cuckold session` · strength not stated · 1,295 dl · Cuckold / hotwife concept LoRA for photorealistic multi-person scenes. Trained to reproduce cuckold  · [source](https://civitai.com/models/2893135?modelVersionId=3271126)

**MOSS (Moss Image / kromoss)**
- `realistic-night-outdoor-photo-real-streetl-moss` — trigger not stated · strength not stated · 363 dl · Photos taken outdoors at night: bus stops, street food stalls, canal railings, parking lots, rooftop · [source](https://civitai.com/models/3048122?modelVersionId=3465868)
- `backrooms-endless-yellow-rooms-moss` — trigger not stated · strength `0.8` (stated) · 233 dl · The Backrooms as the original lore pictures them: mono-yellow wallpaper, damp beige carpet, humming  · [source](https://civitai.com/models/3029551?modelVersionId=3441279)

- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (24024) in same family+category**
- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Dark Ghibli Fairytales](https://civitai.com/models/1349631) (anima, 26,891 dl) — `Studio Ghibli Dark Fairytale` · strength not stated — **downloads 26891 >= 2x best available (10402) in same family+category**

### 34. Character sheets, multi-view, reference layouts

**Illustrious / NoobAI (Illustrious-XL based)**
- `character-design-sheet-flux-ill` — `multiple views`, `characterDesignSheetQuiron`, `characterDesignSheetxQuiron` · strength `0.7 - 1.3` (stated) · 5,338 dl · 👑 Character design sheet - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious this · [source](https://civitai.com/models/834362?modelVersionId=1838736)
- `reference-sheet-illustriousxl-lora-nochekaiser` — `<lora:reference-sheet-illustriousxl-lora-nochekaiser:1>, reference she` · strength `1.0` (stated) · 1,180 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/2799724?modelVersionId=3156120)

**Anima**
- `multiview-of-licking-penis-anima` — `multiview of licking penis anima` · strength `0.9` (stated) · 1,215 dl · multiple view of a girl licking penis. strength ~ 0.9. 2026.8.27 add 'Anima' examples of prompts, mu · [source](https://civitai.com/models/1746990?modelVersionId=3271432)
- `Multiview` — `multiview`, `multiple views, simple background, white background, spread legs, lyin` · strength not stated · 935 dl · lora for pure laziness tag: multiview · [source](https://civitai.com/models/2615809?modelVersionId=2937013)

**Krea2 (detailed-krea2)**
- `character-sheet-helper-krea2` — `FBcs` · strength `0.6` (stated) · 4,565 dl · This model is designed to help you build a character sheet for a character you plan to train, create · [source](https://civitai.com/models/2933017?modelVersionId=3319758)
- `krea2_charactersheet_full_v1` — `Follow the prompt template I left in the workflow.` · strength not stated · 3,182 dl · TripleView is a LoRA trained on approximately 300 character sheet samples, with a strong focus on ge · [source](https://civitai.com/models/2764727?modelVersionId=3203877)

**MOSS (Moss Image / kromoss)**
- `person-file-a-dead-serious-profile-sheet-f-moss` — trigger not stated · strength not stated · 709 dl · A vertical profile / dossier sheet: big headline, ID photo, data table (name, age, height and so on) · [source](https://civitai.com/models/3018066?modelVersionId=3426379)
- `online-meeting-video-conference-grid-scree-moss` — trigger not stated · strength not stated · 595 dl · A convincing online-meeting screenshot: several webcam tiles on a dark meeting interface — 2×2 grid, · [source](https://civitai.com/models/3014506?modelVersionId=3421649)

- Suggest ingest: [BFS - Best Face Swap](https://civitai.com/models/2027766) (krea2, 110,251 dl) — `body_swap: replace the person with the reference person.` · strength not stated — **downloads 110251 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (24024) in same family+category**
- Suggest ingest: [character sheet](https://civitai.com/models/368139) (pony, 30,253 dl) — trigger not stated · strength not stated — **downloads 30253 >= 2x best available (7066) in same family+category**

---

## Andrew's proven stacks

See `guides/andrew-proven-stacks.md` (detailed-krea2 identity/anatomy stack; kromoss benchmark stack).

## Keeping this current

Weekly: `bash scripts/update.sh` (see `UPDATING.md`): re-lists all Octavian123 HF repos, looks up new files on CivitAI, merges newly published LoRAs as candidates, rebuilds this skill and the catalogs, and pushes. Weights are never downloaded or ingested by it.
