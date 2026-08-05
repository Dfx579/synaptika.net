#!/usr/bin/env python3
============================================
fix_seo_complet.py — Synaptika.net
Corrections SEO complètes en une commande
============================================

import os
import re

BASE_URL = "https://synaptika.net"
BASE_DIR = os.path.expanduser("~/synaptika.net")

============================================
PAGES À METTRE EN NOINDEX (parasites)
============================================
NOINDEX_PAGES = [
    "post1.html",
    "post2.html",
    "post3.html",
    "pageconstruction.html",
    "preview-images.html",
    "googlef754b1749eeaa8b6.html",
]

============================================
CORRESPONDANCE fichier → URL canonique
============================================
def get_canonical_url(filepath):
    rel = os.path.relpath(filepath, BASE_DIR)
    Supprimer l'extension .html
    url = rel.replace(".html", "")
    index → racine
    if url == "index":
        return BASE_URL + "/"
    blog/index → /blog
    if url == "blog/index":
        return BASE_URL + "/blog"
    return BASE_URL + "/" + url

============================================
FONCTION : Corriger une page HTML
============================================
def fix_html_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    filename = os.path.basename(filepath)
    rel_path = os.path.relpath(filepath, BASE_DIR)

    --- 1. Corriger le double DOCTYPE (bug détecté dans index.html) ---
    Supprimer les DOCTYPE/html/head dupliqués
    content = re.sub(r'(<!DOCTYPE html>[\s\S]?</head>\s<body[\s\S]?)\s<!DOCTYPE html>', 
                     r'\1', content, flags=re.IGNORECASE)

    --- 2. Ajouter charset UTF-8 si absent ---
    if 'charset' not in content.lower():
        content = content.replace(
            '<head>',
            '<head>\n  <meta charset="UTF-8">',
            1
        )

    --- 3. Ajouter viewport si absent ---
    if 'viewport' not in content.lower():
        content = content.replace(
            '<head>',
            '<head>\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
            1
        )

    --- 4. Gérer noindex ou canonical ---
    canonical_url = get_canonical_url(filepath)
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    noindex_tag = '<meta name="robots" content="noindex, nofollow">'

    if filename in NOINDEX_PAGES:
        Supprimer canonical existant si présent
        content = re.sub(r'<link rel="canonical"[^>]+>', '', content)
        Ajouter noindex si absent
        if 'noindex' not in content:
            content = content.replace('</head>', f'  {noindex_tag}\n</head>', 1)
        print(f"  🚫 NOINDEX ajouté   : {rel_path}")

    else:
        Supprimer canonical existant (pour éviter les doublons)
        content = re.sub(r'\s*<link rel="canonical"[^>]+>', '', content)
        Ajouter le bon canonical avant </head>
        content = content.replace('</head>', f'  {canonical_tag}\n</head>', 1)
        print(f"  ✅ Canonical ajouté : {rel_path} → {canonical_url}")

    --- 5. Corriger les fautes récurrentes ---
    corrections = {
        "potentiel innée": "potentiel inné",
        "confidencialité": "confidentialité",
        " diagnostique": " diagnostic",
        "faîte pour vous": "faite pour vous",
        "faîte pour": "faite pour",
    }
    for wrong, correct in corrections.items():
        if wrong in content:
            content = content.replace(wrong, correct)
            print(f"  ✏️  Faute corrigée   : '{wrong}' → '{correct}'")

    --- Sauvegarder si modifié ---
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

