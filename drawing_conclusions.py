#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions
# Use the space below to address questions on datasets `clean_08.csv` and `clean_18.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 3*.

# In[1]:


# load datasets
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')
df_08.head(50)


# ### Q1: Are more unique models using alternative sources of fuel? By how much?

# In[2]:


#"Let's first look at what the sources of fuel are and which ones are alternative sources."
df_a = df_08.query('fuel != "Gasoline"')
df_08.fuel.value_counts()


# In[3]:


df_b = df_18.query('fuel != "Gasoline"')
df_18.fuel.value_counts()


# In[4]:


# how many unique models used alternative sources of fuel in 2008
alt_08 = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08


# In[5]:


# how many unique models used alternative sources of fuel in 2018
alt_18 = df_18.query('fuel in ["Electricity", "Ethanol"]').model.nunique()
alt_18


# In[6]:


plt.bar(['2008', '2018'], [alt_08, alt_18])
plt.title('Number of Unique Models Using Alternative Fuels')
plt.xlabel('Year')
plt.ylabel('Number of Unique Models');


# In[ ]:


There are 24 more unique models using alternative fuels in 2018 than in 2008 showing a significant increase


# In[7]:


# total unique models each year
total_08 = df_08.model.nunique()
total_18 = df_18.model.nunique()
total_08, total_18


# In[55]:


prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18


# In[58]:


plt.bar(['2008', '2018'], [prop_08, prop_18])
plt.title("Proportion by model using alternative fuels")
plt.xlabel('Year')
plt.xlabel('Number of Unique Models')


# ### Q2: How much have vehicle classes improved in fuel economy?  

# In[ ]:


Average fuel economy for each vehicle class


# In[9]:


vehicle_08 = df_08.groupby('veh_class').cmb_mpg.mean()
vehicle_08


# In[10]:


vehicle_18 = df_18.groupby('veh_class').cmb_mpg.mean()
vehicle_18


# In[11]:


#Difference between each vehicle class
diff = vehicle_18 - vehicle_08
diff


# In[15]:


# Only vehicle class that exist in both will be plotted
diff.dropna(inplace=True)
plt.subplots(figsize=(8, 5))
plt.bar(diff.index, diff)
plt.title('Fuel economy difference between 2008 and 2018')
plt.xlabel('Vehicle class')
plt.ylabel('Increase in Avg Cmb')


# ### Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

# In[17]:


#Analyze df_08 by smart way classification and explore the data
df_08.smartway.unique()


# In[19]:


# Get all smart way vehicles for df_08
smart_08 = df_08.query('smartway == "yes"')
smart_08


# In[32]:


#Explore smart_08
s_08 = smart_08.describe()


# In[27]:


df_18.query('smartway == "Yes"')


# In[21]:


#Analyze df_08 by smart way classification and explore the data
df_18.smartway.unique()


# In[29]:


#Get all smartway vehicles for df_18
smart_18 = df_18.query('smartway in ["Yes", "Elite"]')


# In[31]:


# Explore smartway 
s_18 = smart_18.describe()


# In[36]:


# Further explore

df_18.smartway.value_counts()


# ### Q4: What features are associated with better fuel economy?

# In[38]:


# Explore cmb and other features for df_08
top_08 = df_08.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()


# In[39]:


# Explore cmb in comparison with other features for df_18
top_18 = df_18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()

