# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:06:13 2022

@author: sohum

File to Fourier Transform readings from PSD when blocked and with lights on and off etc to 
determine the major contributing frequencies to the noise in different situations

All of these situations are with no particle being trapped.

"""

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#%% "Fourier Transform of PSD Lights On"

# have to type r before the file location to make it a raw string - this makes loading in files work

t1,t2,v1,v2 = np.loadtxt(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights on\100,000 per batch\batch1", delimiter=',', unpack=True)


#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1 = interp1d(t1,v1, kind='cubic')
f2 = interp1d(t2,v2, kind='cubic')

x1 = np.linspace(t1[0],t1[-1],400000)
x2 = np.linspace(t2[0],t2[-1],400000)

#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#plt.plot(t1,v1,'bx')
#plt.plot(x1,f1(x1))
#plt.xlim(0.15,0.1)
#plt.show()

#D is duration of signal in seconds
D1 = t1[-1] - t1[0] 
D2 = t2[-1] - t2[0] 

#R is the sample rate
R1 = N/D1
R2 = N/D2


yv1 = np.abs(fft(f1(x1))[0:N//2])
xfv1 = fftfreq(N, 1/R1)[:N//2]

yv2 = np.abs(fft(f2(x2))[0:N//2])
xfv2 = fftfreq(N, 1/R2)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

plt.grid()

#plt.plot(xfv1[1:], yv1[1:])
#plt.title('Fourier Transform of PSD Channel 1 Signal with Lights On', fontsize = 40)

#plt.plot(xfv2[1:], yv2[1:])
#plt.title('Fourier Transform of PSD Channel 2 Signal with Lights On', fontsize = 40)

plt.plot(t1,v1, 'rx')

#plt.ylim(0,1500)
#plt.xlim(1,500)
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

print(np.std(v1))
print(np.std(v2))

#%% "Fourier Transform of PSD Lights On, PSD Blocked"

# have to type r before the file location to make it a raw string - this makes loading in files work

data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights on, PSD Blocked\batch3.npy")

t1 = [row[0] for row in data]      
t2 = [row[1] for row in data] 
v1 = [row[2] for row in data]
v2 = [row[3] for row in data]


#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1 = interp1d(t1,v1, kind='cubic')
f2 = interp1d(t2,v2, kind='cubic')

x1 = np.linspace(t1[0],t1[-1],400000)
x2 = np.linspace(t2[0],t2[-1],400000)

#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1 = t1[-1] - t1[0] 
D2 = t2[-1] - t2[0] 

#R is the sample rate
R1 = N/D1
R2 = N/D2

yv1 = np.abs(fft(f1(x1))[0:N//2])
xfv1 = fftfreq(N, 1/R1)[:N//2]

yv2 = np.abs(fft(f2(x2))[0:N//2])
xfv2 = fftfreq(N, 1/R2)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

plt.grid()

#plt.plot(xfv1[1:], yv1[1:])
#plt.title('Fourier Transform of PSD Channel 1 Signal with Lights On, PSD Blocked', fontsize = 40)

#plt.plot(xfv2[1:], yv2[1:])
#plt.title('Fourier Transform of PSD Channel 2 Signal with Lights On, PSD Blocked', fontsize = 40)

plt.plot(t1,v1, 'rx')

#plt.ylim(0,1500)
#plt.xlim(1,500)
#plt.yscale("log")
#plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

print(np.std(v1))
print(np.std(v2))

#%% "Fourier Transform of PSD Lights Off"

# have to type r before the file location to make it a raw string - this makes loading in files work

data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights off\batch1.npy")

t1 = [row[0] for row in data]      
t2 = [row[1] for row in data] 
v1 = [row[2] for row in data]
v2 = [row[3] for row in data]



#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1 = interp1d(t1,v1, kind='cubic')
f2 = interp1d(t2,v2, kind='cubic')

x1 = np.linspace(t1[0],t1[-1],400000)
x2 = np.linspace(t2[0],t2[-1],400000)

#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1 = t1[-1] - t1[0] 
D2 = t2[-1] - t2[0] 

#R is the sample rate
R1 = N/D1
R2 = N/D2

yv1 = np.abs(fft(f1(x1))[0:N//2])
xfv1 = fftfreq(N, 1/R1)[:N//2]

yv2 = np.abs(fft(f2(x2))[0:N//2])
xfv2 = fftfreq(N, 1/R2)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

plt.grid()

#plt.plot(xfv1[1:], yv1[1:])
#plt.title('Fourier Transform of PSD Channel 1 Signal with Lights Off', fontsize = 40)

#plt.plot(xfv2[1:], yv2[1:])
#plt.title('Fourier Transform of PSD Channel 2 Signal with Lights Off', fontsize = 40)

plt.plot(t1,v1, 'rx')

#plt.ylim(0,1500)
#plt.xlim(1,500)
#plt.yscale("log")
#plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

print(np.std(v1))
print(np.std(v2))

#%% "Fourier Transform of PSD Lights Off, PSD Blocked"

# have to type r before the file location to make it a raw string - this makes loading in files work

data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights off, PSD Blocked\batch1.npy")

t1 = [row[0] for row in data]      
t2 = [row[1] for row in data] 
v1 = [row[2] for row in data]
v2 = [row[3] for row in data]


#To get the higher freq components in the fourier transform we need more than 100,000 samples
#To do this we need to make a function that fits the data
#We can then fourier transform that function and use an arbitrarily large amount of samples

f1 = interp1d(t1,v1, kind='cubic')
f2 = interp1d(t2,v2, kind='cubic')

x1 = np.linspace(t1[0],t1[-1],400000)
x2 = np.linspace(t2[0],t2[-1],400000)



#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1 = t1[-1] - t1[0] 
D2 = t2[-1] - t2[0] 

#R is the sample rate
R1 = N/D1
R2 = N/D2

yv1 = np.abs(fft(f1(x1))[0:N//2])
xfv1 = fftfreq(N, 1/R1)[:N//2]

yv2 = np.abs(fft(f2(x2))[0:N//2])
xfv2 = fftfreq(N, 1/R2)[:N//2]


# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

plt.grid()

#plt.plot(xfv1[1:], yv1[1:])
#plt.title('Fourier Transform of PSD Channel 1 Signal with Lights Off, PSD Blocked', fontsize = 40)

#plt.plot(xfv2[1:], yv2[1:])
#plt.title('Fourier Transform of PSD Channel 2 Signal with Lights Off, PSD Blocked', fontsize = 40)

plt.plot(t1,v1, 'rx')

#plt.ylim(0,1500)
#plt.xlim(1,500)
#plt.yscale("log")
#plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()

print(np.std(v1))
print(np.std(v2))
