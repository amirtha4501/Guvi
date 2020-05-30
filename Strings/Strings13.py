s = str(input())
l = []
val = 0
string = ''

for char in s:
  if char.isdigit():
    val = val + int(char)
  else:
    l.append(char)

print(string.join(l)+str(val))