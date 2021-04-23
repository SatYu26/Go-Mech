from prettyprinter import pprint  # to pretty print the cursor result.
import pymongo

from DataFrame import *


# client = pymongo.MongoClient('localhost', 27017)
# db = client.gomechtest
# col = db.collection
# df = mongoImport

# # print(df)

# # you need to pass the 'records' as argument in order to get a list of dict.
# dict = df.to_dict('records')
# # print(dict)
# col.insert_many(dict)
pprint(list(col.find()))
