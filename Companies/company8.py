n = int(input())
arr = list(map(int, input().split()))

if n<=1000000:
  mini = min(arr)
  maxi = max(arr)
  i1 = arr.index(mini)
  i2 = arr.index(maxi)
  
  d = abs(i1-i2)
  
  print(d)