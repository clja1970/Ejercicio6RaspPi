import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BytacoraCasa"]
mycol = mydb["Cuaderno"]

mylist = [{"Coche":[{"Descripción":"Cambio de aceite","fecha":"6-08-21"},{"Descripción":"ITV","fecha":"12-12-21"}]}]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)