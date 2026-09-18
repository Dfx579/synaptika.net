import pathlib

f = pathlib.Path("index.html")
content = f.read_text(encoding="utf-8")

schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "HealthAndBeautyBusiness",
      "name": "Synaptika - Thierry Felicia",
      "description": "Accompagnement de bien-être non médical en Martinique. Séances individuelles de NST Bowen pour retrouver confort et détente, à Fort-de-France.",
      "url": "https://synaptika.net",
      "founder": {
        "@type": "Person",
        "name": "Thierry Felicia"
      },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Fort-de-France",
        "addressRegion": "Martinique",
        "addressCountry": "FR"
      },
      "areaServed": {
        "@type": "City",
        "name": "Fort-de-France"
      },
      "priceRange": "90€",
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "customer support",
        "url": "https://tally.so/r/lb1GPX"
      },
      "makesOffer": {
        "@type": "Offer",
        "name": "Séance individuelle NST Bowen",
        "price": "90",
        "priceCurrency": "EUR",
        "description": "Séance de 45 minutes sur rendez-vous."
      },
      "sameAs": [
        "https://bsky.app/profile/synaptika.bsky.social",
        "https://fr.pinterest.com/synaptikanet",
        "https://www.youtube.com/@synaptika"
      ]
    }
    </script>
'''

idx = content.find("</head>")
if idx == -1:
    print("ERREUR : balise </head> introuvable")
    raise SystemExit(1)

new_content = content[:idx] + schema + content[idx:]
f.write_text(new_content, encoding="utf-8")
print("Donnees structurees ajoutees a index.html (avec sameAs)")
