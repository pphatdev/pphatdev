from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

import requests

from config import WAKA_API, WAKA_TOKEN


class WakaTimeAPIError(Exception):
    """Raised when the WakaTime API request fails."""


class WakaTimeAPI:
    def __init__(self):
        if not WAKA_API:
            raise ValueError("Missing WAKA_API. Set it in .env or .env.example.")
        if not WAKA_TOKEN:
            raise ValueError("Missing WAKA_TOKEN. Set it in .env before running the script.")

        self.base_url = WAKA_API.rstrip("/")
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(WAKA_TOKEN, "")
        self.session.headers.update({"Accept": "application/json"})

    def _get(self, endpoint, *, params=None):
        try:
            response = self.session.get(endpoint, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            status_code = error.response.status_code if error.response else "unknown"
            if status_code == 401:
                raise WakaTimeAPIError(
                    "Authentication failed. Please check your WakaTime API token."
                ) from error
            raise WakaTimeAPIError(
                f"WakaTime API request failed with status {status_code}."
            ) from error
        except requests.exceptions.RequestException as error:
            raise WakaTimeAPIError(f"Network error occurred: {error}") from error

    def get_user_stats(self, range_name="last_7_days"):
        """
        Fetch user stats from WakaTime API
        range options: last_7_days, last_30_days, last_year
        """
        endpoint = f"{self.base_url}/users/current/stats/{range_name}"
        return self._get(endpoint)

    def get_user_projects(self):
        """Fetch all projects from WakaTime API"""
        endpoint = f"{self.base_url}/users/current/projects"
        return self._get(endpoint)

    def get_coding_activity(self, start_date=None, end_date=None):
        """Fetch coding activity for a date range"""
        if not start_date:
            start_date = (
                datetime.now() - timedelta(days=7)
            ).strftime("%Y-%m-%d")
        if not end_date:
            end_date = datetime.now().strftime("%Y-%m-%d")

        endpoint = f"{self.base_url}/users/current/summaries"
        params = {
            "start": start_date,
            "end": end_date
        }

        return self._get(endpoint, params=params)

    def daily_activity(self, date=None):
        """
        Fetch daily coding activity
        Args:
            date: Optional date string in YYYY-MM-DD format. Defaults to today.
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        params = {
            "start": date,
            "end": date
        }

        endpoint = f"{self.base_url}/users/current/summaries"
        return self._get(endpoint, params=params)
