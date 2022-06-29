#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program to scrape the details of most downloaded articles from AI in last 90 days. https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
#Scrape below mentioned details :
#i) Paper Title 
#ii) Authors
#iii) Published Date 
#iv) Paper URL


# In[10]:


from bs4 import BeautifulSoup
import requests
import re


# In[14]:


url='https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
r=requests.get(url)
soup=BeautifulSoup(r.content)

#i) Scraping Paper Titles
titles=soup.find_all('h2',class_='sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR')
print("Paper Titles \n")
for i in titles:
    print(i.text.split("\n"))
    
#ii) Scraping Authors
titles=soup.find_all('span',class_='sc-1w3fpd7-0 pgLAT')
print("\n \n Authors \n")
for i in titles:
    print(i.text.split("\n"))
    
#iii) Scraping Published Date
Pb=soup.find_all('span',class_='sc-1thf9ly-2 bKddwo')
print("\n \n Published date \n")
for i in Pb:
    print(i.text.split("\n"))
    
#iv) Scraping Paper URLs
urls=soup.find_all('a',class_='sc-5smygv-0 nrDZj')
print("\n \n Printing Paper URLs \n")
for item in urls:
    print(item.get('href'))    
       

