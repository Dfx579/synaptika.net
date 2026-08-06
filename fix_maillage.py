import os

base = os.path.expanduser('~/synaptika.net')

corrections = [
    ("href='apropos.html'", "href='/apropos'"),
    ("href='blog.html'", "href='/blog'"),
    ("href='zenbox.html'", "href='/zenbox'"),
    ("href='contact.html'", "href='/contact'"),
    ("href='ressourcesgratuites.html'", "href='/ressourcesgratuites'"),
    ("href='evenements.html'", "href='/evenements'"),
    ('href="apropos.html"', 'href="/apropos"'),
    ('href="blog.html"', 'href="/blog"'),
    ('href="zenbox.html"', 'href="/zenbox"'),
    ('href="contact.html"', 'href="/contact"'),
    ('href="ressourcesgratuites.html"', 'href="/ressourcesgratuites"'),
    ('href="evenements.html"', 'href="/evenements"'),
    ('href="./blog.html"', 'href="/blog"'),
    ('href="index.html"', 'href="/"'),
]

files = []
for f in os.listdir(base):
    if f.endswith('.html'):
        files.append(os.path.join(base, f))
for f in os.listdir(os.path.join(base, 'blog')):
    if f.endswith('.html'):
        files.append(os.path.join(base, 'blog', f))

total = 0
for path in files:
    c = open(path, encoding='utf-8').read()
    original = c
    for wrong, correct in corrections:
        c = c.replace(wrong, correct)
    if c != original:
        open(path, 'w', encoding='utf-8').write(c)
        print('OK: ' + os.path.relpath(path, base))
        total += 1

print('Total modifies: ' + str(total))