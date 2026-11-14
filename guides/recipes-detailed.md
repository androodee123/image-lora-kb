# Detailed goal recipes (top 3 per family, with source-stated example prompts)

Same structure as SKILL.md recipes but deeper. Verified Graydient picks first; HF-only flagged; max 3 Suggest-ingest lines.

### 1. Photoreal skin, realism and detail

Pick one realism/detail LoRA first; extra ones fight each other.

**Illustrious / NoobAI (Illustrious-XL based)**
- `sexy_details_v5` — `sexydet` · strength not stated · 5,994 dl · This is a LORA trained on handpicked images of my personal preference. It is heavily nsfw based and  · [source](https://civitai.com/models/1615374?modelVersionId=3002225)
  - example prompt (from source, DPM++ 2M, steps 30): `(volumetric lighting), digital art style, drawn aesthetic, concept painting, ultra high definition, 1girl, Morphea from brown dust 2, huge breasts, red eyes, beautiful ey` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c359fcb0-4d93-41c4-8b73-994cca4e6596/original=true/132716571.jpeg)
- `zoda-nsfw-detailer-ill-2` — `zoda nsfw detailer ill 2` · strength `0.5 - 1.0` (stated) · 4,625 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2127970)
- `zoda-nsfw-detailer-ill` — `zoda nsfw detailer ill` · strength `0.5 - 1.0` (stated) · 1,942 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130890)

**SDXL**
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)
  - example prompt (from source, DPM++ 2M SDE, steps 43): `<lora:zoda_v1_sdxl:1> masterpiece, best quality, very aesthetic, absurdres, illustration , high resolution, sharp focus, soft lighting, dreamy, serene,  1girl, solo, long` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3feb3e6a-8ea1-43e1-90a3-d27ef4cbb2f8/original=true/95775045.jpeg)
- `amateur-amateur-professional-photography-xl` — trigger not stated · strength not stated · 283 dl · [source](https://civitai.com/models/2973823?modelVersionId=3370283)

**Anima**
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)
  - example prompt (from source, steps 32): `(masterpiece, ultra-HD, best quality, photorealistic, highly detailed, cinematic dramatic lighting), Score_9, score_8, score_7,newest,realistic,photorealism,sharp focus,a` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f99606b1-8a87-452d-8f1b-d7f9bab391ee/original=true/138686019.mp4)
