s1, s2 = map(str, input().split())

s2 = set(s1)
s1 = set(s2)

if s1==s2:
  print('true')
else:
  print('false')