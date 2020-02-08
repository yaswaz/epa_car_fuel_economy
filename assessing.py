#!/usr/bin/env python
# coding: utf-8

# # Assessing
# Use the space below to explore `all_alpha_08.csv` and `all_alpha_18.csv` 

# In[3]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df_08 = pd.read_csv('all_alpha_08.csv')
df_08.head()


# In[4]:


df_08. describe()


# In[5]:


sum(df_08.info())


# In[6]:


df_08.isnull().sum()


# In[7]:


sum(df_08.duplicated())


# In[8]:


df_08.dtypes


# In[9]:


df_08.nunique()


# In[10]:


df_18 = pd.read_csv('all_alpha_18.csv')
df_18.head()


# In[11]:


df_18.info()


# In[12]:


sum(df_18.duplicated())


# In[13]:


df_18.isnull().sum()


# In[14]:


df_18.dtypes


# In[15]:


df_18.nunique()


# In[16]:


df_18[df_18['Fuel'] == 'Gas']


# In[ ]:




