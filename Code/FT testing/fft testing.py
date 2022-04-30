# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:03:34 2022

@author: tisia
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from numpy.random import random
from scipy.interpolate import interp1d
import scipy.optimize as spo

def sine(time,amplitude,frequency,phase,offset):
        wave = amplitude*(np.sin(time*2*np.pi*frequency + phase)) + offset
        return wave
#%% pure

 
N = 400000
t = np.linspace(0,10,N)

test = sine(t,0.04,50,0,2)

fy = np.abs(fft(test)[0:N//2])
fx = fftfreq(N,1/N)[:N//2]

plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(t, test)
plt.show()

#%%
N = 400000
t = np.linspace(0,10,N)

test = sine(t,0.04,50,0,2) + sine(t,0.02,100,0,2)

fy = np.abs(fft(test)[0:N//2])
fx = fftfreq(N,1/N)[:N//2]

plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(t, test)
plt.show()



#%% sine wave of frequencies from 0-20,000 sampled at a rate of 10 KHz for 100,000 samples. Therefore time of sample is 10 seconds

frequencies = np.arange(0,20000,50)

N = 100000
t = np.linspace(0,10,N)
wave = 0
for f in frequencies:
    wave = wave + sine(t,0.04,f,0,2)
    
# to replicate process in actual experiment, interpolate a fit to the 100,000 points to make a smooth function


f1 = interp1d(t,wave, kind='cubic')


x1 = np.linspace(t[0],t[-1],400000)



#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D = t[-1] - t[0]  


#R is the sample rate
R = N/D


fy = np.abs(fft(f1(x1))[0:N//2])
fx = fftfreq(N, 1/R)[:N//2]


#fy = np.abs(fft(wave)[0:N//2])
#fx = fftfreq(N,1/N)[:N//2]

#%% same as above but for a sine wave made of random proportions of frequencies from 0 to 20,000
frequencies = np.array(50000*random(1000))
amps = np.array(random(1000))
N = 1000000
t = np.linspace(0,1,N)
wave = 0
for i in  range(len(frequencies)):
    wave = wave + sine(t,amps[i],frequencies[i],0,2)
    
f1 = interp1d(t,wave, kind='cubic')


x1 = np.linspace(t[0],t[-1],400000)



#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D = t[-1] - t[0]  


#R is the sample rate
R = N/D


fy = np.abs(fft(f1(x1))[0:N//2])
fx = fftfreq(N, 1/R)[:N//2]
    

#fy = np.abs(fft(wave)[0:N//2])
#fx = fftfreq(N,1/N)[:N//2]

#%% sine graph
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(t, wave)
plt.show()


#%% ft graph
plt.grid()
#plt.yscale("log")
#plt.xscale("log")
plt.title('Fourier Transform of a Signal composed of Random mplitude sine waves', fontsize = 40)
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
#plt.legend(loc='best', fontsize = 20)
plt.plot(fx[1:20000], fy[1:20000])
plt.show()
