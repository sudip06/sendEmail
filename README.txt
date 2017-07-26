===========
Send Email
===========

SendEmail lets you sending an email from command prompt(from gmail account)
using smtpLib and Email package. It saves the recipents address, login 
credentials in file system and helps the user in predicting the recipent and
as well as filling up the credentials. Pretty useful when one feels to send 
emails not using the browser. Presently, it supports to send email from your
gmail account to any account.

Salient Features
================
(1) This module also does sanity check and allows user to correct any part
of email before sending the email. Useful for somebody not opening browser
to send a quick email.

(2) The application saves new data in json format along with the existing
data about accounts and senders in /tmp/savedData.json file. While executing,
it helps the user in autocompletion of destination address and login credentials
by using readline package. The user must have read/write access to the said
partition or else should change the location accordingly.

Earlier we were saving the data in pickle, but later on figured that not only previous sessions data,
but all previous successful data should be saved and json seemed very appropriate for the same.

(3) Developed using classes, dictionary objects, lists, readline, autocompleation
feature.

It has been implemented by using python 2.7

P.S
===
Not able to send any mail to gmail as gmail employs reverse DNS to check
spammers :( thus blocking out legitimate ones also except sending mails
to the same account from which the mail is being sent. Trying to figure
out other ways.

Testing
=======
SendEmail$ python ./sendEmail.py
Enter your gmail login:XXXXXXX@gmail.com
Enter the password:XXXXXX
Destination mail id:XXXXXXXXX@gmail.com
Subject:hello, test
Enter Message, end with ^D on a new line:
This is a test email.
Now, I will end here.

Loginid: XXXXXXX@gmail.com
DestAddr: XXXXXXX@gmail.com
Subject: hello, test
Message: This is a test email.
Now, I will end here.

Correct(Y/N)?n
Which one do you wish(login/pass/message/sub/destaddr) to correct?sub
Subject:Test Email

Loginid: XXXXXXX@gmail.com
DestAddr: XXXXXXX@gmail.com
Subject: Test Email
Message: This is a test email.
Now, I will end here.

Correct(Y/N)?y
SendEmail$

Scenario 2:
==========

Enter your gmail login:XXXXXXXXX@gmail.com
Password found for the account: XXXXXXXX@gmail.com
Destination mail id:XXXXXXXX@gmail.com
Subject:hello
Enter Message, end with ^D on a new line:
Hi,         
this is test email.

Loginid: XXXXXXXXX@gmail.com
DestAddr: XXXXXXXXX@gmail.com
Subject: hello
Message: Hi,
this is test email.

Correct(Y/N)?y
SendEmail$

Limitation:
==========
(1)The password is seen when its retrieved from last session.
Checking if thats possible to replace by asterisks.
(2)More strict sanity check on email address should be done.

Authors
  - Sudip Midya