============================================
FONCTION : Créer llms.txt
============================================
def create_llms_txt():
    llms_path = os.path.join(BASE_DIR, "llms.txt")
    content = """Synaptika
> Solutions anti-stress et coaching bien-être par Thierry FELICIA,
> praticien en développement personnel.
> Libérez-vous du stress en 10 minutes par jour, même si vous êtes
> dépassé et fatigué.

À propos
Synaptika propose des méthodes holistiques personnalisées combinant
kinésiologie, Touch for Health, NST Bowen et sagesse taoïste pour
aider les clients à développer leurs propres ressources face au stress.

Praticien
- Nom : Thierry FELICIA
- Spécialité : Développement personnel, gestion du stress, kinésiologie
- Formations : Touch for Health, NST Bowen, Kinésiologie avancée,
  Naturopathie, Tai-Chi, Qi Gong, Ba Gua Zhang
- YouTube : https://www.youtube.com/@Synaptika

Pages principales
- Accueil : https://synaptika.net/
- Blog : https://synaptika.net/blog
- À propos : https://synaptika.net/apropos
- ZenBox : https://synaptika.net/zenbox
- Ressources gratuites : https://synaptika.net/ressourcesgratuites
- Contact : https://synaptika.net/contact
- Événements : https://synaptika.net/evenements

Services
- NST Bowen : https://synaptika.net/blog/Bowen
- Touch for Health : https://synaptika.net/blog/TFH
- Drainage lymphatique : https://synaptika.net/blog/nst-bowen-creole
- Séances personnalisées : https://synaptika.net/contact

Blog — Articles principaux
- Gestion du stress : https://synaptika.net/blog/stress-chronique-signaux
- Touch for Health : https://synaptika.net/blog/TFH
- NST Bowen : https://synaptika.net/blog/Bowen
- Eau et hydratation : https://synaptika.net/blog/eau
- Alimentation et sport : https://synaptika.net/blog/alimentation-sport
- Qi Gong et Tai Chi : https://synaptika.net/blog/qi-gong-tai-chi
- Graines germées : https://synaptika.net/blog/grainesgermees
- Super-aliments créoles : https://synaptika.net/blog/superaliments
- Méditation avec les arbres : https://synaptika.net/blog/arbres
- Rythmes circadiens : https://synaptika.net/blog/rythmes-circadiens-hiboux
- Burnout ou fatigue : https://synaptika.net/blog/burnout-ou-fatigue
- Lâcher prise : https://synaptika.net/blog/lacher-prise
- Résilience : https://synaptika.net/blog/resilience
"""
    with open(llms_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n  ✅ llms.txt créé : {llms_path}")

============================================
FONCTION : Vérifier netlify.toml
============================================
def check_netlify_toml():
    toml_path = os.path.join(BASE_DIR, "netlify.toml")
    with open(toml_path, "r", encoding="utf-8") as f:
        content = f.read()

    additions = []

    Vérifier redirection www → non-www
    if "www.synaptika.net" not in content:
        additions.append("""
[[redirects]]
  from = "https://www.synaptika.net/*"
  to = "https://synaptika.net/:splat"
  status = 301
  force = true
""")

    Vérifier minification
    if "minify" not in content:
        additions.append("""
[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true

[build.processing.images]
  compress = true
""")

    if additions:
        with open(toml_path, "a", encoding="utf-8") as f:
            for addition in additions:
                f.write(addition)
        print(f"\n  ✅ netlify.toml mis à jour ({len(additions)} ajout(s))")
    else:
        print(f"\n  ✅ netlify.toml — déjà à jour")

============================================
PROGRAMME PRINCIPAL
============================================
def main():
    print("=" * 55)
    print("🔧 CORRECTIONS SEO SYNAPTIKA.NET")
    print("=" * 55)

    modified = 0
    skipped = 0

    Collecter tous les fichiers HTML
    html_files = []

    Pages racine
    for f in os.listdir(BASE_DIR):
        if f.endswith(".html"):
            html_files.append(os.path.join(BASE_DIR, f))

    Articles blog
    blog_dir = os.path.join(BASE_DIR, "blog")
    if os.path.exists(blog_dir):
        for f in os.listdir(blog_dir):
            if f.endswith(".html"):
                html_files.append(os.path.join(blog_dir, f))

    html_files.sort()

    print(f"\n📄 {len(html_files)} fichiers HTML trouvés\n")
    print("-" * 55)

    for filepath in html_files:
        result = fix_html_file(filepath)
        if result:
            modified += 1
        else:
            skipped += 1

    Créer llms.txt
    print("\n" + "-" * 55)
    print("📝 CRÉATION DES FICHIERS MANQUANTS")
    print("-" * 55)
    create_llms_txt()

    Vérifier netlify.toml
    print("\n" + "-" * 55)
    print("⚙️  VÉRIFICATION NETLIFY.TOML")
    print("-" * 55)
    check_netlify_toml()

    Résumé final
    print("\n" + "=" * 55)
    print("📊 RÉSUMÉ")
    print("=" * 55)
    print(f"  ✅ Fichiers modifiés  : {modified}")
    print(f"  ⏭️  Fichiers inchangés : {skipped}")
    print(f"  📄 Total traité       : {len(html_files)}")
    print("\n🚀 PROCHAINE ÉTAPE :")
    print("   git add .")
    print('   git commit -m "fix(seo): canoniques, noindex, llms.txt, netlify"')
    print("   git push origin main")
    print("=" * 55)

if __name__ == "__main__":
    main()
