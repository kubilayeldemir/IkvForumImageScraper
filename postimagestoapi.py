import logging
import os
import base64
import requests
import imghdr

authToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEiLCJlbWFpbCI6InN0cmluYkBhc2QuY29tIiwidXNlcm5hbWUiOiJzdHJpbmciLCJyb2xlIjoiYWRtaW4iLCJuYmYiOjE2NTE2Nzc4NTYsImV4cCI6MTY1MTc2NDI1NiwiaWF0IjoxNjUxNjc3ODU2fQ.iHCTZY4A3s1KPg7eVUtyTbpEJMvLDb46u_HW6bBpq5Q"
enableRequests = True
selectedFolder = "images/"

logging.basicConfig(handlers=[
    logging.FileHandler("logs.txt"),
    logging.StreamHandler()
],
    level=logging.INFO,
    format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')

request_data = []

pngB64 = 'data:image/png;base64,'
allowedImages = ["jpeg", "png", "gif", "bmp"]

for root, dirs, files in os.walk("images"):
    i = 0
    for file in files:
        fileType = pngB64
        with open(selectedFolder + file, "rb") as image_file:
            imgType = imghdr.what(image_file)

            if imgType is None:
                print("File is corrupted.: " + file)
                continue

            if allowedImages.count(imgType) > 0:
                fileType = 'data:image/' + imgType + ';base64,'

            encoded_string = base64.b64encode(image_file.read()).decode()
            image_name = os.path.basename(image_file.name)

            splitImageName = image_name.split('_')
            imageTitle = splitImageName[0]
            imageAuthor = splitImageName[1]
            imageDate = splitImageName[2]

            base64_image = fileType + encoded_string
            data = {
                "title": imageTitle,
                "username": imageAuthor,
                "fileBase64": base64_image,
                "timestampString": imageDate,
                "fileType": imgType
            }
            i += 1
            request_data.append(data)
        if i / 10 == 1:
            for val in request_data.__iter__():
                print("Data OK - Title: " + val["title"] + " Username: " + val["username"] + " Timestamp: " + val[
                    "timestampString"])
            if enableRequests:
                response = requests.post(url="http://localhost:5000/api/v1/post/bulk-save-raw", json=request_data,
                                         headers={"Authorization": authToken})
                if response.status_code != 200:
                    print("HATA - Status Code: " + str(response.status_code))
                print(response.content)

            i = 0
            request_data = []

    if len(request_data) > 0:
        for val in request_data.__iter__():
            print("Data OK - Title: " + val["title"] + " Username: " + val["username"] + " Timestamp: " + val[
                "timestampString"])

        if enableRequests:
            response = requests.post(url="http://localhost:5000/api/v1/post/bulk-save-raw", json=request_data,
                                     headers={"Authorization": authToken})
            print(response.content)
