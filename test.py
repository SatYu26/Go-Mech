from prettyprinter import pprint  # to pretty print the cursor result.
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.test

brand = db.brand

brandsample = db.brandsample

# pprint(db.brand.find({'variantId': "2132"}))
# dataRequired = brand.find_one({'variantId': "2132"}).limit(1)
dataRequired = brand.find_one({'variantId': "2132"}, {'_id': 0, })

myquery = {"variantId": "2132"}
newvalues = {"$set": dataRequired}


brandsample.update_many(myquery, newvalues)
print("Success")
