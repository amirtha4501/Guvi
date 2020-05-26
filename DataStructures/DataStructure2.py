n = int(input())

arr = list(map(int, input().split()))

rev_arr = arr[::-1]
print(*rev_arr, sep='->')