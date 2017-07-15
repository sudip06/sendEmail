# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:33:43 2017

@author: Sudip Midya
"""

import smtplib
import email
import getpass
import sys
import os
import pickle

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from validate_email import validate_email

class mailMsg:
    def __init__(self):
        self.contextChanged="first"
        self.loginid=""
        self.password=""
        self.message=""
        self.subject=""
        self.destaddr=""

    def retrieveVal(self, savedStr, newStr):
        if newStr !='':
            #return loginidStr.split("@")[0]
            return newStr
        else:
            return savedStr


    def formMessage(self):
        msg=MIMEMultipart()
        msg['Subject']=mailMsg1.subject
        msg['From']=mailMsg1.loginid
        msg['To']=mailMsg1.destaddr
        msg.attach(MIMEText(mailMsg1.message, 'plain'))
        return msg

    def msgParse(self):
        print "Enter Message, end with ^D on a new line:"
        msg=""
        while True:
            input_=sys.stdin.readline()
            if input_=='':
                break
            else:   msg=msg+input_
        return msg

    def showDetails(self):
        print "\nLoginid:",self.loginid
        print "DestAddr:",self.destaddr
        print "Subject:",self.subject
        print "Message:",self.message

validOptions=("first","login","pass","message","sub","destaddr")

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
except Exception as e:
    print "",e
    print "Exiting"
    os.sys.exit(1)    

mailMsg1=mailMsg()

if os.path.isfile('/tmp/savedData.pickle'):
    with open('/tmp/savedData.pickle') as f:
        mailMsg1.loginid, mailMsg1.password, mailMsg1.destaddr=pickle.load(f)

while 1:
    if mailMsg1.contextChanged != "n":
        if(mailMsg1.contextChanged.lower()=="login" or \
            mailMsg1.contextChanged =="first"): \
            mailMsg1.loginid=mailMsg1.retrieveVal(mailMsg1.loginid, raw_input("Enter your gmail login("+mailMsg1.loginid+"):"))

        if(mailMsg1.contextChanged.lower()=="pass" or mailMsg1.contextChanged =="first"): \
            mailMsg1.password=mailMsg1.retrieveVal(mailMsg1.password, raw_input("Enter the password("+mailMsg1.password+"):"))

        if(mailMsg1.contextChanged.lower()=="destaddr" or mailMsg1.contextChanged =="first"): \
            mailMsg1.destaddr=mailMsg1.retrieveVal(mailMsg1.destaddr, raw_input("Destination mail id("+mailMsg1.destaddr+"):"))

        if(mailMsg1.contextChanged.lower()=="sub" or mailMsg1.contextChanged =="first"): \
            mailMsg1.subject=raw_input("Subject:")

        if(mailMsg1.contextChanged.lower()=="message" or mailMsg1.contextChanged =="first"): \
            mailMsg1.message=mailMsg1.msgParse()

        if mailMsg1.contextChanged.lower() not in validOptions:
            print ("Invalid entry, retry")
            mailMsg1.contextChanged=raw_input("Which one do you wish(login/pass/message/sub/destaddr) to correct?")
            continue

        mailMsg1.showDetails()
        input=raw_input("Correct(Y/N)?")

        try:
            if input.lower() == "y":
                server.login(mailMsg1.loginid,mailMsg1.password)
                msg=mailMsg1.formMessage()
                server.sendmail(mailMsg1.destaddr , mailMsg1.loginid, msg.as_string())

                with open('/tmp/savedData.pickle','w') as f:
                    pickle.dump([mailMsg1.loginid, mailMsg1.password, mailMsg1.destaddr],f)

            else:
                mailMsg1.contextChanged=raw_input("Which one do you wish(login/pass/message/sub/destaddr) to correct?")
                continue
        except smtplib.SMTPAuthenticationError:
            print "Enter the credentials correctly"
            mailMsg1.contextChanged="pass"
            continue
    break
server.quit()
