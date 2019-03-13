#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[196]:


class network:
    def __init__(self, x, w, a): # a = architecture of the network 
        self.x = x               
        self.w = w
        self.a = a
        
    def run(self):
        #adding bias
        self.x.insert(0, np.ones(len(self.x[0])).tolist())
        self.w.insert(0, np.ones(len(self.x[0])).tolist())
        self.a.insert(0, self.w)
        
        for l in range(0, len(self.a)): #number of layers
                if(l == 0):
                    a0 = self.x
                else:
                    h = self.a[0][l] 
                    print("h ", h)
                    a0 = self.activation(z0) + h
                    
                
                print("w ", self.w)
                print("a ", np.squeeze(a0))
                z0 = np.dot( np.squeeze(self.a[l]), np.squeeze(a0))
                print(z0)
        return self.activation(z0)
                
    def activation(self,v):
        return 1/(1+np.exp(-v))


# In[197]:


n = network([[1],[1]], [[0.5], [1]], [[]])
n.run()

