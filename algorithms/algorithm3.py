# Find unique in an array using collections

import collections

n = int(input())

if n <= 100000:
  arr = list(map(int, input().split()[:n]))

  counter = collections.Counter(arr)

  for i in counter.elements():
    # print( "% s : % s" % (i, ele[i]), end ="\n") 
    if counter[i] == 1:
      print(i)