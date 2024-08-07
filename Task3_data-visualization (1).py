#!/usr/bin/env python
# coding: utf-8

# Importing neccesary libraries

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt 


# Reading csv file with a help of read_csv function of pandas and extracting first 20 rows to get overview of the dataset

# In[45]:


data= pd.read_csv("householdtask3.csv")
data.head(20)


# Line chart to get insights of Income and Expenditure both together

# In[91]:


plt.figure(figsize=(7,3))
plt.plot(data['income'],'g')
plt.plot(data['expenditure'],'r')
plt.title('Line chart depicting - Income and Expenditure')
plt.legend(['Income','Expenditure'])
plt.show()


# Scatter chart to get yearly information about owned water management property

# In[131]:


plt.figure(figsize=(7,3))
plt.scatter(data['year'],data['own_wm_prop'], c=data['own_wm_prop'],marker='D')
plt.colorbar()
plt.title('Scatter chart depicting - Year and Own Water management property')
plt.xlabel('Year')
plt.ylabel('Own_wm_prop')
plt.show()


# Bar graph to know the yearly growth with respect to income

# In[133]:


plt.figure(figsize=(7,3))
plt.bar(data['year'],data['income'],color="grey")
plt.title('Bar graph depicting - Year and Income')
plt.xlabel('Year')
plt.ylabel('Income')
plt.show()


# Horizontal bar graph for a clear vision about total house holdings with respect to year

# In[137]:


plt.figure(figsize=(7,3))
plt.barh(data['year'],data['tot_hhs'],color="y")
plt.title('Horizontal Bar graph depicting - House holds in corresponding year')
plt.xlabel('Total House Holds')
plt.ylabel('Year')
plt.show()


# In[ ]:


Histogram showing all the owned property 


# In[159]:


plt.figure(figsize=(7,3))
plt.hist(data['own_prop'])
plt.title('Histogram depicting - own property')
plt.show()

