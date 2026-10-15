const fs = require('fs');
const posts = require('./posts.js');

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const slugOf = f => f.replace(/^\.?\/?blog\//, '');

const items = posts
  .map(p => ({ ...p, slug: slugOf(p.file || '') }))
  .filter(p => p.slug && fs.existsSync(`blog/${p.slug}.html`));

// Choix des articles proches, en répartissant les liens reçus
const assigned = {};
items.forEach(p => { assigned[p.slug] = 0; });
const related = {};
for (const p of items) {
  const pt = p.tags || [];
  const ranked = items
    .filter(q => q.slug !== p.slug)
    .map(q => {
      const shared = (q.tags || []).filter(t => pt.includes(t)).length;
      const sameCat = q.category && q.category === p.category ? 1 : 0;
      return { q, score: 3 * shared + 2 * sameCat - assigned[q.slug] };
    })
    .sort((a, b) => b.score - a.score || String(b.q.date).localeCompare(String(a.q.date)));
  related[p.slug] = ranked.slice(0, 4).map(x => x.q);
  related[p.slug].forEach(q => { assigned[q.slug]++; });
}

const re = /<!-- related-start -->[\s\S]*?<!-- related-end -->\n?/;
let changed = 0;
const skipped = [];
for (const p of items) {
  const file = `blog/${p.slug}.html`;
  const list = related[p.slug]
    .map(q => `    <li><a href="/blog/${q.slug}">${esc(q.title)}</a></li>`).join('\n');
  const block =
`<!-- related-start -->
<section class="related-posts" style="max-width:800px;margin:40px auto;padding:0 20px;">
  <h2 style="font-size:1.3rem;">À lire aussi</h2>
  <ul>
${list}
  </ul>
  <p><a href="/ressourcesgratuites">Ressources gratuites pour gérer le stress</a></p>
</section>
<!-- related-end -->
`;
  const html = fs.readFileSync(file, 'utf8');
  let out;
  if (re.test(html)) out = html.replace(re, () => block);
  else {
    const f = html.indexOf('<footer');
    if (f === -1) { skipped.push(p.slug); continue; }
    const ls = html.lastIndexOf('\n', f) + 1;
    const i = html.slice(ls, f).trim() === '' ? ls : f;
    out = html.slice(0, i) + block + html.slice(i);
  }
  if (out !== html) { fs.writeFileSync(file, out, 'utf8'); changed++; }
}
const counts = Object.values(assigned);
console.log(`✅ ${changed} articles modifiés | liens reçus par article : min ${Math.min(...counts)}, max ${Math.max(...counts)} | ignorés : ${skipped.length ? skipped.join(', ') : 'aucun'}`);
