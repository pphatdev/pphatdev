#!/usr/bin/env py python
# -*- coding: utf-8 -*-

from config import DATA_PATH
from utils.get_daily_activity import get_daily_activity
from waka_api import WakaTimeAPI

wakatimes = WakaTimeAPI()

def main():
    get_daily_activity()


if __name__ == "__main__":
    main()