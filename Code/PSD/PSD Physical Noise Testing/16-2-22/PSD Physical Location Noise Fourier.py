# -*- coding: utf-8 -*-
"""
Created on Wed Feb  16 18:06:13 2022

@author: sohum

File to Fourier Transform readings from PSD when blocked and with lights on and off etc to 
determine the major contributing frequencies to the noise in different physical locations

All of these situations are with no particle being trapped.

"""

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


#%% "Fourier Transform of PSD Best and Worst Physical Conditions"

# have to type r before the file location to make it a raw string - this makes loading in files work
dataw = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\PSD Physical Noise Testing\16-2-22\batch worst physical.npy")
#dataworst physical setup


t1w = [row[0] for row in dataw]      
t2w = [row[1] for row in dataw] 
v1w = [row[2] for row in dataw]
v2w = [row[3] for row in dataw]


#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1w = interp1d(t1w,v1w, kind='cubic')
f2w = interp1d(t2w,v2w, kind='cubic')

x1w = np.linspace(t1w[0],t1w[-1],400000)
x2w = np.linspace(t2w[0],t2w[-1],400000)


#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1w = t1w[-1] - t1w[0] 
D2w = t2w[-1] - t2w[0] 

#R is the sample rate
R1w = N/D1w
R2w = N/D2w

yv1w = np.abs(fft(f1w(x1w))[0:N//2])
xfv1w = fftfreq(N, 1/R1w)[:N//2]

yv2w = np.abs(fft(f2w(x2w))[0:N//2])
xfv2w = fftfreq(N, 1/R2w)[:N//2]


datab = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\PSD Physical Noise Testing\16-2-22\batch best physical.npy")
#databest physical setup

t1b = [row[0] for row in datab]      
t2b = [row[1] for row in datab] 
v1b = [row[2] for row in datab]
v2b = [row[3] for row in datab]


#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1b = interp1d(t1b,v1b, kind='cubic')
f2b = interp1d(t2b,v2b, kind='cubic')

x1b = np.linspace(t1b[0],t1b[-1],400000)
x2b = np.linspace(t2b[0],t2b[-1],400000)

D1b = t1b[-1] - t1b[0] 
D2b = t2b[-1] - t2b[0] 

#R is the sample rate
R1b= N/D1b
R2b = N/D2b

yv1b = np.abs(fft(f1b(x1b))[0:N//2])
xfv1b = fftfreq(N, 1/R1b)[:N//2]

yv2b = np.abs(fft(f2b(x2b))[0:N//2])
xfv2b = fftfreq(N, 1/R2b)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

plt.grid()

#plt.plot(xfv1w[1:], yv1w[1:], label = 'Worst Physical Condition')
#plt.title('Fourier Transform of PSD Channel 1 Signal Worst Physical Conditions', fontsize = 40)

plt.plot(xfv2w[1:], yv2w[1:], label = 'Worst Physical Condition')
#plt.title('Fourier Transform of PSD Channel 2 Signal Worst Physical Conditions', fontsize = 40)

#plt.plot(xfv1b[1:], yv1b[1:], label = 'Best Physical Condition')
#plt.title('Fourier Transform of PSD Channel 1 Signal Best Physical Conditions', fontsize = 40)

plt.plot(xfv2b[1:], yv2b[1:], label = 'Best Physical Condition')
#plt.title('Fourier Transform of PSD Channel 2 Signal Best Physical Conditions', fontsize = 40)


#plt.title('Fourier Transform of Channel 1: Best vs Worst Physical Conditions', fontsize = 40)
plt.title('Fourier Transform of Channel 2: Best vs Worst Physical Conditions', fontsize = 40)
#plt.ylim(0,1500)
#plt.xlim(1,500)
plt.yscale("log")
plt.xscale("log")
plt.ylabel('Amplitude', fontsize = 30)
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc = 'best', fontsize = 20)
plt.show()






