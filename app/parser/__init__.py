import abc
import datetime

from rabbit import RabbitSender
import json
from models import ArticleModel
import time


class AbstractParser(abc.ABC):

    @abc.abstractmethod
    def run(self):
        ...

    @abc.abstractmethod
    def stop(self):
        ...


class ExampleParser(AbstractParser):

    def __init__(self):
        self._sender = RabbitSender()

        self._articles = [
            ArticleModel(
                title=f"title{i}",
                text=f"text{i}",
                publish_date=str(datetime.datetime.now()),
                link=f"link{i}"
            ) for i in range(10)
        ]

    def run(self):
        print("Starting parser")
        for article in self._articles:
            time.sleep(1)
            print("New article found!")
            self._sender.send(
                json.dumps(article.__dict__)
            )

    def stop(self):
        self._sender.close()
