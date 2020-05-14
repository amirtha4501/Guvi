from math import *
from fractions import Fraction

n = int(input())

p = 1/6
k = 1

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)

term1 = factorial(n) / (factorial(k) * factorial(n-k))
term2 = (p**k) * (1-p)**(n-k)

sum = term1 * term2
print(sum)
ans = str(Fraction(sum).limit_denominator(100))
print(ans)
# print(ans[0],ans[2])
