import os

import smtplib
from email.message import EmailMessage


email_address=os.environ.get("email_user")
email_password=os.environ.get("email_pass")

msg=EmailMessage()
msg['Subject']="Hello Welcome to Python"
msg["From"]=email_address
msg["To"]="hello@gmail.com"
msg.set_content("I love to learn Python")



with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	
	smtp.login(email_address,email_password)
	smtp.send_message(msg)
