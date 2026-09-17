import os

base = os.path.expanduser('~/synaptika.net')

faq_index = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qu'est-ce que Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Synaptika est un accompagnement en gestion du stress et developpement personnel propose par Thierry FELICIA, praticien en Martinique. Les methodes utilisees incluent la NST Bowen, le Touch for Health et des pratiques energetiques."
      }
    },
    {
      "@type": "Question",
      "name": "Comment fonctionne la technique des 3 minutes anti-stress ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La technique des 3 minutes est une approche simple pour calmer instantanement la tension accumulee. Elle s'appuie sur des rythmes naturels du corps et peut etre pratiquee n'importe ou, meme apres une journee epuisante. Les resultats varient selon les personnes."
      }
    },
    {
      "@type": "Question",
      "name": "Quels services propose Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Synaptika propose des seances individuelles de NST Bowen et Touch for Health, des stages en groupe et des produits numeriques (guides, formations). Ces prestations sont complementaires a tout suivi medical."
      }
    },
    {
      "@type": "Question",
      "name": "La NST Bowen est-elle une methode medicale ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. La NST Bowen est une approche de bien-etre complementaire. Elle ne constitue pas un traitement medical, un diagnostic ou une prescription. En cas de probleme de sante, consultez toujours un professionnel de sante qualifie."
      }
    },
    {
      "@type": "Question",
      "name": "Synaptika propose-t-il des ressources gratuites ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Synaptika met a disposition plusieurs guides gratuits telechargeables : techniques anti-stress, decouverte de votre signature de genie, carnet d'exploration socratique et d'autres ressources de bien-etre personnel."
      }
    }
  ]
}
</script>'''

faq_apropos = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qui est Thierry FELICIA ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thierry FELICIA est praticien en developpement personnel et gestion du stress en Martinique. Il est certifie en NST Bowen, Touch for Health et kinesiologie avancee. Il a egalement pratique et enseigne le Tai-Chi, Qi Gong et Ba Gua Zhang pendant plusieurs annees a Paris."
      }
    },
    {
      "@type": "Question",
      "name": "Qu'est-ce que la methode Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La methode Synaptika s'inspire du monde informatique : comme une mise a jour de logiciel, elle aide a identifier vos potentiels existants et a en activer de nouveaux. Elle combine kinesiologie, approches holistiques et sagesse ancestrale pour creer un environnement favorable au developpement personnel."
      }
    },
    {
      "@type": "Question",
      "name": "Quelles sont les certifications de Thierry FELICIA ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thierry FELICIA est certifie en Touch for Health (International Kinesiology College, Zurich), kinesiologie avancee (College Francais de Kinesiologie) et NST Bowen. Il a egalement une formation en naturopathie fondamentale."
      }
    },
    {
      "@type": "Question",
      "name": "Synaptika est-il une pratique medicale ou therapeutique ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. Synaptika n'est pas une pratique medicale, ni une methode de guerison. C'est un accompagnement pour creer de meilleures options personnelles et developper ses potentiels innes. Les prestations ne se substituent en aucun cas a des soins medicaux."
      }
    }
  ]
}
</script>'''

faq_zenbox = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qu'est-ce que la ZenBox Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La ZenBox est un programme de bien-etre qui combine la sagesse des 5 elements taoistes et des symboles universels. Elle propose des exercices pratiques pour explorer sa relation au stress et developper ses ressources personnelles."
      }
    },
    {
      "@type": "Question",
      "name": "Comment utiliser la ZenBox au quotidien ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La ZenBox peut etre integree a votre routine matinale. Les exercices sont concus pour etre pratiques en quelques minutes. Les effets percus varient selon les personnes et leur investissement dans la pratique."
      }
    },
    {
      "@type": "Question",
      "name": "La ZenBox remplace-t-elle un suivi medical ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. La ZenBox est un outil d'exploration personnelle et de bien-etre. Elle ne constitue pas un traitement medical. En cas de probleme de sante persistant, consultez un professionnel de sante qualifie."
      }
    }
  ]
}
</script>'''

faq_contact = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Comment prendre rendez-vous avec Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vous pouvez prendre rendez-vous via le formulaire de contact disponible sur cette page. Thierry FELICIA vous repondra pour convenir d'une seance individuelle de NST Bowen, Touch for Health ou d'un stage en groupe."
      }
    },
    {
      "@type": "Question",
      "name": "Les seances se deroulent-elles en presentiel ou en ligne ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Synaptika propose des seances en Martinique ainsi que des accompagnements a distance selon les besoins. Contactez directement Thierry FELICIA pour connaitre les modalites disponibles."
      }
    },
    {
      "@type": "Question",
      "name": "Combien coute une seance ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Les tarifs varient selon le type de prestation. Contactez Synaptika via le formulaire pour obtenir les informations tarifaires actualisees."
      }
    }
  ]
}
</script>'''

faq_ressources = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Quelles ressources gratuites propose Synaptika ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Synaptika propose plusieurs guides gratuits : un kit de decouverte de votre signature de genie, un carnet d'exploration socratique avec 21 questions, des techniques anti-stress naturelles et d'autres ressources de bien-etre personnel."
      }
    },
    {
      "@type": "Question",
      "name": "Ces ressources gratuites sont-elles vraiment sans engagement ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Les ressources gratuites de Synaptika sont telechargeable sans carte bancaire et sans engagement. Elles sont des supports d'information et d'exploration personnelle."
      }
    },
    {
      "@type": "Question",
      "name": "Ces guides remplacent-ils un accompagnement professionnel ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. Ces guides sont des outils d'exploration personnelle. Ils ne constituent pas un traitement medical ou psychologique. En cas de besoin, consultez un professionnel de sante qualifie."
      }
    }
  ]
}
</script>'''

pages = {
    'index.html': faq_index,
    'apropos.html': faq_apropos,
    'zenbox.html': faq_zenbox,
    'contact.html': faq_contact,
    'ressourcesgratuites.html': faq_ressources,
}

for filename, faq in pages.items():
    path = os.path.join(base, filename)
    c = open(path, encoding='utf-8').read()
    if 'FAQPage' not in c:
        c = c.replace('</head>', faq + '\n</head>', 1)
        open(path, 'w', encoding='utf-8').write(c)
        print('OK: ' + filename)
    else:
        print("SKIP: " + filename)
