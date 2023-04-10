#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas as pd
import pandas as pd


# In[2]:


#read Salaries.csv as a dataframe called sal
sal = pd.read_csv('H:\Machine learning\Salaries.csv')


# In[4]:


#check the head (first four rows)
sal.head(4)


# In[31]:


#check info for details
sal.info()
#drop rows and columns containing null values
sal.dropna()


# In[34]:


#check the average base pay
sal['BasePay'].mean()
#check the highest overtime pay
sal['OvertimePay'].max()


# In[21]:


#check the job title of Christopher Chong
sal[sal['EmployeeName']=='Christopher Chong']['JobTitle']


# In[37]:


#check the average total pay of all employees per year
sal.groupby('Year').mean()['TotalPay']
#check the number of unique job titles
sal['JobTitle'].nunique()


# In[27]:


#check the top five most common job titles
sal['JobTitle'].value_counts().head(5)


# In[28]:


#check how many job titles were represented by only one person in 2011
sum(sal[sal['Year']==2011]['JobTitle'].value_counts()==1)


# In[30]:


clear


# In[ ]:




