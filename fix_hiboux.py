with open('blog/rythmes-circadiens-hiboux.html', encoding='utf-8') as f:
    c = f.read()

import re
mots = {
    "ignoree": "ignorée", "epuisent": "épuisent", "frequentes": "fréquentes",
    "precisement": "précisément", "tot": "tôt", "societe": "société",
    "epuises": "épuisés", "designe": "désigne", "regulisent": "régulent",
    "temperature": "température", "secretion": "sécrétion", "metabolisme": "métabolisme",
    "possede": "possède", "lumiere": "lumière", "tombee": "tombée",
    "generales": "générales", "plutot": "plutôt", "evidence": "évidence",
    "genes": "gènes", "reels": "réels", "difficultes": "difficultés",
    "qualite": "qualité", "degradee": "dégradée", "ecrans": "écrans",
    "regulateur": "régulateur", "Reduire": "Réduire", "regularite": "régularité",
    "documentes": "documentés", "fenetre": "fenêtre", "soiree": "soirée",
    "malgre": "malgré", "etat": "état", "creer": "créer", "decaler": "décaler",
    "frequemment": "fréquemment", "citee": "citée", "specialistes": "spécialistes",
    "precedant": "précédant", "etudes": "études", "suggerent": "suggèrent",
    "evaluation": "évaluation", "medicale": "médicale", "difference": "différence",
    "evaluer": "évaluer", "adaptees": "adaptées", "qualifie": "qualifié",
    "kinesologie": "kinésologie", "instabilite": "instabilité",
    "arterielle": "artérielle", "demarche": "démarche", "repond": "répond",
    "preparer": "préparer", "prepares": "préparés",
}
for m, b in mots.items():
    c = re.sub(r'\b' + re.escape(m) + r'\b', b, c)

phrases = [
    ("aide a synchroniser", "aide à synchroniser"),
    ("aider a le décaler", "aider à le décaler"),
    ("a titre informatif", "à titre informatif"),
    ("naturelle a être actif", "naturelle à être actif"),
    ("A la tombée de la nuit", "À la tombée de la nuit"),
    ("commence a sécréter", "commence à sécréter"),
    ("au repos. A l'aube", "au repos. À l'aube"),
    ("l'organisme a l'eveil", "l'organisme à l'éveil"),
    ("associee a des difficultés", "associée à des difficultés"),
    ("chronique est associe a une", "chronique est associé à une"),
    ("au moment ou son organisme", "au moment où son organisme"),
    ("le mieux prepare pour agir", "le mieux préparé pour agir"),
    ("fonctionner a son plein potentiel", "fonctionner à son plein potentiel"),
    ("s'exposer a la lumière", "s'exposer à la lumière"),
    ("aider l'organisme a préparer plus naturellement", "aider l'organisme à préparer plus naturellement"),
    ("se lever a des heures stables", "se lever à des heures stables"),
    ("n'arrivez pas a vous reposer", "n'arrivez pas à vous reposer"),
    ("favorables a la récupération", "favorables à la récupération"),
    ("le moment ou vous le faites", "le moment où vous le faites"),
    ("un facteur a prendre en compte.", "un facteur à prendre en compte."),
    ("facteur a prendre en compte dans une démarche", "facteur à prendre en compte dans une démarche"),
    ("ont observe des liens", "ont observé des liens"),
    ("Un rythme circadien perturbe et", "Un rythme circadien perturbé et"),
    ("Vous avez aime cet article", "Vous avez aimé cet article"),
    ("qui prepare le corps au repos", "qui prépare le corps au repos"),
    ("prepare l'organisme", "prépare l'organisme"),
    ("en partie determine par", "en partie déterminé par"),
    ("change concretement", "change concrètement"),
    ("pourquoi on n'arrive pas a se reposer", "pourquoi on n'arrive pas à se reposer"),
    ("melatonine", "mélatonine"),
    ("pineale", "pinéale"),
    ("bien sur,", "bien sûr,"),
    ("C'est ca, la loi circadienne", "C'est ça, la loi circadienne"),
    ("qu'il ne s'épuisé pas", "qu'il ne s'épuise pas"),
]
for old, new in phrases:
    c = c.replace(old, new)

with open('blog/rythmes-circadiens-hiboux.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("✅ Article hiboux : toutes les corrections appliquées")
