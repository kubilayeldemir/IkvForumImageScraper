from threadHelper import *
from autoScraper import *

logging.basicConfig(handlers=[
    logging.FileHandler("logs.txt"),
    logging.StreamHandler()
],
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')

scrape_threads(1)
