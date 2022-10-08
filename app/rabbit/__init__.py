import pika
import config
from models import ArticleModel
import uuid


class RabbitSender:

    def __init__(self):
        self._connection_params = pika.URLParameters(config.RABBIT_CONNECT_URL)
        self._connection = pika.BlockingConnection(parameters=self._connection_params)
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=config.RABBIT_QUEUE)

    def send(self, body: str):
        self._channel.basic_publish(body=body, exchange='', routing_key=config.RABBIT_QUEUE)

    def close(self):
        self._channel.close()
        self._connection.close()
