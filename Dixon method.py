#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import random


# In[2]:


def  trialdiv(n):
    L=[]
    m=math.ceil(math.sqrt(n))
    for i in  range (2,m+1):
        while n%i==0  and n!=1:
            L.append(i)
            n=n/i
    if n==1:
        return L
    else:
        L.append(int(n))
        return L 


# In[3]:


def Bsmooth(n,B):
    smooth=True
    L=trialdiv(n)
    i=0
    while smooth==True and i<len(L):
        if L[i]>B:
            smooth=False
        i+=1
    return smooth


# In[4]:


def exp(n,B):
    L=trialdiv(n)
    E = []
    i=0
    while len(L)>0 and i<len(B):
        a=L[0]
        if a==B[i]:
            j=0
            count=0
            while j<len(L):
                if L[j]==a:
                    count+=1
                    L.pop(j)
                    j=0
                else:
                    j+=1
            E.append(count%2)
            i+=1
        else:
            i+=1
            E.append(0)
    while len(E)<len(B):
        E.append(0)
    return E        


# In[5]:


def iszero(n):
    bool=True
    L=exp(n,[2,3,5,7])
    i=0
    while bool==True and i<len(L):
        if L[i]==1:
            bool=False
        i+=1
    return bool


# In[14]:


# Function to find the factors of a number
# using the Dixon Factorization Algorithm
def Dixon(n,N):
    z=0
    w=0
    # Base de factores
    base = [2, 3, 5, 7,11,13,17,19,23] 
    L=[]
    #Generación de la lista aleatoria
    while len(L)<N:
        L.append(random.randrange(n))

    B = []
    Z = []
    W=[]
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<N:
        z=L[i]
        w=z**2%n 
        print ("$",z,"^2 \equiv",w," \pmod{n} $ & $",trialdiv(w),"$ & $",Bsmooth(w,23),r"$ \\")
        if Bsmooth(w,23)==True:
            Z.append(z)
            W.append(w)
            B.append(exp(w,base))
        i+=1
        
    return Z,W,B


# In[15]:


#Sin aplicar la idea de Dixon
def DixonV(n,N):
    z=0
    w=0
    # Base de factores
    base = [2, 3, 5, 7, 13] 
    L=[]
    #Generación de la lista aleatoria
    while len(L)<N:
        L.append(random.randrange(n))

    B = []
    Z = []
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<N and len(Z)==0:
        z=L[i]
        w=z**2%n 
        if Bsmooth(w,13)==True and iszero(w)==True :
            Z.append(z)
            B.append(exp(w,base))
        i+=1

    return [math.gcd(int(math.sqrt(Z[0]**2%n))-Z[0],n), math.gcd(int(math.sqrt(Z[0]**2%n))+Z[0],n)]


# In[19]:


Dixon(42477,90)


# In[9]:


(1215*2458)%4277


# In[108]:


(660*2640)**0.5


# In[112]:


math.gcd(1320+1124,4277)


# In[111]:


math.gcd(3064+9,4277)


# In[ ]:




