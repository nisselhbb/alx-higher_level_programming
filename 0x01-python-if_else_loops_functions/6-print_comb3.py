#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        among = ", "
        if i == 8:
            among = "\n"
        print("{:d}{:d}".format(i, j), end=among)
