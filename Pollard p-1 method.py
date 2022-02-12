#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import time


# In[3]:


def Pollardp1 (n,H):
    a=2
    M=1
    d=1
    while M<H and d==1:
        a=(a**M)%n
        d=math.gcd(a-1,n)
        M+=1
    if d!=1 and d!=n:
        return [d, int(n/d)]
    else:
        return 0
        


# In[6]:


inicio= time.time()
m=Pollardp1(817279,100)
print(m)
fin=time.time()
print(fin-inicio)


# In[ ]:




