import pymongo
from pymongo import MongoClient

client = MongoClient ("mongodb+srv://relioadmin:r@cluster0.5tfsl.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('relio-db')
users = db.users

users.count_documents({})
