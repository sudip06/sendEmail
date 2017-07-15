# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:33:43 2017

@author: sudip
"""

import smtplib
import email
import string
import getpass

from validate_email import validate_email

def loginidParse(loginidStr):
    return loginidStr.split("@")[0]
    
validOptions=("first","login","pass","message","destaddr")

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
contextChanged = "first"
while 1:
    if contextChanged != "n":
        try:
            if(contextChanged.lower()=="login" or contextChanged =="first"): loginid=loginidParse(raw_input("Enter your login:"))
            if(contextChanged.lower()=="pass" or contextChanged =="first"): password=getpass.getpass("Enter the password:")
            if(contextChanged.lower()=="message" or contextChanged =="first"): msg=raw_input("Enter the message:")
            if(contextChanged.lower()=="destaddr" or contextChanged =="first"): destinationMailid=raw_input("Destination mail id:") 
            if contextChanged.lower() not in validOptions:
		print ("Invalid entry, retry")
                contextChanged=raw_input("Which one do you wish(login/pass/message/destaddr) to correct?")
		continue
            input=raw_input("Correct(Y/N)?")
            if input.lower() == "y":            
                server.login(loginid+"@gmail.com",password)
                server.sendmail(destinationMailid, loginid+"@gmail.com",msg)
            else:
                contextChanged=raw_input("Which one do you wish(login/pass/message/destaddr) to correct?")
                continue
        except smtplib.SMTPAuthenticationError:
            print "Enter the credentials correctly"
            contextChanged="p"            
            continue
    break


server.quit()   



