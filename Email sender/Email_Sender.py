from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'arjun.191405@ncit.edu.np'
email_password = 'Web&Developer191405@'

email_receiver = 'arjunuchai1234@gmail.com'
subject = 'Email Testing'
body = """
Hello buddy
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


