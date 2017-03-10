import ast
with open("title.txt", 'r') as f:
	data = ast.literal_eval(f.read())

f.close()

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

db = client['test']
collection = db['title']

for doc in data:
	collection.insert_one(doc)
