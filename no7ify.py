#!/usr/bin/env python

# Email notification
# Contributor:
#      pseudokool           <pseudokool@gmail.com>

__version__ = '1.0'

import config
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


# address setup
email_to = config.app_config['to_email']
email_from = formataddr((str(Header(config.app_config['from_name'], 'utf-8')), config.app_config['from_email']))

# email body
email_msg = MIMEText('Drink now!')
#email_msg = MIMEMultipart('alt')
email_msg['From'] = email_from
email_msg['Subject'] = 'Booh! Sip Sip Sip.'


# smtp credentials
smtp_username = config.app_config['smtp_username']
smtp_password = config.app_config['smtp_password']

# initialize smtp
server = smtplib.SMTP(config.app_config['smtp_host'])
server.starttls()
server.login(smtp_username,smtp_password)
server.sendmail(email_from,email_to,email_msg.as_string())
server.quit()