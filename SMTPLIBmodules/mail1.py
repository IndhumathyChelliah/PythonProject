import os

import smtplib

email_address=os.environ.get("email_user")
email_password=os.environ.get("email_pass")

with smtplib.SMTP('localhost',1025) as smtp:

	

	subject="Hello Welcome to Python"

	body="I love to learn Pyhton"

	msg=f"Subject:{subject}\n\n{body}"

	smtp.sendmail(email_address,"hello@gmail.com",msg)

