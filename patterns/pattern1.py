r = int(input())
k = 1
a = ''

if 1<=r and r<=100:
  for i in range(r):
    for j in range(i+1):
      a += str(k)  
      k += 1
      if i != j:
        a += ' '
    a += '\n'
  print(a)