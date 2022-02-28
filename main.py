from bs4 import BeautifulSoup
import logging
import time
import uuid
from request import *
from testFileReader import *
from ikvSoupHelper import *

logging.basicConfig(level=logging.DEBUG)

# ikvPage = readTestFile("ikvPage.txt")
baseLinkToScrape = "http://forum.istanbuloyun.com/viewtopic.php?f=137&t=165147"

ikvPage = getPageWithIkvHeaders(baseLinkToScrape)
ikvPageSoup = BeautifulSoup(ikvPage)

title = find_title_of_post(ikvPageSoup)

pageBody = find_page_body(ikvPageSoup)

pagination = find_pagination_element_on_pagebody(pageBody)

lastPageNumber = find_last_page_number(pagination)


posts = find_all_posts_on_pagebody(pageBody)

imageLinks = []

for i in range(0, lastPageNumber):
    if i == 0:
        print("ilk sayfa zaten elimizde.")
    else:
        linkToScrape = baseLinkToScrape + "&start=" + str(i * 10)
        print(linkToScrape)
        ikvPage = getPageWithIkvHeaders(linkToScrape)
        ikvPageSoup = BeautifulSoup(ikvPage)
        title = find_title_of_post(ikvPageSoup)
        pageBody = find_page_body(ikvPageSoup)
        posts = find_all_posts_on_pagebody(pageBody)

    for post in posts:
        postContent = find_post_content(post)
        images = find_image_tags(postContent)
        postUsername = find_post_username(post)
        filteredImgTags = filter_images(images)
        for imgTag in filteredImgTags:
            link = imgTag['src']
            requestStart = time.time()
            imageResponse = requests.get(link)
            requestEnd = time.time()
            print("Request Elapsed Time:" + str(requestEnd - requestStart))
            if imageResponse.status_code == 200:
                with open("images/"+title + ";" + postUsername + ";" + str(uuid.uuid4()).upper() + ".png", 'wb') as f:
                    f.write(imageResponse.content)
                del imageResponse
            imageLinks.append(imgTag['src'])


print(imageLinks)
print(title)
