#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[11]:


data=pd.read_excel("D:\dataset\Sample - Superstore.xls")#here we are loading a excel file 


# In[12]:


data


# In[13]:


data.head()#top 5 rows displayed by head if in head we display any no it will diplay that much of rows


# In[14]:


data.tail()


# In[15]:


import pandas as pd
datw=pd.read_excel("\D:\dataset\products.xls")#unknown error while loading a file


# In[16]:


data.shape


# In[17]:


datw=pd.read_excel("products.xlsx")#in this we have uploaded a datset to notebook page


# In[18]:


datw


# In[19]:


datw.shape#provide the shape of dataset


# In[20]:


data.columns.values#no of columns present in dataset


# In[21]:


data.info()


# In[22]:


dw=pd.read_excel("D:\dataset\orders.xls")#previous error


# In[23]:


data["Row ID"].head(8)


# In[24]:


data.loc[[2,3]].head()


# In[25]:


data.loc[2,["Row ID","Order ID"]]


# In[26]:


import numpy as np
data={'A':[np.nan,2,np.nan,0],'b':[2,3,4,np.nan],'c':[np.nan,3,np.nan,3],'d':[3,4,5,6]}


# In[27]:


data


# In[28]:


df4=pd.DataFrame(data=data)


# In[29]:


df4


# In[30]:


df4=df4[df4['c'].isnull()==False]


# In[31]:


df4


# In[32]:


df4.reset_index()


# In[33]:


df4


# In[34]:


df4.reset_index(drop=True)


# In[35]:


doc=pd.read_excel("D:\dataset\ x.xls")


# In[36]:


data


# In[37]:


get_ipython().system('pip install df2gspread')


# In[38]:


from df2gspread import df2gspread as d2g


# In[39]:


spreadsheet_ID='1hvUFygc8enAM9aJMaJSQ7-C4UnyHF6kwVhlAo-2whT4'


# In[40]:


sheetname="ankit"


# In[41]:


d2g.upload(datw,spreadsheet_ID,sheetname)


# In[44]:


data


# In[46]:


data=pd.read_excel("D:\dataset\Sample - Superstore.xls")
data


# In[47]:


data['month'] = data['Order Date'].apply(lambda z:z.month)


# In[48]:


data


# In[49]:


data.columns


# In[52]:


data[(data['City'] =='Henderson')]


# In[60]:


data[(data['City'] =='Henderson')&(data['Ship Mode']=='Second Class')]


# In[61]:


data.describe


# In[63]:


orders = pd.read_excel("D:\dataset\orders.xlsx")


# In[64]:


orders


# In[65]:


products =pd.read_excel("D:\dataset\products.xlsx")


# In[66]:


products


# In[70]:


set2=set(products.columns)
set1=set(orders.columns)


# In[71]:


set1.intersection(set2)


# In[72]:


data.merge(products,on=['Order ID'],how='left')


# In[75]:


f={'a':[2,3,34,54],'b':[56,65,54,76]}


# In[78]:


f


# In[79]:


frame=pd.DataFrame(f)


# In[80]:


frame


# In[81]:


f={'a':[20,39,0,5],'b':[5,65,4,6]}


# In[82]:


f


# In[83]:


frame1=pd.DataFrame(f)


# In[84]:


frame1


# In[89]:


q=pd.concat([frame,frame1])#concatination of 2 data set


# In[90]:


q


# In[91]:


import numpy as np
w=np.vstack([frame,frame1])#as vstack is used only by numpy but numpy works in backend of pandas


# In[92]:


w


# In[ ]:




