#!/usr/bin/env py python

from services.readme_updater import get_daily_activity
from services.follower_updater import get_recent_followers_activity

def main():
    print("Fetching daily activity from WakaTime...")
    get_daily_activity()
    print("Fetching recent followers from GitHub...")
    get_recent_followers_activity()
    print("Done!")

if __name__ == "__main__":
    main()
