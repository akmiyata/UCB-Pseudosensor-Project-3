from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pseudoSensor import PseudoSensor
from datetime import datetime
import json
import boto3
import sys

#Set service resource
sqs=boto3.resource('sqs', region_name='us-east-2', aws_access_key_id=" Wouldntyouliketoknow ", aws_secret_access_key="Wouldntyouliketoknow")

#Define queue for messages
queue=sqs.get_queue_by_name(QueueName='5318_Proj1')

#Define client parameters
myMQTTClient = AWSIoTMQTTClient("dojodevice1")
myMQTTClient.configureEndpoint("endpoint", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1 (1).pem","./ Wouldntyouliketoknow ", "./ Wouldntyouliketoknow.crt")


#Connect to client
myMQTTClient.connect()
print("Client Connected")


#Gettimestamp in string format
rn=datetime.now()
timein=str(rn.strftime("%H:%M:%S"))

ps=PseudoSensor()


#Generate 10 weather values
for i in range(10):

  h,t = ps.generate_values()
  foo={"H":[h],"T":[t],"Time":[timein]}

#Reformat json into string, for MQTT use
  json_dump=json.dumps(foo)
  msg = json_dump
  topic = "general/inbound"
  #Publish weather data 
  myMQTTClient.publish(topic, msg, 0)  
  print("Message Sent")
  #Rule to send messages to SQS
  response=queue.send_message(MessageBody=msg)

#Disconnect from MQTT client
myMQTTClient.disconnect()
print("Client Disconnected")
