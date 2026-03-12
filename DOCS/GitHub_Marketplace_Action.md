## GitHub Marketplace Action

This repository now includes a reusable GitHub Action at the root: `action.yml`.

### What it does

- Fetches daily WakaTime coding data
- Updates the section between `<!--START_SECTION:daily-->` and `<!--END_SECTION:daily-->`
- Writes raw API response to `data/coding_stats.json`
- Exposes an output named `changed` (`true` or `false`)

### Inputs

- `waka-token` (required): WakaTime API token
- `github-token` (optional): GitHub token for script compatibility
- `waka-api` (optional): defaults to `https://wakatime.com/api/v1`
- `bar-style` (optional): `block`, `shade`, `ascii`, `dot`, `pipe`, `emoji`
- `python-version` (optional): defaults to `3.12`
- `entrypoint` (optional): defaults to `src/main.py`

### Example workflow usage

```yaml
name: Update README Daily

on:
	schedule:
		- cron: "0 */6 * * *"
	workflow_dispatch:

permissions:
	contents: write

jobs:
	update:
		runs-on: ubuntu-latest
		steps:
			- uses: actions/checkout@v4

			- name: Run Waka README Action
				id: daily
				uses: pphatdev/pphatdev@v1
				with:
					waka-token: ${{ secrets.WAKA_KEY }}
					github-token: ${{ secrets.GITHUB_TOKEN }}
					bar-style: block

			- name: Commit generated files
				if: steps.daily.outputs.changed == 'true'
				uses: stefanzweifel/git-auto-commit-action@v5
				with:
					commit_message: "chore(readme): update daily coding stats"
					file_pattern: "README.md data/coding_stats.json"
```

### Publish to Marketplace

1. Commit and push `action.yml` to `main`.
2. Create a release tag like `v1.0.0`.
3. Create/update moving major tag `v1` to that release commit.
4. Open your repository on GitHub and choose **Publish this Action to Marketplace**.
5. Fill in listing metadata (name, icon, categories, description) and submit.
