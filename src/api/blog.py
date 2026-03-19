import requests
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

BLOG_RSS_URL = "https://pphat.me/rss.xml"
MEDIA_NS = "http://search.yahoo.com/mrss/"


class BlogAPIError(Exception):
    pass


class BlogAPI:
    def __init__(self):
        self.url = BLOG_RSS_URL
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/rss+xml, application/xml, text/xml"})

    def _rss_date_to_iso(self, pub_date: str) -> str:
        try:
            return parsedate_to_datetime(pub_date).isoformat()
        except Exception:
            return pub_date

    def get_recent_posts(self, limit: int = 5):
        try:
            response = self.session.get(self.url, timeout=30)
            response.raise_for_status()
            root = ET.fromstring(response.content)
        except requests.exceptions.RequestException as e:
            raise BlogAPIError(f"Blog RSS Error: Failed to fetch feed - {e}") from e
        except ET.ParseError as e:
            raise BlogAPIError(f"Blog RSS Error: Failed to parse XML - {e}") from e

        posts = []
        for item in root.findall("./channel/item")[:limit]:
            title_el    = item.find("title")
            link_el     = item.find("link")
            desc_el     = item.find("description")
            pub_date_el = item.find("pubDate")
            enclosure_el       = item.find("enclosure")
            media_content_el   = item.find(f"{{{MEDIA_NS}}}content")
            media_thumb_el     = item.find(f"{{{MEDIA_NS}}}thumbnail")

            title       = (title_el.text    or "").strip() if title_el    is not None else ""
            url         = (link_el.text     or "").strip() if link_el     is not None else ""
            description = (desc_el.text     or "").strip() if desc_el     is not None else ""
            pub_date    = (pub_date_el.text  or "").strip() if pub_date_el is not None else ""

            thumbnail = ""
            if media_thumb_el is not None:
                thumbnail = media_thumb_el.get("url", "")
            elif media_content_el is not None:
                thumbnail = media_content_el.get("url", "")
            elif enclosure_el is not None:
                thumbnail = enclosure_el.get("url", "")

            slug = url.split("/posts/")[-1] if "/posts/" in url else url

            posts.append({
                "title":       title,
                "slug":        slug,
                "description": description,
                "thumbnail":   thumbnail,
                "createdAt":   self._rss_date_to_iso(pub_date),
            })

        return posts
