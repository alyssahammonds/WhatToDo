
# This is the file where the program will take user's interests
# and pull the dictionaries returned by the webscraper
# Then, it will find the intersection of the dictionaries to
# be specific to the user. ex: user wants virtual events and
# anything regarding music - we will find the intersection of
# virtualeventsdictionary and musiceventsdictionary

import bigFiveClassification
import webscraper


def showEventsToUser(BigFive, Hobbies, Listofwords):
    default = webscraper.allevents() # dictionary of ALL events in location
    personality = bigFiveClassification.classificationScore(Listofwords) # store Conscientiosness, Extraversion, ...
    dictionaries = []
    for x in Hobbies:
        match Hobbies[x]:
            case "Hiking":
                dictionaries[x] = webscraper.outdoorEvents()
            case "Music":
                dictionaries[x] = webscraper.musicEvents()
            case "Movies":
                dictionaries[x] = webscraper.filmEvents()
    
    # find intersection
    final_dict = {x: dictionaries[x] for x in dictionaries[0] if x in dictionaries[1]} #hardcoded for now

    return final_dict


