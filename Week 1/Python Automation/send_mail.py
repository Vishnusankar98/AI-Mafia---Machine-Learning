import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():
    sender_address="sender_email_address"
    password=getpass.getpass()
    subject="Learn.Inspire.Grow"
    msg="""
        Hello Everyone!
        This is a test program to demonstrate automation in python.
        
        ThankYou
        
    """

    #server initialisation
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_address,password)

    #drafting message body
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']='receipient_email_address'
    receipients='receipient_email_address'

    server.sendmail(sender_address,receipients,msg.as_string())

send_email()

