from bs4 import BeautifulSoup
import requests
import os

# opening the website
r = requests.get("https://www.landkreis-muenchen.de/themen/verbraucherschutz-gesundheit/gesundheit/coronavirus/fallzahlen/")

# getting the value
soup = BeautifulSoup(r.text, 'html.parser')
tds = soup.find_all('td')
for td in tds:
    if td.get_text() == '7-Tage-Inzidenz laut Robert Koch-Institut (RKI):':
        print(td.find_next_sibling().get_text())
