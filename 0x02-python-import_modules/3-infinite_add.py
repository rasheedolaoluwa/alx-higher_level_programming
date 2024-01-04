#!/bin/usr/python3

if __name__ == "__main__":
    """Print addition of infinite arguments"""
    import sys

    sum = 0
    for i in range(len(sys.argv)-1):
        sum += int(sys.srgv[i + 1])
    print("{}".format(sum))
