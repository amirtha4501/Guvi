n = list(map(int, input()))
p = len(n)

val = 0

for i in range(len(n)):
  n[i] = n[i]**p
  val += n[i]
  
print(val)