import requests 
from bs4 import BeautifulSoup

URL = 'https://www.ebay.com/itm/Acer-Predator-Orion-9000-PC-Core-i7-8700K-3-7GHz-32GB-Ram-2TB-HDD-512GB-SSD-W10H/274065670310'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)


soup = BeautifulSoup(page.content, 'html.parser')


title = soup.find(id="itemTitle").get_text()
price = soup.find(id="prcIsum").get_text()
details = soup.find(id="viTabs_0_pd").get_text()

print("\n")
print(title)
print("\n")
print(price)
print("\n")
print(details.strip())
