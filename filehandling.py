n= int(input("number of students: "))
names=[]

f=open("names.txt" , "w")

for i in range(n):
    name=input("enter your name: ")
    names.append(name)
    f.write(name+"\n")
f.close()