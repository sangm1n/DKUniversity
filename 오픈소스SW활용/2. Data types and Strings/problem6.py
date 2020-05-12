"""
Let p be a bank’s interest rate in percent per year. After n years, an initial amount A has taken grown to

A(1+p/100)^n
"""

p = float(input('input interest rate : '))
n = int(input('input year : '))
A = int(input('input initial amount : '))

result = A*(1+p/100)**n

print('total (initial amount + interest) :', round(result))
print('interest (total - initial amount) :', round(result-A))