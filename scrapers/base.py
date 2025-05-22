from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class BaseScraper(ABC):
   # user agent to avoid bot detection
    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/39.0.2171.95 Safari/537.36"
    )

    def __init__(self, url: str):
        self.url = url

    def fetch(self):
        # Getting the full html content of the page
        resp = requests.get(self.url, headers={"User-Agent": self.USER_AGENT})
        resp.raise_for_status()
        return BeautifulSoup(resp.content, "html5lib")

    @abstractmethod
    def parse(self, soup: BeautifulSoup):
        # Parsing content from the soup object (this will be done by subclasses)
        pass

    def scrape(self):
        # Full scraping process
        soup = self.fetch()
        data = self.parse(soup)
        data["source"] = self.__class__.__name__.replace("Scraper", "")

        return data
