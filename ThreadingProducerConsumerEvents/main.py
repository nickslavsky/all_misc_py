import logging
import threading
import Crawler
import Producer
import Consumer
import queue

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='producer_consumer_w_events.log',
                        filemode='w',
                        format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    crawler = Crawler.Crawler('put any URL here')
    url_queue = queue.Queue()
    done = threading.Event()
    producer = Producer.ProducerThread(done_event=done, url_queue=url_queue, crawler=crawler, name='producer')
    consumer = Consumer.ConsumerThread(done_event=done, url_queue=url_queue, name='consumer')
    producer.start()
    consumer.start()
