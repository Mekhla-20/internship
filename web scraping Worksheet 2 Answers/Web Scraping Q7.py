#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link


# In[31]:


from bs4 import BeautifulSoup
import requests
import re


# In[36]:


url='https://www.cnbc.com/world/?region=world'
r=requests.get(url)
soup=BeautifulSoup(r.content)

#i) Scraping headlines
headline=soup.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail')
print("Printing Headlines \n")
for item in headline:
    print(item.text.split("\n"))
    
# ii) Scraping time    
time=soup.find_all('span',class_='RiverByline-datePublished')
print("\n \n Printing Time \n")
for item in time:
    print(item.text)

#iii) Scraping News Link
link=soup.find_all('a',attrs={'href': re.compile("^https://")})
print("\n \n Printing Links \n")
for item in link:
    print(item.get('href'))

