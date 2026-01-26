# Quick Start Guide

## Option 1: Automated Deployment (Recommended)

This uses GitHub Actions to automatically build and deploy your WASM app whenever you push changes.

### Steps:

1. **Create a new repository on GitHub**
   - Go to github.com and create a new repository
   - Don't initialize with README (we already have one)

2. **Push your code**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   git push -u origin main
   ```

3. **Configure GitHub Pages**
   - Go to repository **Settings** → **Pages**
   - Under "Build and deployment":
     - Source: **GitHub Actions**
   - The workflow will automatically run and deploy your app

4. **Access your app**
   - Your app will be live at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`
   - Check the **Actions** tab to see deployment status

## Option 2: Manual Deployment

If you prefer manual control:

1. **Export locally**
   ```bash
   ./deploy.sh
   # Or manually: marimo export html-wasm STRKmodel_interactive.py -o index.html
   ```

2. **Push to GitHub**
   ```bash
   git add index.html
   git commit -m "Add WASM export"
   git push
   ```

3. **Configure GitHub Pages**
   - Go to **Settings** → **Pages**
   - Source: **Deploy from a branch**
   - Branch: **main**, Folder: **/ (root)**

## Testing Locally

Before deploying, test your app locally:

```bash
# Option 1: Run with Marimo
marimo edit STRKmodel_interactive.py

# Option 2: Test the WASM version
# Export to HTML, then open index.html in your browser
marimo export html-wasm STRKmodel_interactive.py -o index.html
```

## Troubleshooting

### GitHub Actions fails
- Check the Actions tab for error messages
- Ensure the workflow file is in `.github/workflows/deploy.yml`
- Verify Python dependencies are listed correctly

### Page shows 404
- Wait a few minutes after deployment
- Check that GitHub Pages is enabled in Settings
- Verify the correct branch and folder are selected

### WASM app doesn't load
- Check browser console for errors
- Ensure you're using a modern browser (Chrome, Firefox, Safari, Edge)
- Try clearing browser cache

## Making Changes

1. Edit `STRKmodel_interactive.py`
2. Test locally with `marimo edit STRKmodel_interactive.py`
3. Commit and push your changes
4. GitHub Actions will automatically rebuild and deploy

That's it! 🎉
