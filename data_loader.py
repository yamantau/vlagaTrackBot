import datetime

import pymongo

client = pymongo.MongoClient("mongodb+srv://vlaga:3lPDBLWuAM1u6lbH@cluster0.jztcayu.mongodb.net/?retryWrites=true&w=majority")

def check_auth_user(tg_id, need_lvl):
    db = client.info.auth

    user = db.find_one({'tg_id': tg_id})

    if user is not None:

        if user['end_subscribe'] > datetime.datetime.now():

            if need_lvl <= user['lvl']:

                return True

            return 'Нет доступа'

        return 'Надо обновить подписку'

    return 'Нет доступа'

def get_rate_binance(INFO):
    db = client.binance[INFO]

    data_res = db.find().skip(db.count_documents({}) - 1)

    return data_res[0]['rate']

def get_exchange_rate(INFO):
    db = client.rate_exchange[INFO]

    data_res = db.find().skip(db.count_documents({}) - 1)

    return data_res[0]['rate']

def get_spred():
     db = client.info['spred_check']

     return db.find()

def get_info(INFO):
    db = client.info[INFO]

    data_res = db.find_one({'name': 'tink'})['open']

    return data_res
