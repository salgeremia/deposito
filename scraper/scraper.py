# https://realpython.com/beautiful-soup-web-scraper-python/
'''
> BEFORE RUNNING:
source venv/bin/activate
> AT THE END:
deactivate
'''

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

cards = soup.find_all("div", class_="card-content")
for card in cards[:1]:
    title = card.find("h2")
    subtitle = card.find("h3")
    location = card.find("p", class_="location")
    time = card.find("time")
    print(title, subtitle, location, time, sep='\n', end='\n\n')
    
'''
h2 = soup.find_all('h2')
for i in range(6):
    print(h2[i].text)
'''    