#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:::


# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

url='https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
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


# In[ ]:


# b) Top 10 ODI Batsmen along with the records of their team and rating.

url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
r=requests.get(url)
soup=BeautifulSoup(r.content)

ranking=[]
batsmen=[]
team=[]
rating=[]

# Scraping rank 1 batsmen details
batsmen1=soup.find('tr',class_='rankings-block__banner')
ranking.append("1")
batsmen.append(batsmen1.text.split("\n")[20])
team.append(batsmen1.text.split("\n")[27])
rating.append(batsmen1.text.split("\n")[31])

# Scraping other batsmen details
other_teams=soup.find_all('tr',class_='table-body')
for i in other_teams:
    ranking.append(i.text.split("\n")[4].split(" ")[36])
    if i.text.split("\n")[8]=="(0)":
        batsmen.append(i.text.split("\n")[13])
        team.append(i.text.split("\n")[17])
        rating.append(i.text.split("\n")[19])
       
    else:
        batsmen.append(i.text.split("\n")[16])
        team.append(i.text.split("\n")[20])
        rating.append(i.text.split("\n")[22])

# Print top 10 Batsmen        
for j in range(10):    
    print("Rank- ",ranking[j])
    print("Batsmen- ",batsmen[j])
    print("Team- ",team[j])
    print("Ratings- ",rating[j],"\n")


# In[ ]:


# c) Top 10 ODI bowlers along with the records of their team and rating.

url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
r=requests.get(url)
soup=BeautifulSoup(r.content)

ranking=[]
bowlers=[]
team=[]
rating=[]

# Scraping rank 1 bowlers details
bowlers1=soup.find('tr',class_='rankings-block__banner')
ranking.append("1")
bowlers.append(bowlers1.text.split("\n")[20])
team.append(bowlers1.text.split("\n")[27])
rating.append(bowlers1.text.split("\n")[31])

# Scraping other bowlers details
other_teams=soup.find_all('tr',class_='table-body')
for i in other_teams:
    ranking.append(i.text.split("\n")[4].split(" ")[36])
    if i.text.split("\n")[8]=="(0)":
        bowlers.append(i.text.split("\n")[13])
        team.append(i.text.split("\n")[17])
        rating.append(i.text.split("\n")[19])
    else:
        bowlers.append(i.text.split("\n")[16])
        team.append(i.text.split("\n")[20])
        rating.append(i.text.split("\n")[22])
        
    
# Printing top 10 Bowlers
for j in range(10):    
    print("Rank- ",ranking[j])
    print("Bowler- ",bowlers[j])
    print("Team- ",team[j])
    print("Ratings- ",rating[j],"\n")

