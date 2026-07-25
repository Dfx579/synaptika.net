with open('blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

blog = blog.replace('<html lang="fr">', '<html lang="fr" class="no-js">', 1)

blog = blog.replace(
    '<head>\n',
    '<head>\n<script>document.documentElement.classList.remove(\'no-js\');</script>\n',
    1
)

css_ajout = """.static-articles { display: none; }
.no-js .static-articles { display: block; }
</style>"""
blog = blog.replace("</style>", css_ajout, 1)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog)

print("✅ blog.html : correction anti-doublon appliquée")
