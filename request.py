import requests


def getPageWithIkvHeaders(pageLink):
    return requests.get(pageLink, headers=headers).content


headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://forum.istanbuloyun.com/viewtopic.php?f=46&t=169906",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ikvforum_o73n9_k=; ikvforum_o73n9_u=73036; ikvforum_o73n9_sid=0da091a90435980619e162ab3444c5bc"
}
