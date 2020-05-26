n = int(input())
arr = []
mini = []

for i in range(n):
  q = list(map(int, input().split()[:2]))
  if q[0]==1:
  	arr.append(q[1])
  elif q[0]==2:
    #if arr==[]:
      #print(-1)
    if arr != []:
      mini.append(min(arr))
    else:
      print(-1)
  else:
    pass
  
print(*mini, sep='-')