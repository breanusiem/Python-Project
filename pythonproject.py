#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
from decimal import Decimal, localcontext
def newt1(p):
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = p**3 - 2*p**2 - 5
        fprimep = 3*p**2 - 4*p
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = 1
p = newt1(p0)
def newt2(p):
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = p**3 + 3*p**2 - 1
        fprimep = 3*p**2 + 6*p
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = -3
p = newt2(p0)
def newt3(p):
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = p - np.cos(p)
        fprimep = 1+np.sin(p)
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = 0
p = newt3(p0)
def newt4(p):
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = p - .8-.2*np.sin(p)
        fprimep = 1-.2*np.cos(p)
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = 0
p = newt4(p0)


# In[82]:


def newt5(p):
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = p**2 - 2*p*np.e**-p+np.e**(-2*p)
        fprimep = 2*p*np.e**-p-2*np.e**-p-2*np.e**(-2*p)+2*p
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = 0
p = newt5(p0)
def newt6(p):
    with localcontext() as ctx:
        ctx.prec = 100
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = Decimal(np.e)**Decimal(6)*p+Decimal(3)*Decimal(np.log(2))**Decimal(2)*Decimal(np.e)**(Decimal(2)*p)-Decimal(np.log(8))*Decimal(np.e)**(Decimal(4)*p)-Decimal(np.log(2))**Decimal(3)
        fprimep = Decimal(6)*Decimal(np.e)**(Decimal(6)*p)-Decimal(4)*Decimal(np.log(8))*Decimal(np.e)**(Decimal(4)*p)+Decimal(6)*Decimal(np.log(2))**Decimal(2)*Decimal(np.e)**(Decimal(2)*p)
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = Decimal(-1)
p = newt6(p0)
def newt7(p):
    with localcontext() as ctx:
        ctx.prec = 100
    maxIt = 1000
    tol = 1e-5
    for i in range(maxIt):
        fp = Decimal(np.e)**Decimal(6)*p+Decimal(1.441)*Decimal(np.e)**Decimal(2)*p-Decimal(2.079)*Decimal(np.e)**(Decimal(4)*p)-Decimal(.333)
        fprimep = Decimal(6)*Decimal(np.e)**Decimal(6)*p-Decimal(8.316)*Decimal(np.e)**Decimal(4)*p+Decimal(2.882)*Decimal(np.e)**Decimal(2)*p
        p_new = p - fp/fprimep
        if abs (p - p_new) < tol:
            return p
        p = p_new
print(p)    
p0 = Decimal(-1)
p = newt7(p0)


# In[86]:


n = int(input('number of data points: '))
x = np.zeros((n))
y = np.zeros((n))
print('data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
xp = float(input('interpolation point: '))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    
print('Interpolated value at %.3f is %.3f.' % (xp, yp))


# In[87]:


n = int(input('number of data points: '))
x = np.zeros((n))
y = np.zeros((n))
print('data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
xp = float(input('interpolation point: '))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    
print('Interpolated value at %.3f is %.3f.' % (xp, yp))

