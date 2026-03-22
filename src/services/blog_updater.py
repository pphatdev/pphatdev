from datetime import datetime
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from config import README_PATH
from api.blog import BlogAPI

START_TAG = "<!--START_SECTION:blogs-->"
END_TAG = "<!--END_SECTION:blogs-->"
SITE_ORIGIN = "https://pphat.me"


def _format_date(iso_str: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y")
    except Exception:
        return iso_str


def _ensure_thumbnail_width(url: str, width: int = 200) -> str:
    if not url:
        return url

    parsed = urlsplit(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query["w"] = str(width)
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(query), parsed.fragment))


def _ensure_absolute_url(url: str, origin: str = SITE_ORIGIN) -> str:
    if not url:
        return url

    if url.startswith(("http://", "https://")):
        return url

    return f"{origin}{url}" if url.startswith("/") else f"{origin}/{url}"


def _build_blogs_section(posts):
    cards = []
    for post in posts:
        title = post.get("title", "Untitled")
        slug = post.get("slug", "")
        thumbnail = _ensure_thumbnail_width(post.get("thumbnail", ""), width=200)
        thumbnail_url = _ensure_absolute_url(thumbnail)
        url = f"https://pphat.me/posts/{slug}"

        card = []
        if thumbnail:
            card.extend(
                [
                    f'<a href="{url}" style="width: 200px;">',
                    "    <picture>",
                    f'    <source media="(prefers-color-scheme: dark)" srcset="{thumbnail_url}">',
                    f'    <img src="{thumbnail_url}" alt="{title}" title="{title}">',
                    "    </picture>",
                    f"    <p>{title}</p>",
                    "</a>",
                ]
            )
        cards.append("\n".join(card))

    return "\n".join(cards)


def get_recent_blog_posts():
    blog_api = BlogAPI()
    posts = blog_api.get_recent_posts(limit=5)

    if not posts:
        return []

    content = README_PATH.read_text(encoding="utf-8")
    start_index = content.find(START_TAG)
    end_index = content.find(END_TAG)

    # Skip silently when README has no blog section markers.
    if start_index == -1 or end_index == -1 or end_index < start_index:
        return posts

    end_index += len(END_TAG)
    new_section = f"{START_TAG}\n{_build_blogs_section(posts)}\n{END_TAG}"
    updated_content = content[:start_index] + new_section + content[end_index:]
    README_PATH.write_text(updated_content, encoding="utf-8")

    return posts
