#!/usr/bin/env python3
import re
import sys
from pathlib import Path

BLOG_DIR = Path("blog")
APPLY = "--apply" in sys.argv

EMOJI_PATTERN = re.compile(
    r'^[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]+\s*'
)

def clean(text):
    text = EMOJI_PATTERN.sub('', text.strip())
    text = re.sub(r'\s*[-—|]\s*(Blog\s+)?Synaptika\s*$', '', text, flags=re.IGNORECASE)
    return text.strip()

def title_from_description(desc):
    desc = clean(desc)
    # coupe sur le premier vrai séparateur de clause
    for sep in [' : ', ' – ', ' — ', ' - ']:
        if sep in desc:
            candidate = desc.split(sep)[0].strip()
            if 15 <= len(candidate) <= 90:
                return candidate
    if '. ' in desc:
        candidate = desc.split('. ')[0].strip()
        if 15 <= len(candidate) <= 90:
            return candidate
    if len(desc) <= 90:
        return desc
    truncated = desc[:87].rsplit(' ', 1)[0]
    return truncated + '…'

changed, skipped = [], []

for html_file in sorted(BLOG_DIR.glob("*.html")):
    content = html_file.read_text(encoding="utf-8")
    title_match = re.search(r'<title>([^<]*)</title>', content)
    if not title_match:
        skipped.append((html_file.name, "aucune balise <title>"))
        continue
    old_title = title_match.group(1)

    ACCENT = re.compile(r"[éèêëàâäîïôöùûüçÉÈÊËÀÂÄÎÏÔÖÙÛÜÇ]")
    if ACCENT.search(old_title):
        continue  # titre deja accentue -> on ne touche pas, meme si different

    og_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)

    if og_match:
        base = clean(og_match.group(1))
        source = "og:title"
    elif desc_match:
        base = title_from_description(desc_match.group(1))
        source = "description"
    else:
        skipped.append((html_file.name, "ni og:title ni description trouvés"))
        continue

    new_title = f"{base} | Synaptika"

    if old_title.strip() == new_title.strip():
        continue

    changed.append((html_file.name, old_title, new_title, source))

    if APPLY:
        new_content = content.replace(
            f"<title>{old_title}</title>",
            f"<title>{new_title}</title>",
            1
        )
        html_file.write_text(new_content, encoding="utf-8")

print(f"{'APPLIQUE' if APPLY else 'APERCU (aucune modification -- relance avec --apply)'}")
print(f"{len(changed)} fichier(s) a corriger, {len(skipped)} ignore(s)\n")

for name, old, new, source in changed:
    print(f"  {name}  [source: {source}]")
    print(f"    avant : {old}")
    print(f"    apres : {new}\n")

if skipped:
    print("--- Ignores (a verifier manuellement) ---")
    for name, reason in skipped:
        print(f"  {name} : {reason}")
