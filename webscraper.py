from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen


def allevents():
    #default
    url = "https://www.eventbrite.com/d/tx--arlington/events/"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_= 'eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text()) #create an array of event names
        print(name.get_text())

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    #arrayLocations = []
    #eventLocation = doc.find_all('div', class_ = 'eds-event-card-content__sub eds-text-bm eds-text-color--ui-600 eds-l-mar-top-1')
    #for location in eventLocation:
    #   arrayLocations.append(location.get_text()) #create an array of event locations

    alleventsdict = {}
    for i in range(0, len(eventnamesarr)):
        temp = {eventnamesarr[i]: datesarrray[i]}
        alleventsdict.update(temp)

    return alleventsdict

def outdoorEvents():
    #if user prefers outdoorsy events
    url = "https://www.eventbrite.com/d/tx--arlington/travel-and-outdoor--events/?page=1"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_='eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text())  # create an array of event names

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    outdooreventsdict = {}
    for i in range(0, len(eventnamesarr)):
        temp = {eventnamesarr[i]: datesarrray[i]}
        outdooreventsdict.update(temp)

    return outdooreventsdict

def musicEvents():
    #if user prefers to be inside
    url = "https://www.eventbrite.com/d/tx--arlington/music--events/?page=1"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_='eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text())  # create an array of event names

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    musiceventsdict = {}
    for i in range(0, len(eventnamesarr)):
        temp = {eventnamesarr[i]: datesarrray[i]}
        musiceventsdict.update(temp)

    return musiceventsdict

def virtualEvents():
    #if no car and introverted, show these
    url = "https://www.eventbrite.com/d/online/all-events/?page=1"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_='eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text())  # create an array of event names

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    virtualeventsdict = {}
    for i in range(0, len(eventnamesarr)):
        temp = {eventnamesarr[i]: datesarrray[i]}
        virtualeventsdict.update(temp)

    print(virtualeventsdict)

    return virtualeventsdict

def filmEvents():
    #if no car and introverted, show these
    url = "https://www.eventbrite.com/d/online/all-events/?page=1"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    eventnamesarr = []
    eventNames = doc.find_all('div', class_='eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy')
    for name in eventNames:
        eventnamesarr.append(name.get_text())  # create an array of event names

    datesarrray = []
    dates = doc.find_all('div', class_ = 'eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    for date in dates:
        datesarrray.append(date.get_text()) #create an array of event dates

    filmeventsdict = {}
    for i in range(0, len(eventnamesarr)):
        temp = {eventnamesarr[i]: datesarrray[i]}
        filmeventsdict.update(temp)

    print(filmeventsdict)
