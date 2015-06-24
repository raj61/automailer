#!/usr/bin/python
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
