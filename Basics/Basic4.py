l, r = map(int, input().split())

count = 0

if l<r and r<=100000:
  for i in range(l, r+1):
    if (i <= 1):
      pass
    elif (i <= 3 or i == 5):
      count += 1
    elif (i%2 == 0 or i%3 == 0):
      pass
    else:
      count += 1
print(count)
    