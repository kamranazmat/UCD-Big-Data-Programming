import ast

json = "comp_cast_type"
PATH = "../../json/" + json + ".json"

with open(PATH, 'r') as f:
	data = ast.literal_eval(f.read())

f.close()

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

db = client['imdb']
collection = db[json]

for doc in data:
	print type(doc)
	# collection.insert_one(doc)
