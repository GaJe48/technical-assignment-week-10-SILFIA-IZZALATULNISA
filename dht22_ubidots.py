from ubidots import ApiClient
import random
import time
import sys
import Adafruit_DHT

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT22
pin = 14

# Create an ApiClient object
api = ApiClient(token='BBFF-I4jKpKqGGug5zXxbzbDVNDfJZZM2ar')

try:
    #Get a Ubidots Variable
    variable1 = api.get_variable("64daf191f570a6000b2f3209")
    variable2 = api.get_variable("64daf1da0bbd57000b8858f3")

except ValueError:
    print ("It is not possible to obtain the variable")

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        variable1.save_value({'value': humidity})
        variable2.save_value({'value': temperature})
        print ("Value sent")
    except ValueError:
        print ("Value not sent") 


