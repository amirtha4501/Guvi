# Check if the array is in sorted form or not in either ascending or descending
n = int(input())
arr = list(map(int, input().split()[:n]))

asc = sorted(arr)
dec = sorted(arr, reverse=True)
res = False

for i in range(0, n):
  if arr[i] == asc[i] or arr[i] == dec[i]:
  	res = True
  else:
    res = False
    break
	
if res == True:
  print('yes')
else: 
  print('no')