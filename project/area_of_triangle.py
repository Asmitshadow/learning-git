#"""" a= first side
# b= second side
# c= third side
# perimeter(s)= (a+b+c)/2
# area= square root(s*(s-a)*(s-b)*(s-c))"""
a= int(input("first side of triangle:  "))
b= int(input("second side of triangle:  "))
c= int(input("third side of triangle:  "))
s = (a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle", round(area, 2))

