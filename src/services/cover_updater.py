import os
import requests
from config import BASE_DIR

def update_cover_images():
    assets_dir = BASE_DIR / "assets"
    assets_dir.mkdir(exist_ok=True)

    images = {
        "stats.svg": "https://stats.pphat.top/stats?username=pphatdev&size=large&avatar_mode=radar&data_border_style=frame",
        "graph.svg": "https://stats.pphat.top/graph?username=pphatdev&show_background=true&animate=pulse&size=small&show_title=false&show_total_contribution=false",
        "languages.svg": "https://stats.pphat.top/languages?username=pphatdev&type=pie&show_info=true&theme=default"
    }

    for filename, url in images.items():
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            file_path = assets_dir / filename
            file_path.write_bytes(response.content)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
