# automailer (withoutdb)
Python script to automate email sending without using db connection.


This is a script which usses YAHOO SMTP server to send automatic emails to the emails listed in the database.
**You can also use GMAIL SMTP server .. replace the host and port number or any mail server**


**Update: Now the email-body can be pulled from text file.**

**update: Email list will be fetched by emails.txt file where email id is seperated by ';'
STEPS:

1. put email body in email-body.txt and email id list in emails.txt

5. (For yahoo user only)Yahoo uses special app password to authenticate your login. For this go to https://edit.yahoo.com/config/eval_asp and create an app specific password using app PYTHON. The replace you password in the main function of the automailer.py file.

6. update EMAIL_SENDER with your own email in globalvar.py

7. Now you can run the scirpt automailer.py.

8. First enter the Subject of Email.

9. Then you should call the main function to send the msg.
    e.g main()
    
10. ALL DONE!!.. 
