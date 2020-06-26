"""
Write and test your Python function to find the maximum and minimum values
"""

import re


def find_value(data):
    valueMax = sorted(data, key=lambda x: x[2], reverse=True)
    valueMin = sorted(data, key=lambda x: x[2], reverse=False)
    result = (valueMax[0][2], valueMin[0][2])

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

    print("maximum value :", find_value(data)[0])
    print("minimum value :", find_value(data)[1])
