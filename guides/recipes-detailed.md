# Detailed goal recipes (top 3 per family, with source-stated example prompts)

Same structure as SKILL.md recipes but deeper. Verified Graydient picks first; HF-only flagged; max 3 Suggest-ingest lines.

### 1. Photoreal skin, realism and detail

Pick one realism/detail LoRA first; extra ones fight each other.

**Illustrious / NoobAI (Illustrious-XL based)**
- `trendcraft-style-detailer-xl` — `trendcraft-style-detailer-xl` · strength `1` (stated) · 22,266 dl · 💖 Support & Share the Magic!  Love this detailer? Like, add to collection, and tag this resource in  · [source](https://civitai.com/models/1350877?modelVersionId=1809575)
  - example prompt (from source, Euler a, steps 30): `lazypos, 1girl, masterpiece, outdoors, upper body, from side, city, street, yellow eyes, twintails, silver hair, looking at viewer, jacked, cloudy sky, long hair, buildin` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/294d1f4f-1b1f-4f90-838f-455b7e190f2e/original=true/77300462.jpeg)
- `add-micro-details-concept-ill-2` — `addmicrodetails` · strength not stated · 17,180 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=2832991)
- `add-micro-details-concept-ill-4` — `addmicrodetails` · strength not stated · 12,040 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=1732142)

**SDXL**
- `trendcraft-the-peoples-style-detailer-base-xl` — trigger not stated · strength not stated · 1,779 dl · Image sources include only Illustrious and NoobAI models. No realistic content. No X or higher rated · [source](https://civitai.com/models/1390819?modelVersionId=1768080)
  - example prompt (from source, DPM++ SDE Karras, steps 30): `macro photo, sparkling magical fantasy glass flower dewdrop, very detailed, amazing quality, intricate, cinematic light, highly detail, beautiful, surreal, dramatic, gala` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2e8e174e-ec63-47f4-97b0-e432615c1632/original=true/75267901.jpeg)
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)
- `trendcraft-the-peoples-style-detailer-base-xl-v2-1a-sdxl-3-12` — trigger not stated · strength not stated · 836 dl · Trained on SDXL base.  Used a lower tagging threshold compared to Pony XL v2.0. Solid improvement co · [source](https://civitai.com/models/1390819?modelVersionId=1571948)

**Pony (Pony Diffusion XL)**
- `penis-real-diffusion-realistic-pony` — `penisQuiron` · strength `0.7 - 1.3` (stated) · 6,585 dl · 👑 Penis Real Diffusion - Illustrious - LORA 👑 realistic ⚙️🔧Model base: Illustrious This LORA is capa · [source](https://civitai.com/models/696766?modelVersionId=936819)
  - example prompt (from source): `Sexy  man saying "Hi, this is really delicious. It's a gift for you." then strokes up and down her penis with his hand very rapidly, and moments later, she saying sadly "` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1bba07f6-1e89-4214-8d6d-86906c4dce5e/original=true/135629625.mp4)
- `amateur-style-diffusion-pony` — `amateurQuironStyle`, `amateurQuiron`, `flash photo`, `webcam photo` · strength `0.7 - 1` (stated) · 4,157 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=833676)
- `trendcraft-the-peoples-style-detailer-xl-b-pony` — trigger not stated · strength not stated · 2,847 dl · V2.0 new tagging method used · [source](https://civitai.com/models/1378661?modelVersionId=1557746)

**Anima**
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)
  - example prompt (from source, steps 32): `(masterpiece, ultra-HD, best quality, photorealistic, highly detailed, cinematic dramatic lighting), Score_9, score_8, score_7,newest,realistic,photorealism,sharp focus,a` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f99606b1-8a87-452d-8f1b-d7f9bab391ee/original=true/138686019.mp4)
- `realskin-slider-anima` — `realskin slider anima` · strength not stated · 6,621 dl · -1：更平滑、更二次元的皮肤质感  0：接近底模原始效果 +1：更真实的皮肤纹理、材质和光影表现 -1 = flat anime skin  0 = base +1 = realistic skin  · [source](https://civitai.com/models/2682590?modelVersionId=3068784)
- `add-micro-details-concept-v1-anima` — `addmicrodetails` · strength not stated · 5,577 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=3287274)

**Krea2 (detailed-krea2)**
- `krea2_nud3` — trigger not stated · strength `0.7 - 1` (stated) · 24,860 dl · New KREA 2 Version Faceless dataset (doesn't influence face), can be used with character lora easily · [source](https://civitai.com/models/2174081?modelVersionId=3066702)
- `realism-enhancer-krea2` — trigger not stated · strength not stated · 16,530 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2727284?modelVersionId=3065628)
- `Emotions V1` — `Detailed Emotions and Expressions` · strength not stated · 10,258 dl · LEAVE A TIP IF YOU LIKE IT, I AM OUT OF BUZZ!! What it does: - Detailed and mostly accurate emotions · [source](https://civitai.com/models/2829908?modelVersionId=3193133)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
  - example prompt (from source, er_sde, steps 50): `A premium, ultra-realistic cinematic portrait designed as a professional logo named REALISM ENHANCER. Show exactly half of a beautiful Japanese woman's face in an extreme` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7af9ea0-848d-4f42-bdde-f5268ab78f19/original=true/147014892.jpeg)
- `amateur-nudes-flux-wan-2-2-zit-zib-krea2` — `Amateur nudes - FLUX, Wan 2.2, ZIT, (ZIB), Krea2` · strength not stated · 3,474 dl · Added MOSS Image (Base) version, same dataset as usual. Not much to give to this model, samples crea · [source](https://civitai.com/models/764517?modelVersionId=3417654)
- `realistic-nudes-krea2` — `completely nude woman, large breasts, shaved pubic area` · strength not stated · 2,794 dl · LoRA for generating very high-quality Realistic NUDES. Basic Triggers: nude, completely nude, toples · [source](https://civitai.com/models/1838378?modelVersionId=3416536)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1779) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**

### 2. Phone / selfie / amateur-photo look

Pairs with a plain, believable scene description; avoid stacking with cinematic looks.

**Illustrious / NoobAI (Illustrious-XL based)**
- `amateur-style-diffusion-ill` — `amateurQuironn 1girl` · strength `0.7 - 1` (stated) · 4,992 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=1484586)
  - example prompt (from source): `wide shot, natural light, edge lighting, soft lighting.  a cute college student brstgrw woman with medium-length straight auburn hair is   working in an office giving a p` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/03c1e6de-412d-4082-992f-d5fc6dbe8fc2/original=true/138062012.mp4)
- `phone-exposure-juxtaposition-ill` — `phoneExposureQuiron`, `juxtaposition`, `Phone Exposure` · strength `0.7 - 1.3` (stated) · 1,770 dl · 👑 Phone Exposure juxtaposition - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustriou · [source](https://civitai.com/models/1657471?modelVersionId=1876047)
- `bathroom-booty-selfie-pose-sink-butt-influ-ill` — `Bo0ty_s3lfie_p0se` · strength not stated · 272 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705691)

**SDXL**
- `amateur-amateur-professional-photography-xl` — trigger not stated · strength not stated · 283 dl · [source](https://civitai.com/models/2973823?modelVersionId=3370283)
  - example prompt (from source, DPM++ 2M SDE, steps 32): `A portrait of a woman in a dress, natural setting, candid photo  <lora:Amateur_v1:2>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/996443bd-d6b5-44ed-a309-7f0b6e836dff/original=true/144228748.jpeg)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)

**Pony (Pony Diffusion XL)**
- `amateur-style-diffusion-pony` — `amateurQuironStyle`, `amateurQuiron`, `flash photo`, `webcam photo` · strength `0.7 - 1` (stated) · 4,157 dl · 👑 Amateur Style Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious thi · [source](https://civitai.com/models/745518?modelVersionId=833676)
  - example prompt (from source): `The 23 year old man in front   The athletic man behind is performing a handjob. says "fuck I'm cumming". He strokes the penis up and down with his hand. (4 seconds).  The` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c68a4970-904e-4cf6-9be1-3465cb5084ed/original=true/136552947.mp4)
- `trans-girl-selfie-pony` — `tgselfie` · strength not stated · 401 dl · [source](https://civitai.com/models/2006272?modelVersionId=2270821)
- `bathroom-booty-selfie-pose-sink-butt-influ-pony` — `Bo0ty_s3lfie_p0se` · strength not stated · 122 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705669)

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

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [Amateur style - slider](https://civitai.com/models/1410317) (pony, 50,928 dl) — trigger not stated · strength not stated — **downloads 50928 >= 2x best available (5757) in same family+category**
- Suggest ingest: [LEAKCORE (LEAKED NUDES STYLE, Realism, Amateur)](https://civitai.com/models/1439962) (sdxl, 48,422 dl) — `amateur photo`, `film grain`, `face out of frame`, `taking a mirror selfie` · strength `0.7-1.1` (stated) — **downloads 48422 >= 2x best available (3670) in same family+category**

### 3. Cinematic film still look

Pick one look. Do not mix with digicam/amateur LoRAs.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-neo-noir-illustriousxl-zimageturbo-f-ill` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,477 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2078295)
  - example prompt (from source, DPM++ 2M, steps 25): `<lora:ayase_momo-koto-Illustrious v01:0.4> ayasemomo, hair between eyes, crossed bangs, green earrings, brown hair, red eyes, black choker, short hair, white shirt, red b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/edd14fa8-ef5a-4b17-8ed2-392eff3bc892/original=true/92165997.jpeg)
- `Kei Yuri Dirty Pair The Movie ダーティペア - v1.0 - mai_dirty_pair` — `mai_dirty_pair,1980s_\(style\),kei_\(dirty_pair\),dark-skinned_female,`, `mai_dirty_pair,1980s_\(style\),yuri_\(dirty_pair\),long_hair,blue_hair` · strength `0.8` (stated) · 622 dl · Character Set from anime movie "Dirty Pair: The Movie ダーティペア the Movie". This model offers a mini-si · [source](https://civitai.com/models/2840732?modelVersionId=3206701)
- `ain-one-piece-film-z-ill` — `1girl,brown eyes,red eyes,blue hair,long hair`, `epaulettes,cape,jacket on shoulders,uniform,military,military uniform,`, `short hair,bow,cape,cloak,crop top,midriff,shorts,black shorts,short s` · strength not stated · 438 dl · Ain from One Piece Appearance: 1girl,brown eyes,red eyes,blue hair,long hair Outfit 1: epaulettes,ca · [source](https://civitai.com/models/1905653?modelVersionId=2156971)

**Pony (Pony Diffusion XL)**
- `arena-1989-movie-style-pony` — `ar3na1989` · strength not stated · 167 dl · [source](https://civitai.com/models/2105155?modelVersionId=2381613)
  - example prompt (from source, Euler a, steps 28): `Background is space station, lights, bokeh, sci-fi environment, score_9, score_8_up, score_7_up, ar3na1989, 1girl, blonde, cleavage, sagging breasts, long breasts, uneven` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fc5572cb-6590-4c8a-892c-1a6f10d3c85f/original=true/109155866.jpeg)

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

- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**
- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [Cinematic Shot ✨](https://civitai.com/models/432586) (krea2, 62,180 dl) — `zy_cinematic` · strength not stated — **downloads 62180 >= 2x best available (11215) in same family+category**

### 4. Anime / manga / illustration style

One style LoRA at a time; add a second only at a lower strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `figure-anime-xl` — `fig`, `nendo`, `figma` · strength not stated · 7,822 dl · Attempt at anime figure style,  trigger word is "fig"  for nendoroid style is "nendo" Intento de est · [source](https://civitai.com/models/631010?modelVersionId=1284415)
- `super-excessive-cum-huge-bukkake-hentai-an-ill` — `huge_bukkake, bukkake, facials,  sperm, cum, excessive cum, excessive `, `black background, Depth of field, blurred background, black floor,` · strength not stated · 7,221 dl · The learning materials are here. Please feel free to use them. https://mega.nz/file/ckg3VJhD#_ZR69FC · [source](https://civitai.com/models/1853417?modelVersionId=2097518)

**SDXL**
- `anime-figure-xl` — `anifigurestyle` · strength `0.5 to 0.7` (stated) · 792 dl · Trained with SDXL base model, using this lora with other XL models will produce uncontrolled results · [source](https://civitai.com/models/429926?modelVersionId=508307)
  - example prompt (from source, DPM++ 2M SDE Heun, steps 75): `full body, 1girl, nsfw, showing private part, sitting, classroom, upper-class school uniform, doujin cover, reflective, \\o/, drooling, sweat, wet body, climax, (see-thro` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bd5f68aa-d66a-41a3-9b31-84a18f03c358/original=true/12556849.jpeg)

**Pony (Pony Diffusion XL)**
- `uno-makoto-marumiya-pony-xl` — trigger not stated · strength not stated · 1,603 dl · [source](https://civitai.com/models/347454?modelVersionId=388734)
  - example prompt (from source, Euler a, steps 20): `score_9,score_8_up,score_7_up,score_6_up,score_5_up,score_4_up,source_anime,futanari,1girl,solo,futanari,penis,pussy,no testicles,large labia,erection, <lora:unomakotoPon` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3717c1fb-0b5e-436e-a8cc-46fb49317326/original=true/7849168.jpeg)
- `terayama-reiko-anime-golden-boy-ponyxl-sd1-pony` — `Terayama Reiko, 1girl,`, `black hair, long hair, makeup, lipstick, brown eyes,`, `bikesuit,`, `open clothes, no bra, cleavage, unzipped` · strength not stated · 916 dl · XL version · [source](https://civitai.com/models/94159?modelVersionId=770710)
- `ponyxl-concept-anime-figures-pony-2` — `Figure`, `Figma`, `Nendoroid` · strength not stated · 568 dl · Lora of Figma, Nendoroid, and Pop Up Parade anime figures. Please leave a review if you like the mod · [source](https://civitai.com/models/656994?modelVersionId=735071)

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

- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (24024) in same family+category**
- Suggest ingest: [MeMaXL Flat Anime Style - Noob/Illustrious/Pony/XL](https://civitai.com/models/269772) (illustrious, 63,089 dl) — `memaxl6_a`, `memaxl6_b`, `memaxl6_c`, `memaxl6_d` · strength not stated — **downloads 63089 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Vector illustration](https://civitai.com/models/60132) (sdxl, 36,693 dl) — `color icon` · strength `0.65-0.9` (stated) — **downloads 36693 >= 2x best available (3670) in same family+category**

### 5. Retro / decade looks (70s-2000s, VHS, airbrush)

Name the decade in the prompt text as well as the trigger.

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `90s-anime-aesthetic-illustriousxl-zimagetu-ill` — `90s_anime_aesthetic, 1990s (style), retro, retro artstyle` · strength `0.8` (stated) · 5,666 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : 90s_anime_aesthetic, 1990s (style) · [source](https://civitai.com/models/1357076?modelVersionId=1532976)
- `retro-neo-noir-illustriousxl-zimageturbo-f-ill` — `retro_neo_noir, retro, retro artstyle,` · strength `0.8` (stated) · 2,477 dl · Krea 2 version : weight between [0.8,1], best at 1 trigger words : retro_neo_noir, retro, retro arts · [source](https://civitai.com/models/1836542?modelVersionId=2078295)

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

- Suggest ingest: [Pony Amateur ✨](https://civitai.com/models/480835) (pony, 167,639 dl) — `photo`, `grainy`, `amateur`, `lowres` · strength `0.2-0.9` (stated) — **downloads 167639 >= 2x best available (6585) in same family+category**
- Suggest ingest: [2000s Analog Core](https://civitai.com/models/1134895) (krea2, 40,517 dl) — trigger not stated · strength `0.9` (stated) — **downloads 40517 >= 2x best available (11215) in same family+category**
- Suggest ingest: [Retro Big Naturals - Photorealistic Natural Boobs](https://civitai.com/models/86483) (sdxl, 28,943 dl) — `retrobigguns` · strength not stated — **downloads 28943 >= 2x best available (1779) in same family+category**

### 6. Comic, cartoon and western animation

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-comic-random-generator-full-color-i-ill` — `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view, Frame, Text, speech bubble, `, `hcr_generator, (comic:1.25), (Multi view:1.1, Frame, Text, speech bubb` · strength not stated · 24,024 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/585589?modelVersionId=2166652)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a2bb3574-37f0-4d8d-af78-081ebd6cb2a9/original=true/97507964.mp4)
- `hentai-comic-random-generator-hard-core-il-ill` — `fcomichardcore, (comic:1.25),(Multi view, Frame, Text, speech bubble, ` · strength not stated · 16,026 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=2166991)
- `hentai-comic-random-generator-start-story-ill` — `(fcomicstart:2), (1page:2),comic,Multi view, Frame, Text, speech bubbl`, `(fcomicstart:2), (2page:2),comic,Multi view, Frame, Text, speech bubbl`, `(fcomicstart:2), (3page:2),comic,Multi view, Frame, Text, speech bubbl` · strength not stated · 6,780 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=2167446)

**SDXL**
- `sano-comic-xl` — `1girl, aika, blonde hair, medium hair, hair down, hair in ponytail, br` · strength not stated · 32 dl · [source](https://civitai.com/models/3055031?modelVersionId=3474989)
  - example prompt (from source, Euler, steps 25): `1girl, aika, blonde hair, medium hair, hair down, hair in ponytail, brown eyes, stud earrings, necklace, big breats, plump, bubble butt, navy blue bikini, white micro bik` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1486a33d-4bb1-4108-b23a-cc2bd8176a3b/original=true/149214792.jpeg)
- `dizzycartoonstyle-e10-xl` — `dizzycartoonstyle` · strength not stated · 19 dl · [source](https://civitai.com/models/2950113?modelVersionId=3341094)

**Pony (Pony Diffusion XL)**
- `hentai-comic-random-generator-hard-core-il-pony` — `(comic:1.25),(Multi view, Frame, Text, speech bubble, frame, heart, tr` · strength not stated · 27,500 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=657169)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3c92c105-b9a2-4588-860d-1a7ddd63127d/original=true/33485644.jpeg)
- `hentai-comic-random-generator-grayscale-as-pony` — `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, `, `(Grayscale:1.1), (monochrome:1.1),  (comic:1.25), (Multi view, Frame, ` · strength not stated · 8,508 dl · [source](https://civitai.com/models/601268?modelVersionId=672051)
- `hentai-comic-random-generator-start-story-pony` — `(1page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr`, `(2page),(comic),Multi view, Frame, Text, speech bubble, frame, heart, `, `(3page),comic,Multi view, Frame, Text, speech bubble, frame, heart, tr` · strength not stated · 8,308 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/592460?modelVersionId=661873)

