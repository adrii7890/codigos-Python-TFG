#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[3]:


import time


# In[28]:


def Pollardp (n,x0,M):
    a=x0
    b=x0
    i=1
    d=1
    while i<=M and d==1:
        a=(a**2-1)%n
        b=(b**2-1)%n
        b=(b**2-1)%n
        print(a ,'y', b)
        d=math.gcd(a-b,n)
        i+=1
    if d!=1 and d!=n:
        return [d,n/d]
    else:
        return 0


# In[29]:


inicio=time.time()
m=Pollardp(12247,2,7)
print(m)
fin=time.time()
print(fin-inicio)


# In[ ]:




