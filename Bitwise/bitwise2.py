n = int(input())
array = list(map(int, input().split()[:n]))

i = 0 

while i < len(array)-1:
  t = array[i]
  array[i] = array[i+1]
  array[i+1] = t
  i += 2
  
print(*array, sep=' ')