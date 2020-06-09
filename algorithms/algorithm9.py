n, k = map(int, input().split())

if n<=10000 and k<=n:
  arr1 = list(map(int, input().split()[:n]))
  arr2 = list(map(int, input().split()[:k]))
  
  maxi = arr1[0]
  arr = []
  for i in arr2:
    arr1.append(i)
    for i in range(n):
      if arr1[i] > maxi:
        maxi = arr1[i]
    arr.append(maxi)

  print(*arr, sep=' ')