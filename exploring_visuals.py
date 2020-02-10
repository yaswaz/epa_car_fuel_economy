#!/usr/bin/env python
# coding: utf-8

# # Exploring with Visuals
# Use `clean_08.csv` and `clean_18.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 3*.

# In[1]:


# load datasets
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# In[2]:


df_08.hist(figsize=(8,8));


# In[3]:


df_18.hist(figsize=(8,8));


# In[4]:


pd.plotting.scatter_matrix(df_08, figsize=(15,15));


# In[5]:


pd.plotting.scatter_matrix(df_18, figsize=(15,15));


# In[6]:


ax1 = df_08.plot(kind='scatter', x='greenhouse_gas_score', y='cmb_mpg', color='r')
ax2 = df_18.plot(kind='scatter', x='greenhouse_gas_score', y='cmb_mpg', color='b')
print(ax1 == ax2)


# In[7]:


ax1 = df_08.plot(kind='scatter', x='displ', y='cmb_mpg', color='r')
ax2 = df_18.plot(kind='scatter', x='displ', y='cmb_mpg', color='b')
print(ax1 == ax2)
