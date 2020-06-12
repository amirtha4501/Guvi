n = int(input())
arr = list(map(int, input().split()[:n]))
new_arr = []
val = 0
for i in arr:
  if i%2==0:
    val += i
    new_arr.append(val)
  else:
    new_arr.append(i)
print(*new_arr, sep=' ')