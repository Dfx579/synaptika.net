#!/usr/bin/env python3
import sys
from pathlib import Path

APPLY = "--apply" in sys.argv

GA_ID = "G-QNN9NJ7QMG"

SNIPPET = f"""    <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GA_ID}');
</script>
"""

EXCLUDE = {"googlef754b1749eeaa8b6.html"}

targets = [p for p in Path(".").glob("*.html") if p.name not in EXCLUDE]
targets += list(Path("blog").glob("*.html"))

changed, skipped = [], []

for html_file in sorted(targets):
    content = html_file.read_text(encoding="utf-8")

    if GA_ID in content:
        skipped.append((html_file.as_posix(), "deja present"))
        continue

    idx = content.find("<head>")
    if idx == -1:
        skipped.append((html_file.as_posix(), "balise <head> introuvable"))
        continue

    insert_at = idx + len("<head>")
    new_content = content[:insert_at] + "\n" + SNIPPET + content[insert_at:]

    changed.append(html_file.as_posix())

    if APPLY:
        html_file.write_text(new_content, encoding="utf-8")

print(f"{'APPLIQUE' if APPLY else 'APERCU (aucune modification -- relance avec --apply)'}")
print(f"{len(changed)} fichier(s) a modifier, {len(skipped)} deja bons/ignores\n")

for name in changed:
    print(f"  + {name}")

if skipped:
    print("\n--- Deja bons / ignores ---")
    for name, reason in skipped:
        print(f"  {name} : {reason}")
