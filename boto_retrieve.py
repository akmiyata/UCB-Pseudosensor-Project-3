from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pseudoSensor import PseudoSensor
from datetime import datetime
import json
import boto3
import sys

#Get service resource
sqs=boto3.resource('sqs', region_name='us-east-2', aws_access_key_id=" Wouldntyouliketoknow ", aws_secret_access_key=" Wouldntyouliketoknow ")

#Get my queue
queue=sqs.get_queue_by_name(QueueName='5318_Proj1')

for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))
    
    # Let the queue know that the message is processed, remove from queue
    message.delete()