# # Print uniques in the list
# n = int(input())
# arr = list(map(str, input().split()[:n]))

# unique = set()
# l = []
# for i in arr:
#   if not (i in unique or unique.add(i)):
#     l.append(i)

# print(*l, sep=' ')


# Remove the immediate duplicate digits 
st = str(input())

new = []
n = len(st)

for i in range(0,n):
    print(st[i])
    if st[i] != st[n-1]:
        if st[i] != st[i+1]:
            new.append(st[i])
            print('oi')
if new==[]:
    print(-1) 
else:
    print(new)

