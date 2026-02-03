x=int(input("enter number"))
new=""
x=bin(x)
newx=x[2:]
for i in newx:
    if i=="1":
        new=new+"0"
    if i=="0":
        new=new+"1"
new=int(new,2)+1
new=bin(new)
print(new)
