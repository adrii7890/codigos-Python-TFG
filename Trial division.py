#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math


# In[5]:


import time


# In[28]:


def NRfloor(n): #Calculo de la función suelo de la raiz cuadrada mediante el método de Newton
    x = n
    y = math.floor((x + 1) / 2)
    while y < x:
        x = y
        y = math.floor((x + n / x) / 2)
    return x


# In[31]:


def trialdiv(n):
    L=[]
    m=NRsuelo(n)
    for i in range (2,m):
        while n%i==0 and n!=1:
            L.append(i)
            n=n/i
            m=NRsuelo(n)
    if n==1:
        return L
    else: 
        L.append(n)
        return L


# In[41]:


inicio=time.time()
p=trialdiv(189988612)
print(p)
fin=time.time()
print(fin-inicio)


# In[ ]:




