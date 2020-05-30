st = str(input())
prev = None
st_new = []

for char in st:
  if char != prev:
    st_new.append(char)
    prev = char
  elif char == prev:
    st_new.remove(prev)

print(*st_new, sep='')