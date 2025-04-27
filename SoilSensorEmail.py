import smtplib
from email.message import EmailMessage
import RPi.GPIO as GPIO
import time

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("No need to water")
    else:
        print("Need to water")
        # when need to water
        # Set the sender email and password and recipient email
        from_email_addr = "3481258900@qq.com"
        from_email_pass = "xpreunbtyulzchfb"
        to_email_addr = "3481258900@qq.com"
        # Create a message object
        msg = EmailMessage()
        # Set the email body
        body = "Hello from Raspberry Pi, Need to water!"
        msg.set_content(body)
        # Set sender and recipient
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        # Set your email subject
        msg['Subject'] = "TEST EMAIL"
        # Connecting to server and sending email
        # Edit the following line with your provider's SMTP server details
        server = smtplib.SMTP('smtp.qq.com', 587)
        # Comment out the next line if your email provider doesn't use Tls
        server.starttls()
        # Login to the SMTp server
        server.login(from_email_addr, from_email_pass)
        # Send the message
        server.send_message(msg)
        print("Email sent")
        # Disconnect from the Server
        server.quit()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(0)
