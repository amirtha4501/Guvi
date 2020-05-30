# Sum of ascii values of the string
s = str(input())
l = [ ord(char) for char in s ]
res = 0

for val in l:
  res += val
  
print(res)