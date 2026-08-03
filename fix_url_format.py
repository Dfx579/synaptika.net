import re, glob

# ---------- 1. Régénérer le sitemap avec le bon format (minuscule, sans extension) ----------
with open('posts.js', encoding='utf-8') as f:
    posts_js = f.read()
fichiers = re.findall(r'file:\s*"([^"]+)"', posts_js)

from datetime import date
today = date.today().isoformat()

urls = [
    ("https://synaptika.net/", "1.0"),
    ("https://synaptika.net/blog", "0.9"),
    ("https://synaptika.net/zenbox", "0.8"),
    ("https://synaptika.net/apropos", "0.7"),
]
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, priority in urls:
    xml.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>')
for fichier in fichiers:
    slug = fichier.replace('./blog/', '').lower()
    url = f'https://synaptika.net/blog/{slug}'
    xml.append(f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>')
xml.append('</urlset>')
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))
print(f"✅ sitemap.xml régénéré au bon format ({len(urls) + len(fichiers)} URLs)")

# ---------- 2. Corriger TOUTES les canoniques des articles (bon format) ----------
corrigees = 0
for f in glob.glob('blog/*.html'):
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    slug = f.split('/')[-1].replace('.html', '').lower()
    bonne_url = f'https://synaptika.net/blog/{slug}'
    nouvelle_balise = f'<link rel="canonical" href="{bonne_url}">'
    if 'rel="canonical"' in c:
        c2 = re.sub(r'<link rel="canonical" href="[^"]*">', nouvelle_balise, c, count=1)
    else:
        c2 = re.sub(r'(</title>)', r'\1\n' + nouvelle_balise, c, count=1)
    if c2 != c:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c2)
        corrigees += 1
print(f"✅ {corrigees} canoniques corrigées au bon format")
