import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from main import scraper

url = 'https://shop.adidas.jp/item/?category=footwear&gender=mens'
r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')


product = soup.find("div", {"class": "test-articleDisplay css-1yuo7po"})
#print(product)
product_url =[]
for link in product.find_all('a'):
    product_url.append("https://shop.adidas.jp" + link.get('href'))

#print(product_url)

df = pd.DataFrame(product_url,  columns =['product_details_url'])
df = df.drop(df[df['product_details_url']=="https://shop.adidas.jp/adiclub/membersweek/"].index)


timestr = time.strftime("%Y%m%d-%H%M%S")
df.to_csv("product-details-url-list"+"-"+timestr+".csv")
print(df)

col_list = df.product_details_url.values.tolist()
print(col_list)

for link in col_list:
    scraper(link)