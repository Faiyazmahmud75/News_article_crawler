import json
import html
from bs4 import BeautifulSoup
from scrapers.base import BaseScraper
from utils.helpers import clean_whitespace

class KalerKanthoScraper(BaseScraper):
    def parse(self, soup):
        headline = soup.select_one("h1.my-3")
        author = soup.select_one("h6.my-4")
        published = soup.select_one("time")

        # Step 1: Find the JSON-LD script tag
        script_tag = soup.find("script", type="application/ld+json")
        content = ""

        if script_tag:
            try:
                json_data = json.loads(script_tag.string)
                raw_article_body = json_data.get("articleBody", "")
                # Step 2: Decode HTML entities like &lt;, &gt;, etc.
                unescaped_html = html.unescape(html.unescape(raw_article_body))
                # Step 3: Strip HTML tags
                inner_soup = BeautifulSoup(unescaped_html, "html.parser")
                content = inner_soup.get_text(separator="\n", strip=True)
            except (json.JSONDecodeError, AttributeError) as e:
                print("Error parsing JSON-LD:", e)

        return {
            "headline": clean_whitespace(headline.get_text()) if headline else "",
            "author": clean_whitespace(author.get_text()) if author else "",
            "content": content,
            "published": clean_whitespace(published.get_text()) if published else "",
        }
