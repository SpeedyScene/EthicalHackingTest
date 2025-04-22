import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

email_list = ["alipps6915@floridapoly.edu", "klawrence4621@floridapoly.edu", "kwalden0969@floridapoly.edu"]
with open("./working.html", 'rb') as file:
    message = MIMEMultipart()
    message["From"] = "info47522techsuppport@gmail.com"
    message["To"] = COMMASPACE.join(email_list)
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = "Google security alert"
    part = MIMEBase('application', "octet-stream")
    part.set_payload(file.read())
    message.attach(part)
    file.close()

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.connect("smtp.gmail.com", 587)
smtp.starttls()
smtp.login("info47522techsuppport@gmail.com", "ABCd1234!")
smtp.sendmail(message["From"], message["To"], message)
smtp.quit()
