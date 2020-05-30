n = int(input())
s = list(map(str, input().split()[:n]))

print(*sorted(s), sep=' ')