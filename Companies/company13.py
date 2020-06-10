# n, k = map(int, input().split())
# a1 = []
# a2 = []

# for i in range(n):
#   t = list(map(int, input().split()[:k]))
#   a1.append(t)
  
# for i in range(len(a1)):
#     for j in range(i+1, len(a1)):
#         print(a1[i],a1[j])

#         for k in a1[i]:
#             # print(k,end=' ')
#             if k in a1[j]:
#                 a2.append(k)
#                 # print(k,end='-')
#         # print(a1[i],a1[j])

# print(*a2, sep=' ')


import itertools

a = ["A", "B", "C"]
b = ["A","C"]
c = ["C","D","E"]

for aval,bval,cval in itertools.product(a,b,c):
    if aval == bval and bval == cval:
        print(aval)