#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


location = "datasets/diamonds.csv"
df = pd.read_csv(location)


# In[8]:


df.head()


# In[9]:


df.tail()


# In[20]:


df.columns = ['ID','carat','cut','color','clarity','depth','table','price','length','width','depth']


# In[21]:


df.head()


# In[25]:


df.sort_values('price', ascending=False)


# In[ ]:




