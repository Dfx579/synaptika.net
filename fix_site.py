# Script de correction SEO Synaptika

# ---------- blog.html ----------
with open('blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

blog = blog.replace('<noscript>\n<!-- STATIC_ARTICLES_START -->', '<!-- STATIC_ARTICLES_START -->')
blog = blog.replace('<!-- STATIC_ARTICLES_END -->\n</noscript>', '<!-- STATIC_ARTICLES_END -->')
blog = blog.replace('<div class="static-articles">', '<div class="static-articles" id="staticArticles">')

blog = blog.replace(
    "  posts.forEach((post, index) => {",
    "  const staticBlock = document.getElementById('staticArticles');\n"
    "  if (staticBlock) staticBlock.style.display = 'none';\n\n"
    "  posts.forEach((post, index) => {"
)

css_ajout = """.static-articles {
  max-width: 1000px; margin: 0 auto; padding: 0 20px;
}
.static-articles article {
  background: var(--card); margin-bottom: 20px; padding: 24px;
  border-radius: 16px; box-shadow: 0 10px 30px var(--shadow);
}
.static-articles h2 { margin-bottom: 8px; font-size: 20px; }
.static-articles a { color: var(--primary); text-decoration: none; }
</style>"""
blog = blog.replace("</style>", css_ajout, 1)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog)

print("✅ blog.html corrigé")

# ---------- index.html ----------
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

ancien_bloc = '''        <div class="blog-grid" id="blog-posts-container">
            <!-- 記事はJavaScriptで動的に読み込まれます -->
        </div>'''

nouveau_bloc = '''        <div class="blog-grid" id="blog-posts-container">
            <div class="bg-white rounded-2xl shadow-md overflow-hidden">
                <img src="./blog/images/nst-bowen-creole.jpg" alt="NST Bowen" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">NST Bowen : on apròch dous pou édé kò-w rétwouvé kalm ak byennèt li</h3>
                    <a href="./blog/nst-bowen-creole.html" class="text-purple-600 font-medium hover:text-purple-800">Lire l'article →</a>
                </div>
            </div>
            <div class="bg-white rounded-2xl shadow-md overflow-hidden">
                <img src="./blog/images/5-elements-assiette.jpg" alt="5 éléments du Tao en cuisine créole" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">5 éléments du Tao en cuisine créole</h3>
                    <a href="./blog/5-elements-tao-cuisine-creole-emotions-martinique.html" class="text-purple-600 font-medium hover:text-purple-800">Lire l'article →</a>
                </div>
            </div>
            <div class="bg-white rounded-2xl shadow-md overflow-hidden">
                <img src="./blog/images/image-optimisee-eft-meridiens.jpg" alt="Comment optimiser votre pratique de l'EFT" class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">Comment optimiser votre pratique de l'EFT ?</h3>
                    <a href="./blog/comment-optimiser-pratique-eft.html" class="text-purple-600 font-medium hover:text-purple-800">Lire l'article →</a>
                </div>
            </div>
        </div>'''

idx = idx.replace(ancien_bloc, nouveau_bloc)

idx = idx.replace(
    "    if (container && typeof posts !== 'undefined') {\n        const latestPosts = posts.slice(0, 3);",
    "    if (container && typeof posts !== 'undefined') {\n        container.innerHTML = '';\n        const latestPosts = posts.slice(0, 3);"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("✅ index.html corrigé")