**Anima**
- `hentai-comic-random-generator-full-color-i-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text`, `1boy, erection, penis, hetero, sex, rough sex, epic sex, head grab, cu`, `2boys, mmf threesome, erection, penis, multiple penises, testicles, cu` · strength not stated · 10,402 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/585589?modelVersionId=3008158)
  - example prompt (from source): `16 image join 2 Video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1cfb527a-11fb-4716-8c03-3805a76fc585/original=true/133154086.mp4)
- `hentai-comic-random-generator-hard-core-il-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text` · strength not stated · 7,151 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/588622?modelVersionId=3014282)
- `hentai-comic-random-generator-lastpage-fin-anima` — `Hentai comic style. Multi-view with 3-5 or more panels displaying text` · strength not stated · 3,507 dl · ⬇️2026 Anima model⬇️ 📢The prompts for the Anima model and the Illustrious model are different. 🖼️Wid · [source](https://civitai.com/models/594918?modelVersionId=3018129)

**Krea2 (detailed-krea2)**
- `clusterfuck-western-illustration-comic-sty-krea2` — `Illustration` · strength not stated · 1,863 dl · First of all, I don't know what I'm doing really. I just trial and errored my way through dozens of  · [source](https://civitai.com/models/154425?modelVersionId=3084476)
- `dc-sci-fi-krea2` — `DCSC1F1.` · strength not stated · 1,567 dl · v1 krea2raw Trigger = DCS1F1. v1 krea2raw Trained @10,000 Steps, Rank 64, Captioned with GPT4.1, Dat · [source](https://civitai.com/models/2976222?modelVersionId=3373246)
- `FComic1to1000_KR2` — `hentai comic style, comic,  Text, speech bubble, frame, heart, trembli` · strength not stated · 1,248 dl · ⚠️This is KREA 2 (RAW) PROTOTYPE Model 🎉You can now specify arbitrary dialogue within speech bubbles · [source](https://civitai.com/models/2846760?modelVersionId=3214289)

**MOSS (Moss Image / kromoss)**
- `retro-vintage-comics-style-xl` — trigger not stated · strength not stated · 603 dl · This LoRA is trained to reproduce a vintage illustrated comic style, with a focus of detailed line a · [source](https://civitai.com/models/1082272?modelVersionId=3418240)
  - example prompt (from source, er_sde, steps 25): `a woman wearing a silver scifi jumpsuit sneaks around a corner of a castle wall, holding a futuristic handgun. A knight in medieval armor stands on the other side, unawar` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b56519e3-9b2e-4b6d-8aec-b998491f3105/original=true/146267267.jpeg)
- `ag-vassago-flat-cartoon-style-moss` — `V4SS4G0X` · strength `0.6-0.8` (stated) · 337 dl · Ars Goetia is series of loras made on a whim, on variety of images, made from mix of Midjourney, Tum · [source](https://civitai.com/models/2853357?modelVersionId=3431233)
- `cartoon-style-moss` — `c4rt00nbun5, Digital cartoon illustration. The overall style is bold w` · strength not stated · 290 dl · A mixture of different datasets from my MJ style collection for Anima. · [source](https://civitai.com/models/3020107?modelVersionId=3428996)

- Suggest ingest: [Eldritch Comics (comic book style illustration)](https://civitai.com/models/262880) (sdxl, 17,999 dl) — `comic book` · strength not stated — **downloads 17999 >= 2x best available (3670) in same family+category**
- Suggest ingest: [Wizard's Vintage Comic Book Cover](https://civitai.com/models/210095) (sdxl, 17,473 dl) — `Vintage comic book with title text: "xyz"`, `vintage comic book` · strength not stated — **downloads 17473 >= 2x best available (3670) in same family+category**

### 7. Painting, watercolor, oil, sketch, ink

**Illustrious / NoobAI (Illustrious-XL based)**
- `public-bdsm-on-black-toilet-real-anime-cos-ill` — `public bdsm, bdsm, restrained, bondage, shibari, black toilet, black r`, `realistic, photorealistic,`, `spread legs, spread_pussy, close up pussy, detailed pussy, detailed an`, `pov, pov penis, vaginal, deep insertion, Grabing ass, spread mons,` · strength not stated · 2,665 dl · This model generates a cosplayer engaged in public bondage play on top of a black toilet bowl. Can b · [source](https://civitai.com/models/2375147?modelVersionId=2671098)
  - example prompt (from source): `14img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eece9fc8-3599-4066-9116-ad4d4a8a5748/original=true/120359098.mp4)
