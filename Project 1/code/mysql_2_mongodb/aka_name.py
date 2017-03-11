import MySQLdb
import json
# import os
import ast
import datetime
from pymongo import MongoClient

a = datetime.datetime.now()
client = MongoClient("mongodb://localhost:27017")

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()
table = "aka_name"

query = "DESCRIBE " + str(table)
cur.execute(query)

index = []
for row in cur.fetchall():
    index.append(str(row[0]))

# query = "SELECT * FROM " + str(table) + " LIMIT 100"
query = "SELECT * FROM " + str(table)
cur.execute(query)


db = client['imdb']
collection = db[table]

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
	val = ast.literal_eval(json.dumps(temp_json, encoding='latin1'))
	print val
	# print ast.literal_eval(json.dumps(temp_json, ensure_ascii=False))
	collection.insert_one(val)

b = datetime.datetime.now()
print "Total time: ", (b - a) 