Str=input("enter a string:")
c=0
a=input("enter the letter to be searched:")
for i in Str:
    if(i==a):
        c=c+1 
print(" occurences of",a,"is",c)
