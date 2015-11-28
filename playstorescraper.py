'''
Scraper for tracing how often an app is released.
'''

import urllib2
from bs4 import BeautifulSoup

pkg = "com.wsandroid.suite"
url = "https://play.google.com/store/apps/details?id=" + pkg


def get_app_lastupdate(pkg):
    url = "https://play.google.com/store/apps/details?id=" + pkg
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    appTitle = soup.find("div", {"class": "document-title"}).text
    date = soup.find("div", {"itemprop": "datePublished"})

    appDict = dict()
    appDict["lastUpdaDate"] = date.text
    appDict["name"] = appTitle
    # appInfoList.append(date.text)
    return appDict

lastUpdate = get_app_lastupdate(pkg)

for item in lastUpdate:
    print item
    for k in lastUpdate[item]:
        print k


# titles = soup.find_all("h1", {"class", "document-title"})
# print titles


# # job_titles = soup.find_all("div", {"class", "row"})
# job_titles = soup.find_all("h2", {"class", "jobtitle"})
# jobs_sponsored = soup.find_all("div", {"data-tn-component", "sponsoredJob"})
#
# for title in job_titles:
#     print title.text.strip()
#     #print title.contents[0].text
#     # print title.contents[1].text
#     # print title.contents[1].find_all("a", {"class", "jobtitle turnstileLink"})
#     #print "\n"
#
#
#
# print "SPONSORED JOB LISTINGS"
# print "\n"
#
# for sponsored in jobs_sponsored:
#     print sponsored.text.strip()