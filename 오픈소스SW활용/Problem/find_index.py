"""
Write and test a Python function that finds row indices whose
Euclidean distance is less than or equal to 10.0 to the 37th row
"""

import re
import math


def find_index(data, row1, row2):
    first = []
    second = []
    dist = 0

    for i in data:
        if i[0] == row1:
            first.append(i)
        if i[0] == row2:
            second.append(i)

    first.sort()
    second.sort()

    for a, b in zip(first, second):
        dist += (a[2] - b[2]) ** 2

    result = math.sqrt(dist)
    return result


def make_data():
    data = []
    fd = open("A.dat", "r")
    fd_data = "".join(fd.readlines())

    p = re.compile(r"(\d+),(\d+):(\d+)|(\d+),(\d+):(-\d+)")
    find = p.findall(fd_data)

    for i in find:
        tmp = list(i)
        tmp.remove("")
        tmp.remove("")
        tmp.remove("")
        tmp = list(map(int, tmp))
        data.append(tmp)
    return data


if __name__ == "__main__":
    data = make_data()

    print("find row indices (less than or equal to 10.0 to the 37th row)")
    for i in range(0, 99):
        temp_result = find_index(data, i, 37)
        if i == 37:
            continue
        elif temp_result <= 10.0:
            print("index :", i)
