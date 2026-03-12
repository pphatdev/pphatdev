import os
import re
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
README_PATH = BASE_DIR / "README.md"

load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR / ".env.example", override=False)


def _resolve_path(value: str) -> Path:
	path = Path(value)
	if path.is_absolute():
		return path
	return BASE_DIR / path


def _sanitize_env_value(value: str) -> str:
	if value is None:
		return ""

	cleaned = value.strip()
	# Guard against malformed env lines like DATA_PATH=dataGITHUB_TOKEN=...
	cleaned = re.split(r"(?:GITHUB_TOKEN|WAKA_TOKEN)\s*=", cleaned, maxsplit=1)[0]
	return cleaned.strip()

GITHUB_API_URL = os.getenv("GITHUB_API_URL", "https://api.github.com")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
STATUS_UPDATE_INTERVAL = int(os.getenv("STATUS_UPDATE_INTERVAL", 60))

WAKA_API = os.getenv("WAKA_API")
WAKA_USERNAME = os.getenv("WAKA_USERNAME")
WAKA_TOKEN = os.getenv("WAKA_TOKEN")
WAKA_PROJECT = os.getenv("WAKA_PROJECT")
WAKA_INTERVAL = int(os.getenv("WAKA_INTERVAL", 60))

_raw_data_path = _sanitize_env_value(os.getenv("DATA_PATH", "data"))
DATA_PATH = _resolve_path(_raw_data_path or "data")

BAR_STYLE = os.getenv("BAR_STYLE", "block")
