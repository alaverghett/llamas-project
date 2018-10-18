from DatasetAPI import Dataset
import os.path
import ijson
import json
OUT_FOLDER = './dataset/tempJSONs'
i = open('./dataset/yelp_academic_dataset_business.json')
# k = [json.loads(j) for j in i]

# print(k)
# for j in i:
#     print(j)
#     input()
# :
#     print(j)
out_path = os.path.join(OUT_FOLDER, "temp.json")
ds = Dataset()
out_file = open(os.path.abspath(out_path), "w")
# for js in i:
#     business = json.loads(js)
#     reviews = ds.get_reviews(business["business_id"])
#     business["reviews"] = {}
#     for review in reviews:
#         business["reviews"][review["review_id"]] = {
#             "user_id": review["user_id"],
#             "stars": review["stars"],
#             "date": review["date"]
    #     }
    # pass


businesses_id = ds.get_business_ids()
# # i = ijson.items(ds.business_file, 'item')
# # for b in i:
# #     print(b)
# #     input()
for i in range(100):

    first = next(businesses_id)

    business = ds.get_business(first)

pass