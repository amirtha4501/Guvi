n = int(input())

arr1 = list(map(int, input().split()[:n]))
arr2 = list(map(int, input().split()[:n]))

rev = arr2[::-1]

if arr1 == rev:
  print('yes')
else:
  print('no')