#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


import time


# In[3]:


def NRtecho(n):  #Calcula la función techo de la raiz cuadrada usando el método de Newton
    x = n
    y = math.ceil((x + 1) / 2)
    while y < x:
        x = y
        y = math.ceil((x + n / x) / 2)
    return x


# In[4]:


def isPerfectSquare(num): #determina si num es un cuadrado perfecto
        return math.sqrt(num) % 1 == 0


# In[5]:


def FermatFact(n,M):
    x=math.ceil(math.sqrt(n))
    j=1
    while j<=M and isPerfectSquare(x**2-n)==False:
        x+=1
        j+=1
    if isPerfectSquare(x**2-n)==True:
        y=math.sqrt(x**2-n)
        return j
    else:
        return 1


# In[7]:


def FermatFact1(n,M):
    x=NRtecho(n)
    j=1
    while j<=M and isPerfectSquare(x**2-n)==False:
        print("$", j ,"$ & $",x,"$ & $", x**2-n)
        x+=1
        j+=1
    if isPerfectSquare(x**2-n)==True:
        print(x**2-n)
        y=math.sqrt(x**2-n)
        return [(x-y),(y+x)]
    else:
        return 0
        


# In[12]:


inicio=time.time()
m=FermatFact1(69,185)
print(m)
fin=time.time()
print(fin-inicio)


# In[ ]:




