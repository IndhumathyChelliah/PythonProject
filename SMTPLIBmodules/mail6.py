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
msg.set_content("This is a plain text email")
msg.add_alternative("""\
	<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>""",subtype='html')
	

	   	    
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	
	smtp.login(email_address,email_password)
	smtp.send_message(msg)

