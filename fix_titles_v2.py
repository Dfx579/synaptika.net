#!/usr/bin/env python3
"""
Corrige les balises <title> des articles de blog en les reconstruisant
à partir de og:title (qui contient déjà la version correcte, accentuée).

Usage :
    python3 fix_titles.py            # aperçu (aucune modification)
    python3 fix_titles.py --apply    # applique les corrections
"""
import re
import sys
from pathlib import Path

BLOG_DIR = Path("blog")
APPLY = "--apply" in sys.argv

# Emojis / symboles courants en début de titre à retirer proprement
EMOJI_PATTERN = re.compile(
    r'^[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF🛑🌿🌴🪐🧠✨💧]+\s*'
)

def clean_title(raw: str) -> str:
    text = raw.strip()
    text = EMOJI_PATTERN.sub('', text)
    # retire les suffixes de marque déjà présents pour éviter les doublons
    text = re.sub(r'\s*[-—|]\s*(Blog\s+)?Synaptika\s*$', '', text, flags=re.IGNORECASE)
    return f"{text.strip()} | Synaptika"

changed = []
skipped = []

for html_file in sorted(BLOG_DIR.glob("*.html")):
    content = html_file.read_text(encoding="utf-8")

    og_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    title_match = re.search(r'<title>([^<]*)</title>', content)

    if not og_match or not title_match:
        skipped.append((html_file.name, "og:title ou <title> introuvable"))
        continue

    new_title = clean_title(og_match.group(1))
    old_title = title_match.group(1)

    if old_title.strip() == new_title.strip():
        continue

    changed.append((html_file.name, old_title, new_title))

    if APPLY:
        new_content = content.replace(
            f"<title>{old_title}</title>",
            f"<title>{new_title}</title>",
            1
        )
        html_file.write_text(new_content, encoding="utf-8")

print(f"{'APPLIQUÉ' if APPLY else 'APERÇU (aucune modification — relance avec --apply pour appliquer)'}")
print(f"{len(changed)} fichier(s) à corriger, {len(skipped)} ignoré(s)\n")

for name, old, new in changed:
    print(f"  {name}")
    print(f"    avant : {old}")
    print(f"    après : {new}\n")

if skipped:
    print("--- Ignorés (à vérifier manuellement) ---")
    for name, reason in skipped:
        print(f"  {name} : {reason}")
