import time as t
import numpy as np
from ADCDACPi import ADCDACPi
import matplotlib.pyplot as plt

# create an instance of the ADCDAC Pi with a DAC gain set to 1 or 2 depending on if
# you want 0 to 2.048 or 3.3 V 
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)

#z = 1.02943288
1.0323639287272723
#z = 1
#z = 1.0357523529696966  #value for scaling factor at 0.8W from our fit function
#z = 1.0310085590303026 #value for scaling factor at 0.1W from our fit function
#z = 1.0323639287272723 #value for scaling factor at 0.3W from our fit function
z = 1.1255542576995787 #scaling factor for 1.3 W used for particle aa

# this is the number we need to multiply channel 2 by to have both channels read the same value
# when no light is getting in to the PSD. (BLOCKED LIGHTS OFF)
# Therefore when particle is in middle of PSD, both channels should read same val


def realtimev(channel): # Looped read from channel of choice, scrolling display
    if channel ==1:
        Z = 1
    else:
        Z = 1.0294179888328863
        
    while True:
        v = Z * adcdac.read_adc_voltage(channel, 0)
        print(v)
        t.sleep(0.2) #waits 1 second before printing the net v reading
        
def realtimev_both(): # Looped read from channel of choice, scrolling display
    while True:
        v1 = adcdac.read_adc_voltage(1, 0)
        v2 = z * adcdac.read_adc_voltage(2, 0)
        print("v1 = ", v1, " v2 = ", v2)
        t.sleep(1) #waits 1 second before printing the net v reading 

def realtimevN(channel, N): # Looped read from channel of choice, scrolling display with N number of points
    start = t.time()
    if channel ==1:
        Z = 1
    else:
        Z = 1.0294179888328863
    
    while N > 0:
        v = Z * adcdac.read_adc_voltage(channel, 0)
        print(v)
        N = N - 1
        #t.sleep(1) #waits 1 second before printing the net v reading 
    end = t.time()
    elapsed = end - start
    print("Time Elapsed = ", elapsed)
    
   # 3.3837053775787354 seconds to display 1000 consecutive redings with no time delay
   
def realtimev_bothN(N): # Looped read from channel of choice, scrolling display with N number of points
    start = t.time()
    v1s = []
    v2s = []
    while N > 0:
        v1 = adcdac.read_adc_voltage(1, 0)
        #v1s.append(v1)
        v2 = z * adcdac.read_adc_voltage(2, 0)
        #v2s.append(v2)
        print("v1 = ", v1, " v2 = ", v2)
        N = N - 1
        t.sleep(1) #waits 1 second before printing the net v reading 
    end = t.time()
    elapsed = end - start
    print("Time Elapsed = ", elapsed)
    
    return v1s, v2s



def stats(channel, samples): # Read N samples of voltage data, do indicative stats.
    varray = np.zeros(samples)
    if channel ==1:
        Z = 1
    else:
        Z = 1.0294179888328863
            
    while samples >= 0 :     # Populate data array
        varray[samples-1] = Z * adcdac.read_adc_voltage(channel, 0)
        samples = samples -1
    
    a= np.mean(varray)
    b= np.std(varray)
    print("Mean = ", a, " SD = ", b)
    
    return a, b

def statsboth(samples): # Read N samples of voltage data, do indicative stats.
    varray1 = np.zeros(samples)
    varray2 = np.zeros(samples)
    while samples >= 0 :     # Populate data array
        varray1[samples-1] = adcdac.read_adc_voltage(1, 0)
        varray2[samples-1] = z * adcdac.read_adc_voltage(2, 0)
        samples = samples -1
    
    a= np.mean(varray1)
    b= np.mean(varray2)
    c= np.std(varray1)
    d= np.std(varray2)
    e= varray1
    f= varray2
    print("Mean 1 = ", a, " Mean 2 = ", b)
    print("SD 1 = ", c, " SD 2 = ", d)
    
    return a, b, c, d

def realtime_stats(channel, samples):
    means = []  #for each run of stats on (samples) number of points append the mean and SD
    SDs = []    #to a list of the means and SDs. We can then calc the mean and sd of the means and Sds
    while True:
        a,b = stats(channel, samples)
        means.append(a)
        SDs.append(b)
        #time.sleep(0.2)
    return means, SDs
        
def realtime_statsboth(samples):
    means1 = []  #for each run of stats on (samples) number of points append the mean and SD
    SDs1 = []    #to a list of the means and SDs. We can then calc the mean and sd of the means and Sds
    means2 = []
    SDs2 = []
    
    while True:
        a,b,c,d = statsboth(samples)
        means1.append(a)
        means2.append(b)
        SDs1.append(c)
        SDs2.append(d)
        #time.sleep(0.2)
    
    return means1, means2, SDs1, SDs2 

def realtime_statsN(channel, samples, N):
    means = []  #for each run of stats on (samples) number of points append the mean and SD
    SDs = []    #to a list of the means and SDs. We can then calc the mean and sd of the means and Sds
    start = t.time()
    #N is numer of times realtime_stats is looped for
    #If smaples is 100, and N = 3 then for thee runs of 100 points, the mean and sd will bbe calculated for
    #each run of the 3 runs of 100 points
    
    while N > 0:
        a,b = stats(channel, samples)
        means.append(a)
        SDs.append(b)
        #t.sleep(0.1)
        N = N -1
        
    return means, SDs
        
    
def realtime_statsbothN(samples, N):
    means1 = []  #for each run of stats on (samples) number of points append the mean and SD
    SDs1 = []    #to a list of the means and SDs. We can then calc the mean and sd of the means and Sds
    means2 = []
    SDs2 = []
    #N is numer of times realtime_stats is looped for
    #If smaples is 100, and N = 3 then for thee runs of 100 points, the mean and sd will bbe calculated for
    #each run of the 3 runs of 100 points
    
    while N > 0:
        a,b,c,d = statsboth(samples)
        means1.append(a)
        means2.append(b)
        SDs1.append(c)
        SDs2.append(d)
        #time.sleep(0.2)
        N = N -1
    
    return means1, means2, SDs1, SDs2 
        
#v1,v2 = statsboth(100000)
#x = np.linspace(0,10,100000)
#plt.plot(x,v1,'rx')
#plt.show()

