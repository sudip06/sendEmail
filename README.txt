===========
Send Email
===========

SendEmail lets you sending an email from command prompt(from gmail account)
using smtpLib and Email package. Presently, it supports to send email from your
gmail account to any account.

Salient Features
================
(1) This module also does sanity check and allows user to correct any part of email
before sending the email. Useful for somebody not opening browser to send a quick
email.
(2) The application retrieves data from last session(saved in /tmp/savedData.pickle
file). Hence the user must have read/write access to the said partition or else
should change the location accordingly.

It has been implemented by using python 2.7

Testing
=======
SendEmail$ python ./sendEmail.py
Enter your gmail login():XXXXXXX@gmail.com
Enter the password():XXXXXX
Destination mail id():XXXXXXXXX@gmail.com
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


Limitation:
==========
(1)The password is seen when its retrieved from last session.
Checking if thats possible to replace by asterisks.
(2)More strict sanity check on email address should be done.

Authors
  - Sudip Midya
