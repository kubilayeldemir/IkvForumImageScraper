from threadHelper import *
import time


def scrape_threads(startingThreadId):
    totalDownloadedImageNumber = 0
    for threadNumber in range(startingThreadId, 165148):
        downloadedImageNumberOnThread = scrape_thread(threadNumber)
        if (downloadedImageNumberOnThread is None):
            downloadedImageNumberOnThread = 0
        totalDownloadedImageNumber = totalDownloadedImageNumber + downloadedImageNumberOnThread
        time.sleep(1)


def scrape_single_page(threadNumber):
    scrape_thread(threadNumber)
