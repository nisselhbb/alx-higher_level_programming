#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add_args = sys.argv[1:]
    if len(add_args) == 0:
        print("0")
    else:
        addition = sum(int(i) for i in add_args)
        print(addition)
