import requests
from turtle import delay
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

myurl = 'https://www.jumia.co.ke/mobile-phones/'

# check if reachable
session = requests.Session()
response = session.get(myurl, headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)

# connect & grab page
req = Request(myurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
client = urlopen(req, timeout=10)
web_page = client.read()
client.close()

soup = BeautifulSoup(web_page, 'html.parser')
phones_cont = soup.find_all("a",{"class":"core"})

# print(len(phones))

for cont in phones_cont:
    brand = cont['data-brand']
    desc = cont['data-name']
    price = cont.find("div", {"class":"prc"}).get_text()
    disc = cont.find("div", {"class":"tag _dsct"}).get_text()    
    print(brand + " " + desc + " " + price + " " + disc )


# print(page_soup.header.prettify())