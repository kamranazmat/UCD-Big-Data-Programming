import MySQLdb
import json
# import os
import ast
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()
table = "cast_info"

query = "DESCRIBE " + str(table)
cur.execute(query)

index = []
for row in cur.fetchall():
    index.append(str(row[0]))

# query = "SELECT * FROM " + str(table) + " LIMIT 100"
START = 0
END = 100000
# 57200000
count = 0
while True:	
	# query = "SELECT * FROM " + str(table) + "WHERE id >" + str(START) + " AND id <" + str(END)
	if count > 57153103:
		break

	query = "SELECT * FROM " + str(table) + " WHERE id > " + str(START) + " AND id < " + str(END)
	cur.execute(query)

	db = client['imdb']
	collection = db[table]

	data = []
	for row in cur.fetchall():
		count += 1
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
	START += 100000
	END += 100000