from kafka import KafkaProducer
import json


class KafkaProduce:
    def __init__(self, topic):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topic = topic

    def send(self, message):
        self.producer.send(self.topic, value=message)
