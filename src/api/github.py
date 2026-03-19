import math
import requests

from config import GITHUB_USERNAME, GITHUB_API_URL, GITHUB_TOKEN

class GitHubAPIError(Exception):
    pass

class GitHubAPI:
    def __init__(self):
        self.base_url = GITHUB_API_URL.rstrip("/")
        self.username = GITHUB_USERNAME
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/vnd.github.v3+json"})
        if GITHUB_TOKEN:
            self.session.headers.update({"Authorization": f"Bearer {GITHUB_TOKEN}"})

    def get_recent_followers(self, limit: int = 14):
        if not self.username:
            raise ValueError("GITHUB_USERNAME configuration is missing.")

        from html.parser import HTMLParser
        
        class FollowerParser(HTMLParser):
            def __init__(self, target_username):
                super().__init__()
                self.target_username = target_username
                self.followers = []
                
            def handle_starttag(self, tag, attrs):
                if tag == 'img':
                    attrs_dict = dict(attrs)
                    class_attr = attrs_dict.get('class', '')
                    if 'avatar' in class_attr and 'avatar-user' in class_attr:
                        alt = attrs_dict.get('alt', '').replace('@', '')
                        src = attrs_dict.get('src', '')
                        if alt and ' ' not in alt and alt.lower() != self.target_username.lower():
                            if not any(f['login'] == alt for f in self.followers):
                                self.followers.append({
                                    'login': alt,
                                    'avatar_url': src,
                                    'html_url': f'https://github.com/{alt}'
                                })

        parser = FollowerParser(self.username)
        try:
            # The GitHub UI natively orders followers by exact follow date
            response = self.session.get(
                f"https://github.com/{self.username}?tab=followers", 
                timeout=30
            )
            response.raise_for_status()
            parser.feed(response.text)
            
            return parser.followers[:limit]

        except requests.exceptions.RequestException as e:
            raise GitHubAPIError(f"GitHub API Error: Failed to fetch followers by follow date - {e}") from e
