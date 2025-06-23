import mysql.connector
from mysql.connector import Error
import json
import os
# Tried integrating a mySQL database to store all the links, but its uncomplete, not sure if it's necessary
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load data
with open(os.path.join(base_dir, 'KalerKantho_and_BD_daily_links.json'), 'r', encoding='utf-8') as f:
    kaler_kantho_BD_daily = json.load(f)
with open(os.path.join(base_dir, 'prothomalo_news_links.json'), 'r', encoding='utf-8') as f:
    prothom_alo = json.load(f)
with open(os.path.join(base_dir, 'samakal_news_links.json'), 'r', encoding='utf-8') as f:
    samakal = json.load(f)
with open(os.path.join(base_dir, 'bhorer_kagoj_news_links.json'), 'r', encoding='utf-8') as f:
    bhorer_kagoj = json.load(f)
data = kaler_kantho_BD_daily + prothom_alo + samakal + bhorer_kagoj

print(f"Total links: {len(data)}")

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',      
        password='',    
        database='political_AI'
    )
    cursor = conn.cursor()
    insert_query = """
        INSERT IGNORE INTO news_links (source, published_at, url)
        VALUES (%s, %s, %s)
    """
    batch_size = 5000
    total_inserted = 0
    for batch in chunks(data, batch_size):
        values = [
            (item[0], item[1].replace('T', ' ').split('+')[0], item[2])
            for item in batch
        ]
        cursor.executemany(insert_query, values)
        conn.commit()
        total_inserted += cursor.rowcount
        print(f"Inserted {total_inserted} rows so far...")
    print(f"Inserted {total_inserted} rows in total.")
except Error as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()