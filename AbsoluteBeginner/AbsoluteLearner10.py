# Find simple interest

# principal = int(input())  |
# rate = int(input())       |  -----> Getting input with three lines
# time = int(input())       |

# principal, time, rate = map(int, input().split()) -----> Getting inline inputs using map

# principal, time, rate = [int(i) for i in input().split()] -----> Getting inline inputs using for loop

# import ast
# principal, time, rate = ast.literal_eval(','.join(input().split()))
# print(principal,time, rate,sep='\n')


principal, time, rate = map(float, input().split())

interest = (principal * time * rate) / 100

print('%.2f' % interest)
