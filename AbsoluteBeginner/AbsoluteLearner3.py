# Find first three multiples 

"""Using for loop and function"""
n = int(input())
def multiplier(n):    
    for i in range (1, 4):
        print(i * n, end=' ')
multiplier(n)
print('\n')

"""Using loop"""
m = int(input())
for i in range(1, 4):
    print(i*m, end=' ')
print('\n')

"""Using list comprehension"""
o = int(input())
ls = [(x+1)*o for x in range(3)]
for i in ls:
    print(i, end=' ')
print('\n')

"""Using simple print"""
s = int(input())
print(1*s, 2*s, 3*s)