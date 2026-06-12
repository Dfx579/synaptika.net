// Liste des articles du blog Synaptika
const posts = [
  {
    title: "Du petit village d'Epsom à votre salle de bain : l'histoire fascinante d'un rituel de détente ancestral",
    file: "./blog/Epsom",
    excerpt: "Découvrez l'histoire fascinante du sel d'Epsom et ses bienfaits méconnus pour votre bien-être quotidien.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Epsom.png",
    tags: ["Santé", "Histoire", "Bien-être"]
  },
  {
    title: "Épuisé à 15 h ? La sagesse millénaire des dauphins pour vaincre la fatigue mentale",
    file: "./blog/dauphins",
    excerpt: "Et si vous adoptiez la technique de sommeil des dauphins pour optimiser votre énergie tout au long de la journée ?",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/dauphin.png",
    tags: ["Productivité", "Sommeil", "Santé"]
  },
  {
    title: "Le médecin qui a tout quitté pour écouter les fleurs 🌸",
    file: "./blog/Bach",
    excerpt: "L'histoire inspirante du Dr Edward Bach et la naissance de la thérapie florale qui révolutionna la médecine alternative.",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/3-2.png",
    tags: ["Nature", "Innovation"]
  },
  {
    title: "Maîtrisez colère, tristesse et injustice : guide inspiré de Lao Tseu et Bouddha ✨",
    file: "./blog/Laotseu",
    excerpt: "Comment vos blessures d'hier contiennent les graines de votre puissance de demain 🌱",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/trois-sagesses.png",
    tags: ["Développement personnel", "Transformation", "Résilience"]
  },
  {
    title: "L'eau pure, source vitale d'hydratation et de santé optimale 💧",
    file: "./blog/eau",
    excerpt: "Pourquoi l'hydratation naturelle est essentielle à votre bien-être",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/eau.png",
    tags: ["Santé", "Nutrition", "Hydratation"]
  },
  {
    title: "La NST Bowen : une solution révolutionnaire pour les manutentionnaires face aux TMS 💪",
    file: "./blog/Bowen-TMS",
    excerpt: "Le quotidien douloureux des manutentionnaires : comprendre pour mieux agir",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Bowen.png",
    tags: ["Santé", "NST Bowen"]
  },
  {
    title: "🧠 Comment les 'pourquoi' restreignent les capacités de votre cerveau",
    file: "./blog/comment-pourquoi",
    excerpt: "L'impact neurologique des questions que nous nous posons",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/cerveau.png",
    tags: ["Développement personnel", "Transformation", "Neurosciences"]
  },
  {
    title: "La NST Bowen : Une solution naturelle contre les douleurs du quotidien",
    file: "./blog/Bowen",
    excerpt: "Qu'est-ce que la NST Bowen ?",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/Bowen.png",
    tags: ["Santé", "NST Bowen"]
  },
  {
    title: "L'Intuition : Votre précieux allié pour une vie épanouie",
    file: "./blog/intuition",
    excerpt: "L'Intelligence du subconscient : Un trésor à redécouvrir",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/intuition.png",
    tags: ["Développement personnel"]
  },
  {
    title: "De l’ombre à la lumière : L’ascension d’un homme hors du commun",
    file: "./blog/ombre-lumiere",
    excerpt: "Du plus bas rang social à la présidence",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/ombre-lumiere.png",
    tags: ["Développement personnel"]
  },
  {
    title: "Le code des graines germées",
    file: "./blog/grainesgermees",
    excerpt: "7 céréales anciennes pour libérer votre potentiel vital",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/grainesgermees.png",
    tags: ["Santé", "Nutrition"]
  },
  {
    title: "🌱 Les super-aliments créoles",
    file: "./blog/superaliments",
    excerpt: "Votre arsenal nutritionnel pour une vitalité optimale",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/super-aliments.png",
    tags: ["Santé", "Nutrition"]
  },
  {
    title: "Découvrez les bienfaits du Touch for Health®",
    file: "./blog/TFH",
    excerpt: "Votre chemin vers l'équilibrage énergétique et le bien-être",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/TFH.png",
    tags: ["Santé", "Nutrition"]
  },
  {
    title: "Léonard de Vinci",
    file: "./blog/leonard-de-vinci",
    excerpt: "Comment la curiosité stimule l’innovation",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/leonard-de-vinci.gif",
    tags: ["Histoire", "Développement personnel"]
  },
  {
    title: "Trouvez la sérénité en méditant avec les arbres",
    file: "./blog/arbres",
    excerpt: "Le secret ancestral de leur pouvoir apaisant",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/meditation-arbres.png",
    tags: ["Techniques", "Énergie"]
  },
  {
    title: "L'Alimentation saine et le sport",
    file: "./blog/alimentation-sport",
    excerpt: "Le duo dynamique pour une santé de fer",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/alimentation-sport.gif",
    tags: ["Santé", "Nutrition", "Hydratation"]
  },
  {
    title: "Explorez votre génie intérieur",
    file: "./blog/zenbox",
    excerpt: "La suite de l'aventure",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/zenbox.gif",
    tags: ["Développement personnel"]
  },
  {
    title: "Révolution éducative au Japon",
    file: "./blog/revolution-cantine-japon",
    excerpt: "Comment une simple cantine a transformé toute une école 🍚🧠",
    date: "",
    author: "",
    reads: "",
    image: "./blog/image/revolution-cantine-japon.png",
    tags: ["Santé", "Nutrition", "Alimentation"]
  }
,{
    title: "Igname, Manioc, Patate Douce : Ce que Votre Grand-Mère Savait Déjà",
    file: "./blog/igname-manioc-patate-douce",
    excerpt: "Votre grand-mère n'avait pas de diplôme en nutrition. Elle avait un jardin.",
    date: "2026-06-11",
    author: "Thierry FELICIA",
    reads: "8 min",
    image: "./blog/images/igname-manioc-patate-douce.jpg",
    tags: ["Nutrition", "Bien-être", "CuisineAntillaise", "AntiStress"]
  }
];

console.log("posts.js chargé avec succès !", posts.length, "articles");
