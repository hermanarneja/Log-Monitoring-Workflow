import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'monitor@turnanewleaf.org'
    msg['To'] = 'manager@turnanewleaf.org'
    msg['Subject'] = subject
    msg.attach(MIMEText(body))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('monitor@turnanewleaf.org', 'password')
    server.send_message(msg)
    server.quit()

def analyze_logs():
    with open('/var/log/auth.log') as f:
        contents = f.read()
        
    failed_logins = contents.count('Failed password')
    
    if failed_logins > 10:
        send_email('Unusual number of failed logins detected',
                   f'An unusual number of failed logins ({failed_logins}) have been detected on the server.')

analyze_logs()
