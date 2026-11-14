# Audit juridique de la communication de Synaptika

**Date de l'audit :** 14 novembre 2026
**Réalisé par :** nyp7 (avec assistance)
**Objet :** Mise en conformité des contenus du site (articles de blog et pages statiques) avec les exigences de la DGCCRF en matière d'allégations thérapeutiques et de pratiques commerciales trompeuses.

---

## Contexte

Dans le cadre de la réglementation applicable aux praticiens du bien-être, il est interdit de :
- Promettre un effet thérapeutique (guérison, soulagement, traitement) sans être professionnel de santé.
- Utiliser un vocabulaire médical (noms de pathologies, termes cliniques).
- Donner des conseils médicaux (posologie, fréquence de traitement, etc.).
- Recourir à des allégations de santé non prouvées (élimination des toxines, prévention de maladies).

Cet audit vise à identifier et corriger ces formulations sur l'ensemble du site.

---

## Méthodologie

1. **Scan automatique** de tous les fichiers HTML (`blog/` et racine) à la recherche de mots-clés à risque : guérison, guérir, thérapeutique, soulagement, douleur, lombalgie, tendinite, TMS, maladie, pathologie, toxine, révolutionnaire, miracle, etc.
2. **Analyse du contexte** de chaque occurrence (pour distinguer les allégations des négations ou des citations).
3. **Correction ciblée** des passages problématiques, avec validation manuelle.
4. **Publication** via Git (commits traçables, un par vague de correction).

---

## Articles de blog corrigés

### Corrections majeures (allégations thérapeutiques)

- **`bowen-tms.html`** (article sur les manutentionnaires)
  - Titre, meta description, `headline` JSON-LD : remplacement de « solution révolutionnaire » et « face aux TMS ».
  - Vague 1 : suppression de 11 allégations thérapeutiques (auto-guérison, lombalgies, tendinites, etc.).
  - Vague 2 : suppression de 7 références médicales (TMS, maladies professionnelles, etc.).
  - Vague 3 : nettoyage des dernières ambiguïtés (meta keywords, ancres, conclusion).
  - Ajout d'une mention légale visible (encadré violet) : « La NST Bowen est une approche de bien-être et de détente. Elle ne constitue pas un acte médical et ne se substitue en aucun cas à un avis ou à un traitement médical. »

- **`bowen.html`** (article sur les caissières)
  - Meta keywords supprimée, `headline` JSON-LD corrigé, « douleurs » → « tensions ».
  - Lien vers `bowen-tms` mis à jour avec le nouveau titre.
  - Ajout de la même mention légale visible.
  - Correction des conseils santé (hydratation, toxines, huile de coco, tarif, fréquence des séances).

### Corrections d'allégations santé

- **`alimentation-sport.html`** : suppression de l'allégation « prévention des maladies (cardiaques, diabète, cancers) ».
- **`qi-gong-tai-chi.html`** : « réduit les douleurs chroniques » → « favorise le confort au quotidien ».
- **`grainesgermees.html`** : « préviennent les maladies cardiovasculaires » → « participent à une alimentation équilibrée ».
- **`5-elements-tao-cuisine-creole-emotions-martinique.html`** : « Lombalgies chroniques » → « Tensions au niveau du dos ».
- **`eau.html`** : « élimination naturelle des toxines » → « contribue à une bonne hydratation ».
- **`deroulement-seance-nst.html`** : « élimine des toxines » → « rester hydraté(e) ».

### Liens rafraîchis (mise à jour des titres d'articles)

- **`epsom.html`**, **`tfh.html`**, **`dauphins.html`** : mise à jour des liens « à lire aussi » vers `bowen-tms` et `bowen` avec les nouveaux titres.

### Articles vérifiés (déjà prudents, aucune modification)

- `rimed-razie.html` (avertissements médicaux présents)
- `nst-sommeil.html` (avertissements médicaux présents)
- `synergie-aromatique.html` (« pas une solution miracle » — négation)
- `resilience.html` (vocabulaire émotionnel, pas médical)
- `rythmes-circadiens-hiboux.html` (contexte scientifique prudent)
- `laotseu.html` (avertissement + citation)
- `sagesse-eau.html` (« pas une promesse de solution miracle » — négation)
- `revolution-cantine-japon.html` (« révolutionnaire » au sens figuré)
- `passe-avenir.html` (« guérir » au sens émotionnel)
- `ombre-lumiere.html` (« douleur » au sens métaphorique)
- `fuir-rend-plus-fort.html` (« douleur » au sens émotionnel)
- `comment-optimiser-pratique-eft.html` (avertissement présent)
- `approche-synaptika.html` (« pas une solution miracle » — négation)
- `pourquoi-le-repos-ne-suffit-pas.html` (« pas un soin médical, ni une solution miracle » — négation)
- `nst-bowen-creole.html` (lien vers `bowen-tms` à jour)
- `bowen.html` (voir corrections ci-dessus)

### Pages statiques vérifiées

- **`apropos.html`** : « pas un programme miracle », « sans promesse miracle » — négations, aucune modification nécessaire.
- Les 11 autres pages statiques (`index.html`, `cgv.html`, `mentions-legales.html`, etc.) ne contiennent aucun mot à risque.

---

## Résultat

L'ensemble des contenus du site (articles de blog et pages statiques) a été passé en revue. **Aucune allégation thérapeutique, référence médicale ou promesse de résultat ne subsiste dans les contenus publiés.**

Les deux articles principaux (`bowen-tms.html` et `bowen.html`) disposent d'une mention légale visible précisant le caractère non médical de la pratique.

---

## Traçabilité

Les corrections ont été publiées via les commits Git suivants (branche `main`) :

- `d85559d` : reformulation prudente du titre et des métadonnées de `bowen-tms`.
- `fec9372` : titre `bowen-tms` aligné dans `posts.js` et `blog.html`.
- `1579f09` : vague 1 (allégations thérapeutiques).
- `65b2d4c` : vague 2 (références médicales).
- `9f840ba` : vague 3 (finitions).
- `2690901` : vague 3 bis (dernière allégation).
- `34da4c1` : ajout de la mention légale dans `bowen-tms`.
- `a33b2b6` : nettoyage complet de `bowen.html`.
- `66595cb` : harmonisation de la mention légale dans `bowen-tms`.
- `f05315c` : correction des conseils santé dans `bowen.html`.
- `3714ba1` : mise à jour des liens dans `epsom.html`.
- `fce26b7` : mise à jour des liens dans `tfh.html`.
- `0c23b03` : mise à jour des liens dans `dauphins.html`.
- `b1b5025` : suppression de l'allégation santé dans `alimentation-sport.html`.
- `7c44acb` : suppression des dernières allégations santé (5 fichiers).

---

*Ce document est conservé à titre de traçabilité. Il pourra être mis à jour si de nouveaux contenus sont ajoutés au site.*
