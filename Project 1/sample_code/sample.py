# import MySQLdb

# db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                      user="root",       # your username
#                      passwd="",  		# your password
#                      db="scott")        # name of the data base

# cur = db.cursor()

# cur.execute("SELECT * FROM EMPLOYEE")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print list(row)

# db.close()

import os



import datetime
a = datetime.datetime.now()
print "loading ....."
b = datetime.datetime.now()

print "Time:", (b - a)
i = 0

while i < 57153103:
	print i
	i += 100000