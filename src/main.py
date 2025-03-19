#!/usr/bin/env py
# -*- coding: utf-8 -*-

import os
import json
import re
from waka_api import WakaTimeAPI
from config import DATA_PATH

wakatimes = WakaTimeAPI()


def generate_progress_bar(percent):
    """Generate a progress bar using emojis based on percentage
    🟩: 10%, 🟨: 5%, ⬜: remaining
    """
    total_blocks = 25
    green_blocks = int((percent / 100) * total_blocks)
    yellow_blocks = 1 if percent > 0 and green_blocks < total_blocks else 0
    white_blocks = total_blocks - green_blocks - yellow_blocks

    progress = "🟩" * green_blocks + "🟨" * yellow_blocks + "⬜" * white_blocks
    return progress


def main():
    try:
        usr_stats = wakatimes.daily_activity()
        data = usr_stats['data']

        # Export Data to JSON file
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        # Generate new content
        new_content = "```diff\n"
        for item in data[0]['languages']:
            progress_bar = generate_progress_bar(item['percent'])
            new_content += f"{progress_bar} ⁝ {item['name']} -----• {item['percent']}%\n"
        new_content += "```\n"

        # Read existing README content
        readme_path = "README.md"
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace content between tags
        start_tag = "<!--START_SECTION:waka-->"
        end_tag = "<!--END_SECTION:waka-->"
        pattern = f"{start_tag}.*?{end_tag}"
        new_content = f"{start_tag}\n{new_content}{end_tag}"

        updated_content = re.sub(pattern, new_content, content, flags=re.DOTALL)
        print(f"--------------{pattern}{new_content}{updated_content}")

        # Write back to README
        # with open(readme_path, 'w', encoding='utf-8') as f:
        #     f.write(updated_content)

    except Exception as e:
        print(f"Fatal error: {e}")


if __name__ == "__main__":
    main()
