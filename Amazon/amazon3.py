n = int(input())
arr = list(map(int, input().split()[:n]))

for i in range(1, n+1):
  if i not in arr:
    print(i)
