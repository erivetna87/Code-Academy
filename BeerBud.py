#! Python 3
#Scraping Data From Beer Advocate
#Flow:

#Project 1 - Beer Bud Webscraper for data on popular beers from Beer Advocate

#Data Points:
#beerName
#beerBrewer
#beerDescription
#beerABV
#beerRatings
#beerScore

import requests, webbrowser, bs4, sys, re

#URLs for Data Points
popUrl = 'https://www.beeradvocate.com/lists/popular/'
topUrl = 'https://www.beeradvocate.com/lists/top/'

#Function to return all HTML data - Could this be improved? (Brett Qst)
def requestUrl(url):
    resUrl = requests.get(url) #why won't this pass the argument?
    resUrl.raise_for_status()
    htmlData = bs4.BeautifulSoup(resUrl.text, "lxml")
    return htmlData
#Function to obtain specific elements from HTML. Both arguments must be strings
def selectElements(url,selectMethod):
    requestUrl(url)
    bsSelectElem = requestUrl(url).select(selectMethod)
    return bsSelectElem

#HTML Elements:

beerNameElems = selectElements(popUrl,'a b')
beerBrewerElems = selectElements(popUrl,'span a')
#TODO: beerDescription
#TODO: beerABV
#TODO: beerRatings
#TODO beerScore

#strips HTML from requestUrl(url).select(selectMethod)
#TODO: May need to change enumerate & if not (index %2) may limit cross-functionality
def htmlStrip(elem):
    for index, i in (enumerate(elem)):
        if not (index % 2):
            elemStr = str(i)
            elemStr = re.sub(r'<.*?>','', elemStr)
            return (elemStr)

#Raw listing of data points in a string:

#Note: len(beerBrewerElems) is 504.
#Last 2 elements irrelevant to Brewer's Name
htmlStrip(beerBrewerElems[2:502])

#TODO: create a function that puts these items into a list -
#May not need. Don't know if str vs. list matters (research point)
