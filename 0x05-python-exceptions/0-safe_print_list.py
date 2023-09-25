#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            e += 1
    except IndexError:
        return e
    print()
    return e
