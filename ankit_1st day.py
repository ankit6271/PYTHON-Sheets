#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("3")


# In[4]:


a=input()


# In[5]:


print(a)


# In[ ]:


for i in range(4):
      mini=0
      minpos=-1
      if(mini>list.i):
          min=list.i
          minpos=i
          i=i+1
  return minpos


# In[8]:


for i in range (5):
    print("a")


# In[9]:


y=input("enter a no")


# In[10]:


print(y)


# y=int(input("enter a no"))
# print(y)

# # hello world

# In[13]:


w=09
print(type(w))


# # welcome 2 the ques 

# In[14]:


print("welcoming yourself in the data science using python")


# In[56]:


hindi=90
english=23
maths=56
ds=56
m1=int(input("enter marks for m1")) 
m2=int(input("enter marks for m2"))
sum=hindi+english+maths+ds+m1+m2
print(sum)
print("average=",sum//6) #//is used for floor values


# # list

# In[1]:


w=["anny",2,"lalit"]
print(w)
#collection of heterogenous mutable items


# In[41]:


print(w.count("ankit"))


# In[42]:


# as list is mutuable as it can be changed so we can assign a new value to the list
# so 
w[0]='ram'
w


# In[43]:


w.append("ramu")
w


# In[44]:


w.remove("ramu")
w


# In[45]:


w.pop()


# In[46]:


w


# # dictionary

# In[5]:


dictionary={23:{'eng':87,'maths':99,'comp':99},24:{'eng':7,'maths':79,'comp':96}}
dictionary
        


# In[8]:


print(dictionary[24])


# In[9]:


dictionary[23]


# In[10]:


dictionary[23]['maths']


# In[11]:


dictionary[24]['eng']


# In[62]:


list=[1,2,3,4,5]
print (list)


# In[67]:


maxi=max(list)#for maximum value ina list
maxi


# # tuples

# In[58]:


tuple_var=(1,"ankit",34,98)
#as heterogenous data str diff values can be kept


# In[60]:


tuple_var


# In[51]:


#as it is not mutable so we cannot change the values of the variable inside the tuple and will throw an error
tuple_var[0]="asian"


# In[54]:


tuple_var.append("ram")
#as not mutable


# In[ ]:




