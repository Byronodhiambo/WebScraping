import requests

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url  = 'https://www.nike.com/w/mens-sale-shoes-3yaepznik1zy7ok'

f = open('menshoe.csv', 'w')
headers = "Brand, Description, Price, Discount, Seller Rating, link \n"
f.write(headers)

req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
client = urlopen(req, timeout=10)
web_page = client.read()
client.close()

soup = BeautifulSoup(web_page, 'html.parser')
shoes = soup.find_all("div",{"class":"product-card"})

print(len(shoes))