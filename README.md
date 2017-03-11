# UCD-Big-Data-Programming

- mysql and connection done using python 
- faced problem during json.dumps, then enoded to 'latin-1' 
- tried inserting data to mongodb, successful !!!

- next automating the script

- i can make the primary key of a table as '_id' in mongodb but the problem will arise when there are more than one column as primary key
- making all 'null' value as 0 (even if it is a string)

- using mongoDB compass to get better visualisation of the database
- all the tables have 'id' as primary key, so this can be made '_id'

- the current script failed, it took around 4-5 hours just to loop around 2 tables
- next I will try to run one by one for each table

Report: 11th March 2017
- SHOW VARIABLES LIKE 'connect_timeout'; --- it was 30 secs, I changed it to 240 secs
- then it started working (error: connection timeout problem !!)
- I tried to access the MySQL database and then retrived one table at a time. Then, I looped around all the row in the table and also inserted it to the MongoDB database at the same time. This was effective from previous attempt.

- table 'movie_info' took 23:22:07715 minutes to transfer data from MySQL database to MongoDB
- similarly, 'movie_company' took 37:12:689009 minutes

- 'cast_info' is left and this is the largest database, this may take upto 2-3 hours
- screenshot added 'mongoDB.png', showing the current status of MongoDB (using MongoDB Compass)