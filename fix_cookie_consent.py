import pathlib

f = pathlib.Path("index.html")
content = f.read_text(encoding="utf-8")

# --- Bloc 1 : remplacer le chargement inconditionnel de counter.dev + Tawk.to ---
old_block = '''<script async src="https://cdn.counter.dev/script.js" data-id="f5657ede-6192-41bd-a900-2c95071972e3" data-utcoffset="-4"></script>

<!--Start of Tawk.to Script：スクロール/クリック後に遅延読み込み（速度改善） -->
<script type="text/javascript">
(function(){
  function loadTawk(){
    if(window._tawkLoaded) return;
    window._tawkLoaded = true;
    var Tawk_API = Tawk_API || {};
    var s1 = document.createElement("script");
    s1.async = true;
    s1.src = 'https://embed.tawk.to/6329db7454f06e12d895d62c/1gddo2ft4';
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin','*');
    document.body.appendChild(s1);
  }
  ['scroll','click','touchstart','keydown'].forEach(function(e){
    window.addEventListener(e, loadTawk, {once: true, passive: true});
  });
  setTimeout(loadTawk, 4000);
})();
</script>
<!--End of Tawk.to Script-->'''

new_block = '''<!--Start of Tawk.to + counter.dev (charges uniquement apres consentement) -->
<script type="text/javascript">
function loadTawkAndCounter(){
  if(window._extrasLoaded) return;
  window._extrasLoaded = true;

  var cs = document.createElement("script");
  cs.async = true;
  cs.src = "https://cdn.counter.dev/script.js";
  cs.setAttribute("data-id", "f5657ede-6192-41bd-a900-2c95071972e3");
  cs.setAttribute("data-utcoffset", "-4");
  document.body.appendChild(cs);

  var Tawk_API = Tawk_API || {};
  var s1 = document.createElement("script");
  s1.async = true;
  s1.src = 'https://embed.tawk.to/6329db7454f06e12d895d62c/1gddo2ft4';
  s1.charset = 'UTF-8';
  s1.setAttribute('crossorigin','*');
  document.body.appendChild(s1);
}
// Si deja accepte lors d'une visite precedente : chargement differe (scroll/clic/4s) pour la performance
if (localStorage.getItem('cookiesAccepted') === 'true') {
  ['scroll','click','touchstart','keydown'].forEach(function(e){
    window.addEventListener(e, loadTawkAndCounter, {once: true, passive: true});
  });
  setTimeout(loadTawkAndCounter, 4000);
}
</script>
<!--End of Tawk.to + counter.dev-->'''

if old_block not in content:
    print("ERREUR : bloc counter.dev/Tawk introuvable, aucune modification faite")
    raise SystemExit(1)

content = content.replace(old_block, new_block, 1)

# --- Bloc 2 : faire en sorte qu'accepter les cookies charge aussi Tawk.to + counter.dev immediatement ---
old_accept = '''function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookieBanner').classList.remove('show');
    loadGTM(); // Charger GTM uniquement maintenant
}'''

new_accept = '''function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookieBanner').classList.remove('show');
    loadGTM(); // Charger GTM uniquement maintenant
    loadTawkAndCounter(); // Charger Tawk.to et counter.dev uniquement maintenant
}'''

if old_accept not in content:
    print("ERREUR : fonction acceptCookies introuvable, aucune modification faite (bloc 2)")
    raise SystemExit(1)

content = content.replace(old_accept, new_accept, 1)

f.write_text(content, encoding="utf-8")
print("OK : counter.dev et Tawk.to sont maintenant conditionnes au consentement cookies.")
