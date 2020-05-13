# nth term of the series 1, 4, 9, 16, 25, 36, ...

n = int(input())

if n == 0:
    print(n)
elif n < 0:
    print("Error")
else:
    print(n**2)
