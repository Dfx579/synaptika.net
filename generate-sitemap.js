const fs = require('fs');
const path = require('path');

const SITE = 'https://synaptika.net';
const today = new Date().toISOString().slice(0, 10);

function listHtml(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => {
    if (e.name.startsWith('.') || e.name === 'node_modules') return [];
    const p = path.join(dir, e.name);
    if (e.isDirectory()) return listHtml(p);
    return e.name.endsWith('.html') ? [p] : [];
  });
}

const urls = listHtml('.')
  .map(p => p.replace(/^\.\//, '').replace(/\.html$/, ''))
  .filter(p => p !== '404')
  .map(p => (p === 'index' ? '' : p))
  .sort((a, b) => (a === '' ? -1 : b === '' ? 1 : a.localeCompare(b)));

const xml =
  '<?xml version="1.0" encoding="UTF-8"?>\n' +
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  urls.map(p => `  <url>\n    <loc>${SITE}/${p}</loc>\n    <lastmod>${today}</lastmod>\n  </url>`).join('\n') +
  '\n</urlset>\n';

fs.writeFileSync('sitemap.xml', xml);
console.log(`✅ sitemap.xml : ${urls.length} URL générées`);
