import logging
import os
import base64
import requests

authToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEiLCJlbWFpbCI6InN0cmluYkBhc2QuY29tIiwidXNlcm5hbWUiOiJzdHJpbmciLCJyb2xlIjoiYWRtaW4iLCJuYmYiOjE2NTEyNTk5OTUsImV4cCI6MTY1MTM0NjM5NSwiaWF0IjoxNjUxMjU5OTk1fQ.wuEh0UXYwkHAvrsCmCuLru0lAj9WnLfZaqEHFh8v71M"
enableRequests = False
selectedFolder = "images/"

logging.basicConfig(handlers=[
    logging.FileHandler("logs.txt"),
    logging.StreamHandler()
],
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')

request_data = []

for root, dirs, files in os.walk("images"):
    i = 0
    for file in files:
        i += 1
        with open(selectedFolder + file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            image_name = os.path.basename(image_file.name)

            splitImageName = image_name.split('_')
            imageTitle = splitImageName[0]
            imageAuthor = splitImageName[1]
            imageDate = splitImageName[2]

            base64_image = 'data:image/png;base64,' + encoded_string
            data = {
                "title": imageTitle,
                "username": imageAuthor,
                "fileBase64": base64_image,
                "timestampString": imageDate
            }
            request_data.append(data)
        if i / 10 == 1:
            if enableRequests:
                response = requests.post(url="http://localhost:5000/api/v1/post/bulk-save-raw", json=request_data,
                                         headers={"Authorization": authToken}, )

            i = 0
            print(request_data)
            request_data = []

    if len(request_data) > 0:
        if enableRequests:
            response = requests.post(url="http://localhost:5000/api/v1/post/bulk-save-raw", json=request_data,
                                     headers={"Authorization": authToken}, )
            print(request_data)


    print("request at")
