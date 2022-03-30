#Crypto updater, with data scraped from coinmarketcap.com
#Author: Joshua W. Smith 
#Date 2/28/22
from bs4 import BeautifulSoup as BS
import requests
class CryptoUpdater():
    def __init__(self):
        self.url = "https://coinmarketcap.com/"
        self.data = requests.get(self.url).text
        self.soup = BS(self.data, "html.parser")
        self.tbody = self.soup.tbody
        self.trs = self.tbody.contents
        self.prices = {}
        print("Initializing CryptoUpdater...")
    def data_to_txt(self):
        with open("cmkdata.txt", "w") as f:
            f.write(self.trs[0].next_sibling.prettify())
    def get_data(self):
        for tr in self.trs[:10]:
            name, price = tr.contents[2:4]
            fixed_name = name.p.string
            fixed_price = price.a.string
            self.prices[fixed_name] = fixed_price
        return self.prices


