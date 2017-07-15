import threading
import logging
import queue
import Crawler


class ProducerThread(threading.Thread):
    def __init__(self, done_event: threading.Event, url_queue: queue.Queue, crawler: Crawler.Crawler,
                 name: str = None) -> None:
        """
        Producer thread. Receives crawler object and calls its crawl() generator. Sets done_event when done
        :type done_event: threading.Event
        :type crawler: Crawler.Crawler
        :type url_queue: queue.Queue
        """
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self.name = name
        assert isinstance(done_event, threading.Event)
        assert isinstance(url_queue, queue.Queue)
        self._queue = url_queue
        self._crawler = crawler
        self._event = done_event

    def run(self):
        for file_url in self._crawler.crawl():
            try:
                self._queue.put(file_url)
                self._logger.debug(f'Putting {str(file_url)} : {str(self._queue.qsize())} items in queue')
            except Exception as ex:
                self._logger.error(ex)
        self._event.set()
