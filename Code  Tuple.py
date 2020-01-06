Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts


#code


y=input("enter the name of the file:")
z="C:\\Users\\Hp\\Desktop\\"
x=z+y
lsit={}
try:
    file=open(x)
except:
    print("file not found")
for line in file:
    line=line.rstrip()
    if line.startswith("From "):
        list=line.split()
        sublist=list[5]
        sublist=sublist.split(":")
        stime=sublist[0]
        lsit[stime]=lsit.get(stime,0)+1
lsit=sorted(lsit.items())     
for k,v in lsit:
    print(k,v)
