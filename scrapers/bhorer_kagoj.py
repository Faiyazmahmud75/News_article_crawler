from .base import BaseScraper
from utils.helpers import clean_whitespace

class BhorerKagojScraper(BaseScraper):
    def parse(self, soup):

        headline = soup.select_one("h1")
        author   = soup.select_one("p.detailReporter")

        content_raw  = soup.select("div.detailBody p")
        # filter out p tags with classes
        content = [p for p in content_raw if not p.has_attr("class")] # p with classes are ads

        published = soup.select_one("p.detailPTime")

        return {
            "headline": clean_whitespace(headline.get_text()) if headline else "",
            "author": clean_whitespace(author.get_text()) if author else "",
            "content": "\n".join(p.get_text() for p in content),
            "published": clean_whitespace(published.get_text()) if published else "",
        }
