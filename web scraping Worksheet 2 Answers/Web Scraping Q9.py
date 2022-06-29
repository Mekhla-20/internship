#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q9)Write a python program to scrape mentioned details from dineout.co.in :
#i) Restaurant name
#ii) Cuisine
#iii) Location 
#iv) Ratings
#v) Image URL


# In[7]:


from bs4 import BeautifulSoup
import requests


# In[33]:


url='https://www.dineout.co.in/delhi-restaurants/welcome-back'
r=requests.get(url)
soup=BeautifulSoup(r.content)

#i) Scraping Restaurants Name
titles=soup.find_all('a',class_='restnt-name ellipsis')
print("Restaurants Name \n")
for i in titles:
    print(i.text)
    
#ii) Scraping Cuisine
cuisine=soup.find_all('span',class_='double-line-ellipsis')
print("\n \n Cuisine \n")
for i in cuisine:
    print(i.text.split("|")[1])    
    
#iii) Scraping Location
locations=soup.find_all('div',class_='restnt-loc ellipsis')
print("\n \n Location \n")
for i in locations:
    print(i.text)    
    
#iv) Scraping Ratings
ratings=soup.find_all('div',class_='restnt-rating rating-4')
print("\n \n Ratings \n")
for i in ratings:
    print(i.text)  
    
#iv) Scraping Image URL
urls=soup.find_all('img',class_='no-img')
print("\n \n Image URLs \n")
for i in urls:
    print(i['data-src'])   


