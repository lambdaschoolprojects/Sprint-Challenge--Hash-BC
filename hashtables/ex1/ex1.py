#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    indices_of_weights = None

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        #if weights[i] is not limit:
        target = abs(weights[i] - limit)
        if hash_table_retrieve(ht, target) is not None:
            if hash_table_retrieve(ht, target) > i:
                indices_of_weights = (hash_table_retrieve(ht, target), i)
            else:
                indices_of_weights = (i, hash_table_retrieve(ht, target))
            break

    return indices_of_weights


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
