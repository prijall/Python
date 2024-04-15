import requests 
import pandas as pd
from bs4 import BeautifulSoup


url='https://ticker.finology.in/'

r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.text, 'lxml')
table=soup.find_all('table', class_='table table-sm table-hover screenertable')
# print(table)
header=soup.find_all('th')
# print(header)

titles=[]
for i in header:
    title= i.text
    titles.append(title)

print(titles)

df=pd.DataFrame(columns=titles)
# print(df)
