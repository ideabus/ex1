import pymongo
client = pymongo.MongoClient("mongodb+srv://dba:test4321@cluster0.talzm.mongodb.net/?retryWrites=true&w=majority")
print(pymongo.version)
db = client.test
print(db)
