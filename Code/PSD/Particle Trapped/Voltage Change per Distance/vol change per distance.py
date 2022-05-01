# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:02:47 2022

@author: sohum
"""

import numpy as np
import matplotlib.pyplot as plt

#micrometer heights, in mm

## OLD DATA AT UNKNOWN INCIDENT POWER ###

#mh = [3.59, 3.09, 2.59, 2.09, 1.59, 1.09, 0.59, 0.09]
#deltah = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5]

#v1s = [1.651716, 1.6723425, 1.6956428, 1.7137074, 1.7204717, 1.7207968, 1.7215692, 1.7216017]
#v1errs = [0.0025618814, 0.0021526425, 0.0008692477, 0.00041336447, 0.00046090691, 0.00034526602, 0.0005581048, 0.00045416123]
#v2s = [1.6512263, 1.6316714, 1.6298865, 1.6481012, 1.6992313, 1.7200434, 1.7214606, 1.7215033]
#v2errs = [0.0026946163, 0.0040665427, 0.0030652252, 0.002861036, 0.00091891026, 0.00049887574, 0.00054023863, 0.0004250131]

h,v1,v2 = np.loadtxt(r'C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\Voltage Change per Distance\heightvoltage.csv', delimiter=',', unpack=True)
h = h - 3.49
h = h[:-5]*1000
v1 = v1[:-5]*1000
v2 = v2[:-5]           

yerrs = 52*[0.01*1000] 
xerrs = 52*[0.01*1000]

fit,cov = np.polyfit(h,v1,1,cov=True)
fitplot = np.poly1d(fit)
sig_0 = np.sqrt(cov[0,0])
sig_1 = np.sqrt(cov[1,1])
          
plt.errorbar(h,v1, xerr = xerrs, yerr = yerrs, fmt = 'rx', label = "channel 1", markersize = 20)
#plt.plot(h[:-5],v2[:-5],'rx', label = "channel 2", markersize = 15)
plt.plot(h,fitplot(h), linewidth = 3)

plt.title('Position of Focused light above PSD centre vs Channel Voltage', fontsize = 40)
plt.ylabel('Voltage (mV)', fontsize = 30)
plt.xlabel('Position of focused ight above centre of PSD (\u03BCm)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(fontsize = 30)
plt.grid()
plt.show()
print(fitplot)