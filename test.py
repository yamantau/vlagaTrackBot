import pymongo
import datetime

#connect to db
client = pymongo.MongoClient("mongodb+srv://vlaga:3lPDBLWuAM1u6lbH@cluster0.jztcayu.mongodb.net/?retryWrites=true&w=majority")

str = '/add 234234 '

db = client.info['is_exchange_open']
db.update_one({'name': 'tink'}, {'$set': {'open': False}})


# def add_user(data_res):
#     db = client.info['auth']
#
#     data_to_save = {
#         'tg_id': int(data_res),
#         'end_subscribe': datetime.datetime.now() + datetime.timedelta(days=30),
#         'lvl': 'user'
#     }
#
#     db.insert_one(data_to_save)
#
# add_user(612680793)
#
# str = '2022-08-20 00:08:29.676604'
#
# print(datetime.timedelta(days=30))
#
# print(datetime.datetime.now() + datetime.timedelta(days=2))

# print(datetime.datetime.now().timestamp() > str.timestamp)

db = client.info.auth
#
# user = db.find_one({'tg_id': 34})
# print(user)
#
# print(user['end_subscribe'] > datetime.datetime.now())
#
#
# def check_auth_user(tg_id):
#     db = client.info.auth
#
#     user = db.find_one({'tg_id': tg_id})
#     print(user)
#
# check_auth_user(999)

# def update_subscribe(data_res):
#     db = client.info['auth']
#
#     db.update_one({'tg_id': data_res}, {'$set': {'end_subscribe': datetime.datetime.now() + datetime.timedelta(days=30)}})
#
# update_subscribe(34)