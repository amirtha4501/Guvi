n = int(input())
arr = list(map(int, input().split()[:n]))
sum_val = 0

for i in arr:
  if i < 0:
    sum_val += i
print(sum_val)