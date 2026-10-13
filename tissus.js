/* Carrousel « Les tissus du corps » — s'initialise dans #tissus-carousel */
(function () {
  var root = document.getElementById('tissus-carousel');
  if (!root) return;
  var IMG_DIR = '/images/tissus/', EXT = 'webp';

  var slides = [
    { file:'muscles',   nav:'Muscles',   c:'var(--muscle)',   title:'Les muscles',      draw:['bones','muscles'],
      alt:"Fibres musculaires stylisées, translucides, dans des tons corail", t:"Ils produisent le mouvement. Sous l'effet du stress ou de la fatigue, ils peuvent rester légèrement contractés sans que l'on s'en rende compte." },
    { file:'os',        nav:'Os',        c:'var(--bone)',     title:'Les os',           draw:['boneshi'],
      alt:"Articulation du genou stylisée, os nacrés et lumineux", t:"La charpente du corps. Ils donnent sa forme et servent de points d'appui aux muscles, aux tendons et aux ligaments." },
    { file:'tendons',   nav:'Tendons',   c:'var(--tendon)',   title:'Les tendons',      draw:['bones','tendons'],
      alt:"Tendons nacrés reliant des fibres musculaires à l'os, illustration stylisée", t:"Ils relient les muscles aux os et transmettent la force du mouvement. Leur souplesse participe à l'aisance du geste." },
    { file:'ligaments', nav:'Ligaments', c:'var(--ligament)', title:'Les ligaments',    draw:['bones','ligaments'],
      alt:"Ligaments dorés stabilisant une articulation du genou, illustration stylisée", t:"Ils relient les os entre eux et stabilisent les articulations, comme ici au niveau du genou." },
    { file:'fascias',   nav:'Fascias',   c:'var(--fascia)',   title:'Les fascias',      draw:['bones','fascias'],
      alt:"Réseau lumineux de fascia enveloppant des fibres musculaires", t:"Un fin tissu continu qui enveloppe et relie les muscles, les tendons et les articulations. On le décrit souvent comme une toile qui traverse tout le corps." },
    { file:'meridiens', nav:'Méridiens', c:'var(--meridian)', title:'Les méridiens',    draw:['bones','meridiens'],
      alt:"Trajets lumineux violets évoquant les méridiens de la tradition chinoise sur une silhouette de jambe", t:"Dans la tradition chinoise, ce sont des trajets le long desquels circule l'énergie. Ce n'est pas une structure anatomique mesurée : c'est un repère issu de la tradition." },
    { file:'ensemble',  pos:'100% 50%', nav:'Ensemble', c:'#ffffff', title:'Un seul ensemble', draw:['bones','fascias','muscles','tendons','ligaments','meridiens'],
      alt:"Deux jambes stylisées en marche, muscles, fascias et trajets lumineux réunis", t:"Muscles, tendons, ligaments et fascias forment un réseau continu : ce qui se passe à un endroit se ressent souvent ailleurs. Les gestes doux de la NST Bowen se pratiquent sur ces zones du corps, dans une démarche de détente et de confort." }
  ];

  // ---- dessins de secours (affichés si l'image ne charge pas) ----
  var fib = ''; for (var i = 0; i <= 11; i++) { var t = i / 11 * 2 - 1;
    fib += '<path class="ts-fib" d="M' + (150+t*52) + ' 42 Q' + (150+t*62) + ' 105 ' + (150+t*12) + ' 172"/><path class="ts-fib" d="M' + (150+t*46) + ' 250 Q' + (150+t*52) + ' 320 ' + (150+t*8) + ' 405"/>'; }
  var OUT = 'M90 36 C70 100 82 155 118 185 L112 230 C92 270 92 340 124 415 L176 415 C208 340 208 270 188 230 L182 185 C218 155 230 100 210 36 C180 22 120 22 90 36 Z';
  var L = {
    bones: function (hi) { var c = hi ? 'ts-bones hi' : 'ts-bones'; return '<path class="' + c + '" d="M128 10 L172 10 C176 90 178 150 188 185 C190 198 170 205 150 203 C130 205 110 198 112 185 C122 150 124 90 128 10 Z"/><path class="' + c + '" d="M118 225 C135 232 165 232 182 225 L172 440 L128 440 Z"/><ellipse class="' + c + '" cx="150" cy="190" rx="20" ry="20"/>'; },
    muscles: '<path d="M96 40 C80 100 90 150 128 178 L172 178 C210 150 220 100 204 40 C180 28 120 28 96 40 Z" fill="rgba(232,141,132,.4)" stroke="#e88d84" stroke-width="1.2"/><path d="M100 245 C88 300 100 360 128 410 L172 410 C200 360 212 300 200 245 Z" fill="rgba(232,141,132,.4)" stroke="#e88d84" stroke-width="1.2"/>' + fib,
    tendons: '<g fill="#f4efe6" fill-opacity=".92" stroke="#fff" stroke-opacity=".5" stroke-width=".8" filter="url(#ts-glow)"><path d="M128 150 L172 150 L162 172 L138 172 Z"/><path d="M140 208 L160 208 L156 242 L144 242 Z"/><path d="M138 395 L162 395 L158 440 L142 440 Z"/></g>',
    ligaments: '<g fill="none" stroke="#f2c46d" stroke-width="5" stroke-linecap="round" filter="url(#ts-glow)"><path d="M108 188 L112 238"/><path d="M192 188 L188 238"/><path d="M140 214 L162 232" stroke-width="4"/><path d="M160 214 L138 232" stroke-width="4"/></g>',
    fascias: '<g class="ts-shimmer"><rect width="300" height="460" fill="url(#ts-mesh)" clip-path="url(#ts-leg)"/><path d="' + OUT + '" fill="none" stroke="#4fd1c5" stroke-width="1.6" filter="url(#ts-glow)"/></g>',
    meridiens: '<g fill="none" stroke="#b9a4ff" stroke-width="1.8" stroke-linecap="round"><path class="ts-flow" d="M205 30 C225 100 215 170 192 200 C196 260 205 330 175 430"/><path class="ts-flow" d="M95 30 C75 100 85 170 108 200 C104 260 95 330 125 430"/><g fill="#b9a4ff" stroke="none" filter="url(#ts-glow)"><circle cx="219" cy="110" r="3"/><circle cx="196" cy="208" r="3"/><circle cx="199" cy="320" r="3"/><circle cx="81" cy="110" r="3"/><circle cx="104" cy="208" r="3"/><circle cx="101" cy="320" r="3"/></g></g>'
  };
  function piece(d) { return d === 'boneshi' ? L.bones(true) : d === 'bones' ? L.bones(false) : L[d]; }

  // ---- structure ----
  root.innerHTML =
    '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' +
    '<clipPath id="ts-leg"><path d="' + OUT + '"/></clipPath>' +
    '<pattern id="ts-mesh" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(32)"><path d="M0 0H16M0 0V16" class="ts-web" fill="none"/></pattern>' +
    '<filter id="ts-glow"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs></svg>' +
    '<div class="ts-viewport"><div class="ts-track"></div></div>' +
    '<button type="button" class="ts-arrow ts-prev" aria-label="Diapositive précédente">←</button>' +
    '<button type="button" class="ts-arrow ts-next" aria-label="Diapositive suivante">→</button>' +
    '<div class="ts-nav"></div>' +
    '<p class="ts-note">Illustrations générées par intelligence artificielle, évoquant le réseau des tissus du corps (muscles, tendons, fascias). Approche de bien-être, non médicale.</p>';

  var track = root.querySelector('.ts-track'), nav = root.querySelector('.ts-nav');
  var boxes = [];
  slides.forEach(function (s, i) {
    var el = document.createElement('div');
    el.className = 'ts-slide'; el.style.setProperty('--accent', s.c);
    el.setAttribute('role', 'group'); el.setAttribute('aria-roledescription', 'diapositive'); el.setAttribute('aria-label', (i+1) + ' sur ' + slides.length);
    el.innerHTML = '<div class="ts-visual"><svg viewBox="0 0 300 460" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Schéma stylisé : ' + s.title.toLowerCase() + '">' + s.draw.map(piece).join('') + '</svg></div>' +
      '<div><p class="ts-step">' + (i+1) + ' / ' + slides.length + '</p><h3 class="ts-title">' + s.title + '</h3><p class="ts-text">' + s.t + '</p></div>';
    track.appendChild(el); boxes.push(el.querySelector('.ts-visual'));
    var b = document.createElement('button'); b.type = 'button';
    b.style.setProperty('--c', s.c); b.innerHTML = '<i></i>' + s.nav; b.onclick = function () { go(i); stop(); };
    nav.appendChild(b);
    if (i < slides.length - 1) { var a = document.createElement('span'); a.className = 'ts-sep'; a.textContent = '›'; a.setAttribute('aria-hidden', 'true'); nav.appendChild(a); }
  });
  var pp = document.createElement('button'); pp.type = 'button'; pp.className = 'ts-pp'; nav.appendChild(pp);

  // ---- chargement différé des images (au moment où la section approche de l'écran) ----
  var loaded = false;
  function loadImages() {
    if (loaded) return; loaded = true;
    slides.forEach(function (s, i) {
      var img = new Image(); img.alt = s.alt; img.decoding = 'async';
      if (s.pos) img.style.objectPosition = s.pos;
      img.onload = function () { boxes[i].appendChild(img); requestAnimationFrame(function () { boxes[i].classList.add('has-img'); }); };
      img.src = IMG_DIR + s.file + '.' + EXT;
    });
  }

  // ---- navigation ----
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var idx = 0, timer = null, playing = !reduce, visible = false, hover = false;
  function btns() { return nav.querySelectorAll('button:not(.ts-pp)'); }
  function go(i) {
    idx = (i + slides.length) % slides.length;
    track.style.transform = 'translateX(' + (-100 * idx) + '%)';
    Array.prototype.forEach.call(track.children, function (s, n) { s.setAttribute('aria-hidden', n !== idx); s.inert = n !== idx; });
    Array.prototype.forEach.call(btns(), function (b, n) { b.setAttribute('aria-current', n === idx); });
  }
  function tick() { clearInterval(timer); if (playing && visible && !hover) timer = setInterval(function () { go(idx + 1); }, 7000); }
  function label() { pp.textContent = playing ? '❚❚ Pause' : '▶ Lecture'; pp.setAttribute('aria-label', playing ? 'Mettre en pause le défilement' : 'Reprendre le défilement'); }
  function stop() { playing = false; label(); tick(); }
  pp.onclick = function () { playing = !playing; label(); tick(); };
  root.querySelector('.ts-prev').onclick = function () { go(idx - 1); stop(); };
  root.querySelector('.ts-next').onclick = function () { go(idx + 1); stop(); };
  root.addEventListener('mouseenter', function () { hover = true; tick(); });
  root.addEventListener('mouseleave', function () { hover = false; tick(); });
  root.setAttribute('tabindex', '-1');
  root.addEventListener('keydown', function (e) {           // flèches : uniquement quand le carrousel a le focus
    if (e.key === 'ArrowRight') { go(idx + 1); stop(); }
    if (e.key === 'ArrowLeft')  { go(idx - 1); stop(); }
  });
  var x0 = null;
  root.addEventListener('pointerdown', function (e) { x0 = e.clientX; });
  root.addEventListener('pointerup', function (e) { if (x0 !== null && Math.abs(e.clientX - x0) > 50) { go(idx + (e.clientX < x0 ? 1 : -1)); stop(); } x0 = null; });

  go(0); label();
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { visible = en[0].isIntersecting; if (visible) loadImages(); tick(); }, { rootMargin: '300px 0px' }).observe(root);
  } else { visible = true; loadImages(); tick(); }
})();
