import pymongo
import datetime
import config

#connect to db
client = pymongo.MongoClient("mongodb+srv://vlaga:3lPDBLWuAM1u6lbH@cluster0.jztcayu.mongodb.net/?retryWrites=true&w=majority")

#get db collection in info
def bin_save_data(data_res, INFO):
    db = client.binance[INFO]

    data_to_save = {
        'date': datetime.datetime.now(),
        'rate': data_res
    }

    db.insert_one(data_to_save)

def rate_exchange_save(data_res, INFO):
    db = client.rate_exchange[INFO]

    data_to_save = {
        'date': datetime.datetime.now(),
        'rate': data_res
    }

    db.insert_one(data_to_save)

def info_update(data_res, INFO):
    db = client.info[INFO]

    data_to_save = {
        'is_exchange_open': data_res
    }

    db.update_one({'name': 'tink'}, {'$set': {'open': data_to_save}})

def add_user(data_res):
    db = client.info['auth']

    data_to_save = {
        'tg_id': int(data_res),
        'end_subscribe': datetime.datetime.now() + datetime.timedelta(days=30),
        'lvl': config.USER
    }

    db.insert_one(data_to_save)

def update_subscribe(data_res):
    db = client.info['auth']

    db.update_one({'tg_id': data_res}, {'$set': {'end_subscribe': datetime.datetime.now() + datetime.timedelta(days=30)}})

def save_spred(name, spred):
    db = client.info['spred_check']

    db.update_one({'name': name}, {'$set': {'spred': spred}})
