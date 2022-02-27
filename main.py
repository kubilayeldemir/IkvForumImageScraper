from bs4 import BeautifulSoup
import requests

f = open('ikvPage.txt', 'r', encoding="utf8")
content = f.read()


headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://forum.istanbuloyun.com/viewtopic.php?f=46&t=169906",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ikvforum_o73n9_k=; ikvforum_o73n9_u=73036; ikvforum_o73n9_sid=f9c6f40a03853938703acca8a0f14f90"
}

ikvPage = requests.get("http://forum.istanbuloyun.com/viewtopic.php?f=137&t=165147&start=10", headers=headers)
soup = BeautifulSoup(ikvPage.content)

title = soup.find("h2", class_="topic-title").text
pageBody = soup.find("div", {"id": "page-body"})

posts = pageBody.findAll("div", {"class": "post"})

for post in posts:
    print("----------------------------------")
    postContent = post.find("div", {"class": "content"})
    images = postContent.findAll('img')
    filtered = filter(lambda image: not image['src'].startswith('./images/smilies'), images)
    for image in filtered:
        print(image['src'])
    print("----------------------------------")


# firstPostsBody = posts.find("div", {"class": "content"})

# print(firstPostsBody)

# print(soup.prettify())
#
# print("hoop")
print(title)

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
