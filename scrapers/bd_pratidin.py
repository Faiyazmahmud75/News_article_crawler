from .base import BaseScraper
from utils.helpers import clean_whitespace

class BDPratidinScraper(BaseScraper):
    def parse(self, soup):

        headline = soup.select_one("h1.card-title")
        author   = soup.select_one("span.fs-5")
        content  = soup.select("article p")

        published = soup.select_one("span.pubNews")
        # if span.pubNews not found, it means publish time is directly in the div tag
        if not published:
            published = soup.select_one("div.col-4.pe-0")

        return {
            "headline": clean_whitespace(headline.get_text()) if headline else "",
            "author": clean_whitespace(author.get_text()) if author else "",
            "content": "\n".join(p.get_text() for p in content),
            "published": clean_whitespace(published.get_text()) if published else "",
        }
