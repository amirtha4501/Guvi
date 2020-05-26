n = int(input())

arr1 = list(map(int, input().split()[:n]))
arr2 = list(map(int, input().split()[:n]))

arr = arr1 + arr2

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

mid = len(arr)//2
sum = arr[mid-1] + arr[mid] 

print(sum)