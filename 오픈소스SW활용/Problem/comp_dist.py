"""
Write and test your Python function to calculate the Euclidean distance
between 10-th and 27-th rows
"""

import re
import math


def comp_dist(data):
    row10 = []
    row27 = []
    dist = 0

    for i in data:
        if i[0] == 10:
            row10.append(i)
        if i[0] == 27:
            row27.append(i)

    row10.sort()
    row27.sort()

    for a, b in zip(row10, row27):
        dist = dist + (a[2] - b[2]) ** 2

    result = round(math.sqrt(dist), 2)
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

    print("calculate the Euclidean distance between 10th and 27th rows")
    print("distance :", comp_dist(data))
