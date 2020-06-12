n, k = map(int, input().split())
arr = list(map(int, input().split()[:n]))
new_arr = []

for i in arr:
  if i != k:
    new_arr.append(i)

if new_arr == []:
  print('empty')
else:
  print(*new_arr, sep=' ')