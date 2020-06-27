s = str(input())
st = ''
prev = 0
for i in range(len(s)):
  if s[i] != prev:
    st += s[i]
    prev = s[i]
  elif s[i] == prev:
    st = st[:-1]

print(st)