#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Send mail to a .csv list of users, with contents from message.txt
"""

import csv
import time
import smtplib
from email.mime.text import MIMEText

sender = 'mail-from@address.here'
subject = 'RSI 30th Anniversary / Alumni Capital Campaign Participation / {name}'
message = open('message.txt').read()

print("Connecting to gmail...")
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo
print("Authenticating...")
session.login(sender, open('.temporary-password').readline())


print("Parsing recipient list...")
recipient_list = []
with open('mail-list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        recipient_list.append(row)
# recipient_list = [('Nick Semenkovich', 'some-test-email@domain.com', '2004')]


print("Sending mail to %s recipients." % (len(recipient_list)))

for recipient_name, recipient_email, year in recipient_list:
    print("\t %s, %s, %s" % (recipient_name, recipient_email, year))
    headers = ["From: Nick Semenkovich <" + sender + ">",
               "Subject: " + subject.format(name=recipient_name),
               "To: " + recipient_name + " <" + recipient_email + ">",
               "MIME-Version: 1.0",
               "Content-Type: text/plain"]
    headers = "\r\n".join(headers)
    session.sendmail(sender, recipient_email, headers + "\r\n\r\n" + message.format(year=year))
    time.sleep(1)

print("All done!")

