n = int(input())

arr = list(map(int, input().split()[:n]))

for i in range(0, n):
  for j in range(i+1, n):
    res = arr[i] ^ arr[j]

print(res)