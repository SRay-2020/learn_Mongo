import os
import pymongo 
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebs" 


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn

    except pymongo.errors.ConnectionFailures as e:
        print("Could not connect to MongoDB: %s") % e
    

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_many({"nationality": "usa"}, {"$set": {"hair_colour": "burgandy"}})

documents = coll.find({"nationality": "usa"})

for doc in documents:
    print(doc)