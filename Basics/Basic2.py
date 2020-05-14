count = 0

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if i == k:
        count += 1
if count == 0:
    print(-1)
else: 
    print(count-1)

# The following command can take n number of inputs 
# n,k=map(int, input().split(' '))
# a=list(map(int,input().split(' ')))
# count=0
# for each in a:
#     if each == k:
#         count+=1
# print(count)