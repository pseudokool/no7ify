#!/usr/bin/env python

# Email notification
# Contributor:
#      pseudokool           <pseudokool@gmail.com>

__version__ = '1.0'

import sys
import config
import datetime
from random import randrange
from sendmail245 import SendMail

now = datetime.datetime.now()
#print now

# Randomly pick mail body content
def pick_line(seq):
    if( seq=='even'):
        return config.msg_collection[randrange(len(config.msg_collection))]   
    else:
        return config.msg_collection[randrange(len(config.msg_collection))]
            

# Only notify between 9am and 11pm, different subject lines for odd and even hours+days            
if( now.hour<9 and now.hour>23 ):
    sys.exit()
else:    
    if( now.hour%2==0 and now.day%2==0 ):
       print 'SEQ_E'
       msg =  pick_line('even')
       subject = "Now is a good time to drink!"
       no7ify = SendMail(config.app_config['to_email'],subject,msg)
       no7ify.do_send()
    elif( now.hour%2>0 and now.day%2>0 ):
       print 'SEQ_O'
       msg = pick_line('odd')
       subject = "It\'s time to sip on some water!"
       no7ify = SendMail(config.app_config['to_email'],subject,msg)
       no7ify.do_send()
    else:
        print 'Inappropriate time to no7ify!'