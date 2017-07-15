import threading
import logging
import queue


class ConsumerThread(threading.Thread):
    def __init__(self, url_queue: queue.Queue, done_event: threading.Event, name=None):
        """
        Consumer thread. Takes an item out of queue for further processing.
        :type url_queue: queue.Queue
        :type done_event: threading.Event
        """
        super().__init__()
        self.name = name
        self._logger = logging.getLogger(self.name)
        assert isinstance(done_event, threading.Event)
        assert isinstance(url_queue, queue.Queue)
        self._queue = url_queue
        self._event = done_event

    def run(self):
        while not (self._queue.empty() and self._event.is_set()):
            if not self._queue.empty():
                item = self._queue.get()
                self._logger.debug(f'Getting {str(item)} : {str(self._queue.qsize())} items in queue')
        self._logger.info(f'Event state: {self._event.is_set()}')
        return
