import os
import json

base_path = "PHOTO-SITE-ASTRO"
galeries = {
    "aurore": [],
    "CIEL PROFOND": [],
    "gab": [],
    "LUNE": [],
    "PLANETES": [],
    "SOLEIL": [],
}

for galerie in galeries:
    folder = os.path.join(base_path, galerie)
    if os.path.exists(folder):
        for file in sorted(os.listdir(folder)):
            if file.lower().endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = os.path.join(base_path, galerie, file).replace("\\", "/")
                galeries[galerie].append({
                    "src": image_path,
                    "title": ""
                })

with open("galerie.json", "w", encoding="utf-8") as f:
    json.dump(galeries, f, indent=4, ensure_ascii=False)

print("✅ galerie.json mis à jour !")
