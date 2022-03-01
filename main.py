# -*- coding: utf-8 -*-
# coding:utf8
import datetime
from bs4 import BeautifulSoup
import time
import uuid
from request import *
from testFileReader import *
from ikvSoupHelper import *
import logging

logging.basicConfig(handlers=[
                        logging.FileHandler("logs.txt"),
                        logging.StreamHandler()
                    ],
                    level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')

# ikvPage = readTestFile("ikvPage.txt")
baseLinkToScrape = "http://forum.istanbuloyun.com/viewtopic.php?f=137&t=165147"

ikvPage = getPageWithIkvHeaders(baseLinkToScrape)
ikvPageSoup = BeautifulSoup(ikvPage, "html.parser")

try:
    title = find_title_of_post(ikvPageSoup)
except Exception as e:
    logging.error("Cannot found page title, session probably is gone. " + str(datetime.datetime.now()))
    # log page number
    quit()

pageBody = find_page_body(ikvPageSoup)

pagination = find_pagination_element_on_pagebody(pageBody)

lastPageNumber = find_last_page_number(pagination)

posts = find_all_posts_on_pagebody(pageBody)

imageLinks = []

for i in range(0, lastPageNumber):
    if i != 0:
        linkToScrape = baseLinkToScrape + "&start=" + str(i * 10)
        ikvPage = getPageWithIkvHeaders(linkToScrape)
        ikvPageSoup = BeautifulSoup(ikvPage, "html.parser")
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
            imageResponse = None
            try:
                imageResponse = requests.get(link)
            except:
                logging.error("Image Not Found :" + link)
            requestEnd = time.time()
            logging.info("Downloading Image Request Elapsed Time:" + str(requestEnd - requestStart))
            if imageResponse is not None and imageResponse.status_code == 200:
                with open("images/" + title + ";" + postUsername + ";" + str(uuid.uuid4()).upper() + ".png", 'wb') as f:
                    f.write(imageResponse.content)
                del imageResponse
                imageLinks.append(imgTag['src'])
logging.info(imageLinks)
