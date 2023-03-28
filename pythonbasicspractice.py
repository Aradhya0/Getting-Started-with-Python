#!/usr/bin/env python
# coding: utf-8

# In[2]:


rows = 6

for num in range(rows):

    for i in range(num):

        print(num, end=" ") # print number

    # line after each row to display pattern correctly

    print(" ")


# In[8]:


rows = 5

for i in range(5):

    for j in range(5):

        print("*", end=' ')

    print("\r")


# In[16]:


#rows = 5

for i in range(5):
    for j in range(5):
        print(i+1, end='')
    print("\r")


# In[17]:


for i in range(5):
    for j in range(5):
        print(j+1, end='')
    print("\r")


# In[25]:


for i in range(6,1,-1):
    for j in range(5,0,-1):
        print(i-1, end='')
    print("\r")


# ##### 

# In[ ]:




