# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy import genfromtxt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks



#%%
#NEED TO SELECT CORRECT DIRECTORY UP IN TOP RIGHT TO LOAD THESE FILES IN

time,voltage = np.loadtxt('TN 2.62 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 2.62 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 2.62 Noise')
plt.grid()
#plt.ylim(0,8)
plt.xlim(10,2500)
plt.show()

#noise freq made up of mostly 125, 242, 366, 492, 975 Hz
#%%

time,voltage = genfromtxt('TN 2.74 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 2.74 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 2.74 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(10,4500)
plt.show()

#%%

time,voltage = genfromtxt('TN 2.86 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 2.86 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 2.86 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 2.95 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 2.95 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 2.95 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.05 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.05 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.05 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.15 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.15 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.15 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.27 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.27 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.27 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.36 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.36 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.36 Noise')
plt.grid()
plt.ylim(0,20)
plt.xlim(0,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.48 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.48 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.48 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(10,2500)
plt.show()

#%%

time,voltage = genfromtxt('TN 3.57 AC.csv', delimiter=',', unpack=True)

#the arrays are 119040 long

#N is the number of samples
N = 119040

#D is duration of signal in seconds
D = time[-1] - time[0] 

#R is the sample rate
R = N/D

f1 = interp1d(time,voltage, kind='cubic')

x1 = np.linspace(time[0],time[-1],N)

#Fourier transform for TN 3.57 AC. The noise part of the signal has been fourier transformed
#to see the main frequency components of the noise 

yv = np.abs(fft(f1(x1))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#the length of xfv is 59520, which is exactly half of N, the number of samples as we only
# want to see the positive frequencies 

#plt.plot(time,voltage,'bx')
#plt.plot(x1,f1(x1))

plt.plot(xfv[1:], yv[1:])
#plt.plot(time,voltage)
plt.title('Fourier Transform of TN 3.57 Noise')
plt.grid()
plt.ylim(0,5)
plt.xlim(0,2500)
plt.show()




