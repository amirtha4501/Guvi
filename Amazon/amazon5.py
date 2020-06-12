n = int(input())
arr = list(map(str, input().split()[:n]))

arr.sort()

print(*arr, sep=' ')