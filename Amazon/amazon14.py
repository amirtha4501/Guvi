n = int(input())
sum = 0
if 1<=n and n<=100000:
  arr = list(map(int, input().split()[:n]))
  for i in arr:
    sum += i
  print(sum)