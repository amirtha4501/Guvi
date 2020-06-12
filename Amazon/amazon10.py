n, k = map(int, input().split())

arr = list(map(int, input().split()[:n]))

arr.sort()

print(arr[-k])