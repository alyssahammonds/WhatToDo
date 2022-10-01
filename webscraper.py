from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen


# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
def myfunc():
    url = "https://www.arlington.org/events/?view=list&sort=date"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")
    #print(doc.prettify())
    eventNames = doc.find_all("a")
    for name in eventNames:
        print(name.find_next_sibling())
    dates = doc.findAll("span", {"class": "mini-date-container"})
    for date in dates:
        print(date.get_text())

    eventLocations = doc.findAll("span", {"class": "locations truncate"})
    for location in eventLocations:
        print(location.get_text())


myfunc()
