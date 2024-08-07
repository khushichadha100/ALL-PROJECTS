#!/usr/bin/env python
# coding: utf-8

# Importing all important libraries

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder , MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Getting overview of data

# In[4]:


data=pd.read_csv('housedata.csv')
data.head()


# Dataset dimensions and information needed for further exploration

# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


data.isnull().sum().sum() #checking null values


# In[9]:


data.duplicated().sum() #checking duplicated values


# Exploratory Data Analysis

# In[11]:


sns.pairplot(data=data,hue='furnishingstatus',palette='colorblind')
plt.show()


# Checking columns which needed to be encoded

# In[13]:


obj_col=data.select_dtypes(include='object')
obj_col_list=list(obj_col)
obj_col_list


# In[14]:


data['furnishingstatus'].unique()


# Using label encoding 

# In[16]:


le=LabelEncoder()
def label(data,columns):
  le = LabelEncoder()
  for column in columns:
    data[column] = le.fit_transform(data[column])
  return data

label(data, ['mainroad',
 'guestroom',
 'basement',
 'hotwaterheating',
 'airconditioning',
 'prefarea',
 'furnishingstatus'])


# Encoded Data now  ready to work

# In[18]:


data.head()


# All the mathematical aspects of dataset to check if outlier present or not

# In[20]:


data.describe()


# Outlier detection using Boxplot

# In[22]:


fig, axs = plt.subplots(2,3, figsize = (10,5))
plt1 = sns.boxplot(x=data['price'], ax = axs[0,0])
plt2 = sns.boxplot(x=data['area'], ax = axs[0,1])
plt3 = sns.boxplot(x=data['bedrooms'], ax = axs[0,2])
plt1 = sns.boxplot(x=data['bathrooms'], ax = axs[1,0])
plt2 = sns.boxplot(x=data['stories'], ax = axs[1,1])
plt3 = sns.boxplot(x=data['parking'], ax = axs[1,2])
plt.tight_layout()


# Outlier removal for column - price

# In[24]:


plt.figure(figsize=(5,3))
sns.boxplot(x=data['price'])
plt.title('price column outliers')
plt.show()


# Using IQR method 

# In[26]:


Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1
min_range= Q1-(1.5*IQR)
max_range= Q3+(1.5*IQR)
IQR , min_range , max_range


# In[27]:


data = data[(data['price'] >= Q1 - 1.5*IQR) & (data['price']<= Q3 + 1.5*IQR)]


# In[28]:


plt.figure(figsize=(5,3))
sns.boxplot(x=data['price'])
plt.title('price column outliers removed')
plt.show()


# Rechecking dataset dimensions

# In[30]:


data.shape


# Removing outliers from area column

# In[32]:


plt.figure(figsize=(5,3))
sns.boxplot(x=data['area'])
plt.title('area column outliers')
plt.show()


# In[33]:


Q1 = data['area'].quantile(0.25)
Q3 = data['area'].quantile(0.75)
IQR = Q3 - Q1
min_range= Q1-(1.5*IQR)
max_range= Q3+(1.5*IQR)
IQR , min_range , max_range


# In[34]:


data = data[(data['area'] >= Q1 - 1.5*IQR) & (data['area']<= Q3 + 1.5*IQR)]


# In[35]:


plt.figure(figsize=(5,3))
sns.boxplot(x=data['area'])
plt.title('area column outliers removed')
plt.show()


# In[36]:


data.head()


# In[37]:


data.shape


# Outliet Analysis Completed

# In[39]:


fig, axs = plt.subplots(2,3, figsize = (10,5))
plt1 = sns.boxplot(x=data['price'], ax = axs[0,0])
plt2 = sns.boxplot(x=data['area'], ax = axs[0,1])
plt3 = sns.boxplot(x=data['bedrooms'], ax = axs[0,2])
plt1 = sns.boxplot(x=data['bathrooms'], ax = axs[1,0])
plt2 = sns.boxplot(x=data['stories'], ax = axs[1,1])
plt3 = sns.boxplot(x=data['parking'], ax = axs[1,2])

plt.tight_layout()


# In[40]:


data.head(10)


# Checking correlation between data

# In[42]:


plt.figure(figsize=(15,7))
sns.heatmap(data.corr(),annot=True)


# In[43]:


sns.pairplot(data=data,hue='furnishingstatus',palette='colorblind')
plt.show()


# In[44]:


data.hist(figsize=(15,10))
plt.show()


# Splitting data into independent and dependent features

# In[46]:


x=data.iloc[:,1:]
x.head()


# In[47]:


y=data['price']
y.head()


# Splitting data for training and testing

# In[49]:


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=20,random_state=90)


# In[50]:


print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# Scaling data for compressed dataset and better results

# In[52]:


ms=MinMaxScaler()
ms.fit_transform(x_train)
ms.fit_transform([y_train])


# Using Random Forest algorithm 

# In[54]:


rfr=RandomForestRegressor()
rfr.fit(x_train,y_train)


# Accuracy score for this model is 73%

# In[56]:


rfr.score(x_test,y_test)*100


# Scaling the test data set also

# In[58]:


ms.fit_transform(x_test)
ms.fit_transform([y_test])


# Predicting using the test data set

# In[60]:


y_predict=rfr.predict(x_test)


# In[61]:


y_predict


# In[62]:


y_test


# Comparison of test prediction and actual prediction 

# In[64]:


plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
plt.title('y_test original')
sns.scatterplot(y_test)
plt.subplot(1,2,2)
plt.title('y_test prediction')
sns.scatterplot(y_predict)
plt.show()


# In[ ]:




