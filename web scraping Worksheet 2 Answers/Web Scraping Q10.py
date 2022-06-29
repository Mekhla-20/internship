#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q10) Write a python program to scrape the details of top publications from Google Scholar from https://scholar.google.com/citations?view_op=top_venues&hl=en
#i) Rank 
#ii) Publication
#iii) h5-index
#iv) h5-median


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[8]:


url='https://scholar.google.com/citations?view_op=top_venues&hl=en'
r=requests.get(url)
soup=BeautifulSoup(r.content)

#i) Scraping Rank
rank=soup.find_all('td',class_='gsc_mvt_p')
print("Rank \n")
for i in rank:
    print(i.text)

#ii) Scraping Publication
pub=soup.find_all('td',class_='gsc_mvt_t')
print("\n \nPublication \n")
for i in pub:
    print(i.text)
    
#iii) Scraping h5-index
h5=soup.find_all('a',class_='gs_ibl gsc_mp_anchor')
print("\n \nh5-index \n")
for i in h5:
    print(i.text)
    
#iv) Scraping h5-median
h5_m=soup.find_all('span',class_='gs_ibl gsc_mp_anchor')
print("\n \nh5-median \n")
for i in h5_m:
    print(i.text)
    

