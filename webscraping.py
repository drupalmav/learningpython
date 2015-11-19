import requests
from bs4 import BeautifulSoup





url = "http://www.indeed.com/jobs?q=hardware+engineer&l=San+Francisco%2C+CA"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# job_titles = soup.find_all("div", {"class", "row"})
job_titles = soup.find_all("h2", {"class", "jobtitle"})
jobs_sponsored = soup.find_all("div", {"data-tn-component", "sponsoredJob"})

for title in job_titles:
    print title.text.strip()
    #print title.contents[0].text
    # print title.contents[1].text
    # print title.contents[1].find_all("a", {"class", "jobtitle turnstileLink"})
    #print "\n"



print "SPONSORED JOB LISTINGS"
print "\n"

for sponsored in jobs_sponsored:
    print sponsored.text.strip()