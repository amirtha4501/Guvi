n = int(input())
arr = list(map(int, input().split()[:n]))

def maxOr(n, arr):
  maximum = 0
  
  for i in range(0, n):
    for j in range(i+1, n):
      maximum = max(maximum, arr[i] | arr[j])
  return maximum

print(maxOr(n, arr))
