string, k = input().split(maxsplit=1)
k = int(k)
new_string = ''
for index, value in enumerate(string):
  if index%k==0:
    # string = string.replace(string[i+1], string[i+1].upper())  
    new_string += value.upper()
  else:
    new_string += value
print(new_string)
