# Sort the array based on the length and alphabetical in case of equal length 
n = int(input())
arr = [str(i) for i in input().split()[:n]]

arr = sorted(arr)
arr.sort(key=len)

print(*arr, sep=' ')