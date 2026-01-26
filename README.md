# STRK Model Interactive - WASM Deployment

This repository contains a Marimo notebook for analyzing STRK price models, deployed as a WASM application on GitHub Pages.

## Live Demo

Once deployed, your app will be available at: `https://[your-username].github.io/[repo-name]/`

## Local Development

### Prerequisites
- Python 3.10+
- Marimo installed (`pip install marimo`)

### Run Locally
```bash
marimo edit STRKmodel_interactive.py
```

## Deployment Instructions

### Step 1: Export to WASM
From your local machine where you have marimo installed, run:

```bash
marimo export html-wasm STRKmodel_interactive.py -o index.html
```

This will generate an `index.html` file that runs entirely in the browser using WebAssembly.

### Step 2: Push to GitHub

1. Create a new repository on GitHub
2. Initialize and push your code:

```bash
git init
git add .
git commit -m "Initial commit: STRK Model WASM app"
git branch -M main
git remote add origin https://github.com/[your-username]/[repo-name].git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under "Source", select **Deploy from a branch**
4. Select branch: **main** and folder: **/ (root)**
5. Click **Save**

Your app will be live in a few minutes at: `https://[your-username].github.io/[repo-name]/`

## Model Description

The STRK price model calculates fair value based on two components:

1. **Straight Value**: $8 / (10Y UST + 0.0423 risk premium)
   - Higher yields → Lower STRK price
   - Represents bond-like valuation floor

2. **Conversion Value**: MSTR Price / 10
   - Higher MSTR → Higher STRK price
   - Represents equity upside potential

**Final STRK Price = Maximum of the two values**

## Credits

Model source: [BuffaloDyl](https://buffalodyl.com/STRK.html)

## License

MIT
