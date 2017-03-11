import ast

json = "role_type"
PATH = "../../json/" + json + ".json"

f = open(PATH, 'r')
# with open(PATH, 'r') as f:
# 	data = ast.literal_eval(f.read())

# f.close()

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

db = client['imdb']
collection = db[json]

for doc in ast.literal_eval(f.read()):
	print doc
	collection.insert_one(doc)
