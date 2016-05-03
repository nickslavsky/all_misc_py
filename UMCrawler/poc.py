import urllib.request
from bs4 import BeautifulSoup


def recurseLinks(base):
    try:
        f = urllib.request.urlopen(base)
        soup = BeautifulSoup(f.read(), "html.parser")
        for anchor in soup.find_all('a'):
            href = anchor.get('href')
            if href.startswith('/') or href.startswith('..'):
                pass # print('skip, most likely the parent folder -> ' + href)'''
            elif href.endswith('/'):
                print('crawl -> [' + base + href + ']')
                recurseLinks(base + href)  # make recursive call w/ the new base folder
            else:
                if href == 'kavbase.kdl':
                    print(base + 'kavbase.kdl')  # save it to a list or return
    except urllib.error.HTTPError as httperr:
        print('HTTP Error in ' + base + ': ' + str(httperr))

# call the initial root web folder
recurseLinks('http://dnl-test.kaspersky-labs.com/iro/updates/')
