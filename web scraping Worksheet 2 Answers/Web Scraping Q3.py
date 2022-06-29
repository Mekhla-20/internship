#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


url='https://www.imdb.com/list/ls009997493/'
r=requests.get(url)
soup=BeautifulSoup(r.content)

name=[]
rating=[]
year_of_release=[]
detail=soup.find('div',class_='ipl-rating-star small')

# Scrapping name and year of release
details_movie=soup.find_all('h3',class_='lister-item-header')
for details in details_movie:
    #name
    name.append(details.text.split("\n")[2])
    #year of relase
    year_of_release.append(details.text.split("\n")[3].replace("(","").replace(")",""))
    
# Scrapping rating
details_rating=soup.find_all('div',class_='ipl-rating-star small')
for details in details_rating:
    rating.append(details.text.split("\n")[8])

# Creating dataframe
lst=list(zip(name,year_of_release,rating))
df=pd.DataFrame(lst,columns=['Name','Year of Release','Rating'])
print(df)


    

