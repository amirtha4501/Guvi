n = int(input())
a = ''

if n<=1000:
  for i in range(n):
    for j in range(i+1):
      a += str(1)
      if i!=j:
        a += ' '+'1'+' '
    a += '\n'
  print(a)