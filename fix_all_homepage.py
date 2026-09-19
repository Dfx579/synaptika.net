from pathlib import Path

f = Path("index.html")
content = f.read_text(encoding="utf-8")

start_marker = '<section class="hero">'
end_marker = '<!-- Blog Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERREUR : marqueur introuvable, verifie index.html")
    raise SystemExit(1)

new_block = '''<!-- Hero Section -->
<section class="hero">
  <div class="hero-content">
    <h1>Un temps pour souffler quand le stress s'installe</h1>
    <p>Un accompagnement de bien-être adapté à votre rythme, dans un cadre calme et non médical.</p>
  </div>
</section>

<!-- Offre principale : Séance NST Bowen -->
<section id="seance" class="section-offer">
  <div class="container">
    <div class="offer-heading">
      <i data-feather="calendar"></i>
      <h2>Séances individuelles de bien-être NST Bowen à Fort-de-France</h2>
    </div>
    <p class="offer-subtitle">
      Une approche corporelle douce pour relâcher les tensions accumulées et retrouver confort et détente.<br>
      <strong>Quarante-cinq minutes sur rendez-vous, 90 €.</strong>
    </p>
    <div class="offer-layout">
      <div class="offer-image-wrap">
        <img src="images/fond1.webp" alt="Séance NST Bowen bien-être Fort-de-France" width="280" height="320" loading="lazy" style="border-radius: 16px; object-fit: cover;">
      </div>
      <div class="offer-box">
        <h3>Ce que vous apporte la séance :</h3>
        <div class="offer-grid">
          <div class="offer-grid-item">
            <span class="icon">🌿</span>
            <div><h4>Relâchement des tensions</h4><p>Des gestes doux et précis sur des points clés pour inviter le corps à relâcher la pression.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Quarante-cinq minutes pour vous</h4><p>Un créneau dédié au calme, loin de l'agitation et des sollicitations du quotidien.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Cabinet à Fort-de-France</h4><p>Un espace discret et accueillant, accessible sur rendez-vous.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Cadre clair et bienveillant</h4><p>Pratique non médicale orientée confort et équilibre corporel.</p></div>
          </div>
        </div>
        <p class="offer-note"><em>Cette approche de bien-être s'inscrit dans une démarche de confort personnel et ne se substitue pas à un avis médical.</em></p>
        <div style="text-align: center; margin-top: 25px;">
          <a href="https://tally.so/r/lb1GPX" target="_blank" rel="noopener noreferrer" class="btn btn-rounded" style="font-size: 1.1rem; padding: 16px 32px; display: inline-block;">
            🌟 Je prends rendez-vous (90 €) →
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Lead Magnet -->
<section id="offer" class="section-offer" style="background: #fafafa; border-top: 1px solid #eee; border-bottom: 1px solid #eee;">
  <div class="container">
    <div class="offer-heading">
      <i data-feather="book-open"></i>
      <h2>Des techniques simples, expérimentées avant d'être transmises</h2>
    </div>
    <p class="offer-subtitle">
      Cinq approches d'exploration personnelle pour calmer le mental et retrouver votre équilibre naturel, à pratiquer chez vous en dix minutes. Découvrez-les librement dans ce guide gratuit.
    </p>
    <div class="offer-layout">
      <div class="offer-image-wrap">
        <img src="images/guide-lead.webp" alt="Guide gratuit Synaptika" width="280" height="320" loading="lazy" style="border-radius: 16px; object-fit: contain; background-color: #fafafa;">
      </div>
      <div class="offer-box">
        <h3>Ce que vous allez explorer :</h3>
        <div class="offer-grid">
          <div class="offer-grid-item">
            <div><h4>Relâchement du mental</h4><p>Une pratique d'attention progressive pour inviter l'esprit à se poser.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Le mouvement libérateur</h4><p>Remettre le corps en dynamique pour évacuer les tensions accumulées.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Vitalité et équilibre</h4><p>Des repères simples pour nourrir l'organisme et respecter son rythme.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Habiter son corps</h4><p>L'attention portée à l'équilibre corporel comme trésor de longévité.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>La ressource du geste simple</h4><p>Une posture de la main qui active l'apaisement plutôt que la réaction de stress.</p></div>
          </div>
        </div>
        <p class="offer-note"><em>Ces techniques sont des outils d'exploration personnelle. Elles ne remplacent pas un suivi médical.</em></p>
        <form method="post" action="https://sendfox.com/form/1k85w9/1r0poy" class="signup-form sendfox-form" id="1r0poy" data-async="true" data-recaptcha="false">
          <div class="form-group">
            <input type="text" id="sendfox_form_name" placeholder="Votre prénom" name="first_name" required>
          </div>
          <div class="form-group">
            <input type="email" id="sendfox_form_email" placeholder="Votre email" name="email" required>
          </div>
          <div style="position: absolute; left: -5000px;" aria-hidden="true">
            <input type="text" name="a_password" tabindex="-1" value="" autocomplete="off">
          </div>
          <p class="form-privacy-note">🔒 Vos données sont protégées et jamais partagées. ✉️ Aucun spam.</p>
          <div class="form-group form-consent">
            <label style="display:flex; align-items:flex-start; gap:8px; font-size:0.85rem; color:#555; cursor:pointer;">
              <input type="checkbox" id="consent_checkbox" required style="margin-top:3px;">
              <span>J'accepte de recevoir le guide gratuit et d'être contacté(e) par Thierry Felicia. <a href="/politique-confidentialite" target="_blank" style="color:#5B3E9C;">Voir la politique de confidentialité</a>.</span>
            </label>
          </div>
          <button type="submit" class="btn-submit" id="submit_guide_btn" disabled style="opacity:0.5; cursor:not-allowed;">Recevoir le guide gratuit →</button>
        </form>
        <script src="https://cdn.sendfox.com/js/form.js" charset="utf-8"></script>
        <script>
          (function() {
            var checkbox = document.getElementById('consent_checkbox');
            var btn = document.getElementById('submit_guide_btn');
            if (checkbox && btn) {
              checkbox.addEventListener('change', function() {
                btn.disabled = !checkbox.checked;
                btn.style.opacity = checkbox.checked ? '1' : '0.5';
                btn.style.cursor = checkbox.checked ? 'pointer' : 'not-allowed';
              });
            }
          })();
        </script>
      </div>
    </div>
  </div>
</section>

<!-- Rappel de réservation -->
<section class="section-holistic">
  <div class="container">
    <h2>Votre temps de pause commence ici</h2>
    <p>Vous n'avez pas besoin de tout changer d'un coup.</p>
    <p>Il suffit d'un premier pas : une séance, un espace où votre corps et votre esprit peuvent enfin souffler.</p>
    <p>Que vous ressentiez de la tension, de la fatigue ou simplement le besoin de relâcher la pression, la séance vous offre un espace adapté à votre rythme.</p>
    <p><strong>Une approche douce, attentive et orientée vers votre confort corporel.</strong></p>
    <p class="methods-tags">🤲 NST Bowen &nbsp;·&nbsp; 🖐️ Touch for Health &nbsp;·&nbsp; 🌀 Approches douces</p>
    <div style="margin-top: 25px;">
      <a href="https://tally.so/r/lb1GPX" target="_blank" rel="noopener noreferrer" class="btn btn-rounded">🌟 Réserver mon créneau à Fort-de-France (90 €) →</a>
    </div>
  </div>
</section>

<!-- Free Resources Section -->
<section class="section-resources">
    <div class="container">
        <h2>Ressources gratuites</h2>
        <p>Découvrez nos guides et conseils éprouvés pour améliorer votre qualité de vie et gérer le stress naturellement en Martinique. Techniques holistiques adaptées à vos besoins.</p>
        <a class="btn btn-rounded" href="/ressourcesgratuites">Télécharger nos guides gratuits</a>
    </div>
</section>

'''

new_content = content[:start_idx] + new_block + content[end_idx:]
f.write_text(new_content, encoding="utf-8")
print("index.html corrige : accents retablis, case a cocher + bouton conditionnel ajoutes, Ressources gratuites restaure.")
