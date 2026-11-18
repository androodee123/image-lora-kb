"""Shared helpers for the image-lora-kb scripts (families, categories, safety filters)."""
from __future__ import annotations
import re

FAMILIES = ["illustrious", "sdxl", "pony", "anima", "krea2", "moss"]
FAMILY_LABEL = {
    "illustrious": "Illustrious / NoobAI (Illustrious-XL based)", "sdxl": "SDXL", "pony": "Pony (Pony Diffusion XL)",
    "anima": "Anima", "krea2": "Krea2 (detailed-krea2)", "moss": "MOSS (Moss Image / kromoss)",
}
GRAYDIENT_REPOS = ("Octavian123/civit", "Octavian123/civit2", "Octavian123/private")

# CivitAI baseModel -> family (None = out of scope)
def family_from_base(b: str | None):
    b = (b or "").lower()
    if not b:
        return None
    if "illustrious" in b or "noobai" in b:
        return "illustrious"
    if b.startswith("anima"):
        return "anima"
    if "moss" in b:
        return "moss"
    if "krea" in b:
        return "krea2"
    if b.startswith("pony"):
        return "pony"
    if b.startswith("sdxl") or b in ("sdxl turbo", "sdxl lightning", "sdxl hyper"):
        return "sdxl"
    return None

OUT_OF_SCOPE_TOKENS = ("flux2", "flux-2", "flux1", "qwen", "zimage", "z-image", "wan", "h3", "ltx", "hunyuan", "video", "sd15", "sd1.5", "flux")

def family_from_name(name: str):
    """Return (family|None, out_of_scope_label|None) from a file name. Conservative."""
    n = name.lower()
    toks = set(re.split(r"[^a-z0-9.]+", n))
    if "krea2" in n or "krea-2" in n or ("krea" in toks and "flux" not in toks):
        return "krea2", None
    if "anima" in toks or n.endswith("-anima") or "_anima" in n or "anima_" in n:
        return "anima", None
    if "moss" in toks or "kromoss" in n:
        return "moss", None
    if toks & {"ill", "illustrious", "il", "noob", "noobai", "illust"} or "illustrious" in n:
        return "illustrious", None
    if "pony" in toks or "ppp" in toks:
        return "pony", None
    if "sdxl" in toks:
        return "sdxl", None
    for t in ("flux2", "flux", "qwen", "zimage", "wan", "h3", "ltx", "video", "hunyuan"):
        if t in toks:
            return None, t
    return None, None

# ---- epoch / training-checkpoint detection ------------------------------------------------
EPOCH_RE = re.compile(r"(?:[-_ .]?epoch[ _-]?\d+|[-_.]0{2,}\d{4,}|[-_]\d{6}|\.TA_trained|[-_ ]?v\d+e\d+|[-_]e\d{1,3}(?:_s\d+)?|[-_]\d{1,2}$|[-_ ]?000\d+)", re.I)

def epoch_group(stem: str):
    """If stem looks like an intermediate training epoch, return (group_key, epoch_number)."""
    s = stem
    m = re.search(r"(?:^|[-_ .])(?:epoch[ _-]?|e)(\d{1,3})(?:_s\d+)?(?:\.TA_trained)?$", s, re.I)
    if m:
        return s[:m.start()].rstrip("-_ ."), int(m.group(1))
    m = re.search(r"[-_.](0{2,}\d{3,})(?:\.TA_trained)?$", s) or re.search(r"[-_](\d{6})(?:\.TA_trained)?$", s)
    if m:
        return s[:m.start()].rstrip("-_ ."), int(m.group(1))
    m = re.search(r"v\d+e(\d{1,3})$", s, re.I)
    if m:
        return s[:m.start()].rstrip("-_ ."), int(m.group(1))
    m = re.search(r"\.TA_trained$", s)
    if m:
        return s[:m.start()].rstrip("-_ ."), 0
    m = re.search(r"[-_ ]epoch[ _-]?(\d+)", s, re.I)
    if m:
        return s[:m.start()].rstrip("-_ ."), int(m.group(1))
    return None, None

# ---- safety: adults only ------------------------------------------------------------------
MINOR_RE = re.compile(r"\b(loli(?!ta)\w*|shota(?!ro)\w*|toddler|underage|under[- ]age|preteen|pre[- ]teen)\b", re.I)  # hard exclusions only; everything else is flagged minor_coded by semantic.py
FORBIDDEN_ID_RE = re.compile(r"youngandrew|handyandy|andrewyoung|andy\.?young", re.I)

def minor_reason(*texts: str):
    for t in texts:
        if not t:
            continue
        if FORBIDDEN_ID_RE.search(t):
            return "forbidden identity (youngandrew/handyandy/andrewyoung)"
        m = MINOR_RE.search(t)
        if m:
            return f"possible minor-coded term: {m.group(0)}"
    return None

# ---- categories ---------------------------------------------------------------------------
CATEGORIES = ["character", "style", "anatomy", "clothing", "pose-composition", "lighting",
              "quality-detail", "nsfw-act", "concept", "utility"]
