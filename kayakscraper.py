from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys


url = "http://www.kayak.com/flights/IAH-ORL/2015-12-24/2015-12-29/2adults"

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

print soup.title.text

# prices = soup.find_all('a', {'class', 'bookitprice'})
#
# for i in prices:
#     print i.text
#     print "\n\n"

results = soup.find_all('div', {'class', 'flightresult'})

for row in results:
    price = row.find('a', {'class', 'bookitprice'})
    airline = row.find('div', {'div', 'airlineName'})
    print "Price = " + price.text + ", Airline = " + airline.text



# for price in prices:
#     print price


#print html
# print soup.prettify()[0:1000]

if "267" in soup.text:
    print "267 is present in the response"

driver.quit()


