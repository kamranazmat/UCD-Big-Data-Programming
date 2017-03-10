import MySQLdb
import pandas as pd
import numpy as np
import json
import os

os.chdir('..')
PATH = os.getcwd()
# os.makedirs('json')

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()
table = "comp_cast_type"

query = "DESCRIBE " + str(table)
cur.execute(query)
index = []
for row in cur.fetchall():
    index.append(str(row[0]))

# query = "SELECT * FROM " + str(table) + " LIMIT 100"
query = "SELECT * FROM " + str(table)
cur.execute(query)

data = []
for row in cur.fetchall():
	print row
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
name = PATH + "/json/" + str(table) + ".json" # "datas/" + 
f = open(name, 'w+')	# '+' to create the file first
f.write(data)
f.close()

db.close()
