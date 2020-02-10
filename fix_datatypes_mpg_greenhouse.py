#!/usr/bin/env python
# coding: utf-8

# ## Fix `city_mpg`, `hwy_mpg`, `cmb_mpg` datatypes
#     2008 and 2018: convert string to float
#
# Load datasets `data_08_v4.csv` and `data_18_v4.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 2*.

# In[1]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v4.csv')
df_18 = pd.read_csv('data_18_v4.csv')


# In[3]:


df_18.head()


# In[4]:


# convert mpg columns to floats
mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']
for c in mpg_columns:
    df_18[c] = df_18[c].astype(float)
    df_08[c] = df_08[c].astype(float)


# ## Fix `greenhouse_gas_score` datatype
#     2008: convert from float to int

# In[6]:


# convert from float to int
df_08['greenhouse_gas_score'] = df_08.greenhouse_gas_score.astype(int)


# ## All the dataypes are now fixed! Take one last check to confirm all the changes.

# In[7]:


df_08.dtypes


# In[8]:


df_18.dtypes


# In[9]:


df_08.dtypes == df_18.dtypes


# In[10]:


# Save your final CLEAN datasets as new files!
df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)
