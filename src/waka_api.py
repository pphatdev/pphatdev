import requests
from datetime import datetime, timedelta
from config import WAKA_API, WAKA_TOKEN


class WakaTimeAPI:
    def __init__(self):
        self.api_key = WAKA_TOKEN
        self.base_url = WAKA_API
        self.headers = {
            "Authorization": f"Basic {WAKA_TOKEN}"
        }

    def get_user_stats(self, range="last_7_days"):
        """
        Fetch user stats from WakaTime API
        range options: last_7_days, last_30_days, last_year
        """
        endpoint = f"{self.base_url}/users/current/stats/{range}"
        response = requests.get(endpoint, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")

    def get_user_projects(self):
        """Fetch all projects from WakaTime API"""
        endpoint = f"{self.base_url}/users/current/projects"
        response = requests.get(endpoint, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching projects: {response.status_code}")

    def get_coding_activity(self, start_date=None, end_date=None):
        """Fetch coding activity for a date range"""
        if not start_date:
            start_date = (datetime.now() - timedelta(days=7)
                          ).strftime("%Y-%m-%d")
        if not end_date:
            end_date = datetime.now().strftime("%Y-%m-%d")

        endpoint = f"{self.base_url}/users/current/summaries"
        params = {
            "start": start_date,
            "end": end_date
        }

        response = requests.get(endpoint, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Error fetching coding activity: {response.status_code}"
            )

    def daily_activity(self):

        """Fetch daily coding activity"""
        endpoint = f"{self.base_url}/users/current/summaries?start=2025-03-18&end=2025-03-19"
        response = requests.get(endpoint, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Error fetching daily coding activity: {response.status_code}"
            )