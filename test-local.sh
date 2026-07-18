#!/bin/bash
echo "🔍 Starting local quality checks..."
echo "📁 Dossier scanné : $(pwd)"
echo "================================================"

ERRORS=0

# Vérification HTML uniquement (rapide)
echo -e "\n🔧 Checking HTML structure..."
while IFS= read -r -d '' file; do
    if [[ "$file" == *"google"* ]] || [[ "$file" == *"pageconstruction"* ]]; then
        continue
    fi
    
    if ! grep -q "<title>" "$file"; then
        echo "❌ Missing <title> in: $file"
        ERRORS=$((ERRORS + 1))
    fi
    if ! grep -q "<meta.*description" "$file"; then
        echo "⚠️  Missing meta description in: $file"
    fi
done < <(find . -maxdepth 3 -name "*.html" -type f -print0)

# Résumé
echo -e "\n================================================"
if [ $ERRORS -eq 0 ]; then
    echo "✅ All checks passed! Ready to commit."
    exit 0
else
    echo "❌ Found $ERRORS critical error(s)."
    exit 1
fi
