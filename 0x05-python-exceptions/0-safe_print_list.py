#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e = 0
    try:
        for i in range(x):
            if e >= x:
                break
            print(my_list[i], end=" ")
            e += 1
            print()
            return e
    except IndexError:
        return 0
