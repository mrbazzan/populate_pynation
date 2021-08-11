
import requests
from bs4 import BeautifulSoup

url = "https://countrycode.org"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def gen(list_data):
    counter = 0
    for data in list_data:
        counter += 1
        yield data, counter


countries = []
table = soup.find('table').findAll('tr')
for table_data in gen(table):

    each_country = []
    for td in gen(table_data[0].findAll('td')):
        if td[1] == 3:
            continue
        if td[0].find('a'):
            each_country.append(td[0].find('a').text.title())
        else:
            each_country.append(td[0].text)

    if each_country:
        countries.append(each_country)

print(countries)
