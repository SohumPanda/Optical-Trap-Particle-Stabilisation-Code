# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:24:26 2021

@author: tisia
"""
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#%%
times,voltages = np.loadtxt(r'C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\ADC Bus Speed Testing\1kHz waves\1kHz 1.2V Sine 100000 samples 2.50 MHz bus data.csv', delimiter=',', usecols=(0,1), unpack=True)

plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.plot(times[100:300], voltages[100:300], 'rx')
plt.show()

#%%

def sin_fit(time,voltage,frequency):
    amplitude = np.std(voltage)*2**0.5
    offset = np.mean(voltage)
    p0 = np.array([amplitude, 2*np.pi*frequency, 0, offset])
    
    
    def sine(t,amp,w,phi,c):
        wave = amp*(np.sin(t*w + phi)) + c
        return wave
    fit,pcov = curve_fit(sine, time, voltage, p0=p0)
    amp, w, phi, c = fit
    f = w/(2.*np.pi)
    fitfunc = lambda t: amp * np.sin(w*t + phi) + c
    residuals = voltage - sine(time, *fit)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((voltage-np.mean(voltage))**2)
    r_squared = 1-(ss_res/ss_tot) #not sure this is legal for a sine function
    return {"amp": amp, "omega": w, "phase": phi, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (p0,fit,pcov), "residuals": residuals, "r_squared": r_squared}

res = sin_fit(times,voltages,1000)
#plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)
# p=[2000, 56, 2] #a is amplitude  #b is mean   #c is standard deviation   #d is a y shift
# fit,cov=spo.curve_fit(gaussian, x, yv1h[start*10:end*10], p)
# #plt.plot(x, gaussian(x, *fit), color='red', linewidth = 4)

def sinewave(time,amplitude,frequency,phase,offset):
        wave = amplitude*(np.sin(time*2*np.pi*frequency + phase)) + offset
        return wave

timetime = np.arange(0.0044, 0.0131, 0.00001)
plt.plot(timetime, sinewave(timetime,0.17673704645414548,1000.1178045841456,-0.02834908688428308,0.18897403623744596), "r-", label = "Fit")

print( "Amplitude=%(amp)s, Angular frequency=%(omega)s, Frequency=%(freq)s, phase=%(phase)s, offset=%(offset)s, Max. Cov.=%(maxcov)s, r_squared=%(r_squared)s" % res )
plt.plot(times[100:300], voltages[100:300], "x", label="Data", linewidth=2, markersize=15)
#plt.plot(times[100:300], res["fitfunc"](times)[100:300], "r-", label="Fit", linewidth=1)
plt.legend(loc="best", fontsize=25)
plt.xlabel('Time (s)', fontsize = 30)
plt.ylabel('Voltage (V)', fontsize = 30)
plt.title('2.55 MHz ADC clock speed, sampling 1 KHz sine wave', fontsize = 40)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.grid()
plt.show()

#%%

