from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from urllib.parse import urlsplit, urljoin

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}


def fix_link(link):
    if link.startswith('//'):
        link = 'http:' + link

    return link


def fix_url(base_url, url):
    uparts = urlsplit(url)
    if not uparts[0] and not uparts[1]:
        url = urljoin(base_url, url)
    elif url.startswith('//'):
        url = 'http:' + url

    return url


def main():
    url = input('Please enter url of page to scrape: ') or 'http://imgur.com/'
    print('Scraping links and images for {0}...'.format(url))
    try:
        r = get(url=url, headers=headers)
        base_url = url
    except RequestException:
        print('Something wrong with the url or with your Internet connection. Sorry :(')
        exit(0)
    soup = BeautifulSoup(r.text)
    print(list(set([fix_link(t["src"]) for t in soup.find_all('img')])))
    print(list(set([fix_url(base_url, t["href"]) for t in soup.find_all('a')])))


if __name__ == '__main__':
    main()