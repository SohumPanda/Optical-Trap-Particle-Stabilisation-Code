# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:37:04 2022

@author: tisia
"""
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# d = lambda D/y for diameter d, screen - particle distance D and fringe spacing y
 
Fringe = np.array([8.35,9.63,6.35,10.3,14.6,7.9,14.1,10,12.6,6.8,7.5,13.2,14.8,14.4,8.2,11])
Camera = np.array([7.3,6.6,6.6,9.9,11.9,8,13.9,11.3,12.6,7.3,6.6,13.9,12.6,12.6,6.6,9.95])
Spacing = 1e-3*np.array([4.01,3.48,5.28,3.25,2.29,4.24,2.38,3.35,2.66,4.93,4.44,2.54,2.25,2.32,4.06,3.02])
Spacingerr = 1e-3*np.array([0.17,0.1,0.17,0.17,0.13,0.17,0.13,0.25,0.13,0.25,0.17,0.17,0.13,0.17,0.25,0.17])
Fringerr = np.array([])
Cameraerr = 0.5*np.array([0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66])
newcamera = (Camera/0.663)*0.733

for i in  range(len(Spacing)):
    ferr = np.sqrt((((532e-9/Spacing[i])*5e-3)**2)+(((532e-9*63e-3)/(Spacing[i])**2)*Spacingerr[i])**2)
    Fringerr = np.append(Fringerr,ferr)



microFringerr = 1e6*Fringerr

fitlin,covlin = np.polyfit(Camera,Fringe,1,w=1/microFringerr,cov=True)


sig_0=np.sqrt(covlin[0,0])
sig_1=np.sqrt(covlin[1,1])
print('Slope:',fitlin[0],'+/-',sig_0)
print('Intercept:',fitlin[1],'+/-',sig_1)

p=np.poly1d(fitlin)
print('Equation')
print(p)

plt.figure('linear')
plt.grid()
plt.errorbar(Camera, Fringe, yerr = microFringerr, xerr = Cameraerr, fmt='x', color='Blue', ms=10, ecolor='Black', capsize=3)
plt.plot(Camera,p(Camera))
plt.title('Fringe spacing vs CCD camera size', fontsize = 20)
plt.xlabel('Size from camera (μm)', fontsize = 18)
plt.ylabel('Size from fringe spacing (μm)', fontsize = 18)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.figure

plt.show

#%% with latest particles

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
 
Fringe = np.array([8.35,9.63,6.35,10.3,14.6,7.9,14.1,10,12.6,6.8,7.5,13.2,14.8,14.4,8.2,11, 12.9,18.6,15.9])
Camera = np.array([7.3,6.6,6.6,9.9,11.9,8,13.9,11.3,12.6,7.3,6.6,13.9,12.6,12.6,6.6,9.95,9.95,15.9,11.9])
Spacing = 1e-3*np.array([4.01,3.48,5.28,3.25,2.29,4.24,2.38,3.35,2.66,4.93,4.44,2.54,2.25,2.32,4.06,3.02,2.6,1.88,2.1])
Spacingerr = 1e-3*np.array([0.17,0.1,0.17,0.17,0.13,0.17,0.13,0.25,0.13,0.25,0.17,0.17,0.13,0.17,0.25,0.17,0.13,0.07,0.17])
Fringerr = np.array([])
Cameraerr = 0.5*np.array([0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66])
newcamera = (Camera/0.663)*0.733

for i in  range(len(Spacing)):
    ferr = np.sqrt((((532e-9/Spacing[i])*5e-3)**2)+(((532e-9*63e-3)/(Spacing[i])**2)*Spacingerr[i])**2)
    Fringerr = np.append(Fringerr,ferr)



microFringerr = 1e6*Fringerr

fitlin,covlin = np.polyfit(Camera,Fringe,1,w=1/microFringerr,cov=True)


sig_0=np.sqrt(covlin[0,0])
sig_1=np.sqrt(covlin[1,1])
print('Slope:',fitlin[0],'+/-',sig_0)
print('Intercept:',fitlin[1],'+/-',sig_1)

p=np.poly1d(fitlin)
print('Equation')
print(p)

plt.figure('linear')
plt.grid()
plt.errorbar(Camera, Fringe, yerr = microFringerr, xerr = Cameraerr, fmt='x', color='Blue', ms=10, ecolor='Black', capsize=3)
plt.plot(Camera,p(Camera))
plt.title('Fringe spacing vs CCD camera size', fontsize = 20)
plt.xlabel('Size from camera (μm)', fontsize = 18)
plt.ylabel('Size from fringe spacing (μm)', fontsize = 18)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.figure

plt.show