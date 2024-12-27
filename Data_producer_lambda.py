import json
from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name = '<Your Kafka topic Name>'
producer = KafkaProducer(
    bootstrap_servers = ['<Your Servers Name and port>'],
    value_serializer = lambda x: dumps(x).encode('utf-8')
)

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            sqs_message = record['body']
            print("Processed plain string message:", record['body'])

            #send message
            try:
                producer.send(topic_name, value = sqs_message)
            except Exception as a:
                print(f"Error in kafka sending message: {a}")
        
        producer.flush()
    except Exception as e:
        print(f"Error processing SQS event: {e}")