- `japanese-style-toilet-girl-il-ill` — `((jptoilet)) , ((Thighs buried in wall)), solo, anus, pussy, ((from ab` · strength not stated · 2,304 dl · The learning materials are available here. Please feel free to use them. https://mega.nz/folder/Q0gn · [source](https://civitai.com/models/1899949?modelVersionId=2242138)
- `chines_Ink_painting_IL_MIX` — `wuguanzhong,,zhang daqian,qi baishi, painting \(medium\), traditional ` · strength `1.75-2.5` (stated) · 1,139 dl · Modern_chinese_ink_painting_ILThe Illustrious version of sd1.5(https://civitai.com/models/736379?mod · [source](https://civitai.com/models/1579508?modelVersionId=1787384)

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

- Suggest ingest: [zyd232's Ink Style](https://civitai.com/models/73305) (sdxl, 30,128 dl) — `zydink`, `ink sketch` · strength `0.6 to 1.2` (stated) — **downloads 30128 >= 2x best available (3670) in same family+category**
- Suggest ingest: [ClassipeintXL (oil paint / oil painting style)](https://civitai.com/models/127139) (sdxl, 25,007 dl) — `oil painting` · strength not stated — **downloads 25007 >= 2x best available (3670) in same family+category**

### 8. 3D render / CG / game-art look

**Illustrious / NoobAI (Illustrious-XL based)**
- `queen-s-blade-gamebook-defeats-concept-il-ill` — `qbdefeat, simple background, white background, number Text,  trembling`, `1boy, pov hand, Tearing other clothes, grabbing other clothes, grabbin` · strength not stated · 3,424 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=2166233)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d5873a7a-0bea-4688-9d74-cd6412513433/original=true/97478986.mp4)
- `sinisistar-2-game-emulator-cg-style-2-ill` — `sinistar2, 1 girl, solo focus ,  (gameplay mechanics , fake screenshot`, `sinistar2, 1 girl, solo focus ,  (gameplay mechanics , fake screenshot`, `gangbang, group sex, 2+male, 2+penis, double penetration, veins penis,`, `monster gangbang, group sex, 2+monsters, 2+penis, double penetration, ` · strength not stated · 2,673 dl · ⚠️Please do not submit gory images to CivitAI.⚠️ Plese Set CFG Scale = 4.5 Landscape 1216x832 (Game  · [source](https://civitai.com/models/1992673?modelVersionId=2255524)
- `black-lilith-style-taimanin-asagi-cg-ill` — `bl-tai1` · strength not stated · 729 dl · Recreates the Black Lilith style for the CGs, have fun! · [source](https://civitai.com/models/1295024?modelVersionId=1461566)

**SDXL**
- `soren3d-soren-jones-art-style-il-sd-xl` — `soren3d, 3d,` · strength not stated · 45 dl · Recreates the art style of Soren3D, or Soren Jones. Have fun! · [source](https://civitai.com/models/1458929?modelVersionId=1649912)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, soren3d, 3d, 1girl, handbag, breasts, dress, fishnets, dark skin, jewelry, solo, dark-skinned female, pink dress, bag, hand on hip, panty` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2694b407-16d1-4e6b-a202-6070668a23ea/original=true/69505666.jpeg)

**Pony (Pony Diffusion XL)**
- `queen-s-blade-gamebook-defeats-concept-il-pony` — `(nipple), (pussy), (QB_Defeat:1.25), simple background, white backgrou` · strength not stated · 4,049 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=927214)
  - example prompt (from source, DPM++ 2M Karras, steps 30): `(nsfw), (Uncensored),   (nipple),(pussy),  <lora:QB_Defeat_PONY_V1:1>(QB_Defeat:1.25), simple background, white background, number Text, ((red speech bubble)), trembling,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/26a5eadc-34a2-4960-b2d9-166d9c898593/original=true/33094809.jpeg)
- `black-lilith-style-taimanin-asagi-cg-pony` — `bl-tai1` · strength not stated · 173 dl · Recreates the Black Lilith style for the CGs, have fun! · [source](https://civitai.com/models/1295024?modelVersionId=1461538)
- `banana-games-comic-style-christian-zanier-pony` — `Bananagcz` · strength not stated · 91 dl · Banana Games Comic Style (Christian Zanier) · [source](https://civitai.com/models/1669832?modelVersionId=1890047)

**Anima**
- `queen-s-blade-gamebook-defeats-concept-il-anima` — `qb defeat, qbdefeat, simple background, white background, number Text,`, `1boy, pov hand, Tearing other clothes, grabbing other clothes, grabbin` · strength not stated · 1,626 dl · Basically, don't set quality improvement as a negative!! --Set Negative (Not Sex Toys) ------------- · [source](https://civitai.com/models/829053?modelVersionId=3051558)
  - example prompt (from source): `20image join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a5770782-f115-4488-bf3b-d261e6b19313/original=true/134301561.mp4)
- `MogudanOldStyle_AnimaBaseV10_byKonan` — trigger not stated · strength `0.8-1` (stated) · 977 dl · Trained on Anima with 103 pictures. Best result with weight between : 0.8-1. Reviews are really appr · [source](https://civitai.com/models/2658734?modelVersionId=2985451)
- `x3d-art-style-anima` — `@X3D` · strength `2` (stated) · 731 dl · ***BIG CHANGE*** I'm now fully moved to moss image Incase you didn't get the result as the preview i · [source](https://civitai.com/models/2987218?modelVersionId=3386869)

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
- Suggest ingest: [Illustrious  Pixel Art XL & 1.5 By creativehotia](https://civitai.com/models/43820) (illustrious, 55,968 dl) — `pixel` · strength `1` (stated) — **downloads 55968 >= 2x best available (24024) in same family+category**

### 9. Fantasy, sci-fi, cyberpunk, horror worlds

**Illustrious / NoobAI (Illustrious-XL based)**
- `retro-sci-fi-90-s-anime-style-illustriousx-anima-3` — `retro_artstyle, retro, cyberpunk` · strength `0.8` (stated) · 14,968 dl · Moss version: weight between [0.8,1], best at 1 trigger words : retro_scifi_90s_anime_style, retro_a · [source](https://civitai.com/models/912942?modelVersionId=1021743)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, <lora:mak1ma0XL_Pony_v1:1> , mak1ma0, red hair, long hair, ringed eyes, braid, white collared shirt,b` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/eb702fa4-c13b-4a54-9bfb-d76f6f3032fe/original=true/38017063.jpeg)
- `dark-fantasy-90-s-anime-style-illustriousx-ill` — `dark_fantasy_style, dark fantasy, retro,` · strength `0.8` (stated) · 5,191 dl · Krea 2 version: weight between [0.8,1], best at 1 trigger words : dark_fantasy_style, dark fantasy,  · [source](https://civitai.com/models/1108959?modelVersionId=1245970)
- `tifa-lockhart-final-fantasy-vii-ill` — `1girl,lips,brown eyes,brown hair,black hair,long hair`, `low-tied long hair,thighhighs,gloves,skirt,crop top,suspenders,midriff`, `ponytail,hat,cowboy hat,straw hat,boots,skirt,midriff,gloves,crop top,`, `bangs,swept bangs,breasts,shorts,tank top,bandages,barefoot,large brea` · strength not stated · 1,338 dl · Tifa Lockhart (ティファ・ロックハート) from Final Fantasy VII Appearance: 1girl,lips,brown eyes,brown hair,blac · [source](https://civitai.com/models/2261708?modelVersionId=2545868)

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

- Suggest ingest: [Velvet's Mythic Fantasy Styles / Flux + Pony + illustrious + ZiT + Ani](https://civitai.com/models/599757) (illustrious, 250,565 dl) — `C0lorL1nes` · strength not stated — **downloads 250565 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Popyay's Epic Fantasy Style / Pony & SDXL](https://civitai.com/models/470073) (sdxl, 55,842 dl) — trigger not stated · strength not stated — **downloads 55842 >= 2x best available (3670) in same family+category**
- Suggest ingest: [MGE Monster Girls](https://civitai.com/models/556479) (illustrious, 36,393 dl) — trigger not stated · strength not stated — **downloads 36393 >= 2x best available (9653) in same family+category**

### 10. A specific character or identity

Search `data/loras.jsonl` by the character name (`rg -i name`). Use ONE identity LoRA per person. Adults only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `defeated-waifu-imminent-penetration-concep-ill` — `defeatedwaifu`, `humiliation`, `slave`, `imminent penetration` · strength not stated · 13,616 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/934757?modelVersionId=1335609)
  - example prompt (from source, Euler a, steps 40): `The camera is static and fixed, the girl's eyes move slowly from side to side, she is still chained, her breasts move slowly with her breathing, she is trying to move but` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/db544069-6516-4dd9-b404-b9a207eaf5b7/original=true/101174665.mp4)
- `miniature-mini-girl-and-penis-diffusion-ill` — `MinigirlPenisQuiron`, `minigirl` · strength `0.7 - 2.5` (stated) · 4,089 dl · 👑 Miniature Mini Girl and Penis Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 T · [source](https://civitai.com/models/1421294?modelVersionId=1606496)
- `holli W iIlluLoRA` — `holliw,`, `makeup, blonde hair, bangs, side locks, thick eyebrows, hair between e`, `White Dress, White leotard, see-through, white choker, thigh boots,` · strength not stated · 3,679 dl · 💋 Holli Would from Cool World 🎨 (Anima, NoobAI vPred, Illustrious) She finally exists! 🙌 I've wanted · [source](https://civitai.com/models/269635?modelVersionId=1353398)
- `Coochies_Manager_-_Art_of_Jaguar_v1.0` **[HF repo only - needs adding to Graydient]** — `c00chiesManager, 1girl, white hair, short hair, grey eyes, huge breast`, `white shirt, pencil skirt, necktie, garter straps, thighhighs, side sl` · strength `1.5` (stated) · 95 dl · Diner manager from art of Jaguar. Sometimes you might need to crank up the strength to 1.5 to get re · [source](https://civitai.com/models/2018495?modelVersionId=2284476)

**SDXL**
- `cheetara-sdxl1-0-xl` — `CheetaraQuiron character`, `skintight bodysuit`, `leotard` · strength not stated · 379 dl · 👑 Cheetara Lora👑 SDXL1.0 v4p  Cheetara from Thundercats series 🔧Model base: SDXL1.0 _____________ 📝🌟 · [source](https://civitai.com/models/127430?modelVersionId=139420)
  - example prompt (from source, Euler a, steps 37): `Breathtaking, Hyper detailed, watercolor, ultra highres, 8k, texture skin, realistic skin, detailed skin, highest detailed, extreme detailed, 8k wallpaper, colorful, 1gir` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ed9a1a63-b7d7-4353-9012-02493681fccd/original=true/1997665.jpeg)
- `bbw-plus-sized-curvy-thicc-woman-il-sd-flu-xl` — `bbw-m0del` · strength not stated · 230 dl · Makes a pleasantly plump bbw, have fun! · [source](https://civitai.com/models/1349500?modelVersionId=1524287)
- `big-titty-goth-girl-big-tiddy-goth-gf-flux-xl` — `B1g-t-g0th` · strength not stated · 219 dl · Make your own big titty goth gf, have fun! · [source](https://civitai.com/models/1462381?modelVersionId=1653858)

**Pony (Pony Diffusion XL)**
- `defeated-waifu-imminent-penetration-concep-pony` — `defeatedwaifu`, `humiliation`, `slave`, `imminent penetration` · strength not stated · 7,066 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/934757?modelVersionId=1046362)
  - example prompt (from source, Euler a, steps 40): `score_9, score_8_up, score_7_up, anime_style, 2D, Emilia, 1girl, braid, crown braid, flower, hair flower, hair ornament, hair ribbon, long hair, pointy ears, purple eyes,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/218dc472-dc0c-441b-9a1b-b3a0a6bac1b6/original=true/39333953.jpeg)
- `taimanin-rpgx-character-collection-concept-pony` — `taimanincc, 1 girl, Solo Focus, character profile title text, Simple b` · strength not stated · 2,837 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=618819)
- `sph-curvy-girl-vs-small-penis-with-pinchin-pony` — `small penis, 1girl, 1boy,`, `pinching gesture,`, `gigantic breasts,`, `huge ass,` · strength not stated · 2,178 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1148758?modelVersionId=1292056)

**Anima**
- `taimanin-rpgx-character-collection-concept-anima` — `1girl, white background, character name, character profile, multi-fram`, `((TITLE TEXT:2,"***Character Name***", ***Character Name***))` · strength not stated · 1,535 dl · --SAMPLE <LORA>->Base->CommonWard->Character-- --------------------------------------  <lora:Taimani · [source](https://civitai.com/models/556011?modelVersionId=3051237)
  - example prompt (from source): `6img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/719f0052-19d4-4d89-a2da-1b7c009ece05/original=true/134290489.mp4)
- `glory-wall-anima` — `Promts for this LoRA:`, `bdsm, glory wall, handsfree breast squeeze, immobilization, public res` · strength not stated · 1,047 dl · My telegram chanel: (https://t.me/+-OTXaB0G5F8yNDJi) My discord server: (https://discord.gg/NWpyuzsH · [source](https://civitai.com/models/2897098?modelVersionId=3275413)
- `anastasya-feodorovna-snezhnaya-the-tsarits-anima` — `tsaritsagenshin` · strength `1.0` (stated) · 971 dl · 💬 Discord — join here / 参加はこちら · 🔓 Patreon — new LoRAs 7 days early / 新作LoRAを7日早く · ☕ Ko-fi — suppor · [source](https://civitai.com/models/2875441?modelVersionId=3249316)

**Krea2 (detailed-krea2)**
- `alt-girl-e-girl-krea2` — trigger not stated · strength not stated · 9,378 dl · Trigger word AltGirl · [source](https://civitai.com/models/2274840?modelVersionId=3198266)
  - example prompt (from source, Euler, steps 8): `AltG1rl.A striking, ultra-close-up selfie captures a young woman with intensely vibrant, electric-blue hair styled in long, straight strands that cascade around her face,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d6bd521b-ee7a-4ea0-9b4d-c8db0a0bf5dd/original=true/138751381.jpeg)
- `realisitc-good-girl-krea2` — `rggl` · strength `1-1.25` (stated) · 5,505 dl · (0, 0.25, 0.5, 0.75, 1, 1.25 in lora strength) Hello friends! Let the beautiful girls out! Things To · [source](https://civitai.com/models/2898581?modelVersionId=3277262)
- `krea2_charactersheet_full_v1` — `Follow the prompt template I left in the workflow.` · strength not stated · 3,182 dl · TripleView is a LoRA trained on approximately 300 character sheet samples, with a strong focus on ge · [source](https://civitai.com/models/2764727?modelVersionId=3203877)

**MOSS (Moss Image / kromoss)**
- `luisap-nsfw-tweak-moss` — trigger not stated · strength not stated · 2,092 dl · There no exactly a important use of this lora it's just some custom selection of data that give a su · [source](https://civitai.com/models/3016687?modelVersionId=3424542)
  - example prompt (from source, Euler, steps 12): `This is a photograph of a young woman with light brown skin and long, wavy brown hair. She is positioned on a bed with white sheets in a dimly lit room. The camera angle ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/49dd2f40-804d-4e51-9cc0-aec71bc9eb3f/original=true/146570305.jpeg)
- `malfoid-genderbent-draco-malfoy-meme-chara-moss` — `M4lfoid` · strength not stated · 1,454 dl · Krea 2 and MOSS character LoRA for Malfoid (Genderbent Draco Malfoy). How to use Trigger word: M4lfo · [source](https://civitai.com/models/3021116?modelVersionId=3435645)
- `natural-skin-realism-moss` — `ral-truskin` · strength not stated · 959 dl · 💪Train your own model: https://runpod.io?ref=gased9mt 🍺 Join my discord: https://discord.com/invite/ · [source](https://civitai.com/models/3024665?modelVersionId=3434930)

- Suggest ingest: [NSFW MASTER](https://civitai.com/models/667086) (krea2, 236,423 dl) — trigger not stated · strength `0.8` (stated) — **downloads 236423 >= 2x best available (9378) in same family+category**
- Suggest ingest: [All Disney Princess XL LoRA Model from Ralph Breaks the Internet](https://civitai.com/models/212532) (illustrious, 209,305 dl) — trigger not stated · strength not stated — **downloads 209305 >= 2x best available (13616) in same family+category**
- Suggest ingest: [NiceGirls UltraReal](https://civitai.com/models/1862761) (anima, 161,022 dl) — trigger not stated · strength `0.6-0.8` (stated) — **downloads 161022 >= 2x best available (3480) in same family+category**

### 11. Lighting and atmosphere

Describe a single motivated light source in prose too.

**Illustrious / NoobAI (Illustrious-XL based)**
- `digitaldelights-impossible-downward-dog-ill` — `<Lora:DigitalDelights-impossible-downward-dog:1>, top-down bottom-up, ` · strength not stated · 1,130 dl · Name is self explanatory it's a yoga pose named dog down taking it to the extreme XD · [source](https://civitai.com/models/2143059?modelVersionId=2423989)
  - example prompt (from source, DDIM, steps 30): `masterpiece, best quality, amazing quality, perfect eyes, source_anime, 1girl, solo, <Lora:DigitalDelights-impossible-downward-dog:1>, top-down bottom-up, spread legs, lo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4a1cc040-96ed-4e28-86e1-c2ef6a7f8bc7/original=true/110929135.jpeg)
- `ritsuko-akagi-neon-genesis-evangelion-ill` — `1girl,brown eyes, blonde hair,mole,mole under eye, short hair`, `makeup,breasts,medium breasts,jewelry,earrings,coat,labcoat,open cloth`, `bangs,parted bangs,makeup,red lips,lipstick,earrings,necklace,jewelry,`, `makeup,lipstick,earrings,jewelry,bare shoulders,shirt,sleeveless,belt,` · strength not stated · 900 dl · Ritsuko Akagi from EVA Appearance: 1girl,brown eyes, blonde hair,mole,mole under eye, short hair Lab · [source](https://civitai.com/models/1905245?modelVersionId=2156508)
- `yui-ikari-neon-genesis-evangelion-ill` — `1girl,black eyes,green eyes,brown hair,short hair`, `skirt,labcoat,sleeves rolled up,high heels,pencil skirt,shirt,jewelry,`, `skirt,jewelry,red skirt,long skirt,necklace,sweater,jacket,long sleeve` · strength not stated · 443 dl · Yui Ikari (碇ユイ) from Neon Genesis Evangelion Appearance: 1girl,black eyes,green eyes,brown hair,shor · [source](https://civitai.com/models/2216793?modelVersionId=2495745)

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
- `realistic-night-outdoor-photo-real-streetl-moss` — trigger not stated · strength not stated · 363 dl · Photos taken outdoors at night: bus stops, street food stalls, canal railings, parking lots, rooftop · [source](https://civitai.com/models/3048122?modelVersionId=3465868)
  - example prompt (from source, er_sde, steps 35): `nightoutdoorphoto, a 23-year-old Korean woman wearing a muted red jacket eating a skewer at a street food stall, smiling at the camera, outdoors at night Everyone in the ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/aba86727-6c74-4d60-8302-7357c08a287a/original=true/148742137.jpeg)
- `amish-barn-straw-hats-suspenders-light-thr-moss` — trigger not stated · strength not stated · 187 dl · An Amish farm in Pennsylvania: weathered wide-plank barns, hay, wooden gates, gravel yards, buggies  · [source](https://civitai.com/models/3034848?modelVersionId=3448284)
- `y2k-neon-moss` — trigger not stated · strength not stated · 103 dl · A dreamy millennium neon palette: purple and pink skies, glowing city skylines and reflections on th · [source](https://civitai.com/models/3049556?modelVersionId=3467759)

- Suggest ingest: [S1 Dramatic Lighting](https://civitai.com/models/661736) (illustrious, 63,463 dl) — `s1_dram` · strength not stated — **downloads 63463 >= 2x best available (3749) in same family+category**
- Suggest ingest: [Smooth Lighting Enhancer (NoobAI/Illustrious)](https://civitai.com/models/1204179) (illustrious, 24,842 dl) — trigger not stated · strength `0.5` (stated) — **downloads 24842 >= 2x best available (3749) in same family+category**
- Suggest ingest: [Luke's Neon Clothing and Accessories (Illustrious + Flux + Pony + 1.5 ](https://civitai.com/models/422657) (sdxl, 22,996 dl) — `glowing-neon-colour-clothing`, `blue, green, pink, orange, red, yellow, purple`, `skirt, jacket, shirt, tank top, shorts, hijab, pants, thighhighs, biki` · strength `0.5-0.7` (stated) — **no Graydient LoRA in this family+category**

### 12. Detail / aesthetic / stabilizer enhancers

Use at most one; start low and raise only if the image gets soft.

**Illustrious / NoobAI (Illustrious-XL based)**
- `add-micro-details-concept-ill-2` — `addmicrodetails` · strength not stated · 17,180 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=2832991)
  - example prompt (from source, DPM++ 2M, steps 30): `16k, 8k, 4k, masterpiece, vibrant colours, best quality, ultra detailed, highly detailed, hyper-detailed, realistic BREAK detailed background, night, inside, apartment, v` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/de433dc2-f6c1-4091-8d90-1721f31739e6/original=true/126483189.jpeg)
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)
- `add-micro-details-concept-ill-4` — `addmicrodetails` · strength not stated · 12,040 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=1732142)

**SDXL**
- `trendcraft-the-peoples-style-detailer-base-xl` — trigger not stated · strength not stated · 1,779 dl · Image sources include only Illustrious and NoobAI models. No realistic content. No X or higher rated · [source](https://civitai.com/models/1390819?modelVersionId=1768080)
  - example prompt (from source, DPM++ SDE Karras, steps 30): `macro photo, sparkling magical fantasy glass flower dewdrop, very detailed, amazing quality, intricate, cinematic light, highly detail, beautiful, surreal, dramatic, gala` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2e8e174e-ec63-47f4-97b0-e432615c1632/original=true/75267901.jpeg)
- `zoda-nsfw-detailer-xl` — trigger not stated · strength `0.5 - 1.0` (stated) · 1,373 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=2137316)
- `trendcraft-the-peoples-style-detailer-base-xl-v2-1a-sdxl-3-12` — trigger not stated · strength not stated · 836 dl · Trained on SDXL base.  Used a lower tagging threshold compared to Pony XL v2.0. Solid improvement co · [source](https://civitai.com/models/1390819?modelVersionId=1571948)

**Pony (Pony Diffusion XL)**
- `trendcraft-the-peoples-style-detailer-xl-b-pony` — trigger not stated · strength not stated · 2,847 dl · V2.0 new tagging method used · [source](https://civitai.com/models/1378661?modelVersionId=1557746)
  - example prompt (from source, Euler a, steps 25): `embedding:lazyup, masterpiece, 1girl, solo, beautiful blue eyes, Covered in Tattoos, her hand on her head, brushing hair behind ear,  Tanktop, cutoff, choker,  On a Cliff` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3c38bc55-8107-4dfc-94d6-7ad3dc2d66c3/original=true/64724055.jpeg)
- `add-micro-details-concept-pony-3` — `addmicrodetails` · strength not stated · 2,703 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=1961984)
- `add-micro-details-concept-pony-4` — `addmicrodetails` · strength not stated · 2,292 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=1673119)

**Anima**
- `hentai-studio-quality-illustriousxl-zimage-anima` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 12,234 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=2814440)
  - example prompt (from source, er_sde, steps 30): `hentai_studio_quality, shiny skin, 1girl, solo, alone, elf, pointy ears, looking at the viewer, bikini, beach, sand, sea, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/236c9bf2-520d-4663-8751-d9324aa5d085/original=true/125784086.jpeg)
- `zoda-nsfw-detailer-anima` — trigger not stated · strength `0.5 - 1.0` (stated) · 8,276 dl · v3_illustrious have 2 files: zoda_v3_illu_hires.safetensors (435MB, Hi-Res version , default option) · [source](https://civitai.com/models/1879987?modelVersionId=3130764)
- `add-micro-details-concept-v1-anima` — `addmicrodetails` · strength not stated · 5,577 dl · Recommended settings: Steps: 25-40 CFG scale: 5-7 Strength – Varies (Sometimes it's hard to tell whi · [source](https://civitai.com/models/1377820?modelVersionId=3287274)

**Krea2 (detailed-krea2)**
- `realism-enhancer-krea2` — trigger not stated · strength not stated · 16,530 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2727284?modelVersionId=3065628)
  - example prompt (from source): `a woman seated outdoors, looking to the side with her left hand raised to adjust oversized tortoiseshell sunglasses, wearing a sheer long-sleeved blouse with a painterly ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/696c960e-2bf4-4561-a744-51b29097fc70/original=true/134723086.jpeg)
- `Emotions V1` — `Detailed Emotions and Expressions` · strength not stated · 10,258 dl · LEAVE A TIP IF YOU LIKE IT, I AM OUT OF BUZZ!! What it does: - Detailed and mostly accurate emotions · [source](https://civitai.com/models/2829908?modelVersionId=3193133)
- `zy_BackgroundDetail_K2` — trigger not stated · strength `0.1-0.75` (stated) · 4,723 dl · ✨REFERRAL CODE: DMD9XGMN ℹ️ Model Overview This LoRA enhances the background of the image, adding mo · [source](https://civitai.com/models/633524?modelVersionId=3211112)

**MOSS (Moss Image / kromoss)**
- `realism-enhancer-moss` — trigger not stated · strength `1` (stated) · 7,118 dl · Realism Enhancer is a full LoRA, not a slider. It was trained exclusively on high quality, 2048px pl · [source](https://civitai.com/models/3023438?modelVersionId=3433342)
  - example prompt (from source, er_sde, steps 50): `A premium, ultra-realistic cinematic portrait designed as a professional logo named REALISM ENHANCER. Show exactly half of a beautiful Japanese woman's face in an extreme` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f7af9ea0-848d-4f42-bdde-f5268ab78f19/original=true/147014892.jpeg)
- `pornmaster-moss-detail-slider-xl` — trigger not stated · strength not stated · 4,239 dl · 模型介紹為中英雙語，中文使用者可以關閉翻譯。 PornMaster 色情大師 Moss Lora權重: -6 to +8 使用正面lora權重時增加增細節，使用負面lora權重時降低細節。 LoRA  · [source](https://civitai.com/models/3010274?modelVersionId=3416145)
- `hentai-studio-quality-illustriousxl-zimage-moss` — `hentai_studio_quality, shiny skin,` · strength `0.8` (stated) · 2,393 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=3420914)

- Suggest ingest: [Detail Tweaker XL](https://civitai.com/models/122359) (sdxl, 465,671 dl) — trigger not stated · strength not stated — **downloads 465671 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Realistic Skin Texture style (Detailed Skin) XL + SD1.5 + F1D + Pony +](https://civitai.com/models/580857) (illustrious, 195,529 dl) — `sharp`, `detailed`, `cinematic style`, `cinematic photography style` · strength not stated — **downloads 195529 >= 2x best available (17180) in same family+category**
- Suggest ingest: [Stabilizer IL/NAI/CK](https://civitai.com/models/971952) (illustrious, 161,491 dl) — trigger not stated · strength not stated — **downloads 161491 >= 2x best available (17180) in same family+category**

### 13. Turbo, distill and speed LoRAs

Only on a matching fast/turbo workflow; never stack with a full-step look at high strength.

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-studio-quality-illustriousxl-zimage-ill` — `hentai_studio_quality, shiny skin` · strength `0.8` (stated) · 12,347 dl · Moss version: weight between [0.8,1], best at 1 prompt : hentai_studio_quality, shiny skin Krea 2 ve · [source](https://civitai.com/models/1459030?modelVersionId=1649913)
  - example prompt (from source, DPM++ 2M, steps 25): `1girl, solo, alone, angel, wings, looking at the viewer, bikini, <lora:hentai_studio_quality-000013:1>, hentai_studio_quality, shiny skin, masterpiece, highres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cdb4ed61-bb72-4655-9dd9-05cbe2f37f48/original=true/69610834.jpeg)
- `hyper-huge-gape-xl` — `HyperAGapeQuiron`, `extreme anal gape`, `extreme gape` · strength `0.7 - 1.5` (stated) · 4,602 dl · 👑 Hyper A Gape Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 This LORA is capab · [source](https://civitai.com/models/109087?modelVersionId=1632779)
- `hyper-huge-gape-diffusion-sd1-5-ill` — `hugeanusGapeQuiron`, `gaping`, `anal gape` · strength `0.7 - 1` (stated) · 1,264 dl · 👑 Hyper A Gape Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 This LORA is capab · [source](https://civitai.com/models/109087?modelVersionId=1489482)

**SDXL**
- `hyperpregnant-hyperpregnancy-il-sd-xl` — `hyperpregnant, huge belly` · strength not stated · 110 dl · Makes characters extremely pregnant, have fun! · [source](https://civitai.com/models/1703222?modelVersionId=1927565)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, 4k, masterpiece, highly detailed, hyperpregnant, huge belly, 1girl, breasts, animal ears, playboy bunny, rabbit ears, pantyhose, solo, pr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a9f8aae8-e160-44e8-a6cb-379429bec7e2/original=true/83756244.jpeg)

**Pony (Pony Diffusion XL)**
- `hyper-huge-gape-diffusion-sd1-5-pony` — `hugeAnusGapeQuiron`, `anal gape`, `hyper anus gape`, `gaping` · strength `0.7 - 1.5` (stated) · 5,757 dl · 👑 Hyper A Gape Diffusion - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious ✅ ✔️ 💬 This LORA is capab · [source](https://civitai.com/models/109087?modelVersionId=1006302)
  - example prompt (from source): `gape lora` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ea967ae0-cc88-434a-9321-7c44fa9e3a4f/original=true/99198490.mp4)
- `Kissing Fetish Hyperlips Kissing Concept LoRA - v1.0 - Kissing_Fetish__Hyperlips_Kissing_Concept_LoRA-000039` — `Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy,` · strength not stated · 1,183 dl · [source](https://civitai.com/models/1162938?modelVersionId=1308166)
- `hyper-gape-pussy-pony` — `pussy gape`, `hyper gape pussy`, `pussy focus` · strength not stated · 254 dl · [source](https://civitai.com/models/2948213?modelVersionId=3338733)

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
- `mature-slider-ill` — trigger not stated · strength not stated · 6,612 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2118055?modelVersionId=2396030)

**SDXL**
- `thick-xl-thin-thick-body-build-slider-xl` — trigger not stated · strength not stated · 369 dl · [source](https://civitai.com/models/2893137?modelVersionId=3271132)
  - example prompt (from source): `A side-by-side two-panel full-length editorial photography reference sheet featuring the same 30-year-old woman in two views.  LEFT PANEL: straight-on frontal view, facin` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2f832f4f-1b0c-4e3e-9ebc-6d261001fdd5/original=true/147621697.mp4)
- `bewbs-breast-size-slider-xl` — trigger not stated · strength not stated · 265 dl · [source](https://civitai.com/models/2947454?modelVersionId=3337780)
- `sheer-clothing-transparency-slider-xl` — trigger not stated · strength not stated · 140 dl · [source](https://civitai.com/models/2911617?modelVersionId=3293497)

**Pony (Pony Diffusion XL)**
- `abs-slider-pony` — trigger not stated · strength `0 to 2` (stated) · 867 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2513137?modelVersionId=2879098)
  - example prompt (from source, Euler a, steps 25): `score_9_up, score_7_up, 1girl, bikini,   <lora:AbsSlider_Pony2:0>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/30a97687-5968-414f-bbb2-8718648c9264/original=true/128174904.jpeg)
- `muscle-slider-pony` — trigger not stated · strength `0 to 2` (stated) · 589 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2518673?modelVersionId=2881011)
- `breasts-slider-pony` — trigger not stated · strength not stated · 381 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2100839?modelVersionId=3196135)

**Anima**
- `Breasts slider - Anima - Breasts_Size_SliderAnima6` — trigger not stated · strength not stated · 13,445 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2100839?modelVersionId=2974098)
  - example prompt (from source, Euler a, steps 25): `masterpiece, 1girl, solo, looking at viewer,  straight-on, arms at sides,  blue bikini,  blonde hair, blue eyes, white background,   <lora:Breasts_Size_SliderAnima6:-2>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b57f5a72-59b7-4310-85b8-8d4a203132c0/original=true/131718491.jpeg)
- `Mature slider - Anima - MatureFemaleSliderAnima` — trigger not stated · strength not stated · 11,760 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2118055?modelVersionId=2979797)
- `breasts-gravity-slider-perky-sagging-breas-anima` — trigger not stated · strength not stated · 7,541 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2533936?modelVersionId=2974276)

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
- `foot-on-breasts-step-on-breasts-trampling-xl` — `St3pping_on_breast, foot on breast, breast trample, stepping, foot, st` · strength not stated · 83 dl · Steps on her breasts, have fun! · [source](https://civitai.com/models/2486225?modelVersionId=2795252)

**Pony (Pony Diffusion XL)**
- `grabbing-breasts-pony` — `grabbing breasts` · strength not stated · 7,694 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=705069)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `score_9, score_8_up, score_7_up,source_anime, high res image,masterpiece,best quality,girl,cute face,clear skin,shiny hair,ultra detailed eyes,simple background, <lora:gr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5735d32b-9e04-4efe-a046-28e7c514fb81/original=true/23256428.jpeg)
- `small-saggy-breasts-pony` — trigger not stated · strength not stated · 3,700 dl · [source](https://civitai.com/models/704319?modelVersionId=947120)
- `pose_femdom_handjobfrench_kiss_nipple_tweak - v1.0 - pose_handjob_french_kiss_nipple_tweak` — `handjob_french_kiss_nipple_tweak, score_9, nipple stimulation, nipple ` · strength not stated · 3,678 dl · [source](https://civitai.com/models/905481?modelVersionId=1013259)

**Anima**
- `nipple-anima-2` — `nipples` · strength `0.6–0.8` (stated) · 7,807 dl · [MOSS] The usage is the same as Anima. Forge Neo: The effect of Adetailer is a bit weak. Turbo: It m · [source](https://civitai.com/models/2385403?modelVersionId=3036905)
  - example prompt (from source, Euler a, steps 28): `masterpiece, best quality, score_7, highres, absurdres, explicit, 1girl, solo, perky breasts, natural breasts, breasts out, breast focus, nipples, Unamused, upper body, <` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/698868c5-aadc-4758-87c2-eb47919bbe22/original=true/133892044.jpeg)
- `grabbing-breasts-anima` — `grabbing breasts` · strength not stated · 3,829 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/630699?modelVersionId=2933804)
- `nipple-v6631-anima` — `nipples` · strength `0.6–0.8` (stated) · 2,928 dl · [MOSS] The usage is the same as Anima. Forge Neo: The effect of Adetailer is a bit weak. Turbo: It m · [source](https://civitai.com/models/2385403?modelVersionId=2966631)

**Krea2 (detailed-krea2)**
- `breasts-helper-v1-krea2` — `HMBreasts` · strength `0.9` (stated) · 7,142 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2740401?modelVersionId=3081828)
  - example prompt (from source): `HMBreasts, Candid shot of a medium-build, fair-skinned woman with curly light brown hair, standing in a hallway with her denim jacket off both shoulders and nothing benea` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c2870f8a-0f6a-44bd-b184-121757161acd/original=true/135241803.jpeg)
- `ski-slope-breasts-mh3-ani-kr2-zit-f1d-pny-krea2` — `SteepSlopeTiddies` · strength `1.10` (stated) · 6,701 dl · Moss XXL / MH3 XXL / Ani XXL / Krea2 XXL / ZiT XXL / ZiT 1.2 / F1D XXL / F1D 1.2 / PNY 1.2 / ILL 1.2 · [source](https://civitai.com/models/942483?modelVersionId=3112303)
- `sbbt-small-build-big-tits-krea2` — `SBBT` · strength not stated · 5,983 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2811208?modelVersionId=3170283)

**MOSS (Moss Image / kromoss)**
- `tiny-tits-small-breasts-v0297-krea2` — `tyneetitpn` · strength `1.15` (stated) · 10,662 dl · MOSS Small breasts puffy nipples Best strength for me was around 1.15.  Trigger: tyneetitspn Some sa · [source](https://civitai.com/models/2733121?modelVersionId=3440297)
- `moss-natural-breasts-xl` — trigger not stated · strength `0.8–1.0` (stated) · 2,420 dl · Natural Breasts — for MOSS Image A small, focused LoRA for natural breast shape on MOSS-Image. It do · [source](https://civitai.com/models/3010783?modelVersionId=3416833)
- `massive-realistic-breasts-macromastia-moss` — trigger not stated · strength not stated · 1,228 dl · ⚠️ An Important Personal Note & The Reality of Future Models I want to be completely transparent wit · [source](https://civitai.com/models/3033173?modelVersionId=3446172)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [Sagging Breasts](https://civitai.com/models/139131) (illustrious, 89,056 dl) — `sagging breasts`, `breasts apart` · strength `1.0` (stated) — **downloads 89056 >= 2x best available (10931) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**

### 16. Penis, scrotum and futa anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `penis-size-difference-ill` — `PSDER, penis size difference, penis, (2boys:1.7), 1girl,  small penis,` · strength `0.6-1.0` (stated) · 8,863 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=1245271)
  - example prompt (from source, Euler a, steps 20): `masterpiece,best quality, (flat style, one piece style, anime style, anime screencap, crossover, artist:kittew:0.5,artist:ratatat74:0.3), PSDER, penis size difference, pe` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/6ba92e14-f6b0-4b17-b42e-4cdf5afb6ec9/original=true/49763219.jpeg)
- `Small Penis - Feminization - SPH - Illustrious - cute_v1.5` — `cute_penis` · strength not stated · 7,251 dl · Twice the gurls and even daintier bits! I've updated the first concept model I created. I incorporat · [source](https://civitai.com/models/1514972?modelVersionId=1738881)
- `Futa_on_male-000055` — `futa on male, futa with male, 1girl, 1boy, futanari,`, `sex, sex from behind,`, `lying,` · strength not stated · 5,526 dl · The most popular and requested LoRA. Comment or message me to let me know what to create next. I mak · [source](https://civitai.com/models/891832?modelVersionId=2066157)

**SDXL**
- `futanari-pegging-male-hassaku-v1-xl` — `Futa_Pegging_Male`, `futa on male, futa pegging male, anal sex,` · strength not stated · 2,769 dl · [source](https://civitai.com/models/790941?modelVersionId=884496)
  - example prompt (from source, Euler a, steps 40): `score_9, score_8_up, score_9, score_8, 1futanari, 1boy, (Futa_Pegging_Male:1.5), anime style, futa on male, futa pegging male, anal sex, hentai, girl with red hair, boy w` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f72df470-4ffe-435f-96e8-935eef51c769/original=true/30992240.jpeg)
- `all-in-one-lying-on-back-female-male-futa-xl` — trigger not stated · strength not stated · 2,306 dl · [source](https://civitai.com/models/810132?modelVersionId=905931)
- `male-blowing-futanari-hassaku-xl` — `Futa_Blowing_Male`, `blowjob`, `futa on male` · strength not stated · 1,707 dl · [source](https://civitai.com/models/769133?modelVersionId=860275)

**Pony (Pony Diffusion XL)**
- `ponyillustrious-futa-xl` — `futa with female, 1futa, breasts, 2girls`, `sex,`, `fellatio,`, `vaginal,` · strength not stated · 5,919 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1107758?modelVersionId=1254269)
  - example prompt (from source, Euler a, steps 30): `safe_pos, score_9, score_8_up, score_7_up, futa with female, 1futa, breasts, 2girls, sex, vaginal` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/688fe610-4d5d-405e-8b2e-abf922daa94e/original=true/50245211.jpeg)
- `hentai-futanari-girls-sex-random-generator-pony` — `(2 girls:1.1),(2 penises:1.1), futanari, futa, (futa with futa:1.1), y` · strength not stated · 4,188 dl · [source](https://civitai.com/models/589732?modelVersionId=658463)
- `futa-ntr-ver-2-pony` — `futa ntr`, `3girls`, `watching`, `netorare` · strength not stated · 4,169 dl · [source](https://civitai.com/models/401443?modelVersionId=447620)

**Anima**
- `concept-wet-penis-saliva-pussy-juice-anal-anima` — `pussy juice on penis`, `saliva on penis`, `anal fluid on penis` · strength not stated · 2,764 dl · This is an experimental initial release. This LoRA focuses specifically on coating the penis with va · [source](https://civitai.com/models/2627734?modelVersionId=3222610)
  - example prompt (from source, er_sde, steps 12): `bar censor, censored,  solo focus, hetero,  wet penis, saliva on penis, after fellatio, veiny penis, (penis on head:1.2), penis on cheek, drooling,  open mouth, saliva, s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0b28a388-4726-4da0-bfeb-20a4924f3030/original=true/139515743.jpeg)
- `penis-size-difference-anima` — `penis size difference` · strength `0.6-1.0` (stated) · 2,479 dl · So this is a Lora for pictures, there a girl have two choices but we all know the answer. Activation · [source](https://civitai.com/models/475453?modelVersionId=3027209)
- `futa-foreskin-taker-pov-anima` — `fftaker` · strength `0.5-1` (stated) · 1,911 dl · Futa Taker POV: a shot in which the viewer is implied to be the subject of the a futa's penis. Mostl · [source](https://civitai.com/models/138423?modelVersionId=3113463)

**Krea2 (detailed-krea2)**
- `femboy-shemale-flaccid-or-small-penis-krea2` — `femboy shemale flaccid or small penis krea2` · strength `1.0` (stated) · 5,728 dl · v Krea 2 Krea version 2 works without any bypass LoRAs or similar censorship modifications. It uses  · [source](https://civitai.com/models/2054525?modelVersionId=3096065)
  - example prompt (from source, Euler, steps 10): `Close-up photo of tiny flaccid penis and scrotum, visible from front, of young pretty woman who wearing pink bikini, her pink thong are moved aside by her hand. Ocean bea` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/59fb4e2b-4566-42b0-9d7e-076b33a042c9/original=true/135665457.jpeg)
- `hmcockface-cock-on-face-krea2` — `HMCockFace` · strength `0.9` (stated) · 4,173 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2753674?modelVersionId=3098191)
- `krea2_equine_penis_0807` — `equine penis, urethral`, `canine penis, penis tip` · strength not stated · 4,131 dl · Primary training objective: equine penis. To avoid severe overfitting in other areas—such as acciden · [source](https://civitai.com/models/2843146?modelVersionId=3209760)

**MOSS (Moss Image / kromoss)**
- `flaccid-vtx-flaccid-uncut-penis-moss` — `flaccid penis` · strength not stated · 1,143 dl · Not sure if I like MOSS over Krea 2 for photorealism, but it's really fast and can do a wider variet · [source](https://civitai.com/models/3008280?modelVersionId=3413532)
  - example prompt (from source, Euler, steps 16): `A high-quality studio photograph of a handsome Caucasian man in his late twenties with a fit, athletic, well-developed physique. He stands centered in the frame against a` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5a3cb833-7154-4870-959d-48f591bf6c57/original=true/146042480.jpeg)
- `f-ing-dick-moss` — trigger not stated · strength not stated · 1,058 dl · Note: You can significantly improve the quality by using a BBOX (Bounding Box) to show the model whe · [source](https://civitai.com/models/3014843?modelVersionId=3422079)
- `prepuce-foreskin-moss` — `pr3puc3`, `prepuce foreskin on tip of penis` · strength not stated · 649 dl · first MOSS lora, still getting the hang of it. If you like my work, please consider purchasing early · [source](https://civitai.com/models/3022195?modelVersionId=3431777)

- Suggest ingest: [Nipples XL](https://civitai.com/models/171014) (sdxl, 73,706 dl) — `oval nipples`, `puffy nipples`, `dark nipples`, `ghost nipples` · strength not stated — **downloads 73706 >= 2x best available (1707) in same family+category**
- Suggest ingest: [[PonyXL/ILXL] Pull out Penis Cumtrail](https://civitai.com/models/467896) (illustrious, 40,651 dl) — `cum string, cumtrail, solo focus`, `cumtrail vagina to penis, , after sex, pulling out penis, cum on penis`, `cumtrail mouth to penis, , pulling out penis, after oral, after ferrat`, `cumtrail breast to penis, , pulling out penis, after paizuri, cum on b` · strength not stated — **downloads 40651 >= 2x best available (10931) in same family+category**
- Suggest ingest: [Penis Worship](https://civitai.com/models/514556) (illustrious, 39,536 dl) — `penis worship`, `heart-shaped pupils`, `penis on face`, `penis on head` · strength `0.4 - 0.6` (stated) — **downloads 39536 >= 2x best available (10931) in same family+category**

### 17. Vulva, vagina and anus anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `mating-press-wide-spread-focus-right-befor-ill` — `mating press`, `focus` · strength `1` (stated) · 13,255 dl · 💖 Support & Share the Magic!  Love these tools? Like, add to collection, and tag this resource in yo · [source](https://civitai.com/models/1280616?modelVersionId=1444772)
  - example prompt (from source, Euler a, steps 30): `mating press, 1girl, 1boy, female focus, long hair, breasts, looking at viewer, blush, open mouth, large breasts, red eyes, nipples, ass, hetero, sweat, nude, lying, peni` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a7ebf604-1e2e-4185-8b39-c9ac4fe89815/original=true/59279931.jpeg)
- `pussy-juice-ill` — `pussy juice` · strength not stated · 10,931 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=1135306)
- `hentai-pussy-inspection-2shot-il-2-ill` — `hpi2, 1 girl, full body, cowboy shot, Clothed girl and nude girl, Cove` · strength not stated · 10,634 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=2113370)
- `Marie-PussyPlayground_2_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link
- `Marie-PussyPlayground_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `gaping-assholes-all-fours-sdxl1-0-concept-xl` — `GapingAssholesAllFourQuiron pose`, `all fours`, `from behind`, `spread ass` · strength not stated · 7,022 dl · 👑 Gaping Assholes All Fours LORA 👑 SDXL1.0 v5.1p 🔧Model base: SDXL1.0 📝🌟 Trigger: (GapingAssholesAll · [source](https://civitai.com/models/130866?modelVersionId=143716)
  - example prompt (from source, Euler a, steps 40): `photo, 8k portrait of beautiful cyborg with brown hair, intricate, elegant, highly detailed, majestic, digital photography, art by artgerm and ruan jia and greg rutkowski` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/40ea32da-742e-4d42-a3d4-65d168412e6a/original=true/2099450.jpeg)
- `all-in-one-lying-on-back-female-male-futa-xl` — trigger not stated · strength not stated · 2,306 dl · [source](https://civitai.com/models/810132?modelVersionId=905931)
- `Hentai_Pussy_inspection2_SDXL` — `Hentai_Pussy_inspection2`, `(wearing clothes, clothes cover body:1.5)`, `solo, multiple views, close-up, looking at viewer, cowboy shot, nude, ` · strength not stated · 1,554 dl · [source](https://civitai.com/models/1662102?modelVersionId=1881250)

**Pony (Pony Diffusion XL)**
- `hentai-pussy-inspection-2shot-il-2-pony` — `solo, multiple views, close-up, looking at viewer, cowboy shot, nude, `, `(Multiple layers),solo, full body, cowboy shot, standing, sweat, oily ` · strength not stated · 11,319 dl · Illustrious version is completely new and re-created version. The learning materials are available h · [source](https://civitai.com/models/573817?modelVersionId=639693)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/755c54b3-86c3-4195-9ee7-da89000171ee/original=true/33529329.jpeg)
- `pussy-juice-pony` — `pussy juice` · strength not stated · 9,912 dl · The strength of Lora is recommended to be around 1.0. It is assumed that it is in a drooping state. · [source](https://civitai.com/models/540855?modelVersionId=601324)
- `anal-side-missionay-anal-pony` — `sideMissionayAnalQuiron`, `sideMissionayAnal` · strength not stated · 8,236 dl · 👑 Anal Side Missionay Anal - PONY - LORA 👑 ⚙️🔧Model base: SDXL - Pony ______________ 📝🌟 Trigger: sid · [source](https://civitai.com/models/168340?modelVersionId=981838)
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
- `anus-grip-moss` — trigger not stated · strength not stated · 1,009 dl · A simple LoRa for helping generation of anus gripping. Use with strenght 0.6-1. No trigger just natu · [source](https://civitai.com/models/3031362?modelVersionId=3470241)

- Suggest ingest: [Labiaplasty Innie Pussy Adjuster [KR2 K9B ZImage SDXL Qwen Chroma SD1]](https://civitai.com/models/112299) (krea2, 176,773 dl) — trigger not stated · strength not stated — **downloads 176773 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Lily](https://civitai.com/models/86788) (sdxl, 99,961 dl) — `pussy_front`, `pussy_rear`, `toys_front`, `toys_rear` · strength not stated — **downloads 99961 >= 2x best available (1707) in same family+category**
- Suggest ingest: [Real Pussy - Peach](https://civitai.com/models/99174) (sdxl, 87,846 dl) — `pussy_scale1`, `pussy_scale2`, `pussy_scale3` · strength not stated — **downloads 87846 >= 2x best available (1707) in same family+category**

### 18. Hands, feet, face and small anatomy

**Illustrious / NoobAI (Illustrious-XL based)**
- `hentai-pussy-inspection-gaping-pussy-opene-ill` — `(gaping pussy opened in fingers),(Put fingers in Vagina), (spread Vagi`, `(close-up clitoris), (close-up layers:1.2),(Multiple layers:1.2), (mul` · strength not stated · 5,194 dl · Inspection out Your WIFE's PUSSY!! Width:832 Height:1216 is best Width:1216 Height:832 is best SAMPL · [source](https://civitai.com/models/870724?modelVersionId=2165255)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3d389cb4-469c-452b-ac92-6621fdd7efcd/original=true/97420279.mp4)
- `two-finger-handjob-crotch-pov-pinching-han-ill` — `tf handjob, crotch pov, penis, male pov,`, `1girl,`, `blowjob, fellatio,`, `ejaculation,` · strength not stated · 3,951 dl · Version 1, kind of sucks. Version 2, actually functional this time. Recommend you use hand negative. · [source](https://civitai.com/models/853056?modelVersionId=1444623)
- `ohho-eyes-nsfw-oho-eye-xl-ill` — `ohho-eyes,  half-close one eye halfway,  Wide-open one eye , heart in `, `pov,pov sex,girl on top,femdom,`, `pov, pov penis, hand job,` · strength not stated · 3,471 dl · The learning materials are here. Please feel free to use them. https://mega.nz/folder/Yoh2SJYR#ZYu3s · [source](https://civitai.com/models/1881720?modelVersionId=2202093)

**SDXL**
- `cumface-xl` — `facial`, `cumface` · strength not stated · 1,094 dl · [source](https://civitai.com/models/1382629?modelVersionId=1562351)
  - example prompt (from source, Euler a, steps 35): `score_7_up, 1girl, close up, dark hair, bangs, messy hair, hetero, facial, cumface, pretty, gorgeous girl, lashes, shy, neck, selfie, large breasts, tank top, wet spot, s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/43987d6e-959e-4a41-9e9c-86019b62e6b9/original=true/64945366.jpeg)
- `push-head-down-face-against-floor-il-sd-xl` — `Face in pillow`, `push head down, hand on another's head` · strength not stated · 488 dl · [source](https://civitai.com/models/1726270?modelVersionId=1953666)
- `ohogao-o-face-ahegao-il-sd-xl` — `ohogao,  puckered lips, trembling, tearing up,  v-shaped eyebrows, rol` · strength not stated · 302 dl · Ohogao is a type of ahegao orgasm face where the mouth is in an ovular O shape with puckered lips, s · [source](https://civitai.com/models/1896670?modelVersionId=2147030)

**Pony (Pony Diffusion XL)**
- `hentai-pussy-inspection-gaping-pussy-opene-pony` — `(dilation Vagina),(Put fingers in Vagina), (spread Vagina wide), (Perf` · strength not stated · 5,112 dl · Inspection out Your WIFE's PUSSY!! Width:832 Height:1216 is best Width:1216 Height:832 is best SAMPL · [source](https://civitai.com/models/870724?modelVersionId=974577)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/be0c3a9b-f287-47dd-9d27-8e1650add4df/original=true/35523008.jpeg)
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
- `Kissing Fetish Hyperlips Kissing Concept LoRA - v1.0 - Kissing_Fetish__Hyperlips_Kissing_Concept_LoRA-000039` — `Kissing Fetish, Hyperlips Kiss, Forced Kiss, Femdom, 1girl, 1boy,` · strength not stated · 1,183 dl · [source](https://civitai.com/models/1162938?modelVersionId=1308166)
- `MCB_hands_pony_epoch_10` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**Anima**
- `lips-size-slider-anima` — trigger not stated · strength `0 to 2` (stated) · 3,339 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2533131?modelVersionId=3044145)
  - example prompt (from source, Euler a, steps 24): `masterpiece, 1girl, solo, looking at viewer, closed mouth, upper body, black hair, black eyes, long hair, white background,    <lora:Lip-thickness-slider-Anima3:0>` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2b11dced-d9ae-4bcc-bf56-fa135c3a95c8/original=true/134078807.jpeg)
- `_feet_epoch_10` — `@feet, feet, toes, soles, tonails, whatever else` · strength not stated · 2,756 dl · Enjoy and share results! Suggestion Box (Higher chance of getting what you want if you attach an ima · [source](https://civitai.com/models/1293552?modelVersionId=3103124)
- `basic-hands-improvement-anima` — `perfect hands` · strength `0.7` (stated) · 2,640 dl · This is my personal (barely working) attempt to improve the hands and fingers, so please don't expec · [source](https://civitai.com/models/2783311?modelVersionId=3134960)

**Krea2 (detailed-krea2)**
- `hmcockface-cock-on-face-krea2` — `HMCockFace` · strength `0.9` (stated) · 4,173 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2753674?modelVersionId=3098191)
  - example prompt (from source): `HMCockFace, POV close-up of a slim brunette with loose dark hair, a hard cock resting flat on her cheek, the shaft pressed against her skin. She is looking up at the came` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c18602c1-f8c1-4d66-ad46-7a750189abd1/original=true/135725699.jpeg)
- `krea2 sex 淫模 - FJ - krea2 footjob` — `krea2fotjob, footjob, 1girl, fishnets, feet, hetero, penis, 1boy, pant` · strength `0.6–0.7` (stated) · 3,299 dl · If you like my models, you can support me on Patreon for $3.99/mo. It is comics only—no videos or re · [source](https://civitai.com/models/2801881?modelVersionId=3187149)
- `Footjob POV Frontview Flux 2 klein 9b - Krea2 - k_footjob` — `f00t, footjob, penis between feet, male pov,` · strength `0.9` (stated) · 2,257 dl · Huggingface for lost Loras: https://huggingface.co/quadratrund Thanks to @AnubisParoh for setting up · [source](https://civitai.com/models/2512932?modelVersionId=3251688)

**MOSS (Moss Image / kromoss)**
- `door-peephole-view-fisheye-visitor-at-the-moss` — trigger not stated · strength not stated · 729 dl · Looking out through an electronic door peephole: a high fisheye angle with the visitor in the center · [source](https://civitai.com/models/3019310?modelVersionId=3427972)
  - example prompt (from source, Euler, steps 50): `doorpeepholeviewconcept, The visitor is a white woman aged 22 with red hair in a messy bun, standing in a dim apartment corridor holding a fluffy bathrobe wide open with ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/5fe38743-a10e-4c84-9d93-e714fee4be4b/original=true/146740141.jpeg)
- `feet-moss` — trigger not stated · strength `0.7` (stated) · 543 dl · A bare-feet concept LoRA for MOSS-Image. Trigger word: feet Trained on 300 real studio photographs ( · [source](https://civitai.com/models/3022702?modelVersionId=3432393)
- `lips-size-slider-moss` — trigger not stated · strength `0 to 2` (stated) · 511 dl · Recommended negative prompt: lowres, bad quality, worst quality, bad anatomy, jpeg artifacts, signat · [source](https://civitai.com/models/2533131?modelVersionId=3418227)

- Suggest ingest: [Hands XL + SD 1.5 + F1D + Pony + Illustrious + zit + ZIB](https://civitai.com/models/200255) (illustrious, 314,114 dl) — `detailed` · strength not stated — **downloads 314114 >= 2x best available (10931) in same family+category**
- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Detailed Perfection style (Hands + Feet + Face + Body + All in one) XL](https://civitai.com/models/411088) (illustrious, 139,148 dl) — `detailed` · strength not stated — **downloads 139148 >= 2x best available (17180) in same family+category**

### 19. Body type, muscle, curves, tan lines

**Illustrious / NoobAI (Illustrious-XL based)**
- `small-but-hung-xl` — `small but hung`, `size difference` · strength not stated · 2,869 dl · v1.1 More refined (i hope), test it out! That said, use whichever fits for u and give feedback if ab · [source](https://civitai.com/models/1991612?modelVersionId=2263536)
  - example prompt (from source, Euler a, steps 30): `masterpiece, best quality, absurdres, highres, newest, very aesthetic, very detailed, cinematic,  small but hung, 1girl, 1boy, minamoto no raikou (fate), hetero, grabbing` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fe950052-73c1-42d4-90d4-780dc757548b/original=true/103109597.jpeg)
- `bottom_up_spread_epoch_10` — `bottom_up_spread, 1girl, solo,  lying,  looking at viewer, on back, sp`, `hip lift,` · strength not stated · 1,359 dl · lora for a sexy posing. A girl spreads legs and lifts her hip. · [source](https://civitai.com/models/2631708?modelVersionId=2954783)
- `torso-onahole-artificial-vagina-with-body-ill` — `1other`, `torso onahole`, `futa torso onahole`, `futa with other` · strength not stated · 1,162 dl · Use Strenght:1.5 or it will mostly not work! I saw some people use my LoRas to make profit. I don't  · [source](https://civitai.com/models/1379014?modelVersionId=1558142)

**SDXL**
- `muscle-mommy-female-bodybuilder-fbb-flux-i-xl` — `Muscl3-m0mmy` · strength not stated · 179 dl · Create your own sexy muscle mommy, have fun! · [source](https://civitai.com/models/1262213?modelVersionId=1423389)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, muscl3-m0mmy, 1girl, veins, muscular female, muscular, breasts, solo, dress, cleavage, earrings, biceps, jewelry, veiny arms, yellow dres` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4fe5e6f9-7b9b-4008-86b4-52eef243047f/original=true/58260111.jpeg)

**Pony (Pony Diffusion XL)**
- `Foot Worship - Foot Licking - Femdom - Foot Fetish Poses Pony SDXL - V1 - Foot_Worship_-_Foot_Licking_-_Femdom_-Foot_Fetish_Poses-000002` — trigger not stated · strength not stated · 2,846 dl · V1. · [source](https://civitai.com/models/561477?modelVersionId=625393)
  - example prompt (from source, Euler a, steps 30): `Source anime, anime colored, score_9, score_8_up, score_7_up, score_6_up, mother and sons, angry  teacher, strict teacher, classroom, black tshirt, black leggings, red lo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/90b41b3a-24d6-46f0-9b37-c45eff2d40e8/original=true/30609476.jpeg)
- `futa-self-cock-worship-pony` — `Self-Licking, Self-Worship,`, `Licking cock` · strength not stated · 1,558 dl · Beta · [source](https://civitai.com/models/1250501?modelVersionId=1409664)
- `futa-pov-body-xl-by-uoc-pony` — `fut4p0vb0dy,futa_pov_body,futa pov body,` · strength not stated · 1,348 dl · [source](https://civitai.com/models/969885?modelVersionId=1085968)

**Anima**
- `Concept Body bridge - v0.0.0 - body_bridge_v0.0.0_0600_cosine-0025` — `body bridge`, `on back`, `arm support`, `tiptoes` · strength not stated · 1,741 dl · I found it difficult to achieve a pose where the body bends into a bridge-like shape, curving like a · [source](https://civitai.com/models/2875579?modelVersionId=3249483)
  - example prompt (from source, er_sde, steps 12): `bar censor,  solo, full body, from side,  1girl, hatsune miku, huge breasts, body bridge, arm support, on back, tiptoes,  nervous smile, no panties, spread legs,    highr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ff3e4a70-981d-4425-a937-d1cb4f958140/original=true/140294954.jpeg)
- `body-writing-erotic-anima` — `body writing,` · strength `1` (stated) · 1,571 dl · Recommended weight： 1 Trigger prompts ： body writing,  Tried making an anima version with a "Body Wr · [source](https://civitai.com/models/2951684?modelVersionId=3343038)
- `thick_nipples_260210` — `thick nipples, hyper nipples, wide nipples, large areolae, hyper areol` · strength not stated · 1,039 dl · ※AI Translation I don't really understand Anima or how to create Lora for Anima. For now, I trained  · [source](https://civitai.com/models/2383224?modelVersionId=2679973)

**Krea2 (detailed-krea2)**
- `Krea2 milf body - V1 - milfbodyhms_v1` — `(fupa:1.2)`, `rounded pubic mound`, `saggy buttocks`, `rounded lower abdomen` · strength not stated · 4,091 dl · try the following: (fupa:1.2) - increase strength for a more distended lower abdomen. I've come to l · [source](https://civitai.com/models/2784421?modelVersionId=3137009)
  - example prompt (from source, Euler, steps 8): `three side-by-side photos of the exact same nude european woman, showing a front view, a side view and a back view. neutral posture, warm smile. plain background.  slim w` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fb94c6dd-3efe-48d4-b14b-b96c867746c7/original=true/137260382.jpeg)
- `z-female-body-retouched-krea2` — trigger not stated · strength `2.0` (stated) · 2,990 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3186931)
- `pawg-small-waist-wide-hips-swwh-krea2` — `SWWH` · strength `0.9` (stated) · 2,413 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2814261?modelVersionId=3173942)

**MOSS (Moss Image / kromoss)**
- `z-female-body-retouched-xl` — trigger not stated · strength `0.6-1.0` (stated) · 1,346 dl · Krea2 v1: Thanks to krea2 build-in knowledge, this versioin is more likely a aesthetic retouch. #### · [source](https://civitai.com/models/2196685?modelVersionId=3413047)
  - example prompt (from source, res_multistep, steps 30): `a naked yamamura_sadako cosplayer, smile, walking, huge breasts, outdoors, wild, overexposured skin, at night, candid amateur shot, blurry foreground` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/0bd4af23-f52f-49f7-8c09-c17f30bb86b3/original=true/146021224.jpeg)
- `thick-inner-labia-moss` — `th1ck-l4b1a	Her pussy has thick inner labia` · strength not stated · 769 dl · try: th1ck-l4b1a Her pussy has thick protruding inner labia, shown curly wrinkled and saggy Yes, I k · [source](https://civitai.com/models/3032886?modelVersionId=3445800)
- `pearshape-body-moss` — `p34rsh4p3-body	She has a pearshape body.` · strength not stated · 677 dl · try: p34rsh4p3-body She has a pearshape body extra-wide hips and narrow shoulders Yes, I know, it's  · [source](https://civitai.com/models/3033031?modelVersionId=3445974)

- Suggest ingest: [[Flux/Pony] Perfect Full Round Breasts & Slim Waist](https://civitai.com/models/61099) (pony, 143,865 dl) — `busty breasts` · strength not stated — **downloads 143865 >= 2x best available (11319) in same family+category**
- Suggest ingest: [BFS - Best Face Swap](https://civitai.com/models/2027766) (krea2, 110,251 dl) — `body_swap: replace the person with the reference person.` · strength not stated — **downloads 110251 >= 2x best available (32481) in same family+category**
- Suggest ingest: [Real Pussy - Cameltoe](https://civitai.com/models/137423) (sdxl, 63,670 dl) — `cameltoe_body`, `cameltoe_hips`, `cameltoe_pussy` · strength not stated — **downloads 63670 >= 2x best available (1707) in same family+category**

### 20. Lingerie, latex, bodysuits, corsets

**Illustrious / NoobAI (Illustrious-XL based)**
- `cat-lingerie-ill` — trigger not stated · strength `0.7` (stated) · 3,088 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2711788)
  - example prompt (from source, DPM++ 2M, steps 25): `masterpiece,amazing quality,newest,absurdres,highres,detailed face,kawaii,cute,perfect eyes,<lora:rich colors enhance_illustrious_V1.0:0.6>,rce,depth of field,simple back` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bcbd35ae-25d0-4f99-ba18-6c0302bd84d6/original=true/121974471.jpeg)
- `thin-bodysuit-ill` — `th1nbodysu1t`, `highleg` · strength `0.8` (stated) · 2,149 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=1417556)
- `peppan2_santopati` — trigger not stated · strength not stated · 1,983 dl · You can look at the sample images above for the example prompts. "peppan" trigger word is optional R · [source](https://civitai.com/models/1240750?modelVersionId=2920404)

**SDXL**
- `thin-bodysuit-xl` — `th1nbodysu1t` · strength `0.8` (stated) · 1,359 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=388278)
  - example prompt (from source, Euler a, steps 20): `masterpiece, ink illustration, perfect shading, comic style, green th1nbodysu1t, a beautiful young arafed woman, Katia from Canada, black, proportional eyes, slim, gorgeo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f3fa8f8f-bfb4-475b-bcb0-ce21b2fe0e80/original=true/7835249.jpeg)
- `thong-upskirt-xl` — trigger not stated · strength not stated · 178 dl · [source](https://civitai.com/models/2898091?modelVersionId=3276640)
- `dildo-under-panties-dildo-under-thong-dild-xl` — `Dildo under panties, thong` · strength not stated · 74 dl · Stretch out panties or thong with a dildo. Have fun! · [source](https://civitai.com/models/2572798?modelVersionId=2895464)

**Pony (Pony Diffusion XL)**
- `costumefishnet-bodysuit-request-pony` — `fishnet bodysuit` · strength not stated · 4,406 dl · [source](https://civitai.com/models/815349?modelVersionId=911750)
  - example prompt (from source, DPM++ 2M, steps 20): `score_8_up, score_7_up, score_6_up, source_anime, 1girl, solo, simple background, pink background, standing, pose, contrapposto, arched back, cowboy shot, facing viewer s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/be8a8217-5bb6-407d-b074-5c66eb432da5/original=true/32275339.jpeg)
- `costumelatex-outfit-request-pony` — `latex shrug (clothing), latex legwear, reverse outfit` · strength not stated · 2,153 dl · [source](https://civitai.com/models/815828?modelVersionId=912285)
- `cat-lingerie-pony` — `cat lingerie,bra,panties,neck bell` · strength `0.7` (stated) · 1,658 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=1740093)

**Anima**
- `cat-lingerie-anima` — `cat lingerie`, `cat ear legwear` · strength `0.7` (stated) · 1,777 dl · The recommended strength of lora is around 0.7. · [source](https://civitai.com/models/1284777?modelVersionId=2939201)
  - example prompt (from source, Euler a, steps 25): `masterpiece, best quality,newest,absurdres,highres,kawaii,cute,<lora:boleromix_anima_V1.0:0.3>,glossy hair,perfect eyes,real skin, <lora:cat lingerie_anima_V1.0:1> cat li` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3dce4dec-6ab8-4c2b-9c82-2dbed273a677/original=true/130473481.jpeg)
- `jav-race-queen-with-highleg-leotard-anima` — `jav fstu 033 032,  1girl, solo,  race queen, clothes writing, highleg `, `holding parasol,  Holding umbrella,`, `2boys, multiple boys,  taking picture, recording, camera boys, boys ar`, `2boys, mmf threesome, hetero, fingering, grabbing, group sex, leotard ` · strength `0.85 - 1` (stated) · 728 dl · This LORA was created to see if it could learn JAV and produce hentai anime. 📋Source material for tr · [source](https://civitai.com/models/2861588?modelVersionId=3232553)
- `costumesatin-lingerie-set-anima` — `satin bra, satin panties, lace trim, (color) bra, (color) panties` · strength not stated · 678 dl · TAGS: satin bra, satin panties, lace trim, (color) panties, (color) bra ISSUES: realism issues, lowe · [source](https://civitai.com/models/2600236?modelVersionId=2958997)

**Krea2 (detailed-krea2)**
- `thin-bodysuit-krea2` — `th1nbodysu1t` · strength `0.8` (stated) · 2,025 dl · A bodysuit LORA created for extremely thin, highleg style bodysuits. More LORA practice, think this  · [source](https://civitai.com/models/302118?modelVersionId=3154439)
  - example prompt (from source, Euler, steps 8): `A close-up glamour photography photo of a beautiful, slim woman with striking cheekbones, expressive brown eyes, elegant eyeliner, long eyelashes, and pink lips. She has ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d60a3126-0371-44c5-9232-b0b22cc77651/original=true/137498130.jpeg)
- `thong-madness-krea2` — trigger not stated · strength not stated · 1,988 dl · Most krea2 models i use struggle to make tiny or string panties or thongs so i made this model to tr · [source](https://civitai.com/models/2995179?modelVersionId=3396864)
- `joschek-s-shiny-latex-bodysuits-for-krea2` — `latex bodysuit` · strength not stated · 1,739 dl · works. · [source](https://civitai.com/models/2729323?modelVersionId=3068160)

**MOSS (Moss Image / kromoss)**
- `micro-bikini-thong-pull-for-moss` — trigger not stated · strength `0.5` (stated) · 843 dl · This model generates a low cut sling style micro bikini. This model also does well with getting the  · [source](https://civitai.com/models/3022730?modelVersionId=3432428)
  - example prompt (from source, res_multistep, steps 8): `With the edge of a backyard in-ground pool in the foreground a young Korean woman with over-saturated wet long black hair rises up out of the water hands on the white til` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fb8e1f16-c9be-48ab-9c56-db53efe6f795/original=true/146962541.jpeg)
- `base-candid-adjusting-panties-moss` — `4dju5t1ng-p4nt135	She is adjusting her panties.` · strength not stated · 277 dl · generates mid-action shots of a woman adjusting her underwear try: 4dju5t1ng-p4nt135 She is adjustin · [source](https://civitai.com/models/3048896?modelVersionId=3466869)
- `base-low-waist-panties-moss` — `l0w-w415t low-waist panties` · strength not stated · 275 dl · you don't need this. but if you like the samples, give it a go. try: l0w-w415t she is wearing low-wa · [source](https://civitai.com/models/3038423?modelVersionId=3452969)

- Suggest ingest: [クロッチずらし/panties aside(XL,Pony)](https://civitai.com/models/471385) (illustrious, 33,017 dl) — `panties aside, panties, pussy`, `anus` · strength not stated — **downloads 33017 >= 2x best available (6777) in same family+category**
- Suggest ingest: [セクシーランジェリー/babydoll,sexy lingerie(SD,ILL,pony)](https://civitai.com/models/522201) (illustrious, 25,785 dl) — `babydoll` · strength not stated — **downloads 25785 >= 2x best available (6777) in same family+category**
- Suggest ingest: [No Bra SDXL](https://civitai.com/models/137296) (sdxl, 17,694 dl) — `no bra`, `covered nipples` · strength not stated — **downloads 17694 >= 2x best available (1359) in same family+category**

### 21. Stockings, thigh-highs, heels and shoes

**Illustrious / NoobAI (Illustrious-XL based)**
- `costumeblack-bodystocking-request-ill` — `bodystocking` · strength not stated · 2,400 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=1244147)
  - example prompt (from source, DPM++ 2M, steps 20): `perfect quality, best quality, masterpiece, 1girl, solo, simple background, pink background, standing, cowboy shot, facing viewer, contrapposto, smile, Classic French Bra` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/38bd2493-882a-4498-8925-d568b7c20404/original=true/49714552.jpeg)
- `jacquard-leggings-ill` — `jacquardleggings`, `fishnet` · strength not stated · 1,034 dl · Lora for ass lifting yoga pants, with or without texture. Add fishnet to your prompt for texture. · [source](https://civitai.com/models/1521437?modelVersionId=1721371)
- `conceptreference-sheet-with-clothes-shoes-ill` — `reference sheet, close-up, multiple views, clothes focus, footwear foc` · strength not stated · 901 dl · This will generate reference sheets with images on the side focusing on different stuff. TAGS: refer · [source](https://civitai.com/models/2403343?modelVersionId=2702274)

**SDXL**
- `lace-pantyhose-hooked-on-heel-meme-il-sd-xl` — `Pantyhose_hooked_on_heel, full body, from side, lying, on stomach, fee` · strength not stated · 49 dl · Creates the meme/viral pose where the character's high heel shoe is hooked on lace pantyhose. Very s · [source](https://civitai.com/models/2212567?modelVersionId=2491084)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, masterpiece, 8k, highly detailed,pantyhose_hooked_on_heel, full body, from side, lying, on stomach, feet up, clothes pull, pantyhose, hig` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/bb38cc8d-504a-42d7-bd79-6fa5d79bf9a9/original=true/113709851.jpeg)

**Pony (Pony Diffusion XL)**
- `costumeblack-bodystocking-request-pony` — `bodystocking` · strength not stated · 1,210 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=908485)
  - example prompt (from source, DPM++ 2M, steps 20): `score_8_up, score_7_up, score_6_up, source_anime, 1girl, solo, simple background, pink background, standing, pose, contrapposto, arched back, cowboy shot, facing viewer s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/3ad50581-5460-4cd4-81a8-88d7cf15a387/original=true/32122829.jpeg)
- `futa-presenting-in-pantyhose-pony` — trigger not stated · strength not stated · 813 dl · [source](https://civitai.com/models/1098370?modelVersionId=1233809)
- `costumepeep-toe-heels-request-pony` — `peep-toe heels, stiletto heels, platform heels` · strength not stated · 768 dl · [source](https://civitai.com/models/815260?modelVersionId=911657)

**Anima**
- `costumeopaque-pantyhose-commission-anima` — `pantyhose, (color) pantyhose` · strength not stated · 698 dl · TAGS: pantyhose, (color) pantyhose ISSUES: sometimes control top or other seams appears · [source](https://civitai.com/models/2730158?modelVersionId=3069195)
  - example prompt (from source, Euler a, steps 32): `<lora:opaquapantyhose_anima:1> pantyhose, black pantyhose, black bra,, score_9, score_8_up, score_7_up, masterpiece, best quality, very aesthetic, absurdres, very awa, de` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c3dab5c7-19e9-4319-a7ba-f7dfad1e0b7d/original=true/134842028.jpeg)
- `costumeembroidered-thigh-highs-commission-anima` — `embroidered legwear, thighhighs, (color) thighhighs` · strength not stated · 672 dl · TAGS: embroidered legwear, thighhighs, (color) thighhighs commissions https://ko-fi.com/aiadoreyou · [source](https://civitai.com/models/2700511?modelVersionId=3032608)
- `take-a-chance-fishnet-bodystocking-anima` — `see-through, fishnet thighhighs, fishnet bodysuit, fishnet chaps, bott` · strength not stated · 476 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/433503?modelVersionId=3439097)

**Krea2 (detailed-krea2)**
- `suspender-stockings-krea2` — `suspender_stockings` · strength not stated · 2,211 dl · A lora for a one-piece garment integrating stockings and garter belt. Keywords include fishnet, torn · [source](https://civitai.com/models/2087323?modelVersionId=3200743)
  - example prompt (from source, Euler, steps 8): `A highly detailed glamour photography photo of a beautiful, slim woman. She has medium auburn hair up in a bun.  She has striking blue eyes and glasses, she has red lips.` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a57df86b-2047-41bb-bd47-eed2bbba6619/original=true/138835392.jpeg)
- `glossy-pantyhose-flux-krea2` — `glossy pantyhose flux krea2` · strength not stated · 1,631 dl · You can use it for glossy or shiny pantyhose. Testet on white, black, tan and brown. · [source](https://civitai.com/models/1443102?modelVersionId=3247385)
- `c666d-pear-booty-pawg-v1-krea2` — `pear booty pawg, thick thighs, wide hips`, `pear booty pawg`, `thick thighs`, `wide hips` · strength `2` (stated) · 1,392 dl · This model is trained with a dataset consisting of 94 images of mixed resolutions. Some of the image · [source](https://civitai.com/models/2909674?modelVersionId=3291063)

**MOSS (Moss Image / kromoss)**
- `heel-grabbers-base-moss` — trigger not stated · strength not stated · 190 dl · Its nice to see you again OBVIOUS PERSON OF TASTE! I spent some time making something your 1girl is  · [source](https://civitai.com/models/3047057?modelVersionId=3464228)
  - example prompt (from source, Euler, steps 50): `A platinum-blonde bimbo in her early twenties with heavy makeup, a yellow and gold spiraling striped party hat with fluffy cotton rim sits atop her head, she has heavily ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a6ce566a-d278-4152-b530-0eb8661b77e3/original=true/148663857.jpeg)
- `10-inches-pleaser-heels-moss` — `101ph`, `[Infinity997,Beyond008,Beyond009,Beyond010LG,Beyond010LG],`, `10 inch platform heels, [color,clear] massive extreme platform soles, `, `[color,clear] [criss-cross,slender thin woven interlaced multi-strap,p` · strength not stated · 166 dl · My Character LoRA Gallery (1000+ Downloadable Character LoRAs & 500+ Runnable Online) Moss Image: St · [source](https://civitai.com/models/1777689?modelVersionId=3451681)
- `transparent-platform-heels-moss` — `tph0, clear pleaser platform heels, a clear transparent strap crosses ` · strength not stated · 162 dl · My Character LoRA Gallery (1000+ Downloadable Character LoRAs & 500+ Runnable Online) Moss Image: St · [source](https://civitai.com/models/1778876?modelVersionId=3454519)

- Suggest ingest: [pantyhose](https://civitai.com/models/26760) (sdxl, 24,942 dl) — `panntyhose`, `black pantyhose`, `white pantyhose` · strength `0.5` (stated) — **downloads 24942 >= 2x best available (1359) in same family+category**
- Suggest ingest: [Erza Scarlet (All Armors & Outfits) (61 Outfits) / Illustrious](https://civitai.com/models/902174) (illustrious, 21,556 dl) — `erz_bwaitress, brown eyes, red hair, long hair, hair over one eye, fak` · strength `0.8 - 1` (stated) — **downloads 21556 >= 2x best available (6777) in same family+category**
- Suggest ingest: [NSFW Bunnysuit](https://civitai.com/models/109759) (illustrious, 19,383 dl) — `reverse bunnysuit,`, `pasties, maebari,`, `crotchless pantyhose` · strength not stated — **downloads 19383 >= 2x best available (6777) in same family+category**

### 22. Swimwear and beach

**Illustrious / NoobAI (Illustrious-XL based)**
- `x micro bikini_illustrious_V2.1` — `x micro bikini` · strength not stated · 4,944 dl · pony;The strength of Lora is recommended to be around 1.0. XL;The strength of Lora is recommended to · [source](https://civitai.com/models/518864?modelVersionId=2651990)
  - example prompt (from source, DPM++ 2M, steps 30): `masterpiece,amazing quality,newest,absurdres,highres,highly-detailed,detailed face,simple background,anime coloring,deep colors,matte coloring,<lora:boleromix pony_illust` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/421c5575-87c8-4a97-a88d-92d213092448/original=true/119642045.jpeg)
- `competitive-swimsuit-sd-xl-ill` — `competitive swimsuit` · strength not stated · 2,523 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2715085)
- `Ultra Micro BikiniSlingshot Swimmsuit - Illustrious - UMBV1` — `ultra_micro_bikini` · strength not stated · 1,988 dl · I had a long description for this but my browser crashed and I don't think I can recreate the magic. · [source](https://civitai.com/models/2273944?modelVersionId=2559479)

**SDXL**
- `condom-bikini-condoms-tied-to-bikini-il-sd-xl` — `c0ndom_bikini, tied condom, used condoms, condoms tied to bikini` · strength not stated · 135 dl · Lets your favorite character wear a condom bikini, or bikini with used condoms tied on it. Have fun! · [source](https://civitai.com/models/1584792?modelVersionId=1793388)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, c0ndom_bikini, tied condom, used condoms, condoms tied to bikini, 1girl, used condom, cum, swimsuit, bikini, gokkun, blonde hair, pink bi` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b2809cd7-39e5-4f80-a699-47d45764de29/original=true/77032231.jpeg)
- `penis-under-another-s-bikini-penis-under-a-xl` — `Penis under another's clothes, bikini` · strength not stated · 82 dl · Have him stick his dick right under her bikini, the best spot! Have fun! · [source](https://civitai.com/models/2024170?modelVersionId=2290925)
- `miami-beach-hotel-interior-background-ad-xl` — `MiaBeaHotInt`, `interior` · strength not stated · 35 dl · [source](https://civitai.com/models/2819289?modelVersionId=3180166)

**Pony (Pony Diffusion XL)**
- `competitive-swimsuit-sd-xl-ill-pony` — `competitive swimsuit` · strength not stated · 4,591 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=614384)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `score_9, score_8_up, score_7_up,source_anime, high res image,masterpiece,best quality,girl,cute face,clear skin,shiny hair,ultra detailed eyes,simple background,  <lora:C` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fa5140b3-5335-47fc-bea2-9edd4d1a53c9/original=true/18131620.jpeg)
- `costumecross-swimsuit-request-pony` — `cross swimsuit`, `areola slip, skin indention` · strength not stated · 1,967 dl · [source](https://civitai.com/models/830254?modelVersionId=928606)
- `costumewhite-swimsuit-request-pony` — `white one-piece swimsuit, highleg swimsuit` · strength not stated · 1,030 dl · [source](https://civitai.com/models/820309?modelVersionId=917281)

**Anima**
- `maid-bikini-anima` — `maid bikini, maid headdress, frills, wrist cuffs,bare shoulders` · strength not stated · 2,193 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/668558?modelVersionId=3055885)
  - example prompt (from source, Euler a, steps 20): `masterpiece,best quality,highres,newest,real skin,perfect eyes,glossy hair <lora:maid bikini_anima_V1.0:1.0> maid bikini, maid headdress, frills, wrist cuffs,bare shoulde` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4acf95ee-6762-4fbf-89c1-840ec533d8fe/original=true/134420686.jpeg)
- `competitive-swimsuit-sd-xl-ill-anima` — `competitive swimsuit` · strength not stated · 1,812 dl · The strength of Lora is recommended to be around 1.0. There are no major changes, but I think the sh · [source](https://civitai.com/models/552104?modelVersionId=2944201)
- `string-only-bikini-real-anime-kr2-anima` — `stringonlybikini, string only swimwear, one-piece tanlines, partially ` · strength `0.85 - 1` (stated) · 1,735 dl · ⬇️This is Anima Model⬇️ [ANIMA] offers remarkably rich expressiveness compared to the [KREA 2] model · [source](https://civitai.com/models/2845651?modelVersionId=3215435)

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
- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,308 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36308 >= 2x best available (9653) in same family+category**
- Suggest ingest: [SDXL_Sexy underwear](https://civitai.com/models/124782) (sdxl, 10,105 dl) — `bikini`, `underwear`, `Lace` · strength `0.6-1.5` (stated) — **downloads 10105 >= 2x best available (1359) in same family+category**

### 23. Costumes, uniforms and cosplay (adult characters)

All characters must be adults.

**Illustrious / NoobAI (Illustrious-XL based)**
- `costumeblack-bodystocking-request-ill` — `bodystocking` · strength not stated · 2,400 dl · TAGS: bodystocking I TAKE REQUESTS AT https://civitai.com/articles/7712/clothing-lora-requests · [source](https://civitai.com/models/812429?modelVersionId=1244147)
  - example prompt (from source, DPM++ 2M, steps 20): `perfect quality, best quality, masterpiece, 1girl, solo, simple background, pink background, standing, cowboy shot, facing viewer, contrapposto, smile, Classic French Bra` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/38bd2493-882a-4498-8925-d568b7c20404/original=true/49714552.jpeg)
- `body-paint-cosplay-event-peint-clothes-cos-ill` — `((paint clothes)), ((bodypaint)), paint_cosplay_event, 1girl, breasts,` · strength not stated · 2,321 dl · Generate a scene from a cosplay event in Tokyo. According to recent regulations, it's OK as long as  · [source](https://civitai.com/models/2017293?modelVersionId=2283114)
- `costumebandeau-maid-ill` — `maid, (color) bandeau, (color) skirt, underboob, waist apron,` · strength not stated · 2,080 dl · TAGS: maid, (color) bandeau, (color) skirt, waist apron, underboob I don't use pony anymore so sorry · [source](https://civitai.com/models/1050728?modelVersionId=1187194)

**SDXL**
- `80s-aerobic-outfit-xl` — `a3robic`, `80s aerobic outfit` · strength not stated · 479 dl · [source](https://civitai.com/models/517542?modelVersionId=575094)
  - example prompt (from source, DDIM, steps 30): `aerobics class, 4 women in 80s aerobic outfit, in a studio` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7ebf68bc-06f7-4c5c-b45e-852e8fe970f2/original=true/15968422.jpeg)
- `outfit-futa-xl` — trigger not stated · strength not stated · 185 dl · V1 · [source](https://civitai.com/models/663022?modelVersionId=741974)
- `nhs-nurse-sister-uniform-v3-xl` — `NHS Nurse Dress`, `short-sleeved dark_blue NHS Nurse Dress with white piping` · strength not stated · 126 dl · Latest iteration of my NHS nurse dress - I wanted a low that consistently produced the dark blue dre · [source](https://civitai.com/models/1150801?modelVersionId=1295407)

**Pony (Pony Diffusion XL)**
- `costumefishnet-bodysuit-request-pony` — `fishnet bodysuit` · strength not stated · 4,406 dl · [source](https://civitai.com/models/815349?modelVersionId=911750)
  - example prompt (from source, DPM++ 2M, steps 20): `score_8_up, score_7_up, score_6_up, source_anime, 1girl, solo, simple background, pink background, standing, pose, contrapposto, arched back, cowboy shot, facing viewer s` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/be8a8217-5bb6-407d-b074-5c66eb432da5/original=true/32275339.jpeg)
- `costumeskimpy-gal-request-pony` — `front-tied shirt, micro bikini, areola slip, miniskirt, pleated skirt` · strength not stated · 2,214 dl · [source](https://civitai.com/models/815009?modelVersionId=911347)
- `costumelatex-outfit-request-pony` — `latex shrug (clothing), latex legwear, reverse outfit` · strength not stated · 2,153 dl · [source](https://civitai.com/models/815828?modelVersionId=912285)

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
- `maid-classic-moss` — `maid,maid apron,maid headdres` · strength not stated · 221 dl · The strength of Lora is recommended to be around 1.0. · [source](https://civitai.com/models/703211?modelVersionId=3456338)
  - example prompt (from source, Euler a, steps 20): `<lora:MOSS_Image_SFT_8_steps_dmd_v0.1:0.6>, masterpiece,amazing quality,anime,cute,simple background,<lora:boleromix_moss_V1.0:0.8>  <lora:maid classic_moss_V1.0:1> maid,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/661d003d-208f-486b-ad5e-9b9fdca780dc/original=true/148275539.jpeg)
- `base-candid-getting-dressed-inspecting-pan-moss` — `p4nt135-1n5p3ct10n	She is inspecting her panties in her hand` · strength not stated · 213 dl · generates mid-action shots of a woman inspecting panties in her hand, in a getting dressed/undressed · [source](https://civitai.com/models/3049187?modelVersionId=3467286)
- `base-candid-getting-dressed-pulling-top-on-moss` — `g3tt1ng-dr3553d	She is getting dressed, pulling her top on.` · strength not stated · 206 dl · generates mid-action shots of a woman getting dressing pulling her top on.  try: g3tt1ng-dr3553d She · [source](https://civitai.com/models/3049177?modelVersionId=3467272)

- Suggest ingest: [Undressing SD1/XL/PONY/FLUX](https://civitai.com/models/505266) (sdxl, 55,860 dl) — `undressing` · strength `1.3` (stated) — **downloads 55860 >= 2x best available (1359) in same family+category**
- Suggest ingest: [Slavekini, aka Slave Leia Outfit - Clothing [Krea2, Anima, IL, Pony, S](https://civitai.com/models/7913) (illustrious, 30,714 dl) — `slave leia outfit`, `or`, `slavekini, pelvic curtain , collar, armlet , hair ornament, braid` · strength `.8-1.0` (stated) — **downloads 30714 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Undressing LoRA [SD1.5 & SDXL1.0]](https://civitai.com/models/242034) (sdxl, 26,132 dl) — `undressing` · strength not stated — **downloads 26132 >= 2x best available (1359) in same family+category**

### 24. Accessories and gear (collars, chastity, piercings, condoms, plugs)

**Illustrious / NoobAI (Illustrious-XL based)**
- `harness-sd-xl-ill` — `harness, bdsm, o-ring`, `bound` · strength not stated · 6,777 dl · The strength of Lora is recommended to be around 0.8 · [source](https://civitai.com/models/583686?modelVersionId=1131895)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,ultra-detailed-background,cute girl, eyelashes,middle` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/af55ddee-1780-4068-aef6-bdf1c704d0aa/original=true/43808908.jpeg)
- `chastity-cage-metal-flat-v1-ill` — `flat chastity cage`, `precum drip`, `testicles`, `ejaculation, ejaculating while penetrated, cum` · strength not stated · 5,868 dl · flat chastity cage lora best used with inpainting check my specialized loras! pov lora https://civit · [source](https://civitai.com/models/1689514?modelVersionId=2429438)
- `clitoris jewely_illustrious_V1.0` — `clitoris jewelry, clitoris, thong` · strength not stated · 4,725 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/576831?modelVersionId=1168859)

**SDXL**
- `condom-bikini-condoms-tied-to-bikini-il-sd-xl` — `c0ndom_bikini, tied condom, used condoms, condoms tied to bikini` · strength not stated · 135 dl · Lets your favorite character wear a condom bikini, or bikini with used condoms tied on it. Have fun! · [source](https://civitai.com/models/1584792?modelVersionId=1793388)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, c0ndom_bikini, tied condom, used condoms, condoms tied to bikini, 1girl, used condom, cum, swimsuit, bikini, gokkun, blonde hair, pink bi` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b2809cd7-39e5-4f80-a699-47d45764de29/original=true/77032231.jpeg)
- `condoms-in-stomach-il-sd-xl` — `c0ndoms_in_st0mach, condoms in stomach, x-ray` · strength not stated · 86 dl · Leaves condoms in her stomach, very few pics of this (and I love making rare concepts), have fun! · [source](https://civitai.com/models/1445083?modelVersionId=1633717)
- `jewelry-exclusive-xl` — `HauteJewls, bracelet, anklet, necklace, toering, ring, gold, silver, d` · strength not stated · 85 dl · [source](https://civitai.com/models/2665564?modelVersionId=2993145)

**Pony (Pony Diffusion XL)**
- `genital-piercing-xl-pony` — `pussy piercing, clitoris piercing`, `pussy`, `spread puusy` · strength not stated · 3,287 dl · [source](https://civitai.com/models/459565?modelVersionId=511474)
  - example prompt (from source, Euler, steps 25): `score_9, score_8_up, score_7_up,source_anime, high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-face,cute girl,spread pussy,cum in pus` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4611900d-a292-4d2b-b65e-1e29bf564d23/original=true/71051377.jpeg)
- `clitoris-jewelry-xl-ill-pony` — `clitoris jewelry` · strength not stated · 2,800 dl · The strength of Lora is recommended to be around 0.8. · [source](https://civitai.com/models/576831?modelVersionId=643187)
- `male-pov-general-micropenis-chastity-cage-pony` — `pov crotch, penis, 1girl,`, `1boy,`, `multiple boys,`, `2boys,` · strength not stated · 1,669 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1289738?modelVersionId=1455327)

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

- Suggest ingest: [Cumflood](https://civitai.com/models/18665) (illustrious, 36,308 dl) — `cumallover`, `cumflooding`, `fillingpool`, `hyperejaculation` · strength not stated — **downloads 36308 >= 2x best available (9653) in same family+category**
- Suggest ingest: [乳首責め/nipple pull](https://civitai.com/models/627113) (illustrious, 33,549 dl) — `nipple pull,holding,1girl,nipples,1boy,nipple piercing,chain,` · strength not stated — **downloads 33549 >= 2x best available (10931) in same family+category**
- Suggest ingest: [Milking Machines](https://civitai.com/models/419704) (pony, 16,179 dl) — `milking machine,suction device,milk machine,harness,object insertion,s` · strength not stated — **downloads 16179 >= 2x best available (7814) in same family+category**

### 25. POV and camera angle / framing

Camera/framing LoRAs go early in the stack; keep strength moderate.

**Illustrious / NoobAI (Illustrious-XL based)**
- `CuckNTR POV Pony LoRa - 3.0 Illustrious - NTR_POV` — trigger not stated · strength not stated · 9,704 dl · Important tags (tag: cuck pov,netorare,femdom) Make person hold a cellphone with porn on it (tags: p · [source](https://civitai.com/models/339447?modelVersionId=1255291)
  - example prompt (from source, Euler a, steps 30): `(masterpiece, best quality), amazing quality, very aesthetic, absurdres, highres, newest, HDR, 8K, high detail RAW  1boy, breasts, cellphone, hetero, ntr, nude, handjob, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/fdfa6065-d12e-4414-a889-0cf6041cf8bf/original=true/50256070.jpeg)
- `toilet-spy-multiple-views-2koma-concept-ve-ill` — `knees together feet apart`, `tile wall`, `toilet use`, `toilet seat` · strength not stated · 5,016 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/1941768?modelVersionId=2197702)
- `conceptmultiple-views-ill` — `multiple views` · strength not stated · 3,881 dl · TAGS: multiple views you can probably prompt this but I'm lazy · [source](https://civitai.com/models/918034?modelVersionId=1027532)

**SDXL**
- `female-masturbation-from-above-xl` — trigger not stated · strength `0.6` (stated) · 895 dl · Try a strength between 0.6 and 1.0. I recommend negative promts like: "maleformed hands, malformed f · [source](https://civitai.com/models/2718384?modelVersionId=3054666)
  - example prompt (from source, DPM++ 2M SDE, steps 20): `<lora:fingering_above_sdxl:1> fingeringwoman, masturbation, female pubic hair, female masturbation, lying, orgasm` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/9e3dd401-36c0-4d03-8c33-733866f055ad/original=true/134384381.jpeg)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)
- `wide-shot-long-shot-zoom-out-xl` — `Wide shot` · strength not stated · 125 dl · Don't like how all your images are so close to the character? The wide shot view is zoomed out so yo · [source](https://civitai.com/models/2623769?modelVersionId=2946010)

**Pony (Pony Diffusion XL)**
- `tg-rear-shot-trans-girls-from-behind-pony` — `TGRearShot` · strength not stated · 265 dl · This is mostly to generate a better rear angle of trans women. I've had decent luck with at 0.6 to 1 · [source](https://civitai.com/models/2015785?modelVersionId=2281365)
  - example prompt (from source, Euler a, steps 18): `score_9, score_8_up, score_7_up, side angle, side view, , a trans woman in a bikini on a blanket in a yard, big round ass, low angle, legs together, looking at viewer, po` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/401bda26-4ec1-4f51-8412-99e785f0ca24/original=true/104151279.jpeg)
- `wide-shot-long-shot-zoom-out-pony` — `Wide shot` · strength not stated · 131 dl · Don't like how all your images are so close to the character? The wide shot view is zoomed out so yo · [source](https://civitai.com/models/2623769?modelVersionId=2946007)
- `bathroom-booty-selfie-pose-sink-butt-influ-pony` — `Bo0ty_s3lfie_p0se` · strength not stated · 122 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705669)

**Anima**
- `fpov-anima` — `female pov looking down her breasts` · strength not stated · 6,246 dl · Hey guys! Hope you love using this new LoRA as much as I loved making it. Just a quick word of advic · [source](https://civitai.com/models/427349?modelVersionId=2948925)
  - example prompt (from source, er_sde simple, steps 30): `absurdrabsurdres, masterpiece, score_7, score_8, 1girl, female pov looking down her breasts, turtleneck sweater, jeans, computer keyboard, at computer, computer mouse, sh` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/496f8ce2-df98-4a1d-ac6d-1e076a08a2fe/original=true/130836662.jpeg)
- `fpcview_v0.0.0-step00000600` — `fpcview`, `from above, wide shot, dutch angle`, `head out of frame, straight-on`, `The character stands near the edge of the frame while a large empty sp` · strength not stated · 2,133 dl · v0.0.0 (Initial Release) The purpose of this LoRA is to break the AI's deeply hardcoded composition  · [source](https://civitai.com/models/2782139?modelVersionId=3133505)
- `ntr-pov-netorase-netorare-cuckold-for-anima` — `NTRedwifeSP`, `netorare, depth of field, a couple having sex behind a sliding door, a` · strength not stated · 1,693 dl · With this Lora, you can watch your Waifu being cuckolded right in front of you. This LoRA may also a · [source](https://civitai.com/models/3016671?modelVersionId=3424519)

**Krea2 (detailed-krea2)**
- `_Krea2__Taking_selfie_from_3rd-person_view_epoch_6` — `th1rd-p3rson-self1e third-person view of`, `viewed from a three-quarters angle`, `she is sitting and reclining back spreading her thighs {and feet up cu`, `she is standing and reaching carefully between her leg holding a smart` · strength not stated · 1,779 dl · Give it a go. It generates images of [women] taking selfies. Not a selfie image as such, as it's fro · [source](https://civitai.com/models/2818090?modelVersionId=3178646)
  - example prompt (from source, Euler, steps 8): `candid photo captured in the moment, unplanned unposed, captured in the moment with candid postures shown mid actions and expressions captured in the moment and unflatter` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/83b749cd-532f-43a8-8c8b-00e32500d8c2/original=true/138163103.jpeg)
- `fpov-female-point-of-view-for-krea2` — `From a top-down view`, `From a first-person perspective` · strength `1` (stated) · 1,728 dl · V1 (alone): This is the main version. This LoRa is the result of 2 years of testing on Flux, but I w · [source](https://civitai.com/models/2918304?modelVersionId=3301630)
- `hm1girl-phone-camera-realism-for-krea2` — `hm1girl` · strength not stated · 1,714 dl · Free ComfyUI workflows, Runpod templates, and guides: 👉 hearmemanai.com For more LoRAs and updates,  · [source](https://civitai.com/models/2967466?modelVersionId=3362360)

**MOSS (Moss Image / kromoss)**
- `home-cctv-hd-clear-home-dorm-security-came-moss` — trigger not stated · strength not stated · 1,552 dl · Description Clear colour home-security stills: a camera mounted high in a room corner looks down acr · [source](https://civitai.com/models/3015044?modelVersionId=3422347)
  - example prompt (from source, Euler, steps 50): `homecctvhd, A clear color CCTV still shows one wide room overview in a residential home. The full landscape frame is a single stationary camera feed, viewed obliquely acr` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e9fc284e-b490-4902-805c-dcb9a33db7ec/original=true/146458072.jpeg)
- `bodycam-view-vlogger-chest-cam-pov-moss` — trigger not stated · strength not stated · 666 dl · A chest-mounted action camera POV: a low, chest-height wide-angle frame facing the person who is tal · [source](https://civitai.com/models/3021452?modelVersionId=3430758)
- `underwater-action-cam-pool-sea-wide-angle-moss` — trigger not stated · strength not stated · 595 dl · Wide-angle frames from an action camera fully below the surface: sunlight refracted through moving w · [source](https://civitai.com/models/3019299?modelVersionId=3427960)

- Suggest ingest: [Upright straddle sex front view](https://civitai.com/models/82128) (sdxl, 59,134 dl) — `1boy, sex, hetero, upright straddle, straddling, girl on top` · strength `1.0` (stated) — **downloads 59134 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Cowgirl Position Sex Non-POV / Third Person](https://civitai.com/models/145887) (sdxl, 47,903 dl) — `1boy, sex, cowgirl position, girl on top, straddling` · strength not stated — **downloads 47903 >= 2x best available (7022) in same family+category**

### 26. Poses and body positions

**Illustrious / NoobAI (Illustrious-XL based)**
- `pose_femdom_pegging_nipple_tweak - v1.0 - pose_pegging_nipple_tweak` — `pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1b` · strength not stated · 3,470 dl · pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1boy, hetero, ejaculation, ejacu · [source](https://civitai.com/models/1295786?modelVersionId=1462424)
  - example prompt (from source, Euler a, steps 30): `masterpiece,best quality,amazing quality,official,  <lora:pose_pegging_nipple_tweak:1>  pose_pegging_nipple_tweak, nipple stimulation, nipple tweak, 1girl, 1boy, hetero, ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/dff3ca52-7d9c-4486-b3c3-b2708d10e186/original=true/60107192.jpeg)
- `jack-o-pose-sex-solo-ill` — `jko, jack-o' challenge,`, `top-down bottom-up,`, `rom behind,`, `1girl, solo,` · strength not stated · 3,062 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1373437?modelVersionId=1551797)
- `posefemale-pov-between-thighs-ill` — `povthighs, pov` · strength not stated · 2,820 dl · TAGS: povthighs, pov made using limited images, so it's not perfect! · [source](https://civitai.com/models/1334474?modelVersionId=1506855)

**SDXL**
- `gaping-assholes-all-fours-sdxl1-0-concept-xl` — `GapingAssholesAllFourQuiron pose`, `all fours`, `from behind`, `spread ass` · strength not stated · 7,022 dl · 👑 Gaping Assholes All Fours LORA 👑 SDXL1.0 v5.1p 🔧Model base: SDXL1.0 📝🌟 Trigger: (GapingAssholesAll · [source](https://civitai.com/models/130866?modelVersionId=143716)
  - example prompt (from source, Euler a, steps 40): `photo, 8k portrait of beautiful cyborg with brown hair, intricate, elegant, highly detailed, majestic, digital photography, art by artgerm and ruan jia and greg rutkowski` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/40ea32da-742e-4d42-a3d4-65d168412e6a/original=true/2099450.jpeg)
- `bathroom-booty-selfie-pose-sink-butt-influ-xl` — `Bo0ty_s3lfie_p0se` · strength not stated · 193 dl · Improve your AI influencer with a classic fan-favorite pose of the booty selfie (also called "sink b · [source](https://civitai.com/models/2406389?modelVersionId=2705689)
- `the-pose-prone-with-legs-crossed-il-sd-xl` — `Th3_p0se` · strength not stated · 171 dl · Makes "The Pose", have fun! · [source](https://civitai.com/models/1412908?modelVersionId=1597335)

**Pony (Pony Diffusion XL)**
- `assuplyingdown-pony` — `auok`, `assuponknees` · strength not stated · 2,790 dl · This is my first LORA, trained off only 11 images, so it's probably rubbish, but it seems to do what · [source](https://civitai.com/models/300336?modelVersionId=441302)
  - example prompt (from source, Euler a, steps 30): `score_9, score_8_up, score_7_up, (score_9:1.1), (score_8:1.1), score_7, 1girl, highly detailed, masterpiece, best quality, absurdres,  wide shot, full body shot, from sid` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c82bbcd1-4723-4f90-892d-df71b44d5698/original=true/9664357.jpeg)
- `jack-o-pose-sex-solo-pony` — `jko, jack-o' challenge,`, `top-down bottom-up,`, `rom behind,`, `1girl, solo,` · strength not stated · 627 dl · As requested, here's the LoRA. Comment or message me to let me know what to create next. I make what · [source](https://civitai.com/models/1373437?modelVersionId=1619238)
- `the-pose-prone-with-legs-crossed-il-sd-pony` — `Th3_p0se` · strength not stated · 626 dl · Makes "The Pose", have fun! · [source](https://civitai.com/models/1412908?modelVersionId=1597289)

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
- `upright-kneeling-moss` — `upright-kneeling` · strength not stated · 249 dl · try: she is is upright-kneeling additional: hands behind her head arching back knees apart Yes, I kn · [source](https://civitai.com/models/3030123?modelVersionId=3442126)

- Suggest ingest: [Pov sex looking down [Updated] (Missionary + doggy style + mating pres](https://civitai.com/models/423398) (illustrious, 51,864 dl) — `MLD, 1girl, 1boy, pov, lying down on ground, on back, straddling,`, `MPLD, 1girl, 1boy, pov, lying down on ground, on back, legs up,`, `DSLD, 1girl, 1boy, pov, lying down on ground, from behind, butt,`, `pinning, pov arms,` · strength not stated — **downloads 51864 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Reverse upright straddle / sitting on lap](https://civitai.com/models/114292) (pony, 41,344 dl) — `reverse upright straddle`, `legs together`, `spread legs` · strength not stated — **downloads 41344 >= 2x best available (8495) in same family+category**

### 27. Oral (blowjob, deepthroat, cunnilingus)

**Illustrious / NoobAI (Illustrious-XL based)**
- `fellatio-and-masturbation-ill` — `fellatio and masturbation, fellatio, female masturbation, 1boy, penis` · strength not stated · 11,460 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=1134882)
  - example prompt (from source, DPM++ 2M Karras, steps 25): `masterpiece,amazing quality,best quality,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,ultra-detailed-background,cute girl, eyelashes <lora:` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b096e211-882c-47d9-a170-9807b295ef2a/original=true/43975686.jpeg)
- `jav-hard-irrumatio-deepthroat-generator-ill` — `JAV_MISS572,  1girl, hetero, solo focus, tears, crying, saliva, snot, `, `bukkake, facial, excessive cum ,  close-up mouth , vomiting,` · strength `0.85 - 1` (stated) · 8,090 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/728512?modelVersionId=2115883)
- `extreme-deepthroat-irrumatio-ill` — `extremedeepthroat, extreme deep throat, :>=,  Tears, runny nose, drool` · strength not stated · 6,127 dl · The learning materials are available here. Please feel free to use them. https://mega.nz/file/ZkBEBA · [source](https://civitai.com/models/1873285?modelVersionId=2120316)

**SDXL**
- `blowjob-top-of-head-pov-sdxl1-0-xl` — `blowjobtopofheadpovQuiron` · strength not stated · 6,789 dl · 👑 Blowjob Top of Head POV - Lora 👑 SDXL1.0 ⚙️🔧Model base: SDXL1.0 ______________ 📝🌟 Trigger: blowjob · [source](https://civitai.com/models/125648?modelVersionId=1312598)
  - example prompt (from source, DPM++ 2M SDE, steps 38): `photo, photorealistic , realistic,  <lora:BlowjobTopofHeadPOVQuiron_v5:1> blowjobtopofheadpovQuiron, 1girl, 1boy,  big penis, fellatio, saliva,  oral sex, blowjob,  textu` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/4dfc5ef3-3a25-407a-8e91-14387210317f/original=true/53042504.jpeg)
- `blowjob-top-of-head-pov-sdxl1-0-xl-2` — `BlowjobTopofHeadPOVQuiron pose`, `a woman with a penis in her mouth`, `oral` · strength not stated · 1,075 dl · 👑 Blowjob Top of Head POV Lora SDXL1.0👑  v3 🔧Model base: SDXL1.0 _____________ 📝🌟 Trigger: BlowjobTo · [source](https://civitai.com/models/125648?modelVersionId=137273)
- `ahegao-facials-xl` — `ahegao_cumshot`, `ahegao_facial`, `eyes closed` · strength not stated · 872 dl · [source](https://civitai.com/models/2078761?modelVersionId=2352101)

**Pony (Pony Diffusion XL)**
- `fellatio-and-masturbation-pony` — `fellatio and masturbation`, `fellatio`, `female masturbation`, `fingering` · strength not stated · 11,628 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=616692)
  - example prompt (from source, DPM++ 2M, steps 25): `score_9, score_8_up, score_7_up,source_anime, high res image,ultra-detailed,8K,illustration,CG,shiny hair,clear skin,ultra-detailed-eyes,simple background,cute girl <lora` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c9bfaf09-0159-4ff4-b31f-08dfb2543a3d/original=true/53416934.jpeg)
- `jav-hard-irrumatio-deepthroat-generator-pony` — `JAV_MISS572,  1girl, hetero, solo focus, tears, crying, saliva, snot, ` · strength `0.85 - 1` (stated) · 11,159 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/728512?modelVersionId=814646)
- `xxx-hard-irrumatio-deepthroat-generator-il-pony` — `((facial)),(lube), cum on hair, cum on tongue, cum string, cum in mout`, `upside-down, lying back, Looking up , from above, facing up,`, `pov, pov penis, girl on boy, handjob, licking, open mouth,` · strength not stated · 7,049 dl · This LORA was created to see if it could learn XXX(SWALLOWED) and produce hentai anime. With LORA ap · [source](https://civitai.com/models/843783?modelVersionId=943981)

**Anima**
- `fellatio-and-masturbation-anima` — `fellatio and masturbation, 1girl, 1boy, penis,pussy` · strength not stated · 3,676 dl · The strength of Lora is recommended to be around 1.0. If you only use trigger words, it will be a no · [source](https://civitai.com/models/554142?modelVersionId=3000440)
  - example prompt (from source, Euler a, steps 20): `masterpiece,amazing quality,best quality,newest,absurdres,highres,highly-detailed,kawaii,cute,real skin,sharp draw lines  <lora:fellatio and masturbation:1> fellatio and ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/94f6dfe3-2d52-4070-b5b5-819a1af4dae3/original=true/132663275.jpeg)
- `deeper-penetration-deepthroat-and-somethin-anima` — `deep penetration`, `deepthroat`, `object insertion` · strength not stated · 2,412 dl · I trained this Lokr to solve the issue of not penetrate deep enough. However, I was too ambitious an · [source](https://civitai.com/models/2708641?modelVersionId=3042522)
- `jav-hard-irrumatio-deepthroat-generator-anima` — `JAV_MISS572,  1girl, solo focus, tears, crying, saliva, snot, drooling`, `bukkake, facial, excessive cum ,  close-up mouth , vomiting,` · strength `0.85 - 1` (stated) · 2,353 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/728512?modelVersionId=3230323)

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

- Suggest ingest: [Subtle Poses](https://civitai.com/models/1444070) (sdxl, 43,698 dl) — `cum`, `cum on body`, `cum in mouth`, `cum on breasts` · strength `0.25-0.75` (stated) — **downloads 43698 >= 2x best available (7022) in same family+category**
- Suggest ingest: [Pov Blowjob + Titjob + Handjob [updated]](https://civitai.com/models/446163) (illustrious, 40,457 dl) — `pov, 1girl, 1boy,`, `fellatio,`, `paizuri,`, `handjob,` · strength not stated — **downloads 40457 >= 2x best available (9704) in same family+category**
- Suggest ingest: [deep_penetration concept slider (for pony XL)](https://civitai.com/models/287556) (pony, 34,682 dl) — `vaginal`, `anal`, `deepthroat` · strength not stated — **downloads 34682 >= 2x best available (14402) in same family+category**

### 28. Sex positions (cowgirl, missionary, doggy, etc.)

Use ONE position LoRA per image.

**Illustrious / NoobAI (Illustrious-XL based)**
- `fucked-silly-xl` — `extreme sex` · strength `1` (stated) · 38,542 dl · 💖 Support & Share the Magic!  Love these tools? Like, add to collection, and tag this resource in yo · [source](https://civitai.com/models/1273929?modelVersionId=1613410)
  - example prompt (from source, Euler a, steps 30): `embedding:lazympos, extreme sex, 1girl, long hair, breasts, blush, shirt, large breasts, brown hair, 1boy, hat, brown eyes, braid, ass, hetero, sweat, nude, teeth, penis,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/192c0948-a62c-4768-a379-feca0f7eb88c/original=true/67550868.jpeg)
- `xxx-gangbang-group-sex-generator-evil-ange-ill` — `1girl, solo forcas, nude, 4+boys, Gangbang, Group Sex, Multiple Boys, ` · strength `0.9-0.6` (stated) · 14,416 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=2110029)
- `mating-press-wide-spread-focus-right-befor-ill` — `mating press`, `focus` · strength `1` (stated) · 13,255 dl · 💖 Support & Share the Magic!  Love these tools? Like, add to collection, and tag this resource in yo · [source](https://civitai.com/models/1280616?modelVersionId=1444772)

**SDXL**
- `sex-machine-sdxl` — `sex machine, restrained, bound, bdsm, stationary restraints, milking m` · strength not stated · 1,976 dl · The strength of Lora is recommended to be around 1.0. 使えそうなプロンプトをトリガーワードにいれましたので、好みで選択してください。 · [source](https://civitai.com/models/829330?modelVersionId=930213)
  - example prompt (from source, DPM++ 2M Karras, steps 15): `masterpiece,ultra-detailed,best quality,8K,illustration,cute face,clean skin ,shiny hair,girl,ultra-detailed-eyes,simple background, <lora:add-detail-xl:1> <lora:sex mach` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/76d856b5-b86c-4025-8de8-d3dff3e18dc7/original=true/33246351.jpeg)
- `trash-can-sex-garbage-can-sex-stuck-in-gar-xl` — `tr4sh-can-s3x, trash can, in container, stuck, lower body, ass, anus, ` · strength not stated · 344 dl · Your favorite character is stuck in a trash can. What's a guy to do 🤣. Have fun! · [source](https://civitai.com/models/1535973?modelVersionId=1737933)
- `dual-penetration-dap-xl` — `DPTP`, `DUAL ANAL PENETRATION` · strength not stated · 253 dl · v1 · [source](https://civitai.com/models/2567761?modelVersionId=2885205)

**Pony (Pony Diffusion XL)**
- `xxx-gangbang-group-sex-generator-evil-ange-pony` — `1girl, solo forcas, nude, Simple background,  depth of field, indoors,` · strength `0.9-0.6` (stated) · 14,402 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=732074)
  - example prompt (from source): `8image join to video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/67006c84-6a86-4492-a012-841d54cd6df1/original=true/33530717.jpeg)
- `hentai-gangbang-group-sex-after-sex-xl-spr-pony` — `group sex, after sex, hetero,6+boys,6+penises,veiny penis, 1girl, solo` · strength not stated · 8,000 dl · [source](https://civitai.com/models/581936?modelVersionId=649130)
- `hentai-gangbang-group-sex-gemuodou-gemuo-i-pony` — `gangbang, group sex, handjob, oral, fellatio, 6+boys, 6+penis, triple ` · strength not stated · 7,605 dl · Width:1216 Height:832 is best SAMPLE <LORA>Common prompts-- ---------------------------------------- · [source](https://civitai.com/models/575593?modelVersionId=641732)

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

- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**
- Suggest ingest: [Mating press](https://civitai.com/models/90532) (pony, 61,812 dl) — `mating press` · strength not stated — **downloads 61812 >= 2x best available (8495) in same family+category**
- Suggest ingest: [Upright straddle sex front view](https://civitai.com/models/82128) (sdxl, 59,134 dl) — `1boy, sex, hetero, upright straddle, straddling, girl on top` · strength `1.0` (stated) — **downloads 59134 >= 2x best available (7022) in same family+category**

### 29. Cum, fluids and aftermath

**Illustrious / NoobAI (Illustrious-XL based)**
- `facial-cumshot-225-xl` — `cumshot, facial, masturbation, ejaculation,`, `pov, pov hands` · strength not stated · 5,489 dl · 🔥 Facial cumshot LoRa for Illustrious 🔥 Hey everyone! This model focuses on creating images with a g · [source](https://civitai.com/models/1164568?modelVersionId=1310077)
  - example prompt (from source, Euler a, steps 30): `anime, masterpiece, best quality, 8k, 1girl, 1boy, arezu (pokemon) , <lora:cumshot:1>, cumshot, facial, masturbation, ejaculation, penis, pov, pov hands` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/be1cd1f6-dda0-4fa5-b3e9-3fb31eeaa565/original=true/52907093.jpeg)
- `doggystyle-view-from-behind-creampie-ill` — `facefocus_doggy,sex from behind,cumshot, cum drip, cum in pussy,lookin`, `arms behind back, restrained,` · strength `0.8` (stated) · 5,246 dl · lora for a doggystyle sex from behind view. A girl is force to look at her pussy and ejaculation. st · [source](https://civitai.com/models/1662410?modelVersionId=1881604)
- `hentai-comic-random-generator-last-orgasm-ill` — `comic,Multi view, Frame, Text, speech bubble, frame, heart, trembling,` · strength `0.5-1` (stated) · 4,290 dl · This model is specialized for randomly generating full-color 💗HARD CORE CREAMPIE & ORGASM LAST PAGE💗 · [source](https://civitai.com/models/2311348?modelVersionId=2600456)
- `MCB Lubed ill v2-15` **[HF repo only - needs adding to Graydient]** — trigger not stated · strength not stated · no source link

**SDXL**
- `pornmaster-projectile-cumejaculationcumsho-xl` — `projectile cum, penis,` · strength not stated · 4,139 dl · SDXL-V1培訓字幕excel檔案下載。 SDXL-V1 training subtitle excel file download. -- 培训图片包含男同性恋，要生成女性图片正面提示词放入女性聚 · [source](https://civitai.com/models/950655?modelVersionId=1064347)
  - example prompt (from source, DPM++ 2M, steps 25): `DSLR,a beautiful 18 year old Korean idol,projectile cum,multiple penises,multiple boys,(female focus),penis, hetero,gangbang,completely nude,breasts,nipples, flat chest ,` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e57dd4a1-99be-436c-9410-887a9337ad82/original=true/40260994.jpeg)
- `cumshot-xl` — trigger not stated · strength not stated · 455 dl · [source](https://civitai.com/models/1538069?modelVersionId=1740302)
- `toilet-slave-il-sd-xl` — `T0ilet-sl4ve, toilet, bound, bdsm` · strength not stated · 374 dl · [source](https://civitai.com/models/1561517?modelVersionId=1767032)

**Pony (Pony Diffusion XL)**
- `hentai-falling-into-the-toilet-girl-3-shot-pony` — `((3girls)), multiple views, multiple frame, (covered nipples),(covered` · strength not stated · 4,294 dl · This's LORA who turns cheeky girls into cum toilets.. Due to its structure, it is effective to gener · [source](https://civitai.com/models/677434?modelVersionId=758325)
  - example prompt (from source, DPM++ 2M Karras, steps 30): `(nsfw:1), (Uncensored:1),  score_9, score_8_up, score_7_up, best quality, masterpiece, 4k, uncensored, prefect lighting, rating_explicit, very aesthetic, source_anime, BR` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/53decf6d-bac8-4b0d-ab31-5886b021b08d/original=true/25742088.jpeg)
- `cumshots-meme-for-ponyxl-pony` — `cumshots meme` · strength not stated · 2,221 dl · Initial Version · [source](https://civitai.com/models/491746?modelVersionId=546832)
- `huge-facial-bukkake-ponyxl-xl-pony` — `nm_btrfacials,`, `facials,`, `bukkake,` · strength not stated · 2,063 dl · A Lora of Huge facial/bukkake trigger tag: NM_btrfacials, cum, facial, cum on hair, bukkake, excessi · [source](https://civitai.com/models/935204?modelVersionId=1305311)
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

- Suggest ingest: [NSFW POV All In One SDXL (Realistic/Anime/WD14 - 74MB Version Availabl](https://civitai.com/models/144203) (sdxl, 222,847 dl) — `blowjob`, `butterfly sex`, `cumshot`, `doggy style` · strength `0.5 - 0.8` (stated) — **downloads 222847 >= 2x best available (1779) in same family+category**
- Suggest ingest: [Bukkake / excessive cum](https://civitai.com/models/109745) (pony, 105,734 dl) — `excessive cum` · strength not stated — **downloads 105734 >= 2x best available (14402) in same family+category**
- Suggest ingest: [PornMaster-颜射，內射，精液滴下，精液，肛交後，做愛後-bukkake,creampie,cumdrip,cum,after an](https://civitai.com/models/96933) (illustrious, 77,853 dl) — `(realistic, real skin:1.2)`, `cum, bukkake, cum on her face`, `cum on glasses`, `creampie, cum in ass, cum in pussy, cum on crotch` · strength not stated — **downloads 77853 >= 2x best available (38542) in same family+category**

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
- `futa-handjob-female-xl` — `FutaHandjobFemale` · strength not stated · 190 dl · [source](https://civitai.com/models/1336319?modelVersionId=1509014)

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
- `base-pov-fingering-moss` — `p0v-f1ng3r1ng    pov view of a female viewer reaching hand between leg` · strength not stated · 323 dl · try: p0v-f1ng3r1ng pov view of a female viewer reaching hand between legs and fingering pussy slick  · [source](https://civitai.com/models/3050006?modelVersionId=3468343)
- `blow-up-sex-doll-inflatable-sex-toy-moss` — trigger not stated · strength not stated · 240 dl · Honestly I never saw a blow-up doll IRL 😅, this is just my take on Dollification porn CGI wirh an hy · [source](https://civitai.com/models/2993967?modelVersionId=3432220)

- Suggest ingest: [Multiple Boys - Concept](https://civitai.com/models/1431750) (illustrious, 23,068 dl) — `<lora:multiple-boys-v9-illustriousxl-lora-nochekaiser:1>, multiple boy` · strength `1.0` (stated) — **downloads 23068 >= 2x best available (9653) in same family+category**
- Suggest ingest: [SDXL dildo](https://civitai.com/models/138380) (sdxl, 19,591 dl) — `dildo`, `sex toy`, `vaginal object insertion`, `anal object insertion` · strength `0.2` (stated) — **downloads 19591 >= 2x best available (2431) in same family+category**
- Suggest ingest: [SexToy - Dildo](https://civitai.com/models/263021) (sdxl, 9,436 dl) — `See tag discription` · strength not stated — **downloads 9436 >= 2x best available (2431) in same family+category**

### 31. BDSM, bondage and restraints

Consensual adult scenes only.

**Illustrious / NoobAI (Illustrious-XL based)**
- `jav-hard-core-bdsm-generator-m-drag-m-ill` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 11,673 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=2106832)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7ac5ccf9-0ff9-4b84-bd54-19fdb756471f/original=true/93850194.mp4)
- `jav-hard-bdsm-generator-bondage-wall-il-xl-ill` — `1girl, legs up, m legs, licking, slave, spread legs, wide spread legs,`, `(oral), ((cunnilingus)), perfect hands, spread_pussy, male profile, to`, `Hands holding dildo, hands holding vibrator, Foreign object vaginal in`, `(pov), (sex),  large insertion, large penis, thick penis,` · strength not stated · 9,242 dl · This LORA was created to see if it could learn JAV and produce hentai anime. Width:832 Height:1216 i · [source](https://civitai.com/models/903161?modelVersionId=2117424)
- `Spooning Femdom Handjob Pegging Pony Illustrious - Illustrious - Spooning_Femdom_Handjob__Pegging_Pony__Illustrious-000058` — `Spooning, lying, on side, 1girl, 1boy, hetero, from above,`, `handjob, reach-around,`, `pegging, anal, strap-on, dildo,`, `hug from behind,` · strength not stated · 5,064 dl · Spooning Femdom for Pony & Illustrious · [source](https://civitai.com/models/1449583?modelVersionId=1639171)

**SDXL**
- `bondage-bdsm-xl` — `rope`, `black tape gag`, `bondage` · strength not stated · 21,468 dl · Training lora need more buzz, give me support! Please leave a review if you like this lora！ ver. “花と · [source](https://civitai.com/models/136849?modelVersionId=150991)
  - example prompt (from source, DPM++ 2M SDE Karras, steps 30): `breathtaking 1girl,rope over clothes,bound,pubic hair,cum in pussy,wet body,arms behind back,masterpiece,best quality,highly detailed, <lora:zzy_SDXL_1_:1>,zzy, <lora:bds` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/052ce9a0-fd5a-40b1-978b-3e3447d46092/original=true/2258502.jpeg)
- `femdom handjob SDXL - SDXL v1.0 - femdom handjob SDXL_epoch_19` — trigger not stated · strength `0.6` (stated) · 403 dl · Try a strength between 0.6 and 1.0. · [source](https://civitai.com/models/2570715?modelVersionId=2888449)
- `step-sis-bdsm-bondage-simulator-xl` — `step-sis_bound` · strength not stated · 181 dl · [source](https://civitai.com/models/3010878?modelVersionId=3416954)

**Pony (Pony Diffusion XL)**
- `jav-hard-core-bdsm-generator-m-drag-m-pony` — `1girl, solo forcas, nude, Simple background, black background, depth o`, `deepthroat,oral,Portrait, (close-up face), Crying, tears, cum, facial,`, `deepthroat,oral,cowboy shot, toilet, forehead, cock in mouth, Stringy `, `after fellatio, Portrait,(close-up mouth), tongue, foam, open mouth, (` · strength `0.85 - 1` (stated) · 12,530 dl · ⬇️2026 Anima model⬇️ ⚠️The Anima model is trained using the same training image data as the Illustri · [source](https://civitai.com/models/645017?modelVersionId=721539)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/910fd244-2bc4-4925-877e-da98725e43c3/original=true/33533282.jpeg)
- `jav-hard-bdsm-generator-bondage-wall-il-xl-pony` — `1girl, legs up, m legs, licking, slave, spread legs, wide spread legs,`, `(oral), ((cunnilingus)), perfect hands, spread_pussy, male profile, to`, `Hands holding dildo, hands holding vibrator, Foreign object vaginal in`, `(pov), (sex),  large insertion, large penis, thick penis,` · strength not stated · 9,515 dl · This LORA was created to see if it could learn JAV and produce hentai anime. Width:832 Height:1216 i · [source](https://civitai.com/models/903161?modelVersionId=1015638)
- `0565-bdsm-clothing-1-pony` — `ruanyi0565,bdsm,white bondage outfit,barbell piercing,choker,clitoris ` · strength not stated · 3,844 dl · 0.9 · [source](https://civitai.com/models/465238?modelVersionId=517724)

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

- Suggest ingest: [Bondage Suspension](https://civitai.com/models/8762) (illustrious, 92,975 dl) — `suspension` · strength not stated — **downloads 92975 >= 2x best available (38542) in same family+category**
- Suggest ingest: [Erza Scarlet (All Armors & Outfits) (61 Outfits) / Illustrious](https://civitai.com/models/902174) (illustrious, 21,556 dl) — `erz_bwaitress, brown eyes, red hair, long hair, hair over one eye, fak` · strength `0.8 - 1` (stated) — **downloads 21556 >= 2x best available (6777) in same family+category**
- Suggest ingest: [Slave Restraints](https://civitai.com/models/151223) (sdxl, 17,090 dl) — `slave_restraints outfit` · strength not stated — **downloads 17090 >= 2x best available (1359) in same family+category**

### 32. Multiple partners, gangbang, threesome

**Illustrious / NoobAI (Illustrious-XL based)**
- `xxx-gangbang-group-sex-generator-evil-ange-ill` — `1girl, solo forcas, nude, 4+boys, Gangbang, Group Sex, Multiple Boys, ` · strength `0.9-0.6` (stated) · 14,416 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=2110029)
  - example prompt (from source): `8img join 2 video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b8d53e55-5802-493e-8eaa-5b2b1ca9b559/original=true/94045066.mp4)
- `spitroast-foot-xl` — `prone bone`, `on stomach`, `defeat`, `humiliation` · strength not stated · 6,956 dl · Ohayo, my hot and kinky people 🔥😈!, I find myself needing to use this intro from now on for my origi · [source](https://civitai.com/models/1336016?modelVersionId=1508669)
- `hentai-gangbang-group-sex-gemuodou-gemuo-i-ill` — `gemuo, gangbang, group sex, handjob, oral, fellatio, 6+boys, 6+penis, ` · strength not stated · 6,787 dl · Width:1216 Height:832 is best SAMPLE <LORA>Common prompts-- ---------------------------------------- · [source](https://civitai.com/models/575593?modelVersionId=2118824)
- `suze-group_epoch_10-ill` **[HF repo only - needs adding to Graydient]** _(epoch-only)_ — trigger not stated · strength not stated · no source link

**SDXL**
- `straining-expression-il-sd-flux-xl` — `str4in, clenched teeth, sweating, blushing, drool, eyes rolling up` · strength not stated · 240 dl · [source](https://civitai.com/models/1246430?modelVersionId=1405076)
  - example prompt (from source, DDIM, steps 30): `Score_9, score_8_up, score_7_up, str4in, clenched teeth, sweating, blushing, drool, eyes rolling up, 1girl, teeth, green eyes, long hair, solo, saliva, rolling eyes, blac` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d96e67b5-a7e8-465a-937e-376bf465029b/original=true/57472876.jpeg)
- `double-dildo-deepthroat-il-z-sd-xl` — `Double_dildo_deepthroat` · strength not stated · 129 dl · Have two characters deepthroat a double dildo together. Have fun! · [source](https://civitai.com/models/2356803?modelVersionId=2650703)
- `double-barrel-blowjob-double-blowjob-2-dic-xl` — `Double_barrel_blowjob, double blowjob` · strength not stated · 117 dl · One dick isn't enough for her mouth, so feed her two with a double barrel blowjob. Have fun! · [source](https://civitai.com/models/2392768?modelVersionId=2690433)

**Pony (Pony Diffusion XL)**
- `xxx-gangbang-group-sex-generator-evil-ange-pony` — `1girl, solo forcas, nude, Simple background,  depth of field, indoors,` · strength `0.9-0.6` (stated) · 14,402 dl · This LORA was created to see if it could learn XXX(Evil Engel) and produce hentai anime. With LORA a · [source](https://civitai.com/models/654360?modelVersionId=732074)
  - example prompt (from source): `8image join to video` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/67006c84-6a86-4492-a012-841d54cd6df1/original=true/33530717.jpeg)
- `hentai-gangbang-group-sex-after-sex-xl-spr-pony` — `group sex, after sex, hetero,6+boys,6+penises,veiny penis, 1girl, solo` · strength not stated · 8,000 dl · [source](https://civitai.com/models/581936?modelVersionId=649130)
- `hentai-gangbang-group-sex-gemuodou-gemuo-i-pony` — `gangbang, group sex, handjob, oral, fellatio, 6+boys, 6+penis, triple ` · strength not stated · 7,605 dl · Width:1216 Height:832 is best SAMPLE <LORA>Common prompts-- ---------------------------------------- · [source](https://civitai.com/models/575593?modelVersionId=641732)

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

**MOSS (Moss Image / kromoss)**
- `trio-for-threesomes-moss` — trigger not stated · strength not stated · 305 dl · Trio is a Krea 2 LoRA trained on 153 captioned images of threesomes.  Start your prompt with one of  · [source](https://civitai.com/models/3040250?modelVersionId=3475732)
  - example prompt (from source, er_sde, steps 25): `Vertical editorial cover, photographed from directly overhead. A small jacuzzi pool sits on a dark, weathered concrete floor. Exactly three adults relax in the shallow wa` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b29b9c6d-ae50-4246-957c-bf02cffaac2c/original=true/149258881.jpeg)

- Suggest ingest: [Multiple insertion / penetration](https://civitai.com/models/89125) (pony, 36,633 dl) — `multiple penetrations`, `multiple insertions`, `anal object insertion`, `vaginal object insertion` · strength not stated — **downloads 36633 >= 2x best available (14402) in same family+category**
- Suggest ingest: [Fondled](https://civitai.com/models/705447) (illustrious, 30,962 dl) — `1girl surrounded by males, girl sandwiched by boys, group, multiple bo`, `groping,`, `breast grab,`, `fingering,` · strength `0.5-0.8` (stated) — **downloads 30962 >= 2x best available (9704) in same family+category**
- Suggest ingest: [Mtu Virus](https://civitai.com/models/57573) (illustrious, 29,967 dl) — `mtu virus`, `multiple views` · strength not stated — **downloads 29967 >= 2x best available (9653) in same family+category**

### 33. Backgrounds, rooms and environments

**Illustrious / NoobAI (Illustrious-XL based)**
- `backgroundpurple-nightclub-ill` — `nightclub` · strength not stated · 3,749 dl · The 'nightclub' tag works in regular Illustrious, but I wanted something slightly more defined and p · [source](https://civitai.com/models/1232013?modelVersionId=1388252)
  - example prompt (from source, DPM++ 2M, steps 20): `perfect quality, best quality, masterpiece, 1girl, solo, mature female, large breasts, brown eyes, Platinum hair, Curly Bob, short dress, bodycon, smile, blush, contrappo` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/86fe9418-cea8-4e88-8391-50241d080fb9/original=true/56589699.jpeg)
- `jav-1girl-1boy-hetero-bathroom-pov-sex-gen-ill` — `1girl, nude, solo focus, looking at viewer, wet body,  1boy, pov sex, ` · strength not stated · 3,470 dl · This LoRa has learned JAV of Japanese style bathroom POV SEX. ❤In Japan, if you rent a private bathr · [source](https://civitai.com/models/2089710?modelVersionId=2364345)
- `wearing-clothes-changing-room-hentai-manga-ill` — `((wearing clothes)), 4koma:1.3, multiple views, ((Underwear only view)` · strength not stated · 2,738 dl · Thank you 1016183941431. for the good suggestion. This LoRa generates the appearance of wearing clot · [source](https://civitai.com/models/2013516?modelVersionId=2278867)

**SDXL**
- `atomicpunk-interior-buildings-ad-xl` — `AtoPunInt`, `interior` · strength not stated · 47 dl · [source](https://civitai.com/models/2949992?modelVersionId=3340943)
  - example prompt (from source, Euler a, steps 35): `very awa, aesthetically pleasing, masterpiece, best quality, Clean Composition, dutch angle, in'ei, chiaroscuro, 8K, HDR, CGI, interior, <lora:AtoPunInt_(Buildings)_(SDXL` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/309e9d53-8a18-4d88-87f4-1ce6c0d284b0/original=true/143249968.jpeg)
- `miami-beach-hotel-interior-background-ad-xl` — `MiaBeaHotInt`, `interior` · strength not stated · 35 dl · [source](https://civitai.com/models/2819289?modelVersionId=3180166)
- `Penthouse Floor Window Lifestyle Scene Backdrop SDXL LoRA - v1.0 - scene_penthouse_floor_window_v1` — trigger not stated · strength not stated · 32 dl · [source](https://civitai.com/models/2871727?modelVersionId=3244663)

**Pony (Pony Diffusion XL)**
- `milf-city-sexy-milfs-mature-moms-and-couga-pony` — `MilfCity` · strength not stated · 629 dl · I wanted a good MILF lora that could do both elegant and trashy older women. Have fun. Be responsibl · [source](https://civitai.com/models/1983105?modelVersionId=2244787)
  - example prompt (from source, Euler a, steps 18): `score_9, score_8_up, score_7_up,   MilfCity, 1girl, breasts, jewelry, solo, cleavage, necklace, huge breasts, sagging breasts, dark dress, loose dress, freckles, curvy, t` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/82e1c063-d54c-4fc3-bb8d-37e54289fbe0/original=true/102059064.jpeg)
- `miami-beach-hotel-bedroom-background-ad-pony` — `MiaBeaHotBed`, `hotel bedroom`, `interior` · strength not stated · 77 dl · [source](https://civitai.com/models/2819331?modelVersionId=3180223)
- `steelpunk-interior-architecture-buildings-pony` — `StePunInt`, `interior` · strength not stated · 52 dl · [source](https://civitai.com/models/2914191?modelVersionId=3296717)

**Anima**
- `japanese-school-hallway-background-ad-anima` — `JapHal` · strength `0.8 to 1.25` (stated) · 328 dl · This is an Anima lora for Japanese School Hallway backgrounds. The samples largely came from anime l · [source](https://civitai.com/models/2976615?modelVersionId=3373714)
  - example prompt (from source, ER SDE, steps 32): `<lora:training_1850035-20261001044740066-seds:0.8> JapHal, interior, school hallway, Masterclass illustration, anime. An interior view of a Japanese highschool hallway. W` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/095d8708-813f-45f3-8b48-c89502006895/original=true/144355745.jpeg)
- `meeting-room-anima` — `m33t1ng`, `indoors, long table, window, chairs, ceiling light, cityscape` · strength not stated · 305 dl · Creates a meeting room / board room background Trigger: m33t1ng Additional: indoors, long table, win · [source](https://civitai.com/models/2956232?modelVersionId=3348667)
- `t-rex-studio-t-rex-animation-style-anima` — `TRexStudio` · strength not stated · 304 dl · Based on T-Rex Animation Studio. Have fun! · [source](https://civitai.com/models/2815365?modelVersionId=3175311)

**Krea2 (detailed-krea2)**
- `Nightmare_Grunge_Krea_2_Version_epoch_9` — trigger not stated · strength `0.5 to 1` (stated) · 1,769 dl · Many models are very "clean" and "bright"- grunge, dirt, darkness and atmospheric horror details are · [source](https://civitai.com/models/2804228?modelVersionId=3161763)
  - example prompt (from source, Euler, steps 12): `A high-resolution anime-style masterpiece depicting a lone female figure with long black hair reclining in a cluttered, dimly lit bathroom at night, surrounded by cracked` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/da60c806-fd9f-40a4-ab61-93a0e586ad64/original=true/137713903.jpeg)
- `cuckold-scene-concept-krea2` — `cuckold session` · strength not stated · 1,295 dl · Cuckold / hotwife concept LoRA for photorealistic multi-person scenes. Trained to reproduce cuckold  · [source](https://civitai.com/models/2893135?modelVersionId=3271126)
- `cctv-room-krea2` — `cctvfootage` · strength not stated · 717 dl · About this version v2 focuses on better prompt adherence and more precise control through detailed d · [source](https://civitai.com/models/2992439?modelVersionId=3393441)

**MOSS (Moss Image / kromoss)**
- `realistic-night-outdoor-photo-real-streetl-moss` — trigger not stated · strength not stated · 363 dl · Photos taken outdoors at night: bus stops, street food stalls, canal railings, parking lots, rooftop · [source](https://civitai.com/models/3048122?modelVersionId=3465868)
  - example prompt (from source, er_sde, steps 35): `nightoutdoorphoto, a 23-year-old Korean woman wearing a muted red jacket eating a skewer at a street food stall, smiling at the camera, outdoors at night Everyone in the ` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/aba86727-6c74-4d60-8302-7357c08a287a/original=true/148742137.jpeg)
- `backrooms-endless-yellow-rooms-moss` — trigger not stated · strength `0.8` (stated) · 233 dl · The Backrooms as the original lore pictures them: mono-yellow wallpaper, damp beige carpet, humming  · [source](https://civitai.com/models/3029551?modelVersionId=3441279)
- `fourth-wall-interior-a-dollhouse-cutaway-b-moss` — trigger not stated · strength not stated · 233 dl · The whole front wall of a building removed like a dollhouse, seen straight on at eye level: every ro · [source](https://civitai.com/models/3037640?modelVersionId=3451923)

- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (24024) in same family+category**
- Suggest ingest: [T-Rex Studio V2 NEW!!- Hentai +18 - / STYLE / PONY XL / Illustrious XL](https://civitai.com/models/960593) (illustrious, 76,380 dl) — `TRexStyle,,`, `(anime coloring, anime screencap), shiny skin,,` · strength not stated — **downloads 76380 >= 2x best available (24024) in same family+category**
- Suggest ingest: [Dark Ghibli Fairytales](https://civitai.com/models/1349631) (anima, 26,891 dl) — `Studio Ghibli Dark Fairytale` · strength not stated — **downloads 26891 >= 2x best available (10402) in same family+category**

### 34. Character sheets, multi-view, reference layouts

**Illustrious / NoobAI (Illustrious-XL based)**
- `character-design-sheet-flux-ill` — `multiple views`, `characterDesignSheetQuiron`, `characterDesignSheetxQuiron` · strength `0.7 - 1.3` (stated) · 5,338 dl · 👑 Character design sheet - Illustrious - LORA 👑 ⚙️🔧Model base: Illustrious Based on Illustrious this · [source](https://civitai.com/models/834362?modelVersionId=1838736)
  - example prompt (from source, DPM++ 2M SDE, steps 22): `, masterpiece, best quality,  <lora:characterDesignSheetQuiron_illus:1>   characterDesignSheetQuiron,   standing, full body,  multiple views, Elsa (Frozen): Elsa's flowin` · [example image](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f254bb52-07e9-4a15-b978-bba0bdf45cc7/original=true/78806439.jpeg)
- `reference-sheet-illustriousxl-lora-nochekaiser` — `<lora:reference-sheet-illustriousxl-lora-nochekaiser:1>, reference she` · strength `1.0` (stated) · 1,180 dl · Order a commission here! https://www.fiverr.com/s/vvE412e Support my work by subscribing to patreon! · [source](https://civitai.com/models/2799724?modelVersionId=3156120)
- `conceptreference-sheet-with-clothes-shoes-ill` — `reference sheet, close-up, multiple views, clothes focus, footwear foc` · strength not stated · 901 dl · This will generate reference sheets with images on the side focusing on different stuff. TAGS: refer · [source](https://civitai.com/models/2403343?modelVersionId=2702274)

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
- Suggest ingest: [Character Design Sheet (HELPER) (3-PERSPECTIVES)+(COLOR PALETTE) - Z-I](https://civitai.com/models/100435) (illustrious, 103,141 dl) — `CharacterDesignIllustrious,,`, `reference sheet, simple white background, (color guide:1.2), (multiple` · strength not stated — **downloads 103141 >= 2x best available (24024) in same family+category**
- Suggest ingest: [character sheet](https://civitai.com/models/368139) (pony, 30,253 dl) — trigger not stated · strength not stated — **downloads 30253 >= 2x best available (7066) in same family+category**
