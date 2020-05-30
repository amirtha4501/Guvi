#  print only the consonants present in the string without affecting the sentence spacings
s = str(input())
vowels = 'aeiouAEIOU'

for char in vowels:
  s = s.replace(char,'')
print(s)

# Replace the ':' in string with none 
st = str(input())
print(s.replace(':',''))