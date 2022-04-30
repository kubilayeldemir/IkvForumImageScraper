import logging
import requests

def getPageWithIkvHeaders(pageLink):
    logging.info("Getting page: " + pageLink)
    return requests.get(pageLink, headers=headers).content


headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http://forum.istanbuloyun.com/viewtopic.php?f=46&t=169906",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "ikvforum_o73n9_k=; ikvforum_o73n9_u=73036; ikvforum_o73n9_sid=7ca9e3d02f16c184b6dd9dcb0f2f68dd"
}

#To get the session cookie:
#curl 'http://forum.istanbuloyun.com/ucp.php?mode=login'   -H 'Connection: keep-alive'   -H 'Cache-Control: max-age=0'   -H 'Upgrade-Insecure-Requests: 1'   -H 'Origin: http://forum.istanbuloyun.com'   -H 'Content-Type: application/x-www-form-urlencoded'   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21'   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'   -H 'Referer: http://forum.istanbuloyun.com/ucp.php?mode=login'   -H 'Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'   -H 'Cookie: ikvforum_o73n9_u=1; ikvforum_o73n9_k=; ikvforum_o73n9_sid=07b1f0105140f9ee7d9ea23c291e5679'   --data-raw 'username=<your-username>&password=<your-password>&redirect=.%2Fucp.php%3Fmode%3Dlogin&sid=07b1f0105140f9ee7d9ea23c291e5679&redirect=index.php&login=Giri%C5%9F'   --compressed   --insecure -i