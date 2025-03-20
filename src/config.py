import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = os.getenv("GITHUB_API_URL", "https://api.github.com")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
STATUS_UPDATE_INTERVAL = int(os.getenv("STATUS_UPDATE_INTERVAL", 60))

WAKA_API= os.getenv("WAKA_API")
WAKA_USERNAME = os.getenv("WAKA_USERNAME")
WAKA_TOKEN = os.getenv("WAKA_TOKEN")
WAKA_PROJECT = os.getenv("WAKA_PROJECT")
WAKA_INTERVAL = int(os.getenv("WAKA_INTERVAL", 60))

DATA_PATH=os.getenv("DATA_PATH", "data")