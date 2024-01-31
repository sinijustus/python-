student={}
n=int(input("enter the number of students:"))
for i in range(0,n):
    name=input("enter the names:")
    age=input("enter age:")
    perc=input("enter percentage:")
    student[name]=age,perc
print(student)
