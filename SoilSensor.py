import RP1.GPIO as GPio
import time

channel==4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def callback(channel):
       if GPIO.input(channel):
           print ("water Detected")
   	else:
		PRINT("WATER Detected")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channek,callback)

while loop:
 	time.sleep(0)
