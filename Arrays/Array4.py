n = int(input())
arr = list(map(int, input().split()[:n]))
min = arr[0]
max = arr[0]

for i in range(n-1):
  if arr[i]<min:
    min = arr[i]
  elif arr[i]>max:
    max = arr[i]
  else:
    pass
i1 = arr.index(max)
i2 = arr.index(min)
d = i1 - i2
print(d)