# The sum of first n natural numbers
def sumOfNaturals(n):
    sum = 0
    i = 1

    while i <= n:
        sum += i
        i += 1
    return sum 

n = int(input())

if n < 100000:
    print(sumOfNaturals(n))