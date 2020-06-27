n = int(input())
arr = [int(i) for i in str(n)]

odd = []
for i in arr:
  if i%2 != 0:
    odd.append(i)
print(*odd, sep=' ')