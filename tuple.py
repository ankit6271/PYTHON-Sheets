list1=[]
list3=[]
a=int(input("enter x"))
b=int(input("enter y"))
c=int(input("enter z"))
x=a
y=b
z=c
N=int(input("enter n"))
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=N:
                list1=[i,j,k]
                list3=list3+[list1]
print(list3)
    
    