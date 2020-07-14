#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:54:42 2020

@author: raghav
"""

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 2, 3]

#plt.figure()
plt.title("Data - X and Y")
plt.plot(x, y, '*')
plt.xticks([0, 1, 2, 3])
plt.yticks([0, 1, 2, 3])
plt.show()

def linearRegression(theta0, theta1):
    yPredicted = []
    for i in x:
        yPredicted.append((theta0 + (theta1 * i)))
 #   plt.figure()
    plt.title("Predictions")
    plt.plot(x, yPredicted, '.')
    plt.xticks([0, 1, 2, 3])
    plt.yticks([0, 1, 2, 3])
    plt.show()

theta0 = 1.5
theta1 = 0 
linearRegression(theta0, theta1)

theta0a = 0
theta1a = 1.5 
linearRegression(theta0a, theta1a)

theta0b = 1
theta1b = 0.5
linearRegression(theta0b, theta1b)