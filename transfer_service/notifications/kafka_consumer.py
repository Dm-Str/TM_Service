from kafka import KafkaConsumer
import json


class KafkaConsumer:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic, 
                                      bootstrap_servers=['localhost:9092'], 
                                      auto_offset_reset='earliest',
                                      group_id='my-group',
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    def listen(self):
        for message in self.consumer:
            self.send_notigication(message.value)

    def send_notigication(self, data):
        print(data)
