n, k = map(int, input().split())

if n<=100000:
  arr = list(map(int, input().split()[:n]))  
  a1 = arr[:k]
  a2 = arr[k:]
  a1.sort()
  a2.sort(reverse=True)
  for i in a2:
    a1.append(i)
  
  print(*a1, sep=' ')