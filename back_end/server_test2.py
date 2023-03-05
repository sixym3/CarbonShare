import pymongo
import ssl

client = pymongo.MongoClient('mongodb+srv://admin-user-01:k99lp2MIboGTmXOq@test-cluster-01.ecwli33.mongodb.net/?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
db = client['test-cluster-01']
 
item_details = db.rides.find()
for item in item_details:
   # This does not give a very readable output
   print(item)