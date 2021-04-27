import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.test

brand = db.brand

brandsample = db.brandsample

# pprint(db.brand.find({'variantId': "2132"}))
# dataRequired = brand.find_one({'variantId': "2132"}).limit(1)
dataRequired = brand.find({}, {'_id': 0, 'variantId': 0, 'd2IExcellent': 0, 'd2IGood': 0, 'd2IFair': 0, 'i2DExcellent': 0, 'i2DGood': 0, 'i2DFair': 0, 'i2IExcellent': 0,
                               'i2IGood': 0, 'i2IFair': 0, 'priceExcellent': 0, 'priceGood': 0, 'onePrice': 0, 'makeId': 0, 'modelId': 0, 'year': 0, 'owner': 0, 'kmDriven': 0, 'seller_type': 0, 'city_name': 0, })

for x in dataRequired:
    myquery = {"variantId": '2132'}   # ask question
    newvalues = {"$set": x}

    brandsample.update_many(myquery, newvalues)

    print("Success")
