#!/bin/bash
echo "🔍 Starting local quality checks for synaptika.net..."
echo "📁 Dossier scanné : $(pwd)"
echo "================================================"

ERRORS=0

# 1. Vérification des liens avec lychee (mode simple)
echo -e "\n📌 Checking links..."
if command -v lychee &> /dev/null; then
    # Lancer lychee et capturer la sortie
    OUTPUT=$(lychee --no-progress \
        --accept '200,204,301,302,403,404,429' \
        --exclude-path 'google' \
        --exclude 'at://.*' \
        --exclude 'accounts.google.com' \
        --exclude 'bsky.app' \
        --exclude 'pinterest.com' \
        './**/*.html' 2>&1)
    
    # Filtrer uniquement les vrais fichiers manquants
    MISSING=$(echo "$OUTPUT" | grep -E 'File not found' | grep -v 'Cannot resolve root-relative')
    
    if [ -n "$MISSING" ]; then
        echo "$MISSING"
        ERRORS=$((ERRORS + 1))
        echo -e "\n❌ Some files are missing"
    else
        echo -e "✅ All files are valid"
    fi
else
    echo "⚠️  lychee non installé."
fi

# 2. Vérification HTML
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

# 3. Résumé
echo -e "\n================================================"
if [ $ERRORS -eq 0 ]; then
    echo "✅ All checks passed! Ready to commit."
    exit 0
else
    echo "❌ Found $ERRORS critical error(s)."
    exit 1
fi
