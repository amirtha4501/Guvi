# the position of first 1 from right to left, in binary representation of an Integer


# import math
# n = int(input())
# com = n & -n
# print(math.log2(com)+1)


n = int(input())
com = n & -n

def logarithm(val, b):
  if val < b:
    return 0
  return 1 + logarithm(val/b, b)

print(logarithm(com, 2) + 1)