#!/usr/bin/env python

# Email notification
# Contributor:
#      pseudokool           <pseudokool@gmail.com>

import config
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


class SendMail:
    def __init__(self, to, subject, msg):
        self.server = smtplib.SMTP(config.app_config['smtp_host'])
        self.server.set_debuglevel(True)
        self.smtp_username = config.app_config['smtp_username']
        self.smtp_password = config.app_config['smtp_password']
        # address setup
        self.email_to = to
        self.email_from = formataddr((str(Header(config.app_config['from_name'], 'utf-8')), config.app_config['from_email']))
        # email body
        self.email_msg = MIMEText(msg)
        self.email_msg['From'] = self.email_from
        self.email_msg['Subject'] = subject

    def do_send(self):
        print 'do_send'
        # initialize smtp
        self.server.starttls()
        self.server.login(self.smtp_username, self.smtp_password)
        self.server.sendmail(self.email_from, self.email_to, self.email_msg.as_string())
        self.server.quit()
