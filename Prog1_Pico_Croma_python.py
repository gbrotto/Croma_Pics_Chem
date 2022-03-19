# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:53:11 2022

@author: gbrotto
"""

import numpy as np
import matplotlib.pyplot as plt



def gauss(t, t_max, width):
    f = np.exp(-np.log(2)*((t-t_max)/(width/2))**2)
    return f

N = 500
t = np.linspace(0, 10, N)
t_max = 7.5
width = .25
height = 10

dp = .02

erro = dp*np.random.randn(N)

f = height*gauss(t, t_max, width)+erro

plt.plot(t, f, 'b-')

plt.xlabel('Time, min')
plt.ylabel('Absorbance, mAu')
plt.show()
