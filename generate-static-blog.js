const fs = require('fs');
const path = require('path');

const posts = require('./posts.js');

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

const articlesHtml = posts.map(post => {
  const slug = post.file.replace('./blog/', '').replace(/\.html$/, '');
  return `  <article>
    <h2><a href="./blog/${slug}.html">${escapeHtml(post.title)}</a></h2>
    <p>${escapeHtml(post.excerpt)}</p>
  </article>`;
}).join('\n');

const newBlock = `<!-- STATIC_ARTICLES_START -->
<div class="static-articles">
${articlesHtml}
</div>
<!-- STATIC_ARTICLES_END -->`;

const blogPath = path.join(__dirname, 'blog.html');
let html = fs.readFileSync(blogPath, 'utf8');

const markerRegex = /<!-- STATIC_ARTICLES_START -->[\s\S]*?<!-- STATIC_ARTICLES_END -->/;

if (!markerRegex.test(html)) {
  console.error("❌ Marqueurs introuvables dans blog.html. Rien n'a été modifié.");
  process.exit(1);
}

html = html.replace(markerRegex, newBlock);
fs.writeFileSync(blogPath, html, 'utf8');

console.log(`✅ blog.html mis à jour avec ${posts.length} articles depuis posts.js.`);
