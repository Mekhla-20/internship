#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1) Write a python program to display all the header tags from wikipedia.org


# In[ ]:


from bs4 import BeautifulSoup 


# In[ ]:


import requests


# In[ ]:


url="https://www.wikipedia.org/"
r=requests.get(url)


# In[ ]:


soup=BeautifulSoup(r.content)
print(soup.prettify())


# In[ ]:


heading1=c.find("h1",attrs={'class':'central-textlogo-wrapper'})
print(heading1)
heading2=c.findAll("h2",attrs={'class':'bookshelf-container'})
print(heading2)


# In[ ]:




