import re, glob

# ---------- 1. Ajouter les canoniques manquantes ----------
files = glob.glob('blog/*.html')
ajoutes = 0
for f in files:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    if 'rel="canonical"' not in c:
        nom_fichier = f.split('/')[-1]
        canonical_url = f'https://synaptika.net/blog/{nom_fichier}'
        c = re.sub(
            r'(</title>)',
            r'\1\n<link rel="canonical" href="' + canonical_url + '">',
            c, count=1
        )
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        ajoutes += 1
print(f"✅ Canonique ajoutée sur {ajoutes} articles")

# ---------- 2. Corriger les 2 canoniques cassées/incohérentes ----------
with open('blog/5-elements-tao-cuisine-creole-emotions-martinique.html', encoding='utf-8') as f:
    c = f.read()
c = c.replace(
    'https://synaptika.net/blog/5-elements-tao-cuisine-creole-émotions-martinique',
    'https://synaptika.net/blog/5-elements-tao-cuisine-creole-emotions-martinique.html'
)
with open('blog/5-elements-tao-cuisine-creole-emotions-martinique.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('blog/comment-optimiser-pratique-eft.html', encoding='utf-8') as f:
    c = f.read()
c = c.replace(
    'https://synaptika.net/blog/comment-optimiser-pratique-eft"',
    'https://synaptika.net/blog/comment-optimiser-pratique-eft.html"'
)
with open('blog/comment-optimiser-pratique-eft.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("✅ 2 canoniques incohérentes corrigées")

# ---------- 3. Corriger la meta description dupliquée ----------
with open('blog/sensations-apres-seance.html', encoding='utf-8') as f:
    c = f.read()
c = c.replace(
    'content="Detente, legere fatigue, émotions qui remontent... Decouvrez ce que vous pouvez ressentir apres une seance de NST Bowen et pourquoi c\'est normal."',
    'content="Que ressent-on juste après une séance de NST Bowen ? Détente, légère fatigue ou émotions qui remontent : voici ce qui est normal et pourquoi."'
)
with open('blog/sensations-apres-seance.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("✅ Meta description dupliquée corrigée")
