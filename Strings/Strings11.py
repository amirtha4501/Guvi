original_string = str(input())

list1 = original_string.split()
list2 = []

for word in list1:
  if list2 == []:
    list2.append(word)
  elif list2[-1] != word:
    list2.append(word)
  elif list2[-1] == word:
    list2.remove(word)
  else:
    pass
    
new_string = ' '

if list2 != []:
  print(new_string.join(list2))
else:
  print(-1)