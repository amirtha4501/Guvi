number_of_lists = int(input())
for list_number in range(1, number_of_lists+1):
    current_list = []
    number_of_values = int(input())
    for value_number in range(number_of_values):
        value = map(int,input().split())
        current_list.append(value)
    print(str(current_list))
    print(str(sorted(current_list)))