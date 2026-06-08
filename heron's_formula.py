#Heron's Formula (Area of Triangle) = sqrt(s * (s-a) * (s-b) * (s-c)) where s = (a+b+c)/2
import math
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))
sqrt= math.sqrt(d)
print(f"area of triangle using heron's formula: {sqrt}")
