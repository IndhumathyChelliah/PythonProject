import os
import imghdr

import smtplib
from email.message import EmailMessage


email_address=os.environ.get("email_user")
email_password=os.environ.get("email_pass")

msg=EmailMessage()
msg['Subject']="Resume in pdf format"
msg["From"]=email_address
msg["To"]="hello@gmail.com"
msg.set_content("Resume Attached....")

files=["resume.pdf"]

for file in files:
	with open(file,"rb") as f:
		file_data=f.read()

		file_name=f.name
	msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)	

	   	    
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	
	smtp.login(email_address,email_password)
	smtp.send_message(msg)

