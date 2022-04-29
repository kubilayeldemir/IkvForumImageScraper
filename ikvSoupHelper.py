def is_error_page(ikvPageSoup):
    x = ikvPageSoup.find("body", {"id": "errorpage"})
    return x is not None


def find_title_of_post(ikvPageSoup):
    return ikvPageSoup.find("h2", class_="topic-title").text


def is_still_logged_in(ikvPageSoup):
    usernameDiv = ikvPageSoup.find("li", {"id": "username_logged_in"})
    scraperAccountsUsername = None
    if usernameDiv is not None:
        scraperAccountsUsername = ikvPageSoup.find("span", {"class": "username"}).text
    return usernameDiv is not None, scraperAccountsUsername


def find_post_date(ikvPage):
    postBody = ikvPage.find("div", class_="postbody")
    authorP = postBody.find("p", class_="author")
    date = authorP.contents[4][:-4]
    date = date.replace(":", "-")
    date = date.replace(" ", "-")
    return date


def find_page_body(soup):
    return soup.find("div", {"id": "page-body"})


def find_all_posts_on_pagebody(pageBodySoup):
    return pageBodySoup.findAll("div", {"class": "post"})


def find_pagination_element_on_pagebody(pageBody):
    return pageBody.find("div", class_="pagination")


def find_last_page_number(pagination):
    paginationLiElements = pagination.findAll("li")
    if paginationLiElements:
        lastPageNumber = int(paginationLiElements[-2].text)
    else:
        lastPageNumber = 1
    return lastPageNumber


def find_post_content(post):
    return post.find("div", {"class": "content"})


def find_image_tags(element):
    return element.findAll('img')


def find_post_username(post):
    username = post.find('span', {"class": "username"})
    if not username:
        username = post.find('span', {"class": "username-coloured"})
    return username.text


def filter_images(images):
    filtered = filter(lambda image: not image['src'].startswith('./images/smilies'), images)
    filtered = filter(lambda image: not image['src'].startswith('//cdn.jsdelivr'), filtered)
    filtered = filter(lambda image: not image['src'].startswith('https://r.resimlink.com'), filtered)
    filtered = filter(lambda image: not image['src'].startswith('http://resim.myasinay.com/images/'), filtered)
    filtered = filter(
        lambda image: not image['src'].startswith("http://forum.istanbuloyun.com/images/uploads/etkinlik/"), filtered)
    return list(filtered)


def remove_quotes_from_post(postContent):
    for blockquote in postContent.findAll("blockquote"):
        blockquote.decompose()

