# Print the maximum repeating number.
import collections

n = int(input())
arr = list(map(int, input().split()[:n]))

counter = collections.Counter(arr)

max = 0
for i in counter.elements():
  if counter[i] > max:
    max = counter[i]
    key = i

print(key)