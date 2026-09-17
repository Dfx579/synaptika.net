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
    <p>Un accompagnement de bien-etre adapte a votre rythme, dans un cadre calme et non medical.</p>
  </div>
</section>

<!-- Offre principale : Seance NST Bowen -->
<section id="seance" class="section-offer">
  <div class="container">
    <div class="offer-heading">
      <i data-feather="calendar"></i>
      <h2>Seances individuelles de bien-etre NST Bowen a Fort-de-France</h2>
    </div>
    <p class="offer-subtitle">
      Une approche corporelle douce pour relacher les tensions accumulees et retrouver confort et detente.<br>
      <strong>Quarante-cinq minutes sur rendez-vous, 90 euros.</strong>
    </p>
    <div class="offer-layout">
      <div class="offer-image-wrap">
        <img src="images/fond1.webp" alt="Seance NST Bowen bien-etre Fort-de-France" width="280" height="320" loading="lazy" style="border-radius: 16px; object-fit: cover;">
      </div>
      <div class="offer-box">
        <h3>Ce que vous apporte la seance :</h3>
        <div class="offer-grid">
          <div class="offer-grid-item">
            <span class="icon">🌿</span>
            <div><h4>Relachement des tensions</h4><p>Des gestes doux et precis sur des points cles pour inviter le corps a relacher la pression.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Quarante-cinq minutes pour vous</h4><p>Un creneau dedie au calme, loin de l'agitation et des sollicitations du quotidien.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Cabinet a Fort-de-France</h4><p>Un espace discret et accueillant, accessible sur rendez-vous.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Cadre clair et bienveillant</h4><p>Pratique non medicale orientee confort et equilibre corporel.</p></div>
          </div>
        </div>
        <p class="offer-note"><em>Cette approche de bien-etre s'inscrit dans une demarche de confort personnel et ne se substitue pas a un avis medical.</em></p>
        <div style="text-align: center; margin-top: 25px;">
          <a href="https://tally.so/r/lb1GPX" target="_blank" rel="noopener noreferrer" class="btn btn-rounded" style="font-size: 1.1rem; padding: 16px 32px; display: inline-block;">
            🌟 Je prends rendez-vous (90 euros) →
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
      <h2>Des techniques simples, experimentees avant d'etre transmises</h2>
    </div>
    <p class="offer-subtitle">
      Cinq approches d'exploration personnelle pour calmer le mental et retrouver votre equilibre naturel, a pratiquer chez vous en dix minutes. Decouvrez-les librement dans ce guide gratuit.
    </p>
    <div class="offer-layout">
      <div class="offer-image-wrap">
        <img src="images/guide-lead.webp" alt="Guide gratuit Synaptika" width="280" height="320" loading="lazy" style="border-radius: 16px; object-fit: contain; background-color: #fafafa;">
      </div>
      <div class="offer-box">
        <h3>Ce que vous allez explorer :</h3>
        <div class="offer-grid">
          <div class="offer-grid-item">
            <div><h4>Relachement du mental</h4><p>Une pratique d'attention progressive pour inviter l'esprit a se poser.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Le mouvement liberateur</h4><p>Remettre le corps en dynamique pour evacuer les tensions accumulees.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Vitalite et equilibre</h4><p>Des reperes simples pour nourrir l'organisme et respecter son rythme.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>Habiter son corps</h4><p>L'attention portee a l'equilibre corporel comme tresor de longevite.</p></div>
          </div>
          <div class="offer-grid-item">
            <div><h4>La ressource du geste simple</h4><p>Une posture de la main qui active l'apaisement plutot que la reaction de stress.</p></div>
          </div>
        </div>
        <p class="offer-note"><em>Ces techniques sont des outils d'exploration personnelle. Elles ne remplacent pas un suivi medical.</em></p>
        <form method="post" action="https://sendfox.com/form/1k85w9/1r0poy" class="signup-form sendfox-form" id="1r0poy" data-async="true" data-recaptcha="false">
          <div class="form-group">
            <input type="text" id="sendfox_form_name" placeholder="Votre prenom" name="first_name" required>
          </div>
          <div class="form-group">
            <input type="email" id="sendfox_form_email" placeholder="Votre email" name="email" required>
          </div>
          <div style="position: absolute; left: -5000px;" aria-hidden="true">
            <input type="text" name="a_password" tabindex="-1" value="" autocomplete="off">
          </div>
          <p class="form-privacy-note">Vos donnees sont protegees et jamais partagees.</p>
          <button type="submit" class="btn-submit">Recevoir le guide gratuit →</button>
          <p class="form-spam-note">🔒 Donnees protegees &nbsp;·&nbsp; ✉️ Aucun spam.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- Rappel de reservation -->
<section class="section-holistic">
  <div class="container">
    <h2>Votre temps de pause commence ici</h2>
    <p>Vous n'avez pas besoin de tout changer d'un coup.</p>
    <p>Il suffit d'un premier pas : une seance, un espace ou votre corps et votre esprit peuvent enfin souffler.</p>
    <p>Que vous ressentiez de la tension, de la fatigue ou simplement le besoin de relacher la pression, la seance vous offre un espace adapte a votre rythme.</p>
    <p><strong>Une approche douce, attentive et orientee vers votre confort corporel.</strong></p>
    <p class="methods-tags">🤲 NST Bowen &nbsp;·&nbsp; 🖐️ Touch for Health &nbsp;·&nbsp; 🌀 Approches douces</p>
    <div style="margin-top: 25px;">
      <a href="https://tally.so/r/lb1GPX" target="_blank" rel="noopener noreferrer" class="btn btn-rounded">🌟 Reserver mon creneau a Fort-de-France (90 euros) →</a>
    </div>
  </div>
</section>

'''

new_content = content[:start_idx] + new_block + content[end_idx:]
f.write_text(new_content, encoding="utf-8")
print("index.html mis a jour avec succes.")
