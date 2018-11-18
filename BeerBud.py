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

#Initial beginning approach maintained for reference

#Request URL
#resPop = requests.get(popUrl)
#resTop = requests.get(topUrl)

#Exception Monitoring
#resPop.raise_for_status()
#resTop.raise_for_status()

#passes URLs into BeautifulSoup Object
#popBeers = bs4.BeautifulSoup(resPop.text, "lxml")
#topBeers = bs4.BeautifulSoup(resTop.text, "lxml")

#beerNameElems = requestUrl(popUrl).select('a b')
#beerBrewerElems = requestUrl(popUrl).select('.muted a')

#print (beerNameElems)

import requests, webbrowser, bs4, sys

#URLs or Data Points
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

#Useful for certain websites that have poor HTML structure.
def stringSlice(elems,startIndex,endIndex):
    elemsStr = str(elems)
    start = elemsStr.find(startIndex) + 1
    end = elemsStr.find(endIndex, start)
    print (elemsStr)




#beerNameElems = selectElements(popUrl,'a b') - keep

beerBrewerElems = selectElements(popUrl,'span a')
#print (beerBrewerElems)
#stringSlice(beerBrewerElems,'','')
print (beerBrewerElems)


#print (stringSlice(beerBrewerElems,'>','<'))




#Initial approach maintained for reference

#Request URL
#resPop = requests.get(popUrl)
#resTop = requests.get(topUrl)

#Exception Monitoring
#resPop.raise_for_status()
#resTop.raise_for_status()

#passes URLs into BeautifulSoup Object
#popBeers = bs4.BeautifulSoup(resPop.text, "lxml")
#topBeers = bs4.BeautifulSoup(resTop.text, "lxml")

#beerNameElems = requestUrl(popUrl).select('a b')
#beerBrewerElems = requestUrl(popUrl).select('.muted a')

#print (beerNameElems)
