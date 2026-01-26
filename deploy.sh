#!/bin/bash

# STRK Model WASM Deployment Script
# This script exports the Marimo notebook to a WASM HTML file

echo "🚀 Exporting Marimo notebook to WASM..."

# Check if marimo is installed
if ! command -v marimo &> /dev/null; then
    echo "❌ Error: marimo is not installed"
    echo "Install it with: pip install marimo"
    exit 1
fi

# Export to WASM HTML
marimo export html-wasm STRKmodel_interactive.py -o index.html

if [ $? -eq 0 ]; then
    echo "✅ Successfully exported to index.html"
    echo ""
    echo "Next steps:"
    echo "1. Test locally by opening index.html in your browser"
    echo "2. Commit and push to GitHub:"
    echo "   git add index.html"
    echo "   git commit -m 'Export WASM app'"
    echo "   git push"
    echo "3. Enable GitHub Pages in repository settings"
else
    echo "❌ Export failed"
    exit 1
fi
