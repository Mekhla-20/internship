#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
url='https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
r=requests.get(url)
soup=BeautifulSoup(r.content)

rankings=[]
teams=[]
matches=[]
points=[]
ratings=[]

# Scrapping 1st team
team1=soup.find('tr',class_='rankings-block__banner')
rankings.append(team1.text.split("\n")[1])
teams.append(team1.text.split("\n")[4])
matches.append(team1.text.split("\n")[7])
points.append(team1.text.split("\n")[8])
ratings.append(team1.text.split("\n")[10].split(" ")[28])

# Scraping other teams
other_teams=soup.find_all('tr',class_='table-body')
for i in other_teams:
    rankings.append(i.text.split("\n")[1])
    teams.append(i.text.split("\n")[4])
    matches.append(i.text.split("\n")[7])
    points.append(i.text.split("\n")[8])
    ratings.append(i.text.split("\n")[9])

#Printing top 10 teams
for j in range(10):    
    print("Rank- ",rankings[j])
    print("Team- ",teams[j])
    print("Matches- ",matches[j])
    print("Points- ",points[j])
    print("Ratings- ",ratings[j],"\n")


# In[3]:


# b) Top 10 women’s ODI Batting players along with the records of their team and rating

url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting'
r=requests.get(url)
soup=BeautifulSoup(r.content)

ranking=[]
batting=[]
team=[]
rating=[]

# Scraping rank 1 batting details
bat1=soup.find('tr',class_='rankings-block__banner')
ranking.append("1")
batting.append(bat1.text.split("\n")[20])
team.append(bat1.text.split("\n")[27])
rating.append(bat1.text.split("\n")[31])

# Scraping other batting details
other_teams=soup.find_all('tr',class_='table-body')
for i in other_teams:
    ranking.append(i.text.split("\n")[4].split(" ")[36])
    if i.text.split("\n")[8]=="(0)":
        batting.append(i.text.split("\n")[13])
        team.append(i.text.split("\n")[17])
        rating.append(i.text.split("\n")[19])
        
        
    else:
        batting.append(i.text.split("\n")[16])
        team.append(i.text.split("\n")[20])
        rating.append(i.text.split("\n")[22])

# Print top 10 Batting women        
for j in range(10):    
    print("Rank- ",ranking[j])
    print("Batting- ",batting[j])
    print("Team- ",team[j])
    print("Ratings- ",rating[j],"\n")


# In[ ]:


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'
r=requests.get(url)
soup=BeautifulSoup(r.content)

ranking=[]
allRounder=[]
team=[]
rating=[]

# Scraping rank 1 all rounder details
AR1=soup.find('tr',class_='rankings-block__banner')
ranking.append("1")
allRounder.append(AR1.text.split("\n")[20])
team.append(AR1.text.split("\n")[27])
rating.append(AR1.text.split("\n")[31])

# Scraping other all rounder details
other_teams=soup.find_all('tr',class_='table-body')
for i in other_teams:
    print(i.text.split("\n"))
    ranking.append(i.text.split("\n")[4].split(" ")[36])
    if i.text.split("\n")[8]=="(0)":
        allRounder.append(i.text.split("\n")[13])
        team.append(i.text.split("\n")[17])
        rating.append(i.text.split("\n")[19])
        
    else:
        allRounder.append(i.text.split("\n")[16])
        team.append(i.text.split("\n")[20])
        rating.append(i.text.split("\n")[22])
        
# Printing top 10 all rounders
for j in range(10):    
    print("Rank- ",ranking[j])
    print("All Rounder- ",allRounder[j])
    print("Team- ",team[j])
    print("Ratings- ",rating[j],"\n")

