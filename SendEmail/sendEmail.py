# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:33:43 2017

@author: sudip
"""

import smtplib
import email
import getpass
import sys
import os

from validate_email import validate_email

class mailMsg:
    def __init__(self):
        self.contextChanged="first"
        self.loginid=""
        self.password=""
        self.message=""
        self.destaddr=""
    def loginidParse(self, loginidStr):
        return loginidStr.split("@")[0]
    
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
        print "Message:",self.message

validOptions=("first","login","pass","message","destaddr")

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
except Exception as e:
    print "",e
    print "Exiting"
    os.sys.exit(1)    


mailMsg1=mailMsg()

while 1:
    if mailMsg1.contextChanged != "n":
        if(mailMsg1.contextChanged.lower()=="login" or \
            mailMsg1.contextChanged =="first"): \
            mailMsg1.loginid=mailMsg1.loginidParse(raw_input("Enter your gmail loginid:"))

        if(mailMsg1.contextChanged.lower()=="pass" or mailMsg1.contextChanged =="first"): \
            mailMsg1.password=getpass.getpass("Enter the password:")

        if(mailMsg1.contextChanged.lower()=="message" or mailMsg1.contextChanged =="first"): \
            mailMsg1.message=mailMsg1.msgParse()

        if(mailMsg1.contextChanged.lower()=="destaddr" or mailMsg1.contextChanged =="first"): \
            mailMsg1.destaddr =raw_input("Destination mail id:")

        if mailMsg1.contextChanged.lower() not in validOptions:
            print ("Invalid entry, retry")
            contextChanged=raw_input("Which one do you wish(login/pass/message/destaddr) to correct?")
            continue

        mailMsg1.showDetails()
        input=raw_input("Correct(Y/N)?")

        try:
            if input.lower() != "n":            
                server.login(mailMsg1.loginid+"@gmail.com",mailMsg1.password)
                server.sendmail(mailMsg1.destaddr , mailMsg1.loginid+"@gmail.com",mailMsg1.message)
            else:
                mailMsg1.contextChanged=raw_input("Which one do you wish(login/pass/message/destaddr) to correct?")
                continue
        except smtplib.SMTPAuthenticationError:
            print "Enter the credentials correctly"
            mailMsg1.contextChanged="pass"
            continue
    break
server.quit()
