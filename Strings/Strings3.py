# Palindrome or not

s = str(input())
rev = s[::-1]

val = 0

for i in range(len(s)):
  if s[i] == rev[i]:
    val = 1
  else:
    val = 0

print(val)