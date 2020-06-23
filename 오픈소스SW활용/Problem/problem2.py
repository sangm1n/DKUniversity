"""
Develop a function that finds the minimum or maximum value in a list,
depending on the caller’s request.
"""

value = list(map(int, input('input values : ').split()))


def loop(value):
    min_idx = 0
    min_value = value[0]

    for i in range(1, len(value)):
        if value[i] < min_value:
            min_value = value[i]
            min_idx = i

    return min_value, min_idx


def min_index(value):
    return min(value), value.index(min(value))


def max_index(value):
    return max(value), value.index(max(value))


check = int(input('   - If you check the loop function, input a number 1\n'
                  '   - If you check the minimum function, input a number 2\n'
                  '   - If you check the maximum function, input a number 3\n>> '))

if check == 1:
    print("(minimum value, value's index) :", loop(value))
elif check == 2:
    print("(minimum value, value's index) :", min_index(value))
else:
    print("(maximum value, value's index) :", max_index(value))
