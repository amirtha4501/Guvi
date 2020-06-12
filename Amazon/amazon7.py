n, m = map(int, input().split())

if n>=1 and m>=1 and n<=106 and m<=106:
  a1 = list(map(int, input().split()[:n]))
  a2 = list(map(int, input().split()[:m]))
  a3 = []
  arr = []
  
  for i in a2:
    for j in a1:
      if i==j:
        arr.append(j)

  for ele in a1:
    if ele not in arr:
      a3.append(ele)

  a3.sort()
  arr += a3
  print(*arr, sep=' ')








