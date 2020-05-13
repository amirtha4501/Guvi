# Finding the quadratic equation

from math import sqrt

a, b, c = map(int, input().split())

d  = (b**2) - (4*a*c)

x = (-b + sqrt(d)) / (2*a)
y = (-b - sqrt(d)) / (2*a)

print('%.2f' % x)
print('%.2f'% y)