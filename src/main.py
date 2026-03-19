#!/usr/bin/env python

from services.readme_updater import get_daily_activity
from services.follower_updater import get_recent_followers_activity
from services.blog_updater import get_recent_blog_posts

def main():
    print("Fetching daily activity from WakaTime...")
    get_daily_activity()
    print("Fetching recent followers from GitHub...")
    get_recent_followers_activity()
    print("Fetching recent blog posts from pphat.me...")
    get_recent_blog_posts()
    print("Done!")

if __name__ == "__main__":
    main()
