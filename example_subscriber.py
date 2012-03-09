import pymongo
from pymongo_pubsub import Subscriber

connection = pymongo.Connection()
database = connection.pubsub_db

def test_cb(timestamp, data):
    print '{0:f}: {1:s}'.format(timestamp, data)

subscriber = Subscriber(database, 'test_event', callback=test_cb)
subscriber.listen()