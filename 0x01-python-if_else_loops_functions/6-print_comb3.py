#!/usr/bin/python3
for _digit in range(0, 99):
    if _digit % 10 > _digit / 10:
        if _digit != 89:
            print("{:02d}, ".format(_digit), end='')
        else:
            print("{:02d}".format(_digit))
