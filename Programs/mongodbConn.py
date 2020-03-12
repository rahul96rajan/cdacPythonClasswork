from pymongo import MongoClient

my_client = MongoClient('localhost', 27017)
print(my_client.list_database_names())
my_db = my_client['sample']
my_collection = my_db['my_table']
my_collection2 = my_db['my_table2']

sample_list = mylist = [
  {"id": 1, "name": "John", "address": "Highway 37"},
  {"id": 2, "name": "Peter", "address": "Lowstreet 27"},
  {"id": 3, "name": "Amy", "address": "Apple st 652"},
  {"id": 4, "name": "Hannah", "address": "Mountain 21"},
  {"id": 5, "name": "Michael", "address": "Valley 345"},
  {"id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  {"id": 7, "name": "Betty", "address": "Green Grass 1"},
  {"id": 8, "name": "Richard", "address": "Sky st 331"},
  {"id": 9, "name": "Susan", "address": "One way 98"},
  {"id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  {"id": 11, "name": "Ben", "address": "Park Lane 38"},
  {"id": 12, "name": "William", "address": "Central st 954"},
  {"id": 13, "name": "Chuck", "address": "Main Road 989"},
  {"id": 14, "name": "Viola", "address": "Sideway 1633"}
]

return_val = my_collection.insert_many(sample_list)
print(return_val)
ret_val = my_collection.insert_one({"id": 15, "name": "Sherlock",
                                    "address": "221B Baker Street"})
print(ret_val)

print(my_client.list_database_names())

for x in my_collection.find():
    print(x)

my_collection2.insert_one({ "id": 15, "name": "Sherlock",
                          "address": "221B Baker Street"})

print(my_client.list_database_names())
my_collection.drop()
print(my_client.list_database_names())
my_client.drop_database("sample")
