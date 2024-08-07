#!/usr/bin/env python
# coding: utf-8

# Importing libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# Data Overview

# In[4]:


data=pd.read_csv('USvideos.csv')
data.head()


# In[5]:


data.shape


# Removing Duplicate Values

# In[7]:


data.drop_duplicates(inplace=True)
data.shape


# Mathematical Aspects of Data

# In[9]:


data.describe()


# In[10]:


data.info()


# Dropping un-useful Columns from Data

# In[11]:


data=data.drop(columns=['thumbnail_link','description'])


# In[12]:


data.info()


# Extracting year , day and month from the date column in proper format

# In[14]:


data['trending_date']=data['trending_date'].apply(lambda x : dt.datetime.strptime(x,'%y.%d.%m'))


# In[15]:


data.head(3)


# Extracting Time in proper format from publish time column 

# In[17]:


data['publish_time']=pd.to_datetime(data['publish_time'])


# In[18]:


data.head(3)


# Setting up new columns for each extracted month , day and hour from publish month column

# In[20]:


data['publish_month']=data['publish_time'].dt.month
data['publish_day']=data['publish_time'].dt.day
data['publish_hour']=data['publish_time'].dt.hour


# New Data overview with new columns and columns in proper format now

# In[22]:


data.head()


# Extracting the category id and assigning the type of category to each in new column 

# In[24]:


sorted(data['category_id'].unique())


# In[25]:


data['category_name']=np.nan
data.loc[(data['category_id'] == 1),'category_name']='Film and Animation'
data.loc[(data['category_id'] == 2),'category_name']='Autos and Vehicles'
data.loc[(data['category_id'] == 10),'category_name']='Music'
data.loc[(data['category_id'] == 15),'category_name']='Pets and Annimals'
data.loc[(data['category_id'] == 17),'category_name']='Sports'
data.loc[(data['category_id'] == 19),'category_name']='Travel and Events'
data.loc[(data['category_id'] == 20),'category_name']='Gaming'
data.loc[(data['category_id'] == 22),'category_name']='People and Blogs'
data.loc[(data['category_id'] == 23),'category_name']='Comedy'
data.loc[(data['category_id'] == 24),'category_name']='Entertainment'
data.loc[(data['category_id'] == 25),'category_name']='News and Politics'
data.loc[(data['category_id'] == 26),'category_name']='How to and Style'
data.loc[(data['category_id'] == 27),'category_name']='Education'
data.loc[(data['category_id'] == 28),'category_name']='Science and Technology'
data.loc[(data['category_id'] == 29),'category_name']='Non Profits and Activism'
data.loc[(data['category_id'] == 30),'category_name']='Movies'
data.loc[(data['category_id'] == 43),'category_name']='Shows'


# In[26]:


data.head(2)


# EXPLORATORY DATA ANALYSIS

# In[28]:


plt.figure(figsize=(9,4))
data['year']=data['publish_time'].dt.year
yearly_counts=data.groupby('year')['video_id'].count()
yearly_counts.plot(kind='bar',xlabel='Year',ylabel='Total Publish Count',title='Total Publish Video Per Year',color='grey',edgecolor='k')
plt.show()


# In[29]:


plt.figure(figsize=(9,4))
yearly_views=data.groupby('year')['views'].sum()
yearly_views.plot(kind='bar',xlabel='Year',ylabel='Total views', title='Total views per year',color='orange',edgecolor='k')
plt.xticks(rotation=0)
plt.show()


# In[30]:


plt.figure(figsize=(9,4))
category_views=data.groupby('category_name')['views'].sum().reset_index()
top_categories=category_views.sort_values(by='views',ascending=False).head()
plt.bar(top_categories['category_name'],top_categories['views'],color='pink',edgecolor='k')
plt.xlabel('Category Name')
plt.ylabel('Total views')
plt.title('Top 5 Categories')
plt.show()


# In[31]:


plt.figure(figsize=(9,4))
sns.countplot(x='category_name',data=data, order=data['category_name'].value_counts().index,palette='viridis')
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()


# In[32]:


plt.figure(figsize=(9,4))
videos_per_hour=data['publish_hour'].value_counts().sort_index()
sns.barplot(x=videos_per_hour.index,y=videos_per_hour.values,palette='rocket')
plt.xlabel('Hour of Day')
plt.xticks(rotation=45)
plt.ylabel('No. of Videos')
plt.title('No. of Videos per Hour')
plt.show()


# In[33]:


plt.figure(figsize=(9,4))
data['publish_time']=pd.to_datetime(data['publish_time'])
data['publish_date']=data['publish_time'].dt.date
video_count_by_date=data.groupby('publish_date').size()
sns.lineplot(data=video_count_by_date,color='olive')
plt.xlabel('Publish Date')
plt.ylabel('No. of Videos')
plt.title('Videos Published Over Time')
plt.xticks(rotation=45)
plt.show()


# In[34]:


plt.figure(figsize=(9,4))
sns.scatterplot(data=data,x='views',y='likes',palette='viridis',hue='likes')
plt.title('Views VS Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.legend(loc='right')
plt.show()


# In[35]:


plt.figure(figsize=(14,8))
plt.subplots_adjust(wspace=0.2,hspace=0.4,top=0.9)
plt.subplot(2,3,1)
g=sns.countplot(x='comments_disabled',data=data,color='pink',edgecolor='k')
g.set_title('Comments Disabled')
plt.subplot(2,3,2)
g1=sns.countplot(x='ratings_disabled',data=data,color='yellow',edgecolor='k')
g1.set_title('Ratings Disabled')
plt.subplot(2,3,3)
g2=sns.countplot(x='video_error_or_removed',data=data,color='grey',edgecolor='k')
g2.set_title('Video Error or Removed')
plt.tight_layout()
plt.show()


# Checking correlation between Views and Likes column

# In[36]:


corr_matrix=data['views'].corr(data['likes'])
corr_matrix

