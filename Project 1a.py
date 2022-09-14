#!/usr/bin/env python
# coding: utf-8

# # Project 1a
# ### Prepared By: Sujit Khatiwada (C0835126) Group H

# # 1. Import an XML file using python

# In[1]:


#Using tree method of retreival
import xml.etree.ElementTree as ET


# In[2]:


# We are using a sample test.xml file for retrieval
tree = ET.parse("test.xml")
tree


# In[3]:


root = tree.getroot()
# reaching root


# In[4]:


# Iterating through the child element of XML file
for child in root:
  print({x.tag for x in root.findall(child.tag+"/*")})


# In[5]:


#Getting first book 
book1 = root[0]
book1


# In[6]:


#getting the Id of first book
book1.attrib['id']


# In[7]:


# Gatherning the nodes on one book
for child in book1:
    print(child.tag, child.attrib)


# In[18]:


# Let us see the nodes as a dataframe by using pandas
import pandas as pd
rows = []
columns = ["author", "title", "genre", "price", "publish_date","description"]
for node in root: 
    res = []
    for el in columns[0:]: 
        if node is not None and node.find(el) is not None:
            res.append(node.find(el).text)
        else: 
            res.append(None)
    rows.append({columns[i]: res[i] 
                    for i, _ in enumerate(columns)})
dataframe = pd.DataFrame(rows, columns=columns)
dataframe


# # 2. Import a JSON file and analyze different parts of JSON file

# In[2]:


import json # Import JSON for JSON parse


# In[3]:


with open('sample4.json') as file:
    data = json.load(file) #Loading file
    #creates and returns a new Python dictionary with the key-value pairs in the JSON file.


# In[4]:


data
#Checking the data information from json file


# In[5]:


print(data["people"])


# In[6]:


print(len(data["people"]))
#The output is 3 because the value of the main key "people" is a list with three elements.


# In[7]:


#We can also use the keys to access their corresponding values. This is what we typically do when we work with JSON files.
#For example, to access the phone number of the first person, we would write:
data["people"][0]["number"]


# In[8]:


import pandas as pd
df = pd.json_normalize(data["people"])
df


# # 3. Import the breast cancer dataset and store it in a JSON file

# In[23]:


import sklearn.datasets
import pandas as pd
data = sklearn.datasets.load_breast_cancer()


# In[20]:


# load Sklearm datasets to pandas dataframe
df = pd.DataFrame(data.data, columns=data.feature_names)
df


# In[21]:


df['target'] =data.target
# attaching target variable


# In[24]:


# JSON Storage
df.to_json('./cancer_data.json', orient='index')


# # 4. Make a regression dataset and store them on disk in a csv file

# In[25]:


from sklearn.datasets import make_regression
from matplotlib import pyplot
# generate regression dataset
X, y = make_regression(n_samples=500, n_features=1, noise=0)
# plot regression dataset
pyplot.scatter(X,y)
pyplot.show()


# In[26]:


#Creating a regression for 500 sample wth 7 features and 4 informative
X, y = make_regression(n_samples=500, n_features=7, n_informative=4)


# In[27]:


import csv

header = y
data = X

with open('sample_regression.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

