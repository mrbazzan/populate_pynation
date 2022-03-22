
import requests
import sys
from bs4 import BeautifulSoup

url = "https://www.sport-histoire.fr/en/Geography/Countries_by_alphabetical_order.php"

try:
    response = requests.get(url)
except requests.exceptions.ConnectionError:
    print("Service Error.")
    sys.exit()

soup = BeautifulSoup(response.text, 'html.parser')


def gen(data):
    for element in data:
        yield element.find_all("td")[:-1]


table = soup.find("table").find("tbody").findAll('tr')

country_capital = []
for row in gen(table):
    # ['country', 'capital']
    country_capital.append(list(map(lambda x: x.get_text(), row)))

print(country_capital)
