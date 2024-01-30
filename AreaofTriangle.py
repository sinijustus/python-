print("area of triangle")
a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))
p=a+b+c
s=p/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area=",area)
