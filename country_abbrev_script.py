
import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.iban.com/country-codes"
response = requests.get(url)

conn = sqlite3.connect("codes.db")
conn.row_factory = sqlite3.Row

db = conn.cursor()

# TODO:- add an integer primary key?
db.execute("""
    CREATE TABLE IF NOT EXISTS country_code(
        country TEXT NOT NULL,
        Alpha2 TEXT PRIMARY KEY,
        Alpha3 TEXT NOT NULL,
        numeric INTEGER);
""")

sql = "INSERT INTO country_code(country, Alpha2, Alpha3, numeric) VALUES (?, ?, ?, ?)"

soup = BeautifulSoup(response.text, 'html.parser')
ans = soup.find('table', {'id': 'myTable'})


for code in ans.find_next('tbody').find_all("tr"):
    _, a, b, c, d, _ = code.text.split("\n")
    try:
        db.execute(sql, (a, b, c, d))
        conn.commit()
    except sqlite3.IntegrityError:
        raise Exception("PRIMARY KEY MUST BE UNIQUE FOR EACH RECORD")

db.close()
