import re, glob

# ---------- 1. Corriger la CSS manquante .recette ----------
fichier_recette = "blog/5-elements-tao-cuisine-creole-emotions-martinique.html"
with open(fichier_recette, encoding='utf-8') as f:
    contenu = f.read()

css_recette = """.recette {
    background: #fff; border-radius: 16px; padding: 24px;
    margin: 30px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    border-left: 5px solid #7f21f3;
}
.recette h3 { margin-bottom: 15px; color: #7f21f3; }
.recette h4 { margin-top: 15px; margin-bottom: 8px; }
</style>"""
contenu = contenu.replace("</style>", css_recette, 1)

with open(fichier_recette, 'w', encoding='utf-8') as f:
    f.write(contenu)

print(f"✅ CSS .recette ajoutée dans {fichier_recette}")

# ---------- 2. Corriger les accents manquants sur tout le blog ----------
corrections = {
    "epuise": "épuisé", "epuisement": "épuisement", "genetique": "génétique",
    "decouvrez": "découvrez", "decalage": "décalage", "reguliere": "régulière",
    "derniere": "dernière", "periode": "période", "secreter": "sécréter",
    "glande": "glande", "necessite": "nécessite", "severite": "sévérité",
    "systeme": "système", "energie": "énergie", "equilibre": "équilibre",
    "emotion": "émotion", "emotions": "émotions", "synchronise": "synchronise",
    "probleme": "problème", "problemes": "problèmes", "preparee": "préparée",
}

total = 0
for path in glob.glob("blog/*.html"):
    with open(path, encoding='utf-8') as f:
        texte = f.read()
    original = texte
    for mauvais, bon in corrections.items():
        texte = re.sub(r'\b' + mauvais + r'\b', bon, texte)
    if texte != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(texte)
        n = sum(len(re.findall(r'\b' + m + r'\b', original)) for m in corrections)
        total += 1
        print(f"✏️  Corrigé : {path}")

print(f"\n✅ {total} article(s) corrigé(s) au total")
