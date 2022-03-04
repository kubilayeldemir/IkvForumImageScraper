from threadHelper import *
import time
from txtWriterHelper import *


def scrape_threads(startingThreadId):
    totalDownloadedImageNumber = 0
    for threadNumber in range(startingThreadId, 165148):
        downloadedImageNumberOnThread = 0
        try:
            downloadedImageNumberOnThread = scrape_thread(threadNumber)
        except:
            try:
                downloadedImageNumberOnThread = scrape_thread(threadNumber)
            except Exception as e:
                write_to_later_list("laterlist.txt", threadNumber)
                write_to_later_list("errorLogs.txt", threadNumber)


        if (downloadedImageNumberOnThread is None):
            downloadedImageNumberOnThread = 0
        totalDownloadedImageNumber = totalDownloadedImageNumber + downloadedImageNumberOnThread
        time.sleep(1)


def scrape_single_page(threadNumber):
    scrape_thread(threadNumber)


def scrape_threads_reverse(lastThreadId):
    totalDownloadedImageNumber = 0
    for threadNumber in range(lastThreadId, 0, -1):
        downloadedImageNumberOnThread = 0
        try:
            downloadedImageNumberOnThread = scrape_thread(threadNumber)
        except:
            try:
                downloadedImageNumberOnThread = scrape_thread(threadNumber)
            except Exception as e:
                write_to_later_list("laterlist.txt", threadNumber)
                write_to_later_list("errorLogs.txt", str(e))

        if downloadedImageNumberOnThread is None:
            downloadedImageNumberOnThread = 0
        totalDownloadedImageNumber = totalDownloadedImageNumber + downloadedImageNumberOnThread
        time.sleep(1)

