# 🌿 KrishiBloom AI — Complete Pages Portfolio Website

A luxury-nature agriculture website with separate navigable pages and functioning **demo** shopping interactions.

## Pages

- Welcome → Login → Sign Up (demo session only)
- Home
- Shop with search, category filter, sorting, quick view, wishlist and basket
- Fresh Deals with illustrative sale poster and products
- AI Scanner with image upload and preview; **NO trained prediction model**
- Crop Guide (5 published rice-leaf dataset class names with general educational text)
- Model Insights with published dataset metadata and clear unfinished-model status
- About & Social Responsibility
- Contact/FAQ with a local text-file feedback export (nothing transmitted)

## Run

Open `demo.html` directly in a browser; it bundles all CSS, JavaScript, product data and local images. Or deploy all repository files to GitHub Pages (the primary application is `index.html`). A local development server also works: `python -m http.server 8000`.

## GitHub Pages

1. Create a public repository named `KrishiBloom-AI`.
2. Extract the ZIP and upload its **contents** to the repository root.
3. Go to **Settings → Pages → Deploy from a branch → main → /(root)**.
4. Save. The typical URL is `https://USERNAME.github.io/KrishiBloom-AI/`. This project has not been published to your GitHub account by the assistant.

## Transparency

- **Prices are illustrative sample data**, not real retailer prices. Cart/wishlist persist in localStorage; no order/payment system.
- Login and signup are **demo flows**: passwords are never stored, authenticated or sent. Do not use a real password.
- Google/Facebook login is intentionally disabled.
- The AI Scanner is upload/preview only: **no crop-disease model, prediction, confidence or Grad-CAM** is claimed.
- Dataset metadata on the Model Insights page is attributed to the published RiceLeafDisease-BD5 v2 dataset, [Mendeley Data](https://data.mendeley.com/datasets/sjkptpgv79/2), DOI [10.17632/sjkptpgv79.2](https://doi.org/10.17632/sjkptpgv79.2), labelled CC BY 4.0. Raw image archive has not been independently audited.
- Font styles load from Google Fonts when online, with built-in system fallbacks offline.

## Technologies

HTML5, CSS3, vanilla JavaScript, JSON, responsive layouts, GitHub Pages. No build tool, API key, paid server or npm install is needed.

## Assets

Local photos and illustrations in `assets/`; no third-party product photos are hotlinked. The greeting farmer image was sourced from the user's earlier project asset. All product visuals are emoji artwork.

## Improvement path

Train and validate a leakage-aware rice-leaf model, export a browser-compatible inference model, run browser parity and mobile benchmarks, and only then enable actual diagnostic predictions.
