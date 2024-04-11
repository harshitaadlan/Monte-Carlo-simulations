import random

import numpy as np

from math import exp,pi,sin


n=23
c=2**n
x=np.zeros(c)
for i in range(len(x)):
    x[i]=random.uniform(0,10)

def func(x):
    return exp(-x)*(sin(pi*x))**2
area=0
for i in range(c):
    area+=func(x[i])
value=10/float(c) * area
print(value)







