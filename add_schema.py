import os
base = os.path.expanduser('~/synaptika.net')

schemas = {
    'index.html': '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"Synaptika","url":"https://synaptika.net","description":"Solutions anti-stress et bien-etre par Thierry FELICIA en Martinique.","inLanguage":"fr","publisher":{"@type":"Person","name":"Thierry FELICIA","url":"https://synaptika.net/apropos"}}</script>',
    'blog.html': '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Blog","name":"Blog Synaptika","url":"https://synaptika.net/blog","description":"Articles sur la gestion du stress, le bien-etre et le developpement personnel.","inLanguage":"fr","author":{"@type":"Person","name":"Thierry FELICIA","url":"https://synaptika.net/apropos"}}</script>',
    'contact.html': '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ContactPage","name":"Contact Synaptika","url":"https://synaptika.net/contact","description":"Contactez Thierry FELICIA pour une seance NST Bowen ou Touch for Health en Martinique."}</script>',
    'zenbox.html': '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"ZenBox Synaptika","url":"https://synaptika.net/zenbox","description":"Programme ZenBox pour transformer votre relation au stress.","brand":{"@type":"Brand","name":"Synaptika"}}</script>',
    'ressourcesgratuites.html': '<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Ressources gratuites Synaptika","url":"https://synaptika.net/ressourcesgratuites","description":"Guides gratuits pour explorer le bien-etre personnel.","author":{"@type":"Person","name":"Thierry FELICIA","url":"https://synaptika.net/apropos"}}</script>',
}

for filename, schema in schemas.items():
    path = os.path.join(base, filename)
    c = open(path, encoding='utf-8').read()
    if 'application/ld+json' not in c:
        c = c.replace('</head>', schema + '\n</head>', 1)
        open(path, 'w', encoding='utf-8').write(c)
        print('OK: ' + filename)
    else:
        print('SKIP: ' + filename)