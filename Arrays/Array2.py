n, m = map(int, input().split())

arr = list(map(int, input().split()))
new_arr = []
for i in range(n-1):
    d = abs(arr[i]-arr[i+1])
    if d>m:
        new_arr.append(1)
    else:
        new_arr.append(0)

last = abs(arr[0]-arr[-1])
if last>m:
    new_arr.append(1)
else:
    new_arr.append(0)

print(*new_arr, sep=' ')