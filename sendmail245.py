#!/usr/bin/env python

# Email notification
# Contributor:
#      pseudokool           <pseudokool@gmail.com>

#!/usr/bin/env python

# Email notification
# Contributor:
#      pseudokool           <pseudokool@gmail.com>

import config
import smtplib
#from email.mime.text import MIMEText
#from email.MIMEMultipart import MIMEMultipart
#from email.header import Header
#from email.utils import formataddr


class SendMail:
    def __init__(self, to, subject, msg):
        self.server = smtplib.SMTP()
        self.server.set_debuglevel(True)
        self.smtp_username = config.app_config['smtp_username']
        self.smtp_password = config.app_config['smtp_password']
        # address setup
        print msg
        self.email_to = to
        self.email_from = config.app_config['from_email']
        # email body
        # email body
        self.email_msg = "\r\n".join([
  "From: " + config.app_config['from_name'] + " <" + config.app_config['from_email'] + ">",
  "To: " + config.app_config['to_email'],
  "Subject: " + subject,
  "",
  msg
  ])

        
    def do_send(self):
        print 'do_send'
        # initialize smtp
        self.server.connect(config.app_config['smtp_host'])
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.smtp_username, self.smtp_password)
        self.server.sendmail(self.email_from, self.email_to, self.email_msg)
        self.server.quit()