import pymongo 
import dns
import certifi

print("works")

client = pymongo.MongoClient("mongodb+srv://western:western@hackwestern.xg1hozh.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client['test']
col = db['test1']

print(db.list_collection_names())
print("yea")