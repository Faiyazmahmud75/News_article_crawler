from .base import BaseScraper
from utils.helpers import clean_whitespace

class ProthomAloScraper(BaseScraper):
    def parse(self, soup):
        
        headline = soup.select_one("h1")
        author   = soup.select("div.author-details span._8TSJC, div.author-details span._8-umj")
        content  = soup.select("div.story-element p")
        published = soup.select_one("time")

        return {
            "headline": clean_whitespace(headline.get_text()),
            "author":   ' '.join(el.get_text() for el in author) if author else "",
            "content":  "\n".join(p.get_text() for p in content),
            "published": clean_whitespace(published.get_text()) if published else "",
        }
