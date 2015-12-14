'''
Scraper for tracing how often an app is released.
'''

import urllib2
from bs4 import BeautifulSoup
import csv

pkg = "com.mavdev.focusoutfacebook"
url = "https://play.google.com/store/apps/details?id=" + pkg

def get_app_lastupdate(pkg):
    url = "https://play.google.com/store/apps/details?id=" + pkg

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()

    soup = BeautifulSoup(data, 'html.parser')

    appTitle = soup.find("h1", {"class": "document-title"}).text
    date = soup.find("div", {"itemprop": "datePublished"})
    downloads = soup.find("div", {"itemprop": "numDownloads"})
    rating = soup.find('div', {'class': 'score'}).text

    reviews_list = list()

    individualReviews = soup.find_all("div", {"class": "single-review"})
    for oneReview in individualReviews:

        reviewDict = dict()
        author = oneReview.find('span', {'class': 'author-name'}).text
        date = oneReview.find('span', {'class': 'review-date'}).text
        link = "https://play.google.com/" + oneReview.find('a', {'class': 'reviews-permalink'}).get("href")
        title = oneReview.find('span', {'class': 'review-title'}).text
        body = oneReview.find('div', {'class': 'review-body'}).text
        rating = oneReview.find('div', {'class': 'tiny-star star-rating-non-editable-container'}).text


        reviewDict['author'] = author
        reviewDict['date'] = date
        reviewDict['link'] = link
        reviewDict['title'] = title
        reviewDict['body'] = body
        reviewDict['rating'] = rating

        reviews_list.append(reviewDict)

    revCntStr = soup.find('span',{'class':'rating-count'}).text
    revCntStr = revCntStr.replace(",", "")
    reviewCnt = int(revCntStr)



    appDict = dict()
    appDict['lastUpdaDate'] = date
    appDict['name'] = appTitle
    appDict['downloadCnt'] = downloads.text
    appDict['reviewCnt'] = reviewCnt
    appDict['reviews_list'] = reviews_list
    appDict['rating'] = rating
    return appDict


def print_individual_appdetail(package):
    lastUpdate = get_app_lastupdate(package)

    print lastUpdate['name']
    print lastUpdate['lastUpdaDate']
    print lastUpdate['downloadCnt']
    print lastUpdate['reviewCnt']
    print lastUpdate['rating']




def searchappsbykeywords(keyword):

    url = "https://play.google.com/store/search?q=" + keyword + "&c=apps"

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()

    soup = BeautifulSoup(data, 'html.parser')

    allapps = soup.find_all('div', {'class': 'card-content id-track-click id-track-impression'})

    print len(allapps)

    #for eachapp in allapps:
        #print eachapp
        #title = eachapp.find('a', {'class': 'title'}).text
        #print title
    for eachapp in allapps:
        link = eachapp.find('a', {'class': 'title'}).get("href")
        pkg = link.rsplit('=', 1)[1]
        print_individual_appdetail(pkg)


searchappsbykeywords("procrastination")

'''
#WRITING TO CSV FILE
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
'''
