#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("voice.csv") #read csv and load into a dataframe
data.head()

data["label"] = data["label"].map({"male":"0", "female":"1"}) #encoder mapping of categorical variable "label"

X = data.iloc[:,0:19]
Y = data["label"]

# 2.Fit a linear regression model and measure the accuracy on the test set.
# [Hint:Refer to Linear Models section in scikit-learn]

#loading package for test train split
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20)

#loading regression model
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import metrics

ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

#measuring of accuracy
predicted_data = ln_model.predict(test_x)
metrics.accuracy_score(predicted_data, test_y)

# 3.Compute the correlation matrix that describes the dependence between all predictors and identify the
# predictors that are highly correlated.  Plot the correlation matrix using seaborn heatmap.
# [Hint: Explore dataframe methods to identify appropriate method]
import seaborn as sns
corr = data.corr()
sns.heatmap(corr)
plt.show()

# 4.Based on correlation remove those predictors that are correlated and fit a logistic regression model
# again and compare the accuracy with that of previous model.
# [Hint:Identify correlated variable pairs and remove one among them]

X = X.drop("dfrange",axis=1) #dropping one of the highly correlated pair

#split data againg and applying the regression model
train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20)

ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

predicted_data = ln_model.predict(test_x)
metrics.accuracy_score(predicted_data, test_y)

