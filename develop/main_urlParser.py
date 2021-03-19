import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_kbsp():
        mass = []
        url = "https://www.mirea.ru/schedule/"
        r = requests.get(url)
        result = pd.DataFrame()

        r = requests.get(url) 
        soup = BeautifulSoup(r.text, "lxml")
        print("страница загружена")

        for link in soup.find("div").parent.find_all('a',{'class': 'uk-link-toggle'}):
            mass.append(link.get("href"))
        return mass
kbsp_searcher = search_kbsp()
for i in kbsp_searcher:
        if i.find("КБиСП 1") > 0 and i.find("магистры") == -1:
            print(i)