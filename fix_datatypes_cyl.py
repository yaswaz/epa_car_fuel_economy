#!/usr/bin/env python
# coding: utf-8

# # Fixing `cyl` Data Type
# - 2008: extract int from string
# - 2018: convert float to int
#
# Load datasets `data_08_v2.csv` and `data_18_v2.csv`. You should've created these data files in the previous section: *Filter, Drop Nulls, Dedupe*.

# In[1]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v2.csv')
df_18 = pd.read_csv('data_18_v2.csv')


# In[2]:


# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()


# Read [this](https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas) to help you extract ints from strings in Pandas for the next step.

# In[3]:


# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)


# In[4]:


# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()


# In[5]:


# convert 2018 cyl column to int
df_18['cyl'] = df_18.cyl.astype(int)


# In[6]:


df_18['cyl'].value_counts()


# In[7]:


df_08.to_csv('data_08_v3.csv', index=False)
df_18.to_csv('data_18_v3.csv', index=False)


# In[9]:


df_18.head()