KW = {
    "utility": r"slider|turbo|lightning|distill|hyper[- ]?(sd|xl|lora)?|accelerat|\blcm\b|speed[- ]?up|lightx2v|fix(er)?\b|upscal|merge|remap|adapter|controlnet|\bdmd",
    "quality-detail": r"detail|quality|aesthetic|realism|realistic|skin|texture|enhanc|stabiliz|sharp|hires|high[- ]?res|photoreal|film grain|boost|refin|\bhdr\b|amateur|candid|iphone|polaroid",
    "lighting": r"light(ing|s)?\b|shadow|neon|sunset|sunrise|rim[- ]light|glow|bokeh|golden hour|volumetric|chiaroscuro|backlit|studio light",
    "nsfw-act": r"blowjob|fellatio|sex\b|sexual|cum\b|cumshot|creampie|bukkake|facial|penetrat|anal\b|doggy|cowgirl|missionary|handjob|titjob|paizuri|footjob|orgasm|masturbat|fingering|cunnilingus|gangbang|deepthroat|ejaculat|squirt|bdsm|bondage|threesome|orgy|hentai sex|fuck|spitroast|reverse cowgirl|prone bone|sixty|69\b|rimjob|gokkun|piledriver|mating press|stuck in|glory ?hole|pegging|hetero",
    "anatomy": r"breast|boob|nipple|areola|penis|cock\b|dick|balls|scrotum|testicle|clit|labia|pussy|vagina|vulva|anus|foreskin|futa|abs\b|muscle|belly|navel|thigh|hips?\b|ass\b|butt|body|feet|foot|toes?|hands?\b|fingers?|tongue|eyes?\b|face\b|lips|teeth|armpit|collarbone|hair\b|tan lines?|stretch mark|veins?|cleavage|pubic",
    "clothing": r"dress|lingerie|bikini|swimsuit|stocking|thigh[- ]?high|latex|corset|heels?\b|panties|panty|\bbra\b|uniform|costume|outfit|kimono|bodysuit|cosplay|socks?\b|gloves?|shoes?|boots?|hat\b|glasses|mask|collar|harness|leotard|apron|jeans|skirt|shorts|leggings|sweater|hoodie|jacket|coat|cape|armor|fishnet|garter|nightgown|robe|towel|bandage|piercing|jewel|choker|condom|chastity|cockring|cock ring|buttplug|plug\b",
    "pose-composition": r"pose|angle|\bpov\b|view\b|from behind|from below|from above|close[- ]?up|framing|composition|selfie|perspective|wide shot|upskirt|camera|full[- ]body|portrait|layout|lying|kneeling|squatting|sitting|standing|spread|split\b|bent over|all fours|\bdutch\b|fisheye|panorama|multiple views|reference sheet|character sheet",
    "style": r"\bstyle\b|art ?style|artstyle|anime|painting|watercolor|comic|retro|\b[1-9]0s\b|manga|doujin|pixel|sketch|illustration|oil paint|cartoon|3d render|\bcg\b|ukiyo|impressionis|vaporwave|cyberpunk|synthwave|aesthetic|artist|by [a-z]+|vintage|noir|gothic|fantasy|sci-?fi|horror|movie|film\b|cinematic|photography",
    "character": r"character|celebrity|actress|model\b|idol|person|\bwoman\b|\bgirl\b|real person|cosplayer|waifu|hololive|genshin|pokemon|fate/|from [a-z ]+ \(|vtuber|\bnami\b|persona",
}
TAG_MAP = {"character": "character", "celebrity": "character", "person": "character", "real person": "character",
           "style": "style", "art style": "style", "artstyle": "style", "anime": "style", "clothing": "clothing", "clothes": "clothing",
           "pose": "pose-composition", "poses": "pose-composition", "concept": "concept", "sex position": "nsfw-act", "sex-positions": "nsfw-act",
           "porn": "nsfw-act", "anatomy": "anatomy", "body": "anatomy", "background": "lighting", "photorealistic": "quality-detail",
           "realistic": "quality-detail", "detail": "quality-detail", "tool": "utility", "slider": "utility", "lighting": "lighting"}

def categorize(name: str, tags: list[str] | None, description: str = "") -> str:
    name_l = (name or "").lower().replace("_", " ").replace("-", " ")
    desc_l = (description or "")[:300].lower()
    scores = {c: 0 for c in CATEGORIES}
    for c, pat in KW.items():
        rx = re.compile(pat, re.I)
        if rx.search(name_l):
            scores[c] += 3
        if rx.search(desc_l):
            scores[c] += 1
    for t in tags or []:
        c = TAG_MAP.get(t.lower())
        if c:
            scores[c] += 2
    # priority tie-break order
    order = ["utility", "nsfw-act", "character", "clothing", "anatomy", "pose-composition", "lighting", "quality-detail", "style", "concept"]
    best = max(order, key=lambda c: (scores[c], -order.index(c)))
    return best if scores[best] > 0 else "concept"

STRENGTH_RE = re.compile(r"(?:(?:recommended|suggested|best|ideal|optimal|works? (?:well|best))?\s*(?:lora\s*)?(?:strength|weight|scale|str)\b|<lora:[^>:]+:)\s*(?:is|of|:|=|at|around|between|from)?\s*([0-9]*\.?[0-9]+(?:\s*(?:-|–|to)\s*[0-9]*\.?[0-9]+)?)", re.I)

def extract_strength(*texts: str):
    """Return strength string ONLY if the source text states one. Else ''."""
    for t in texts:
        if not t:
            continue
        t2 = re.sub(r"<[^>]+>", lambda m: m.group(0) if m.group(0).lower().startswith("<lora:") else " ", t)
        t2 = re.sub(r"\s+", " ", t2)
        for m in re.finditer(r"(?:strength|weight|scale)\b[^0-9<]{0,30}?([0-9]*\.?[0-9]+(?:\s*(?:-|–|to)\s*[0-9]*\.?[0-9]+)?)", t2, re.I):
            v = m.group(1).strip()
            try:
                hi = float(re.split(r"-|–|to", v)[-1])
            except Exception:
                continue
            if 0 < hi <= 2.5:
                return v
    return ""
