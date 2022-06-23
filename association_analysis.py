#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt
import collections
import math
import warnings
from itertools import permutations
from efficient_apriori import apriori
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')


# ## read csv files

# In[3]:


df = pd.read_csv('_data.csv')
size = len(df["InvoiceNo"])


# ## data processing

# In[4]:


C="C"
transactions_map = {}

for i in range(size):
    l=str(df['Description'][i]).split(",")
    if df['InvoiceNo'][i][0] == C[0] or df['Country'][i] != "United Kingdom" or l[0] == "POSTAGE" or pd.isna(df['Description'][i]):
        continue
    if not df["InvoiceNo"][i] in transactions_map:
        transactions_map[df["InvoiceNo"][i]] = []
    transactions_map[df["InvoiceNo"][i]] += l


# In[5]:


transactions = []
for key in transactions_map:
    transactions += [transactions_map[key]]


# In[147]:


itemsets, rules = apriori(transactions,min_support=0.009,min_confidence=0.5)


# In[148]:


result = []
for res in rules:
    result += [[list(res.lhs), list(res.rhs)]]


# In[149]:


def inn (l1, l2):
    ll1, ll2 = list(permutations(l1,len(l1))), list(permutations(l2,len(l2)))
    for lll1 in ll1:
        for lll2 in ll2:
            if [list(lll1), list(lll2)] in result:
                return True
    return False


# In[150]:


pred = pd.read_csv("prediction.csv")
out = pd.read_csv("ans_example.csv")


# In[151]:


c=0
for i in range(len(pred["index"])):#
    l1 = pred["Association Rule antecedents"][i].split(",")
    l2 = pred["Association Rule consequents"][i].split(",")

    if inn(l1,l2):
        out["label"][i] = str(1)
        c+=1
    else :
        out["label"][i] = str(0)
    out["index"][i] = str(i)
out.to_csv('test.csv', index=False)


# In[ ]:





# In[180]:


number1 = []
idx = [i for i in range(len(itemsets[1]))]
for item in itemsets[1]:
    number1 += [itemsets[1][item]]
number1.sort()
plt.ylabel("Purchase quantity")
plt.bar(idx,number1)


# In[133]:


number2 = []
idx = [i for i in range(len(itemsets[2]))]
for item in itemsets[2]:
    number2 += [itemsets[2][item]]
number2.sort()
plt.bar(idx,number2)


# In[134]:


number3 = []
idx = [i for i in range(len(itemsets[3]))]
for item in itemsets[3]:
    number3 += [itemsets[3][item]]
number3.sort()
plt.bar(idx,number3)


# In[135]:


number4 = []
idx = [i for i in range(len(itemsets[4]))]
for item in itemsets[4]:
    number4 += [itemsets[4][item]]
number4.sort()
plt.bar(idx,number4)


# In[ ]:





# In[ ]:





# In[176]:


y=[0 for i in range(110)]
x=[i for i in range(110)]
for tmp in number1:
    y[tmp//20]+=1


# In[181]:


plt.xlabel("Purchase quantity")
plt.ylabel("Data amount")
plt.plot(x,y)


# In[ ]:




