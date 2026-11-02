#!/usr/bin/env python
import sys
from pathlib import Path

# Ensure 'src' is in sys.path so sibling packages (services, config, api, utils) resolve
src_dir = str(Path(__file__).resolve().parent)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from services.readme_updater import get_daily_activity
from services.follower_updater import get_recent_followers_activity
from services.blog_updater import get_recent_blog_posts
from services.cover_updater import update_cover_images

def main():
    print("Fetching daily activity from WakaTime...")
    result = get_daily_activity()
    if result is None:
        print("Daily activity update skipped.")
    print("Fetching recent followers from GitHub...")
    get_recent_followers_activity()
    print("Fetching recent blog posts from pphat.me...")
    get_recent_blog_posts()
    print("Downloading cover images...")
    update_cover_images()
    print("Done!")

if __name__ == "__main__":
    main()
