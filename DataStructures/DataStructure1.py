a, b = map(int,input().split())

def Factorial(n):
  return 1 if (n==0 or n==1) else n *  Factorial(n-1)

if a<=10000 and b<=10000 and a-b<=5:
  value = Factorial(a) / Factorial(b)
  print(value)