import pymongo
from pymongo_pubsub import Publisher

connection = pymongo.Connection()
database = connection.pubsub_db

publisher = Publisher(database, 'test_event')
publisher.push({'message': 'hello world', 'answer': 42})