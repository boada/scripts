#!/usr/bin/python

import smtplib

sender = 'boada@physics.tamu.edu'
receivers = ['boada@physics.tamu.edu',
        'papovich@physics.tamu.edu',
        'vy@physics.tamu.edu',
        'freeland@physics.tamu.edu',
        'pellerin@physics.tamu.edu',
        'tilvi@physics.tamu.edu',
        'sheerfox@gmail.com',
        'bsalmon925@gmail.com',
        'heath.shipley@tamu.edu',
        'jimmy@physics.tamu.edu',
        'kyle.cook@tamu.edu']

message = """From: Galaxy Group Lunch <boada@physics.tamu.edu>
To: Galaxy Group <boada@physics.tamu.edu>
Subject: Galaxy Group Lunch

This is a friendly remind that we'll be eating together on Thursday, from noon
to 1pm. The lunch will be better with you there.

Replying to this email does not reply to the entire group.
"""

try:
   smtpObj = smtplib.SMTP('smtp.physics.tamu.edu:25')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
