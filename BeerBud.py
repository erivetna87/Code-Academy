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
    resUrl = requests.get(url) 
    resUrl.raise_for_status()
    htmlData = bs4.BeautifulSoup(resUrl.text, "lxml")
    return htmlData
#Function to obtain specific elements from HTML. Both arguments must be strings
def selectElements(url,selectMethod):
    requestUrl(url)
    bsSelectElem = requestUrl(url).select(selectMethod)
    return bsSelectElem

#HTML Elements:
#TODO: Get elements from topUrl
beerNameElems = selectElements(popUrl,'a b')
beerBrewerElems = selectElements(popUrl,'span a')
#TODO: beerDescription
#TODO: beerABV
#TODO: beerRatings
#TODO: beerScore

#strips HTML from requestUrl(url).select(selectMethod)
#this was probably a bad approach or there is a much simpler way. Talk to Brett on this.
#TODO: Need to change enumerate & if not (index % 2). lt will limit cross-functionality for different HTML requests.
def htmlStrip(elem):
    for index, i in (enumerate(elem)):
        if not (index % 2):
            elemStr = str(i)
            elemStr = re.sub(r'<.*?>','', elemStr)
            return (elemStr)

#Raw listing of data points in a string:

#Note: len(beerBrewerElems) is 504.
#Last 2 elements irrelevant to Brewer's Name
#TODO: Add beerNameElems. Assign each to variables.
htmlStrip(beerBrewerElems[2:502])

#TODO: create a function that puts these items into a list -
#May not need. Don't know if str vs. list matters. Likely to need list type for writing into .csv or type tuple for SQL?
