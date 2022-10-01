from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen



#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
html = urlopen("https://www.arlington.org/events/")
bsObj = BeautifulSoup(html, "html.parser")

eventNames = bsObj.findAll("span", {"class":"title truncate"})
for name in eventNames:
    print(name.get_text())

dates = bsObj.findAll("span", {"class":"month"})
for date in dates:
    print(date.get_text())

eventLocations = bsObj.findAll("span", {"class":"locations truncate"})
for location in eventLocations:
    print(location.get_text())
    
    
