import pymongo
client = pymongo.MongoClient("mongodb+srv://roadtodsmlai:WhiteKnight_01@cluster0.l5xlzmv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name":"piyush",
     "email": "piyushraipure@gmail.com",
     "surname": "raipure"
}

db1 = client['Mongotest']
coll = db1['test']
coll.insert_one(d)