import sys
import MySQLdb
import mysql.connector


person = input('Which Customer Would You Like To Look Up?: ')
con = mysql.connector.connect(user='root',password='root',database='classicmodels')

cursor = con.cursor()
args =(person,)
holder = False
cursor.callproc('function_1',args)
for result in cursor.stored_results():
    row = result.fetchone()
    while row is not None:
        if holder == False:
                print "Showing Orders for Customer#: ",row[0],"Customer Name:",row[1]
                print row[2],row[3],row[4]
                holder = True
                row = result.fetchone()
        elif holder != False:
                print row[3],row[4]
                row = result.fetchone()
~                                                                                                                                                                                                         
~                                                                                                                                                                                                         
~                                                                                                                                                                                                         
~                                                   