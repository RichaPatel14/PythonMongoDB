import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

x = mycol.find_one()
print(x)
