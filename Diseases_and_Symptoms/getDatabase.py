from pymongo import MongoClient
import dns
import certifi
import config

def get_database():
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(config.CONNECTION_STRING, tlsCAFile=certifi.where())
   db = client['test']
   print("collections in db: ", db.list_collection_names())
   # Create the database for our example (we will use the same database throughout the tutorial
   return db
  
if __name__ == "__main__":   
   # Get the database
   dbname = get_database()

