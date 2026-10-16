import json, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
required=['index.html','app.js','style.css','demo.html','README.md','data/products.json','assets/mark.svg','assets/farmer-portrait.webp']
assert all((root/x).exists() for x in required)
html=(root/'index.html').read_text()
for page in ['home','shop','deals','scanner','guide','model','about','contact']: assert f'data-page="{page}"' in html
assert 'login-form' in html and 'signup-form' in html and 'welcome-screen' in html
assert 'no crop-disease model' in (root/'README.md').read_text().lower()
assert len(json.loads((root/'data/products.json').read_text()))>=15
print('Structure and data integrity checks passed')
