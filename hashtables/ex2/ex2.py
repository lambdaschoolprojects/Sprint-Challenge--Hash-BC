#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []
    next = None

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].destination, tickets[i].source)

    for i in range(length):
        if next is None:
            route.insert(0, "NONE")
            next = hash_table_retrieve(hashtable, "NONE")
        else:
            next = hash_table_retrieve(hashtable, next)
        if(next is not "NONE"):
            route.insert(0, next)

    return route

    return route
