#!/usr/bin/python3
if __name == "__main__":
    from calculator_1 import summ, diff, prod, quot
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, summ(a, b)))
    print("{} - {} = {}".format(a, b, diff(a, b)))
    print("{} * {} = {}".format(a, b, prod(a, b)))
    print("{} / {} = {}".format(a, b, quot(a, b)))
