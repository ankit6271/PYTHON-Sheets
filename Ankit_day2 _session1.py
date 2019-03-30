#!/usr/bin/env python
# coding: utf-8

# # If else

# In[2]:


"'to calculate the sum of 2 nos and provide the grades'"
x=int(input("enter value of x"))
y=int(input("enter value of y"))
z=x+y
if(z>=10):                      #value of z when z is greater than 10
    print("grade A")
elif(z==10):                    #value of z when z is equal to 10
    print("grade B")
else:
    print("grade C")            #value when less than 10
    


# In[3]:


range(2,30,1) #starting,ending,inc/dec


# # to initialize the list firstly

# In[1]:


marks=[int(input("value of maths")),int(input("value of physics")),int(input("value of chemistry"))]


# # to add values to empty list

# In[3]:


marks=[]
marks.append(int(input("value of maths")))
marks
marks.append(int(input("value of phy")))
marks


# In[4]:


no=0
q=int(input("enter the no of students"))
while(q!=no):
    x=input(" roll no for student")
    students={x:[int(input("value of maths for 1 student")),int(input("value of physics for 1 student")),int(input("value of chemistry for 1 student"))]}
    q=q-1
students


# # palindrome

# In[1]:


y=input("enter the name to check for palindrome\t")
for i in range(len(y)):
    


# # functions

# In[38]:


x=int(input("enter value of x "))
y=int(input("enter value of y "))
list=[23,43,21,98]
list
def yup(x,y):
    if(x<y):
        print("x is small")
    else:
        print("y is small")
    return 1
def minimummarks(list):
  
    return min(list)
def maximummarks(list):
    y=max(list)
    return y
yup (x,y)
print("minimum marks",minimummarks(list))
aq=maximummarks(list)
print("maximum value",aq)
pos = list.index(aq)
print("position of grts no is",pos)


# # datetime

# In[35]:


import datetime as dt
date=dt.datetime.now()
date1 = str(date)
def funcdate(date1):
    dat1=date1[:10:1]
    return dat1
def functime(date1):
    time1=date1[10:26:1]
    return time1
dat1=funcdate(date1)
time1=functime(date1)
print(dat1)
print(time1)


# In[34]:


import datetime as dt
date=dt.datetime.now()
date1=str(date)
print(date1)


# # NUMPY

# In[1]:


import numpy#import is a keyword


# In[42]:


import numpy as np#to perform operation faster
list1=[1,2,23]
a=np.array(list1)
print(a)
type(a)


# In[43]:


print(a.dtype)


# In[51]:


list=[1,2,3,4]
list1=[3,5,67,77]
a=np.array([list,list1])
a


# In[7]:


type(a)


# In[9]:


a.shape


# In[12]:


a.shape=(4,2)
print(a)


# In[47]:


x=np.array([-2,-4,7,10,12,12])
x.shape


# In[48]:


x.shape=(3,2)


# In[49]:


x


# In[24]:


print(x)


# In[27]:


np.reshape=(x,(2,3))
np.reshape


# In[29]:


import pandas as pd


# In[35]:



name=pd.Series([23,34,55])
name


# In[36]:


name=pd.Series(["anny","ram"])#0 and 1 are index
name


# In[38]:


name=pd.Series(name)#shift+tab for documentation
name


# In[42]:


#to change the index ie 0 and 1
ind=pd.Series(name,index=["stud","ram"])
ind


# In[51]:


list2=pd.Series([1,2,3,4])
list1=pd.Series([14,23,3,24,7])#nan is not applicable number
#when series is not same it will show float as nan is predefined as float
l=list2+list1
l


# In[52]:


type(l)


# In[53]:


#to apply a function 2 a series use lambda



l.mean()#for mean value


# In[55]:


w=l[l>l.mean()]
w


# # data frames

# In[30]:



import pandas as pd
dataframe=pd.DataFrame(["lalit","ankit"])
dataframe


# In[31]:


dataframe=pd.DataFrame(["lalit","ankit"],["lsl","snny"],columns = ['a'])
dataframe


# In[32]:


dataframe.to_csv("anny.csv")


# In[33]:


dataframe.to_excel("anny.xls")


# In[34]:


s=pd.read_csv("anny.csv")
s


# In[40]:


y=pd.read_excel("anny.xls")
y


# In[ ]:




