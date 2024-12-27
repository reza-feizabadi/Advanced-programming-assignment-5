import math
a = 2
b = 8
c = 4
discriminant =((b*b) - (4.0*a*c))
if discriminant < 0:
    print('No real roots')
else:
    d = math.sqrt(discriminant)
    print((-b + d) / (2.0 * a))
    print((-b - d) / (2.0 * a))
