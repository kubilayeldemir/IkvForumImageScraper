from bs4 import BeautifulSoup
import requests
import logging
import time
import uuid

logging.basicConfig(level=logging.DEBUG)


def getPageBody(soup):
    return soup.find("div", {"id": "page-body"})


def findAllPostsOnPageBody(pageBody):
    return pageBody.findAll("div", {"class": "post"})


headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://forum.istanbuloyun.com/viewtopic.php?f=46&t=169906",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ikvforum_o73n9_k=; ikvforum_o73n9_u=73036; ikvforum_o73n9_sid=0da091a90435980619e162ab3444c5bc"
}

f = open('ikvPage.txt', 'r', encoding="utf8")
baseLinkToScrape = "http://forum.istanbuloyun.com/viewtopic.php?f=137&t=165147"
# ikvPage = f.read()
ikvPage = requests.get(baseLinkToScrape, headers=headers)

soup = BeautifulSoup(ikvPage.content)

title = soup.find("h2", class_="topic-title").text

pageBody = getPageBody(soup)

pagination = pageBody.find("div", class_="pagination")

paginationLiElements = pagination.findAll("li")

if paginationLiElements:
    lastPageNumber = int(paginationLiElements[-2].text)
else:
    lastPageNumber = 1

posts = findAllPostsOnPageBody(pageBody)

imageLinks = []

for i in range(0, lastPageNumber):
    if i == 0:
        # TODO linkToScrape scrape page
        linkToScrape = baseLinkToScrape
        print(linkToScrape)
    else:
        linkToScrape = baseLinkToScrape + "&start=" + str(i * 10)
        # TODO get page and scrape page

        print(linkToScrape)

for post in posts:
    postContent = post.find("div", {"class": "content"})
    images = postContent.findAll('img')
    postUsername = post.find('span', {"class": "username"}).text
    filteredImgTags = filter(lambda image: not image['src'].startswith('./images/smilies'), images)
    for imgTag in filteredImgTags:
        link = imgTag['src']
        requestStart = time.time()
        imageResponse = requests.get(link)
        requestEnd = time.time()
        print("Request Elapsed Time:" + str(requestEnd - requestStart))
        if imageResponse.status_code == 200:
            with open(title + ";" + postUsername + ";" + str(uuid.uuid4()).upper() + ".png", 'wb') as f:
                f.write(imageResponse.content)
            del imageResponse
        imageLinks.append(imgTag['src'])

print(imageLinks)
print(title)
