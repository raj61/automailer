# automailer
Python script to automate email sending using MySQL database connection


This is a script which usses YAHOO SMPT server to send automatic emails to the emails listed in the database.
**You can also use GMAIL SMPT server .. replace the host and port number**

STEPS:

1. Create a database and replace the name with dbname in the autoemailer.py file.
 
2. create emails table having min. two column id and email.

3. insert some row in the database.(Emails id).

4. Replace the username and password with your own database username and password in the database connection in autoemailer.py file.

5. Yahoo uses special app password to authenticate your login. For this go to https://edit.yahoo.com/config/eval_asp and create an app specific password using app PYTHON. The replace you password in the main function of the automailer.py file.

6. Now you can run the scirpt.

7. First enter the Subject of Email.

8. Then you should call the main function with your message.
    e.g main("HELLO WORLD!")
    
9. ALL DONE!!.. 
