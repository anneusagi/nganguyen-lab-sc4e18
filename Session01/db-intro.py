#SQL
#noSGL
#GraphQL


from pymongo import MongoClient

mongo_uri = "mongodb://ad16:admin16@ds147450.mlab.com:47450/c4e18-lab"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database[]
db = client.get_default_database()

#3. Create collection
comics = db['comic']

#4. Create document
# new_comics = {
#     "title": "DB",
#     "description": "Dragon Balls"
# }

#5. Insert document into collection
# comics.insert_one(new_comics)

all_comics = comics.find()

for comics in all_comics:
    print(comics)