#!/usr/bin/python
from smtplib import SMTP
from smtplib import SMTP_SSL
from smtplib import SMTPException
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from email import encoders
import sys
from database import getemail
from globalvar import EMAIL_SUBJECT
from globalvar import EMAIL_SENDER
from globalvar import TEXT_SUBTYPE
from globalvar import YAHOO_SMTP
from globalvar import YAHOO_SMTP_PORT


 
def listToStr(lst):
    """This method makes comma separated list item string"""
    return ','.join(lst)
 
def send_email(pswd, emailr):
    #set attachement and body and attachement
    COMMASPACE = ', '	
    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_SENDER
    msg['To'] = COMMASPACE.join(emailr)
    body = MIMEMultipart('alternative')
    #attach body of email from email-body.txt
    body.attach(MIMEText(file("email-body.txt").read(), 'plain'))

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<br><img src="cid:image1"><br>', 'html')
    body.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('test.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    
    msg.attach(body)
    #replace filename with your filename and data to the address of attacments
    attachments=[{'filename' : 'pdf.pdf', 'data' : file("pdf.pdf").read()},
                {'filename' : 'email-body.txt', 'data' : file("email-body.txt").read()}]
    for attachment in attachments:
	    if attachment['filename'].find('doc') > 0:
		    attachFile = MIMEBase('application', 'msword')     
	    elif attachment['filename'].find('pdf') > 0:
		    attachFile = MIMEBase('application', 'pdf')	
	    else:
		    attachFile = MIMEBase('application', 'octet-stream')    
		
	    attachFile.set_payload(attachment['data'])
		
	    encoders.encode_base64(attachFile)
	    attachFile.add_header('Content-Disposition', 'attachment', filename=attachment['filename'])
		
	    msg.attach(attachFile);

       
    try:
      #Yahoo allows SMTP connection over SSL. 
      smtpObj = SMTP_SSL(YAHOO_SMTP, YAHOO_SMTP_PORT)
      #If SMTP_SSL is used then ehlo and starttls call are not required.
      smtpObj.login(user=EMAIL_SENDER, password=pswd)
      smtpObj.sendmail(EMAIL_SENDER, emailr, msg.as_string())
      smtpObj.quit();
      print 'Email succesfully sent.'
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)
 
def main():
    """This is a simple main() function which demonstrates sending of email using smtplib."""
    #replace yourapppassword with your own yahoo app password . Refer Readme for more information.
    pswd='yourapppassword'
    li=getemail()
    send_email(pswd, li);
 
if __name__ == "__main__":
    """If this script is executed as stand alone then call main() function."""
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "call main() to send email"
        sys.exit(0)
