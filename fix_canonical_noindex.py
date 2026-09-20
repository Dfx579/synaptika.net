import pathlib

# Pages publiques : ajouter une balise canonique auto-referente
CANONICAL_PAGES = {
    "blog.html": "https://synaptika.net/blog",
    "cgv.html": "https://synaptika.net/cgv",
    "contact.html": "https://synaptika.net/contact",
    "evenements.html": "https://synaptika.net/evenements",
    "mentions-legales.html": "https://synaptika.net/mentions-legales",
    "politique-confidentialite.html": "https://synaptika.net/politique-confidentialite",
}

# Pages de travail : exclure de l'indexation
NOINDEX_PAGES = [
    "pageconstruction.html",
    "preview-images.html",
]

done_canonical = []
done_noindex = []
skipped = []

for filename, url in CANONICAL_PAGES.items():
    p = pathlib.Path(filename)
    if not p.exists():
        skipped.append((filename, "fichier introuvable"))
        continue
    content = p.read_text(encoding="utf-8")
    if 'rel="canonical"' in content:
        skipped.append((filename, "canonical deja present"))
        continue
    tag = f'<link rel="canonical" href="{url}">\n'
    idx = content.find("</head>")
    if idx == -1:
        skipped.append((filename, "balise </head> introuvable"))
        continue
    new_content = content[:idx] + "    " + tag + content[idx:]
    p.write_text(new_content, encoding="utf-8")
    done_canonical.append(filename)

for filename in NOINDEX_PAGES:
    p = pathlib.Path(filename)
    if not p.exists():
        skipped.append((filename, "fichier introuvable"))
        continue
    content = p.read_text(encoding="utf-8")
    if 'noindex' in content:
        skipped.append((filename, "noindex deja present"))
        continue
    tag = '<meta name="robots" content="noindex, nofollow">\n'
    idx = content.find("</head>")
    if idx == -1:
        skipped.append((filename, "balise </head> introuvable"))
        continue
    new_content = content[:idx] + "    " + tag + content[idx:]
    p.write_text(new_content, encoding="utf-8")
    done_noindex.append(filename)

print(f"Canonical ajoute sur {len(done_canonical)} page(s) : {done_canonical}")
print(f"Noindex ajoute sur {len(done_noindex)} page(s) : {done_noindex}")
if skipped:
    print("Ignores :")
    for name, reason in skipped:
        print(f"  {name} : {reason}")
