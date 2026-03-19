from datetime import datetime

from config import README_PATH
from api.blog import BlogAPI

START_TAG = "<!--START_SECTION:blogs-->"
END_TAG = "<!--END_SECTION:blogs-->"


def _format_date(iso_str: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y")
    except Exception:
        return iso_str


def _build_blogs_section(posts):
    cards = []
    for post in posts:
        title = post.get("title", "Untitled")
        slug = post.get("slug", "")
        description = " ".join(post.get("description", "").split())
        thumbnail = post.get("thumbnail", "")
        created_at = _format_date(post.get("createdAt", ""))
        url = f"https://pphat.me/posts/{slug}"

        card = ["<td width=\"50%\" valign=\"top\">", "<table>"]
        if thumbnail:
            card.extend(
                [
                    "<tr>",
                    f'<td><a href="{url}"><img src="{thumbnail}" width="100%" alt="{title}" /></a></td>',
                    "</tr>",
                ]
            )
        card.extend(
            [
                "<tr>",
                f'<td><strong><a href="{url}">{title}</a></strong></td>',
                "</tr>",
            ]
        )
        if description:
            card.extend(
                [
                    "<tr>",
                    f"<td>{description}</td>",
                    "</tr>",
                ]
            )
        card.extend(
            [
                "<tr>",
                f"<td><sub>{created_at}</sub></td>",
                "</tr>",
                "</table>",
                "</td>",
            ]
        )
        cards.append("\n".join(card))

    rows = []
    for index in range(0, len(cards), 2):
        row_cards = cards[index:index + 2]
        if len(row_cards) == 1:
            row_cards.append('<td width="50%"></td>')
        rows.append("<tr>\n" + "\n".join(row_cards) + "\n</tr>")

    return "<table>\n" + "\n".join(rows) + "\n</table>"


def get_recent_blog_posts():
    blog_api = BlogAPI()
    posts = blog_api.get_recent_posts(limit=5)

    if not posts:
        return []

    content = README_PATH.read_text(encoding="utf-8")
    start_index = content.find(START_TAG)
    end_index = content.find(END_TAG)

    if start_index == -1 or end_index == -1:
        raise ValueError("Could not find blog section markers in README.md")

    end_index += len(END_TAG)
    new_section = f"{START_TAG}\n{_build_blogs_section(posts)}\n{END_TAG}"
    updated_content = content[:start_index] + new_section + content[end_index:]
    README_PATH.write_text(updated_content, encoding="utf-8")

    return posts
