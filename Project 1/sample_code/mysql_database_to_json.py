import MySQLdb
import pandas as pd
import numpy as np
import json

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()
# cur.execute("DESCRIBE aka_title")
cur.execute("SHOW TABLES")

tables = []
for table in cur.fetchall():
    tables.append(str(table[0]))

for table in tables:
	query = "DESCRIBE " + str(table)
	cur.execute(query)
	index = []
	for row in cur.fetchall():
	    index.append(str(row[0]))
	
	query = "SELECT * FROM " + str(table) + " LIMIT 100"
	cur.execute(query)

	data = []
	for row in cur.fetchall():
		temp_json = {}
		for i in range(len(index)):
			if index[i] == 'md5sum':
				continue

			if type(row[i]) == type(None):
				temp_json[index[i]] = 0
			elif type(row[i]) == type(5L):
				temp_json[index[i]] = int(row[i])
			else:
				temp_json[index[i]] = row[i]
		data.append(temp_json)

	data = json.dumps(data, encoding='latin1')
	name = "json/" + str(table) + ".txt" # "datas/" + 
	f = open(name, 'w+')	# '+' to create the file first
	f.write(data)
	f.close()

db.close()
