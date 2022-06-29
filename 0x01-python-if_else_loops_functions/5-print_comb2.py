#!/usr/bin/python3
for _digit in range(0, 100):
    if _digit != 99:
        print("{:02d}, ".format(_digit), end='')
    else:
        print("{:02d}".format(_digit))
