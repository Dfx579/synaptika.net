#!/bin/bash
echo "🔍 Starting local quality checks for synaptika.net..."
echo "📁 Dossier scanné : $(pwd)"
echo "================================================"

ERRORS=0

# 1. Vérification des liens avec lychee (mode pragmatique)
echo -e "
📌 Checking links..."
if command -v lychee &> /dev/null; then
    # On ignore les liens absolus et on se concentre sur les fichiers manquants
    lychee --no-progress         --accept '200,204,301,302,403,404,429'         --exclude-path 'google'         --exclude 'at://.*'         --exclude 'accounts.google.com'         --exclude 'bsky.app'         --exclude 'pinterest.com'         --exclude '^file:///[^/]+$'         --exclude '^file:///home/nyp7/[^/]+$'         './**/*.html' 2>&1 | grep -E '(File not found|ERROR.*file://)' | grep -v 'Cannot resolve root-relative'

    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        ERRORS=$((ERRORS + 1))
        echo -e "
❌ Some files are missing"
    else
        echo -e "✅ All files are valid"
    fi
else
    echo "⚠️  lychee non installé."
fi

# 2. Vérification HTML
echo -e "
🔧 Checking HTML structure..."
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
echo -e "
================================================"
if [ $ERRORS -eq 0 ]; then
    echo "✅ All checks passed! Ready to commit."
else
    echo "❌ Found $ERRORS critical error(s)."
fi
