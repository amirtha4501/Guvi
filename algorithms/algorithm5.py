n, m = map(int, input().split())

cost = 0
arr = []

if n<=1000 and m<=1000:
    for i in range(n):
        arr.append(str(input()))

    for word in arr:
        for i in range(len(word)-1):
            word = word.upper()
            if word[i] == word[i+1]:
                if word[i] == 'G':
                    cost += 3
                elif word[i] == 'R':
                    cost += 5
                else:
                    pass
print(cost)
