"""
Design and implement a Python script that reads a set of integers
and returns the integers that occur two or more times
"""


def dup(input):
    tmp = []

    for i in input:
        count = 0
        for j in input:
            if (i == j):
                count += 1
        if (count > 1):
            tmp.append(i)

    result = list(set(tmp))
    return result


if __name__ == "__main__":
    input = [10, 9, 8, 7, 6, 5, 4, 3, -3, -3, 4, 4]

    print("duplicate number :", dup(input))