- `realskin-slider-anima` — `realskin slider anima` · strength not stated · 6,621 dl · -1：更平滑、更二次元的皮肤质感  0：接近底模原始效果 +1：更真实的皮肤纹理、材质和光影表现 -1 = flat anime skin  0 = base +1 = realistic skin  · [source](https://civitai.com/models/2682590?modelVersionId=3068784)
- `detailer-anima` — `detailer anima` · strength `1` (stated) · 3,359 dl · Detailer lora for Anima. v2 - Whole thing is rebalanced. Colorfix added. Antisweat added. Additional · [source](https://civitai.com/models/2767064?modelVersionId=3142679)

**Krea2 (detailed-krea2)**
- `krea2_nud3` — trigger not stated · strength `0.7 - 1` (stated) · 24,860 dl · New KREA 2 Version Faceless dataset (doesn't influence face), can be used with character lora easily · [source](https://civitai.com/models/2174081?modelVersionId=3066702)
- `Emotions V1` — `Detailed Emotions and Expressions` · strength not stated · 10,258 dl · LEAVE A TIP IF YOU LIKE IT, I AM OUT OF BUZZ!! What it does: - Detailed and mostly accurate emotions · [source](https://civitai.com/models/2829908?modelVersionId=3193133)
- `oiled-skin-krea2` — trigger not stated · strength `1.0` (stated) · 8,842 dl · Krea 2 Turbo Info: Use the trigger phrase "OiledSkin" for best results. Keep strength at 1.0 for max · [source](https://civitai.com/models/87685?modelVersionId=3096878)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
  - example prompt (from source, er_sde, steps 50): `A premium, ultra-realistic cinematic portrait designed as a professional logo named REALISM ENHANCER. Show exactly half of a beautiful Japanese woman's face in an extreme` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7af9ea0-848d-4f42-bdde-f5268ab78f19/original=true/147014892.jpeg)
- `amateur-nudes-flux-wan-2-2-zit-zib-krea2` — `Amateur nudes - FLUX, Wan 2.2, ZIT, (ZIB), Krea2` · strength not stated · 3,474 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3417654)
- `realistic-nudes-krea2` — `completely nude woman, large breasts, shaved pubic area` · strength not stated · 2,794 dl · LoRA for generating very high-quality Realistic NUDES. Basic Triggers: nude, completely nude, toples · [source](https://civitai.com/models/1838378?modelVersionId=3416536)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1373) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1373) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (5994) in same family+category**

### 2. Phone / selfie / amateur-photo look

Pairs with a plain, believable scene description; avoid stacking with cinematic looks.

**Illustrious / NoobAI (Illustrious-XL based)**
- `persephone-aeons-echo-project-qt-ill` — `persephone`, `silver hair`, `very long hair`, `huge breasts` · strength `0.6 - 1.0` (stated) · 134 dl · Support my work or request a custom lora here! Even 1$ can make a big difference ☕ UPDT V2.0 + Masqu · [source](https://civitai.com/models/2176104?modelVersionId=3271186)
  - example prompt (from source, Euler a, steps 30): `masterpiece, best quality, amazing quality, very aesthetic, high resolution, ultra-detailed, absurdres, newest, <lora:Persephone:0.8>,persephone,1girl,red eyes,silver hai` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dd3d96f3-216e-4629-81f0-c7b537af77a7/original=true/140974246.jpeg)

**SDXL**
- `amateur-amateur-professional-photography-xl` — trigger not stated · strength not stated · 283 dl · [source](https://civitai.com/models/2973823?modelVersionId=3370283)
  - example prompt (from source, DPM++ 2M SDE, steps 32): `A portrait of a woman in a dress, natural setting, candid photo  <lora:Amateur_v1:2>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/996443bd-d6b5-44ed-a309-7f0b6e836dff/original=true/144228748.jpeg)

**Anima**
- `ILANIMA Irrumatio selfie NSFW Concept - ANIMA - NSFW_selfie_epoch_3` — `1girl, solo focus, selfie, reaching towards viewer, looking at viewer,`, `deepthroat,`, `clothed female nude male` · strength `0.7-0.9` (stated) · 907 dl · Like my model? Review, like, and post an image! Hope you have a nice day! Thanks! Just because why n · [source](https://civitai.com/models/2253084?modelVersionId=3249951)
  - example prompt (from source, er_sde_sgm_uniform, steps 25): `masterpiece, amazing quality, best quality, absurdres, highres, newest, detailed eyes, perfect eyes, score_7, score_8, amane misa, 1girl, bare shoulders, bead bracelet, b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c9f2a233-3d8c-467e-a0a1-b4fc2ca50335/original=true/140314851.jpeg)
- `ccdishwasher-style-anima` — trigger not stated · strength `0.8` (stated) · 318 dl · Model Introduction The dishwasher-style model boasts an extremely high level of accuracy. ANIMA V3:  · [source](https://civitai.com/models/2711269?modelVersionId=3434763)
- `big-breasts-selfie-anima` — `Huge breasts`, `Veiny breasts` · strength not stated · 280 dl · Big breast's · [source](https://civitai.com/models/2732963?modelVersionId=3072726)

**Krea2 (detailed-krea2)**
- `Amateur nudes - FLUX Wan 2.2 ZIT ZIB Krea2 - v1.0 Krea2 - Amateur_Nudes_v1_Krea2` — trigger not stated · strength not stated · 4,385 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3245545)
  - example prompt (from source, Euler, steps 8): `A young, nude white woman with light skin and straight, shoulder-length blonde hair snaps a selfie in a bathroom. She's got a slim bod, small tits, and a natural bush. Ro` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7ec336f-e3f1-492d-87bb-49703e9515e1/original=true/140173459.jpeg)
- `better-amateur-anal-xl` — `NM_amtanal,` · strength not stated · 2,454 dl · A Lora of Better amateur anal trigger tag: NM_AmtAnal, You can support my work by following the link · [source](https://civitai.com/models/963175?modelVersionId=3365704)
- `hot-shot-selfie-aesthetic-krea2` — trigger not stated · strength not stated · 2,257 dl · Glamourize your krea girls! My goal isn't realism but instead a curated aesthetic. This lora is an e · [source](https://civitai.com/models/2999042?modelVersionId=3401718)

**MOSS (Moss Image / kromoss)**
- `amateur-nudes-flux-wan-2-2-zit-zib-krea2` — `Amateur nudes - FLUX, Wan 2.2, ZIT, (ZIB), Krea2` · strength not stated · 3,474 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3417654)
  - example prompt (from source, Euler, steps 10): `A young, nude white woman with light skin and straight, shoulder-length blonde hair snaps a selfie in a bathroom. She's got a slim bod, small tits, and a natural bush. Ro` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/47813805-960c-4231-82a8-782173052aac/original=true/146244038.jpeg)
- `phone-photography-2000-2025-moss` — `This is a candid photograph taken with a smartphone of` · strength not stated · 2,706 dl · Stop prompting from scratch, explore 11,000+ Prompts for free 👉 PromptDexter.com LoRAs for simulatin · [source](https://civitai.com/models/2537408?modelVersionId=3426517)
- `direct-flash-film-point-and-shoot-flash-sn-xl` — trigger not stated · strength not stated · 2,456 dl · Color film snapshots shot with a cheap point-and-shoot and its on-camera flash: the nearest face and · [source](https://civitai.com/models/3013030?modelVersionId=3419791)

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **no Graydient LoRA in this family+category**
- Suggest ingest: [Amateur style - slider](https://civitai.com/models/1410317) (pony, 50,928 dl) — trigger not stated · strength not stated — **downloads 50928 >= 2x best available (1183) in same family+category**
- Suggest ingest: [LEAKCORE (LEAKED NUDES STYLE, Realism, Amateur)](https://civitai.com/models/1439962) (sdxl, 48,422 dl) — `amateur photo`, `film grain`, `face out of frame`, `taking a mirror selfie` · strength `0.7-1.1` (stated) — **downloads 48422 >= 2x best available (3670) in same family+category**

### 3. Cinematic film still look

Pick one look. Do not mix with digicam/amateur LoRAs.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-neo-noir-illustriousxl-zimageturbo-f-ill` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,477 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2078295)
  - example prompt (from source, DPM++ 2M, steps 25): `<lora:ayase_momo-koto-Illustrious v01:0.4> ayasemomo, hair between eyes, crossed bangs, green earrings, brown hair, red eyes, black choker, short hair, white shirt, red b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/edd14fa8-ef5a-4b17-8ed2-392eff3bc892/original=true/92165997.jpeg)
- `Kei Yuri Dirty Pair The Movie ダーティペア - v1.0 - mai_dirty_pair` — `mai_dirty_pair,1980s_\(style\),kei_\(dirty_pair\),dark-skinned_female,`, `mai_dirty_pair,1980s_\(style\),yuri_\(dirty_pair\),long_hair,blue_hair` · strength `0.8` (stated) · 622 dl · Character Set from anime movie "Dirty Pair: The Movie ダーティペア the Movie". This model offers a mini-si · [source](https://civitai.com/models/2840732?modelVersionId=3206701)
- `bayonetta-bayonetta-bloody-fate-movie-movi-ill` — `mai_bblf,mai_bayonetta,long_hair,black_hair,grey_eyes,mole_under_mouth` · strength `0.7` (stated) · 276 dl · Bayonetta (ベヨネッタ) from anime movie "Bayonetta: Bloody Fate ベヨネッタ ブラッディフェイト". This model offers a min · [source](https://civitai.com/models/3015280?modelVersionId=3422689)

**Anima**
- `Retro_Neo_Noir_Anima` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,301 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2803271)
  - example prompt (from source, er_sde, steps 30): `retro_neo_noir, retro, retro artstyle, 1girl, solo, long hair, magenta hair, purple hair, very long hair, flowing hair, blue eyes, looking at viewer, confident, smirk, se` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0bf57ec4-ab56-4f4c-ad42-feb026c3ba09/original=true/125356558.jpeg)
- `Retro_Synth_Noir_Anima_step00002300` — `retro_synth_noir, retro, retro_artstyle, film_grain,` · strength `0.7` (stated) · 1,394 dl · Anima version: weight between [0.7,1], best at 1 trigger words : retro_synth_noir, retro, retro_arts · [source](https://civitai.com/models/2038668?modelVersionId=2841795)
- `80s-fantasy-movie-anima` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 957 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3002110)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `70s-horror-movie-krea2` — `ArsMovieStill, movie still from a 1970s horror movie,` · strength not stated · 1,464 dl · This LoRA is designed to capture the specific atmosphere of 70s horror movies. The trigger words are · [source](https://civitai.com/models/863136?modelVersionId=3187148)
- `ektachrome-fade-film-krea2` — `ektachrome fade film` · strength `0.5–0.6` (stated) · 1,115 dl · MY FIRST LORA :  Style LoRA for Krea 2. Faded slide-film look: grain, mild highlight bloom, warm hig · [source](https://civitai.com/models/2904145?modelVersionId=3284125)

**MOSS (Moss Image / kromoss)**
- `direct-flash-film-point-and-shoot-flash-sn-xl` — trigger not stated · strength not stated · 2,456 dl · Color film snapshots shot with a cheap point-and-shoot and its on-camera flash: the nearest face and · [source](https://civitai.com/models/3013030?modelVersionId=3419791)
  - example prompt (from source, Euler, steps 50): `directflashfilmconcept, A color film snapshot taken with a cheap point-and-shoot camera and its direct flash catches a filthy rented apartment kitchen: a Russian adult ma` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2562858c-25bb-4f8a-ba2d-15bfe8d7da11/original=true/146343112.jpeg)
- `tjfilm-style-moss` — `vifilm` · strength `1` (stated) · 497 dl · TJFilmStyle is a style LoRA I specifically trained to simulate real film photography, featuring the  · [source](https://civitai.com/models/2840370?modelVersionId=3454092)
- `80s-fantasy-movie-moss` — `ArsMovieStill, 80s Fantasy Movie Still` · strength not stated · 483 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3413429)

- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (5994) in same family+category**
- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **no Graydient LoRA in this family+category**
- Suggest ingest: [Cinematic Shot ✨](https://civitai.com/models/432586) (krea2, 62,180 dl) — `zy_cinematic` · strength not stated — **downloads 62180 >= 2x best available (11215) in same family+category**

### 4. Anime / manga / illustration style

One style LoRA at a time; add a second only at a lower strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `figure-anime-xl` — `fig`, `nendo`, `figma` · strength not stated · 7,822 dl · Attempt at anime figure style,  trigger word is "fig"  for nendoroid style is "nendo" Intento de est · [source](https://civitai.com/models/631010?modelVersionId=1284415)
- `dark-fantasy-90-s-anime-style-illustriousx-ill` — `dark_fantasy_style, dark fantasy, retro,` · strength `0.8` (stated) · 5,191 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : dark_fantasy_style, dark fantasy,  · [source](https://civitai.com/models/1108959?modelVersionId=1245970)

**SDXL**
- `anime-figure-xl` — `anifigurestyle` · strength `0.5 to 0.7` (stated) · 792 dl · Trained with SDXL base model, using this lora with other XL models will produce uncontrolled results · [source](https://civitai.com/models/429926?modelVersionId=508307)
  - example prompt (from source, DPM++ 2M SDE Heun, steps 75): `full body, 1girl, nsfw, showing private part, sitting, classroom, upper-class school uniform, doujin cover, reflective, \\o/, drooling, sweat, wet body, climax, (see-thro` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bd5f68aa-d66a-41a3-9b31-84a18f03c358/original=true/12556849.jpeg)

**Pony (Pony Diffusion XL)**
- `Prison School anime style PDXL - PSV1F - Prison_School_anime_style_Pony_r2` — `score_9_up, score_8_up, score_7_up,` · strength not stated · 1,686 dl · [source](https://civitai.com/models/525298?modelVersionId=583646)
  - example prompt (from source, DDIM, steps 30): `score_9_up, score_8_up, score_7_up, <lora:Prison_School_anime_style_Pony_r2:1>, meiko shiraki,  solo, glasses, sky, cloud, day, grey hair, short hair, choker, brown eyes,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3bb10e08-bb08-487c-bfa9-1922af93ac6d/original=true/16455339.jpeg)
- `uno-makoto-marumiya-pony-xl` — trigger not stated · strength not stated · 1,603 dl · [source](https://civitai.com/models/347454?modelVersionId=388734)
- `terayama-reiko-anime-golden-boy-ponyxl-sd1-pony` — `Terayama Reiko, 1girl,`, `black hair, long hair, makeup, lipstick, brown eyes,`, `bikesuit,`, `open clothes, no bra, cleavage, unzipped` · strength not stated · 916 dl · XL version · [source](https://civitai.com/models/94159?modelVersionId=770710)

**Anima**
- `90s_anime_melancholy_Anima-step00003300` — `90s_melancholy, retro,` · strength `0.8` (stated) · 3,887 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : 90s_melancholy, retro, Anima vers · [source](https://civitai.com/models/1738546?modelVersionId=2820017)
  - example prompt (from source, er_sde, steps 30): `90s_melancholy, retro, (ayase momo:0.6), hair between eyes, crossed bangs, green earrings, brown hair, red eyes, black choker, short hair, white shirt, red bowtie,pleated` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/80f441f8-2028-46dd-ad12-1f94a09eff0f/original=true/126004280.jpeg)
- `90s anime aesthetic Anima-step00001600` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle,` · strength `0.8` (stated) · 3,164 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=2795022)
- `buanime-nsfw-style-pack-anima` — `BuAnime NSFW Style Pack Anima` · strength `0.7–1.2` (stated) · 2,847 dl · Bu Hentai Fantasy [Bu_HF] Bu Hentai Fantasy is my personal LoRA with a stronger focus on fantasy whi · [source](https://civitai.com/models/2645819?modelVersionId=3301514)

**Krea2 (detailed-krea2)**
- `Line Art Anime Flat - Krea.v2 - K2_Anime_Flat_V20_nnegret` — `线条动漫` · strength `0.6` (stated) · 2,496 dl · 交流群：173273201 最新的V3主要加强了线条风格，以及对tag形式的提示词支持更好了 使用技巧 1. 最佳参数组合 参数推荐值： LoRA Weight 0.6 ~ 0.9（默认 0.6） C · [source](https://civitai.com/models/2741033?modelVersionId=3103017)
  - example prompt (from source, er_sde, steps 8): `线条动漫, 一个色情的女美女双手交叉祷告` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c3980eb5-22ee-4594-b75f-2868004d09cf/original=true/135871305.jpeg)
- `clusterfuck-western-illustration-comic-sty-krea2` — `Illustration` · strength not stated · 1,863 dl · First of all, I don't know what I'm doing really. I just trial and errored my way through dozens of  · [source](https://civitai.com/models/154425?modelVersionId=3084476)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-2` — `retro_scifi_90s, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 1,803 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=3346833)

**MOSS (Moss Image / kromoss)**
- `anime-flat-style-moss` — trigger not stated · strength not stated · 2,919 dl · This LoRA is designed to generate vibrant, clean anime artwork featuring bold, flat colors with mini · [source](https://civitai.com/models/1952560?modelVersionId=3413292)
  - example prompt (from source, Euler, steps 8): `digital art, anime style, female knight, white and gold armor, red cape flowing, red-haired, determined expression, holding sword in right hand, dragon in background, dra` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c184d2d8-d212-49c7-923e-26ec450e38f1/original=true/146033519.jpeg)
- `cel-animation-art-style-moss` — trigger not stated · strength not stated · 1,743 dl · Cel-Animation Art Style No trigger words are required, and the default strength is recommended. It w · [source](https://civitai.com/models/3012746?modelVersionId=3419395)
- `il-meion-meion39-artist-style-moss` — `MeIoN Style Type-I`, `MeIoN Style Type-II` · strength not stated · 1,540 dl · Help fuel my passion! Even $1 makes a difference. ☕ https://ko-fi.com/flyx3 让我保持创作热情，付费款/隐藏款模型可以在 爱发 · [source](https://civitai.com/models/2798280?modelVersionId=3423430)

- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (23879) in same family+category**
- Suggest ingest: [MeMaXL Flat Anime Style - Noob/Illustrious/Pony/XL](https://civitai.com/models/269772) (illustrious, 63,089 dl) — `memaxl6_a`, `memaxl6_b`, `memaxl6_c`, `memaxl6_d` · strength not stated — **downloads 63089 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Vector illustration](https://civitai.com/models/60132) (sdxl, 36,693 dl) — `color icon` · strength `0.65-0.9` (stated) — **downloads 36693 >= 2x best available (3670) in same family+category**

### 5. Retro / decade looks (70s-2000s, VHS, airbrush)

Name the decade in the prompt text as well as the trigger.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `retro-neo-noir-illustriousxl-zimageturbo-f-ill` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,477 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2078295)
- `Dirty Pair Yuri and Kei 2-in-1 1980s style - V1 - Yuri_and_Kei_Dirty_Pair` — `1980s (style), retro artstyle, traditional media`, `Yuri (Dirty Pair), 1girl, solo, blue hair, long hair`, `Yuri's standard outfit (appearance), single glove, yellow belt, jewelr`, `Kei (Dirty Pair), 1girl, solo, red hair, short hair,` · strength not stated · 1,555 dl · I just like retro anime from before I was born, so here is a classic pair of characters in one model · [source](https://civitai.com/models/1828907?modelVersionId=2069696)

**Pony (Pony Diffusion XL)**
- `80s-vintage-porn-magazine-style-v1-pony` — `80spm, vintage porn, 80s era, 1980s photo` · strength not stated · 2,061 dl · [source](https://civitai.com/models/1007808?modelVersionId=1129515)
  - example prompt (from source, DPM++ 2M SDE, steps 30): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, rating_explicit, 80spm, vintage porn, 80s era, 1980s photo, 1girl, 1boy, breasts, nipples, penis, smi` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fd65c31a-60fd-44e0-8ab4-7135ec84cc7a/original=true/43686875.jpeg)
- `FTRXSRFQS8A10TW5FTQ3PVKD10` — `R3troF4nt4sy, fantasy art, painting,` · strength not stated · 90 dl · This should help you make a retro fantasy look to your babes. · [source](https://civitai.com/models/2564814?modelVersionId=2881983)

**Anima**
- `90s anime aesthetic Anima-step00001600` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle,` · strength `0.8` (stated) · 3,164 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=2795022)
  - example prompt (from source, er_sde, steps 30): `90s_anime_aesthetic, 1990s (style), retro, retro artstyle,1girl, solo, blonde hair, long hair, straight hair, green eyes, elf ears, pointy ears, smile, looking at viewer,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/73b082a5-37ce-4cbb-8e0e-5a4ab0ccdab9/original=true/125047093.jpeg)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-5` — `retro_scifi_90s_anime_style, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 2,778 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=2808683)
- `Retro_Neo_Noir_Anima` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,301 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2803271)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `Private Magazine Style - Private Magazine 2000s - Private_Magazine_2000s_v1` — `privatemag` · strength `1.5` (stated) · 2,563 dl · Private Magazine 1970s NEW! Tested raising the lora weight to 1.5 and found out it helps a lot if th · [source](https://civitai.com/models/2833524?modelVersionId=3266535)
- `Private Magazine Style - Private Magazine 1990s - Private_Magazine_1990s_v1` — `90s magazine photography` · strength `1.5` (stated) · 2,318 dl · Private Magazine 1970s NEW! Tested raising the lora weight to 1.5 and found out it helps a lot if th · [source](https://civitai.com/models/2833524?modelVersionId=3256977)

**MOSS (Moss Image / kromoss)**
- `retro-vintage-photo-moss-z-image-base-xl` — trigger not stated · strength `2` (stated) · 1,203 dl · I spent some serious time digging through the Internet Archive to put this together. This LoRA is tr · [source](https://civitai.com/models/2380695?modelVersionId=3419437)
  - example prompt (from source, er_sde, steps 25): `A nostalgic 1970s street portrait captures a young woman with feathered honey-blonde hair and curtain bangs smiling warmly on an urban city avenue. She poses in a medium ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5123b9a8-2a36-4f80-9c19-4770c8def21a/original=true/146334272.jpeg)
- `retro-vintage-comics-style-xl` — trigger not stated · strength not stated · 603 dl · This LoRA is trained to reproduce a vintage illustrated comic style, with a focus of detailed line a · [source](https://civitai.com/models/1082272?modelVersionId=3418240)
- `80s-fantasy-movie-moss` — `ArsMovieStill, 80s Fantasy Movie Still` · strength not stated · 483 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3413429)

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **no Graydient LoRA in this family+category**
- Suggest ingest: [2000s Analog Core](https://civitai.com/models/1134895) (krea2, 40,517 dl) — trigger not stated · strength `0.9` (stated) — **downloads 40517 >= 2x best available (11215) in same family+category**
- Suggest ingest: [NEW ERA / LORA / PONY DIFFUSION](https://civitai.com/models/28600) (pony, 38,748 dl) — `retro artstyle`, `1990s \(style\)`, `1980s \(style\)`, `2000s \(style\)` · strength not stated — **downloads 38748 >= 2x best available (8308) in same family+category**

### 6. Comic, cartoon and western animation

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-comic-random-generator-start-story-ill` — `(fcomicstart:2), (1page:2),comic,Multi view, Frame, Text, speech bubbl`, `(fcomicstart:2), (2page:2),comic,Multi view, Frame, Text, speech bubbl`, `(fcomicstart:2), (3page:2),comic,Multi view, Frame, Text, speech bubbl` · strength not stated · 6,780 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=2167446)
  - example prompt (from source): `9img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d22e5959-f5c4-4a90-a1c9-e5dc636790a8/original=true/97550425.mp4)
- `hentai-comic-random-generator-lastpage-fin-ill` — `lastpage:2, comic:1.25, Multi view, Frame, Text:1.5, speech bubble:1.5`, `Mini characters, chibi characters,`, `Close-up face, hugging, kissing,` · strength not stated · 6,513 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/594918?modelVersionId=2175478)
- `hentai-comic-random-generator-start-story-ill-2` — `(1page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr`, `(2page),(comic),Multi view, Frame, Text, speech bubble, frame, heart, `, `(3page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr` · strength not stated · 3,139 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=2109590)

**SDXL**
- `dizzycartoonstyle-e10-xl` — `dizzycartoonstyle` · strength not stated · 19 dl · [source](https://civitai.com/models/2950113?modelVersionId=3341094)
  - example prompt (from source, Euler, steps 25): `1girl, solo, breasts, short hair, shirt, looking at viewer, upper body, white shirt, medium breasts, lips` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/74eeb86c-1c8d-4a60-9599-2d22f04876af/original=true/143265465.jpeg)

**Pony (Pony Diffusion XL)**
- `hentai-comic-random-generator-start-story-pony` — `(1page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr`, `(2page),(comic),Multi view, Frame, Text, speech bubble, frame, heart, `, `(3page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr` · strength not stated · 8,308 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=661873)
  - example prompt (from source, DPM++ 2M Karras, steps 30): `(nsfw:1), (Uncensored:1), score_9, score_8_up, score_7_up, source_anime, BREAK  <lora:FComic1To3Page_Pony_V1:1>(1page),comic,Multi view, Frame, Text, speech bubble, frame` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/8babe0b8-d99f-46de-a3ea-79de87370f3e/original=true/20772820.jpeg)
- `hentai-comic-random-generator-lastpage-fin-pony` — `lastpage, (comic:1.25), (Multi view, Frame, Text, speech bubble, frame` · strength not stated · 7,136 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/594918?modelVersionId=664510)

**Anima**
- `hentai-comic-random-generator-lastpage-fin-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text` · strength not stated · 3,507 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/594918?modelVersionId=3018129)
  - example prompt (from source): `10image join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b2f033c0-9005-4f25-94c6-812c6d8ae5c5/original=true/133313917.mp4)
- `hentai-comic-random-generator-start-story-anima` — `1page, Hentai comic style. Multi-view with 3-5 or more panels displayi`, `2page, Hentai comic style. Multi-view with 3-5 or more panels displayi`, `3page, Hentai comic style. Multi-view with 3-5 or more panels displayi` · strength not stated · 3,403 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=3014531)
- `FComic1to1000_Anima` — `Hentai comic style. Multi-view with 3 or more panels displaying text, ` · strength not stated · 2,696 dl · 💕This model is for "ANIMA".💕 The prompt structure is significantly different from Illustrious and Po · [source](https://civitai.com/models/2599213?modelVersionId=2919739)

**Krea2 (detailed-krea2)**
- `clusterfuck-western-illustration-comic-sty-krea2` — `Illustration` · strength not stated · 1,863 dl · First of all, I don't know what I'm doing really. I just trial and errored my way through dozens of  · [source](https://civitai.com/models/154425?modelVersionId=3084476)
- `dc-sci-fi-krea2` — `DCSC1F1.` · strength not stated · 1,567 dl · v1 krea2raw Trigger = DCS1F1. v1 krea2raw Trained @10,000 Steps, Rank 64, Captioned with GPT4.1, Dat · [source](https://civitai.com/models/2976222?modelVersionId=3373246)
- `FComic1to1000_KR2` — `hentai comic style, comic,  Text, speech bubble, frame, heart, trembli` · strength not stated · 1,248 dl · ⚠️This is KREA 2 (RAW) PROTOTYPE Model 🎉You can now specify arbitrary dialogue within speech bubbles · [source](https://civitai.com/models/2846760?modelVersionId=3214289)

**MOSS (Moss Image / kromoss)**
- `retro-vintage-comics-style-xl` — trigger not stated · strength not stated · 603 dl · This LoRA is trained to reproduce a vintage illustrated comic style, with a focus of detailed line a · [source](https://civitai.com/models/1082272?modelVersionId=3418240)
  - example prompt (from source, er_sde, steps 25): `a woman wearing a silver scifi jumpsuit sneaks around a corner of a castle wall, holding a futuristic handgun. A knight in medieval armor stands on the other side, unawar` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b56519e3-9b2e-4b6d-8aec-b998491f3105/original=true/146267267.jpeg)
- `ag-vassago-flat-cartoon-style-moss` — `V4SS4G0X` · strength `0.6-0.8` (stated) · 337 dl · Ars Goetia is series of loras made on a whim, on variety of images, made from mix of Midjourney, Tum · [source](https://civitai.com/models/2853357?modelVersionId=3431233)
- `cartoon-style-moss` — `c4rt00nbun5, Digital cartoon illustration. The overall style is bold w` · strength not stated · 290 dl · A mixture of different datasets from my MJ style collection for Anima. · [source](https://civitai.com/models/3020107?modelVersionId=3428996)

- Suggest ingest: [Hentai Comic Random Generator (FULL COLOR) Anima / Pony / IL XL / フルカラ](https://civitai.com/models/585589) (illustrious, 66,772 dl) — `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view:1.1, Frame, Text, speech bubb` · strength not stated — **downloads 66772 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Hentai Comic Random Generator (HARD CORE) Anima / Pony / IL XL / ハードコア](https://civitai.com/models/588622) (illustrious, 55,821 dl) — `fcomichardcore, (comic:1.25),(Multi view, Frame, Text, speech bubble, ` · strength not stated — **downloads 55821 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Cartoon style](https://civitai.com/models/45521) (pony, 24,606 dl) — trigger not stated · strength not stated — **downloads 24606 >= 2x best available (8308) in same family+category**

### 7. Painting, watercolor, oil, sketch, ink

**Illustrious / NoobAI (Illustrious-XL based)**
- `chines_Ink_painting_IL_MIX` — `wuguanzhong,,zhang daqian,qi baishi, painting \(medium\), traditional ` · strength `1.75-2.5` (stated) · 1,139 dl · Modern_chinese_ink_painting_ILThe Illustrious version of sd1.5(https://civitai.com/models/736379?mod · [source](https://civitai.com/models/1579508?modelVersionId=1787384)
  - example prompt (from source, LCM, steps 12): `masterpiece, best_quality, very_aesthetic, highres, absurdres,very_aesthetic, ultra detailed, <lora:negXL:0.5>   <lora:Modern_chinese_ink_painting_IL_MIX:1> wuguanzhong,,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1739c154-d198-4c7d-9df4-275eaebd8aab/original=true/76219869.jpeg)
- `personal-style-manga-sketch-style-v1-ill` — `MagsketchStyle`, `monochrome`, `traditional media`, `sketch` · strength not stated · 657 dl · This is a drawing style based on my personal sketches. I used it to generate random images in my tra · [source](https://civitai.com/models/1694909?modelVersionId=1918183)
- `amamiya-reina-star-twinkle-precure-ill` — `amamiyareina` · strength not stated · 375 dl · prompt example : anime screencap, solo,1girl, amamiyareina,pants,pink dress, ribbon, hair bow<lora:a · [source](https://civitai.com/models/2932530?modelVersionId=3319109)

**SDXL**
- `Ink Splatter Abstract Art Style SDXL LoRA - v1.0 - art_ink_splatter_abstract_v1` — trigger not stated · strength not stated · 41 dl · [source](https://civitai.com/models/2870349?modelVersionId=3243001)
  - example prompt (from source, DPM++ 2M, steps 28): `<lora:art_ink_splatter_abstract_v1:0.80>, artinksplatter, a portrait of a young woman, expressive ink-splatter abstract art, dynamic dripping texture, bold contrast, ener` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/40602055-a1e7-418b-b688-67108802ee73/original=true/140278477.jpeg)

**Pony (Pony Diffusion XL)**
- `hash sketch - v 8.26 noobai - Desenho_de_Rachurado` — trigger not stated · strength not stated · 17 dl · [source](https://civitai.com/models/2242730?modelVersionId=2524719)
  - example prompt (from source, DDIM, steps 30): `score_9,score_8_up,score_7_up, 1man, solo, muscular chest, short hair, handsome, rosy cheeks, cute, unzipped hooded brown bear onesie, penis showing, precum, pubic hair, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e26b7761-a914-4d61-986c-393714de7dc8/original=true/115410322.jpeg)

**Anima**
- `Anime Oil Touch - v1.0 - 123.1` — trigger not stated · strength not stated · 695 dl · 默认lora强度为1即可。 · [source](https://civitai.com/models/2884752?modelVersionId=3260812)
  - example prompt (from source, Euler a, steps 15): `fujita kotone (gakuen idolmaster), blonde hair, yellow eyes, long hair, twin braids, fang, blush, idol, casual clothes, on bed, front view, masterpiece, best quality   Th` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/9e74b012-ac76-42b3-b949-6940260cbe1c/original=true/140648775.jpeg)
- `kok-takenawa-style-pastel-anime-illustrati-anima` — `@koktakenawa`, `anime illustration, clean lineart, pastel colors,` · strength `1.0` (stated) · 360 dl · A style LoRA trained on 158 images of the artist kok/takenawa for anime illustrations with light lin · [source](https://civitai.com/models/2976007?modelVersionId=3372990)
- `yuming-li-style-luminous-painterly-fantasy-anima` — `@yumingli`, `painterly, soft brushwork, dramatic lighting,` · strength `0.8` (stated) · 280 dl · This LoRA was trained on a set of 87 curated images of the artist Yuming Li, with both booru-style t · [source](https://civitai.com/models/2971260?modelVersionId=3367097)

**Krea2 (detailed-krea2)**
- `krea2_ta86_inkriot_V2` — `ta86_inkriot`, `graphic cel shading`, `bold black outlines` · strength `2` (stated) · 4,844 dl · ta86_inkriot Graphic Cel Shaded Chaos and Hand-Inked Worldmorph-like Aesthetics. You all can guess w · [source](https://civitai.com/models/2827717?modelVersionId=3190465)
  - example prompt (from source, (None, steps 12): `ta86_inkriot, a masked man trader portrait, medium close-up, off-center framing, slight low angle, cracked patchwork mask with asymmetrical eye plates, layered scarf coll` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e30c400c-84c8-4cd6-9e75-c014cf78bd7a/original=true/138511383.jpeg)
- `fantasy-graphite-sketch-krea2` — `@fantasysketcheight` · strength `0.5 to 0.7` (stated) · 863 dl · So, yeah, descriptions are in model descriptions. V1 Just a simple sketch lora for Pony. I wanted a  · [source](https://civitai.com/models/580163?modelVersionId=3188163)
- `kreasketching-krea2` — `Bradhamel art style` · strength not stated · 842 dl · Images were created with ComfyUI and include workflow. If your images are not appearing on my model  · [source](https://civitai.com/models/2817577?modelVersionId=3316359)

**MOSS (Moss Image / kromoss)**
- `friendly-sketch-moss` — `friendlysketch` · strength `0.8 to 1.2` (stated) · 599 dl · Apply a friendly, warm style to your Moss-Image illustrations. (See the Krea 2 version or the Anima  · [source](https://civitai.com/models/3013132?modelVersionId=3419935)
  - example prompt (from source, Euler, steps 10): `friendlysketch, A young woman in street clothes , blonde hair half-up with a thin braid on her left and right temple  Standing on a sidewalk in NYC, hazy warm afternoon l` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f300e2cf-ec80-4126-bf77-a425f192a304/original=true/146348754.jpeg)
- `hd-digital-painting-moss` — `digital painting` · strength not stated · 405 dl · A sharp digital painting style that doesn't look plastic! · [source](https://civitai.com/models/3034351?modelVersionId=3447679)
- `digital-painting-moss` — `dpaintingM0style`, `illustration` · strength not stated · 362 dl · Based on art by Anato Finnstark. · [source](https://civitai.com/models/2516075?modelVersionId=3424792)

- Suggest ingest: [Vixon's Classic Art Styles - Detailed Painting](https://civitai.com/models/888250) (pony, 40,117 dl) — `1dk`, `painting (medium)` · strength not stated — **downloads 40117 >= 2x best available (8308) in same family+category**
- Suggest ingest: [zyd232's Ink Style](https://civitai.com/models/73305) (sdxl, 30,128 dl) — `zydink`, `ink sketch` · strength `0.6 to 1.2` (stated) — **downloads 30128 >= 2x best available (3670) in same family+category**
- Suggest ingest: [ClassipeintXL (oil paint / oil painting style)](https://civitai.com/models/127139) (sdxl, 25,007 dl) — `oil painting` · strength not stated — **downloads 25007 >= 2x best available (3670) in same family+category**

### 8. 3D render / CG / game-art look

**Illustrious / NoobAI (Illustrious-XL based)**
- `sleepless-a-midsummer-night-s-dream-girls-ill` — `Mamiya Marie Game`, `thighhighs, dress, underwear, thighs, choker, necklace` · strength `0.8` (stated) · 360 dl · LORA CHARACTER FROM Sleepless: A Midsummer Night's Dream Trigger Words: Mamiya Marie + Game or Anime · [source](https://civitai.com/models/2111079?modelVersionId=2388560)
  - example prompt (from source, euler-a, steps 20): `masterpiece, anime source, newest, Mamiya Marie, solo, looking at viewer, smile, thighhighs, dress, bare shoulders, underwear, panties, thighs, choker, necklace, indoors,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/47c0aca2-ffeb-4739-bd47-223b315edfe4/original=true/109445623.jpeg)
- `ssurface3d-style-2-0-ill` — `ssurface3d style` · strength not stated · 103 dl · This is my first time training an AI to try and replicate the style of the artist ssurface3d, so the · [source](https://civitai.com/models/3006693?modelVersionId=3411491)
- `mogudan-style-artbook-cg-ill` — `m0gu1dan0cgsty` · strength not stated · 102 dl · ver1 · [source](https://civitai.com/models/2979935?modelVersionId=3377917)

**Anima**
- `MogudanOldStyle_AnimaBaseV10_byKonan` — trigger not stated · strength `0.8-1` (stated) · 977 dl · Trained on Anima with 103 pictures. Best result with weight between : 0.8-1. Reviews are really appr · [source](https://civitai.com/models/2658734?modelVersionId=2985451)
  - example prompt (from source, ER SDE, steps 32): `masterpiece, best quality, 1girl, ayanami rei,  short hair,blue hair, red eyes, tokyo-3 middle school uniform,  huge breasts, impossible shirt,  expressionless,  solo,  l` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3c1b4f4a-fa92-4cb7-80b0-b7795c85572e/original=true/132163194.jpeg)
- `aziib-pixel-style-anima` — `aziib pixel style` · strength not stated · 580 dl · trigger word for Anima, Krea2 and MiniMax H3 : aziib pixel style trigger word for Z-image Turbo: azi · [source](https://civitai.com/models/672328?modelVersionId=3402371)
- `Miro3D Style Characters G4E Bloodlust Cerene - Anima V1.0 - Miro3D_3D_Artstyle_ANI-step00007840P96` — `miro3dstyle glossy 3D CGI render`, `wearing black deep v dress with purple lace bolero and matching high h`, `taram3 with fair skin, platinum blonde side swept hair, light eye make`, `wearing white lace halter dress and transparent high heels` · strength not stated · 483 dl · This is a model replicating the old 3D art style of the artist Miro3D The MOSS Image versions V0.5 a · [source](https://civitai.com/models/2848146?modelVersionId=3215950)

**Krea2 (detailed-krea2)**
- `krea2 sex 淫模 - CG - krea cowgirl` — `kreacowgirl, 1girl, 1boy, hetero, long hair, ass, black hair, anus, gi` · strength `0.6–0.7` (stated) · 4,986 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3158775)
  - example prompt (from source, Euler, steps 8): `kreacowgirl, 1girl, 1boy, hetero, nipples, breasts, jewelry, sex, penis, nude, realistic, girl on top, necklace, straddling, navel, closed eyes, cowgirl position, long ha` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c5b203de-9c43-48d2-804d-e5f8d667e8c5/original=true/137626899.jpeg)
- `pure-pixar-3d-krea2` — `KR2Pix` · strength not stated · 1,981 dl · This is a style LoRA that blends Pixar and realistic aesthetics. Use the following sentences or term · [source](https://civitai.com/models/2977241?modelVersionId=3374517)
- `pixelart-5x5-v1-krea2` — `pixelart 5x5 v1 krea2` · strength not stated · 1,301 dl · Pixel Art 16-Bit Style (5x5 Grid) - Krea 2 🎮 Description This LoRA adds a crisp, clean 16-bit pixel  · [source](https://civitai.com/models/2890305?modelVersionId=3267619)

**MOSS (Moss Image / kromoss)**
- `stylr-blender3d-nai5-moss` — `@blender` · strength not stated · 1,508 dl · Moss&Anima-V2.0 触发词：@blender, 辅助提示词：dreamy smooth polished body rendering, wet oily skin look, anime · [source](https://civitai.com/models/3028260?modelVersionId=3441491)
- `3dcg-master-ultimate-stylized-cg-skin-glos-v3-moss` — `style_3dcg_master` · strength `1.0` (stated) · 964 dl · # 🌟 3DCG Master: Stylized Anime 3D & Skin Gloss LoRA > 🔥 Latest Version: V3 (Pure Anime 3D & Style B · [source](https://civitai.com/models/3018834?modelVersionId=3431432)
- `pixel-art-moss` — trigger not stated · strength `1.0` (stated) · 766 dl · moss-pixelart-v.0.3 Model Description moss-pixelart-v.0.3 is a Low-Rank Adaptation (LoRA) model fine · [source](https://civitai.com/models/3024672?modelVersionId=3434941)

- Suggest ingest: [3D rendering style](https://civitai.com/models/73756) (sdxl, 177,723 dl) — `3DMM` · strength `2` (stated) — **downloads 177723 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Pixel Art XL](https://civitai.com/models/120096) (sdxl, 120,889 dl) — trigger not stated · strength not stated — **downloads 120889 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Illustrious  Pixel Art XL & 1.5 By creativehotia](https://civitai.com/models/43820) (illustrious, 55,968 dl) — `pixel` · strength `1` (stated) — **downloads 55968 >= 2x best available (23879) in same family+category**

### 9. Fantasy, sci-fi, cyberpunk, horror worlds

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `dark-fantasy-90-s-anime-style-illustriousx-ill` — `dark_fantasy_style, dark fantasy, retro,` · strength `0.8` (stated) · 5,191 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : dark_fantasy_style, dark fantasy,  · [source](https://civitai.com/models/1108959?modelVersionId=1245970)
- `Lucy from Cyberpunk Edgerunners IllustriousXL - v1.2 - ILCPELucy` — `CPELucy, 1girl, short hair, White hair, multicolored hair, multicolore` · strength not stated · 1,157 dl · Hey Everyone! Reviews, Hearts, Likes etc. are very appreciated! The outcome of your generations may  · [source](https://civitai.com/models/1154116?modelVersionId=2309390)

**SDXL**
- `raven-mercer-a-gothic-beauty-with-a-danger-xl` — `cfRavenWoman` · strength not stated · 24 dl · [source](https://civitai.com/models/3047362?modelVersionId=3464623)
  - example prompt (from source, DPM++ 2M SDE, steps 32): `cfRavenWoman, dramatic three-quarter-length gothic fashion portrait in an old Victorian mansion, wearing an elaborate fitted black velvet gown with a structured bodice, i` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/663f8ab3-6bfe-4c98-9f7d-01eea3686220/original=true/148686470.jpeg)

**Pony (Pony Diffusion XL)**
- `karin-cecil-vongielen-space-pirate-sara-uc-pony` — `vongielentwin`, `black hair`, `long hair`, `red eyes` · strength not stated · 302 dl · Base version, trained here on Civitai 6 Epochs, 99 uncropped pictures, 0.3 threshhold, 20 tags, 3 re · [source](https://civitai.com/models/1191236?modelVersionId=1341210)
  - example prompt (from source, Euler a, steps 24): `score_9, score_8_up, score_7_up, source_anime, source_hentai, solo, indoors, medium cowboy shot, <lora:Von_Gielen_Twin-000006:1>, vongielentwin, 1girl, standing, black ha` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2432da9d-3365-4cf4-90e9-b06d1206f880/original=true/54366534.jpeg)
- `sara-scorpion-pirat-sala-uchuu-kaizoku-sar-pony` — `Sara_Scorpion`, `blonde hair, blue eyes, long hair, side-swept bangs, earrings,`, `dark blue coat, long coat, open coat, red inner coat, high collar, sho`, `visual novel style, game cg,` · strength not stated · 180 dl · First version of the 50th Lora. · [source](https://civitai.com/models/2486705?modelVersionId=2795758)
- `sylia-von-bernstein-uchuu-kaizoku-sara-spa-pony` — `Sylia_Von_Bernstein`, `orange hair, purple eyes, short hair, side bangs, bangs between eyes,`, `black leotard, turtleneck leotard, sleeveless leotard, white trim, sid`, `white armor, breastplate, single shoulder plate, right shoulder plate,` · strength not stated · 117 dl · First version of Sylia and second part of 50th Lora celebration. · [source](https://civitai.com/models/2489498?modelVersionId=2798736)

**Anima**
- `moriimee-gothic-niji-journey-style-anima` — `realistic` · strength `0.8-1` (stated) · 3,603 dl · Trained on Anima with 36 pictures. Best result with weight between : 0.8-1. Prompts : realistic Insp · [source](https://civitai.com/models/2485109?modelVersionId=2945538)
  - example prompt (from source, ER SDE, steps 32): `masterpiece, best quality, realistic, 1girl, purple eyes, black hair, long hair, blunt bangs, hime cut, eyelashes, lips, makeup, black dress, black neck ribbon, puffy sle` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1a761f16-2982-4dbc-968a-da236ea8af11/original=true/130707745.jpeg)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-5` — `retro_scifi_90s_anime_style, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 2,778 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=2808683)
- `moriimee-gothic-xl` — `morimee_style`, `cute face`, `nun,latex,bdsm outfit` · strength not stated · 2,590 dl · Style LoRa based on the Niji Midjourney aesthetic of goth style from MoriiMee (Twitter / DeviantArt) · [source](https://civitai.com/models/915918?modelVersionId=3124327)

**Krea2 (detailed-krea2)**
- `80s-fantasy-movie-krea2` — `ArsMovieStill, 80s Fantasy Movie Still,` · strength not stated · 3,823 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3091396)
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-2` — `retro_scifi_90s, retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 1,803 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=3346833)
- `Nightmare_Grunge_Krea_2_Version_epoch_9` — trigger not stated · strength `0.5 to 1` (stated) · 1,769 dl · Many models are very "clean" and "bright"- grunge, dirt, darkness and atmospheric horror details are · [source](https://civitai.com/models/2804228?modelVersionId=3161763)

**MOSS (Moss Image / kromoss)**
- `80s-fantasy-movie-moss` — `ArsMovieStill, 80s Fantasy Movie Still` · strength not stated · 483 dl · This LoRA is designed to capture the distinct look and feel of early 80s fantasy movies. The trigger · [source](https://civitai.com/models/789313?modelVersionId=3413429)
  - example prompt (from source, er_sde, steps 25): `ArsMovieStill, 80s Fantasy Movie Still, The image is a close-up portrait of a young woman holding a sword. She is wearing a white shirt with a blue and gold patterned ves` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e4e89fc7-984e-4e3c-b491-baf10ed2d0ed/original=true/146047711.jpeg)
- `cyberpunk-realism-moss` — trigger not stated · strength not stated · 387 dl · This should create some cyperpunk style for ANIMA · [source](https://civitai.com/models/2628831?modelVersionId=3430753)
- `1980s-horror-movies-moss` — trigger not stated · strength not stated · 313 dl · Bring out your werewolf costumes and put on the zombie makeup. Set "Thriller" on repeat. If you thou · [source](https://civitai.com/models/1592586?modelVersionId=3435489)

- Suggest ingest: [Velvet's Mythic Fantasy Styles / Flux + Pony + illustrious + ZiT + Ani](https://civitai.com/models/599757) (illustrious, 250,565 dl) — `C0lorL1nes` · strength not stated — **downloads 250565 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Popyay's Epic Fantasy Style / Pony & SDXL](https://civitai.com/models/470073) (sdxl, 55,842 dl) — trigger not stated · strength not stated — **downloads 55842 >= 2x best available (3670) in same family+category**
- Suggest ingest: [MGE Monster Girls](https://civitai.com/models/556479) (illustrious, 36,393 dl) — trigger not stated · strength not stated — **downloads 36393 >= 2x best available (5848) in same family+category**

### 10. A specific character or identity

Search `data/loras.jsonl` by the character name (`rg -i name`). Use ONE identity LoRA per person. Adults only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `holli W iIlluLoRA` — `holliw,`, `makeup, blonde hair, bangs, side locks, thick eyebrows, hair between e`, `White Dress, White leotard, see-through, white choker, thigh boots,` · strength not stated · 3,679 dl · 💋 Holli Would from Cool World 🎨 (Anima, NoobAI vPred, Illustrious) She finally exists! 🙌 I've wanted · [source](https://civitai.com/models/269635?modelVersionId=1353398)
  - example prompt (from source): `smoothmixanime,beautiful woman with blonde hair blue eyes, dancing slowly seductively looking at viewer. Neon lights glowing around her` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7726371a-2383-4f2f-943b-23d224cd2b85/original=true/128675757.mp4)
- `taimanin-rpgx-character-collection-concept-ill` — `1girl, white background, character name, character profile, multi-fram`, `((TITLE TEXT:2,"***Character Name***", ***Character Name***))` · strength not stated · 3,389 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=2182340)
- `Meiko Shiraki - Prison School - Illustrious - MeikoPS-10` — `Shiraki Meiko, grey hair, hair bun, brown eyes, huge breasts`, `thighhighs, boots. cleavage, orange jacket, school uniform, pleated sk`, `navel, cleavage, bare shoulders, yellow tank top, crop top, micro shor`, `black thighhighs, cleavage, apron, pink apron, frills, white shirt, of` · strength not stated · 2,819 dl · Vice-President of the Underground Student Council - Meiko Shiraki from Prison School · [source](https://civitai.com/models/988192?modelVersionId=1676203)
- `Coochies_Manager_-_Art_of_Jaguar_v1.0` **[HF repo only - needs adding to Graydient]** — `c00chiesManager, 1girl, white hair, short hair, grey eyes, huge breast`, `white shirt, pencil skirt, necktie, garter straps, thighhighs, side sl` · strength `1.5` (stated) · 95 dl · Diner manager from art of Jaguar. Sometimes you might need to crank up the strength to 1.5 to get re · [source](https://civitai.com/models/2018495?modelVersionId=2284476)

**SDXL**
- `shrugging-pose-woman-krea2` — trigger not stated · strength not stated · 200 dl · [source](https://civitai.com/models/2689129?modelVersionId=3367802)
  - example prompt (from source, Euler, steps 8): `<lora:training_2660648-20260921042434860:0.8> woman with bust measurement makes shrugging pose with her arms and hands. pink minidress with cutoff. brown hair, long hair,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e8e9c4bb-1c2e-4660-9c85-4b849ade1361/original=true/144146259.jpeg)
- `model-xl` — `nuruteka,tickle,` · strength not stated · 44 dl · [source](https://civitai.com/models/2979551?modelVersionId=3377414)
- `character-animagine-xl-4-0-elsa-slim-style-xl` — `(frozen movie style), 3d, cgi, 3d render, blender render, ray tracing,`, `3LS4S3, blue eyes, blonde hair, hair bun, single hair bun, eyeshadow, `, `3LS4S3, blonde hair, blue eyes, long hair, braid, single braid, long h`, `(huge breasts, huge ass, curvy figure, thick thighs, wide hips, huge r` · strength not stated · 41 dl · This version was trained using the Animagine-XL 4.0 checkpoint This version was trained with more th · [source](https://civitai.com/models/2969213?modelVersionId=3364562)

**Pony (Pony Diffusion XL)**
- `taimanin-rpgx-character-collection-concept-pony` — `taimanincc, 1 girl, Solo Focus, character profile title text, Simple b` · strength not stated · 2,837 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=618819)
  - example prompt (from source, DPM++ 2M Karras, steps 40): `score_9, score_8_up, score_7_up, source_anime, BREAK <lora:TaimaninCC_Pony_V1:0.8>taimanincc, 1 girl, Solo Focus, character profile title text, Simple background, white b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/794780c9-eac5-4122-81b7-62e7d2c8439e/original=true/18393335.jpeg)
- `kirill-from-shounen-ga-otona-ni-natta-nats-pony` — `1girl, solo, breasts, red hair, long hair, large breasts, huge breasts` · strength not stated · 412 dl · Standard Pony · [source](https://civitai.com/models/823310?modelVersionId=920656)
- `kaneda-maiko-hentai-discipline-record-of-a-pony` — `Kaneda Maiko, 1girl, brown hair, red eyes, hairclip, glasses`, `purple school uniform, two-tone jacket, necktie, pleated skirt, purple`, `black school uniform, black thighhighs`, `sleeveless shirt, sleeveless turtleneck, white shirt, cleavage cutout,` · strength not stated · 160 dl · Kaneda Maiko from Discipline: Record of a Crusade is on ANIMA / NoobAI-XL V-pred / Epsilon / IL / Po · [source](https://civitai.com/models/1852388?modelVersionId=2096360)

**Anima**
- `draco-malfoid-malfoy-redteneri-genderswap-anima` — `femdraco, 1girl, blonde hair, long hair, asymmetrical bangs, parted ha`, `hogwarts school uniform, black robe, grey sweater, collared shirt, gre` · strength not stated · 3,480 dl · Based on Redteneri's Genderswap Draco Prompts: femdraco, 1girl, pale blonde hair, long hair, asymmet · [source](https://civitai.com/models/2967285?modelVersionId=3362156)
  - example prompt (from source, ER SDE, steps 32): `masterpiece, best quality, solo, <lora:Draco_Malfoy_Genderswap_femdraco-redteneri-anima-v1-000011:1>, femdraco, 1girl, blonde hair, long hair, asymmetrical bangs, parted ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/92c7f792-9505-43b0-ba3c-6053eac218c4/original=true/143951590.jpeg)
- `taimanin-rpgx-character-collection-concept-anima` — `1girl, white background, character name, character profile, multi-fram`, `((TITLE TEXT:2,"***Character Name***", ***Character Name***))` · strength not stated · 1,535 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=3051237)
- `glory-wall-anima` — `Promts for this LoRA:`, `bdsm, glory wall, handsfree breast squeeze, immobilization, public res` · strength not stated · 1,047 dl · My telegram chanel: (https://t.me/+-OTXaB0G5F8yNDJi) My discord server: (https://discord.gg/NWpyuzsH · [source](https://civitai.com/models/2897098?modelVersionId=3275413)

**Krea2 (detailed-krea2)**
- `alt-girl-e-girl-krea2` — trigger not stated · strength not stated · 9,378 dl · Trigger word AltGirl · [source](https://civitai.com/models/2274840?modelVersionId=3198266)
  - example prompt (from source, Euler, steps 8): `AltG1rl.A striking, ultra-close-up selfie captures a young woman with intensely vibrant, electric-blue hair styled in long, straight strands that cascade around her face,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d6bd521b-ee7a-4ea0-9b4d-c8db0a0bf5dd/original=true/138751381.jpeg)
- `krea2_charactersheet_full_v1` — `Follow the prompt template I left in the workflow.` · strength not stated · 3,182 dl · TripleView is a LoRA trained on approximately 300 character sheet samples, with a strong focus on ge · [source](https://civitai.com/models/2764727?modelVersionId=3203877)
- `The YARN Collection for Krea2 - ThisYearsModel - YARN_ThisYearsModel` — trigger not stated · strength `0.2 - 1.5` (stated) · 2,312 dl · The YARN (Yet Another Realistic NSFW) Collection includes diverse styles for use with Krea 2. While  · [source](https://civitai.com/models/2880467?modelVersionId=3255885)

**MOSS (Moss Image / kromoss)**
- `luisap-nsfw-tweak-moss` — trigger not stated · strength not stated · 2,092 dl · There no exactly a important use of this lora it's just some custom selection of data that give a su · [source](https://civitai.com/models/3016687?modelVersionId=3424542)
  - example prompt (from source, Euler, steps 12): `This is a photograph of a young woman with light brown skin and long, wavy brown hair. She is positioned on a bed with white sheets in a dimly lit room. The camera angle ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/49dd2f40-804d-4e51-9cc0-aec71bc9eb3f/original=true/146570305.jpeg)
- `malfoid-genderbent-draco-malfoy-meme-chara-moss` — `M4lfoid` · strength not stated · 1,454 dl · Krea 2 and MOSS character LoRA for Malfoid (Genderbent Draco Malfoy). How to use Trigger word: M4lfo · [source](https://civitai.com/models/3021116?modelVersionId=3435645)
- `natural-skin-realism-moss` — `ral-truskin` · strength not stated · 959 dl · 💪Train your own model: https://runpod.io?ref=gased9mt 🍺 Join my discord: https://discord.com/invite/ · [source](https://civitai.com/models/3024665?modelVersionId=3434930)

- Suggest ingest: [NSFW MASTER](https://civitai.com/models/667086) (krea2, 236,423 dl) — trigger not stated · strength `0.8` (stated) — **downloads 236423 >= 2x best available (9378) in same family+category**
- Suggest ingest: [All Disney Princess XL LoRA Model from Ralph Breaks the Internet](https://civitai.com/models/212532) (illustrious, 209,305 dl) — trigger not stated · strength not stated — **downloads 209305 >= 2x best available (3679) in same family+category**
- Suggest ingest: [NiceGirls UltraReal](https://civitai.com/models/1862761) (anima, 161,022 dl) — trigger not stated · strength `0.6-0.8` (stated) — **downloads 161022 >= 2x best available (3480) in same family+category**

### 11. Lighting and atmosphere

Describe a single motivated light source in prose too.

**Illustrious / NoobAI (Illustrious-XL based)**
- `digitaldelights-impossible-downward-dog-ill` — `<Lora:DigitalDelights-impossible-downward-dog:1>, top-down bottom-up, ` · strength not stated · 1,130 dl · Name is self explanatory it's a yoga pose named dog down taking it to the extreme XD · [source](https://civitai.com/models/2143059?modelVersionId=2423989)
  - example prompt (from source, DDIM, steps 30): `masterpiece, best quality, amazing quality, perfect eyes, source_anime, 1girl, solo, <Lora:DigitalDelights-impossible-downward-dog:1>, top-down bottom-up, spread legs, lo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4a1cc040-96ed-4e28-86e1-c2ef6a7f8bc7/original=true/110929135.jpeg)
- `nephis-shadow-slave-ill` — `1girl,grey eyes,brown eyes,black eyes,grey hair,white hair,long hair,b`, `crown,tiara,armor,plate armor,black armor,breastplate,shoulder armor,p`, `very long hair,ponytail,sidelocks,armor,breastplate,shoulder armor,pau`, `crown,tiara,armor,breastplate,boobplate,shoulder armor,pauldrons,gaunt` · strength not stated · 206 dl · Nephis from Shadow Slave Appearance: 1girl,grey eyes,brown eyes,black eyes,grey hair,white hair,long · [source](https://civitai.com/models/2579289?modelVersionId=2897698)
- `jet-shadow-slave-ill` — `1girl,blue eyes,black hair,short hair,medium hair,bangs,hair between e`, `black shirt,shirt,turtleneck,turtleneck sweater,black sweater,sweater,`, `black jacket,leather jacket,jacket,open jacket,open clothes,long sleev`, `hair over one eye,black jacket,jacket,coat,open clothes,sleeves rolled` · strength not stated · 162 dl · Jet from Shadow Slave Appearance: 1girl,blue eyes,black hair,short hair,medium hair,bangs,hair betwe · [source](https://civitai.com/models/2871206?modelVersionId=3244038)

**Anima**
- `vixon-s-styles-gothic-neon-anima` — `g0thic n30n, neon lights, glowing` · strength not stated · 5,773 dl · the OG dataset now brought to anima! Hey guys! Hope you love using this new LoRA as much as I loved  · [source](https://civitai.com/models/888231?modelVersionId=3022620)
  - example prompt (from source, er_sde simple, steps 30): `absurdres, masterpiece, score_7, score_8, g0thic n30n, neon lights, glowing energy, 1girl, city, distored cyber wings, distortion, horns, halo, goth, twintails, neon text` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e50ed8ee-f6c0-4df7-a347-344a4de8b4d2/original=true/133444219.jpeg)
- `vixon-s-styles-gothic-neon-anima-2` — `cityscape`, `@g0thic, neon, glowing, neon lights, gothic` · strength not stated · 2,355 dl · the OG dataset now brought to anima! Hey guys! Hope you love using this new LoRA as much as I loved  · [source](https://civitai.com/models/888231?modelVersionId=2934771)
- `Anima_ring_light_reflection_v1.2` — `ring light reflection` · strength `0.4-1.0` (stated) · 670 dl · Anima用の「ring light reflection」のLoRAです。 ※チェックポイントによって効果が出やすかったり、出にくかったりします。更に、高速化のspectrumの設定でも相当に変動し · [source](https://civitai.com/models/2481322?modelVersionId=2789756)

**Krea2 (detailed-krea2)**
- `neon-vhs-dreams-krea2` — trigger not stated · strength `0.8–1.0` (stated) · 1,189 dl · ☕ Like my work? Feel free to support me on Ko-fi: https://ko-fi.com/granddyser Thanks! 🙏 Neon VHS Dr · [source](https://civitai.com/models/2987989?modelVersionId=3387832)
  - example prompt (from source, er_sde, steps 10): `1988 cinematic porn sex full body portrait playboy , visible vagina, a nude skinny black woman , naked aerobic standing with a black Side Ponytail hair,beautiful breasts,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/663b6e37-cea4-4845-9866-6e025f0acdfe/original=true/144851264.jpeg)
- `fleshlight_000006750` — `fleshlight` · strength not stated · 992 dl · Man masturbating with a fleshlight. Training captions include the following (but does not always wor · [source](https://civitai.com/models/2766256?modelVersionId=3113736)
- `better-light-shadow-krea2` — trigger not stated · strength not stated · 721 dl · Lived-in home interiors with bookshelves, plants and worn wood, lit through window lattices, shutter · [source](https://civitai.com/models/3039481?modelVersionId=3459297)

**MOSS (Moss Image / kromoss)**
- `amish-barn-straw-hats-suspenders-light-thr-moss` — trigger not stated · strength not stated · 187 dl · An Amish farm in Pennsylvania: weathered wide-plank barns, hay, wooden gates, gravel yards, buggies  · [source](https://civitai.com/models/3034848?modelVersionId=3448284)
  - example prompt (from source, res_multistep, steps 25): `amishbarn, Shot from the ground straight up: three Amish men aged 22, 23 and 24 in straw hats and suspenders stand and sit on the bare timber frame of a half-built barn, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0348fe4f-a8cf-48dd-a872-073af6ed041a/original=true/147786726.jpeg)
- `y2k-neon-moss` — trigger not stated · strength not stated · 103 dl · A dreamy millennium neon palette: purple and pink skies, glowing city skylines and reflections on th · [source](https://civitai.com/models/3049556?modelVersionId=3467759)

- Suggest ingest: [S1 Dramatic Lighting](https://civitai.com/models/661736) (illustrious, 63,463 dl) — `s1_dram` · strength not stated — **downloads 63463 >= 2x best available (1130) in same family+category**
- Suggest ingest: [Smooth Lighting Enhancer (NoobAI/Illustrious)](https://civitai.com/models/1204179) (illustrious, 24,842 dl) — trigger not stated · strength `0.5` (stated) — **downloads 24842 >= 2x best available (1130) in same family+category**
- Suggest ingest: [Luke's Neon Clothing and Accessories (Illustrious + Flux + Pony + 1.5 ](https://civitai.com/models/422657) (sdxl, 22,996 dl) — `glowing-neon-colour-clothing`, `blue, green, pink, orange, red, yellow, purple`, `skirt, jacket, shirt, tank top, shorts, hijab, pants, thighhighs, biki` · strength `0.5-0.7` (stated) — **no Graydient LoRA in this family+category**

### 12. Detail / aesthetic / stabilizer enhancers

Use at most one; start low and raise only if the image gets soft.

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)
  - example prompt (from source, DPM++ 2M, steps 25): `1girl, solo, alone, angel, wings, looking at the viewer, bikini, <lora:hentai_studio_quality-000013:1>, hentai_studio_quality, shiny skin, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cdb4ed61-bb72-4655-9dd9-05cbe2f37f48/original=true/69610834.jpeg)
- `sexy_details_v5` — `sexydet` · strength not stated · 5,994 dl · This is a LORA trained on handpicked images of my personal preference. It is heavily nsfw based and  · [source](https://civitai.com/models/1615374?modelVersionId=3002225)
- `zoda-nsfw-detailer-ill-2` — `zoda nsfw detailer ill 2` · strength `0.5 - 1.0` (stated) · 4,625 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2127970)

**SDXL**
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)
  - example prompt (from source, DPM++ 2M SDE, steps 43): `<lora:zoda_v1_sdxl:1> masterpiece, best quality, very aesthetic, absurdres, illustration , high resolution, sharp focus, soft lighting, dreamy, serene,  1girl, solo, long` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3feb3e6a-8ea1-43e1-90a3-d27ef4cbb2f8/original=true/95775045.jpeg)

**Anima**
- `hentai-studio-quality-illustriousxl-zimage-anima` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 12,234 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=2814440)
  - example prompt (from source, er_sde, steps 30): `hentai_studio_quality, shiny skin, 1girl, solo, alone, elf, pointy ears, looking at the viewer, bikini, beach, sand, sea, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/236c9bf2-520d-4663-8751-d9324aa5d085/original=true/125784086.jpeg)
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)
- `detailer-anima` — `detailer anima` · strength `1` (stated) · 3,359 dl · Detailer lora for Anima. v2 - Whole thing is rebalanced. Colorfix added. Antisweat added. Additional · [source](https://civitai.com/models/2767064?modelVersionId=3142679)

**Krea2 (detailed-krea2)**
- `Emotions V1` — `Detailed Emotions and Expressions` · strength not stated · 10,258 dl · LEAVE A TIP IF YOU LIKE IT, I AM OUT OF BUZZ!! What it does: - Detailed and mostly accurate emotions · [source](https://civitai.com/models/2829908?modelVersionId=3193133)
  - example prompt (from source, Euler, steps 8): `<lora:Krea2_TextFusion_Blocks_Only_v3_000007900:1> A high-quality photorealistic detailed well lit image of a handsome Caucasian man with unblemished pale skin, a short b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1a852d00-2894-41bc-857f-bdbf3afa39af/original=true/138601169.jpeg)
- `zy_BackgroundDetail_K2` — trigger not stated · strength `0.1-0.75` (stated) · 4,723 dl · ✨REFERRAL CODE: DMD9XGMN ℹ️ Model Overview This LoRA enhances the background of the image, adding mo · [source](https://civitai.com/models/633524?modelVersionId=3211112)
- `hyperdetailed-colored-pencil-krea2` — `ArsMJStyle, Colored pencil hyperdetailed realism,` · strength `1.2` (stated) · 3,656 dl · A LoRA inspired by one of my favourite styles of hyperdetailed colored pencil illustrations. This st · [source](https://civitai.com/models/1155749?modelVersionId=3113897)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
  - example prompt (from source, er_sde, steps 50): `A premium, ultra-realistic cinematic portrait designed as a professional logo named REALISM ENHANCER. Show exactly half of a beautiful Japanese woman's face in an extreme` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7af9ea0-848d-4f42-bdde-f5268ab78f19/original=true/147014892.jpeg)
- `pornmaster-moss-detail-slider-xl` — trigger not stated · strength not stated · 4,239 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -6 to +8 使用正面lora權重時增加增細節，使用負面lora權重時降低細節。 LoRA  · [source](https://civitai.com/models/3010274?modelVersionId=3416145)
- `hentai-studio-quality-illustriousxl-zimage-moss` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 2,393 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=3420914)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1373) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (5994) in same family+category**
- Suggest ingest: [Stabilizer IL/NAI/CK](https://civitai.com/models/971952) (illustrious, 161,491 dl) — trigger not stated · strength not stated — **downloads 161491 >= 2x best available (5994) in same family+category**

### 13. Turbo, distill and speed LoRAs

Only on a matching fast/turbo workflow; never stack with a full-step look at high strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)
  - example prompt (from source, DPM++ 2M, steps 25): `1girl, solo, alone, angel, wings, looking at the viewer, bikini, <lora:hentai_studio_quality-000013:1>, hentai_studio_quality, shiny skin, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cdb4ed61-bb72-4655-9dd9-05cbe2f37f48/original=true/69610834.jpeg)
- `chub-ass-hyperpigmentation-dark-crack-ill` — `hyperpigmentation, ass, ass focus, solo, from behind`, `spread ass`, `dark skin` · strength not stated · 67 dl · For the enjoyers of chub/fat bodies out in the RL: you ever get behind that big ol' thang.. spread t · [source](https://civitai.com/models/2853677?modelVersionId=3290931)

**Pony (Pony Diffusion XL)**
- `Kissing Fetish Hyperlips Kissing Concept LoRA - v1.0 - Kissing_Fetish__Hyperlips_Kissing_Concept_LoRA-000039` — `Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy,` · strength not stated · 1,183 dl · [source](https://civitai.com/models/1162938?modelVersionId=1308166)
  - example prompt (from source, Euler a, steps 30): `safe_pos, Score_9, score_8_up, score_7_up, best quality, high definition, bold outlines,   Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy, clothed femal` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/233c003d-af46-46cf-9911-a140a9dfe7a4/original=true/52828025.jpeg)

**Anima**
- `hentai-studio-quality-illustriousxl-zimage-anima` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 12,234 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=2814440)
  - example prompt (from source, er_sde, steps 30): `hentai_studio_quality, shiny skin, 1girl, solo, alone, elf, pointy ears, looking at the viewer, bikini, beach, sand, sea, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/236c9bf2-520d-4663-8751-d9324aa5d085/original=true/125784086.jpeg)
- `2-9b-turbo-remapped-anima` — trigger not stated · strength not stated · 3,853 dl · Turbo LoRA for Anima-2.9 if you're having problems with the OG lora. It's just a temporary solution  · [source](https://civitai.com/models/2857451?modelVersionId=3227488)
- `hyperdetailed-colored-pencil-anima` — `ArsMJStyle, Colored pencil hyperdetailed realism,` · strength `1.2` (stated) · 2,282 dl · A LoRA inspired by one of my favourite styles of hyperdetailed colored pencil illustrations. This st · [source](https://civitai.com/models/1155749?modelVersionId=3033029)

**Krea2 (detailed-krea2)**
- `hyperdetailed-colored-pencil-krea2` — `ArsMJStyle, Colored pencil hyperdetailed realism,` · strength `1.2` (stated) · 3,656 dl · A LoRA inspired by one of my favourite styles of hyperdetailed colored pencil illustrations. This st · [source](https://civitai.com/models/1155749?modelVersionId=3113897)
- `god-tier-tits-zimage-turbo-flux-ill-krea2` — `GodTierTits` · strength `1.0` (stated) · 2,021 dl · Krea2 added using v1.1 dataset! ZiT added using v1.1 dataset! This one can handle strengths up to th · [source](https://civitai.com/models/961829?modelVersionId=3312813)
- `cum-slider-z-imageturbo-krea2` — `a semi-translucent milky liquid flowing onto the skin, a young woman, `, `a semi-translucent milky liquid flowing onto the skin, a young woman, `, `a semi-translucent milky liquid flowing onto the skin, a young woman, ` · strength not stated · 1,877 dl · Try size: 768 x 1024 or 768 x 1280 Weights: 1.0 (semi-translucent, milky-custard and MILKYx2) Weight · [source](https://civitai.com/models/2342702?modelVersionId=3144946)

**MOSS (Moss Image / kromoss)**
- `turbo-loras-moss` — trigger not stated · strength not stated · 11,500 dl · I'll be uploading different Moss Image Turbo LoRAs I use here and crediting the original creators. I · [source](https://civitai.com/models/3006599?modelVersionId=3414934)
  - example prompt (from source, er_sde_simple, steps 4): `A real photograph shot on 35mm film from a very low angle looking up at an adult woman standing against a pitch-black night sky, framed from above her head down to her hi` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f182e7bb-6e37-43f8-8f08-fc8f0573e506/original=true/146112590.jpeg)
- `hentai-studio-quality-illustriousxl-zimage-moss` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 2,393 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=3420914)
- `pastel-pinup-palooza-r7-moss` — `kkpinup` · strength not stated · 233 dl · Pastel Pinup Palooza r7 Trigger word: kkpinup Rank / Alpha: 32 Training steps: 3,000 License: Non-co · [source](https://civitai.com/models/3023306?modelVersionId=3433174)

- Suggest ingest: [Anima Turbo LoRA](https://civitai.com/models/2560840) (anima, 82,342 dl) — trigger not stated · strength `1` (stated) — **downloads 82342 >= 2x best available (13445) in same family+category**
- Suggest ingest: [LCM-LoRA Weights - Stable Diffusion Acceleration Module](https://civitai.com/models/195519) (sdxl, 78,879 dl) — trigger not stated · strength not stated — **downloads 78879 >= 2x best available (369) in same family+category**
- Suggest ingest: [SDXL Lightning LoRAs](https://civitai.com/models/350450) (sdxl, 72,507 dl) — trigger not stated · strength not stated — **downloads 72507 >= 2x best available (369) in same family+category**

### 14. Sliders (weight, size, expression, realism)

Sliders usually accept negative strengths; the source page states the range. Age sliders are excluded from this KB.

**Illustrious / NoobAI (Illustrious-XL based)**
- `large_areolae_addift` — `large areolae` · strength not stated · 10,181 dl · Areolae size slider · [source](https://civitai.com/models/1384966?modelVersionId=1565020)
  - example prompt (from source, Euler a, steps 30): `1girl, upper body, portrait, nude, large areolae, breasts focus,  white background (masterpiece, best quality, amazing quality, very aesthetic, absurdres, highres, extrem` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fc6d4902-cb91-4662-8b42-af377cbd0cf5/original=true/65088306.jpeg)
- `long_nipples_addift_v2` — `long nipples` · strength not stated · 6,613 dl · Nipple length slider · [source](https://civitai.com/models/1384979?modelVersionId=1771546)
- `puffy_anus` — `puffy anus` · strength not stated · 6,501 dl · Large anus slider LoRA · [source](https://civitai.com/models/1550214?modelVersionId=1754090)

**SDXL**
- `thick-xl-thin-thick-body-build-slider-xl` — trigger not stated · strength not stated · 369 dl · [source](https://civitai.com/models/2893137?modelVersionId=3271132)
  - example prompt (from source): `A side-by-side two-panel full-length editorial photography reference sheet featuring the same 30-year-old woman in two views.  LEFT PANEL: straight-on frontal view, facin` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2f832f4f-1b0c-4e3e-9ebc-6d261001fdd5/original=true/147621697.mp4)
- `sheer-clothing-transparency-slider-xl` — trigger not stated · strength not stated · 140 dl · [source](https://civitai.com/models/2911617?modelVersionId=3293497)
- `oiled-oiled-skin-slider-xl` — trigger not stated · strength not stated · 120 dl · [source](https://civitai.com/models/2981260?modelVersionId=3379540)

**Pony (Pony Diffusion XL)**
- `breast-size-slider-pony` — trigger not stated · strength `1` (stated) · 273 dl · A simple concept LoRA slider designed to make image generation easier and more controllable. Recomme · [source](https://civitai.com/models/2692638?modelVersionId=3261772)
  - example prompt (from source, Euler a, steps 32): `score_9, score_8_up, score_7_up, masterpiece, best quality, absurdres, 1girl, breast focus` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/344ba137-eae7-4e4e-a9fd-0206d506b754/original=true/140682330.jpeg)
- `muscle-slider-for-women-pony` — trigger not stated · strength not stated · 77 dl · [source](https://civitai.com/models/2941832?modelVersionId=3330744)

**Anima**
- `Breasts slider - Anima - Breasts_Size_SliderAnima6` — trigger not stated · strength not stated · 13,445 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2100839?modelVersionId=2974098)
  - example prompt (from source, Euler a, steps 25): `masterpiece, 1girl, solo, looking at viewer,  straight-on, arms at sides,  blue bikini,  blonde hair, blue eyes, white background,   <lora:Breasts_Size_SliderAnima6:-2>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b57f5a72-59b7-4310-85b8-8d4a203132c0/original=true/131718491.jpeg)
- `Mature slider - Anima - MatureFemaleSliderAnima` — trigger not stated · strength not stated · 11,760 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2118055?modelVersionId=2979797)
- `Ass-Slider-Anima5` — trigger not stated · strength `2 to 2` (stated) · 7,372 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2524206?modelVersionId=3017358)

**Krea2 (detailed-krea2)**
- `penis-size-krea2` — `penis-size-krea2` · strength not stated · 21,904 dl · https://wallofthieves.com/  Krea 2 - V2 V2 is here, and it is MUCH better then V1. Improvements: - M · [source](https://civitai.com/models/2687793?modelVersionId=3154138)
  - example prompt (from source): `The image is a candid smartphone photograph in even indoor daylight, taken from below at floor level, looking up at the subjects. In the foreground, a gray floor occupies` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/9ee4e3d6-8608-4b47-bddb-6aac71bb5571/original=true/137494853.jpeg)
- `innie-labia-minora-slider-krea2` — `innie labia minora slider krea2` · strength not stated · 16,118 dl · https://wallofthieves.com/  Labia Minora Slider Works well to control the size of the labia minora,  · [source](https://civitai.com/models/2811308?modelVersionId=3170393)
- `pubic-hair-slider-body-hair-slider-zit-krea2` — `pubic hair slider body hair slider zit krea2` · strength not stated · 15,955 dl · https://wallofthieves.com/  Krea2: I have made a completely new way of making slider LoRAs, witch al · [source](https://civitai.com/models/2617090?modelVersionId=3136749)

**MOSS (Moss Image / kromoss)**
- `pornmaster-moss-realism-slider-xl` — trigger not stated · strength `2` (stated) · 5,479 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -2 to +4.5 使用正面lora權重時增加增真實感，使用負面lora權重時增加2d感。 L · [source](https://civitai.com/models/3010059?modelVersionId=3415845)
  - example prompt (from source, Euler, steps 30): `two kitsune women, POV cooperative butt job, cooperative sex assfuck. Left woman has blue hair, right woman has white hair; both have toned fitness buttocks. They are rub` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e2a89d53-e2d9-435e-92ed-484ac0fe3c44/original=true/146155409.jpeg)
- `pornmaster-moss-detail-slider-xl` — trigger not stated · strength not stated · 4,239 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -6 to +8 使用正面lora權重時增加增細節，使用負面lora權重時降低細節。 LoRA  · [source](https://civitai.com/models/3010274?modelVersionId=3416145)
- `weight-slider-moss` — trigger not stated · strength `1.0` (stated) · 3,869 dl · Weight Slider · MOSS Image A universal body-mass slider for MOSS Image: slide negative for a leaner  · [source](https://civitai.com/models/3009566?modelVersionId=3415231)

- Suggest ingest: [Penis Size Slider - Pony/Illustrious](https://civitai.com/models/465379) (illustrious, 123,867 dl) — `Futanari` · strength not stated — **downloads 123867 >= 2x best available (12347) in same family+category**
- Suggest ingest: [Breast Size Slider - Pony / Illustrious](https://civitai.com/models/481016) (illustrious, 104,242 dl) — trigger not stated · strength not stated — **downloads 104242 >= 2x best available (12347) in same family+category**
- Suggest ingest: [extremely detailed (no trigger) - sliders.ntcai.xyz](https://civitai.com/models/229213) (sdxl, 102,055 dl) — `extremely detailed` · strength not stated — **downloads 102055 >= 2x best available (369) in same family+category**

### 15. Breasts, nipples and chest anatomy

Use an anatomy LoRA only if the base model draws the area poorly.

**Illustrious / NoobAI (Illustrious-XL based)**
- `grabbing-breasts-ill` — `grabbing breasts` · strength not stated · 10,744 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=1389783)
  - example prompt (from source, Euler, steps 30): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,simple background,cute girl, eyelashes, <lora:grabbin` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/08cf9f75-8192-4a37-9ed5-37d95da7f8fa/original=true/56656488.jpeg)
- `breasts-squeeze-xl-ill` — `breasts squeeze, breasts, cleavage` · strength not stated · 3,341 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/849396?modelVersionId=961201)
- `slave-nipple-and-clitoris-chain-ill` — `((collar chained to cuffs,chained, nipple bar, clitoris piercing, nipp` · strength not stated · 2,548 dl · Like · [source](https://civitai.com/models/1965638?modelVersionId=2224896)
- `marie-breast-helper_epoch_12-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `flat-chest-xl` — `flat body` · strength `1.0` (stated) · 605 dl · Updated dataset  Tags - flatties, flat-chest, flat, chest, petite, nipples, solo, 1girl, nude, navel · [source](https://civitai.com/models/2240675?modelVersionId=3145094)
  - example prompt (from source): `Start from the exact first image: the same nude woman with long dark brown hair on all fours in doggy-style position on the white hotel bed, looking back over her left sh` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/870c9e75-b8c8-4551-852d-f83116be1a7e/original=true/137941552.mp4)
- `huge-sag-breasts-xl` — trigger not stated · strength not stated · 223 dl · [source](https://civitai.com/models/2939810?modelVersionId=3328196)

**Pony (Pony Diffusion XL)**
- `grabbing-breasts-pony` — `grabbing breasts` · strength not stated · 7,694 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=705069)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `score_9, score_8_up, score_7_up,source_anime, high res image,masterpiece,best quality,girl,cute face,clear skin,shiny hair,ultra detailed eyes,simple background, <lora:gr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5735d32b-9e04-4efe-a046-28e7c514fb81/original=true/23256428.jpeg)
- `small-saggy-breasts-pony` — trigger not stated · strength not stated · 3,700 dl · [source](https://civitai.com/models/704319?modelVersionId=947120)
- `pose_femdom_handjobfrench_kiss_nipple_tweak - v1.0 - pose_handjob_french_kiss_nipple_tweak` — `handjob_french_kiss_nipple_tweak, score_9, nipple stimulation, nipple ` · strength not stated · 3,678 dl · [source](https://civitai.com/models/905481?modelVersionId=1013259)

**Anima**
- `nipple-anima-2` — `nipples` · strength `0.6–0.8` (stated) · 7,807 dl · [MOSS] The usage is the same as Anima. Forge Neo: The effect of Adetailer is a bit weak. Turbo: It m · [source](https://civitai.com/models/2385403?modelVersionId=3036905)
  - example prompt (from source, Euler a, steps 28): `masterpiece, best quality, score_7, highres, absurdres, explicit, 1girl, solo, perky breasts, natural breasts, breasts out, breast focus, nipples, Unamused, upper body, <` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/698868c5-aadc-4758-87c2-eb47919bbe22/original=true/133892044.jpeg)
- `grabbing-breasts-anima` — `grabbing breasts` · strength not stated · 3,829 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=2933804)
- `breast-implants-round-breasts-anima` — `breast implants, round breasts` · strength `0.8 - 1.0` (stated) · 2,786 dl · This Lora will give your beautiful Waifus breast implants, which gives the tits a sexy spherical sha · [source](https://civitai.com/models/1429234?modelVersionId=2984102)

**Krea2 (detailed-krea2)**
- `ski-slope-breasts-mh3-ani-kr2-zit-f1d-pny-krea2` — `SteepSlopeTiddies` · strength `1.10` (stated) · 6,701 dl · Moss XXL / MH3 XXL / Ani XXL / Krea2 XXL / ZiT XXL / ZiT 1.2 / F1D XXL / F1D 1.2 / PNY 1.2 / ILL 1.2 · [source](https://civitai.com/models/942483?modelVersionId=3112303)
  - example prompt (from source): `Woman poses nude for a high end men's magazine` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3f0b683a-d67a-4417-af36-4834ade42fc4/original=true/136167194.mp4)
- `Breast Size Shape Megapack Krea2 Update - Krea2 - Breast_Size_Shape_fp16` — `small breasts`, `large breasts`, `massive breasts`, `massive saggy breasts` · strength not stated · 4,077 dl · Breast Size & Shape Megapack  Silicone Implants Large Natural Breasts Saggy Breasts Small Breasts Te · [source](https://civitai.com/models/597667?modelVersionId=3248883)
- `fake-breasts-bimbo-fake-tits-krea2` — `fake breasts` · strength `0.4-0.6` (stated) · 4,000 dl · Trigger phrase is: "fake breasts", or "huge fake breasts". Anima: Dataset is IRL photos, recommend h · [source](https://civitai.com/models/2182514?modelVersionId=3075496)

**MOSS (Moss Image / kromoss)**
- `tiny-tits-small-breasts-v0297-krea2` — `tyneetitpn` · strength `1.15` (stated) · 10,662 dl · MOSS Small breasts puffy nipples Best strength for me was around 1.15.  Trigger: tyneetitspn Some sa · [source](https://civitai.com/models/2733121?modelVersionId=3440297)
- `moss-natural-breasts-xl` — trigger not stated · strength `0.8–1.0` (stated) · 2,420 dl · Natural Breasts — for MOSS Image A small, focused LoRA for natural breast shape on MOSS-Image. It do · [source](https://civitai.com/models/3010783?modelVersionId=3416833)
- `massive-realistic-breasts-macromastia-moss` — trigger not stated · strength not stated · 1,228 dl · ⚠️ An Important Personal Note & The Reality of Future Models I want to be completely transparent wit · [source](https://civitai.com/models/3033173?modelVersionId=3446172)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [Sagging Breasts](https://civitai.com/models/139131) (illustrious, 89,056 dl) — `sagging breasts`, `breasts apart` · strength `1.0` (stated) — **downloads 89056 >= 2x best available (10931) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (11673) in same family+category**

### 16. Penis, scrotum and futa anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `penis-size-difference-ill` — `PSDER, penis size difference, penis, (2boys:1.7), 1girl,  small penis,` · strength `0.6-1.0` (stated) · 8,863 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=1245271)
  - example prompt (from source, Euler a, steps 20): `masterpiece,best quality, (flat style, one piece style, anime style, anime screencap, crossover, artist:kittew:0.5,artist:ratatat74:0.3), PSDER, penis size difference, pe` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/6ba92e14-f6b0-4b17-b42e-4cdf5afb6ec9/original=true/49763219.jpeg)
- `Small Penis - Feminization - SPH - Illustrious - cute_v1.5` — `cute_penis` · strength not stated · 7,251 dl · Twice the gurls and even daintier bits! I've updated the first concept model I created. I incorporat · [source](https://civitai.com/models/1514972?modelVersionId=1738881)
- `Futa_on_male-000055` — `futa on male, futa with male, 1girl, 1boy, futanari,`, `sex, sex from behind,`, `lying,` · strength not stated · 5,526 dl · The most popular and requested LoRA. Comment or message me to let me know what to create next. I mak · [source](https://civitai.com/models/891832?modelVersionId=2066157)

**SDXL**
- `Futanari Pegging Male Hassaku XL - v1.0 - Futa_Pegging_Male_v1` — `Futa_Pegging_Male`, `futa on male, futa pegging male, anal sex,` · strength not stated · 2,769 dl · [source](https://civitai.com/models/790941?modelVersionId=884496)
  - example prompt (from source, Euler a, steps 40): `score_9, score_8_up, score_9, score_8, 1futanari, 1boy, (Futa_Pegging_Male:1.5), anime style, futa on male, futa pegging male, anal sex, hentai, girl with red hair, boy w` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f72df470-4ffe-435f-96e8-935eef51c769/original=true/30992240.jpeg)

**Pony (Pony Diffusion XL)**
- `size-difference-absurd-stomach-bulge-xl-pony` — trigger not stated · strength not stated · 2,890 dl · [source](https://civitai.com/models/798170?modelVersionId=892550)
  - example prompt (from source, Euler, steps 20): `score_9,score_8_up,realistic,1girl,giant man,size difference,slender,realistic,vaginal penetration, penetration,absurd stomach bulge,hanging on penis,cute,looks at viewer` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fd519aeb-c548-4478-96e2-6a503f00b3b4/original=true/31374968.jpeg)
- `long-erect-clitoris-large-clit-pony` — `XLclit`, `Erect_clitoris` · strength not stated · 2,792 dl · [source](https://civitai.com/models/686987?modelVersionId=768861)
- `penis-size-difference-concept-pony` — `Penis Size Difference`, `large insertion`, `sub with tiny penis`, `dom with huge penis` · strength not stated · 2,197 dl · a lora designed to hopefully have the dominant male have a large penis, and the sub have a small pen · [source](https://civitai.com/models/809516?modelVersionId=905253)

**Anima**
- `concept-wet-penis-saliva-pussy-juice-anal-anima` — `pussy juice on penis`, `saliva on penis`, `anal fluid on penis` · strength not stated · 2,764 dl · This is an experimental initial release. This LoRA focuses specifically on coating the penis with va · [source](https://civitai.com/models/2627734?modelVersionId=3222610)
  - example prompt (from source, er_sde, steps 12): `bar censor, censored,  solo focus, hetero,  wet penis, saliva on penis, after fellatio, veiny penis, (penis on head:1.2), penis on cheek, drooling,  open mouth, saliva, s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0b28a388-4726-4da0-bfeb-20a4924f3030/original=true/139515743.jpeg)
- `penis-size-difference-anima` — `penis size difference` · strength `0.6-1.0` (stated) · 2,479 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=3027209)
- `futa-foreskin-taker-pov-anima` — `fftaker` · strength `0.5-1` (stated) · 1,911 dl · Futa Taker POV: a shot in which the viewer is implied to be the subject of the a futa's penis. Mostl · [source](https://civitai.com/models/138423?modelVersionId=3113463)

**Krea2 (detailed-krea2)**
- `femboy-shemale-flaccid-or-small-penis-krea2` — `femboy shemale flaccid or small penis krea2` · strength `1.0` (stated) · 5,728 dl · v Krea 2 Krea version 2 works without any bypass LoRAs or similar censorship modifications. It uses  · [source](https://civitai.com/models/2054525?modelVersionId=3096065)
  - example prompt (from source, Euler, steps 10): `Close-up photo of tiny flaccid penis and scrotum, visible from front, of young pretty woman who wearing pink bikini, her pink thong are moved aside by her hand. Ocean bea` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/59fb4e2b-4566-42b0-9d7e-076b33a042c9/original=true/135665457.jpeg)
- `krea2_equine_penis_0807` — `equine penis, urethral`, `canine penis, penis tip` · strength not stated · 4,131 dl · Primary training objective: equine penis. To avoid severe overfitting in other areas—such as acciden · [source](https://civitai.com/models/2843146?modelVersionId=3209760)
- `krea2 sex 淫模 - BD - krea2_big_dick_epoch_10` — `krea2dic, big dick, 1girl, sex, penis, hetero, blonde hair, 1boy, brea` · strength `0.6–0.7` (stated) · 3,324 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3230990)

**MOSS (Moss Image / kromoss)**
- `flaccid-vtx-flaccid-uncut-penis-moss` — `flaccid penis` · strength not stated · 1,143 dl · Not sure if I like MOSS over Krea 2 for photorealism, but it's really fast and can do a wider variet · [source](https://civitai.com/models/3008280?modelVersionId=3413532)
  - example prompt (from source, Euler, steps 16): `A high-quality studio photograph of a handsome Caucasian man in his late twenties with a fit, athletic, well-developed physique. He stands centered in the frame against a` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5a3cb833-7154-4870-959d-48f591bf6c57/original=true/146042480.jpeg)
- `f-ing-dick-moss` — trigger not stated · strength not stated · 1,058 dl · Note: You can significantly improve the quality by using a BBOX (Bounding Box) to show the model whe · [source](https://civitai.com/models/3014843?modelVersionId=3422079)
- `prepuce-foreskin-moss` — `pr3puc3`, `prepuce foreskin on tip of penis` · strength not stated · 649 dl · first MOSS lora, still getting the hang of it. If you like my work, please consider purchasing early · [source](https://civitai.com/models/3022195?modelVersionId=3431777)

- Suggest ingest: [Nipples XL](https://civitai.com/models/171014) (sdxl, 73,706 dl) — `oval nipples`, `puffy nipples`, `dark nipples`, `ghost nipples` · strength not stated — **downloads 73706 >= 2x best available (1554) in same family+category**
- Suggest ingest: [Balls Deep / Deep(er) Penetration](https://civitai.com/models/550870) (illustrious, 70,061 dl) — `deep penetration` · strength not stated — **downloads 70061 >= 2x best available (11673) in same family+category**
- Suggest ingest: [[PonyXL/ILXL] Pull out Penis Cumtrail](https://civitai.com/models/467896) (illustrious, 40,651 dl) — `cum string, cumtrail, solo focus`, `cumtrail vagina to penis, , after sex, pulling out penis, cum on penis`, `cumtrail mouth to penis, , pulling out penis, after oral, after ferrat`, `cumtrail breast to penis, , pulling out penis, after paizuri, cum on b` · strength not stated — **downloads 40651 >= 2x best available (10931) in same family+category**

### 17. Vulva, vagina and anus anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `pussy-juice-ill` — `pussy juice` · strength not stated · 10,931 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=1135306)
  - example prompt (from source, Euler, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,24K,illustration,shiny hair,clear skin,beautiful eyes,cute girl,kawaii,eyelashes <lora:pussy juice_illustrious_V1.` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1bc823f5-78ff-4601-868f-c898a8a3eea9/original=true/68544794.jpeg)
- `hentai-pussy-inspection-2shot-il-2-ill` — `hpi2, 1 girl, full body, cowboy shot, Clothed girl and nude girl, Cove` · strength not stated · 10,634 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=2113370)
- `5luttyPu55y_IL_v2` — `5lutty pussy, long labia, dark labia, urethra,`, `pink nipples,` · strength `1` (stated) · 9,655 dl · グロマンLoRA Anima版を追加しました。まだ学習、出力、動作確認のノウハウがなくて手探りの状態で、画風によっては安定しない感じがします。 Anima A dark and meaty labia · [source](https://civitai.com/models/1155055?modelVersionId=1331578)
- `Marie-PussyPlayground_2_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `Marie-PussyPlayground_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `Hentai_Pussy_inspection2_SDXL` — `Hentai_Pussy_inspection2`, `(wearing clothes, clothes cover body:1.5)`, `solo, multiple views, close-up, looking at viewer, cowboy shot, nude, ` · strength not stated · 1,554 dl · [source](https://civitai.com/models/1662102?modelVersionId=1881250)
  - example prompt (from source, Euler a, steps 25): `1girl, shiranui mai, fatal fury, large breasts, (wearing clothes, clothes cover breasts, clothes cover waist:1.5),  [artist:sakimichan/artist:v-mag/artist:youshu ohepe/ar` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/10a8c1ac-d4c7-4242-9b21-984e4eeba4f6/original=true/81895005.jpeg)
- `step-sis-backside-anal-fingering-simulator-xl` — `finger_ass` · strength not stated · 260 dl · [source](https://civitai.com/models/3009204?modelVersionId=3414763)
- `step-sis-ass-spread-simulator-xl` — `ass_spread` · strength `0.80–0.95` (stated) · 141 dl · High-fidelity interaction & pose LoRA for SDXL and Illustrious XL. Trained using a precise UNet-only · [source](https://civitai.com/models/3012318?modelVersionId=3418834)

**Pony (Pony Diffusion XL)**
- `hentai-pussy-inspection-2shot-il-2-pony` — `solo, multiple views, close-up, looking at viewer, cowboy shot, nude, `, `(Multiple layers),solo, full body, cowboy shot, standing, sweat, oily ` · strength not stated · 11,319 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=639693)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/755c54b3-86c3-4195-9ee7-da89000171ee/original=true/33529329.jpeg)
- `pussy-juice-pony` — `pussy juice` · strength not stated · 9,912 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=601324)
- `hentai-pussy-inspection-il-xl-cosine-pony` — `(Multiple layers), multiple views, simple bacground, Character profile` · strength not stated · 8,147 dl · Width:832 Height:1216 is best SAMPLE <LORA>Common prompts-- ---------------------------------------- · [source](https://civitai.com/models/570883?modelVersionId=636338)
- `Marie-pussyplayground_v3_epoch_12-pony` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `mcb-pussy-helper_epoch_10-pony` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Anima**
- `pussy-juice-anima` — `pussy juice` · strength not stated · 4,376 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=2981405)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.1:0.6>,glossy hair,perfect eyes,real skin,  <lora:pussy juice_anima_V1.0:1> pussy ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0b5ada01-ae4e-4841-8ff6-8c8a8004d551/original=true/131990152.jpeg)
- `hentai-pussy-inspection-2shot-il-2-anima` — `hpi2, 1 girl, full body, cowboy shot, Clothed girl and nude girl, Cove` · strength not stated · 4,203 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=3055825)
- `vaginal_gaping_cervix-v2-ana-concept-soralz` — `<lora:vaginal_gaping_cervix-v2-ana-concept-soralz:1>, vaginal gaping, ` · strength `0.6` (stated) · 3,593 dl · Commissions are open if you have character wish to be made, please check my profile for details. Not · [source](https://civitai.com/models/2632973?modelVersionId=2956220)

**Krea2 (detailed-krea2)**
- `krea2filterbypass-krea2` — trigger not stated · strength `1.0` (stated) · 32,481 dl · Since people can't read. Strength can be used at 1.0 all the way up to 40000.0 If you use poorly qua · [source](https://civitai.com/models/2728234?modelVersionId=3067151)
  - example prompt (from source, steps 8): `A close-up, low-angle shot captures a solo female with short, vibrant pink hair and glowing pink eyes looking directly at the viewer. She has slightly pointy ears adorned` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/802f4756-0f7c-4df8-b4df-697e29f91d7f/original=true/134771503.jpeg)
- `anal-helper-krea2` — `anal-helper-krea2` · strength not stated · 17,728 dl · https://wallofthieves.com/  Anal Helper LoRA (Not a slider) I have found it frustrating that most Lo · [source](https://civitai.com/models/2759414?modelVersionId=3105253)
- `better-pussy-krea2-3` — `better pussy krea2 3` · strength `0.7-0.95` (stated) · 11,375 dl · Lora strength: 0.7-0.95 V4.2.1 increases the proportion of hairless pussy images in the dataset, mak · [source](https://civitai.com/models/2729157?modelVersionId=3111211)
- `marie-pussyassist-krea2-v1e12` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**MOSS (Moss Image / kromoss)**
- `anal-assistant-for-moss` — trigger not stated · strength not stated · 1,617 dl · This should aid with all things Anal · [source](https://civitai.com/models/3037721?modelVersionId=3452026)
  - example prompt (from source, Euler, steps 12): `Ultra realistic candid raw photo.  anal sex, anal penetration, from behind, top-down and bottom up, large penis,  image shows a girl with blonde hair,  shot from a dynami` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/97a105f6-0812-4500-8b50-1cc599e82dd2/original=true/147984538.jpeg)
- `better-pussy-moss` — trigger not stated · strength not stated · 1,113 dl · Moss knows anatomy pretty well out of the box but i find it likes to make multiple labia lips, or st · [source](https://civitai.com/models/3039119?modelVersionId=3453860)
- `door-peephole-view-fisheye-visitor-at-the-moss` — trigger not stated · strength not stated · 729 dl · Looking out through an electronic door peephole: a high fisheye angle with the visitor in the center · [source](https://civitai.com/models/3019310?modelVersionId=3427972)

- Suggest ingest: [Labiaplasty Innie Pussy Adjuster [KR2 K9B ZImage SDXL Qwen Chroma SD1]](https://civitai.com/models/112299) (krea2, 176,773 dl) — trigger not stated · strength not stated — **downloads 176773 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Lily](https://civitai.com/models/86788) (sdxl, 99,961 dl) — `pussy_front`, `pussy_rear`, `toys_front`, `toys_rear` · strength not stated — **downloads 99961 >= 2x best available (1554) in same family+category**
- Suggest ingest: [Real Pussy - Peach](https://civitai.com/models/99174) (sdxl, 87,846 dl) — `pussy_scale1`, `pussy_scale2`, `pussy_scale3` · strength not stated — **downloads 87846 >= 2x best available (1554) in same family+category**

### 18. Hands, feet, face and small anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `Facesitting Sitting on Face Footjob Femdom Pony Illustrious - Illustrious - FSFJ` — `Femdom Facesitting, sitting on person, sitting on face, 1girl, 1boy, h`, `crossed legs, stepping on penis,`, `footjob,`, `two-footed footjob,` · strength not stated · 3,460 dl · Femdom Concept: Female face sitting upright with the option of foot job included.  Can add "Chair",  · [source](https://civitai.com/models/626710?modelVersionId=1398509)
  - example prompt (from source, Euler a, steps 30): `safe_pos, masterpiece, best quality, amazing quality, very aesthetic, absurdres, scenery, volumetric lighting, background, colorful, dark, foreshortening, Femdom Facesitt` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2c0b4dbf-ba88-4ae8-ad76-29d0d11d7b63/original=true/57071381.jpeg)
- `FemdomFoot lickingboy lyingamazon positionreverse insertion into pussy - v2.0 - foot_licking_amazon-000001` — `(foot licking:1.8)`, `(cock in pussy:1.5),(Amazon position:1.1)`, `full-body shot including visible female feet,` · strength not stated · 2,608 dl · V1.5 Prompt:  (cock in pussy:2.2), penis in pussy, 1girl ,dominant female,assertive female,hands fir · [source](https://civitai.com/models/1749598?modelVersionId=2055175)
- `clitoris-slip-ill` — `clitoris slip, lowleg panties`, `clitoris slip, lowleg bikini` · strength `1` (stated) · 2,421 dl · strength=1 Distillation to make the 'clitoris slip' more stable · [source](https://civitai.com/models/1176254?modelVersionId=1323523)

**SDXL**
- `solarum-lattice-touched-xl-glowing-teal-la-xl` — `jlattice_touched` · strength not stated · 19 dl · Retrained from scratch on a new dataset (147 DreamUp images, my own prompts). UNet-only training, ep · [source](https://civitai.com/models/2855521?modelVersionId=3421397)
  - example prompt (from source, Euler a, steps 24): `Macro study of a Dinka woman's dark brown eye, thin glowing neon-teal ring inside the iris around the pupil, calm steady gaze, faint spore-dust drifting past lashes, soft` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/37ac2b61-847b-48ce-856b-72f9f3466eb3/original=true/146413187.jpeg)

**Pony (Pony Diffusion XL)**
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
  - example prompt (from source, Euler a, steps 30): `Source anime, anime colored, score_9, score_8_up, score_7_up, score_6_up, mother and sons, angry  teacher, strict teacher, classroom, black tshirt, black leggings, red lo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/90b41b3a-24d6-46f0-9b37-c45eff2d40e8/original=true/30609476.jpeg)
- `Kissing Fetish Hyperlips Kissing Concept LoRA - v1.0 - Kissing_Fetish__Hyperlips_Kissing_Concept_LoRA-000039` — `Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy,` · strength not stated · 1,183 dl · [source](https://civitai.com/models/1162938?modelVersionId=1308166)
- `Putting You in Your Place Femdom Foot to Chest Pose PONY - v1.0 - hud_f3mdom_k1ck_XLP` — `1girl, hud_f3mdom_k1ck, femdom, leg up, high heels, kicking, 1boy, nud`, `view from side` · strength not stated · 1,006 dl · [source](https://civitai.com/models/704816?modelVersionId=788374)
- `MCB_hands_pony_epoch_10` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Anima**
- `_feet_epoch_10` — `@feet, feet, toes, soles, tonails, whatever else` · strength not stated · 2,756 dl · Enjoy and share results! Suggestion Box (Higher chance of getting what you want if you attach an ima · [source](https://civitai.com/models/1293552?modelVersionId=3103124)
  - example prompt (from source, Euler a, steps 24): `@feet,  1girl, anklet, barefoot, close-up, feet, foot focus  jewelry, nail polish, out of frame, purple nails, soles, solo, tattoo, toe ring, toenail polish, toenails, to` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b6aac67f-2d85-4bbe-bc1c-67755da1cfb8/original=true/135874709.jpeg)
- `basic-hands-improvement-anima` — `perfect hands` · strength `0.7` (stated) · 2,640 dl · This is my personal (barely working) attempt to improve the hands and fingers, so please don't expec · [source](https://civitai.com/models/2783311?modelVersionId=3134960)
- `disgusted_face_anima_goofy` — `disgusted face,shaded face` · strength not stated · 2,284 dl · Private commission on fiverr  I officially host and maintain all my models on Tensor.art I was hopin · [source](https://civitai.com/models/196908?modelVersionId=3196945)

**Krea2 (detailed-krea2)**
- `krea2 sex 淫模 - FJ - krea2 footjob` — `krea2fotjob, footjob, 1girl, fishnets, feet, hetero, penis, 1boy, pant` · strength `0.6–0.7` (stated) · 3,299 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3187149)
  - example prompt (from source, Euler, steps 8): `krea2fotjob, footjob, nude, realistic, nipples, feet, pussy, barefoot, pubic hair, brown hair, censored, toes, on back, navel, lying, 1girl, female pubic hair, completely` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a924e1cd-74c6-4d13-a8dc-b4d7b7e14f4f/original=true/138410652.jpeg)
- `Footjob POV Frontview Flux 2 klein 9b - Krea2 - k_footjob` — `f00t, footjob, penis between feet, male pov,` · strength `0.9` (stated) · 2,257 dl · Huggingface for lost Loras: https://huggingface.co/quadratrund Thanks to @AnubisParoh for setting up · [source](https://civitai.com/models/2512932?modelVersionId=3251688)
- `hands-on-experience-solo-nsfw-krea2` — `kavrena2` · strength `0.7` (stated) · 1,818 dl · Hands-On Experience Sometimes a model just needs a little more… practical experience. Hands-On Exper · [source](https://civitai.com/models/2980096?modelVersionId=3378125)

**MOSS (Moss Image / kromoss)**
- `door-peephole-view-fisheye-visitor-at-the-moss` — trigger not stated · strength not stated · 729 dl · Looking out through an electronic door peephole: a high fisheye angle with the visitor in the center · [source](https://civitai.com/models/3019310?modelVersionId=3427972)
  - example prompt (from source, Euler, steps 50): `doorpeepholeviewconcept, The visitor is a white woman aged 22 with red hair in a messy bun, standing in a dim apartment corridor holding a fluffy bathrobe wide open with ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5fe38743-a10e-4c84-9d93-e714fee4be4b/original=true/146740141.jpeg)
- `feet-moss` — trigger not stated · strength `0.7` (stated) · 543 dl · A bare-feet concept LoRA for MOSS-Image. Trigger word: feet Trained on 300 real studio photographs ( · [source](https://civitai.com/models/3022702?modelVersionId=3432393)
- `american-dorm-college-double-room-cctv-eye-moss` — trigger not stated · strength `0.6` (stated) · 506 dl · A realistic American university double dorm room: a single bed with a wooden frame sits against each · [source](https://civitai.com/models/3022560?modelVersionId=3432222)

- Suggest ingest: [Hands XL + SD 1.5 + F1D + Pony + Illustrious + zit + ZIB](https://civitai.com/models/200255) (illustrious, 314,114 dl) — `detailed` · strength not stated — **downloads 314114 >= 2x best available (10931) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1373) in same family+category**
- Suggest ingest: [Detailed Perfection style (Hands + Feet + Face + Body + All in one) XL](https://civitai.com/models/411088) (illustrious, 139,148 dl) — `detailed` · strength not stated — **downloads 139148 >= 2x best available (5994) in same family+category**

### 19. Body type, muscle, curves, tan lines

**Illustrious / NoobAI (Illustrious-XL based)**
- `small-but-hung-xl` — `small but hung`, `size difference` · strength not stated · 2,869 dl · v1.1 More refined (i hope), test it out! That said, use whichever fits for u and give feedback if ab · [source](https://civitai.com/models/1991612?modelVersionId=2263536)
  - example prompt (from source, Euler a, steps 30): `masterpiece, best quality, absurdres, highres, newest, very aesthetic, very detailed, cinematic,  small but hung, 1girl, 1boy, minamoto no raikou (fate), hetero, grabbing` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fe950052-73c1-42d4-90d4-780dc757548b/original=true/103109597.jpeg)
- `bottom_up_spread_epoch_10` — `bottom_up_spread, 1girl, solo,  lying,  looking at viewer, on back, sp`, `hip lift,` · strength not stated · 1,359 dl · lora for a sexy posing. A girl spreads legs and lifts her hip. · [source](https://civitai.com/models/2631708?modelVersionId=2954783)
- `thigh-sex-concept-ill` — `thigh sex concept ill` · strength `1.0` (stated) · 1,040 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/1449748?modelVersionId=3274843)

**Pony (Pony Diffusion XL)**
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
  - example prompt (from source, Euler a, steps 30): `Source anime, anime colored, score_9, score_8_up, score_7_up, score_6_up, mother and sons, angry  teacher, strict teacher, classroom, black tshirt, black leggings, red lo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/90b41b3a-24d6-46f0-9b37-c45eff2d40e8/original=true/30609476.jpeg)

**Anima**
- `Concept Body bridge - v0.0.0 - body_bridge_v0.0.0_0600_cosine-0025` — `body bridge`, `on back`, `arm support`, `tiptoes` · strength not stated · 1,741 dl · I found it difficult to achieve a pose where the body bends into a bridge-like shape, curving like a · [source](https://civitai.com/models/2875579?modelVersionId=3249483)
  - example prompt (from source, er_sde, steps 12): `bar censor,  solo, full body, from side,  1girl, hatsune miku, huge breasts, body bridge, arm support, on back, tiptoes,  nervous smile, no panties, spread legs,    highr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ff3e4a70-981d-4425-a937-d1cb4f958140/original=true/140294954.jpeg)
- `body-writing-erotic-anima` — `body writing,` · strength `1` (stated) · 1,571 dl · Recommended weight： 1 Trigger prompts ： body writing,  Tried making an anima version with a "Body Wr · [source](https://civitai.com/models/2951684?modelVersionId=3343038)
- `thick_nipples_260210` — `thick nipples, hyper nipples, wide nipples, large areolae, hyper areol` · strength not stated · 1,039 dl · ※AI Translation I don't really understand Anima or how to create Lora for Anima. For now, I trained  · [source](https://civitai.com/models/2383224?modelVersionId=2679973)

**Krea2 (detailed-krea2)**
- `Krea2 milf body - V1 - milfbodyhms_v1` — `(fupa:1.2)`, `rounded pubic mound`, `saggy buttocks`, `rounded lower abdomen` · strength not stated · 4,091 dl · try the following: (fupa:1.2) - increase strength for a more distended lower abdomen. I've come to l · [source](https://civitai.com/models/2784421?modelVersionId=3137009)
  - example prompt (from source, Euler, steps 8): `three side-by-side photos of the exact same nude european woman, showing a front view, a side view and a back view. neutral posture, warm smile. plain background.  slim w` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fb94c6dd-3efe-48d4-b14b-b96c867746c7/original=true/137260382.jpeg)
- `z-female-body-retouched-krea2` — trigger not stated · strength `2.0` (stated) · 2,990 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3186931)
- `Back_Body_Bridge_Krea2` — `backbodybridge` · strength not stated · 1,610 dl · Lora created to render a specific pose, subject on back with a very arched back. Example prompt (Pon · [source](https://civitai.com/models/2114472?modelVersionId=3200446)

**MOSS (Moss Image / kromoss)**
- `z-female-body-retouched-xl` — trigger not stated · strength `0.6-1.0` (stated) · 1,346 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3413047)
  - example prompt (from source, res_multistep, steps 30): `a naked yamamura_sadako cosplayer, smile, walking, huge breasts, outdoors, wild, overexposured skin, at night, candid amateur shot, blurry foreground` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0bd4af23-f52f-49f7-8c09-c17f30bb86b3/original=true/146021224.jpeg)
- `wide-hips-thigh-gap-moss` — `wide pelvis`, `thigh gap` · strength not stated · 309 dl · Prompt "wide hips" has become conjoined with concepts like big ass and thick thighs. This is an atte · [source](https://civitai.com/models/3041324?modelVersionId=3456891)
- `prego-pregnant-body-for-moss` — trigger not stated · strength `.5-1.5` (stated) · 261 dl · Assists with pregnant tits, belly, and glowing skin. Use keyword pregnant. Use at strength .5-1.5. I · [source](https://civitai.com/models/3045940?modelVersionId=3462803)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [BFS - Best Face Swap](https://civitai.com/models/2027766) (krea2, 110,251 dl) — `body_swap: replace the person with the reference person.` · strength not stated — **downloads 110251 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Cameltoe](https://civitai.com/models/137423) (sdxl, 63,670 dl) — `cameltoe_body`, `cameltoe_hips`, `cameltoe_pussy` · strength not stated — **downloads 63670 >= 2x best available (1554) in same family+category**

### 20. Lingerie, latex, bodysuits, corsets

**Illustrious / NoobAI (Illustrious-XL based)**
- `cat-lingerie-ill` — trigger not stated · strength `0.7` (stated) · 3,088 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2711788)
  - example prompt (from source, DPM++ 2M, steps 25): `masterpiece,amazing quality,newest,absurdres,highres,detailed face,kawaii,cute,perfect eyes,<lora:rich colors enhance_illustrious_V1.0:0.6>,rce,depth of field,simple back` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bcbd35ae-25d0-4f99-ba18-6c0302bd84d6/original=true/121974471.jpeg)
- `thin-bodysuit-ill` — `th1nbodysu1t`, `highleg` · strength `0.8` (stated) · 2,149 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=1417556)
- `peppan2_santopati` — trigger not stated · strength not stated · 1,983 dl · You can look at the sample images above for the example prompts. "peppan" trigger word is optional R · [source](https://civitai.com/models/1240750?modelVersionId=2920404)

**SDXL**
- `thong-upskirt-xl` — trigger not stated · strength not stated · 178 dl · [source](https://civitai.com/models/2898091?modelVersionId=3276640)
  - example prompt (from source, DPM++ SDE, steps 39): `<lora:training_212156-20260829072242405:1>a photograph of a woman in a miniskirt, skirt, (thong:1.3), indoor, hi res, highly detailed, best quality, photorealistic, reali` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1cda698f-f904-4d0b-9c2f-1303592699fd/original=true/141267396.jpeg)
- `bullet-bra-xl` — trigger not stated · strength not stated · 53 dl · [source](https://civitai.com/models/2903504?modelVersionId=3283348)
- `black-latex-male-xl` — trigger not stated · strength not stated · 27 dl · ### 🖤 What's new in v1.0: - Full SDXL 1.0 Architecture: Upgraded to 64-dim (Rank 64 / Alpha 32) high · [source](https://civitai.com/models/2725020?modelVersionId=3424391)

**Pony (Pony Diffusion XL)**
- `cat-lingerie-pony` — `cat lingerie,bra,panties,neck bell` · strength `0.7` (stated) · 1,658 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=1740093)
  - example prompt (from source, DPM++ 2M, steps 40): `score_9,score_8_up,score_7_up,source_anime,high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,kawaii,<lora:cat lingerie_pony_V1.0:` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e26956e4-325d-4ca7-9568-beab9faf06b5/original=true/73907285.jpeg)
- `80s-aerobics-high-leg-leotard-pony` — `Thong_leotard, skintight, leg warmers` · strength not stated · 731 dl · [source](https://civitai.com/models/964808?modelVersionId=1080241)
- `latex-women-submissive-dominatrix-pony` — trigger not stated · strength not stated · 118 dl · [source](https://civitai.com/models/2995215?modelVersionId=3396904)

**Anima**
- `cat-lingerie-anima` — `cat lingerie`, `cat ear legwear` · strength `0.7` (stated) · 1,777 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2939201)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.0:0.3>,glossy hair,perfect eyes,real skin, <lora:cat lingerie_anima_V1.0:1> cat li` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3dce4dec-6ab8-4c2b-9c82-2dbed273a677/original=true/130473481.jpeg)
- `jav-race-queen-with-highleg-leotard-anima` — `jav fstu 033 032,  1girl, solo,  race queen, clothes writing, highleg `, `holding parasol,  Holding umbrella,`, `2boys, multiple boys,  taking picture, recording, camera boys, boys ar`, `2boys, mmf threesome, hetero, fingering, grabbing, group sex, leotard ` · strength `0.85 - 1` (stated) · 728 dl · This LORA was created to see if it could learn JAV and produce hentai anime. 📋Source material for tr · [source](https://civitai.com/models/2861588?modelVersionId=3232553)
- `mobbunny-latex-nun-bodysuit-anima` — `nun, latex bodysuit, juliet sleeves, shiny clothes` · strength not stated · 597 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/1785994?modelVersionId=3387289)

**Krea2 (detailed-krea2)**
- `thin-bodysuit-krea2` — `th1nbodysu1t` · strength `0.8` (stated) · 2,025 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=3154439)
  - example prompt (from source, Euler, steps 8): `A close-up glamour photography photo of a beautiful, slim woman with striking cheekbones, expressive brown eyes, elegant eyeliner, long eyelashes, and pink lips. She has ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d60a3126-0371-44c5-9232-b0b22cc77651/original=true/137498130.jpeg)
- `thong-madness-krea2` — trigger not stated · strength not stated · 1,988 dl · Most krea2 models i use struggle to make tiny or string panties or thongs so i made this model to tr · [source](https://civitai.com/models/2995179?modelVersionId=3396864)
- `joschek-s-shiny-latex-bodysuits-for-krea2` — `latex bodysuit` · strength not stated · 1,739 dl · works. · [source](https://civitai.com/models/2729323?modelVersionId=3068160)

**MOSS (Moss Image / kromoss)**
- `micro-bikini-thong-pull-for-moss` — trigger not stated · strength `0.5` (stated) · 843 dl · This model generates a low cut sling style micro bikini. This model also does well with getting the  · [source](https://civitai.com/models/3022730?modelVersionId=3432428)
  - example prompt (from source, res_multistep, steps 8): `With the edge of a backyard in-ground pool in the foreground a young Korean woman with over-saturated wet long black hair rises up out of the water hands on the white til` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fb8e1f16-c9be-48ab-9c56-db53efe6f795/original=true/146962541.jpeg)
- `joschek-s-latex-bodysuits-for-moss` — `latex bodysuit` · strength not stated · 236 dl · 'nother moss port from krea, but with this one i actually redid the captions with qwen 3.8. will upd · [source](https://civitai.com/models/3034825?modelVersionId=3448250)
- `pokebra-poke-ball-bra-panties-pokemon-clot-moss` — `she is wearing a black pokeball bra and pokeball thong panties` · strength `1.0` (stated) · 168 dl · MOSS Image release 10/28/2026 Suggested strength: 1.0 Suggested tags: wearing a black pokeball bra , · [source](https://civitai.com/models/1488578?modelVersionId=3433689)

- Suggest ingest: [クロッチずらし/panties aside(XL,Pony)](https://civitai.com/models/471385) (illustrious, 33,017 dl) — `panties aside, panties, pussy`, `anus` · strength not stated — **downloads 33017 >= 2x best available (6777) in same family+category**
- Suggest ingest: [セクシーランジェリー/babydoll,sexy lingerie(SD,ILL,pony)](https://civitai.com/models/522201) (illustrious, 25,785 dl) — `babydoll` · strength not stated — **downloads 25785 >= 2x best available (6777) in same family+category**
- Suggest ingest: [No Bra SDXL](https://civitai.com/models/137296) (sdxl, 17,694 dl) — `no bra`, `covered nipples` · strength not stated — **downloads 17694 >= 2x best available (479) in same family+category**

### 21. Stockings, thigh-highs, heels and shoes

**Illustrious / NoobAI (Illustrious-XL based)**
- `longer-thigh-highs-and-legwear-ill` — trigger not stated · strength `0.75-1.25` (stated) · 567 dl · Notes on V4: Less overfitted than v3, should have less drastic effects on anatomy and art style. LoR · [source](https://civitai.com/models/2812363?modelVersionId=3384601)
  - example prompt (from source, dpmpp_3m_sde_gpu, steps 30): `thighhighers, white thighhighs, ass support,   1girl, solo, white panties, black pleated skirt, miniskirt, from behind, head out of frame, lower body, full body, leg focu` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d5fcd352-906f-4d95-be76-2dbebcd441bb/original=true/144710528.jpeg)
- `lesbian-pantyhose-ill` — `lespan` · strength not stated · 87 dl · Created from 50+ images of lesbian women in pantyhose nsfw · [source](https://civitai.com/models/3007307?modelVersionId=3412303)
- `scanty-panty-stocking-with-garterbelt-ill` — `Scanty_Pan_St0`, `green hair` · strength not stated · 80 dl · Character from anime Panty & Stocking with Garterbelt. · [source](https://civitai.com/models/3012396?modelVersionId=3418925)

**Anima**
- `take-a-chance-fishnet-bodystocking-anima` — `see-through, fishnet thighhighs, fishnet bodysuit, fishnet chaps, bott` · strength not stated · 476 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/433503?modelVersionId=3439097)
  - example prompt (from source, er_sde simple, steps 30): `absurdres, masterpiece, score_7, score_8, anime coloring, anime screenshot, 1girl, see-through, fishnet thighhighs, fishnet bodysuit, fishnet chaps, bottomless, curvy, ma` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f9a9ebc3-86cb-411b-af6c-264f0a0a3f0c/original=true/147321570.jpeg)
- `detailed-stockings-anima` — trigger not stated · strength `0.6–0.8` (stated) · 439 dl · 它把丝袜分为两种方向：油光 glossy stockings 与 哑光 matte stockings，并会根据提示词改变高光形态、表面密度和织物质感。 其中，油光效果最强，尤其是黑色丝袜 / 黑色裤 · [source](https://civitai.com/models/3033106?modelVersionId=3446088)
- `fishnet-bodystocking-clothing-anima` — `fishnet bodystocking, bodysuit, fishnets, fishnet bodysuit` · strength `1.0` (stated) · 373 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/3025218?modelVersionId=3435651)

**Krea2 (detailed-krea2)**
- `glossy-pantyhose-flux-krea2` — `glossy pantyhose flux krea2` · strength not stated · 1,631 dl · You can use it for glossy or shiny pantyhose. Testet on white, black, tan and brown. · [source](https://civitai.com/models/1443102?modelVersionId=3247385)
  - example prompt (from source): `Woman is pulling down her white miniskirt and moves her legs to pevent filming her ass. Woman is laughing into viewer and shakes head as a gesture of 'no'` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/da0bc3ec-02b1-495c-b89b-98d0617a9c10/original=true/146333292.mp4)
- `shoes-pantyhose-cleavage-zit-krea2` — `STOCKINGS`, `PANTYHOSE`, `HIGH HEELS`, `PUMPS` · strength `0.8 to 1.2` (stated) · 1,100 dl · Shoes-Cleavage for Krea2 / Z-Image-Turbo / MOSS MOSS version has been uploaded！ v 2.0 Kera2 Stocking · [source](https://civitai.com/models/2812414?modelVersionId=3383379)
- `no-rise-leggings-krea2` — `no rise leggings krea2` · strength not stated · 980 dl · Covers everything normal leggings does, except for the essentials. Trigger word: no-rise leggings · [source](https://civitai.com/models/2918600?modelVersionId=3302000)

**MOSS (Moss Image / kromoss)**
- `heel-grabbers-base-moss` — trigger not stated · strength not stated · 190 dl · Its nice to see you again OBVIOUS PERSON OF TASTE! I spent some time making something your 1girl is  · [source](https://civitai.com/models/3047057?modelVersionId=3464228)
  - example prompt (from source, Euler, steps 50): `A platinum-blonde bimbo in her early twenties with heavy makeup, a yellow and gold spiraling striped party hat with fluffy cotton rim sits atop her head, she has heavily ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a6ce566a-d278-4152-b530-0eb8661b77e3/original=true/148663857.jpeg)
- `10-inches-pleaser-heels-moss` — `101ph`, `[Infinity997,Beyond008,Beyond009,Beyond010LG,Beyond010LG],`, `10 inch platform heels, [color,clear] massive extreme platform soles, `, `[color,clear] [criss-cross,slender thin woven interlaced multi-strap,p` · strength not stated · 166 dl · My Character LoRA Gallery (1000+ Downloadable Character LoRAs & 500+ Runnable Online) Moss Image: St · [source](https://civitai.com/models/1777689?modelVersionId=3451681)
- `transparent-platform-heels-moss` — `tph0, clear pleaser platform heels, a clear transparent strap crosses ` · strength not stated · 162 dl · My Character LoRA Gallery (1000+ Downloadable Character LoRAs & 500+ Runnable Online) Moss Image: St · [source](https://civitai.com/models/1778876?modelVersionId=3454519)

- Suggest ingest: [pantyhose](https://civitai.com/models/26760) (sdxl, 24,942 dl) — `panntyhose`, `black pantyhose`, `white pantyhose` · strength `0.5` (stated) — **downloads 24942 >= 2x best available (479) in same family+category**
- Suggest ingest: [Erza Scarlet (All Armors & Outfits) (61 Outfits) / Illustrious](https://civitai.com/models/902174) (illustrious, 21,556 dl) — `erz_bwaitress, brown eyes, red hair, long hair, hair over one eye, fak` · strength `0.8 - 1` (stated) — **downloads 21556 >= 2x best available (6777) in same family+category**
- Suggest ingest: [NSFW Bunnysuit](https://civitai.com/models/109759) (illustrious, 19,383 dl) — `reverse bunnysuit,`, `pasties, maebari,`, `crotchless pantyhose` · strength not stated — **downloads 19383 >= 2x best available (6777) in same family+category**

### 22. Swimwear and beach

**Illustrious / NoobAI (Illustrious-XL based)**
- `x micro bikini_illustrious_V2.1` — `x micro bikini` · strength not stated · 4,944 dl · pony;The strength of Lora is recommended to be around 1.0. XL;The strength of Lora is recommended to · [source](https://civitai.com/models/518864?modelVersionId=2651990)
  - example prompt (from source, DPM++ 2M, steps 30): `masterpiece,amazing quality,newest,absurdres,highres,highly-detailed,detailed face,simple background,anime coloring,deep colors,matte coloring,<lora:boleromix pony_illust` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/421c5575-87c8-4a97-a88d-92d213092448/original=true/119642045.jpeg)
- `competitive-swimsuit-sd-xl-ill` — `competitive swimsuit` · strength not stated · 2,523 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2715085)
- `Ultra Micro BikiniSlingshot Swimmsuit - Illustrious - UMBV1` — `ultra_micro_bikini` · strength not stated · 1,988 dl · I had a long description for this but my browser crashed and I don't think I can recreate the magic. · [source](https://civitai.com/models/2273944?modelVersionId=2559479)

**Pony (Pony Diffusion XL)**
- `competitive-swimsuit-sd-xl-ill-pony` — `competitive swimsuit` · strength not stated · 4,591 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=614384)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `score_9, score_8_up, score_7_up,source_anime, high res image,masterpiece,best quality,girl,cute face,clear skin,shiny hair,ultra detailed eyes,simple background,  <lora:C` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fa5140b3-5335-47fc-bea2-9edd4d1a53c9/original=true/18131620.jpeg)
- `venus-bikini-pony` — `Pony`, `venus bikini` · strength not stated · 356 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2073281?modelVersionId=2362455)
- `micro-bikini-pony` — `m1cr0` · strength not stated · 41 dl · [source](https://civitai.com/models/2958153?modelVersionId=3351021)

**Anima**
- `maid-bikini-anima` — `maid bikini, maid headdress, frills, wrist cuffs,bare shoulders` · strength not stated · 2,193 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/668558?modelVersionId=3055885)
  - example prompt (from source, Euler a, steps 20): `masterpiece,best quality,highres,newest,real skin,perfect eyes,glossy hair <lora:maid bikini_anima_V1.0:1.0> maid bikini, maid headdress, frills, wrist cuffs,bare shoulde` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4acf95ee-6762-4fbf-89c1-840ec533d8fe/original=true/134420686.jpeg)
- `competitive-swimsuit-sd-xl-ill-anima` — `competitive swimsuit` · strength not stated · 1,812 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2944201)
- `nano-slingshot-bikini-anima` — `nano slingshot bikini,micro bikini` · strength not stated · 1,055 dl · Private commission on fiverr  I officially host and maintain all my models on Tensor.art I was hopin · [source](https://civitai.com/models/2885834?modelVersionId=3262119)

**Krea2 (detailed-krea2)**
- `micro-bikini-krea2` — `Micr0Bikini` · strength not stated · 2,315 dl · Generates images of women with micro bikinis. I recommend upscaling after generating, not all images · [source](https://civitai.com/models/2317614?modelVersionId=3136903)
  - example prompt (from source, Euler, steps 8): `Micr0Bikini. She’s a young woman with dark, tousled hair and heavy-lidded eyes, gazing directly into the camera with a sultry, slightly parted-lip expression that radiate` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0721d557-e45f-4e30-a42f-1f37df0aea1c/original=true/136919226.jpeg)
- `Tan-Lines-Krea2_epoch_10` — trigger not stated · strength `0.6 – 1.2` (stated) · 2,112 dl · Bikini Tan Lines LoRA A clean, detailed skin LoRA that adds realistic bikini tan lines to female cha · [source](https://civitai.com/models/2840638?modelVersionId=3206585)
- `StringOnlyBikini_Real_KR2` — `stringonlybikini, bikini, wedgie, covered pussy, peek nipples,` · strength `0.85 - 1` (stated) · 1,988 dl · ⬇️This is Anima Model⬇️ [ANIMA] offers remarkably rich expressiveness compared to the [KREA 2] model · [source](https://civitai.com/models/2845651?modelVersionId=3212894)

**MOSS (Moss Image / kromoss)**
- `micro-bikini-thong-pull-for-moss` — trigger not stated · strength `0.5` (stated) · 843 dl · This model generates a low cut sling style micro bikini. This model also does well with getting the  · [source](https://civitai.com/models/3022730?modelVersionId=3432428)
  - example prompt (from source, res_multistep, steps 8): `With the edge of a backyard in-ground pool in the foreground a young Korean woman with over-saturated wet long black hair rises up out of the water hands on the white til` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fb8e1f16-c9be-48ab-9c56-db53efe6f795/original=true/146962541.jpeg)
- `4472-swimsuit-party-xl` — `@ruanyi4472,areola slip,long sleeves,o-ring,revealing clothes,purple d` · strength not stated · 281 dl · Hello everyone! Whenever a new model is released, I just have to try training it and really put it t · [source](https://civitai.com/models/3010194?modelVersionId=3416032)
- `perfect-bikini-body-for-moss` — trigger not stated · strength `0.8 – 1.05` (stated) · 190 dl · Have you ever wanted to give your plain Jane outputs that extra umph? This LoRA does just that. Appl · [source](https://civitai.com/models/3038277?modelVersionId=3452751)

- Suggest ingest: [Slingshot swimsuit [SD1.5/Pony/Illustrious/Anima]](https://civitai.com/models/7957) (illustrious, 133,438 dl) — `slingshot swimsuit` · strength not stated — **downloads 133438 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,268 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36268 >= 2x best available (5848) in same family+category**
- Suggest ingest: [SDXL_Sexy underwear](https://civitai.com/models/124782) (sdxl, 10,105 dl) — `bikini`, `underwear`, `Lace` · strength `0.6-1.5` (stated) — **downloads 10105 >= 2x best available (479) in same family+category**

### 23. Costumes, uniforms and cosplay (adult characters)

All characters must be adults.

**Illustrious / NoobAI (Illustrious-XL based)**
- `illustriousxl-quency-escape-queen-from-nik-ill` — `Promts for this LoRA:`, `Character/Anime*`, `cosplay, parody, alternate costume,`, `official alternate costume, quency (escape queen) (nikke), quency (nik` · strength not stated · 891 dl · I have created a discord (https://discord.gg/NWpyuzsHqn) server where you can post your work and off · [source](https://civitai.com/models/2231547?modelVersionId=2512132)
  - example prompt (from source): `no` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/64f45eb1-bc8c-4653-a7bb-ebbe1103041a/original=true/114181408.mp4)
- `Girly Fishnet Swimsuit Outfits - Strapless Swimsuit - Girly Fishnet Strapless Swimsuit` — `Girly Fishnet Swimsuit (naked, fishnet swimsuit, high leged, large mes` · strength not stated · 672 dl · Girly Fishnet Swimsuit Outfits! ... it's going to be a hot summer ❤ Swimsuit: Girly Fishnet Swimsuit · [source](https://civitai.com/models/2697285?modelVersionId=3241583)
- `sheerfloralembroidery` — `see-through bra, see-through panties, frills, floral embroidery, cover` · strength not stated · 667 dl · TAGS: see-through bra, see-through panties, frills, floral embroidery, covered nipples commissions h · [source](https://civitai.com/models/2606181?modelVersionId=2926379)

**SDXL**
- `80s-aerobic-outfit-xl` — `a3robic`, `80s aerobic outfit` · strength not stated · 479 dl · [source](https://civitai.com/models/517542?modelVersionId=575094)
  - example prompt (from source, DDIM, steps 30): `aerobics class, 4 women in 80s aerobic outfit, in a studio` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7ebf68bc-06f7-4c5c-b45e-852e8fe970f2/original=true/15968422.jpeg)

**Pony (Pony Diffusion XL)**
- `seductress-witch-halloween-costume-cosplay-pony` — `Sexy_Witch`, `Sexy_Witch, witch hat, front-tie cape, black bikini top, microskirt, s` · strength not stated · 39 dl · Seductress Witch Halloween Costume / Cosplay - t2ukmyjm · [source](https://civitai.com/models/2981843?modelVersionId=3380282)
  - example prompt (from source, DPM++ 2M Karras, steps 30): `Masterpiece, best quality, amazing quality, absurdres, newest, very awa, 1girl, solo, beautiful eyes, white background, simple background,  Princess Daisy, green eyes, or` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/05f97cbe-68fd-4ef7-8d7d-d598744f8b8f/original=true/144869661.jpeg)
- `catwoman-costume-1989-pony` — `bmcw` · strength not stated · 35 dl · [source](https://civitai.com/models/3000665?modelVersionId=3403770)

**Anima**
- `maid-bikini-anima` — `maid bikini, maid headdress, frills, wrist cuffs,bare shoulders` · strength not stated · 2,193 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/668558?modelVersionId=3055885)
  - example prompt (from source, Euler a, steps 20): `masterpiece,best quality,highres,newest,real skin,perfect eyes,glossy hair <lora:maid bikini_anima_V1.0:1.0> maid bikini, maid headdress, frills, wrist cuffs,bare shoulde` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4acf95ee-6762-4fbf-89c1-840ec533d8fe/original=true/134420686.jpeg)
- `bondage-outfit-xl-ill-anima` — `bondage outfit, thighhighs, gloves, latex, dominatrix,skirt,o-ring` · strength not stated · 1,557 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/572670?modelVersionId=3086911)
- `undressed_by_ttcls_anm_v1` — `undressed by tentacles, tentacles`, `tentacle [article of clothing] lift`, `tentacle [article of clothing] pull` · strength not stated · 786 dl · LoRA for tentacles gently undressing their partner instead of tearing off clothes. Anm_v1: Same art, · [source](https://civitai.com/models/2384535?modelVersionId=3083548)

**Krea2 (detailed-krea2)**
- `bondage-outfit-v3-krea2` — `bondage outfit, fluxbondage, 1girl, breasts, solo, nipples, twintails,` · strength `0.8` (stated) · 2,775 dl · Krea2 bondage outfit v3 （Slim harness） Lora type:Krea2 triger：bondage outfit, fluxbondage, prompt：bo · [source](https://civitai.com/models/2053543?modelVersionId=3192079)
  - example prompt (from source, DDIM, steps 8): `bondage outfit, fluxbondage, 1girl, breasts, nipples, feet, barefoot, piercing, tongue, solo, foot focus, soles, long hair, toes, tongue out, black hair, realistic, sitti` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d7ad496e-d584-4ad9-92f2-8e99a0f7ed03/original=true/138561970.jpeg)
- `krea2 thong floss outfit` — `zithong, thong floss outfit, 1girl, breasts, solo, nipples, realistic,` · strength `0.8` (stated) · 1,606 dl · Krea2 thong_floss_outfit Lora type:Krea2 triger：zithong, thong floss outfit, prompt：zithong, thong f · [source](https://civitai.com/models/2217869?modelVersionId=3190414)
- `cheerleader-outfit-flux-2-klein-9b-flux-2-krea2` — `cheerleader outfit flux 2 klein 9b flux 2 krea2` · strength `0.7 - 1.0` (stated) · 1,477 dl · A outfit lora based on replicating a cheerleader's outfit. Recommended strength: 0.7 - 1.0. · [source](https://civitai.com/models/2610117?modelVersionId=3200034)

**MOSS (Moss Image / kromoss)**
- `team-rocket-cosplay-pokemon-ani-il-moss-xl` — `t34mr0ck3t,`, `t34mr0ck3t,  team rocket uniform, white jacket, cropped jacket, white ` · strength not stated · 253 dl · Prepare for trouble! 🚀 Follow me on X/Twitter for exclusive content: https://x.com/Citron_Legacy 😁 P · [source](https://civitai.com/models/371976?modelVersionId=3416558)
  - example prompt (from source, steps 10): `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced. integrated_multimodal_description: shkzz,  realistic jiggle.` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ac8c694e-0817-4923-b167-be90b39b2416/original=true/146200666.mp4)
- `maid-classic-moss` — `maid,maid apron,maid headdres` · strength not stated · 221 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/703211?modelVersionId=3456338)
- `outfit-cut-out-bodysuit-moss` — `@GP`, `She is wearing a black, long-sleeve, cut-out bodysuit that exposes her` · strength not stated · 128 dl · use this for outfit and Trigger word @GP She is wearing a black, long-sleeve, cut-out bodysuit that  · [source](https://civitai.com/models/3042275?modelVersionId=3458123)

- Suggest ingest: [Undressing SD1/XL/PONY/FLUX](https://civitai.com/models/505266) (sdxl, 55,860 dl) — `undressing` · strength `1.3` (stated) — **downloads 55860 >= 2x best available (479) in same family+category**
- Suggest ingest: [Slavekini, aka Slave Leia Outfit - Clothing [Krea2, Anima, IL, Pony, S](https://civitai.com/models/7913) (illustrious, 30,714 dl) — `slave leia outfit`, `or`, `slavekini, pelvic curtain , collar, armlet , hair ornament, braid` · strength `.8-1.0` (stated) — **downloads 30714 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Undressing LoRA [SD1.5 & SDXL1.0]](https://civitai.com/models/242034) (sdxl, 26,132 dl) — `undressing` · strength not stated — **downloads 26132 >= 2x best available (479) in same family+category**

### 24. Accessories and gear (collars, chastity, piercings, condoms, plugs)

**Illustrious / NoobAI (Illustrious-XL based)**
- `harness-sd-xl-ill` — `harness, bdsm, o-ring`, `bound` · strength not stated · 6,777 dl · The strength of Lora is recommended to be around 0.8 · [source](https://civitai.com/models/583686?modelVersionId=1131895)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,ultra-detailed-background,cute girl, eyelashes,middle` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/af55ddee-1780-4068-aef6-bdf1c704d0aa/original=true/43808908.jpeg)
- `clitoris jewely_illustrious_V1.0` — `clitoris jewelry, clitoris, thong` · strength not stated · 4,725 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/576831?modelVersionId=1168859)
- `buttplugs-ill` — `buttplug`, `heart-shaped buttplug` · strength not stated · 3,717 dl · 🔥Buttplugs LoRa / Illustrious🔥 How to Use: It was trained on a large enough dataset, so it should no · [source](https://civitai.com/models/1293802?modelVersionId=1460149)

**SDXL**
- `scary-masks-xl` — trigger not stated · strength not stated · 20 dl · msk · [source](https://civitai.com/models/3016013?modelVersionId=3423617)
  - example prompt (from source, DPM++ 2M SDE, steps 20): `"msk, The object is a vivid mask against black background. Set on flat surface, lighting highlights details. Camera angle is frontal, focusing on the object's expressive ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0bf297d3-b67e-45d2-8af3-574e2679d960/original=true/146529906.jpeg)

**Pony (Pony Diffusion XL)**
- `genital-piercing-xl-pony` — `pussy piercing, clitoris piercing`, `pussy`, `spread puusy` · strength not stated · 3,287 dl · [source](https://civitai.com/models/459565?modelVersionId=511474)
  - example prompt (from source, Euler, steps 25): `score_9, score_8_up, score_7_up,source_anime, high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-face,cute girl,spread pussy,cum in pus` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4611900d-a292-4d2b-b65e-1e29bf564d23/original=true/71051377.jpeg)
- `clitoris-jewelry-xl-ill-pony` — `clitoris jewelry` · strength not stated · 2,800 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/576831?modelVersionId=643187)
- `clitoris-piercing-xl-pony-2` — `clitoris piercing`, `clitoris ring` · strength not stated · 782 dl · Removed some images that were messy. Added more images. This one feels more consistent. · [source](https://civitai.com/models/337473?modelVersionId=380331)

**Anima**
- `[Anima][Concept]flat_chastity_cage-10` — `flat chastity cage`, `pov, pov chastity`, `chastity strap`, `chastity ring` · strength `1.0` (stated) · 2,533 dl · Anima Version Update: Flat Chastity Cage for Anima model. Not perfect but works well with other lora · [source](https://civitai.com/models/1037793?modelVersionId=3020542)
  - example prompt (from source, Euler a, steps 28): `masterpiece, best quality, highres, year 2025, score_9, score_8, score_7, uncensored.  @sugoi hi, 1girl, futanari, large breasts, flat chastity cage, chastity strap, stan` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2fc86023-aa16-45cb-8c79-a50438cd6d61/original=true/133381333.jpeg)
- `harness-sd-xl-anima` — `harness,o-ring` · strength not stated · 2,154 dl · The strength of Lora is recommended to be around 0.8 · [source](https://civitai.com/models/583686?modelVersionId=3064972)
- `nipple-piercing-zit-il-flux-anima` — `nipple piercing zit il flux anima` · strength `0.7` (stated) · 1,492 dl · Just an attempt to create a different lora, if it turns out good, I'll create more. I accept suggest · [source](https://civitai.com/models/1096396?modelVersionId=3050316)

**Krea2 (detailed-krea2)**
- `used-condom-krea2` — `usedc0nd0m.` · strength not stated · 4,476 dl · About this version The used condom Lora for Krea2 is here. The preview image includes a workflow, wh · [source](https://civitai.com/models/2780495?modelVersionId=3131462)
  - example prompt (from source, er_sde, steps 12): `A hyper-realistic, intimate studio portrait of a woman, captured in a dramatic, warm-lit setting against a deep black background.  **Subject: woman** *   **Face & Express` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ddd1c52c-7861-47f5-95e1-2c2ace3980dc/original=true/136762516.jpeg)
- `nipple-piercing-zit-il-flux-krea2` — `pierced nipples,` · strength `0.7` (stated) · 3,716 dl · Just an attempt to create a different lora, if it turns out good, I'll create more. I accept suggest · [source](https://civitai.com/models/1096396?modelVersionId=3182058)
- `used-condom-krea2-2` — `used condom`, `upside down condom` · strength not stated · 2,416 dl · Krea 2 didn't understand much about this but it didn't take much to open up its abilities. Version 1 · [source](https://civitai.com/models/2825038?modelVersionId=3198969)

**MOSS (Moss Image / kromoss)**
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)
  - example prompt (from source, er_sde, steps 25): `Beautiful, realistic,  cinematic, masterpiece. Pretty woman deep throating a deepdilgag. Her throat bulges a lot. The dildo gag is strapped into her throat. Her eyes are ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f0e6809b-da93-4ee4-b6c5-1507b3fe53be/original=true/146591869.jpeg)
- `barbell-nipple-piercings-ultra-hd-moss` — `nipple piercings` · strength not stated · 532 dl · Barbell Nipple Piercings Trained with at 1024x1024 with hand cropped patches from 20MP images High d · [source](https://civitai.com/models/2357066?modelVersionId=3451406)
- `harness-gag-xl` — trigger not stated · strength `1.2` (stated) · 514 dl · Harness gag Hunyuan model Trained a Hunyuan video model using the same dataset used for the Flux mod · [source](https://civitai.com/models/676488?modelVersionId=3412034)

- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,268 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36268 >= 2x best available (5848) in same family+category**
- Suggest ingest: [乳首責め/nipple pull](https://civitai.com/models/627113) (illustrious, 33,549 dl) — `nipple pull,holding,1girl,nipples,1boy,nipple piercing,chain,` · strength not stated — **downloads 33549 >= 2x best available (10931) in same family+category**
- Suggest ingest: [Milking Machines](https://civitai.com/models/419704) (pony, 16,179 dl) — `milking machine,suction device,milk machine,harness,object insertion,s` · strength not stated — **downloads 16179 >= 2x best available (7814) in same family+category**

### 25. POV and camera angle / framing

Camera/framing LoRAs go early in the stack; keep strength moderate.

**Illustrious / NoobAI (Illustrious-XL based)**
- `CuckNTR POV Pony LoRa - 3.0 Illustrious - NTR_POV` — trigger not stated · strength not stated · 9,704 dl · Important tags (tag: cuck pov,netorare,femdom) Make person hold a cellphone with porn on it (tags: p · [source](https://civitai.com/models/339447?modelVersionId=1255291)
  - example prompt (from source, Euler a, steps 30): `(masterpiece, best quality), amazing quality, very aesthetic, absurdres, highres, newest, HDR, 8K, high detail RAW  1boy, breasts, cellphone, hetero, ntr, nude, handjob, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fdfa6065-d12e-4414-a889-0cf6041cf8bf/original=true/50256070.jpeg)
- `Pov Urethral Insertion femdom 主観尿道責め 第一人称尿道责 - IL_V1_0 - pov_urethral_insertion` — `pov urethral insertion`, `metal urethral plug`, `urethral beads`, `latex urethral plug` · strength `0.8` (stated) · 2,127 dl · Introduction This LoRA is primarily designed to depict first-person urethral stimulation (pov_urethr · [source](https://civitai.com/models/1662303?modelVersionId=1881475)
- `Femdom POV illustrious - V1 - Upskirt_POV-000008` — `Femdom_pov_illus` · strength not stated · 1,437 dl · Femdom POV for illustrious · [source](https://civitai.com/models/1695778?modelVersionId=1919205)

**SDXL**
- `datultimatepxl-next-gen-explicit-mechanics-xl` — `datup3xl` · strength not stated · 85 dl · ⚡ Recommended Base Checkpoint: For peak tag execution, maximum structural stability, and crisp rende · [source](https://civitai.com/models/2891929?modelVersionId=3275368)
  - example prompt (from source, Euler a, steps 25): `masterpiece, perfect outlines, black outline, bold outlines, brush strokes, best quality, absurdres, wind, western art <lora:DABMsJapanXL-2.0:2.7> dabmsjapanxl2 woman sho` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/80108fb3-c5ec-44a9-93df-6c28814c9e60/original=true/141120362.jpeg)

**Pony (Pony Diffusion XL)**
- `soryu-asuka-langley-neon-genesis-evangelio-xl` — `asuka_a_pxl, souryuu asuka langley, long hair, bangs, blue eyes, brown`, `bodysuit, pilot suit, plugsuit, plugsuit (evangelion), red bodysuit, i` · strength not stated · 36 dl · [source](https://civitai.com/models/3045453?modelVersionId=3462148)
  - example prompt (from source, Euler a, steps 30): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_anime,  asuka_a_pxl, souryuu asuka langley, long hair, bangs, blue eyes, brown hair, hair orn` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cc058513-daff-4ec3-859f-c13f392fb9c6/original=true/148553733.jpeg)

**Anima**
- `fpov-anima` — `female pov looking down her breasts` · strength not stated · 6,246 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/427349?modelVersionId=2948925)
  - example prompt (from source, er_sde simple, steps 30): `absurdrabsurdres, masterpiece, score_7, score_8, 1girl, female pov looking down her breasts, turtleneck sweater, jeans, computer keyboard, at computer, computer mouse, sh` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/496f8ce2-df98-4a1d-ac6d-1e076a08a2fe/original=true/130836662.jpeg)
- `fpcview_v0.0.0-step00000600` — `fpcview`, `from above, wide shot, dutch angle`, `head out of frame, straight-on`, `The character stands near the edge of the frame while a large empty sp` · strength not stated · 2,133 dl · v0.0.0 (Initial Release) The purpose of this LoRA is to break the AI's deeply hardcoded composition  · [source](https://civitai.com/models/2782139?modelVersionId=3133505)
- `ntr-pov-netorase-netorare-cuckold-for-anima` — `NTRedwifeSP`, `netorare, depth of field, a couple having sex behind a sliding door, a` · strength not stated · 1,693 dl · With this Lora, you can watch your Waifu being cuckolded right in front of you. This LoRA may also a · [source](https://civitai.com/models/3016671?modelVersionId=3424519)

**Krea2 (detailed-krea2)**
- `_Krea2__Taking_selfie_from_3rd-person_view_epoch_6` — `th1rd-p3rson-self1e third-person view of`, `viewed from a three-quarters angle`, `she is sitting and reclining back spreading her thighs {and feet up cu`, `she is standing and reaching carefully between her leg holding a smart` · strength not stated · 1,779 dl · Give it a go. It generates images of [women] taking selfies. Not a selfie image as such, as it's fro · [source](https://civitai.com/models/2818090?modelVersionId=3178646)
  - example prompt (from source, Euler, steps 8): `candid photo captured in the moment, unplanned unposed, captured in the moment with candid postures shown mid actions and expressions captured in the moment and unflatter` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/83b749cd-532f-43a8-8c8b-00e32500d8c2/original=true/138163103.jpeg)
- `fpov-female-point-of-view-for-krea2` — `From a top-down view`, `From a first-person perspective` · strength `1` (stated) · 1,728 dl · V1 (alone): This is the main version. This LoRa is the result of 2 years of testing on Flux, but I w · [source](https://civitai.com/models/2918304?modelVersionId=3301630)
- `pov-handjob-krea2` — trigger not stated · strength `0.6` (stated) · 1,700 dl · Try a strength between 0.6 and 1.0.  SDXL: Sorry, this LoRA is a bit tricky to use and requires a fe · [source](https://civitai.com/models/2804245?modelVersionId=3376062)

**MOSS (Moss Image / kromoss)**
- `home-cctv-hd-clear-home-dorm-security-came-moss` — trigger not stated · strength not stated · 1,552 dl · Description Clear colour home-security stills: a camera mounted high in a room corner looks down acr · [source](https://civitai.com/models/3015044?modelVersionId=3422347)
  - example prompt (from source, Euler, steps 50): `homecctvhd, A clear color CCTV still shows one wide room overview in a residential home. The full landscape frame is a single stationary camera feed, viewed obliquely acr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e9fc284e-b490-4902-805c-dcb9a33db7ec/original=true/146458072.jpeg)
- `bodycam-view-vlogger-chest-cam-pov-moss` — trigger not stated · strength not stated · 666 dl · A chest-mounted action camera POV: a low, chest-height wide-angle frame facing the person who is tal · [source](https://civitai.com/models/3021452?modelVersionId=3430758)
- `underwater-action-cam-pool-sea-wide-angle-moss` — trigger not stated · strength not stated · 595 dl · Wide-angle frames from an action camera fully below the surface: sunlight refracted through moving w · [source](https://civitai.com/models/3019299?modelVersionId=3427960)

- Suggest ingest: [Upright straddle sex front view](https://civitai.com/models/82128) (sdxl, 59,134 dl) — `1boy, sex, hetero, upright straddle, straddling, girl on top` · strength `1.0` (stated) — **downloads 59134 >= 2x best available (213) in same family+category**
- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Cowgirl Position Sex Non-POV / Third Person](https://civitai.com/models/145887) (sdxl, 47,903 dl) — `1boy, sex, cowgirl position, girl on top, straddling` · strength not stated — **downloads 47903 >= 2x best available (213) in same family+category**

### 26. Poses and body positions

**Illustrious / NoobAI (Illustrious-XL based)**
- `pose_femdom_pegging_nipple_tweak - v1.0 - pose_pegging_nipple_tweak` — `pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1b` · strength not stated · 3,470 dl · pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1boy, hetero, ejaculation, ejacu · [source](https://civitai.com/models/1295786?modelVersionId=1462424)
  - example prompt (from source, Euler a, steps 30): `masterpiece,best quality,amazing quality,official,  <lora:pose_pegging_nipple_tweak:1>  pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1boy, hetero, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dff3ca52-7d9c-4486-b3c3-b2708d10e186/original=true/60107192.jpeg)
- `Amen_pose8` — `Amposp,legs,praying hands,ass,bent over,blush,sweat,heart,standing,han` · strength not stated · 1,855 dl · Test Lora: First attempt at creating a concept Lora. It might not work perfectly, but it has some de · [source](https://civitai.com/models/2261838?modelVersionId=2546013)
- `size-difference-wall-xl` — `CAWSDV1, against wall, foot on another's chest, size difference, wall,` · strength not stated · 1,792 dl · Father of lies, Cum in disguise Real Description part since pack is getting pretty big: -If you wond · [source](https://civitai.com/models/1196912?modelVersionId=2919043)

**SDXL**
- `step-sis-ass-spread-simulator-xl` — `ass_spread` · strength `0.80–0.95` (stated) · 141 dl · High-fidelity interaction & pose LoRA for SDXL and Illustrious XL. Trained using a precise UNet-only · [source](https://civitai.com/models/3012318?modelVersionId=3418834)
  - example prompt (from source, DPM++ 2M SDE, steps 30): `ass_spread, side view, profile, one hand, hand resting on butt, flat palm, separated fingers, five distinct fingers, perfect human hands, close-up, low angle, shot from b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/6456c2b9-9103-4fde-943f-4714f8c47043/original=true/146294194.jpeg)
- `pillow-pillow-play-pose-xl` — `P1ll0w`, `Humping a pillow` · strength not stated · 81 dl · [source](https://civitai.com/models/3020840?modelVersionId=3429960)

**Anima**
- `folded-pose-anima` — `folded`, `legs up`, `knees together`, `legs together` · strength not stated · 3,918 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/623820?modelVersionId=2923111)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.0:0.3>,glossy hair,perfect eyes,real skin,  <lora:manguri_anima_V1.0:1> folded,spr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a9ed33ed-ff08-4e68-8aff-3295d8ac40a2/original=true/129817283.jpeg)
- `butt-to-butt-copulation-human-pose-anima` — `butt to butt copulation`, `all fours` · strength not stated · 1,816 dl · 神秘小姿势 trigger word: butt to butt copulation better with: all fours, testicles, x-ray, ass ripple opt · [source](https://civitai.com/models/2727765?modelVersionId=3066227)
- `jack-o-challenge-pose-helper-rear-front-anima` — `she is posing jack-o'_challenge, the image is split into two horizonta` · strength not stated · 1,790 dl · IMPORTANT: READ BELOW The model is trained using natural language. I recommend using 1024x1024. Trig · [source](https://civitai.com/models/2568958?modelVersionId=2886534)

**Krea2 (detailed-krea2)**
- `krea2 sex 淫模 - carry - krea2 standing and carry` — `zitstanding, stand_and_carry, 1girl, 1boy, hetero, penis, sex, nude, a` · strength `0.6–0.7` (stated) · 5,912 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170121)
  - example prompt (from source, Euler, steps 8): `zitstanding, stand_and_carry, 1girl, 1boy, hetero, penis, sex, nude, ass, testicles, indoors, black hair, suspended congress, barefoot, long hair, nipples, vaginal, leg h` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dd22a7fd-13e5-4757-8cb4-3d0e5b9bb964/original=true/137922857.jpeg)
- `krea2 sex 淫模 - Leg - standing_on_one_leg_sex_epoch_10` — trigger not stated · strength `0.6–0.7` (stated) · 3,697 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3249142)
- `KREA2 Femdom Facesitting - v1.0 - Krea2_Facesitting_.1.0` — trigger not stated · strength not stated · 3,265 dl · LORA trained pretty good on KREA2. No keyword is needed. *PLEASE NOTE: ALL PROMPTS GENERATED WITH GE · [source](https://civitai.com/models/2744320?modelVersionId=3086707)

**MOSS (Moss Image / kromoss)**
- `ek-s-aio-pose-nsfw-moss` — `many!! see description!` · strength not stated · 1,672 dl · This lora is for MOSS image This is a ALL IN ONE Pose set I worked on for a while Its purpose Is to  · [source](https://civitai.com/models/3020392?modelVersionId=3429378)
  - example prompt (from source, Euler, steps 15): `Cinematic photorealistic shot in a dark forest. a young woman in a tent, topless, small cleavage. Her very long blonde hair is tied in twin tails, and she wears attractiv` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ff0122c6-3392-45c1-9d53-8da2534d0e13/original=true/146805159.jpeg)
- `blowbowpose-moss` — `blowbowpose` · strength not stated · 743 dl · The keyword for this model is "blowbowpose" To prompt this model you need to know a few bonus things · [source](https://civitai.com/models/2987554?modelVersionId=3428844)
- `yogabowpose-moss` — `yogabowpose` · strength not stated · 220 dl · The keyword for this model is "yogabowpose" You can change the outfit, background, hair color, acces · [source](https://civitai.com/models/2987547?modelVersionId=3428836)

- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (213) in same family+category**
- Suggest ingest: [Reverse upright straddle / sitting on lap](https://civitai.com/models/114292) (pony, 41,344 dl) — `reverse upright straddle`, `legs together`, `spread legs` · strength not stated — **downloads 41344 >= 2x best available (8495) in same family+category**

### 27. Oral (blowjob, deepthroat, cunnilingus)

**Illustrious / NoobAI (Illustrious-XL based)**
- `fellatio-and-masturbation-ill` — `fellatio and masturbation, fellatio, female masturbation, 1boy, penis` · strength not stated · 11,460 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=1134882)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,ultra-detailed-background,cute girl, eyelashes <lora:` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b096e211-882c-47d9-a170-9807b295ef2a/original=true/43975686.jpeg)
- `facial-cumshot-225-xl` — `cumshot, facial, masturbation, ejaculation,`, `pov, pov hands` · strength not stated · 5,489 dl · 🔥 Facial cumshot LoRa for Illustrious 🔥 Hey everyone! This model focuses on creating images with a g · [source](https://civitai.com/models/1164568?modelVersionId=1310077)
- `Autofellatio_v3.0(NAI_ROUWEI)-000007` — `autofellatio` · strength `0.8-1` (stated) · 3,413 dl · Illustrious-XL version now available, with even better anatomy I made a video on how to achieve the  · [source](https://civitai.com/models/24866?modelVersionId=1656798)

**SDXL**
- `ahegao-facials-xl` — `ahegao_cumshot`, `ahegao_facial`, `eyes closed` · strength not stated · 872 dl · [source](https://civitai.com/models/2078761?modelVersionId=2352101)

**Pony (Pony Diffusion XL)**
- `fellatio-and-masturbation-pony` — `fellatio and masturbation`, `fellatio`, `female masturbation`, `fingering` · strength not stated · 11,628 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=616692)
  - example prompt (from source, DPM++ 2M, steps 25): `score_9, score_8_up, score_7_up,source_anime, high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,simple background,cute girl <lora` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c9bfaf09-0159-4ff4-b31f-08dfb2543a3d/original=true/53416934.jpeg)
- `huge-facial-bukkake-ponyxl-xl-pony` — `nm_btrfacials,`, `facials,`, `bukkake,` · strength not stated · 2,063 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=1305311)
- `Futadom Blowjob kneeling male. - V1 - Futadom_Blowjob_kneeling_male.` — `futadom`, `kneeling male`, `standing futa`, `face fucking` · strength not stated · 1,625 dl · [source](https://civitai.com/models/569699?modelVersionId=634976)

**Anima**
- `fellatio-and-masturbation-anima` — `fellatio and masturbation, 1girl, 1boy, penis,pussy` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=3000440)
  - example prompt (from source, Euler a, steps 20): `masterpiece,amazing quality,best quality,newest,absurdres,highres,highly-detailed,kawaii,cute,real skin,sharp draw lines  <lora:fellatio and masturbation:1> fellatio and ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/94f6dfe3-2d52-4070-b5b5-819a1af4dae3/original=true/132663275.jpeg)
- `deeper-penetration-deepthroat-and-somethin-anima` — `deep penetration`, `deepthroat`, `object insertion` · strength not stated · 2,412 dl · I trained this Lokr to solve the issue of not penetrate deep enough. However, I was too ambitious an · [source](https://civitai.com/models/2708641?modelVersionId=3042522)
- `huge-facial-bukkake-ponyxl-xl-anima` — `huge facial bukkake ponyxl xl anima` · strength not stated · 2,247 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=3171504)

**Krea2 (detailed-krea2)**
- `how-much-cum-yes-bukkake-gokkun-cum-overfl-krea2` — `cum,`, `semen,`, `sperm,`, `gokkun` · strength `0.8-0.9` (stated) · 8,807 dl · Join my Discord: https://discord.gg/tMbPUdkP27 Excellent cum texture, put that shit on everything! I · [source](https://civitai.com/models/2512358?modelVersionId=3221218)
  - example prompt (from source): `image is a raw candid photo,  image shows dark haired girl. she is wearing her dark ornamental dress. holding one glas in her hand.   the glas is filled with semen. the g` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ae5471d8-02be-43a6-be23-9aa309a25fda/original=true/139475622.jpeg)
- `krea2 sex 淫模 - BJ - kreablowjob` — `kreablowjob, 1girl, realistic, hetero, breasts, 1boy, penis, nipples, ` · strength `0.6–0.7` (stated) · 4,514 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3158893)
- `pressed-down-deepthroat-krea2` — `deepthroat, rough deepthroat, struggling, blush, forceful head grab,`, `wide eyes, frown,`, `close up, from side,` · strength `0.8-1.0` (stated) · 4,266 dl · Join my Discord:https://discord.gg/tMbPUdkP27 Idea is, that the man helps the woman get deeper.  Str · [source](https://civitai.com/models/2937576?modelVersionId=3325478)

**MOSS (Moss Image / kromoss)**
- `cum-xl` — trigger not stated · strength not stated · 2,247 dl · Commonly used vocabulary in captioning: - Fluid states (use one or two): glossy · thick white · visc · [source](https://civitai.com/models/3012757?modelVersionId=3419412)
  - example prompt (from source, res_multistep, steps 20): `Hyper realistic iphone photo. a naked 20 year old  asian woman in bed, her legs spread wide and pussy dripping cum. elbows pressing into the bed to prop her up. Her face ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f015cb99-c805-4fac-beb8-bcbbd63be3a4/original=true/146390132.mp4)
- `pov-blowjob-moss` — `Highly explicit, high-angle, close-up photo of a nude woman. She is pe` · strength not stated · 1,272 dl · Basic Prompt: Highly explicit, high-angle, close-up photo of a nude woman. She is performing oral se · [source](https://civitai.com/models/2514609?modelVersionId=3434597)
- `blowjob-moss` — `Highly explicit photo. She is performing oral sex, blowjob on a man wh` · strength not stated · 948 dl · Basic Prompt: Highly explicit photo of a nude woman. She is performing oral sex, blowjob on a man wh · [source](https://civitai.com/models/2500766?modelVersionId=3431704)

- Suggest ingest: [X-ray (vaginal, anal & oral) LoRa / PonyXL & Illustrious](https://civitai.com/models/494435) (illustrious, 44,397 dl) — `vaginal xray`, `oral xray`, `anal xray` · strength not stated — **downloads 44397 >= 2x best available (11673) in same family+category**
- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (213) in same family+category**
- Suggest ingest: [Pov Blowjob + Titjob + Handjob [updated]](https://civitai.com/models/446163) (illustrious, 40,457 dl) — `pov, 1girl, 1boy,`, `fellatio,`, `paizuri,`, `handjob,` · strength not stated — **downloads 40457 >= 2x best available (9704) in same family+category**

### 28. Sex positions (cowgirl, missionary, doggy, etc.)

Use ONE position LoRA per image.

**Illustrious / NoobAI (Illustrious-XL based)**
- `sex machine_XL_illustrious_V1.0` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 6,822 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=972316)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `masterpiece,ultra-detailed,best quality,8K,illustration,cute face,clean skin ,shiny hair,woman,ultra-detailed-eyes,simple background, <lora:add-detail-xl:1>nude <lora:sex` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/de66290c-ada5-4e10-bffb-ea22652db501/original=true/35404026.jpeg)
- `doggystyle-view-from-behind-creampie-ill` — `facefocus_doggy,sex from behind,cumshot, cum drip, cum in pussy,lookin`, `arms behind back, restrained,` · strength `0.8` (stated) · 5,246 dl · lora for a doggystyle sex from behind view. A girl is force to look at her pussy and ejaculation. st · [source](https://civitai.com/models/1662410?modelVersionId=1881604)
- `Spooning Femdom Handjob Pegging Pony Illustrious - Illustrious - Spooning_Femdom_Handjob__Pegging_Pony__Illustrious-000058` — `Spooning, lying, on side, 1girl, 1boy, hetero, from above,`, `handjob, reach-around,`, `pegging, anal, strap-on, dildo,`, `hug from behind,` · strength not stated · 5,064 dl · Spooning Femdom for Pony & Illustrious · [source](https://civitai.com/models/1449583?modelVersionId=1639171)

**SDXL**
- `dual-penetration-dap-xl` — `DPTP`, `DUAL ANAL PENETRATION` · strength not stated · 253 dl · v1 · [source](https://civitai.com/models/2567761?modelVersionId=2885205)
  - example prompt (from source, LCM, steps 8): `dptp, anal, breasts, sex, nipples, pussy, high heels, penis, hetero, group sex, spread pussy, mmf threesome, brown hair, threesome, 2boys, pubic hair, uncensored, realist` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dc11e28f-b607-4757-8526-c03351cabfd4/original=true/128400892.jpeg)

**Pony (Pony Diffusion XL)**
- `sex-machine-xl-ill-pony` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 6,571 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=927540)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `score_9, score_8_up, score_7_up,source_anime, high res image,masterpiece,best quality,(girl,big breasts:1.0),cute face,clear skin,shiny hair,ultra detailed eyes,simple ba` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f6bacfb4-6836-44a3-b3ab-4a25a3f6590b/original=true/33108543.jpeg)
- `sex-from-behind-ill-pony` — `sex from behind` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/868502?modelVersionId=971982)
- `Sex_Machines_V2` — `s3xm@ch!n3` · strength not stated · 3,088 dl · Scrubbed training data of watermarks and logos. Retrained · [source](https://civitai.com/models/546416?modelVersionId=685247)

**Anima**
- `sex-machine-xl-ill-anima` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 4,153 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=2952118)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.0:0.3>,glossy hair,perfect eyes,real skin, woman  <lora:sex machine_anima_V1.0:0.8` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bd2d05a8-5c5b-43ed-a9ac-daa86d64a388/original=true/130956658.jpeg)
- `human-onahole-fantasy-sex-concept-collecti-anima` — `HBGV2, giant, holding person, size difference,` · strength not stated · 3,219 dl · I BARELY HAD ANY DICKS INSIDE ME Real description:  Held By Giant - it gets the same effect, seeming · [source](https://civitai.com/models/1319951?modelVersionId=2987156)
- `sex-from-behind-ill-anima` — `sex from behind` · strength not stated · 2,966 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/868502?modelVersionId=2980425)

**Krea2 (detailed-krea2)**
- `K_gangbanghelper` — `prompt anything with:`, `gangbang, double penetration, gets double penetrated, anal sex, vagina`, `She is on her back.`, `she is kneeling.` · strength `0.7-1.0` (stated) · 6,569 dl · Krea2 This is a All holes filled-lora. She will have the tendency to always have a penis in her mout · [source](https://civitai.com/models/2240240?modelVersionId=3159235)
  - example prompt (from source): `the image is a amateur raw candid photo. image shows jinx with blue braids on a white bed in a moody dark bedroom. she wears her outfit. she is on her back.  she is in a ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/53da9495-0360-4e91-b2ba-33569ccee773/original=true/137637843.jpeg)
- `krea2 sex 淫模 - carry - krea2 standing and carry` — `zitstanding, stand_and_carry, 1girl, 1boy, hetero, penis, sex, nude, a` · strength `0.6–0.7` (stated) · 5,912 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170121)
- `Krea2penetrationbellyb1000step` — trigger not stated · strength `1-2` (stated) · 5,675 dl · This Lora is for making images of sexual acts with deeper penetration than have been possible with K · [source](https://civitai.com/models/2823421?modelVersionId=3200626)

**MOSS (Moss Image / kromoss)**
- `pantyhose-sex-moss` — trigger not stated · strength not stated · 329 dl · Guidance 2.5 Steps 25 Sampler er_sde Seed 2 · [source](https://civitai.com/models/3022457?modelVersionId=3432090)
  - example prompt (from source, er_sde, steps 25): `1 female, explicit, heterosexual, vulva, penis, 1 male, vagina, sexual act, nipples, breasts, legs spread, unhidden, pantyhose, clitoris, medium-sized breasts, testicles,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2e9b88d9-7a50-48d6-880c-841350fde376/original=true/146941478.jpeg)
- `ek-s-mecha-suit-sex-machine-moss` — `sex machine mecha suit` · strength not stated · 279 dl · edit: added extracted loras. r16 seems to be quite fine. and it is just 75 mega not over one giga bi · [source](https://civitai.com/models/3041593?modelVersionId=3457246)
- `blow-up-sex-doll-inflatable-sex-toy-moss` — trigger not stated · strength not stated · 240 dl · Honestly I never saw a blow-up doll IRL 😅, this is just my take on Dollification porn CGI wirh an hy · [source](https://civitai.com/models/2993967?modelVersionId=3432220)

- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (11673) in same family+category**
- Suggest ingest: [Balls Deep / Deep(er) Penetration](https://civitai.com/models/550870) (illustrious, 70,061 dl) — `deep penetration` · strength not stated — **downloads 70061 >= 2x best available (11673) in same family+category**
- Suggest ingest: [Mating press](https://civitai.com/models/90532) (pony, 61,812 dl) — `mating press` · strength not stated — **downloads 61812 >= 2x best available (8495) in same family+category**

### 29. Cum, fluids and aftermath

**Illustrious / NoobAI (Illustrious-XL based)**
- `facial-cumshot-225-xl` — `cumshot, facial, masturbation, ejaculation,`, `pov, pov hands` · strength not stated · 5,489 dl · 🔥 Facial cumshot LoRa for Illustrious 🔥 Hey everyone! This model focuses on creating images with a g · [source](https://civitai.com/models/1164568?modelVersionId=1310077)
  - example prompt (from source, Euler a, steps 30): `anime, masterpiece, best quality, 8k, 1girl, 1boy, arezu (pokemon) , <lora:cumshot:1>, cumshot, facial, masturbation, ejaculation, penis, pov, pov hands` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/be1cd1f6-dda0-4fa5-b3e9-3fb31eeaa565/original=true/52907093.jpeg)
- `doggystyle-view-from-behind-creampie-ill` — `facefocus_doggy,sex from behind,cumshot, cum drip, cum in pussy,lookin`, `arms behind back, restrained,` · strength `0.8` (stated) · 5,246 dl · lora for a doggystyle sex from behind view. A girl is force to look at her pussy and ejaculation. st · [source](https://civitai.com/models/1662410?modelVersionId=1881604)
- `Flaccid penis femdom after cum handjob finger handjob Request - Illustrious - after-cum_handjob-afcuhj-IL` — `afcuhj, penis, foreskin, pov,`, `handjob,`, `footjob,`, `clothed female nude male, testicles, caressing testicles,` · strength `0.6 - 1` (stated) · 3,614 dl · If you have any questions or problems, please use DM or Discussion. And please send Discussion(comme · [source](https://civitai.com/models/1454328?modelVersionId=1644383)
- `MCB Lubed ill v2-15` **[HF repo only - needs adding to Graydient]** — trigger not stated · strength not stated · no source link

**SDXL**
- `pornmaster-projectile-cumejaculationcumsho-xl` — `projectile cum, penis,` · strength not stated · 4,139 dl · SDXL-V1培訓字幕excel檔案下載。 SDXL-V1 training subtitle excel file download. -- 培训图片包含男同性恋，要生成女性图片正面提示词放入女性聚 · [source](https://civitai.com/models/950655?modelVersionId=1064347)
  - example prompt (from source, DPM++ 2M, steps 25): `DSLR,a beautiful 18 year old Korean idol,projectile cum,multiple penises,multiple boys,(female focus),penis, hetero,gangbang,completely nude,breasts,nipples, flat chest ,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e57dd4a1-99be-436c-9410-887a9337ad82/original=true/40260994.jpeg)
- `cumshot-xl` — trigger not stated · strength not stated · 455 dl · [source](https://civitai.com/models/1538069?modelVersionId=1740302)

**Pony (Pony Diffusion XL)**
- `cumshots-meme-for-ponyxl-pony` — `cumshots meme` · strength not stated · 2,221 dl · Initial Version · [source](https://civitai.com/models/491746?modelVersionId=546832)
  - example prompt (from source, Euler a, steps 20): `score_9, score_8_up, score_7_up, cumshots meme, 1girl, long hair, blue hair, purple eyes, breasts, pussy, anus, ass up, nude, blush, butt, cum, cum drip, cum string, cum ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/76adf0d5-834c-422a-b0df-e2424139fc43/original=true/14404000.jpeg)
- `huge-facial-bukkake-ponyxl-xl-pony` — `nm_btrfacials,`, `facials,`, `bukkake,` · strength not stated · 2,063 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=1305311)
- `Under Toilet Seat - V1 - Under_Toilet_Seat` — `under toilet seat`, `femdom`, `closed lid`, `anus` · strength not stated · 1,835 dl · [source](https://civitai.com/models/855068?modelVersionId=956696)
- `MCB Lubed pony v1-14` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `MCB Lubed pony v2-10` **[HF repo only - needs adding to Graydient]** — trigger not stated · strength not stated · no source link

**Anima**
- `female-ejaculation-krea2-2` — `female ejaculation, pussy` · strength not stated · 3,114 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/558452?modelVersionId=2980272)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.0:0.3>,glossy hair,perfect eyes,real skin, <lora:female ejaculation_anima_V1.0:1> ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a60c8278-b1dc-4e22-baf9-443f51258724/original=true/131945296.jpeg)
- `huge-facial-bukkake-ponyxl-xl-anima` — `huge facial bukkake ponyxl xl anima` · strength not stated · 2,247 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=3171504)
- `anus_cum_expulsion` — `cum in anus`, `excessive cum` · strength not stated · 1,241 dl · less of an explosion and more of a steady thick flow. has a bias towards fat asses and generally low · [source](https://civitai.com/models/2715039?modelVersionId=3050439)

**Krea2 (detailed-krea2)**
- `realcumk4` — `cum on face`, `cum covered face`, `cum in mouth` · strength not stated · 16,673 dl · I'm back. realcum krea2 alpha This is the first version for testing the concept with the krea2 model · [source](https://civitai.com/models/326320?modelVersionId=3208030)
  - example prompt (from source, ER SDE, steps 10): `<lora:realcumk4:1> from above  amateur photo of a (Mongolian0:.4) mature woman, cute  smile, cum on face,she is caressing and grabbing a penis and pushing the penis into ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5b7f94d6-8675-4075-8cbf-1678538e0d43/original=true/139056790.jpeg)
- `oiled-skin-krea2` — trigger not stated · strength `1.0` (stated) · 8,842 dl · Krea 2 Turbo Info: Use the trigger phrase "OiledSkin" for best results. Keep strength at 1.0 for max · [source](https://civitai.com/models/87685?modelVersionId=3096878)
- `how-much-cum-yes-bukkake-gokkun-cum-overfl-krea2` — `cum,`, `semen,`, `sperm,`, `gokkun` · strength `0.8-0.9` (stated) · 8,807 dl · Join my Discord: https://discord.gg/tMbPUdkP27 Excellent cum texture, put that shit on everything! I · [source](https://civitai.com/models/2512358?modelVersionId=3221218)
- `MCB Lubed krea2 v1-08` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**MOSS (Moss Image / kromoss)**
- `cum-xl` — trigger not stated · strength not stated · 2,247 dl · Commonly used vocabulary in captioning: - Fluid states (use one or two): glossy · thick white · visc · [source](https://civitai.com/models/3012757?modelVersionId=3419412)
  - example prompt (from source, res_multistep, steps 20): `Hyper realistic iphone photo. a naked 20 year old  asian woman in bed, her legs spread wide and pussy dripping cum. elbows pressing into the bed to prop her up. Her face ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f015cb99-c805-4fac-beb8-bcbbd63be3a4/original=true/146390132.mp4)
- `cum-on-face-moss` — `semen on her face`, `semen dripping from her chin` · strength `0.8-0.6` (stated) · 1,212 dl · Probably the only cumshot lora you will ever need. 💦💦 Weight: 0.8-0.6 Trigger words: semen on her fa · [source](https://civitai.com/models/146522?modelVersionId=3434966)
- `cumswap-for-moss` — trigger not stated · strength not stated · 459 dl · Seems to work pretty well to aid with cumswaps · [source](https://civitai.com/models/3037703?modelVersionId=3452004)

- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1373) in same family+category**
- Suggest ingest: [Bukkake / excessive cum](https://civitai.com/models/109745) (pony, 105,734 dl) — `excessive cum` · strength not stated — **downloads 105734 >= 2x best available (12530) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (11673) in same family+category**

### 30. Solo, masturbation and fingering

**Illustrious / NoobAI (Illustrious-XL based)**
- `fellatio-and-masturbation-ill` — `fellatio and masturbation, fellatio, female masturbation, 1boy, penis` · strength not stated · 11,460 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=1134882)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,ultra-detailed-background,cute girl, eyelashes <lora:` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b096e211-882c-47d9-a170-9807b295ef2a/original=true/43975686.jpeg)
- `fingering-ill` — `fingering` · strength not stated · 6,896 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/551963?modelVersionId=2101849)
- `Reverse Nursing Handjob - Concept - booru v2 - reverse-nursing-handjob-v2-illustriousxl-lora-nochekaiser` — `<lora:reverse-nursing-handjob-v2-illustriousxl-lora-nochekaiser:1>, re` · strength `1.0` (stated) · 5,935 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/1266705?modelVersionId=2076440)

**SDXL**
- `femdom handjob SDXL - SDXL v1.0 - femdom handjob SDXL_epoch_19` — trigger not stated · strength `0.6` (stated) · 403 dl · Try a strength between 0.6 and 1.0. · [source](https://civitai.com/models/2570715?modelVersionId=2888449)
  - example prompt (from source, DPM++ 2M SDE, steps 20): `realistic, high quality, 8k,  <lora:femdom handjob SDXL_epoch_19:0.65> femdom handjob, submissive handjob, hetero, 1boy, penis, 1girl, bdsm, femdom, blonde woman hairbob,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/33c2c133-df19-480d-b2b7-aa5f677415ee/original=true/128520689.jpeg)
- `step-sis-backside-anal-fingering-simulator-xl` — `finger_ass` · strength not stated · 260 dl · [source](https://civitai.com/models/3009204?modelVersionId=3414763)

**Pony (Pony Diffusion XL)**
- `fellatio-and-masturbation-pony` — `fellatio and masturbation`, `fellatio`, `female masturbation`, `fingering` · strength not stated · 11,628 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=616692)
  - example prompt (from source, DPM++ 2M, steps 25): `score_9, score_8_up, score_7_up,source_anime, high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,simple background,cute girl <lora` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c9bfaf09-0159-4ff4-b31f-08dfb2543a3d/original=true/53416934.jpeg)
- `fingering-pony` — `fingering` · strength not stated · 6,541 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/551963?modelVersionId=614217)
- `Handjob with Handgag Femdom - PonyXL - V1 - g4gh4nd` — `g4gh4nd,handjob` · strength not stated · 3,778 dl · [source](https://civitai.com/models/636063?modelVersionId=711159)

**Anima**
- `masturbation-with-dildo-object-insertion-anima` — `female masturbation, object insertion, dildo grab`, `vaginal object insertion, vaginal`, `anal object insertion, anal` · strength `0.8-1.0` (stated) · 4,019 dl · A girl and her trusty friend. If you have any request or would like a commission, feel free to comme · [source](https://civitai.com/models/218726?modelVersionId=3057069)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality, newest,  1girl, fox girl, wavy hair, long hair, hair between eyes,brown hair, blue eyes, white pupils, brown fox tail, sitting, spread legs, fe` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/091caad7-7b60-41a5-8f73-127a7fcaeb8f/original=true/134457411.jpeg)
- `fellatio-and-masturbation-anima` — `fellatio and masturbation, 1girl, 1boy, penis,pussy` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=3000440)
- `fingering-anima` — `fingering` · strength not stated · 3,632 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/551963?modelVersionId=3054388)

**Krea2 (detailed-krea2)**
- `fingering-krea2` — `fingering-krea2` · strength `0.6–0.85` (stated) · 6,754 dl · V1:  krea2_fingering_v0.1 — Krea 2 concept LoRA that improves fingering (vaginal/anal). No trigger w · [source](https://civitai.com/models/2813245?modelVersionId=3172724)
  - example prompt (from source): `Amateur-style photograph of a realistic 40-year-old woman sitting naked on a plain wooden chair in an ordinary bedroom. Her legs are lifted and spread wide, knees bent, f` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/6c385b10-4ddf-4587-82c3-4a2e49236abd/original=true/137994034.jpeg)
- `krea2 sex 淫模 - mast - krea2 masturbation` — `zitmast, female masturbation, 1girl, solo, realistic, spread legs, fem` · strength `0.6–0.7` (stated) · 4,792 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3170098)
- `krea2 sex 淫模 - HJ - handjob_krea2_3264617_epoch_10` — `handjob, krea2grab, 1girl, jewelry, breasts, blonde hair, nipples, ear` · strength `0.6–0.7` (stated) · 4,206 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3265921)

**MOSS (Moss Image / kromoss)**
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)
  - example prompt (from source, er_sde, steps 25): `Beautiful, realistic,  cinematic, masterpiece. Pretty woman deep throating a deepdilgag. Her throat bulges a lot. The dildo gag is strapped into her throat. Her eyes are ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f0e6809b-da93-4ee4-b6c5-1507b3fe53be/original=true/146591869.jpeg)
- `blow-up-sex-doll-inflatable-sex-toy-moss` — trigger not stated · strength not stated · 240 dl · Honestly I never saw a blow-up doll IRL 😅, this is just my take on Dollification porn CGI wirh an hy · [source](https://civitai.com/models/2993967?modelVersionId=3432220)

- Suggest ingest: [PornMaster-潮吹，淫水水坑，自慰，湿，高潮脸，滴下淫水-squirting,female ejaculation,pussy ju](https://civitai.com/models/106683) (illustrious, 46,541 dl) — `squirting excessive pussy juice upward from her pussy, pussy juice,spr`, `squirting,female ejaculation, pussy juice,spread pussy` · strength not stated — **downloads 46541 >= 2x best available (11673) in same family+category**
- Suggest ingest: [XXX Gangbang/Group Sex Generator (Evil Angel) PONY / IL XL / 輪姦ジェネレーター](https://civitai.com/models/654360) (illustrious, 28,696 dl) — `1girl, solo forcas, nude, 4+boys, Gangbang, Group Sex, Multiple Boys, ` · strength `0.9-0.6` (stated) — **downloads 28696 >= 2x best available (11673) in same family+category**
- Suggest ingest: [Nursing handjob](https://civitai.com/models/101854) (pony, 25,566 dl) — `nursing handjob` · strength not stated — **downloads 25566 >= 2x best available (12530) in same family+category**

### 31. BDSM, bondage and restraints

Consensual adult scenes only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `jav-hard-core-bdsm-generator-m-drag-m-ill` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 11,673 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=2106832)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7ac5ccf9-0ff9-4b84-bd54-19fdb756471f/original=true/93850194.mp4)
- `Spooning Femdom Handjob Pegging Pony Illustrious - Illustrious - Spooning_Femdom_Handjob__Pegging_Pony__Illustrious-000058` — `Spooning, lying, on side, 1girl, 1boy, hetero, from above,`, `handjob, reach-around,`, `pegging, anal, strap-on, dildo,`, `hug from behind,` · strength not stated · 5,064 dl · Spooning Femdom for Pony & Illustrious · [source](https://civitai.com/models/1449583?modelVersionId=1639171)
- `otk-spanking-bdsm-ill-2` — trigger not stated · strength `0.6` (stated) · 4,326 dl · Is with a great pleasure that i present this Lora. Change log Anima V1 Cleared motion lines, Made sp · [source](https://civitai.com/models/979512?modelVersionId=1097112)

**SDXL**
- `femdom handjob SDXL - SDXL v1.0 - femdom handjob SDXL_epoch_19` — trigger not stated · strength `0.6` (stated) · 403 dl · Try a strength between 0.6 and 1.0. · [source](https://civitai.com/models/2570715?modelVersionId=2888449)
  - example prompt (from source, DPM++ 2M SDE, steps 20): `realistic, high quality, 8k,  <lora:femdom handjob SDXL_epoch_19:0.65> femdom handjob, submissive handjob, hetero, 1boy, penis, 1girl, bdsm, femdom, blonde woman hairbob,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/33c2c133-df19-480d-b2b7-aa5f677415ee/original=true/128520689.jpeg)
- `step-sis-bdsm-bondage-simulator-xl` — `step-sis_bound` · strength not stated · 181 dl · [source](https://civitai.com/models/3010878?modelVersionId=3416954)

**Pony (Pony Diffusion XL)**
- `jav-hard-core-bdsm-generator-m-drag-m-pony` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 12,530 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=721539)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/910fd244-2bc4-4925-877e-da98725e43c3/original=true/33533282.jpeg)
- `0565-bdsm-clothing-1-pony` — `ruanyi0565,bdsm,white bondage outfit,barbell piercing,choker,clitoris ` · strength not stated · 3,844 dl · 0.9 · [source](https://civitai.com/models/465238?modelVersionId=517724)
- `Handjob with Handgag Femdom - PonyXL - V1 - g4gh4nd` — `g4gh4nd,handjob` · strength not stated · 3,778 dl · [source](https://civitai.com/models/636063?modelVersionId=711159)

**Anima**
- `jav-hard-core-bdsm-generator-m-drag-m-anima` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 2,743 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=3229257)
  - example prompt (from source): `30img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7987858-0e44-4cf0-88e1-5801ae50b989/original=true/139720937.mp4)
- `shibari-sd-xl-ill-anima` — `shibari` · strength not stated · 2,613 dl · The strength of Lora is recommended to be around 0.4. · [source](https://civitai.com/models/591433?modelVersionId=2944205)
- `posebound-19` — `metal bondage frame`, `metal vine bondage`, `metal harness` · strength not stated · 2,028 dl · If you like the model, please leave a comment or post an image! 🥰 Or if the model doesn't work as we · [source](https://civitai.com/models/2759105?modelVersionId=3115106)

**Krea2 (detailed-krea2)**
- `arms-tied-around-legs-doggystyle-bdsm-bond-krea2` — `bd5m, top-down bottom up, tied up, arms tied to legs, anal sex, anal p`, `Image is shot from side, side view,` · strength `0.7-1.0` (stated) · 3,628 dl · Based on a few training pics, works best with horizontal layouts. Krea 2 Strength: 0.7-1.0 Have fun! · [source](https://civitai.com/models/2358990?modelVersionId=3220184)
  - example prompt (from source): `this image is a candid raw photograph,    image shows the gprincess zelda in a torn dress.  She is wearing a torn dress.  scene is in a dark dungeon. Looking directly at ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5aa197c6-0ec9-4771-8899-8330c007811c/original=true/139436658.jpeg)
- `bondage-outfit-v3-krea2` — `bondage outfit, fluxbondage, 1girl, breasts, solo, nipples, twintails,` · strength `0.8` (stated) · 2,775 dl · Krea2 bondage outfit v3 （Slim harness） Lora type:Krea2 triger：bondage outfit, fluxbondage, prompt：bo · [source](https://civitai.com/models/2053543?modelVersionId=3192079)
- `brkn-bdsm-krea2` — `brkn-bdsm-krea2` · strength not stated · 2,734 dl · This is an early test version of the model. I trained it fairly quickly using a limited dataset, mai · [source](https://civitai.com/models/2730222?modelVersionId=3069273)

**MOSS (Moss Image / kromoss)**
- `bondage-gags-megapack-aio-moss` — trigger not stated · strength not stated · 1,878 dl · See example prompts in images. Trained on 10,750 steps 430 images. All images posted with SFT model, · [source](https://civitai.com/models/3009470?modelVersionId=3415104)
  - example prompt (from source, Euler, steps 12): `Five Women kneeling on the floor, Side by side.   1st woman from the left: Blonde. She has a silver hollow O-ring gag in her open mouth fastened with black leather straps` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/98c444f9-fc5a-4e16-adb3-176ace636adf/original=true/146122325.jpeg)
- `deep-throat-dildo-gag-moss` — `deep throating deepdilgag`, `dildo gag strapped into throat`, `bulging throat` · strength not stated · 642 dl · Generates big, thick cock gags in the subject's throat. Currently only trained on a pool of female i · [source](https://civitai.com/models/2383141?modelVersionId=3425010)
- `harness-gag-xl` — trigger not stated · strength `1.2` (stated) · 514 dl · Harness gag Hunyuan model Trained a Hunyuan video model using the same dataset used for the Flux mod · [source](https://civitai.com/models/676488?modelVersionId=3412034)

- Suggest ingest: [Bondage Suspension](https://civitai.com/models/8762) (illustrious, 92,975 dl) — `suspension` · strength not stated — **downloads 92975 >= 2x best available (11673) in same family+category**
- Suggest ingest: [bondage 来吧 go BDSM, lora for Moss Qwen21 ZiB F1 & XL](https://civitai.com/models/136849) (moss, 34,221 dl) — `bondage`, `shibari`, `ropes`, `1990年代风格` · strength not stated — **downloads 34221 >= 2x best available (13485) in same family+category**
- Suggest ingest: [[Flux/SDXL/Pony] Device Bondage](https://civitai.com/models/528877) (sdxl, 24,957 dl) — `device bondage`, `naked woman`, `dark wood background`, `wrist cuffs` · strength not stated — **downloads 24957 >= 2x best available (4139) in same family+category**

### 32. Multiple partners, gangbang, threesome

**Illustrious / NoobAI (Illustrious-XL based)**
- `Double_Dildo_ILXL` — `yuri, double dildo, ass-to-ass, ass to ass, wet glistening pussies, se`, `anal sex, anal, anal penetration, anal object insertion,`, `vaginal object insertion, object insertion, vaginal, after vaginal,`, `upper body, face to face, face-to-face, yuri, looking at another, from` · strength not stated · 3,737 dl · have created a discord (https://discord.gg/NWpyuzsHqn) server where you can post your work and offer · [source](https://civitai.com/models/1157997?modelVersionId=1302583)
  - example prompt (from source, Euler a, steps 30): `highres, hi res, best quality, masterpiece, 2d, intricate details, 4k, anime coloring, shadow, uncensored, 2girls, eyelashes, nose, curly hair, green hair, bangs, blush, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c161a995-7f23-422f-b1f3-e86c6dee3fee/original=true/52550395.jpeg)
- `multiple-penetrations-ill-xl` — `multiple penetrations, 1girl, multiple boys, penis, sex, group sex,` · strength `1.0` (stated) · 3,723 dl · A strength of around 1.0 for Lola is recommended. · [source](https://civitai.com/models/1370965?modelVersionId=1548943)
- `multiple insertion_illustrious_V1.1` — `multiple insertion, sex toy`, `vaginal object insertion`, `anal object insertion` · strength `1.0` (stated) · 3,280 dl · A strength of around 1.0 is recommended for Lola. It is unstable. · [source](https://civitai.com/models/1368757?modelVersionId=1546401)
- `suze-group_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Pony (Pony Diffusion XL)**
- `Strap-on assisted reverse spitroast - FFMFFF femdomlesbian concept for Pony - v6.0 - reverse_strapon_spitroast-v6-pony` — `reverse strapon spitroast`, `2girls, 1boy, ffm threesome, multiple girls, hetero, pegging, strap-on`, `3girls, fff threesome, multiple girls, lesbian, strap-on, strap-on sex` · strength not stated · 344 dl · This took a lot of trial and error to get a somewhat working version... · [source](https://civitai.com/models/2397616?modelVersionId=2695806)
  - example prompt (from source, DPM++ 2M SDE, steps 30): `score_9, score_8_up, score_7_up, score_6_up, source_anime, anime coloring, <lora:reverse_strapon_spitroast-v6-pony:0.8>, 2girls, 1boy, hetero, ffm threesome, threesome, c` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/9f017927-686d-4d3a-918f-0a59b55cb29b/original=true/121341730.jpeg)

**Anima**
- `group-sex-with-a-large-number-of-boys-anima` — `groupsex_ani,` · strength `0.8` (stated) · 2,457 dl · lora for a group sex with a large number of boys. strength ~0.8. It is better to use landscape form  · [source](https://civitai.com/models/1932245?modelVersionId=3312976)
  - example prompt (from source, er_sde, steps 27): `masterpiece, best quality, anime illustration, screen cap, highres, score_9, score_8_up, score_7_up, uncensored, score_6_up, face focus, full body, from side groupsex_ani` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2d44d75d-7598-461d-8dee-4cf723e45c12/original=true/142352598.jpeg)
- `multiple penetration_anima_V1.0` — `multiple boys, multiple penetration, group sex, gangbang, 1girl, anal,` · strength `1.0` (stated) · 1,946 dl · A strength of around 1.0 for Lola is recommended. · [source](https://civitai.com/models/1370965?modelVersionId=2958545)
- `AN_doggydp_epoch_5` — `d0ggy,, 1girl, 3boys, doggystyle, anal, vaginal,` · strength `0.7-1.0` (stated) · 1,604 dl · This is double Penetration in Doggystyle, many think the cowgirl DP is Doggy-version. But no.. Krea  · [source](https://civitai.com/models/2213833?modelVersionId=3074935)

**Krea2 (detailed-krea2)**
- `K_gangbanghelper` — `prompt anything with:`, `gangbang, double penetration, gets double penetrated, anal sex, vagina`, `She is on her back.`, `she is kneeling.` · strength `0.7-1.0` (stated) · 6,569 dl · Krea2 This is a All holes filled-lora. She will have the tendency to always have a penis in her mout · [source](https://civitai.com/models/2240240?modelVersionId=3159235)
  - example prompt (from source): `the image is a amateur raw candid photo. image shows jinx with blue braids on a white bed in a moody dark bedroom. she wears her outfit. she is on her back.  she is in a ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/53da9495-0360-4e91-b2ba-33569ccee773/original=true/137637843.jpeg)
- `k_doggystyledp` — `d0ggy,, double penetration, doggystyle, vaginal sex, anal sex, double `, `the girl has sex in doggystyle position and get double penetrated by t` · strength `0.7-1.0` (stated) · 3,896 dl · This is double Penetration in Doggystyle, many think the cowgirl DP is Doggy-version. But no.. Krea  · [source](https://civitai.com/models/2213833?modelVersionId=3156267)
- `krea2 sex 淫模 - GB - gangbang_epoch_10` — `krea2gang, gangbang, 1girl, multiple boys, sex, mmf threesome, penis, ` · strength `0.6–0.7` (stated) · 3,582 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3252428)
- `mcbbedridden-krea2-000010.TA_trained` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

- Suggest ingest: [Multiple insertion / penetration](https://civitai.com/models/89125) (pony, 36,633 dl) — `multiple penetrations`, `multiple insertions`, `anal object insertion`, `vaginal object insertion` · strength not stated — **downloads 36633 >= 2x best available (12530) in same family+category**
- Suggest ingest: [Double Penetration LoRa / PonyXL & Illustrious](https://civitai.com/models/482827) (illustrious, 33,894 dl) — `doublepen, vaginal, anal` · strength `0.7` (stated) — **downloads 33894 >= 2x best available (11673) in same family+category**
- Suggest ingest: [Fondled](https://civitai.com/models/705447) (illustrious, 30,962 dl) — `1girl surrounded by males, girl sandwiched by boys, group, multiple bo`, `groping,`, `breast grab,`, `fingering,` · strength `0.5-0.8` (stated) — **downloads 30962 >= 2x best available (9704) in same family+category**

### 33. Backgrounds, rooms and environments

**Illustrious / NoobAI (Illustrious-XL based)**
- `D3P9WJVGGMEE3747FK3A77VFC0` — `wifesp` · strength not stated · 437 dl · test · [source](https://civitai.com/models/2653049?modelVersionId=2979016)
  - example prompt (from source, Euler a, steps 29): `masterpiece, best quality, absurdres, highres, 1girl, milf, 43 years old, mature female, asian female,brown hair, large natural breasts, large aerolas, fair skin, blush, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dc72c570-31a8-467e-953e-f13eb891e592/original=true/132417499.jpeg)
- `Soviet Gothic Architecture Buildings NoobAI AD - v1.0 - Soviet_Gothic_Architecture_Buildings_NoobAI_AD` — `Soviet_Gothic`, `city`, `building` · strength `0.5 to 1` (stated) · 37 dl · This is a NoobAI lora for the Soviet Gothic architecture style. A weight of 0.5 to 1 works well with · [source](https://civitai.com/models/2889839?modelVersionId=3267053)
- `space-age-farming-background-ad-ill` — `SpAgFa`, `agriculture` · strength `0.6 to 1.15` (stated) · 27 dl · This is a NoobAI lora for Space Age style farming backgrounds.  A weight of 0.6 to 1.15 works well w · [source](https://civitai.com/models/2952642?modelVersionId=3344248)

**SDXL**
- `atomicpunk-interior-buildings-ad-xl` — `AtoPunInt`, `interior` · strength not stated · 47 dl · [source](https://civitai.com/models/2949992?modelVersionId=3340943)
  - example prompt (from source, Euler a, steps 35): `very awa, aesthetically pleasing, masterpiece, best quality, Clean Composition, dutch angle, in'ei, chiaroscuro, 8K, HDR, CGI, interior, <lora:AtoPunInt_(Buildings)_(SDXL` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/309e9d53-8a18-4d88-87f4-1ce6c0d284b0/original=true/143249968.jpeg)
- `Penthouse Floor Window Lifestyle Scene Backdrop SDXL LoRA - v1.0 - scene_penthouse_floor_window_v1` — trigger not stated · strength not stated · 32 dl · [source](https://civitai.com/models/2871727?modelVersionId=3244663)
- `Greek Island Terrace Lifestyle Scene Backdrop SDXL LoRA - v1.0 - scene_greek_island_terrace_v1` — trigger not stated · strength not stated · 27 dl · [source](https://civitai.com/models/2872943?modelVersionId=3246147)

**Pony (Pony Diffusion XL)**
- `space-age-farming-background-ad-pony` — `SpAgFa`, `agriculture` · strength not stated · 29 dl · [source](https://civitai.com/models/2953322?modelVersionId=3345092)
  - example prompt (from source, Euler a, steps 35): `very awa, aesthetically pleasing, masterpiece, absurd details, best quality, Clean Composition, dutch angle, in'ei, chiaroscuro, <lora:SpAg_(Buildings)_(Pony)_(AD):1.5> S` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/acec9bbb-356d-4cc7-b8a3-bf2d308d3921/original=true/143388141.jpeg)

**Anima**
- `japanese-school-hallway-background-ad-anima` — `JapHal` · strength `0.8 to 1.25` (stated) · 328 dl · This is an Anima lora for Japanese School Hallway backgrounds. The samples largely came from anime l · [source](https://civitai.com/models/2976615?modelVersionId=3373714)
  - example prompt (from source, ER SDE, steps 32): `<lora:training_1850035-20261001044740066-seds:0.8> JapHal, interior, school hallway, Masterclass illustration, anime. An interior view of a Japanese highschool hallway. W` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/095d8708-813f-45f3-8b48-c89502006895/original=true/144355745.jpeg)
- `meeting-room-anima` — `m33t1ng`, `indoors, long table, window, chairs, ceiling light, cityscape` · strength not stated · 305 dl · Creates a meeting room / board room background Trigger: m33t1ng Additional: indoors, long table, win · [source](https://civitai.com/models/2956232?modelVersionId=3348667)
- `Makikusu Makinaru Sakura Bitch Street Fighter Doujin Style Anima - v1.0 - Makikusu Makinaru Sakura Bitch Street Fighter Doujin Style Anima` — `Malebolgia, Makinaru` · strength `1` (stated) · 288 dl · The model I think is fairly self explanatory. https://vocaroo.com/1dCKgpymuk1M Back to my devilish t · [source](https://civitai.com/models/2889444?modelVersionId=3266586)

**Krea2 (detailed-krea2)**
- `Nightmare_Grunge_Krea_2_Version_epoch_9` — trigger not stated · strength `0.5 to 1` (stated) · 1,769 dl · Many models are very "clean" and "bright"- grunge, dirt, darkness and atmospheric horror details are · [source](https://civitai.com/models/2804228?modelVersionId=3161763)
  - example prompt (from source, Euler, steps 12): `A high-resolution anime-style masterpiece depicting a lone female figure with long black hair reclining in a cluttered, dimly lit bathroom at night, surrounded by cracked` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/da60c806-fd9f-40a4-ab61-93a0e586ad64/original=true/137713903.jpeg)
- `cuckold-scene-concept-krea2` — `cuckold session` · strength not stated · 1,295 dl · Cuckold / hotwife concept LoRA for photorealistic multi-person scenes. Trained to reproduce cuckold  · [source](https://civitai.com/models/2893135?modelVersionId=3271126)
- `cctv-room-krea2` — `cctvfootage` · strength not stated · 717 dl · About this version v2 focuses on better prompt adherence and more precise control through detailed d · [source](https://civitai.com/models/2992439?modelVersionId=3393441)

**MOSS (Moss Image / kromoss)**
- `background-inset-moss` — `bgeyes`, `bgface` · strength `0.6` (stated) · 223 dl · Krea2 V1.0 There we go. The Krea2 version also works great. And it respects the proportions of the b · [source](https://civitai.com/models/2138798?modelVersionId=3427591)
  - example prompt (from source, Euler, steps 10): `masterpiece, very aesthetic, score_7_up, , , fashion shoot, comic style, two-tone_background. female character is soulcalibur taki_\(soulcalibur\) black_hair brown_eyes p` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/8c83907c-3f76-42e7-b293-8b0dd38b03ea/original=true/146716562.jpeg)
- `joker-style-olive-cinema-grade-olive-gray-moss` — trigger not stated · strength `0.5` (stated) · 157 dl · A film color grade: everything pushed to olive gray and dark green, pale sodium and fluorescent lamp · [source](https://civitai.com/models/3034837?modelVersionId=3448264)
- `rooms-onsen-moss` — `z1os` · strength `1` (stated) · 143 dl · Finding all my models or profile elsewhere than Civitai is without my consent ! Please don't repost  · [source](https://civitai.com/models/3025069?modelVersionId=3435474)

- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (23879) in same family+category**
- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Pony Character Concept Art XL & 1.5 by creativehotia](https://civitai.com/models/23167) (pony, 37,904 dl) — `conceptart,multiple views,white background,simple background` · strength `1` (stated) — **downloads 37904 >= 2x best available (8308) in same family+category**

### 34. Character sheets, multi-view, reference layouts

**Illustrious / NoobAI (Illustrious-XL based)**
- `reference-sheet-illustriousxl-lora-nochekaiser` — `<lora:reference-sheet-illustriousxl-lora-nochekaiser:1>, reference she` · strength `1.0` (stated) · 1,180 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/2799724?modelVersionId=3156120)
  - example prompt (from source): `Subtle idle animation. The subject stays in place and breathes slowly and naturally, chest and shoulders rising and falling. A gentle, slow head and upper-body sway with ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7bebb8b6-3fdd-458f-9a9a-1517db938644/original=true/137572771.mp4)
- `character-sheet-turnaround-generator-ill` — `charsheet`, `multiple views, turnaround, front view, back view, side view, referenc` · strength `0.5` (stated) · 745 dl · Generates character design/reference sheets: turnarounds (front/side/back), outfit breakdowns with d · [source](https://civitai.com/models/2925755?modelVersionId=3310717)
- `two-panel-mating-press-2-ill` — `twopanel_mpress` · strength `0.7–1.0` (stated) · 394 dl · Two-Panel Mating Press / 2コマ種付けプレス This LoRA generates a two-panel mating press composition, combini · [source](https://civitai.com/models/3008450?modelVersionId=3413739)

**Anima**
- `multiview-of-licking-penis-anima` — `multiview of licking penis anima` · strength `0.9` (stated) · 1,215 dl · multiple view of a girl licking penis. strength ~ 0.9. 2026.8.27 add 'Anima' examples of prompts, mu · [source](https://civitai.com/models/1746990?modelVersionId=3271432)
  - example prompt (from source, Euler, steps 25): `masterpiece, best quality, highres, uncensored, score_9, score_8_up, score_7_up, score_6_up multiple_oral, oral, multiple views, kneeling, testicles, saliva, licking, lic` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/902b8dbb-bfd0-4a7b-b4f3-b9b4ac6f3927/original=true/140983031.jpeg)
- `Multiview` — `multiview`, `multiple views, simple background, white background, spread legs, lyin` · strength not stated · 935 dl · lora for pure laziness tag: multiview · [source](https://civitai.com/models/2615809?modelVersionId=2937013)
- `FBKDYR658QDKD568APPT0N61N0` — `CharacterSheet, reference sheet, color guide, multiple views, full bod` · strength not stated · 830 dl · Character Sheet · [source](https://civitai.com/models/2692844?modelVersionId=3023593)

**Krea2 (detailed-krea2)**
- `character-sheet-helper-krea2` — `FBcs` · strength `0.6` (stated) · 4,565 dl · This model is designed to help you build a character sheet for a character you plan to train, create · [source](https://civitai.com/models/2933017?modelVersionId=3319758)
  - example prompt (from source, Euler a, steps 10): `FBcs,  A female goblin, green skin, leather and canvas clothes, short stack body, small hooked nose, red hair. White background.` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/01ee239d-3402-4de0-a560-574aa5e1e35b/original=true/142560346.jpeg)
- `krea2_charactersheet_full_v1` — `Follow the prompt template I left in the workflow.` · strength not stated · 3,182 dl · TripleView is a LoRA trained on approximately 300 character sheet samples, with a strong focus on ge · [source](https://civitai.com/models/2764727?modelVersionId=3203877)
- `ingrid-street-streetfighter6-krea2` — `1ngrid` · strength not stated · 380 dl · 提示词推荐(Prompt recommendations): 1ngrid 建议添加该提示词加强3D效果 It is recommended to add this prompt to enhance · [source](https://civitai.com/models/2938102?modelVersionId=3326123)

**MOSS (Moss Image / kromoss)**
- `person-file-a-dead-serious-profile-sheet-f-moss` — trigger not stated · strength not stated · 709 dl · A vertical profile / dossier sheet: big headline, ID photo, data table (name, age, height and so on) · [source](https://civitai.com/models/3018066?modelVersionId=3426379)
  - example prompt (from source, Euler, steps 50): `personfileconcept, This white resume page uses thin sans-serif typography, thin outlines, pale grey table cells and red bars. "BODY REFERENCE SHEET" is centered at the to` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/71b406f8-9f3c-4167-97e5-49b55f6f4525/original=true/146664107.jpeg)
- `online-meeting-video-conference-grid-scree-moss` — trigger not stated · strength not stated · 595 dl · A convincing online-meeting screenshot: several webcam tiles on a dark meeting interface — 2×2 grid, · [source](https://civitai.com/models/3014506?modelVersionId=3421649)

- Suggest ingest: [BFS - Best Face Swap](https://civitai.com/models/2027766) (krea2, 110,251 dl) — `body_swap: replace the person with the reference person.` · strength not stated — **downloads 110251 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (23879) in same family+category**
- Suggest ingest: [Hentai Comic Random Generator (FULL COLOR) Anima / Pony / IL XL / フルカラ](https://civitai.com/models/585589) (illustrious, 66,772 dl) — `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view:1.1, Frame, Text, speech bubb` · strength not stated — **downloads 66772 >= 2x best available (23879) in same family+category**
