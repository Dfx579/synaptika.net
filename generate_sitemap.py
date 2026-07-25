import re
from datetime import date

with open('posts.js', encoding='utf-8') as f:
    posts_js = f.read()

# Extrait tous les chemins d'articles depuis posts.js
fichiers = re.findall(r'file:\s*"([^"]+)"', posts_js)
today = date.today().isoformat()

urls = [
    ("https://synaptika.net/", "1.0"),
    ("https://synaptika.net/blog", "0.9"),
    ("https://synaptika.net/zenbox.html", "0.8"),
    ("https://synaptika.net/apropos.html", "0.7"),
]

xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for loc, priority in urls:
    xml.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

for fichier in fichiers:
    url = fichier.replace('./', 'https://synaptika.net/') + '.html'
    xml.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")

xml.append('</urlset>')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))

print(f"✅ sitemap.xml régénéré avec {len(urls) + len(fichiers)} URLs ({len(fichiers)} articles)")
