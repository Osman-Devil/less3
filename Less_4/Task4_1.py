import requests
from bs4 import BeautifulSoup

def currency_rates():
   url = "http://www.cbr.ru/scripts/XML_daily.asp"
   r = requests.get(url)
   soup = BeautifulSoup(r.text, 'lxml')


   return soup


print(currency_rates())