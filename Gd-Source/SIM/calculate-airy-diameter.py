# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 04:07:46 2023

@author: darro
this script will determine the first minimum from an airy disk
"""

import numpy as np
import matplotlib.pyplot as plt

# Wavelength
y = 165E-9 
# Aperture
d = [50E-6,100E-6,200E-6,500E-6]
# Distance from aperture
l = np.linspace(0,3,num=100)
# Convert inches to mm
in2mm = 25.4


# First minimum diameter

# Beam FWHM
def fwhm(y,d):
    return 1.025*y/d
# Angle of first minimum
def theta(y,d):
    return 1.22*y/d
# Beam diameter at range
def beam(t,x):
    r = x*np.tan(t)
    return 2*r

figure, axis = plt.subplots(1,1,dpi=100)
axis.set_yscale('log')
axis.set_ylabel('Beam Diameter [mm]')
axis.set_xlabel('Distance [in]')
for aperture in d:
    axis.plot(l,beam(theta(y,aperture),l)*in2mm,label='Aperture = %i um'%(aperture*1E6))
    axis.axhline(aperture*1E3,ls='--',color='k',alpha=0.5)
axis.legend()
    


