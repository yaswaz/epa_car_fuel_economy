#!/usr/bin/env python
# coding: utf-8

# # Filter, Drop Nulls, Dedupe
# Use `data_08_v1.csv` and `data_18_v1.csv`. 

# In[12]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v1.csv')
df_18 = pd.read_csv('data_18_v1.csv')
df_18.head()


# In[13]:


# view dimensions of dataset
df_08.shape


# In[14]:


# view dimensions of dataset
df_18.shape


# ## Filter by Certification Region

# In[15]:


# filter datasets for rows following California standards
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')


# In[16]:


# confirm only certification region is California
df_08['cert_region'].unique()


# In[17]:


# confirm only certification region is California
df_18['cert_region'].unique()


# In[18]:


# drop certification region columns form both datasets
df_08.drop(['cert_region'], axis=1, inplace=True)
df_18.drop(['cert_region'], axis=1, inplace=True)
df_08.head(1)


# In[19]:


df_08.shape


# In[20]:


df_18.shape


# ## Drop Rows with Missing Values

# In[21]:


# view missing value count for each feature in 2008
df_08.isnull().values.sum()


# In[22]:


# view missing value count for each feature in 2018
df_18.isnull().values.sum()


# In[23]:


# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)


# In[24]:


# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()


# In[25]:


# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()


# ## Dedupe Data

# In[26]:


# print number of duplicates in 2008 and 2018 datasets
sum(df_08.duplicated())
sum(df_18.duplicated())


# In[27]:


# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)


# In[28]:


# print number of duplicates again to confirm dedupe - should both be 0
sum(df_08.duplicated())
sum(df_18.duplicated())


# In[ ]:


# save progress for the next section
df_08.to_csv('data_08_v2.csv', index=False)
df_18.to_csv('data_18_v2.csv', index=False)

