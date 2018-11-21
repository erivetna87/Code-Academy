#! Python 3
#Scraping Data From Beer Advocate


#Project 1 - Beer Bud Webscraper for data on popular beers from Beer Advocate

#Data Points:
#beerName
#beerBrewer
#beerDescription
#beerABV
#beerRatings
#beerScore

import requests, webbrowser, bs4, sys, re
from pprint import pprint

#URLs for Data Points
popUrl = 'https://www.beeradvocate.com/lists/popular/'
topUrl = 'https://www.beeradvocate.com/lists/top/'

#Function to return all HTML data - Could this be improved? (Brett Qst)
def requestUrl(url):
    resUrl = requests.get(url)
    resUrl.raise_for_status()
    htmlData = bs4.BeautifulSoup(resUrl.text, "lxml")
    return htmlData
#Function to obtain specific elements from HTML. Both arguments must be strings
def selectElements(url,selectMethod):
    bsSelectElem = requestUrl(url).select(selectMethod)
    return bsSelectElem

def beerABV(url):
    numericRegex = re.compile(r'''
    (\d+\.\d+%)
    ''', re.VERBOSE)
    foo = (requestUrl(url).getText())
    result = numericRegex.findall(foo)
    return (result)

#HTML Elements:
#TODO: Get elements from topUrl
#Grabs Beer Name, Beer Brewer and Beer Type
beerInfoElems = selectElements(popUrl,'td a')
#Grab Beer ABV
beer_ABV = beerABV(popUrl)
#Grabs Rating and Score
beerRankElems = selectElements(popUrl,'td b')

def htmlStrip(elem):
    result = []
    for i in (elem):
            elemStr = i.getText()
            # elemStr = str(i)
            # elemStr = re.sub(r'<.*?>','', elemStr)
            result.append(elemStr)
            #print(elemStr)
    return result

#TODO: Assign each to variables.
#TODO: Check for completeness of elements by doing a len/count/enumerate/whatever. All clean data elements should be 250 for popURL

#Data Points in type list for POPULAR beers
beerName = (htmlStrip(beerInfoElems[0::3]))
beerBrewer = (htmlStrip(beerInfoElems[1::3]))
beerType = (htmlStrip(beerInfoElems[2::3]))
beer_ABV = beerABV(popUrl)
beerScore = (htmlStrip(beerRankElems[2::3]))
beerRatings = (htmlStrip(beerRankElems[1::3]))

beerPopData = [beerName, beerBrewer, beerType, beer_ABV, beerScore, beerRatings]

def completenessCheck(Data):
    for i in Data:
        if (len(i)) == 250:
            print ("true")
        else:
            print ("false")

pprint (completenessCheck(beerPopData))




#TODO: consider putting data in dictionary.
#list type for writing into .csv or type tuple for SQL? how do files read/write dictionaries? research this
