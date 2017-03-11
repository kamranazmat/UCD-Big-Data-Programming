from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

db = client['test']
collection = db['title']

print collection.find_one()
collection.insert_one({"production_year": 2012, "movie_id": 399, "title": "#LdnOnt", "kind_id": 2, "note": 0, "season_nr": 0, "phonetic_code": "L353", "imdb_index": 0, "episode_nr": 0, "id": 3, "episode_of_id": 0}, {"production_year": 0, "movie_id": 411, "title": "@IglesiaPresents", "kind_id": 7, "note": 0, "season_nr": 1, "phonetic_code": "I2421", "imdb_index": 0, "episode_nr": 12, "id": 4, "episode_of_id": 3})
