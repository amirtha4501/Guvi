# Bitwise AND operator

size = int(input())
n = list(map(int, input().split()[:size]))

val = n[0]

for i in range(len(n)):
  val &= n[i]
print(val)

# Check whether a, b, c forms a triangle

a, b, c = map(int, input().split())

if a<=100000 and b<=100000 and c<=100000:
  if a+b>c and b+c>a and c+a>b:
    print('yes')
  else:
    print('no')