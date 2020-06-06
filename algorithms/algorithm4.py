n = int(input())
arr = list(map(int, input().split()[:n]))
res_arr = []
arr = sorted(arr)
sp = n//2
min_arr = arr[:sp]
max_arr = sorted(arr[sp:], reverse=True)

for i in range(n//2):
  res_arr.append(max_arr[i])
  res_arr.append(min_arr[i])
if n%2 != 0:
    res_arr.append(max_arr[-1])
print(*res_arr, sep=' ')
