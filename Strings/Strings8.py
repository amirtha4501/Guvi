s = str(input())
l = len(s) 
mid = l//2

if (s[mid]=="M" or s[mid]=="m") and (s[0]=="a" or s[0]=="A") and (s[-1]=="z" or s[-1]=="Z"):
  print(1)
else:
  print(0)