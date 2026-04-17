import json
from datetime import datetime, timedelta

from config import BAR_STYLE, DATA_PATH, README_PATH
from utils.formatting import BAR_STYLES, generate_progress_bar
from api.wakatime import WakaTimeAPI


START_TAG = "<!--START_SECTION:daily-->"
END_TAG = "<!--END_SECTION:daily-->"
CODING_STATS_PATH = DATA_PATH / "coding_stats.json"


def _build_daily_section(languages, style="block"):
    if style not in BAR_STYLES:
        raise ValueError(f"Unknown BAR_STYLE '{style}'. Choose from: {', '.join(BAR_STYLES)}")
    lines = ["```diff"]
    for item in languages:
        progress_bar = generate_progress_bar(item["percent"], style=style)
        lines.append(f"{progress_bar} ⁝ {item['percent']}% • {item['name']}")
    lines.append("```")
    return "\n".join(lines)


def get_daily_activity():
    wakatimes = WakaTimeAPI()
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    stats = wakatimes.daily_activity(date=yesterday)
    daily_entries = stats.get("data", [])
    languages = daily_entries[0].get("languages", []) if daily_entries else []

    if not languages:
        print(f"No language activity found for {yesterday}. Falling back to cached stats.")
        if CODING_STATS_PATH.exists():
            cached = json.loads(CODING_STATS_PATH.read_text(encoding="utf-8"))
            cached_entries = cached.get("data", [])
            languages = cached_entries[0].get("languages", []) if cached_entries else []

        if not languages:
            print("No cached activity available. Skipping daily section update.")
            return None

    DATA_PATH.mkdir(parents=True, exist_ok=True)
    CODING_STATS_PATH.write_text(
        json.dumps(stats, indent=4),
        encoding="utf-8",
    )

    content = README_PATH.read_text(encoding="utf-8")
    start_index = content.find(START_TAG)
    end_index = content.find(END_TAG)

    if start_index == -1 or end_index == -1:
        raise ValueError("Could not find daily section markers in README.md")

    end_index += len(END_TAG)
    new_section = f"{START_TAG}\n{_build_daily_section(languages, style=BAR_STYLE)}\n{END_TAG}"
    updated_content = content[:start_index] + new_section + content[end_index:]
    README_PATH.write_text(updated_content, encoding="utf-8")

    return stats