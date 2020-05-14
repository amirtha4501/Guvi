array = list(str(input()))
# array = list(arr)
i = 0
while i < len(array) - 1:
    t = array[i]
    array[i] = array[i + 1]
    array[i + 1] = t
    i += 2

for i in range(len(array)-1):
    print(array[i], end='')
print(array[-1])