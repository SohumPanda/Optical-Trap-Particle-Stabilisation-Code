#from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt

# t1,t2,v1,v2 = np.loadtxt('/home/pi/Desktop/Sohum and Kai/PSD/No particle trapped/Lights on/100,000 per batch/batch1', delimiter=',', unpack=True) #be mindful of if you are loading a .csv or.txt or if file has nothing next to it just write it like that

# t1,v1 = np.loadtxt('batch1', delimiter=',', unpack = True) #loads times and voltages as ARRAYS
# t2,v2 = np.loadtxt('batch2', delimiter=',', unpack = True)

# there is a gap in time between the last time reading in batch 1 and the 1st time reading in batch2 due to the time it takes to save.
# however from our continous run function, we know the value of each gap, and so for the first gap, we can add the gap value and the last time
# of the batch1 to every time in batch 2 to get the times in batch2 to follow chronologically after 0. Each batch saves its first point s t=0

# g = [0.02251720428466797]


# for i in range(len(t2)):
#     t2[i] += t1[-1] + g[0]
    
# t = np.concatenate([t1,t2])
# v = np.concatenate([v1,v2])

#data1 = np.load('batch1.npy')
#t1 = [row[0] for row in data1]       #loads times and voltages as lists      
#v1 = [row[1] for row in data1]

#data2 = np.load('batch2.npy')
#t2 = [row[0] for row in data2]      
#v2 = [row[1] for row in data2] 

data = np.load(r'C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\No particle trapped\Lights on, PSD Blocked\batch1.npy')
#data = np.load('/home/pi/Desktop/Sohum and Kai/Splicing batches together/batch worst physical.npy')
#data = np.load('batch1.npy')
#data = np.load(r'C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\Voltage Change per Distance/batch 0,09 mm.npy')
#ata = np.load(r'C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\Voltage Change Using Camera/batch1.npy')    
#data = np.load('//home/pi/Desktop/Sohum and Kai/PSD/Particle Trapped/particle h/batch2.npy')
#data = np.load('/home/pi/Desktop/Sohum and Kai/PSD/Particle Trapped/Voltage Change per Distance/Scale factor for 0,6 micro Watt/batch1.npy')

t1 = [row[0] for row in data]      
t2 = [row[1] for row in data] 
v1 = [row[2] for row in data]
v2 = [row[3] for row in data]

#g = [0.003008604049682617]

#for i in range(len(t2)):
    #t2[i] += t1[-1] + g[0]
    
#t = t1 + t2   #for lists you don't need to use CONCATENATE. This is how you add a list onto the end of another one     
#v = v1 + v2

plt.grid()
#plt.xlabel('Time (s)')
#plt.ylabel('Voltage (V)')
# plt.xlim(0.015,0.07)
#plt.savefig("5 Hz 1.2V 0V offset 100000 samples retest.png")
#plt.plot(readv1.tarray1[100:20000], readv1.varray1[100:20000])
#plt.plot(readv1.tarray1[100:4000], readv1.varray1[100:4000], 'rx')
#plt.plot(readv1.tarray1[100:20000], readv1.varray1[100:20000])
#plt.title('Section of ADC output for 1.2V 1kHz sine wave 2 MHz bus')
# plt.title('First PSD Reading')


#plt.plot(t, v, 'bx')
# plt.plot(t1, v1, 'bx')
# plt.plot(t2, v2, 'rx')
#plt.plot(t, v)
# plt.plot(t1, v1)
# plt.plot(t2, v2)
#plt.savefig('batches combined 5Hz 3V 0V Offset') #for some reason on SAMSUNG SD, I'cant see the plot but if i save it and open it up it works


plt.xlabel('Time (s)', fontsize = 30)
plt.ylabel('Voltage (V)', fontsize = 30)
plt.plot(t1, v1, 'bx', label = 'channel1', markersize = 15 )
plt.plot(t2, v2, 'rx', label = 'channel2', markersize = 15)
plt.title('Voltage against Time for PSD Blocked, Lights Off', fontsize = 40)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
#plt.axhline(y=meanSD2, color = 'r', linestyle = '-') #this is to plot the mean value of the SDs Channel 1
#plt.axhline(y=meanSD2, color = 'r', linestyle = '-') #this is to plot the mean value of the SDs Channel 2
#plt.errorbar(N, mSD2, yerr = SDSD2, fmt = 'none')
#plt.legend()
plt.show()
print(np.mean(v1))
print(np.std(v1))
print(np.mean(v2))
print(np.std(v2))
print(np.mean(v1)/np.mean(v2))