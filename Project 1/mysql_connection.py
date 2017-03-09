import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()

cur.execute("SHOW TABLES")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()