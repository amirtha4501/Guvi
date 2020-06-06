n = str(input())

def binToHexConverter(n):
  hexa_dec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
  res = ""
  
  dec = int(n,2)
  
  while dec>0:
    rem = dec % 16
    dec -= rem
    dec //= 16
    res += str(hexa_dec[rem])
    
  print(res[::-1])
  
binToHexConverter(n)