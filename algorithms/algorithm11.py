n = int(input())
arr = list(map(int, input().split()[:n]))
new_arr = []
res = []
for i in arr:
  new_arr.append(i)
  res.append(min(new_arr))
  
print(*res, sep=' ')