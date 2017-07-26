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
import json
import readline 
import collections 

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

savedFile="/tmp/savedData.json"
dataStr=collections.defaultdict(lambda:'x')  #data string loaded from savedFile
#from validate_email import validate_email

lst=[]#to hold logins and destination address for readline to process

def formList(data,isDict):
    listRet=[]
    if isDict==True:
        for key in data.keys():
                listRet.append(key)
        return listRet
    else:
        return data

def completer(text, state):
    options = [x for x in lst if x.startswith(text)]
    try:
        return options[state]
    
    except IndexError:
        return None


def loadDataFromFile():
    dataStr1=""
    if os.path.isfile(savedFile):
        with open(savedFile) as data_file:    
            try:
                data = json.load(data_file)
                dataStr1=json.loads(data)
            except ValueError:
                print "some exceptional error has happened"
                sys.exit(1)
    return dataStr1

def dumpData(loginid, passwd, destAddr):
    if os.path.isfile(savedFile):
        dataStr["credentials"][loginid]=passwd
        if destAddr not in dataStr["destAddr"]:
            dataStr["destAddr"].append(destAddr)
    else:
        #dataStr.({"credentials":{},"destAddr":[]})
        dataStr["credentials"]={}
        dataStr["destAddr"]=[]
        dataStr["credentials"][loginid]=passwd
        dataStr["destAddr"]=dataStr["destAddr"]+[destAddr]
    json_data=json.dumps(dataStr)
    with open(savedFile, 'w') as outfile:
        json.dump(json_data, outfile)

class mailMsg:
    def __init__(self):
        self.contextChanged="first"
        self.loginid=""
        self.password=""
        self.message=""
        self.subject=""
        self.destaddr=""

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


if os.path.isfile(savedFile):
    dataStr=loadDataFromFile()
validOptions=("first","login","pass","message","sub","destaddr")

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
            mailMsg1.contextChanged =="first"):
            readline.set_completer(completer)
            readline.parse_and_bind("tab: complete")
            if any(dataStr):lst=formList(dataStr["credentials"],1) 
            mailMsg1.loginid=raw_input("Enter your gmail login:")

        if(mailMsg1.contextChanged.lower()=="pass" or mailMsg1.contextChanged =="first"):
            if not any(dataStr) or mailMsg1.contextChanged.lower()=="pass" or \
                mailMsg1.loginid not in dataStr["credentials"]:
                mailMsg1.password=raw_input("Enter the password:")
            else:
                mailMsg1.password=dataStr["credentials"][mailMsg1.loginid]
                print "Password found for the account:",mailMsg1.loginid

        if any(dataStr):lst=formList(dataStr["destAddr"],0) 
        if(mailMsg1.contextChanged.lower()=="destaddr" or mailMsg1.contextChanged =="first"):
            mailMsg1.destaddr=raw_input("Destination mail id:")

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

                dumpData(mailMsg1.loginid, mailMsg1.password, mailMsg1.destaddr)

            else:
                mailMsg1.contextChanged=raw_input("Which one do you wish(login/pass/message/sub/destaddr) to correct?")
                continue
        except smtplib.SMTPAuthenticationError:
            print "Enter the credentials correctly for:",mailMsg1.loginid,mailMsg1.password
            mailMsg1.contextChanged="pass"
            continue
    break
server.quit()
