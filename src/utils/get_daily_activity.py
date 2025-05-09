import os
from waka_api import WakaTimeAPI
from config import DATA_PATH
from utils.helpers import generate_progress_bar

wakatimes = WakaTimeAPI()

from datetime import datetime, timedelta

def get_daily_activity():
    try:
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        usr_stats = wakatimes.daily_activity(date=yesterday)
        data = usr_stats['data']

        # Export Data to JSON file
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        # Generate new content
        new_content = "```diff\n"
        for item in data[0]['languages']:
            progress_bar = generate_progress_bar(item['percent'])
            new_content += f"{progress_bar} ⁝ {item['percent']}% • {item['name']}\n"
        new_content += "```\n"

        # Read existing README content
        readme_path = "README.md"
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace content between tags
        start_tag = "<!--START_SECTION:daily-->"
        end_tag = "<!--END_SECTION:daily-->"

        # Split the content
        start_index = content.find(start_tag)
        end_index = content.find(end_tag) + len(end_tag)

        if start_index == -1 or end_index == -1:
            raise ValueError("Could not find daily section markers in README.md")

        # Construct new content
        new_section = f"{start_tag}\n{new_content}{end_tag}"

        # Replace the section
        updated_content = content[:start_index] + new_section + content[end_index:]

        # Write back to README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

    except Exception as e:
        print(f"Fatal error: {e}")