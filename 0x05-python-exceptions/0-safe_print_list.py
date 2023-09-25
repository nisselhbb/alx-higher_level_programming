#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        e = 0
        for i in my_list:
            if x > e:
                print(i, end="")
                e += 1
        print()
        return e
    except IndexError:
        return 0
