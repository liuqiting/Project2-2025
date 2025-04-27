import sotplib
from emal message import EoailNessage

#Set the sender email and password and recipient emaic
from_emaiL_addr ="3481258900@qq.com"
from_email_pass ="xpreunbtyulzchfb"
to_email_addr ="3481258900@qq.com"

# Create a message object
msg =EMailMessage()

# Set the email body
body ="Hello from Raspberry Pi"
msg.set_content(body)

# Set sender and recipient

msg['From']= from_email_addr
msg['To']= to_email_addr

# Set your email subject
msg['Subject’] = "TEST EMAIL”

# Connecting to server and sending email
# Edit the following line with your provider's SMTP server details

Sever=smtplib.SNTP( ‘smtp.qq.com',587 )

# Comment out the next line if your email provider doesn't use Tls
Sever.starttls()

# Login to the SMTp server
serxer.login(from_email_addr, from_email_pass)

#Send the message

Serxer.send_message (msg)

print("Email sent")

#Disconnect from the Server
server.guit()
