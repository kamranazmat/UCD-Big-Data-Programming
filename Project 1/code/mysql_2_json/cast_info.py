import MySQLdb
import pandas as pd
import numpy as np
import json
import os
import datetime

os.chdir('..')
PATH = os.getcwd()
# os.makedirs('json')

a = datetime.datetime.now()

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

b = datetime.datetime.now()
print b - a

cur = db.cursor()
table = "cast_info"

query = "DESCRIBE " + str(table)
cur.execute(query)
index = []
for row in cur.fetchall():
    index.append(str(row[0]))

print datetime.datetime.now()

# query = "SELECT * FROM " + str(table) + " LIMIT 100"
query = "SELECT * FROM " + str(table)
cur.execute(query)

print datetime.datetime.now()
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

print datetime.datetime.now()

data = json.dumps(data, encoding='latin1')
print datetime.datetime.now()
name = PATH + "/json/" + str(table) + ".json" # "datas/" + 
f = open(name, 'w+')	# '+' to create the file first
f.write(data)
f.close()

db.close()
