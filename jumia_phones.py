import requests
from turtle import delay
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

myurl = ['https://www.jumia.co.ke/mobile-phones/''https://www.jumia.co.ke/mobile-phones/?page=2#catalog-listing', 'https://www.jumia.co.ke/mobile-phones/?page=3#catalog-listing', 'https://www.jumia.co.ke/mobile-phones/?page=4#catalog-listing'] 

f = open('phones.csv', 'w')
headers = "Brand, Description, Price, Discount, Seller Rating, link \n"
f.write("Brand, Description, Price, Discount, Seller Rating \n")

for url in myurl:
    # # reachable
    # session = requests.Session()
    # response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    # print(response.status_code)

    # connect & grab page
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
    client = urlopen(req, timeout=10)
    web_page = client.read()
    client.close()

    soup = BeautifulSoup(web_page, 'html.parser')
    phones_cont = soup.find_all("a",{"class":"core"})

    print(len(phones_cont))
    count = 0

    for cont in phones_cont:
        count = count+1        
        try:
            brand = cont['data-brand']
            desc = cont['data-name']
            price = cont.find("div", {"class":"prc"}).get_text()
            if (cont.find("div", {"class":"tag _dsct"}) == None):
                disc =cont.find("div", {"class":"tag _dsct _sm"}).get_text()
            else:
                disc = cont.find("div", {"class":"tag _dsct"}).get_text() 
            rating = cont.find("div", {"class":"stars _s"}).get_text()
            link = "https://www.jumia.co.ke"+cont['href']

            f.write(brand + " | " + desc + " | " + price + " | " + disc + " | " + rating + " | " + link +"\n")

        except:
            brand = 'None'
            desc = 'None'
            disc = "Not available"
            price = 'None'
            rating = 'None'
            link = 'None'

        

        print(count , " " + brand + " " + desc + " " + price + " " + disc + " " + rating + "  " + link )
    
f.close()
    # print(page_soup.header.prettify())