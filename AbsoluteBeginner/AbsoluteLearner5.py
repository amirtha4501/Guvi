# Calculate circumference

import math

radius = float(input())

if radius >= 0:
    circumference = 2 * math.pi * radius
    print('%.2f' % circumference)
else:
    print("Error")