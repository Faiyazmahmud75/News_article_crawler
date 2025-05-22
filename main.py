import pandas as pd
from scrapers.samakal import SamakalScraper
from scrapers.prothom_alo import ProthomAloScraper
from scrapers.kaler_kantho import KalerKanthoScraper
from scrapers.bhorer_kagoj import BhorerKagojScraper
from scrapers.bd_pratidin import BDPratidinScraper

URLS = {
    SamakalScraper: [
        "https://samakal.com/politics/article/296385/...",
        "https://samakal.com/lifestyle/article/296314/%E0%A6%A8%E0%A6%BF%E0%A7%9F%E0%A6%AE%E0%A6%BF%E0%A6%A4-%E0%A6%AC%E0%A6%BF%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B0%E0%A6%B8-%E0%A6%96%E0%A6%BE%E0%A6%93%E0%A7%9F%E0%A6%BE%E0%A6%B0-%E0%A6%89%E0%A6%AA%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%A4%E0%A6%BE",
        "https://samakal.com/sports/article/296837/%E0%A6%A6%E0%A6%B0%E0%A7%8D%E0%A6%B6%E0%A6%95%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%97%E0%A6%BE%E0%A6%B2%E0%A6%BF%E0%A6%B0-%E0%A6%9C%E0%A6%AC%E0%A6%BE%E0%A6%AC%E0%A7%87-%E0%A6%89%E0%A6%A4%E0%A7%8D%E0%A6%A4%E0%A6%AA%E0%A7%8D%E0%A6%A4-%E0%A6%AA%E0%A6%B0%E0%A6%BF%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A6%BF%E0%A6%A4%E0%A6%BF-%E0%A6%B6%E0%A6%BE%E0%A6%AE%E0%A7%80%E0%A6%AE%E0%A6%95%E0%A7%87-%E0%A6%86%E0%A6%9F%E0%A6%95%E0%A6%BE%E0%A6%B2%E0%A7%87%E0%A6%A8-%E0%A6%A4%E0%A6%BE%E0%A6%A8%E0%A6%9C%E0%A6%BF%E0%A6%AE",
        "https://samakal.com/international/article/296819/%E0%A6%B6%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF%E0%A6%B6%E0%A6%BE%E0%A6%B2%E0%A7%80-%E0%A6%AD%E0%A7%82%E0%A6%AE%E0%A6%BF%E0%A6%95%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A7%87%E0%A6%B0-%E0%A6%86%E0%A6%98%E0%A6%BE%E0%A6%A4-%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%BF%E0%A6%B8%E0%A7%87-%E0%A6%95%E0%A6%BE%E0%A6%81%E0%A6%AA%E0%A6%B2-%E0%A6%87%E0%A6%B8%E0%A6%B0%E0%A6%BE%E0%A7%9F%E0%A7%87%E0%A6%B2%E0%A6%93",
    ],
    ProthomAloScraper: [
        "https://www.prothomalo.com/world/india/inllfwyxis",
        "https://www.prothomalo.com/politics/0mykhciei0",
        "https://www.prothomalo.com/world/0sy3xyspju",
        "https://www.prothomalo.com/sports/cricket/ls1a6xcniv",
    ],
    KalerKanthoScraper: [
        "https://www.kalerkantho.com/online/world/2025/05/20/1520141",
        "https://www.kalerkantho.com/online/country-news/2025/05/22/1521222",
        "https://www.kalerkantho.com/online/Islamic-lifestylie/2025/05/22/1521254",
        "https://www.kalerkantho.com/online/business/2025/05/21/1520902",
        "https://www.kalerkantho.com/online/sport/2025/05/22/1521130"

    ],
    BhorerKagojScraper: [
        "https://bhorerkagoj.com/tech/770256",
        "https://bhorerkagoj.com/india/770376",
        "https://bhorerkagoj.com/international/770358",
        "https://bhorerkagoj.com/middleeast/770364",
        "https://bhorerkagoj.com/economics/770236"

    ],
    BDPratidinScraper: [
        "https://www.bd-pratidin.com/campus-online/2025/05/22/1119214",
        "https://www.bd-pratidin.com/international-news/2025/05/22/1119234",
        "https://www.bd-pratidin.com/country/2025/05/22/1119236",
        "https://www.bd-pratidin.com/city-news/2025/05/22/1119233",
        

    ],
}

# Function to run all scrapers 

def run_all():
    print("Scraping...")
    all_data = []
    for ScraperClass, urls in URLS.items():
        for url in urls:
            scraper = ScraperClass(url)
            try:
                all_data.append(scraper.scrape())
            except Exception as e:
                print(f"[!] {ScraperClass.__name__} failed for {url}: {e}")
    return all_data

# Main function to run the script
if __name__ == "__main__":
    results = run_all()

    df = pd.DataFrame(results)
    df.to_csv('scrapped_data.csv', index=False)
    
    print(f"Scraping completed. total {len(results)} articles extracted")


# test = KalerKanthoScraper("https://www.kalerkantho.com/online/sport/2025/05/22/1521130")
# print(test.scrape())