from itertools import permutations

s = str(input())
arr = []

for tup in permutations(s):
  for val in tup:
    arr.append(val)
    print(val, end='')
  print()