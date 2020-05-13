# Find largest
def largest(a, b, c):
    if a > b and a > c:
        print(a)

    elif b > c:
        print(b)
    
    else:
        print(c)

a = int(input())
b = int(input())
c = int(input())

largest(a, b, c)