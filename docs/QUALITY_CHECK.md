# KrishiBloom AI — Final QA Notes

## Automated checks completed

- `python tests/check_structure.py` passed
- `node --check app.js` passed
- The ZIP passed `unzip -t`
- Browser interactions tested with Chromium using an inline, self-contained `demo.html` build and temporary localStorage shim (required by the restricted test browser's `about:blank` origin)
- 29 interaction checks passed: Welcome, Login, Sign Up, Home, Shop, search, categories, wishlist, bag, drawer, Deals, Scanner, photo preview, Crop Guide, filter, Model Insights, About, Contact, feedback download, mobile menu, and no browser JS errors
- Responsive desktop and mobile screenshots generated; mobile horizontal overflow checked at 390px

## Limitations

- Not published to GitHub Pages from this session. Public live link is not verified.
- Product catalogue and prices are illustrative data, not real merchandise or inventory.
- Login/sign-up is a local UI flow, not a secure identity system. No passwords are stored or authenticated.
- Google/Facebook OAuth intentionally disabled. No payment, delivery or backend message sending.
- Scanner supports image upload/preview, **not disease detection**. No trained AI model, validation metrics or Grad-CAM is bundled.
- RiceLeafDisease-BD5 v2 class distribution is from published dataset metadata; raw image archive not independently audited.

## Next stage for genuine crop AI

Only after access to the primary dataset archive: image integrity, leakage audit, group split, trained-model evaluation, exported runtime, numeric parity and end-device profiling.
