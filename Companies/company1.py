# n = int(input())
# if n>=1 and n<=10000:
#   arr = list(map(int, input().split()[:n]))  
#   for i in range(n, 1, -1):
#     print(i, end='=>')
#   print(arr[0])

n = int(input())

arr = list(map(int, input().split()[:n]))

for i in range(n, 1, -1):
  print(i, end='->')
print(arr[0])