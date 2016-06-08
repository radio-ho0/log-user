#!/usr/bin/python

import MySQLdb 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
first_name = form.getvalue('first_name')
phone_num  = form.getvalue('phone_num')

# Get data from fields

print "Content-type:text/html\r\n\r\n"
print ""
print "<html>"
print "<head>"
print "<title>Hello - This is Robert speaking !!!</title>"
print "</head>"
print "<body>"
print "<h2>Welcome %s - %s</h2>" % (first_name, phone_num)
print "</body>"
print "</html>"


print "<!--"

def insertName( name, phone ):
    con = MySQLdb.connect("localhost", "testuser", "test623", "testdb")
    with con :
        cur = con.cursor()
        #cur.execute("create table if not exists log(id int primary key auto_increment, name varchar(32), phone varchar(32))")
        sql = "insert into log(name, phone) values( '%s', '%s' )" % (name , phone)
        cur.execute(sql)

insertName(first_name, phone_num)

print " -->"
