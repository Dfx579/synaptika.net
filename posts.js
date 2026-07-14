// Liste des articles du blog Synaptika
const posts = [
  {
    title: "🌴 5 éléments du Tao en cuisine créole : les plats martiniquais qui régulent vos émotions",
    file: "./blog/5-elements-tao-cuisine-creole-emotions-martinique",
    excerpt: "Citron pays, margose, giromon, christophine, pois noirs : votre cuisine créole a toujours su prendre soin de vous.",
    date: "2026-06-21",
    author: "Felicia Thierry",
    reads: "15 min",
    image: "./blog/images/5-elements-assiette.jpg",
    tags: ["5Éléments", "Tao", "CuisineCreole", "Martinique", "Émotions"],
    category: "Nutrition créole"
  },
  {
    title: "🌿 Comment optimiser votre pratique de l'EFT ?",
    file: "./blog/comment-optimiser-pratique-eft",
    excerpt: "Tapoter plus ne suffit pas. Découvrez comment enrichir votre pratique de l'EFT grâce à une lecture énergétique globale.",
    date: "2026-06-26",
    author: "Felicia Thierry",
    reads: "10 min",
    image: "./blog/images/image-optimisee-eft-meridiens.jpg",
    tags: ["EFT", "Tapping", "Méridiens", "Énergétique", "Bien-être"],
    category: "Bien-être holistique"
  },
  {
    title: "Igname, Manioc, Patate Douce : Ce que Votre Grand-Mère Savait Déjà",
    file: "./blog/igname-manioc-patate-douce",
    excerpt: "Votre grand-mère n'avait pas de diplôme en nutrition. Elle avait un jardin.",
    date: "2026-06-11",
    author: "Thierry FELICIA",
    reads: "8 min",
    image: "./blog/images/igname-manioc-patate-douce.jpg",
    tags: ["Nutrition créole", "Bien-être", "CuisineAntillaise", "AntiStress"],
    category: "Nutrition créole"
  },
  {
    title: "🛑 Pourquoi plus vous travaillez dur sous pression, plus vous sabotez vos résultats : Le piège de l'identité héroïque",
    file: "./blog/identite-heroique-stress",
    excerpt: "Entrepreneurs et cadres : comprenez pourquoi vos meilleures intentions échouent quand la pression monte — et comment sortir du piège identitaire.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/pression-travail-entrepreneur-cafe.webp",
    tags: ["Développement personnel", "Leadership", "Gestion du stress", "Entrepreneur"],
    category: "Développement personnel"
  },
  {
    title: "🪐 Pourquoi le même stress revient-il toujours ? Ce que votre thème astral peut vous révéler",
    file: "./blog/theme-astral-stress",
    excerpt: "Le stress n'est pas toujours lié à vos circonstances actuelles — il puise parfois ses racines dans des empreintes symboliques bien plus profondes.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/theme-astral-stress.webp",
    tags: ["Développement personnel", "Astrologie", "Gestion du stress", "Connaissance de soi"],
    category: "Développement personnel"
  },
  {
    title: "🌴 7 smoothies créoles pour les 7 visages du stress",
    file: "./blog/smoothie-creole",
    excerpt: "Une fusion entre les saveurs tropicales et les plantes médicinales pour transformer votre gestion du stress en plaisir quotidien savoureux.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/smoothie.webp",
    tags: ["Nutrition créole", "Bien-être", "Martinique Nature", "Libération stress"],
    category: "Nutrition créole"
  },
  {
    title: "Ce que votre miroir sait de vous — et que vous ne regardez plus",
    file: "./blog/miroir",
    excerpt: "Décryptez les signaux subtils que votre organisme vous envoie chaque matin : mains, ongles, yeux.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/femme-mirroir.webp",
    tags: ["Bien-être", "Développement personnel", "Conscience corporelle"],
    category: "Développement personnel"
  },
  {
    title: "La sagesse de l'eau : pourquoi résister au changement nous épuise 💧 [Guide pratique]",
    file: "./blog/sagesse-eau",
    excerpt: "Série \"Le flux du changement\" — Article 1/3",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/sagesse-eau.webp",
    tags: ["Développement personnel", "Gestion du stress", "Libération stress"],
    category: "Développement personnel"
  },
  {
    title: "Et si ce qu'on cherche à fuir était justement ce qui nous rend plus forts ?",
    file: "./blog/fuir-rend-plus-fort",
    excerpt: "Ce que des enfants dans la boue, un système immunitaire et un système d'exploitation ont en commun",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/boue-immunite.webp",
    tags: ["Bien-être", "Développement personnel", "Libération stress"],
    category: "Développement personnel"
  },
  {
    title: "Et si la solution n'était pas de faire plus — mais d'aller plus profond ?",
    file: "./blog/qi-gong-tai-chi",
    excerpt: "Qi Gong et Tai Ch'i : une sagesse ancestrale, des bienfaits prouvés que vous ne soupçonnez pas encore",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/tai-chi-maitre-ballerine-chef-orchestre-harmonie.webp",
    tags: ["Bien-être", "Tai Ji Chuan", "Qi Gong"],
    category: "Bien-être holistique"
  },
  {
    title: "Ce que votre grand-mère savait que Google ne sait pas",
    file: "./blog/rimed-razie",
    excerpt: "Rimèd razié : 10 plantes médicinales créoles de Martinique pour le stress, le sommeil et la vitalité — le patrimoine vivant des yayas",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/rimed-razie.webp",
    tags: ["Bien-être", "Rimèd Razié", "Martinique Nature"],
    category: "Bien-être holistique"
  },
  {
    title: "Ces ressources que le stress a ensevelies — et comment les retrouver",
    file: "./blog/ressources-enfouies",
    excerpt: "Et si rien ne s'était perdu — mais était simplement enseveli ? 🌱",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/chemin-foret.webp",
    tags: ["Bien-être", "Développement personnel", "Libération stress"],
    category: "Développement personnel"
  },
  {
    title: "Ce que les affiches japonaises nous apprennent sur la légèreté",
    file: "./blog/affiches-japonaises",
    excerpt: "Comment un bout de papier peut transformer votre rapport au stress 🌸",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/ruelle-de-quartier-populaire.webp",
    tags: ["Japon", "Bien-être"],
    category: "Sagesses & Inspiration"
  },
  {
    title: "Transformez votre quotidien en 10 minutes par jour : le pouvoir des micro-évolutions",
    file: "./blog/transformez-votre-quotidien-10-minutes",
    excerpt: "Même si vous vous sentez dépassé. Même si vous êtes épuisé.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/jeune-pousse.webp",
    tags: ["Développement personnel", "Bien-être"],
    category: "Développement personnel"
  },
  {
    title: "Et si vos émotions vous parlaient déjà de votre prochaine transformation ? 🌸",
    file: "./blog/essence-yiking",
    excerpt: "Ce que vous ressentez n'est pas un problème",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/essence.webp",
    tags: ["Développement personnel", "Essences florales", "Yi King"],
    category: "Bien-être holistique"
  },
  {
    title: "La synergie aromatique qui crée une pause mentale en quelques instants",
    file: "./blog/synergie-aromatique",
    excerpt: "Et pourquoi vous avez tout faux sur la menthe poivrée",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/aromatherapie-efficace.webp",
    tags: ["Libération stress", "Aromathérapie efficace"],
    category: "Bien-être holistique"
  },
  {
    title: "Votre ordinateur devrait être un miroir, pas un placard",
    file: "./blog/ordinateur-miroir-placard",
    excerpt: "Transformez votre chaos numérique en clarté productive",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/ordinateur.webp",
    tags: ["Développement personnel", "Organisation numerique", "Productivite"],
    category: "Productivité"
  },
  {
    title: "Du petit village d'Epsom à votre salle de bain : l'histoire fascinante d'un rituel de détente ancestral",
    file: "./blog/Epsom",
    excerpt: "Découvrez l'histoire fascinante du sel d'Epsom et ses bienfaits méconnus pour votre bien-être quotidien.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Epsom.webp",
    tags: ["Santé", "Histoire", "Bien-être"],
    category: "Sagesses & Inspiration"
  },
  {
    title: "Épuisé à 15 h ? La sagesse millénaire des dauphins pour vaincre la fatigue mentale",
    file: "./blog/dauphins",
    excerpt: "Et si vous adoptiez la technique de sommeil des dauphins pour optimiser votre énergie tout au long de la journée ?",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/dauphin.webp",
    tags: ["Productivité", "Sommeil", "Santé"],
    category: "Productivité"
  },
  {
    title: "Le médecin qui a tout quitté pour écouter les fleurs 🌸",
    file: "./blog/Bach",
    excerpt: "L'histoire inspirante du Dr Edward Bach et la naissance de la thérapie florale qui révolutionna la médecine alternative.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/3-2.png",
    tags: ["Nature", "Innovation"],
    category: "Sagesses & Inspiration"
  },
  {
    title: "Maîtrisez colère, tristesse et injustice : guide inspiré de Lao Tseu et Bouddha ✨",
    file: "./blog/Laotseu",
    excerpt: "Comment vos blessures d'hier contiennent les graines de votre puissance de demain 🌱",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/trois-sagesses.webp",
    tags: ["Développement personnel", "Transformation", "Résilience"],
    category: "Développement personnel"
  },
  {
    title: "L'eau pure, source vitale d'hydratation et de santé optimale 💧",
    file: "./blog/eau",
    excerpt: "Pourquoi l'hydratation naturelle est essentielle à votre bien-être",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/eau.webp",
    tags: ["Santé", "Nutrition créole", "Hydratation"],
    category: "Nutrition créole"
  },
  {
    title: "La NST Bowen : une solution révolutionnaire pour les manutentionnaires face aux TMS 💪",
    file: "./blog/Bowen-TMS",
    excerpt: "Le quotidien douloureux des manutentionnaires : comprendre pour mieux agir",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Bowen.webp",
    tags: ["Santé", "NST Bowen"],
    category: "Bien-être holistique"
  },
  {
    title: "🧠 Comment les 'pourquoi' restreignent les capacités de votre cerveau",
    file: "./blog/comment-pourquoi",
    excerpt: "L'impact neurologique des questions que nous nous posons",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/cerveau.png",
    tags: ["Développement personnel", "Transformation", "Neurosciences"],
    category: "Développement personnel"
  },
  {
    title: "La NST Bowen : Une solution naturelle contre les douleurs du quotidien",
    file: "./blog/Bowen",
    excerpt: "Qu'est-ce que la NST Bowen ?",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Bowen.webp",
    tags: ["Santé", "NST Bowen"],
    category: "Bien-être holistique"
  },
  {
    title: "L'Intuition : Votre précieux allié pour une vie épanouie",
    file: "./blog/intuition",
    excerpt: "L'Intelligence du subconscient : Un trésor à redécouvrir",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/intuition.png",
    tags: ["Développement personnel"],
    category: "Développement personnel"
  },
  {
    title: "L'Alliance du Tai Ji Chuan et du Qi Gong",
    file: "./blog/qi-gong-tai-chi",
    excerpt: "Une synergie de mouvement et d'énergie pour une santé optimale",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/yin-yang-tai-ji.webp",
    tags: ["Tai Ji Chuan", "Qi Gong", "Santé"],
    category: "Bien-être holistique"
  },
  {
    title: "De l'ombre à la lumière : L'ascension d'un homme hors du commun",
    file: "./blog/ombre-lumiere",
    excerpt: "Du plus bas rang social à la présidence",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/ombre-lumiere.png",
    tags: ["Développement personnel"],
    category: "Sagesses & Inspiration"
  },
  {
    title: "Le code des graines germées",
    file: "./blog/grainesgermees",
    excerpt: "7 céréales anciennes pour libérer votre potentiel vital",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/grainesgermees.png",
    tags: ["Santé", "Nutrition créole"],
    category: "Nutrition créole"
  },
  {
    title: "🌱 Les super-aliments créoles",
    file: "./blog/superaliments",
    excerpt: "Votre arsenal nutritionnel pour une vitalité optimale",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/super-aliments.webp",
    tags: ["Santé", "Nutrition créole"],
    category: "Nutrition créole"
  },
  {
    title: "Découvrez les bienfaits du Touch for Health®",
    file: "./blog/TFH",
    excerpt: "Votre chemin vers l'équilibrage énergétique et le bien-être",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/TFH.png",
    tags: ["Santé", "Nutrition créole"],
    category: "Bien-être holistique"
  },
  {
    title: "Léonard de Vinci",
    file: "./blog/leonard-de-vinci",
    excerpt: "Comment la curiosité stimule l'innovation",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/leonard-de-vinci.mp4",
    tags: ["Histoire", "Développement personnel"],
    category: "Sagesses & Inspiration"
  },
  {
    title: "Trouvez la sérénité en méditant avec les arbres",
    file: "./blog/arbres",
    excerpt: "Le secret ancestral de leur pouvoir apaisant",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/meditation-arbres.png",
    tags: ["Techniques", "Énergie"],
    category: "Bien-être holistique"
  },
  {
    title: "L'Alimentation saine et le sport",
    file: "./blog/alimentation-sport",
    excerpt: "Le duo dynamique pour une santé de fer",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/alimentation-sport.mp4",
    tags: ["Santé", "Nutrition créole", "Hydratation"],
    category: "Nutrition créole"
  },
  {
    title: "Explorez votre génie intérieur",
    file: "./blog/zenbox",
    excerpt: "La suite de l'aventure",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/zenbox.mp4",
    tags: ["Développement personnel"],
    category: "Développement personnel"
  },
  {
    title: "Révolution éducative au Japon",
    file: "./blog/revolution-cantine-japon",
    excerpt: "Comment une simple cantine a transformé toute une école 🍚🧠",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/revolution-cantine-japon.webp",
    tags: ["Santé", "Nutrition créole", "Alimentation"],
    category: "Nutrition créole"
  },
  {
    title: "Résilience : 3 Forces cachées pour transformer votre passé douloureux selon la sagesse ancienne",
    file: "./blog/resilience",
    excerpt: "Transformer votre passé en potentiel infini",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/resilience.webp",
    tags: ["Développement personnel", "Transformation", "Résilience"],
    category: "Développement personnel"
  },
  {
    title: "Passé et avenir : Comment vos héritages façonnent votre bien-être",
    file: "./blog/passe-avenir",
    excerpt: "Une sagesse inspirée de la nature",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/passe-avenir.webp",
    tags: ["Développement personnel", "Transformation", "Résilience"],
    category: "Bien-être holistique"
  },

  {
    title: "L'Approche Synaptika: comment votre corps sait déjà retrouver son équilibre",
    file: "./blog/approche-synaptika",
    excerpt: "Découvrez l'Approche Synaptika, une méthode unique en Martinique centrée sur la NST Bowen pour retrouver votre équilibre naturel.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "6 min",
    image: "./blog/images/approche-synaptika.jpg",
    tags: ["NST Bowen Martinique", "développement personnel", "bien-être Martinique", "système nerveux", "équilibre naturel", "Synaptika"],
    category: "Développement personnel"
  },
  {
    title: "Comment se déroule une séance de NST Bowen en Martinique: le guide complet",
    file: "./blog/deroulement-seance-nst",
    excerpt: "Le guide complet pour votre première séance de NST Bowen en Martinique: déroulement, préparation, sensations et conseils pratiques.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "4 min",
    image: "./blog/images/deroulement-seance-nst.jpg",
    tags: ["NST Bowen séance", "première séance Martinique", "déroulement NST", "préparation séance bien-être", "contre-indications NST"],
    category: "Bien-être holistique"
  },
  {
    title: "NST Bowen et gestion du stress: comment votre corps peut retrouver son calme naturellement",
    file: "./blog/nst-gestion-stress",
    excerpt: "Comment la NST Bowen aide votre système nerveux à retrouver son calme naturellement. Mécanismes, bienfaits et conseils pratiques.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "5 min",
    image: "./blog/images/nst-gestion-stress.jpg",
    tags: ["NST Bowen stress", "gestion du stress Martinique", "système nerveux", "détente naturelle 972", "stress chronique"],
    category: "Bien-être holistique"
  },
  {
    title: "Les sensations après une séance de NST Bowen: ce qu'il faut savoir",
    file: "./blog/sensations-apres-seance",
    excerpt: "Découvrez ce qu'il est normal de ressentir après une séance de NST Bowen et comment accompagner votre corps dans le processus d'intégration.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "4 min",
    image: "./blog/images/sensations-apres-seance.jpg",
    tags: ["après séance NST", "sensations NST Bowen", "intégration corps", "réactions post-séance", "récupération bien-être"],
    category: "Bien-être holistique"
  },
  {
    title: "Combien de séances de NST Bowen sont nécessaires? Le guide complet",
    file: "./blog/combien-seances-nst",
    excerpt: "Découvrez combien de séances de NST Bowen sont réellement nécessaires selon votre situation. Parcours typique et conseils pratiques.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "5 min",
    image: "./blog/images/combien-seances-nst.jpg",
    tags: ["nombre séances NST Bowen", "fréquence séances Martinique", "parcours NST", "durée accompagnement bien-être", "suivi NST"],
    category: "Bien-être holistique"
  },
  {
    title: "NST Bowen et sommeil: comment retrouver des nuits réparatrices naturellement",
    file: "./blog/nst-sommeil",
    excerpt: "Découvrez comment la NST Bowen aide à retrouver un sommeil réparateur en Martinique. Solutions naturelles contre l'insomnie.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "5 min",
    image: "./blog/images/nst-sommeil.jpg",
    tags: ["NST Bowen sommeil", "insomnie Martinique", "troubles du sommeil 972", "sommeil réparateur naturel", "mieux dormir sans médicaments"],
    category: "Bien-être holistique"
  },
  {
    title: "Le mensonge du Lâcher Prise: pourquoi votre cerveau refuse de vous détendre",
    file: "./blog/lacher-prise",
    excerpt: "Vous n'arrivez pas à lâcher prise? Votre cerveau a besoin de signaux PHYSIQUES, pas mentaux. Découvrez le protocole somatique en 2 minutes.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "5 min",
    image: "./blog/images/lacher-prise.svg",
    tags: ["lâcher prise", "stress chronique", "système nerveux autonome", "approche somatique", "gestion du stress"],
    category: "Développement personnel"
  },
  {
    title: "Pourquoi les hiboux ne burnoutent jamais: la loi circadienne",
    file: "./blog/rythmes-circadiens-hiboux",
    excerpt: "Vous forcez à 22h et êtes épuisé à 10h? Découvrez la loi circadienne que les entrepreneurs ignorent et le Rythme du Hibou.",
    date: "2026-07-12",
    author: "Thierry Felicia",
    reads: "5 min",
    image: "./blog/images/rythmes-circadiens-hiboux.svg",
    tags: ["rythme circadien", "productivité", "burn-out", "chronobiologie", "énergie"],
    category: "Productivité"
  }
];

console.log("posts.js chargé avec succès !", posts.length, "articles");

if (typeof module !== 'undefined' && module.exports) {
  module.exports = posts;
}
