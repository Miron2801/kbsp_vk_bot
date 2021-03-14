import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.mirea.ru/schedule/"
r = requests.get(url)
result = pd.DataFrame()

r = requests.get(url) 
soup = BeautifulSoup(r.text, "lxml")
#for i in range(len( soup.find_all('a', {'class': 'uk-link-toggle'}) )):
 #   print("=============================================================")
#tables=soup.find_all('a', {'class': 'uk-link-toggle', })
print("страница загружена")

#print(soup.find_all('a',{'class': 'uk-link-toggle'}))

for link in soup.find("div").parent.find_all('a',{'class': 'uk-link-toggle'}):
    print("=====================")
    print(link.get("href"))
 #   print(link)
    #print(td.text)

 #   print(tables)