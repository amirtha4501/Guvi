n = int(input())

arr = list(map(int, input().split()[:n]))
new = []

if 1<=n and n<=100000:
  for i, v in enumerate(arr):
    if i==v:
      new.append(v)
  new.sort()
  
  if new==[]:
    print(-1)
  else:
    print(*new, sep=' ')