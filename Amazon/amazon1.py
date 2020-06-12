n = int(input())
arr = list(map(int, input().split()[:n]))

v1 = 0
v2 = 0
a1 = arr[:3]
a2 = arr[-3:]

for i in range(3):
  v1 += a1[i]
  v2 += a2[i]

if v1 == v2:
  print(1)
else:
  print(0)