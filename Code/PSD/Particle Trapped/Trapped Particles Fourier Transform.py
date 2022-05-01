# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:06:13 2022

@author: sohum

File to Fourier Transform readings from data recorded on PSD when a particle is trapped 


All of these situations are with particle being trapped and lights off in the lab.

"""

import numpy as np 
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy.optimize as spo

#depending on if you are using this file on the Pi or on PC or a laptop, you'll need to chnge the path name to get the files you want
#%% "Fourier Transform of PSD Lights Off, PSD Blocked"

# have to type r before the file location to make it a raw string - this makes loading in files work

#data = np.load(r"/home/pi/Desktop/Sohum and Kai/PSD/No particle trapped/Lights off, PSD Blocked/batch1.npy")
data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights off, PSD Blocked\batch1.npy")
#data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\particle k\batch1.npy")

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

plt.axvline(50, color = 'orange', linewidth=3)

plt.plot(xfv1[1:], yv1[1:], label = 'PSD Blocked, Lights Off')
plt.title('Fourier Transform of PSD Channel 1 Signal with Lights Off, PSD Blocked', fontsize = 40)

#plt.plot(xfv2[1:], yv2[1:], label = 'PSD Blocked, Lights Off')
#plt.title('Fourier Transform of PSD Channel 2 Signal with Lights Off, PSD Blocked', fontsize = 40)


#plt.plot(t1,v1,'rx')
#plt.xlabel('Time (s)', fontsize = 30)
#plt.ylabel('Voltage (V)', fontsize = 30)
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)
#plt.legend(loc='best', fontsize = 20)

plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)
#plt.ylim(0,1500)
#plt.xlim(1,500)
#plt.yscale("log")
#plt.xscale("log")
#plt.xlabel('Frequency (Hz)', fontsize = 30)
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)

plt.axvline(5000, color = 'red', linewidth=3)
plt.show()

#%% PARTICLE X - 

# for particle h take batch 2 as batch didn't have the scattered light all on PSD properly 
# use this code to load in any batch for any particle, just change the file location
particle = 'ac'
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

PSDLength = 3.5 #3.5 mm PSD resistive length taken from Hammamatsu Datasheet
Mag = -0.65
position = []
time = []

for i in range(len(v1h)):
    p = 0.5*PSDLength*(v2h[i] -v1h[i])/((v1h[i]+v2h[i])*Mag)
    t = (t1h[i]+t2h[i])/2
    position.append(p)
    time.append(t)
    
#%%
PSDLength = 3.5 #3.5 mm PSD resistive length taken from Hammamatsu Datasheet
Mag = -0.65
position = []
time = []

for i in range(len(v1h)):
    p = 0.5*PSDLength*(v2h[i] -v1h[i])/((v1h[i]+v2h[i])*Mag)
    t = (t1h[i]+t2h[i])/2
    position.append(p)
    time.append(t)

#%% OLD FOURIER TRANSFORM, WILL ONLY GO UP TO 5kHz

x1h = np.linspace(t1h[0],t1h[-1],100000)
x2h = np.linspace(t2h[0],t2h[-1],100000)
xx = np.linspace(time[0],time[-1],100000)

N = 100000

#D is duration of signal in seconds
D1h = t1h[-1] - t1h[0] 
D2h = t2h[-1] - t2h[0]
D = time[-1] - time[0] 

#R is the sample rate
R1h = N/D1h
R2h = N/D2h
R = N/D

yv1h = np.abs(fft(v1h)[0:N//2])
xfv1h = fftfreq(N, 1/R1h)[:N//2]

yv2h = np.abs(fft(v2h)[0:N//2])
xfv2h = fftfreq(N, 1/R2h)[:N//2]

yv = np.abs(fft(position)[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

#%%
f1h = interp1d(t1h,v1h, kind='cubic')
f2h = interp1d(t2h,v2h, kind='cubic')
ff = interp1d(time, position, kind='cubic')


x1h = np.linspace(t1h[0],t1h[-1],400000)
x2h = np.linspace(t2h[0],t2h[-1],400000)
xx = np.linspace(time[0],time[-1],400000)

#N is number of samples
#if we use the raw data then it's 100,000 points
#but if we use the fit function, we can make N as large as we want
#and can thus get up to higher frequencies in our fourier transform
N = 400000

#D is duration of signal in seconds
D1h = t1h[-1] - t1h[0] 
D2h = t2h[-1] - t2h[0]
D = time[-1] - time[0] 

#R is the sample rate
R1h = N/D1h
R2h = N/D2h
R = N/D

yv1h = np.abs(fft(f1h(x1h))[0:N//2])
xfv1h = fftfreq(N, 1/R1h)[:N//2]

yv2h = np.abs(fft(f2h(x2h))[0:N//2])
xfv2h = fftfreq(N, 1/R2h)[:N//2]

yv = np.abs(fft(ff(xx))[0:N//2])
xfv = fftfreq(N, 1/R)[:N//2]

# the length of the xfv is exactly half of N, the number of samples as we only
# want to see the positive frequencies 


def gaussian(x,a,b,c):  #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
    exp= np.exp(-((x-b)**2)/(2*c**2))
    return (a*exp)

#%% Rel Pos vs Time

# plt.figure()
# plt.grid()
# plt.title('Particle {}, {}Hz injected sine wave, Relative Position'.format(particle,freq), fontsize = 40)
# plt.plot(time,position,'gx', label = 'Particle {}'.format(particle))
# plt.xlabel('Time (s)', fontsize = 30)
# plt.ylabel('Relative Position (mm)', fontsize = 30)
# plt.xticks(fontsize = 30)
# plt.yticks(fontsize = 30)
# plt.legend(loc='best', fontsize = 20)

#%% Channel Voltage vs Time

plt.figure()

#plt.title('Particle {}, Voltage vs Time, Channel 1'.format(particle), fontsize = 40)
plt.title('Particle {}, {}Hz injected sine wave, Channel 1'.format(particle,freq), fontsize = 40)
plt.plot(t1h,v1h, 'rx', label = 'Particle {}'.format(particle))

plt.grid()
plt.xlabel('Time (s)', fontsize = 30)
plt.ylabel('Voltage (V)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)


plt.figure()

#plt.title('Particle {}, Voltage vs Time, Channel 2'.format(particle), fontsize = 40)
plt.title('Particle {}, {}Hz injected sine wave, Channel 2'.format(particle,freq), fontsize = 40)
plt.plot(t2h,v2h, 'rx', label = 'Particle {}'.format(particle))

plt.grid()
plt.xlabel('Time (s)', fontsize = 30)
plt.ylabel('Voltage (V)', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)

#%% FT of Rel Pos vs Time and Log Log of That

# plt.figure()
# plt.grid()
# plt.title('FT of Particle {} Relative Position, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
# plt.plot(xfv[1:], yv[1:], label = 'Particle {}'.format(particle))
# plt.xlabel('Frequency (Hz)', fontsize = 30)
# plt.ylabel('Amplitude', fontsize = 30)
# plt.xticks(fontsize = 30)
# plt.yticks(fontsize = 30)
# plt.legend(loc='best', fontsize = 20)
# 
# 
# plt.figure()
# plt.grid()
# plt.title('FT of Particle {} Relative Position, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
# plt.plot(xfv[1:], yv[1:], label = 'Particle {}'.format(particle))
# plt.yscale("log")
# plt.xscale("log")
# plt.xlabel('Frequency (Hz)', fontsize = 30)
# plt.ylabel('Amplitude', fontsize = 30)
# plt.xticks(fontsize = 30)
# plt.yticks(fontsize = 30)
# plt.legend(loc='best', fontsize = 20)

#%% FT of Channel Voltage vs Time

# plt.figure()
# 
# plt.title('FT of Particle {} Channel 1'.format(particle), fontsize = 40)
# #plt.title('FT of Particle {} Channel 1, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
# plt.plot(xfv1h[1:], yv1h[1:], label = 'Particle {}'.format(particle))
# 
# #plt.title('FT of Particle {} Channel 2'.format(particle), fontsize = 40)
# #plt.title('FT of Particle {} Channel 2, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
# #plt.plot(xfv2h[1:], yv2h[1:], label = 'Particle {}'.format(particle))
# 
# plt.grid()
# plt.xlabel('Frequency (Hz)', fontsize = 30)
# plt.ylabel('Amplitude', fontsize = 30)
# plt.xticks(fontsize = 30)
# plt.yticks(fontsize = 30)
# plt.legend(loc='best', fontsize = 20)

#%%  FT of Channel Voltage vs Time Log Log

plt.figure()

plt.title('FT of Particle {} Channel 1'.format(particle), fontsize = 40)
#plt.title('FT of Particle {} Channel 1, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
plt.plot(xfv1h[1:], yv1h[1:], label = 'Particle {}'.format(particle), color = 'red')

plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)

#%%
plt.figure()

plt.title('FT of Particle {} Channel 2'.format(particle), fontsize = 40)
#plt.title('FT of Particle {} Channel 2, {}Hz injected sine wave'.format(particle,freq), fontsize = 40)
plt.plot(xfv2h[1:], yv2h[1:], label = 'Particle {}'.format(particle))

plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)

#%% FT of Channel and PSD Noise

plt.figure()

plt.title('FT of Particle {} Compared to PSD Noise, Channel 1'.format(particle), fontsize = 40)
plt.plot(xfv1[1:], yv1[1:], label = 'PSD Blocked, Lights Off')
plt.plot(xfv1h[1:], yv1h[1:], label = 'Particle {}'.format(particle))

plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)


plt.figure()

plt.title('FT of Particle {} Compared to PSD Noise, Channel 2'.format(particle), fontsize = 40)
plt.plot(xfv2[1:], yv2[1:], label = 'PSD Blocked, Lights Off')
plt.plot(xfv2h[1:], yv2h[1:], label = 'Particle {}'.format(particle))

plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Frequency (Hz)', fontsize = 30)
plt.ylabel('Amplitude', fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.legend(loc='best', fontsize = 20)

#%% p 55Hz

#plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')


# start = 40
# end = 70
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[2000, 56, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% p 250Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 60Hz
# 
# #plt.plot(xfv1h[590:700], yv1h[590:700], label = 'Particle w')
# 
# 
# start = 55
# end = 70
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[2500, 60, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 70Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 80Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 90Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 100Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]
# 
#%% w 250Hz
# 
# #plt.plot(xfv1h[400:700], yv1h[400:700], label = 'Particle p', color='b')
# 
# 
# start = 230
# end = 280
# no_points = (end-start)*10
# 
# x = xfv1h[start*10:end*10]
# 
# 
# 
# p=[600, 250, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# 
# #print(*fit) #prints the [amplitude, mean, standard deviatio, y shift]

#%% plotting hortizontal and vert lines for corner freq 
 
 
#plt.axhline(160) #h  corner freq = 165
#plt.axhline(130) #i  corner freq = 158  
#plt.axhline(60) #j   corner freq = 96
#plt.axhline(170) #k  corner freq = 131
#plt.axhline(100) #m  corner freq = 173
#plt.axhline(30) #n   corner freq = 157
#plt.axhline(100) #o  corner freq = 170
#plt.axhline(65) #v   corner freq = 130
#plt.axhline(10) #w   corner freq = 150
#plt.axhline(60) #z   corner freq = 100
#plt.axhline(35)  #ab  corner freq = 151
 
 
#plt.axvline(100)
#plt.axvline(97)
#plt.axvline(90)
 
#plt.axvline(120)
#plt.axvline(130)
#plt.axvline(140)
plt.axvline(151)
#plt.axvline(155)
#plt.axvline(157)
plt.axvline(160)
#plt.axvline(165)
plt.axvline(170)
#plt.axvline(173)
#plt.axvline(180)
#plt.axvline(190)

plt.show()


