# -*- coding: utf-8 -*
"""
Created on Wed Feb 23 14:20:13 2022

@author: sohum

Measure laser power at back of optical rail from the little bit of light that gets through.
Measure laser power directly on top of laser beam as going up optical rail
Find relation between two so that can measure power out the back without blocking beam and
can hence trap particle at same time
"""
import numpy as np
import matplotlib.pyplot as plt

back = [115,108,91,83.2,76,60.9,48.8,33.7,22.3] #want this as x as we will be measuring this from now
top = [310,280,250,224,187,150,119,91,58.4] #want this as y as this is what we will be calculating

back_err = [0.6,0.8,1,0.5,1,0.5,0.4,1.5,0.3]
top_err = [1,1,2,1,3,1,1,1,2]

fit,cov = np.polyfit(back,top,1, w = 1/np.array(top_err), cov=True)
fitplot = np.poly1d(fit)
sig0 = np.sqrt(cov[0,0])
sig1 = np.sqrt(cov[1,1])

plt.plot(back, fitplot(back))
#plt.plot(back,top, 'x',)
plt.errorbar( back, top, yerr = top_err, xerr=back_err, fmt='x')
plt.xlabel('Back Beam Power (mW)', fontsize = 30)
plt.ylabel('Vertical Beam Power (mW)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
#plt.legend(loc='best', fontsize = 20)
plt.grid()
plt.show()

print('Slope = %.10f +- %.4f' %(fit[0],sig0))
print('Intercept = %.10f +- %.4f' %(fit[1],sig1))
print('Equation')
print(fitplot)


