const fs = require('fs');
const path = require('path');
const posts = require('./posts.js');

const SITE_URL = 'https://synaptika.net';
const DEFAULT_AUTHOR = 'Thierry Felicia';

function absoluteUrl(relativePath) {
  return SITE_URL + '/' + relativePath.replace(/^\.\//, '');
}

function resolveFile(file) {
  return file.endsWith('.html') ? file : file + '.html';
}

let updated = 0;
let skipped = 0;

posts.forEach(post => {
  const relFile = resolveFile(post.file);
  const filePath = path.join(__dirname, relFile.replace(/^\.\//, ''));

  if (!fs.existsSync(filePath)) {
    console.warn(`Fichier introuvable, ignore : ${relFile}`);
    skipped++;
    return;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  const schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": post.title,
    "description": post.excerpt,
    "author": {
      "@type": "Person",
      "name": post.author && post.author.trim() ? post.author : DEFAULT_AUTHOR,
      "url": `${SITE_URL}/apropos.html`
    },
    "publisher": {
      "@type": "Organization",
      "name": "Synaptika",
      "url": SITE_URL
    },
    "datePublished": post.date,
    "dateModified": post.date,
    "image": post.image ? absoluteUrl(post.image) : undefined,
    "keywords": (post.tags || []).join(', '),
    "articleSection": post.category || undefined,
    "inLanguage": "fr-MQ"
  };

  const jsonLd = `<!-- ARTICLE_SCHEMA_START -->
<script type="application/ld+json">
${JSON.stringify(schema, null, 2)}
</script>
<!-- ARTICLE_SCHEMA_END -->`;

  const markerRegex = /<!-- ARTICLE_SCHEMA_START -->[\s\S]*?<!-- ARTICLE_SCHEMA_END -->/;

  if (markerRegex.test(html)) {
    html = html.replace(markerRegex, jsonLd);
  } else if (html.includes('</head>')) {
    html = html.replace('</head>', `${jsonLd}\n</head>`);
  } else {
    console.warn(`Pas de head trouve dans ${relFile}, ignore.`);
    skipped++;
    return;
  }

  fs.writeFileSync(filePath, html, 'utf8');
  updated++;
});

console.log(`${updated} article(s) mis a jour avec le balisage Schema.org.`);
if (skipped > 0) console.log(`${skipped} fichier(s) ignore(s), voir avertissements ci-dessus.`);
