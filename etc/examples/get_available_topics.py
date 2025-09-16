from is_wire.core import Channel, Subscription
from is_msgs.common_pb2 import ConsumerList

channel = Channel("amqp://guest:guest@localhost:5672")
subscription = Subscription(channel)
subscription.subscribe(topic="BrokerEvents.Consumers")

while True:
    msg = channel.consume()
    consumers = msg.unpack(ConsumerList)
    for topic, nodes in consumers.info.items():
        print(f"Tópico: {topic} -> Consumidores: {nodes}")