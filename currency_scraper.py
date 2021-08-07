
import requests
from bs4 import BeautifulSoup

url = "https://thefactfile.org/countries-currencies-symbols/"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

table_body = soup.find('table')

all_country = []
table_row_all = table_body.findAll('tr')
a = 0
# TODO: Implement a generator here
for table_row in table_row_all:
    table_data_all = table_row.findAll('td') or table_row.findAll('th')
    a_country = []

    for table_data in table_data_all[1:]:
        a_country.append(table_data.text)

    continent = table_data_all[0].text
    try:
        float(continent)
    except ValueError:
        new_continent = continent

    if a_country != ['Country', 'Currency', 'Code', 'Symbol']:
        a_country.insert(0, new_continent)
        all_country.append(a_country)

print(all_country)
