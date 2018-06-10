from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    "title": "Dream, Hope and Love",
    "author": "Nga Nguyễn",
    "content": "Life ends when you stop dreaming, hope ends when you stop believing and love ends when you stop caring. So dream hope and love"
}

posts.insert_one(new_post)