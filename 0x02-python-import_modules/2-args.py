#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_num = len(sys.argv) - 1
    if args_num == 0:
        print("0 arguments.")
    elif args_num == 1:
        print("1 argument:")
    else:
        print(f"{args_num} arguments:")
    for i in range(args_num):
        print("{}: {}".format(i + 1, (sys.argv[i + 1])))
