from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen

range_miles = [] #store range from user
prices = [] #store price of the product
ratings = [] #store rating of the product


#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
html = urlopen("https://www.michigan.org/events?page=0")
bsObj = BeautifulSoup(html, "html.parser")

eventNames = bsObj.findAll("span", {"class":"field field--name-field-display-title field--type-string field--label-hidden field__item"})
for name in eventNames:
    print(name.get_text())

dates = bsObj.findAll("span", {"class":"event-dates"})
for date in dates:
    print(date.get_text())

eventLocations = bsObj.findAll("span", {"class":"field field--name-field-cities field--type-entity-reference field--label-hidden field__items"})
for location in eventLocations:
    print(location.get_text())
