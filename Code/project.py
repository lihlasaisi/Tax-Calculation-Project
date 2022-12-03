#Lihla Saisi Shiribwa lihla.saisi@azubiafrica.org

import pandas as pd
import numpy as np


# In[14]:


products = [{'product_id':23,'name':'Computer',      'wholesale':500,'retail_price':1000,'sales':100},
            {'product_id':96,'name':'Python Workout','wholesale':35, 'retail_price':75,  'sales':1000},
            {'product_id':97,'name':'Pandas Workout','wholesale':35, 'retail_price':75,  'sales':500},
            {'product_id':15,'name':'Banana',        'wholesale':0.5,'retail_price':1,   'sales':200},
            {'product_id':87,'name':'Sandwich',      'wholesale':3,  'retail_price':5,   'sales':300}]

sales=pd.DataFrame(products)
sales


# In[15]:


#Calculating Total Profit for each item
profit_sales = (sales['retail_price'] - sales ['wholesale'])*sales['sales'] 

#Adding the Column for Profit for each item
sales['profit'] = profit_sales

sales


# In[16]:


#Calculating 15% Tax
tax_sale1 = (sales['retail_price'])*.85 
sales['15% Tax'] = tax_sale1
#Calculating 15% Tax
tax_sale2 = (sales['retail_price'])*.80 
sales['20% Tax'] = tax_sale2
#Calculating 15% Tax
tax_sale3 = (sales['retail_price'])*.75 
sales['25% Tax'] = tax_sale3


# In[17]:


#Income at 15% Tax
profit_sales1 = (sales['15% Tax'] - sales ['wholesale'])*sales['sales']
sales['Profit 15% Tax'] = profit_sales1
#Income at 20% Tax
profit_sales2 = (sales['20% Tax'] - sales ['wholesale'])*sales['sales'] 
sales['Profit 20% Tax'] = profit_sales2
#Income at 25% Tax
profit_sales3 = (sales['25% Tax'] - sales ['wholesale'])*sales['sales'] 
sales['Profit 25% Tax'] = profit_sales3
sales


# In[12]:


print("Total Net Revenue at 0% Tax Ksh" , sales['profit'].sum())

print("Total Net Revenue at 15% Tax Ksh" , sales['Profit 15% Tax'].sum())

print("Total Net Revenue at 20% Tax Ksh" , sales['Profit 20% Tax'].sum())

print("Total Net Revenue at 25% Tax Ksh" , sales['Profit 25% Tax'].sum())





