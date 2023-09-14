#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_k = []
    for key, v in a_dictionary.items():
        if v == value:
            delete_k.append(key)
    for key in delete_k:
        del a_dictionary[key]
