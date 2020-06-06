r = int(input())

if 1<=r and r<=100:
    for i in range(r, 0, -1):
        for j in range(i):
          print('$', end="")
        print()
        
        
        