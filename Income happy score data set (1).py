#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
happyscore_income = pd.read_csv(r"C:\Users\BT\Downloads\happyscore_income.csv")
happyscore_income.head()


# In[25]:


happyscore_income.plot.scatter("avg_income","happyScore")
plt.title("Happy Score Income data set")
plt.show()


# In[ ]:




