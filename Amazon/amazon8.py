k = int(input())
arr = []

for i in range(k):
  a = list(map(int, input().split()))
  arr += a

arr.sort()

print(*arr, sep=' ')