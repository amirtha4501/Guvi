n = int(input())
arr = list(map(int, input().split()[:n]))

c = False
not_unique = []
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j] and arr[i] not in not_unique:
            not_unique.append(arr[i])
            c = True
if c==True:
  print(*not_unique, sep=' ')
else:
  print(-1)