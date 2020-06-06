# try:
#   n, m = map(int, input().split())
#   i = 1
#   while(i <= n and i <= m):
#     if(n % i == 0 and m % i ==0):
#       gcd = i
#     i += 1
#   print(gcd)
# except: 
#    print(-1)



# n, m = map(float, input().split())

# while(m != 0):
#   t = m
#   m = n%m
#   n = t
# gcd = n
# print(gcd)


n, m = map(int, input().split())

def GCD(n,m):
    if m==0:
      return n
    else:
      return GCD(m, n%m)

gcd = GCD(n,m)

if gcd < 2: 
  print(-1)
else:
  print(gcd)