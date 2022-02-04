from pymongo import MongoClient


# database connection

client = MongoClient('localhost',27017)
db = client["test"]

