# -*- coding: utf-8 -*-
# coding:utf8
import datetime
from bs4 import BeautifulSoup
import time
import uuid
from request import *
from testFileReader import *
from ikvSoupHelper import *
from txtWriterHelper import *
import logging


def scrape_thread(threadId):
    # ikvPage = readTestFile("ikvPage.txt")
    baseLinkToScrape = "http://forum.istanbuloyun.com/viewtopic.php?f=137&t=" + str(threadId)
    imageLinks = []

    ikvPage = getPageWithIkvHeaders(baseLinkToScrape)
    ikvPageSoup = BeautifulSoup(ikvPage, "html.parser")
    isStillLoggedIn, loggedInUsername = is_still_logged_in(ikvPageSoup)
    if not isStillLoggedIn:
        logging.error("Account is not logged in. Session Expired " + str(datetime.datetime.now()))
        logging.error("BaseUrl: " + baseLinkToScrape)
        logging.error("ThreadId: " + str(threadId))
        quit()

    logging.info("User still logged in: " + loggedInUsername)

    try:
        title = find_title_of_post(ikvPageSoup)
    except Exception as e:
        logging.error("Cannot found page title, page is deleted or hidden. Returning..." + str(datetime.datetime.now()))
        return None

    pageBody = find_page_body(ikvPageSoup)

    postDate = find_post_date(pageBody)

    pagination = find_pagination_element_on_pagebody(pageBody)

    lastPageNumber = find_last_page_number(pagination)

    posts = find_all_posts_on_pagebody(pageBody)

    for i in range(0, lastPageNumber):
        try:
            scrape_all_pages_on_thread(baseLinkToScrape, i, imageLinks, postDate, posts, title)
        except:
            try:
                scrape_all_pages_on_thread(baseLinkToScrape, i, imageLinks, postDate, posts, title)
            except Exception as e:
                write_to_later_list("laterlist.txt", threadId)
                write_to_later_list("errorLogs.txt", str(e))
    logging.info(imageLinks)
    return len(imageLinks)


def scrape_all_pages_on_thread(baseLinkToScrape, i, imageLinks, postDate, posts, title):
    time.sleep(1)
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
                imageResponse = requests.get(link, timeout=10)
            except:
                logging.error("Image Not Found :" + link)
            requestEnd = time.time()
            logging.info("Downloading Image Request Elapsed Time:" + str(requestEnd - requestStart))
            if imageResponse is not None and imageResponse.status_code == 200:
                filename = "" + title + "_" + postUsername + "_" + postDate + "_" + str(uuid.uuid4()).upper()
                keepcharacters = (' ', '_', '-')
                safeFilename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()
                with open("images/" + safeFilename + ".png", 'wb') as f:
                    f.write(imageResponse.content)
                del imageResponse
                imageLinks.append(imgTag['src'])
