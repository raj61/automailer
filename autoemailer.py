#!/usr/bin/python
from smtplib import SMTP
from smtplib import SMTP_SSL
from smtplib import SMTPException
from email.mime.text import MIMEText
import sys
import MySQLdb

def getemail():
    alist=[]
    # Open database connection Replace username, password with your username password and dbname with the name of database
    db = MySQLdb.connect("localhost","username","password","dbname" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #replace emails with your table name containing a column 'email' holding the email addresses
    sql = "SELECT * FROM emails"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          alist.append(row['email'])
      
    except:
       print "Error: unable to fecth data"
   

    # disconnect from server
    db.close()
    return alist


#Global varialbes
#EMAIL_SUBJECT = "Email from Python script"
print 'Enter Subject'
EMAIL_SUBJECT=str(raw_input())
#replace abc@yahoo.com with your yahoo email id
EMAIL_SENDER  =  'abc@yahoo.com'
TEXT_SUBTYPE = "plain"
 
YAHOO_SMTP = "smtp.mail.yahoo.com"
YAHOO_SMTP_PORT = 465
 
def listToStr(lst):
    """This method makes comma separated list item string"""
    return ','.join(lst)
 
def send_email(content, pswd, emailr):
    """This method sends an email"""
    msg = MIMEText(content, TEXT_SUBTYPE)
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_SENDER
    msg["To"] = listToStr(emailr)
     
    try:
      #Yahoo allows SMTP connection over SSL. 
      smtpObj = SMTP_SSL(YAHOO_SMTP, YAHOO_SMTP_PORT)
      #If SMTP_SSL is used then ehlo and starttls call are not required.
      smtpObj.login(user=EMAIL_SENDER, password=pswd)
      smtpObj.sendmail(EMAIL_SENDER, emailr, msg.as_string())
      smtpObj.quit();
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)
 
def main(content):
    """This is a simple main() function which demonstrates sending of email using smtplib."""
    #replace yourapppassword with your own yahoo app password . Refer Readme for more information.
    pswd='yourapppassword'
    li=getemail()
    send_email(content, pswd, li);
 
if __name__ == "__main__":
    """If this script is executed as stand alone then call main() function."""
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Please provide message using main('message')"
        sys.exit(0)
