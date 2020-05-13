# Print the table of nine with single space between the elements till the number that is input.

"""Using for loop"""
a = int(input())
for i in range(1, a+1):
    print(i * 9, end=' ')

"""Using list comprehension"""
n = int(input())
if n==0:
  print("NULL")
elif n>0:
  ls = [(x+1)*9 for x in range(n)] 
  for i in ls:
    print(i, end=" ")
else:
  print("Error")  

"""Using also list comprehension"""
n = int(input())
if n > 0:
  ls = [print((x+1)*9, end=" ") for x in range(n-1)] 
  print(n*9)
elif n==0:
  print("NULL")
else:
  print("Error")  