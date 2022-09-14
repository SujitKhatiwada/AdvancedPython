#!/usr/bin/env python
# coding: utf-8

# In[13]:


#importing pymongo for Db Connection
import pymongo


# In[16]:


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
print("Connection Successful")


# In[17]:


client.list_database_names()


# In[19]:


db_name = "sample_db"
sample_db = client[db_name]
collection_name = "fruits"
fruits_collection = sample_db[collection_name]


# In[20]:


# Create Operation using the data provided in ppt
fruits =[{"fruit": "Apple",    "size": "Large",    "color": "Red"},
               {"fruit": "Mango",    "size": "Medium",    "color": "Yellow"},
{"fruit": "Guava",    "size": "small",    "color": "Green"}]

fruits_collection.insert_many(fruits)


# In[21]:


query1 = {'fruit':'Apple'}
result = fruits_collection.find_one(query1)


# In[22]:


# Read operation for result
result


# In[25]:


# Update data for fruit apple to orange
query_old = {"fruit":"Apple"}
query_new = {'$set':{"fruit": "Orange"}}
fruits_collection.update_one(query_old, query_new)

#Recheck the Orange item
query2 = {'fruit':'Orange'}
result2 = fruits_collection.find_one(query2)
result2


# In[28]:


# Delete Operation
query_del ={"fruit":"Orange"}
retVal = fruits_collection.delete_one(query_del)


# In[29]:


retVal


# In[ ]:




