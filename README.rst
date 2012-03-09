=======================================================================
pymongo-pubsub — a publish-subscribe pattern implementation for pymongo
=======================================================================

------

Ever wished you could use your MongoDB to drive an event-driven enviroment?

Now you can.

pymongo-pubsub uses a round-robin *capped* collection to store its data on one
end and a *tailable* cursor to catch it as it is inserted on the other.

The publisher
=============

A publisher is a piece of code responsible for pumping data into the database: ::

    import pymongo
    from pymongo_pubsub import Publisher

    connection = pymongo.Connection()
    database = connection.pubsub_db

    publisher = Publisher(database, 'test_event')
    publisher.push({'message': 'hello world', 'answer': 42})

The subscriber
==============

A subscriber is a piece of code responsible for processing data as it is pulled
from the database: ::

    import pymongo
    from pymongo_pubsub import Subscriber

    connection = pymongo.Connection()
    database = connection.pubsub_db

    def test_cb(timestamp, data):
        print '{0:f}: {1:s}'.format(timestamp, data)

    subscriber = Subscriber(database, 'test_event', callback=test_cb)
    subscriber.listen()

The details
===========

A ``Publisher`` will take care of setting up the underlying collection. You can
pass it optional ``max_size`` and ``max_length`` parameters to define storage
limits of the collection at the time it is created. The default size is
``1000000`` bytes and the default length limit is ``None``.

The subscriber will never create any collections in the database and in case
the collections is missing it will cowardly raise a ``KeyError`` exception.
This is not a bug. This is to avoid having to synchronize collection limits
between the publisher and all of the subscribers.

Make sure your queue is big enough to never overflow or you're going to start
losing data. You care about your data, right?