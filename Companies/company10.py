# import collections

# string = str(input())
# new_string = ''

# counter = collections.Counter(string)

# for i in counter:
#   val = i + str(counter[i])
#   new_string += val
  
# # print(new_string)
# print(counter.elements())

# import collections

# string = str(input())

# if len(string)<=100000:
#   counter = collections.Counter(string)

#   for i in counter:
#     val = i+str(counter[i])
#     print(val, end='')

from collections import OrderedDict

string = str(input())
st = ''

if len(string)<=100000:
  mydic = OrderedDict.fromkeys(string,0)
  
  for char in string:
    mydic[char] += 1
  
  for k,v in mydic.items():
    st += k + str(v)
  print(st, end='')