# Check whether the sum of arr value is divisible by 2,3 and 5 or not
n = int(input())

arr = list(map(int, input().split()[:n]))
val = 0
for i in range(n):
  val += arr[i] 
if val%2==0 and val%3==0 and val%5==0:
    print(1)
else:
    print(0)