import pymongo
from config import DB_NAME, CONNECTION_URL

client = pymongo.MongoClient(CONNECTION_URL)
db = client[DB_NAME]
 
item_details = db.rides.find()
for item in item_details:
   # This does not give a very readable output
   print(item)