st = str(input())
s = list(st)

mid = s[(len(s)-1)//2:(len(s)+2)//2]

if len(mid)==2:
  s[(len(s)-1)//2:(len(s)+2)//2] = '**'
  
else:
  s[(len(s)-1)//2:(len(s)+2)//2] = '*'
  
st = "".join(s)

print(st)
