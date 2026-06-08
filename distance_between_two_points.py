#Distance between two points = sqrt((x2-x1)^2 + (y2-y1)^2)
import math
x2= float(input("enter the value of x2: "))
x1= float(input("enter the value of x1:"))
a=x2-x1
y2= float(input("enter the value of y2:"))
y1= float(input("enter the value of y1:"))
b=y2-y1
c=a**2+b**2
sqrt = math.sqrt(c)
print(f"the distance between two points :{sqrt}")

