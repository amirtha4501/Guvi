# Check whether the year is leap year or not

year = int(input())

if year%400==0 or year%4==0 and year%100!=0:
	print("Y")
else:
	print("N")

# Area of a triangle

a = float(input())

area = (1/4) * ((3**0.5)*a*a)
print('%.2f' % area)