#!/usr/bin/env python
# coding: utf-8

# Importing Libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Data overview

# In[4]:


data=pd.read_csv("swiggy_banglore_outlet_data_analysis.csv")
data.head()


# In[5]:


data.info()


# In[6]:


data.shape


# In[7]:


data.isnull().sum()


# In[8]:


data['Rating'].values


# In[9]:


data.describe()


# Data Cleaning and Replacement

# In[11]:


data['Rating']=data['Rating'].str.replace('--','0')


# In[12]:


data['Rating']=data['Rating'].astype("float")


# In[13]:


data['Rating'].values


# In[14]:


data.dtypes


# In[15]:


data.info()


# In[16]:


data.head()


# In[17]:


data['Cost_for_Two'].values


# In[18]:


data['Cost_for_Two']=data['Cost_for_Two'].str.replace('₹','')


# In[19]:


data['Cost_for_Two']=data['Cost_for_Two'].astype("float")


# In[20]:


data['Cost_for_Two'].values


# Cleaned Data

# In[22]:


data.dtypes


# In[23]:


data.info()


# In[24]:


data.describe()


# In[25]:


data.head()


# Data Analysis 

# In[27]:


plt.figure(figsize=(5,4))
data['Rating'].plot.hist(bins=8)


# In[28]:


plt.figure(figsize=(7,4))
data['Cost_for_Two'].plot.hist(bins=8)


# In[29]:


data.sort_values(by='Rating', ascending=False)
plt.figure(figsize=(7,3))
plt.scatter(data['Shop_Name'].head(),data['Rating'].head(),marker='D',c=data['Rating'].head())
plt.colorbar()
plt.title("Shop Names with respect to their Ratings")
plt.ylabel("RATINGS")
plt.xlabel("SHOP NAMES")
plt.tight_layout()
plt.show()


# In[30]:


data.sort_values(by='Cost_for_Two', ascending=True)
plt.figure(figsize=(15,5))
plt.barh(width=data['Cost_for_Two'].head(),y=data['Cuisine'].head(),color='grey')
plt.title("Cuisines with respect to their Costs")
plt.ylabel("CUISINES")
plt.xlabel("COSTS")
plt.tight_layout()
plt.show()


# In[31]:


plt.pie(labels=data['Cuisine'].head(),x=data['Cost_for_Two'].head(),shadow=True,explode=(0,0,0,0.1,0.1))
plt.figure(figsize=(7,4))
plt.show()

