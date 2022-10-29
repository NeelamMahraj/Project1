#!/usr/bin/env python
# coding: utf-8

# # Analyzing Car Price Dataset

# # Import libraries & read csv

# In[7]:


#Import libraries

import pandas as pd
import numpy as np
import plotly.express as px


# In[20]:


#Read csv file

df = pd.read_csv("D:\\COAL\CarPrice.csv")
df


# # 1. Visualization

# In[44]:


#create a box plot for visualization

fig = px.box(df, x='wheelbase')
fig1= px.box(df, x='carwidth')
fig2 = px.box(df, x='enginesize')

fig.show()
fig1.show()
fig2.show()


# # 2. Count Outliers

# In[35]:


#create a function to find number of outliers using IQR
#WheelBase

def find_outliers_IQR(df):
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    return outliers

outliers = find_outliers_IQR(df['wheelbase'])

print('number of outliers: '+ str(len(outliers)))

print('max outlier value: '+ str(outliers.max()))

print('min outlier value: '+ str(outliers.min()))

outliers


# In[36]:


#create another function to find number of outliers using IQR
#Carwidth

def find_outliers1_IQR(df):
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    return outliers

outliers1 = find_outliers1_IQR(df['carwidth'])

print('number of outliers: '+ str(len(outliers1)))

print('max outlier value: '+ str(outliers1.max()))

print('min outlier value: '+ str(outliers1.min()))

outliers1


# In[37]:


#create another function to find number of outliers using IQR
#Enginesize

def find_outliers2_IQR(df):
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    return outliers

outliers2 = find_outliers2_IQR(df['enginesize'])

print('number of outliers: '+ str(len(outliers2)))

print('max outlier value: '+ str(outliers2.max()))

print('min outlier value: '+ str(outliers2.min()))

outliers2


# # 3. To remove outlier less than 4

# In[119]:


for x in ['wheelbase']:
    q75,q25 = np.percentile(df.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    df.loc[df[x] < min,x] = np.nan
    df.loc[df[x] > max,x] = np.nan

print(df["wheelbase"].isna().sum())
df['wheelbase'].dropna()
print(df["wheelbase"])


# # 4. Convert greater than 4 value to NAN

# In[87]:


numeric_col = ['enginesize','carwidth']


# In[88]:


for x in ['carwidth']:
    q75,q25 = np.percentile(df.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    df.loc[df[x] < min,x] = np.nan
    df.loc[df[x] > max,x] = np.nan


# In[89]:


for x in ['wheelbase']:
    q75,q25 = np.percentile(df.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    df.loc[df[x] < min,x] = np.nan
    df.loc[df[x] > max,x] = np.nan


# In[90]:


df.boxplot(numeric_col)


# In[94]:


#sum of Nan values in Car Width
df['carwidth'].isnull().sum()


# In[95]:


#sum of Nan values in Engine Size
df['enginesize'].isnull().sum()


# In[96]:


# list of values of 'carwidth' column
marks_list = df['carwidth'].tolist()

# show the list
print(marks_list)


# In[97]:


# list of values of 'Engine Size' column
marks_list = df['enginesize'].tolist()
  
# show the list
print(marks_list)


# In[102]:


# Convert NaN to mean

a = df["carwidth"].mean()
round(a)


# In[103]:


a = df["enginesize"].mean()
round(a)


# In[104]:


#Finding the mean of the column having NaN
mean_value=df['carwidth'].mean()
  
# Replace NaNs in column S2 with the
# mean of values in the same column
df['carwidth'].fillna(value=mean_value, inplace=True)


# In[105]:


# list of values of 'carwidth' column
marks_list = df['carwidth'].tolist()
  
# show the list
print(marks_list)


# In[106]:


#Finding the mean of the column having NaN
mean_value=df['enginesize'].mean()
  
# Replace NaNs in column S2 with the
# mean of values in the same column
df['enginesize'].fillna(value=mean_value, inplace=True)


# In[107]:


# list of values of 'enginesize' column
marks_list = df['enginesize'].tolist()
  
# show the list
print(marks_list)


# # 5. Visualizing & Removing horsepower using binning method

# In[108]:


fig3 = px.box(df, x='horsepower')

fig3.show()


# # Q4

# In[120]:


# importing pandas as pd
import pandas as pd


# In[121]:


# importing data using .read_csv() function
df = pd.read_csv('CarPrice_Structure.csv')
 
# printing DataFrame
df


# # 1. Extract first name of CarName attribute

# In[122]:


# Split a phrase in all rows of a column and make a list of the first word
list_data = [df.CarName.str.split(' ')[index][0]
             for index in range(0, len(df))]
print(list_data)


# In[123]:


# Find the name of the column by index
n = df.columns[2]
n


# In[124]:


# Drop that column
df.drop(n, axis = 1, inplace = True)

# Put whatever series you want in its place
df[n] = list_data


# In[125]:


df


# # 2. Writing the regex for solution accordingly

# In[126]:


#To replace doornumber : alphabetic values to numeric form

df['doornumber'].replace({'four':4, 'two':2, 'three':3}, inplace=True)
print(df)


# In[127]:


#To replace carlength: alphabetic values to numeric form

df['carlength'] = df['carlength'].str.replace('cm', '')


# In[128]:


df


# # 3. Replace cathegorical data to numerical data

# In[129]:


# list of values of 'Fuel Type' column
marks_list = df['fueltype'].tolist()
  
# show the list
print(marks_list)


# In[130]:


# 0 replace gas attribute and 1 replace diesel attribute

df['fueltype'].replace({'gas':0, 'diesel':1}, inplace=True)
print(df)


# In[ ]:




