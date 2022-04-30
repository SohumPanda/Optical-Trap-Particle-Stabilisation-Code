#from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt
import copy

# t1,t2,v1,v2 = np.loadtxt('/home/pi/Desktop/Sohum and Kai/PSD/Lights on, no particle/batch1', delimiter=',', unpack=True) #be mindful of if you are loading a .csv or.txt or if file has nothing next to it just write it like that

####### SPLICING FOR ARRAYS. NOT USED AS WE SAVE DATA WITH NP.SAVE NOW SO ONLY NEED TO HAVE SPLICING FOR LISTS #######

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

#######################################################################################################################


#data = np.load('batch1.npy')
# t1 = [row[0] for row in data]      
# t2 = [row[1] for row in data] 
# v1 = [row[2] for row in data]
# v2 = [row[3] for row in data]


st,g1,g2 = np.loadtxt('savetimes_and_gaps', delimiter=',', unpack=True)
#loads in the savetimes and gaps from the run


#THIS CAN LOAD IN TIMES AND VOLTAGES FROM N BATCHES

t1s = [] # a list of all the t1's lists from each batch
t2s = [] # a list of all the t2's lists from each batch
v1s = [] # a list of all the v1's lists from each batch
v2s = [] # a list of all the v2's lists from each batch

N = 10 # no of batches to load in

for x in range(1,N+1): #go from 1 to no_batches
    
    data = np.load('batch' + str(x) + '.npy')
    
    t1bx = [row[0] for row in data]      
    t2bx = [row[1] for row in data] 
    v1bx = [row[2] for row in data]
    v2bx = [row[3] for row in data]
    
    t1s.append(t1bx)
    t2s.append(t2bx)
    v1s.append(v1bx)
    v2s.append(v2bx)
        

a = copy.deepcopy(t1s)
b = copy.deepcopy(t2s)
c = copy.deepcopy(v1s)
d = copy.deepcopy(v2s)

t1 = a[0]  #take the first times list from t1s and let the cumulative t1 = t1 from batch 1
t2 = b[0]
v1 = c[0]
v2 = d[0]

# Adds all the times up correctly from the N batches for channels 1 and 2
# Also combines all the voltages up into one long list for v1s and v2s

for x in range(N-1):
    t1_next = a[x+1]
    t2_next = b[x+1]
    v1_next = c[x+1]
    v2_next = d[x+1]
    
    for i in range(len(t1_next)):
        t1_next[i] += t1[-1] + g1[x]   
        t2_next[i] += t2[-1] + g2[x]
    
    t1 = t1 + t1_next  #adds the next array to the combined times array
    t2 = t2 + t2_next  #for lists you don't need to use CONCATENATE. This is how you add a list onto the end of another one
    v1 = v1 + v1_next
    v2 = v2 + v2_next
    

plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
# plt.xlim(0.015,0.07)
#plt.savefig("5 Hz 1.2V 0V offset 100000 samples retest.png")
#plt.plot(readv1.tarray1[100:20000], readv1.varray1[100:20000])
#plt.plot(readv1.tarray1[100:4000], readv1.varray1[100:4000], 'rx')
#plt.plot(readv1.tarray1[100:20000], readv1.varray1[100:20000])
#plt.title('Section of ADC output for 1.2V 1kHz sine wave 2 MHz bus')
# plt.title('First PSD Reading')
#plt.plot(t, v, 'bx')
plt.plot(t1, v1, 'bx')
# plt.plot(t2, v2, 'rx')
#plt.plot(t, v)
# plt.plot(t1, v1)
# plt.plot(t2, v2)
#plt.savefig('batches combined 5Hz 3V 0V Offset') #for some reason on SAMSUNG SD, I'cant see the plot but if i save it and open it up it works
plt.show()
