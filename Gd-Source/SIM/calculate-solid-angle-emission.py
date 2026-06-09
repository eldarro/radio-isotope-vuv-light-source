# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:00:07 2023

@author: darro
calculate the amount of light detected by a coincidence sensor for the Gd source
"""

import numpy as np
import matplotlib.pyplot as plt

def SA(l,d):
    phi = np.arctan((d/2)/l)
    I = (1-np.cos(phi))/2
    return I

def NPE(l,d,Q,PDE):
    W = 30
    phi = np.arctan((d/2)/l)
    I = (1-np.cos(phi))/2
    T = 0.8
    npe = Q/W*I*T*PDE
    return npe

print('')
# R6834 PMT at 25 mm
print('Photons observed from Gd-148 alpha with R6834 PMT at 1 inch: %i'%NPE(25,25,3E6,0.05))
# R8520 PMT at 25 mm
print('Photons observed from Gd-148 alpha with R8520 PMT at 1 inch: %i'%NPE(25,23.1,3E6,0.3))
# VUV4 quad at 25 mm
print('Photons observed from Gd-148 alpha with VUV4-quad at 1 inch: %i'%NPE(25,13.5,3E6,0.24))

print('')
# VUV4 quad at 56 mm
print('Photons observed from Cf-252 alpha with VUV4-quad at 2.2 inch: %i'%NPE(56,13.5,6.1E6,0.24))
# R6834 PMT at 56 mm
print('Photons observed from Cf-252 alpha with R6834 PMT at 2.2 inch: %i'%NPE(56,25,6.1E6,0.05))
    

