"""
Consider two functions f (x) = x abd g(x) = x2 on the interval f(x) =  abd g(x) = x^2
on the interval [-4, 4]. Write a program that finds approximately for which value of
x the two graphs cross. Do this by considering N equally distributed points on the interval,
at each point checking whether |f(x)-g(x)| < e with a fixed value e.
Let N and e be user input to the program and let the result be printed to screen.

Run your program with N=400 and e=0.01
"""

N = int(input('input N : '))
e = float(input('input e : '))

arr = []
result = []
sum = -4

for i in range(N+1):
    arr.append(round(sum, 2))
    sum += (8/N)

    if abs(sum - sum**2) < e:
        result.append(round(sum, 2))

print('x :', result)