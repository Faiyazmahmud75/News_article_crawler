import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import random
import json

# end date for scraping links
end_date = datetime(2025, 6, 3)

# Newspaper info
newspapers = {
    # 'Kaler Kantho': {
    #     'start_date': datetime(2024, 1, 1),
    #     'template': 'https://www.kalerkantho.com/daily-sitemap/{date}/sitemap.xml',
    #     'domain': 'https://www.kalerkantho.com'
    # },
    # 'BD Pratidin': {
    #     'start_date': datetime(2023, 1, 1),
    #     'template': 'https://www.bd-pratidin.com/daily-sitemap/{date}/sitemap.xml',
    #     'domain': 'https://www.bd-pratidin.com'
    # },
    'Samakal': {
        'start_date': datetime(2025, 6, 2),
        'template': 'https://samakal.com/sitemap/sitemap-daily-{date}.xml',
        'domain': 'https://samakal.com'
    },
    # 'Prothom Alo': {
    #     'start_date': datetime(2009, 8, 28),
    #     'template': 'https://www.prothomalo.com/sitemap/sitemap-daily-{date}.xml',
    #     'domain': 'https://www.prothomalo.com'
    # },
    # 'Bhorer Kagoj': {
    #     'start_date': datetime(2017, 10, 3),
    #     'template': 'https://bhorerkagoj.com/sitemap/sitemap-daily-{date}.xml',
    #     'domain': 'https://bhorerkagoj.com'
    # }
}
# HTTP headers to mimic browser requests
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/125.0.0.0 Safari/537.36'
    ),
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}


results = []

# Loop through the newspapers dictionary (key, value)
for paper, item in newspapers.items():
    # each newspaper's details for scraping
    current_date = item['start_date']
    template = item['template']
    domain = item['domain']

    print(f"\n ~~~Crawling from {paper}~~~")
    # while loop until start date to end date to scrape links
    while current_date <= end_date:

        date_str = current_date.strftime('%Y-%m-%d')
        sitemap_url = template.format(date=date_str)
        
        print(f"Extracted [{len(results)}] links so far from ~{str(paper).upper()}~ | Processing date: <{date_str}>", end='\r')

        try:
            response = requests.get(sitemap_url, headers=headers, timeout=30)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content, 'xml')
                    urls = soup.find_all('url') #parent element of <loc>

                    for url in urls:
                        loc_tag = url.find('loc') #<loc> tag contains the news article url
                        lastmod_tag = url.find('lastmod')

                        if loc_tag:
                            news_url = loc_tag.text
                            if not news_url.startswith(domain):
                                continue
                            news_time = lastmod_tag.text if lastmod_tag else date_str

                            results.append([paper, news_time, news_url])

                except Exception as e: # Catching any parsing errors
                    print(f"Parsing error: {sitemap_url} - {e}")
            else:
                print(f"Failed: {sitemap_url} (status {response.status_code})")

        except requests.exceptions.RequestException as e: # Catch all requests exceptions
            print(f"Request Error: {e} — URL: {sitemap_url}")

        current_date += timedelta(days=1)
        time.sleep(random.uniform(0.5, 1.5))

print(f"Total news link found: {len(results)}")

# saving resluts to a Json file
try:
    with open('sm_news_links.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"Results successfully saved to news_links.json")
except Exception as e:
    print(f"Error saving results to file: {e}")

print("\n ===Execution Complete===")

# for row in results[:5]:  # preview first 10
#     print(row)

