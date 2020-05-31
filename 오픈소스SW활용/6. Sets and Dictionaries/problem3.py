"""
A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 3, 0, 0, 0].
Storing all those zeros in a list wastes memory, so programmers often use dictionaries
instead to keep track of just the nonzero entries.
For example, the vector shown earlier would be represented as {0:1, 6:3},
because the vector it is meant to represent has the value 1 at index 0 and the value 3 at index 6.
"""

first = [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]
second = {1: 2, 6: 2}
print('normal :', first)

def normal_to_sparse(list):
    temp = {}
    for idx, value in enumerate(list):
        if value != 0:
            temp[idx] = value
    return temp

def change_sign(dict):
    temp = {}
    for key, value in dict.items():
        temp[key] = dict[key] * -1
    return temp

def add_vector(one, two):
    one_list = [0 for x in range(10)]
    two_list = [0 for x in range(10)]
    for key, value in one.items():
        if key in range(10):
            one_list[key] = value
    for key, value in two.items():
        if key in range(10):
            two_list[key] = value

    total = [sum([one_list[i], two_list[i]]) for i in range(len(one_list))]
    return normal_to_sparse(total)

def minus_vector(one, two):
    return add_vector(one, change_sign(two))


sparse = normal_to_sparse(first)
minus_sparse = change_sign(sparse)
total = add_vector(sparse, second)
subtract = minus_vector(sparse, second)

print('\nnormal to sparse :', sparse)
print('change sign', minus_sparse)
print('\nshow two sparse vector :', sparse, second)
print('add :', total)
print('subtract :', subtract)