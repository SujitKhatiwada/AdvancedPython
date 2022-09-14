#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Group H
#We want to import python compatible drivers for SQL Connection
import pyodbc

#Shows the list of drivers as part of pyodoc
pyodbc.drivers()


# In[2]:


#Creating a connection using our pyton client code against the Server
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-2VM8P06F\SQLSERVER2019;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')
print(conn)


# In[3]:


#Read Operation
query2 ="SELECT * FROM Person.Person"
cursor = conn.cursor();
cursor.execute(query2);
data1 = cursor.fetchall()
data1


# In[10]:


# Create Operation
query1 = "Create table AmazonProducts(ProductId int, ProductName varchar(200),Cost int)"
cursor = conn.cursor();
cursor.execute(query1);


# In[11]:


#Read Operation
query2 ="Select * from AmazonProducts"
cursor.execute(query2);
data1 = cursor.fetchall()
data1


# In[12]:


# insert Operation
query3 ="insert into AmazonProducts values (1,'Bag', 150)"
query4="insert into AmazonProducts values (2,'Pen', 25)"
query5 ="insert into AmazonProducts values (3,'Book', 300)"
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query5)


# In[13]:


#Read Operation
query2 ="Select * from AmazonProducts"
cursor.execute(query2);
data1 = cursor.fetchall()
data1


# In[14]:


# Update Operation
query7="update AmazonProducts set Cost=120 where ProductId=1 "
cursor.execute(query7)
query8 ="Select * from AmazonProducts"
cursor.execute(query8);
data2 = cursor.fetchall()
data2


# In[15]:


# Delete Operation
query9 = "delete from AmazonProducts where ProductId=3"
cursor.execute(query9);
query10 ="Select * from AmazonProducts"
cursor.execute(query10);
data3 = cursor.fetchall()
data3


# In[ ]:




