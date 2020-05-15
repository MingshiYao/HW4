# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:56:20 2020

@author: Hasee
"""

import numpy as np
####chapter 6 #3
A = np.array([[4, -2, 1], [3, 6, -4], [2, 1, 8]])
B1 = np.array([12, -25, 32])
B2 = np.array([4, -10, 22])
B3 = np.array([20, -30, 40])
X1 = np.linalg.inv(A).dot(B1)
X2 = np.linalg.inv(A).dot(B2)
X3 = np.linalg.inv(A).dot(B3)
####chapter 6 #5
from scipy.linalg import hilbert
An=hilbert(100)
Bn=An[:,1]
Xn=np.linalg.inv(An).dot(Bn)#far different from analytic solution
####chapter 7 # 