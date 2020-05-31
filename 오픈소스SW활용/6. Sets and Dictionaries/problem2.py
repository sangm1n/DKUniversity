"""
The keys in a dictionary are guaranteed to be unique, but the values are not.
Write a function that takes a single dictionary as an argument
and returns the number of distinct values it contains.
For example, given the input {’red’: 1, ’green’: 1, ’blue’: 2}, your function should return 2.
"""

problem = {'red': 1, 'green': 1, 'blue': 2, 'pink': 1, 'purple': 2, 'grey': 3}
print(problem)

def count_values1(problem):
    val = list(problem.values())
    temp = []

    for i in range(len(val)):
        if val[i] not in temp:
            temp.append(val[i])
    return temp

def count_values2(problem):
    val = set(problem.values())
    return val

print('distinct values :', count_values1(problem))
print('distinct values :', count_values2(problem))