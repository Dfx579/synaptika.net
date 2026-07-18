#!/bin/bash
echo "🔄 Mise à jour des catégories..."

# 1. Renommer "Nutrition" → "Nutrition créole"
find . -name "*.html" -type f -exec sed -i 's/"Nutrition"/"Nutrition créole"/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/🥗 Nutrition/🥗 Nutrition créole/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/#NutritionMartinique/#NutritionCréole/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/#Nutrition</#NutritionCréole</g' {} \;
find . -name "*.html" -type f -exec sed -i 's/NutritionScolaire/NutritionCréoleScolaire/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/RévolutionNutritionnelle/RévolutionNutritionCréole/g' {} \;

# 2. Fusionner "Santé & Bien-être" → "Bien-être holistique"
find . -name "*.html" -type f -exec sed -i 's/"Santé & Bien-être"/"Bien-être holistique"/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/💚 Santé & Bien-être/🧘 Bien-être holistique/g' {} \;

# 3. Fusionner "Thérapies corporelles" → "Bien-être holistique"
find . -name "*.html" -type f -exec sed -i 's/"Thérapies corporelles"/"Bien-être holistique"/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/🤲 Thérapies corporelles/🧘 Bien-être holistique/g' {} \;

# 4. Fusionner "Techniques énergétiques" → "Bien-être holistique"
find . -name "*.html" -type f -exec sed -i 's/"Techniques énergétiques"/"Bien-être holistique"/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/☯️ Techniques énergétiques/🧘 Bien-être holistique/g' {} \;

# 5. Renommer "Histoire & Inspiration" → "Sagesses & Inspiration"
find . -name "*.html" -type f -exec sed -i 's/"Histoire & Inspiration"/"Sagesses \& Inspiration"/g' {} \;
find . -name "*.html" -type f -exec sed -i 's/🏛 Histoire & Inspiration/📖 Sagesses \& Inspiration/g' {} \;

echo "✅ Catégories mises à jour !"
