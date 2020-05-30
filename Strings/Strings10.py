# sum of ints in string
s = str(input())
num = []

for char in s:
  if char.isdigit():
    num.append(int(char))    
res = 0
res = sum([i for i in num])

print(res)