"""
Write and test your Python function to find the maximum values of row and column
"""

import re


def find_size(data):
    rowMax = sorted(data, key=lambda x: x[0], reverse=True)
    colMax = sorted(data, key=lambda x: x[1], reverse=True)
    result = (rowMax[0][0]+1, colMax[0][1]+1)

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

    print("maximum value of row :", find_size(data)[0])
    print("maximum value of column :", find_size(data)[1])
