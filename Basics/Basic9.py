# check whether a number is composite 
n = int(input())

if n > 3 and n%2 == 0 or n%3 == 0:
  print('yes')
else:
  print('no')


# Find difference
k, n = map(int, input().split())
print(abs(k-n))


# Print bitwise not
n = int(input())
if n <= 10000 and n >= 1:
  print(~n)


# Bitwise OR for the array
size = int(input())
n = list(map(int, input().split()[:size]))
res = n[0]
for i in range(1, len(n)):
    res = res | n[i]
print(res)