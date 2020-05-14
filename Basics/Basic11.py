# # Presence of an element

# limit, k = map(int, input().split())
# n = list(map(int,input().split()[:limit]))

# count = False
# for i in range(len(n)):
#   if k == n[i]:
#     count = True

# if count == True:
#     print('yes')
# else:
#     print('no')



# # Find index of min and max

# size = int(input())
# n = list(map(int, input().split()[:size]))

# min = n[0]
# max = n[0]

# for i in range(len(n)):
#   if n[i] < min:
#     min = n[i]
#   elif n[i] > max:
#     max = n[i]
#   else:
#     pass
    
# print(n.index(min)+1, n.index(max)+1)


a, b = map(str, input().split())

a = a.upper()
b = b.upper()

if a==b:
  print('D')
  
elif a=='R' and b=='P':
  print(b)
elif a=='P' and b=='R':
  print(a)
  
elif a=='R' and b=='S':
  print(a)
elif a=='S' and b=='R':
  print(b)
  
elif a=='P' and b=='S':
  print(b)
elif a=='S' and b=='P':
  print(a)
  
else:
  pass
