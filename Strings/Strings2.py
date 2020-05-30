# Count of the different char in string
import collections 

st = str(input())
myStr = collections.Counter(st)

if len(myStr) == 3:
  print("wonder")
else:
  print('-1')



# String Reverse with title case

s = str(input())
print(s[::-1].title())