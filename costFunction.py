#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:31:36 2020

@author: raghav
"""

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 2, 3]

m = len(y)

def costFunction(theta0, theta1):
    yPredicted = [theta0+(theta1*1), theta0+(theta1*2), theta0+(theta1*3)]
    sum = 0
    for i,j in zip(yPredicted, y):
        sum = sum + ((i-j)**2)
    J = 1/(2*m)*sum
    return J

theta0 = [1.5, 0, 1]
theta1 = [0, 1.5, 0.5]

for i,j in zip(theta0, theta1):
    print("Cost when theta0 = %r theta1 = %r :"%(i,j), costFunction(i,j))