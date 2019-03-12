#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#x1 = [1,2,3,4,5,6,7]
x1 = [5, 5, 6, 7, 7, 8, 4]
x2 = [5,4,6,4,3,7,4]
x0 = np.ones(len(x1))
#x = [x0, x1, x2]
x = np.transpose(np.matrix([x0, x1, x2]))
y = np.transpose(np.matrix([6.8, 6.5, 7.0, 6.3, 4.4, 7.1, 7.4]))
theta = np.matrix([[1.2], [0.6], [0.3]])
alpha = 0.01
iterations = 10000

print(theta)
print(x)
print(y)


# In[3]:


def error(x, y, theta):
    return 1/(2*len(y)) * np.sum(np.power(np.subtract(np.matmul(x,theta), y), 2))


# In[4]:


def predictions(theta, x):
    return np.matmul(x,theta)


# In[5]:


predictions(theta, x)


# In[6]:


def gradient(x,y,theta, alpha, iterations):
    for i in range(iterations):
        theta = np.subtract(theta , (np.multiply(
                                        (alpha*(1/len(y))),(np.matmul(np.transpose(x),(
                                                                    np.subtract(np.matmul(x,theta),
                                                                                y))  
                                                                     )
                                                           )
        )
                                    )
                           )
    return theta    


# In[7]:


thetaop = gradient(x,y,theta, alpha, iterations)
print(thetaop)


# In[8]:


nextsem = [1 , 5, 5]
print(predictions(thetaop, nextsem))
print(error(x,y,thetaop))

