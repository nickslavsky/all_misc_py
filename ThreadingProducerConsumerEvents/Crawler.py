import logging
import urllib.request
import urllib.error
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, base_url: str):
        self._logger = logging.getLogger(__name__)
        assert isinstance(base_url, str)
        self._base = base_url

    def crawl(self, base_url=None):
        """
        Start with base_url and recursively crawl all directories. Yield a link to every file
        :type base_url: str
        """
        if not base_url:
            base_url = self._base
        try:
            f = urllib.request.urlopen(base_url)
            soup = BeautifulSoup(f.read(), "html.parser")
            for anchor in soup.find_all('a'):
                href = anchor.get('href')
                if href.startswith('/') or href.startswith('..'):
                    # skip, most likely the parent folder
                    pass
                elif href.endswith('/'):
                    # make recursive call w/ the new base folder
                    yield from self.crawl(base_url + href)
                else:
                    yield base_url + href
        except urllib.error.HTTPError as http_error:
            self._logger.error(f'HTTP Error in {base_url}: {http_error}')
