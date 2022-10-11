from __future__ import division
import requests
from turtle import delay
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

myurl = 'https://www.ncsasports.org/mens-basketball/colleges'

f = open('college.csv', 'w')
headers = "Brand, Description, Price, Discount, Seller Rating, link \n"
f.write("Brand, Description, Price, Discount, Seller Rating \n")

req = Request(myurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
client = urlopen(req, timeout=10)
web_page = client.read()
client.close()



soup = BeautifulSoup(web_page, 'html.parser')
table = soup.find_all("div", class_="container")
# print(len(table))

data = table[3]
print(data.prettify())
row = data.find_all('div')
# print(row.prettify())
school = row[0].a.get_text()
city_and_state = row[1].span.get_text() + ', ' + row[1].span.next_sibling.next_sibling.get_text()
region = row[2].span.get_text()
conference =row[3].get_text()
division = row[4].get_text()
for data in table:
    row = data.find_all('div')
    school = row[0].get_text()
    city_and_state = row[1].get_text()
    region = row[2].get_text()
    conference =row[3].get_text()
    division = row[4].get_text()
    f.write(school + " | " + city_and_state + " | " + region + " | " + conference + " | " + division + "\n")
    



# print(len(row))
# print(conference + ', '+ division)
# for row in table:
#     print(row.prettify())
#     row = table[i].find_all('div')
#     if ((row[0].a.get_text() == 'school')):
#         pass
#     try:
#             school = row[0].a.get_text()
#             city_and_state = row[1].span.get_text() + ', ' + row[1].span.next_sibling.next_sibling.get_text()
#             region = row[2].span.get_text()
#             conference =row[3].get_text()
#             division = row[4].get_text()
#             f.write(school + " | " + city_and_state + " | " + region + " | " + conference + " | " + division + "\n")
#     except:
#             school = 'None'
#             city_and_state = 'None'
#             region = "Not available"
#             conference = 'None'
#             division = 'None'