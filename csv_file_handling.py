import csv


n= int(input("number of students: "))
names=[]
marks=[]

f=open("data.csv", "w")
cols= ["Names","Marks"]
writer= csv.writer(f)
# writer.writerow(cols) 
 
for i in range(n):
    name=input("enter your name: ")
    mark=float(input("enter your marks: "))
    names.append(name)
    marks.append(mark)
    
    # writer.writerow([name,mark])
record=list(zip(names,marks))
writer.writerows(record)
f.close()