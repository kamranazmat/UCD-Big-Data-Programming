import MySQLdb
import pandas as pd
import numpy as np

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",       # your username
                     passwd="",  		# your password
                     db="imdb")        # name of the data base

cur = db.cursor()
cur.execute("DESCRIBE aka_title")

index = []
for row in cur.fetchall():
    index.append(str(row[0]))

cur.execute("SELECT * FROM aka_title LIMIT 100")

db.close()

json = {}

data = []
for row in cur.fetchall():
	data.append(list(row))

data = np.array(data)

"""
	for j in range (len(index)):
		data[index[j]].append(row[j])
	i += 1
	if i == 1000:
		break
    #data.append(list(row))
"""
"""
df = pd.DataFrame(data)
df.set_index(index)
"""

print data

for i in range(len(index)):
	json[index[i]] = data[:, i]
 
print json
