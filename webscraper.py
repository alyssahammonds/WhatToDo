
from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen


def socialevents():
    url = "https://www.eventbrite.com/d/tx--arlington/events/"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_= 'eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text()) #create an array of event names

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    arrayLocations = []
    eventLocation = doc.find_all('div', class_ = 'eds-event-card-content__sub eds-text-bm eds-text-color--ui-600 eds-l-mar-top-1')
    for location in eventLocation:
        arrayLocations.append(location.get_text()) #create an array of event locations
