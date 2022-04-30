# -*- coding: utf-8 -*-
"""
When looking at raw data from each channel it is a combination 
of brightness and position that we are seeing. 

We want to extract position from this data, which we can do by 
[ ch1 - ch2/ (ch1 + ch2) ] x [PSD length]

This will give the relative displacement of the particle from equilibrium. 
Equilibrium which would be the point at which the readings on both channels are the same.
The equilibrium should be the middle of the PSD

The electronics have a slight discrepancy which means a multiplicative factor needs to be 
added to give both channels the same reading when the C.O.M of the light is on the actual middle of the PSD


Created on Mon Mar 21 11:38:20 2022

@author: sohum
"""
import numpy as np 
import matplotlib.pyplot as plt
#%%
data = np.load(r"batch1.npy")
#data = np.load(r"C:\Users\sohum\OneDrive\Documents\Uni\Year4\Masters Project\Sohum and Kai\PSD\Particle Trapped\particle k\batch1.npy")

t1 = [row[0] for row in data]      
t2 = [row[1] for row in data] 
v1 = [row[2] for row in data]
v2 = [row[3] for row in data]

PSDLength = 3.5 #3.5 mm PSD resistive length taken from Hammamatsu Datasheet
Mag = -0.65
position = []
time = []

for i in range(len(v1)):
    p = 0.5*PSDLength*(v2[i] -v1[i])/((v1[i]+v2[i])*Mag)
    t = (t1[i]+t2[i])/2
    position.append(p)
    time.append(t)
    
#np.savetxt('position', position)
    
plt.grid()
plt.plot(time,position,'gx')
plt.plot(t1,v1,'rx')
plt.plot(t2,v2,'bx')
plt.show()
