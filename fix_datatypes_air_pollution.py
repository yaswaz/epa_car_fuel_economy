#!/usr/bin/env python
# coding: utf-8

# # Fixing `air_pollution_score` Data Type
# - 2008: convert string to float
# - 2018: convert int to float
#
# Load datasets `data_08_v3.csv` and `data_18_v3.csv`.

# In[1]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v3.csv')
df_18 = pd.read_csv('data_18_v3.csv')


# In[2]:


# try using pandas' to_numeric or astype function to convert the
# 2008 air_pollution_score column to float -- this won't work
df_08['air_pollution_score'] = df_08.air_pollution_score.astype(float)


# # Figuring out the issue
# Looks like this isn't going to be as simple as converting the datatype. According to the error above, the air pollution score value in one of the rows is "6/4" - let's check it out.

# In[3]:


df_08[df_08.air_pollution_score == '6/4']


# # It's not just the air pollution score!
# The mpg columns and greenhouse gas scores also seem to have the same problem - maybe that's why these were all saved as strings! According to [this link](http://www.fueleconomy.gov/feg/findacarhelp.shtml#airPollutionScore), which I found from the PDF documentation:
#
#     "If a vehicle can operate on more than one type of fuel, an estimate is provided for each fuel type."
#
# Ohh... so all vehicles with more than one fuel type, or hybrids, like the one above (it uses ethanol AND gas) will have a string that holds two values - one for each. This is a little tricky, so I'm going to show you how to do it with the 2008 dataset, and then you'll try it with the 2018 dataset.

# In[4]:


# First, let's get all the hybrids in 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
hb_08


# Looks like this dataset only has one! The 2018 has MANY more - but don't worry - the steps I'm taking here will work for that as well!

# In[5]:


# hybrids in 2018
hb_18 = df_18[df_18['fuel'].str.contains('/')]
hb_18


# We're going to take each hybrid row and split them into two new rows - one with values for the first fuel type (values before the "/"), and the other with values for the second fuel type (values after the "/"). Let's separate them with two dataframes!

# In[6]:


# create two copies of the 2008 hybrids dataframe
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle

# Each one should look like this
df1


# For this next part, we're going use pandas' apply function. See the docs [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html).

# In[7]:


# columns to split by "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])


# In[8]:


# this dataframe holds info for the FIRST fuel type of the hybrid
# aka the values before the "/"s
df1


# In[9]:


# this dataframe holds info for the SECOND fuel type of the hybrid
# aka the values after the "/"s
df2


# In[10]:


# combine dataframes to add to the original dataframe
new_rows = df1.append(df2)

# now we have separate rows for each fuel type of each vehicle!
new_rows


# In[11]:


# drop the original hybrid rows
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows
df_08 = df_08.append(new_rows, ignore_index=True)


# In[12]:


# check that all the original hybrid rows with "/"s are gone
df_08[df_08['fuel'].str.contains('/')]


# In[13]:


df_08.shape


# # Repeat this process for the 2018 dataset

# In[14]:


# create two copies of the 2018 hybrids dataframe, hb_18
df1 = hb_18.copy()
df2 = hb_18.copy()


# ### Split values for `fuel`, `city_mpg`, `hwy_mpg`, `cmb_mpg`
# You don't need to split for `air_pollution_score` or `greenhouse_gas_score` here because these columns are already ints in the 2018 dataset.

# In[15]:


# list of columns to split
split_columns = ['fuel', 'city_mpg', 'hwy_mpg', 'cmb_mpg']


# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])


# In[16]:


# append the two dataframes
new_rows = df1.append(df2)

# drop each hybrid row from the original 2018 dataframe
# do this by using pandas' drop function with hb_18's index
df_18.drop(hb_18.index, inplace=True)

# append new_rows to df_18
df_18 = df_18.append(new_rows, ignore_index=True)


# In[17]:


# check that they're gone
df_18[df_18['fuel'].str.contains('/')]


# In[18]:


df_18.shape


# ### Now we can comfortably continue the changes needed for `air_pollution_score`! Here they are again:
# - 2008: convert string to float
# - 2018: convert int to float

# In[20]:


# convert string to float for 2008 air pollution column
df_08['air_pollution_score'] = df_08.air_pollution_score.astype(float)


# In[21]:


# convert int to float for 2018 air pollution column
df_18['air_pollution_score'] = df_18.air_pollution_score.astype(float)


# In[22]:


df_08.to_csv('data_08_v4.csv', index=False)
df_18.to_csv('data_18_v4.csv', index=False)



# In[24]:


df_18.shape
