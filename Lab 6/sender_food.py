import paho.mqtt.client as mqtt
import uuid

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

while True:
	topic = "IDD/eatmyfood/food"
	print(f"now writing to topic {topic}")
	print("type new-topic to swich topics")
	while True:
		val = input(">> message: ")
		if val =='new-topic':
			break
		else:
			client.publish(topic, val)