
# coding: utf-8

# ## Connect to the Northwind dataset using SQL

# In[31]:

import pandas as pd
import numpy as np
import psycopg2 
get_ipython().magic(u'matplotlib inline')

constr =  "host='dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com' dbname='northwind' user='dsi_student' password = 'gastudents'"

conn = psycopg2.connect(constr)



# ## Create a pandas df that is the combination of the orders and order_details tables
# Each row of your df represents a unique order / product pair.  You could either bring in the tables separately, and join in pandas, or join in SQL, and bring in one table.  Ideally you should try both ways to practice!

# In[32]:

df = pd.read_sql('SELECT * FROM orders JOIN order_details ON orders."OrderID" = order_details."OrderID";', conn)


df


# ## Explore the data!  Convert data types as appropriate, calculate new variables, do some exploratory analysis with pivot_tables and plotting
# You can treat this as an open-ended assignment, and decide what you want to explore, or you can answer the questions below.

# In[16]:

# things to clean: orderDate, RequiredDate, ShippedDate
"""
df['new_ShippedDate']= pd.to_datetime(df['ShippedDate'])
df['shippedMonth'] = df['newdate'].dt.month
df['shippedMonth2'] = df['newdate'].dt.strftime('%b')

df5['newdate']= pd.to_datetime(df5['ShippedDate'])
df5['shippedMonth'] = df5['newdate'].dt.month
df5['shippedMonth2'] = df5['newdate'].dt.strftime('%b')

[4:12]  
also take a look at  df5['daystoship']= (df5['ShippedDate'] -df5['OrderDate']).astype('timedelta64[D]')
df

"""


# ### 1)  Which employee had the highest total revenues?  Plot a bar chart to show this.

# In[33]:

df["total_sales"]= df["UnitPrice"] * df["Quantity"]

pd.pivot_table(df, index="EmployeeID", values="total_sales", aggfunc=sum).plot(kind = "bar")


# ### Challenge: create a scatter plot of unit price / quantity and colour-code by employee

# In[36]:

pd.pivot_table(df, index="EmployeeID").plot.scatter(x="UnitPrice", y="Quantity")



# ### 2) Calculate and plot the total volume of products shipped by month

# In[47]:

import datetime

df['newdate']= pd.to_datetime(df['ShippedDate']) 
#Convert argument to datetime. type

df['shippedMonth'] = df['newdate'].dt.month
#takes the month from newdate column as number

df['shippedMonth2'] = df['newdate'].dt.strftime('%b')
#takes the month from newdate column as string 

pd.pivot_table(df, index="shippedMonth", values="total_sales").plot()
df


# ### 3) Calculate and plot a histogram of the number of days taken to ship

# In[52]:

df['new_orderdate']= pd.to_datetime(df['OrderDate'])
df['new_shipdate']= pd.to_datetime(df['ShippedDate'])

df["diff"] = (df['new_shipdate'] - df['new_orderdate']).dt.days
df["diff"].hist()


# ### Challenge: compare the distributions for USA and UK on one plot

# In[ ]:




# ### 4) Plot the daily revenues over time (by Order Date)

# In[56]:

pd.pivot_table(df, index= "OrderDate", values = "total_sales").plot(figsize = (30, 20))


# In[ ]:



