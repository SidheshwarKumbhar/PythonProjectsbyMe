"""-----------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------"""

# !/usr/bin/python3
import smtplib

sender_mail = 'sidheshwarkumbhar7894@gmail.com'
receivers_mail = ['sidheshwarkumnhar7894@gmail.com']
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""
try:
    password = 'cmuyifochdyqhoaf'
    smtpobj = smtplib.SMTP('gmail.com', 587)
    smtpobj.login(sender_mail, password)
    smtpobj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception as e:
    raise Exception("Error: unable to send email", e)
