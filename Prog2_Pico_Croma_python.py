# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:06:35 2022

@author: gbrotto
"""

import numpy as np
import matplotlib.pyplot as plt

def gauss(t, t_max, width):
    f = np.exp(-np.log(2)*((t-t_max)/(width/2))**2)
    return f

def gauss_sk(t, t_max, width, tail):
    f = np.zeros(np.size(t))
    ft0 = (1+2*tail*(t-t_max)/width) > 0
    f[ft0] = np.exp(-np.log(2)*((np.log(1+2*tail*(t[ft0]-t_max)/width)/tail)**2))
    return f

N = 500
t = np.linspace(0, 10, N)
t_max = 7.5
width = .25
height = 10
tail = .4

dp = .02
erro = dp*np.random.randn(N)
#f = height*gauss(t, t_max, width)+erro

f = height*gauss_sk(t, t_max, width, tail)+erro

plt.plot(t, f, 'b-')

plt.xlabel('Time, min')
plt.ylabel('Absorbance, mAu')
plt.show()
