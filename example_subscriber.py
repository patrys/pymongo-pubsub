import pymongo
from pymongo_pubsub import Subscriber

connection = pymongo.Connection()
database = connection.pubsub_db

def test_cb(data):
    print '{0:f}: {1:s}'.format(data['_id'], data['message'])

subscriber = Subscriber(database, 'test_event', callback=test_cb,
                        matching={'answer': 42})
subscriber.listen()