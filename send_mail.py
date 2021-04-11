import smtplib
# from email.message import EmailMessage
from email.mime.text import MIMEText

server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)


def send_mail(recipient, subject, body):
    # port = 465
    # smtp_server = 'smtp.gmail.com'
    login = 'flaskreminder@gmail.com'
    password = 'developersinstitute123'
    message = body
    sender_email = 'flaskreminder@gmail.com'
    receiver_email = recipient
    msg = MIMEText(message, 'html')
    msg['Subject'] = str(subject)
    msg['From'] = 'flaskreminder@gmail.com'
    msg['To'] = recipient
    # with smtplib.SMTP(smtp_server, port) as server:
    server_ssl1 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl1.login(login, password)
    server_ssl1.sendmail(sender_email, receiver_email, msg.as_string())
