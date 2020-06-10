n, k = map(int, input().split())
key = False

if n<=100000:
  arr = list(map(int, input().split()[:n]))
  if k in arr:
    key = True

  if key:
    print('yes')
  else:
    print('no')