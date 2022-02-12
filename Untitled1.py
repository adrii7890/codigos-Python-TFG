#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[17]:


def pruebaWilson(n):
    x=math.factorial(n-1)+1
    if x%n==0:
        return True
    else:
        return False

