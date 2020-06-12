s = list(map(str, input().split()))
stack = []

for i in range(len(s)-1, -1, -1):
  stack.append(s[i])

print(*stack, sep=' ')