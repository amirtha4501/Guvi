n = int(input())
p = 0
factors = []
for i in range(2, n):
  if n%i==0:
    p = 1
    for j in range(2, i//2):
      if i%j==0:
        p = 0
    if p==1:
      factors.append(i)

print(*factors, sep=' ')