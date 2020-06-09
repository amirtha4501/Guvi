n, k = map(int, input().split())

arr = list(map(int, input().split()[:n]))

if n>=1 and n<=1000000000000000: 
    if k in arr:
      print('Yes')
    else:
      print('no')