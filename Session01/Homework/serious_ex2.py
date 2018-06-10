from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    "title": "What I think about c4e18 classs?",
    "author": "Nga Nguyễn",
    "content": "I feel very pleased with this class. Teachers are so enthusiastic and friendly "
}

posts.insert_one(new_post)