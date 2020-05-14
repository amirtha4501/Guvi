# Check whether it is a right angled triangle

a, b, c = map(int, input().split())
if (a**2 + b**2) == c**2:
    print('yes')
else:
    print('no')


# Reverse the words in a string

s = str(input())
reverse = []
words = s.split(' ')
for word in words:
    reverse.insert(0,word)
print(' '.join(reverse))

# Find minimun

size = 10
n = list(map(int, input().split()[:size]))
min = n[0]
for i in range(len(n)):
  if n[i] < min:
    min = n[i]
print(min)

