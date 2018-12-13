#!/usr/bin/python
import time
import smtplib
from datetime import date

fromaddr = 'excursion.house@gmail.com'
username = 'excursion.house@gmail.com'
password = '*******'

#connect with smtp to send emails
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)

with open('/home/blake/excursion/yassine/gearCountEmailMsg.txt', 'r') as content_file:
    msg = content_file.read()

	
with open('/home/blake/excursion/yassine/gearcountdays.txt','r') as content_file:
    toaddrs = content_file.readlines()[date.today().weekday()]

server.sendmail(fromaddr, toaddrs, msg)
server.quit()

