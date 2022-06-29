#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm


# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[21]:


url='https://presidentofindia.nic.in/former-presidents.htm'
r=requests.get(url)
soup=BeautifulSoup(r.content)

name=[]
term_of_office=[]

# Scrapping name and term of office
details=soup.find_all('div',class_='presidentListing')
for i in details:
    #name
    name.append(i.text.split("\n")[1].split("(")[0])
    #term of office
    term_of_office.append(i.text.split("\n")[2].split(":")[1])

# Printing scrapped details
print("The list of names of respective former presidents of India:::\n \n",name,"\n")
print("The list of term of their office:::\n \n",term_of_office,"\n")
print("Combined list of names and there respective terms of office:::\n \n",list(zip(name,term_of_office)))

