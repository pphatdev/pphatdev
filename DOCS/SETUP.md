# GitHub README Stats Project Setup

## Overview

This project updates the daily coding activity section in the root `README.md` using data from the WakaTime API.

When you run the script, it:

1. Loads environment variables from the project root.
2. Requests yesterday's coding summary from WakaTime.
3. Saves the raw API response to `data/coding_stats.json`.
4. Replaces the content between the daily section markers in `README.md`.

## Project Structure

```text
.
|-- README.md
|-- doc.md
|-- requirements.txt
|-- data/
|   `-- coding_stats.json
`-- src/
    |-- config.py
    |-- main.py
    |-- waka_api.py
    `-- utils/
        |-- get_daily_activity.py
        `-- helpers.py
```

## Requirements

- Python 3.10 or newer is recommended.
- A WakaTime account and API token.
- A `README.md` file that contains these markers:

```md
<!--START_SECTION:daily-->
<!--END_SECTION:daily-->
```

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Configuration

Copy `.env.example` to `.env` and adjust the values for your account.

```powershell
Copy-Item .env.example .env
```

Current environment variables:

```env
GITHUB_API_URL=https://api.github.com
GITHUB_USERNAME=
GITHUB_REPO=
GITHUB_TOKEN=
STATUS_UPDATE_INTERVAL=60

WAKA_API=https://wakatime.com/api/v1
WAKA_USERNAME=
WAKA_TOKEN=
WAKA_PROJECT=
WAKA_INTERVAL=60

DATA_PATH=data
```

Required for the current script flow:

- `WAKA_API`
- `WAKA_TOKEN`

Notes:

- `src/config.py` loads `.env` first, then `.env.example` as fallback defaults.
- `DATA_PATH` is resolved relative to the project root.
- `README.md` in the project root is the file that gets updated.

## Running the Script

Run the entry point from the project root:

```powershell
python .\src\main.py
```

The script fetches yesterday's WakaTime summary and writes a diff-style language block into the daily section of `README.md`.

## Output

After a successful run:

- `README.md` contains refreshed daily language stats between the section markers.
- `data/coding_stats.json` contains the raw WakaTime response used for the update.

## Troubleshooting

- If you get `Missing WAKA_API`, set `WAKA_API` in `.env` or `.env.example`.
- If you get `Missing WAKA_TOKEN`, add a valid WakaTime API token to `.env`.
- If the script reports missing daily markers, add the start and end tags to `README.md`.
- If no activity is returned, confirm that WakaTime has data for yesterday.
