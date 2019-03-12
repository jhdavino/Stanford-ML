#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = [1, 2, 3]
y = [1, 2, 3]
theta_1 = 0
theta_2 = 0.5

def Squared_error(x, y, theta1, theta2):
    hipotesys = [theta1 + theta2*k for k in x]
    #print (hipotesys)
    errors = 0.0
    for i in range(len(x)):
        errors += (hipotesys[i] - y[i])**2
    
    return (1/(2*len(x)))*errors

Squared_error(x, y, theta_1, theta_2)


# In[ ]:




