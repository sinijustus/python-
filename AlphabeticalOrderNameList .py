num=int(input("enter the number of students:"))
names=[]
for i in range(0,num):
    items=input("enter the names:")
    names.append(items)
names.sort()
for x in names:
    print(x)
