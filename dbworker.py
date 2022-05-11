import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")

current_db = db_client["lab4db"]

collection = current_db["brands"]

#ins_audi = [
#    {'brand': 'porsche', 'model': '718'},
#    {'brand': 'porsche', 'model': '911'},
#    {'brand': 'porsche', 'model': 'Taycan'},
#    {'brand': 'porsche', 'model': 'Panamera'},
#    {'brand': 'porsche', 'model': 'Macan'},
#    {'brand': 'porsche', 'model': 'Cayenne'}
#]

#ins_result = collection.insert_many(ins_audi)
#print(ins_result.inserted_ids)

def find_models(br):
    models = ""
    for brand in collection.find({"brand": br}):

        print(brand["model"])
        if models == "":
            models += (brand["model"])
        else:
            models += ", " + brand["model"]

    return models