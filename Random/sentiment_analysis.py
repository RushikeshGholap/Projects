# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 01:31:29 2017

@author: Akshay
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.moneycontrol.com/news/world/'
z = requests.get(url)
htmltext = z.text
soup = BeautifulSoup(z.text,'lxml')
newsfeed=soup.find(class_="fleft")


headers1=newsfeed.find_all(class_="clearfix")

headers2=[]
content2 = []
for i in range(1,len(headers1)):
    content1=''
    headers2.append(headers1[i].a["title"])
    
    urlx = headers1[i].a["href"]
    pagex = requests.get(urlx)
    htmlx = pagex.text
    soupx = BeautifulSoup(htmlx,'lxml')
    contentx = soupx.find(class_="arti-flow")
    paragraphx = contentx.find_all("p")
    for j in paragraphx:
        try:
            content1 = content1+'\n'+j.string
        except:
            content1 = ''
    content2.append(content1)
    
df = pd.DataFrame({'header':headers2,'content':content2})

df["header"].iloc[1]

