string = str(input())
n = len(string)
vow = ''
con = ''
if n<=10000:
  for char in string:
    if char in 'aeiouAEIOU':
      vow += char
    else:
      con += char
  
  string = vow + con
  print(string)