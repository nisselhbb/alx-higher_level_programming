#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for n in range(len(dir(hidden_4))):
        if (dir(hidden_4)[n][2:] != "__"):
            print(dir(hidden_4)[n])
