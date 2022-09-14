#!/usr/bin/env python
# coding: utf-8

# # Project 3a
# ## US House Price Prediction  using Linear Regrssion
# ### Sujit Khatiwada (Group H)

# In[1]:


# Importing essential Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# USA_Housing Data as csv
df = pd.read_csv("USA_Housing.csv")
df.head()


# In[3]:


df.info(verbose=True) ### Check basic info on the data set


# In[4]:


# describe()' method to get the statistical summary of the various features of the data set**
df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9])


# In[5]:


#'columns' method to get the names of the columns (features)**
df.columns


# In[6]:


# Visualization on the data set
# Pairplots using seaborn
sns.pairplot(df)


# In[7]:


# **Distribution of price (the predicted quantity)** in histogram
df['Price'].plot.hist(bins=25,figsize=(8,4))


# In[8]:


df['Price'].plot.density()


# In[9]:


# Correlation matrix and heatmap
df.corr()


# In[10]:


plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,linewidths=2)


# In[11]:


l_column = list(df.columns) # Making a list out of column names
len_feature = len(l_column) # Length of column vector list
l_column


# In[12]:


# **Put all the numerical features in X and Price in y, ignore Address which is string for linear regression**
X = df[l_column[0:len_feature-2]]
y = df[l_column[len_feature-2]]


# In[13]:


print("Feature set size:",X.shape)
print("Variable set size:",y.shape)


# In[14]:


X.head()


# In[15]:


y.head()


# In[16]:


# Test Train Data
# Create X and y train and test splits in one command using a split ratio
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)


# 

# In[17]:


# Check the size and shape of train/test splits
print("Training feature set size:",X_train.shape)
print("Test feature set size:",X_test.shape)
print("Training variable set size:",y_train.shape)
print("Test variable set size:",y_test.shape)


# In[18]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics
lm = LinearRegression() # Creating a Linear Regression object 'lm'
lm.fit(X_train,y_train) # Fit the linear model on to the 'lm' object itself i.e. no need to set this to another variable


# In[19]:


print("The intercept term of the linear model:", lm.intercept_)


# In[20]:


print("The coefficients of the linear model:", lm.coef_)


# In[21]:


cdf = pd.DataFrame(data=lm.coef_, index=X_train.columns, columns=["Coefficients"])
cdf


# In[22]:


# Prediction using the lm model
predictions = lm.predict(X_test)
print ("Type of the predicted object:", type(predictions))
print ("Size of the predicted object:", predictions.shape)


# In[23]:


plt.figure(figsize=(10,7))
plt.title("Actual vs. predicted house prices",fontsize=25)
plt.xlabel("Actual test set house prices",fontsize=18)
plt.ylabel("Predicted house prices", fontsize=18)
plt.scatter(x=y_test,y=predictions)
# Scatter plot of predicted price and y_test set to see if the data fall on a 45 degree straight line


# In[24]:


# Regression evaluation metrices
print("Mean absolute error (MAE):", metrics.mean_absolute_error(y_test,predictions))
print("Mean square error (MSE):", metrics.mean_squared_error(y_test,predictions))
print("Root mean square error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test,predictions)))


# In[25]:


# R-square value
print("R-squared value of predictions:",round(metrics.r2_score(y_test,predictions),3))

