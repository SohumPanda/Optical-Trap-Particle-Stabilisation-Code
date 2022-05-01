# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:11:21 2022

@author: sohum
"""

import numpy as np 
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy.optimize as spo

#%% Fitting the power spectrum to give the corner frequency 
particle = 'k'
freq = 60

datah = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\particle {}\batch1.npy".format(particle))
#datah = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\Injecting a Freq\particle {}\2V peak to peak sine wave {}Hz\batch1.npy".format(particle,freq))
#datah = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\Injecting a Freq\particle {}\2V peak to peak sine wave {}Hz\batch1.npy".format(particle,freq))
#datah = np.load(r"/home/pi/Desktop/Sohum and Kai/PSD/Particle Trapped/Injecting a Freq/particle {}/2V peak to peak sine wave {}Hz/batch1.npy".format(particle,freq))
#datah = np.load(r"/home/pi/Desktop/Sohum and Kai/PSD/Particle Trapped/particle {}/batch2.npy".format(particle))

t1h = [row[0] for row in datah]      
t2h = [row[1] for row in datah] 
v1h = [row[2] for row in datah]
v2h = [row[3] for row in datah]


f1h = interp1d(t1h,v1h, kind='cubic')
f2h = interp1d(t2h,v2h, kind='cubic')

x1h = np.linspace(t1h[0],t1h[-1],400000)
x2h = np.linspace(t2h[0],t2h[-1],400000)


#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1h = t1h[-1] - t1h[0] 
D2h = t2h[-1] - t2h[0]


#R is the sample rate
R1h = N/D1h
R2h = N/D2h


yv1h = np.abs(fft(f1h(x1h))[0:N//2])
xfv1h = fftfreq(N, 1/R1h)[:N//2]

yv2h = np.abs(fft(f2h(x2h))[0:N//2])
xfv2h = fftfreq(N, 1/R2h)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 



p_size = 8.0e-6 #need to put the apppropriate diameter for the particle power spectrum you want to fit. 
friction_coeff = 0.5*6*np.pi*1e-12*18.13e-6*p_size #radius and dynamic viscosity
kb = 1.38e-23   #botlzmann constant
T = 24 + 273 #room temperture in kelvin 

def lorentzian(x,a):
    power = 0.5*(np.pi**-2)*kb*T*(friction_coeff**-1)*((a**2 + x**2)**-1)
    return power


p=[120] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
fit,cov=spo.curve_fit(lorentzian, xfv1h, yv1h, p)
plt.plot(xfv1h, lorentzian(xfv1h, *fit), color='red', linewidth = 4)
plt.plot(xfv1h[1:], yv1h[1:], label = 'Particle {}'.format(particle), color = 'blue')

plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)

 
print(*fit)

#%%
# using the particle size from the camera as the particle size for now



# particle name = [        h,   i,    k,   m,    n,     o,   v,    w,  ab]
particle_size = np.array([9.9, 11.9, 8.0, 13.9, 11.3, 12.6, 6.6, 9.95, 11.9])
size_err = np.array([0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66,0.66])
corner_freq = np.array([165, 158, 131, 173, 157, 170, 130, 150, 151])
freq_err = np.array([5,5,5,5,5,5,5,5,5])

friction_coeff = 0.5*6*np.pi*1e-12*18.13e-6*particle_size #radius and dynamic viscosity
spring_constant = np.pi*2*friction_coeff*corner_freq
co = 12*((np.pi)**2)*1e-12*18.13e-6
spring_err = np.sqrt(((co*corner_freq*0.5*size_err)**2)+(co*0.5*particle_size*freq_err)**2)

#%%
fit,cov = np.polyfit(particle_size,corner_freq,1,cov=True)
fitplot = np.poly1d(fit)
sig0 = np.sqrt(cov[0,0])
sig1 = np.sqrt(cov[1,1])

#plt.grid()
#plt.xlabel('Sample Rate (Hz)')
#plt.ylabel('Number of Maths Loops')
plt.plot(particle_size, fitplot(particle_size))
#plt.plot(samplerate,loopno, 'x')
#plt.show()

print('Slope = %.10f +- %.4f' %(fit[0],sig0))
print('Intercept = %.10f +- %.4f' %(fit[1],sig1))
print('Equation')
print(fitplot)

plt.grid()
#plt.plot(particle_size, corner_freq, 'rx')
plt.errorbar(particle_size, corner_freq, yerr = freq_err, xerr = size_err, fmt = 'x')
plt.title('Corner Frequency against Particle Size', fontsize = 40)
plt.xlabel('Particle size (\u03bcm)', fontsize = 30)
plt.ylabel('Corner Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

#%%
fit,cov = np.polyfit(particle_size,spring_constant,1,cov=True)
fitplot = np.poly1d(fit)
sig0 = np.sqrt(cov[0,0])
sig1 = np.sqrt(cov[1,1])

#plt.grid()
#plt.xlabel('Sample Rate (Hz)')
#plt.ylabel('Number of Maths Loops')
plt.plot(particle_size, fitplot(particle_size))
#plt.plot(samplerate,loopno, 'x')
#plt.show()

print('Slope = %.10f +- %.4f' %(fit[0],sig0))
print('Intercept = %.10f +- %.4f' %(fit[1],sig1))
print('Equation')
print(fitplot)

plt.grid()
#plt.plot(particle_size, corner_freq, 'rx')
plt.errorbar(particle_size, spring_constant, xerr = size_err, yerr = spring_err, fmt = 'x', markersize = 15)
plt.title('Trap strength vs particle size', fontsize = 40)
plt.xlabel('Particle size (\u03bcm)', fontsize = 30)
plt.ylabel('Trap strength (pN/\u03bcm)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()
#%%

plt.plot(particle_size, friction_coeff, 'x')
plt.show()