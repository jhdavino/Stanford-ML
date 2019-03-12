#!/usr/bin/env python
# coding: utf-8

# In[25]:


y = [3, 2, 1, 2, 3]
x = [1, 2, 3, 4]
theta_0 = 0.2
theta_1 = 0.3
alpha = 0.3

def Gradient_descent(x, y, theta1, theta2, alpha):
    while(True):
        theta0, theta1 = theta1, theta2
        theta1, theta2 = update_theta(x,y,theta1,theta2,alpha)
        
        if((theta1 >= theta0)&(theta2 >= theta1)):
            #print("theta0 ", theta1)
            #print("theta1 ", theta2)
            return theta1, theta2;
        
def update_theta(x, y, theta1, theta2, alpha):
    sum_1 = 0.0
    sum_2 = 0.0
    hipotesys = [theta1 + theta2*k for k in x]
    for i in range(len(x)):
        sum_1 += (hipotesys[i] - y[i])**2 - y[i]
        sum_2 += ((hipotesys[i] - y[i])**2 - y[i])*x[i]       
    #sum_1 = Squared_error(x,y,theta1,theta2) - sum(y)
    #sum_2 = Squared_error(x,y,theta1,theta2) - sum
    
    theta1 = theta1 - alpha*sum_1
    theta2 = theta2 - alpha*sum_2
    return theta1, theta2

#def Squared_error(x, y, theta1, theta2):
#    hipotesys = [theta1 + theta2*k for k in x]
#    #print (hipotesys)
#    errors = 0.0
#    for i in range(len(x)):
#        errors += (hipotesys[i] - y[i])**2
#    
#    return (1/(2*len(x)))*errors

def predict(theta1, theta2, x):
    hipotesys = [(theta1 + theta2*data) for data in x]
    return hipotesys
        
theta_0, theta_1 = Gradient_descent(x,y,theta_0,theta_1, alpha)
print("theta0 ", theta_0)
print("theta1 ", theta_1)
prediction = predict(theta_0, theta_1, [0.5])
print ("original ", y)
print ("prediction ", prediction)

