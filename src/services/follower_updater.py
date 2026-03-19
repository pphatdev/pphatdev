from config import README_PATH
from api.github import GitHubAPI

START_TAG = "<!--START_SECTION:followers-->"
END_TAG = "<!--END_SECTION:followers-->"

def _build_followers_section(followers):
    lines = []
    for follower in followers:
        login = follower.get("login")
        avatar_url = follower.get("avatar_url")
        html_url = follower.get("html_url")
        lines.append(
            f'<a href="{html_url}"><img src="{avatar_url}" width="60" height="60" alt="{login}" style="border-radius: 50%; vertical-align: middle; margin: 10px;" /></a>'
        )
    return "\n".join(lines)


def get_recent_followers_activity():
    github_api = GitHubAPI()
    recent_followers = github_api.get_recent_followers(limit=8)

    if not recent_followers:
        return []

    content = README_PATH.read_text(encoding="utf-8")
    start_index = content.find(START_TAG)
    end_index = content.find(END_TAG)

    if start_index == -1 or end_index == -1:
        raise ValueError("Could not find followers section markers in README.md")

    end_index += len(END_TAG)
    new_section = f"{START_TAG}\n{_build_followers_section(recent_followers)}\n{END_TAG}"
    updated_content = content[:start_index] + new_section + content[end_index:]
    README_PATH.write_text(updated_content, encoding="utf-8")

    return recent_followers
