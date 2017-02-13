import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'Creolop@zhi.com'
receivers = ['']

message = MIMEText('Python email sending test...','plain','utf-8')
message['From'] = Header("Creolop",'utf-8')
message['To'] = Header('Testing','utf-8')

subject = "Python SMTP testing"
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('success')
except smtplib.SMTPException as e:
    print('fail')
