n = int(input())
arr = list(map(int, input().split()[:n]))

min = arr[0]
for i in range(n-1):
  if min > arr[i]:
    min = arr[i]
print(min)