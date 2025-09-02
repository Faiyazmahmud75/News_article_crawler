##  Purpose
This project has been prepared to collect, analyse and train a Political AI model for an ongoing academic research project. 
### Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`
- `html5lib`
- `pandas`

You can install the dependencies with:

```bash
pip install requests beautifulsoup4 html5lib pandas
```

### Usage

### 1. Clone the Repository

```bash
git clone https://github.com/hiar-ac/political-ai.git
cd political-ai
```

### 2. Install Dependencies

Ensure you have Python 3 installed. Install the required packages:

```bash
pip install -r requirements.txt
```
*If `requirements.txt` does not exist, manually install the packages as shown above.*

### 3. Run the Scraper

The main script is `main.py`. To extract articles from the supported news sites and save them to a CSV file, run:

```bash
python main.py
```

This will:
- Scrape articles from predefined URLs for each site. 
- Aggregate the results.
- Output the data to `scrapped_data.csv`.

### 4. Output

After running, you'll find a file called `scrapped_data.csv` in the project directory. This file contains all the scraped articles with columns for:
- **Headline**,
- **Author**,
- **Content**,
- **Published date**, and
- **Source**
---
### Additional Information

Apart from scraping articles, this project also includes a news link scrapper (scrapers > url_crawler.py) that collects article links from the sitemaps of the targetted news websites within a given date range.

Total 2.32 million news links have been collected from 5 newspaper sites using this crawler.
