# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:52:17 2017

@author: Akshay
"""

#Optimization problems
# MIN -> x1*x4*(x1+x2+x3)+x3
# x1x2x3x4 >=25
# Sum of squares of all x1 to x4 is 40

import numpy as np
from scipy.optimize import minimize

#Objective
def objective(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

#Constraints
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25

def constraint2(x):
    sum_sq=40
    for i in range(4):
        sum_sq = sum_sq - x[i]**2
    return sum_sq

con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1,con2]

#Bounds
b = (1.0, 5.0)
bnds = (b,b,b,b)

#Optimizer
x0=[1,5,7,1]
sol = minimize(objective, x0, method = 'SLSQP', bounds = bnds, constraints = cons)

print(sol.x)
print(sol)




