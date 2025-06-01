import requests
import html5lib
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


url_list = [
    'https://www.prothomalo.com/world/india/inllfwyxis',
    'https://www.prothomalo.com/world/europe/ax7orqb6f4',
    'https://www.prothomalo.com/technology/artificial-intelligence/sdtumhrq22',
    'https://www.prothomalo.com/world/india/0tc2dor615',
    'https://www.bd-pratidin.com/national/2025/05/20/1118507',
    'https://www.bd-pratidin.com/national/2025/05/19/1118162',
    'https://www.bd-pratidin.com/islam/2025/05/19/1118085',
    'https://www.bd-pratidin.com/science/2025/05/01/1111821',
    'https://bhorerkagoj.com/tech/770256',
    'https://bhorerkagoj.com/law-justice/770229',
    'https://bhorerkagoj.com/tech/770172',
    'https://www.kalerkantho.com/online/world/2025/05/20/1520141',
    'https://www.kalerkantho.com/online/Islamic-lifestylie/2025/05/19/1519822',
    'https://www.kalerkantho.com/online/business/2025/05/18/1519341',
    'https://www.kalerkantho.com/online/sport/2025/05/20/1520156',
    'https://samakal.com/lifestyle/article/296473/%E0%A6%9A%E0%A6%BF%E0%A6%A8%E0%A6%BF%E0%A6%B0-%E0%A6%AA%E0%A6%BE%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%87-%E0%A6%AA%E0%A6%BF%E0%A6%81%E0%A6%AA%E0%A7%9C%E0%A6%BE-%E0%A6%A6%E0%A7%82%E0%A6%B0-%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87%E0%A6%A8-%E0%A6%AF%E0%A7%87%E0%A6%AD%E0%A6%BE%E0%A6%AC%E0%A7%87',
    'https://samakal.com/lifestyle/article/296304/%E0%A6%88%E0%A6%A6%E0%A7%87-%E0%A6%B2%E0%A6%BE-%E0%A6%B0%E0%A6%BF%E0%A6%AD%E0%A7%87%E0%A6%B0-%E2%80%98%E0%A6%A1%E0%A6%BF%E0%A6%AD%E0%A7%8B%E0%A6%B6%E0%A6%A8%E2%80%99',
    'https://samakal.com/lifestyle/article/296314/%E0%A6%A8%E0%A6%BF%E0%A7%9F%E0%A6%AE%E0%A6%BF%E0%A6%A4-%E0%A6%AC%E0%A6%BF%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B0%E0%A6%B8-%E0%A6%96%E0%A6%BE%E0%A6%93%E0%A7%9F%E0%A6%BE%E0%A6%B0-%E0%A6%89%E0%A6%AA%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%A4%E0%A6%BE',
]

for url in url_list:
    response = requests.get(url, headers=headers)  
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(soup.find('h1').text)