import logging
import os
import base64
import requests


logging.basicConfig(handlers=[
    logging.FileHandler("logs.txt"),
    logging.StreamHandler()
],
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')

print("sa")
request_data = []

for root, dirs, files in os.walk("images"):
    i = 0
    for file in files:
        i += 1
        with open("images/" + file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            image_name = image_file.name
            base64_image = 'data:image/png;base64,' + encoded_string
            print(base64_image)
            data = {"fileName": image_name, "fileBase64": base64_image}
            request_data.append(data)
        if i == 10:
            print(request_data)
            print("request at")
            i = 0
            request_data = []
    print(request_data)
    print("request at")
