#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np 
from numpy.linalg import pinv


# In[19]:


x1 = [6.5, 7, 6.9, 10, 3, 2, 6.2, 5.9, 7.3]
y = (0, 1, 0, 1, 0, 0, 0, 0, 1)
x0 = np.ones(len(x1),).tolist()
x = np.matrix([x0, x1])


# In[20]:


x = np.transpose(x)
y = np.transpose(np.matrix(y))


# In[21]:


def train(x, y):
    theta = np.transpose(np.matrix(np.ones(len(y))))
    return np.dot(pinv(np.matmul(np.transpose(x), x)), np.matmul(np.transpose(x), y)) 


# In[22]:


theta = train(x,y)
print(theta)


# In[23]:


def predict(x, theta, threshold): # i dont know if its right
    h = [1/(1+v) for v in np.exp(-np.matmul(x,theta))]
    hypotesis = []
    for v in h:
        if(v > threshold):
            hypotesis.append(1)
        else:
            hypotesis.append(0)
    return hypotesis


# In[24]:


predict(x, theta, 0.6) 


# In[25]:


def predict_cross_entropy(x, y, theta):
    h = [1/(1+v) for v in np.exp(-np.matmul(x,theta))]
    errors = []
    for i in range(0,len(x)):
        if(y[i][0] == 1):
            errors.append(- np.log(h[i][0]))
        elif(y[i][0] == 0):
            errors.append(-np.log(1 - h[i][0]))
    return errors


# In[26]:


error(x, y, theta)


# In[10]:


classify = []
threshold = 0.5
for e in error(x, y, theta):
    if(e < threshold):
        classify.append(1)
    else: 
        classify.append(0)
classify


# In[29]:


# testing
x = [[1, 5.9], [1, 7.1], [1, 6.9]]
y = [[0],[1],[0]]

classify = []
threshold = 0.5
for e in error(x, y, theta):
    if(e < threshold):
        classify.append(1)
    else: 
        classify.append(0)
classify

