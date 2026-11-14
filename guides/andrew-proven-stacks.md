# Andrew's proven stacks (from his own skills; adults only)

## detailed-krea2 (minekrea rules)
`/workflow /run:detailed-krea2 /size:1536x1920 /images:1 <identity:0.7> <anatomy-assist:0.7> <concept:0.7> <style:0.7> triggers..., natural-language scene`

- Size: 1536x1920 for one person; 1920x1536 for two or more people, rooms, wide scenes. Never 1024x1024 unless asked.
- Bracket order: identities, anatomy assists, concepts, style/look. Slugs only inside `<>`; triggers after all brackets in the same order.
- Weight 0.7 unless the catalog line states a strength (minekrea: nude "me" penis LoRA `mypeniserect-krea2` is always 0.4; Cyber-shot uses 1.2).
- Anatomy assists named by minekrea: visible penis -> `<penis-krea2:0.7>` trigger `p3n15`; penetration -> `<penetration-control-v2-krea2:1.2>`; semen -> `<real-cum-4k-krea2:1.0>`; nude marie -> `<marie-pussyassist-krea2>`.
- Prose paragraph in order: camera/composition, who, action, clothing, place, light last. Put readable text in "quotes". No `/seed`, `/steps`, `/guidance` unless asked.

## kromoss still (benchmark run Andrew marked HIGHLY successful, Nov 2026)
`/workflow /run:kromoss /size:1536x1536 /steps:40 /guidance:3.5 /images:2` + tag prompt (`(uncensored, explicit full body photo), score_9, best quality pinup photography, ...`) + `[[censorship, emoji, watermark, website, bad anatomy, worst quality]]` + LoRAs `<mcbcore-moss:0.8> <condom-moss:0.4> <andrdpna-moss:0.4> <suze-moss:0.1> <face-moss:0.4>`.
Keep the identity LoRA highest; name condom details explicitly (transparent latex, glossy, tip state); full body in frame, eye-level.
