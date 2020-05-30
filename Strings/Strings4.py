s = str(input())
res = False

for i in 'aeiou':
  if i in s:
    res = True

if res:
  print('yes')
else:
  print('no')