# n, m = map(int, input().split())
# print(n*m)

stack = [] 

# Traversing the Expression  
for char in expr: 
    if char in ["(", "{", "["]: 

        # Push the element in the stack  
        stack.append(char) 
    else: 

        if stack: 
            stack_char = stack.pop()
            
        else:
            print(0)

#         current_char = stack.pop() 
#         if current_char == '(': 
#             if char != ")": 
#                 # return False
#                 pass
#         if current_char == '{': 
#             if char != "}": 
#                 # return False
#                 pass
#         if current_char == '[': 
#             if char != "]": 
#                 # return False
#                 pass

# # Check Empty Stack 
# if stack: 
#     return False
# return True


