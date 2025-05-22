from .base import BaseScraper
from utils.helpers import clean_whitespace

class SamakalScraper(BaseScraper):
    # function for scraping data
    def parse(self, soup):
        headline_elements = soup.select('div.dheading > h2, div.dheading > h1')
        # Filter out empty texts and clean whitespace
        headline_parts = [h.get_text(strip=True) for h in headline_elements if h.get_text(strip=True)]
        
        reporter = soup.select_one('div.writter')
        content  = soup.select('div#contentDetails p')
        published = soup.select_one('div.dateAndTime p')

        # returning the data as a dictionary (will be used in the main.py file)
        return {
            "headline": " | ".join(headline_parts),
            "author": clean_whitespace(reporter.get_text()) if reporter else "",
            "content": "\n".join(p.get_text(strip=True) for p in content),
            "published": clean_whitespace(published.get_text()) if published else "",
        }
