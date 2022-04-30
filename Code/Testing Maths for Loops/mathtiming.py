from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
#import matplotlib.pyplot as plt

# file dedicated to testing how the math loop can adjust the samplerate
# for a given bus speed, all testing was done with 2.5MHz bus 


# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(1)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)
# testing how long a math calculation takes so that we can loop that to control
# the samplerate


#ONCE AGAIN NEED TO HAVE A COPY OF ADCDACPi.py in same folder as this file



def readvsr(channel, no_samples, input_samplerate):
    # function to read and save as many datapoints as you like into an array
    # from channel 1 or 2
    # this function is with an adjustable sample rate, however seems to not work
    # if manual sample rate is low like 10-100 Hz is fine, however higher values
    # don't work. Without t.sleep() if max speed is 28kHz, no matter how high
    # make input_sample rate, the acctual measured rate is only 6kHz ish max
    
    counter = 1
    
    varray = np.zeros(no_samples)
    tarray = np.zeros(no_samples)
    
    ln = int(-0.04711*input_samplerate + 1307)  # where ln is loop number

    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to voltages array
        varray[counter - 1] = adcdac.read_adc_voltage(channel, 0)
        tarray[counter - 1] = ti.time()
        counter = counter + 1
        for o in range(ln):
            1+1
 
    start = tarray[0]
    #print("Start: " + str(start))
    end = tarray[-1]
    #print("End: " + str(end))
    
    totalseconds = end - start
    samplerate = no_samples / totalseconds #actual samples per second

    #print("Time Elapsed = ", totalseconds)
    #print("No. Samples per Channel = ", no_samples)
    #print("Input Samplerate = ", input_samplerate)
    print("Actual Samplerate = " + str(samplerate))
    
    for i in range(len(tarray)):
        tarray[i]-=start
        
    return varray, tarray, samplerate



def readvbothsr(no_samples,input_samplerate):
    # function to read and save as many datapoints as you like into 2 arrays
    # 1 for channel 1, and 1 for channel 2. Both channels take same number of readings
    # this function can only sample each channel at half the speed of a single channel
    # so at 2.5MHz with no math loop delay, each channel samples at 14.6 kHz 

    counter = 1
    
    varray1 = np.zeros(no_samples)
    varray2 = np.zeros(no_samples)

    tarray1 = np.zeros(no_samples)
    tarray2 = np.zeros(no_samples)
    
    start = ti.time()
    #print("Start: " + str(start))

    ln = int(-0.1357*input_samplerate + 1995)  # where ln is loop number # 
    #print(ln/2)

    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to volatages array
        varray1[counter - 1] = adcdac.read_adc_voltage(1, 0)
        tarray1[counter - 1] = ti.time()
        varray2[counter - 1] = adcdac.read_adc_voltage(2, 0)
        tarray2[counter - 1] = ti.time()
        counter = counter + 1
        for o in range(ln): #dividing by 2 overshoots the sample rate a bit so I changed to 1.8 to see
            1+1                      #this seems to give a closer sample rate to what's desired

    end = ti.time()
    #print("End: " + str(end))
    
    totalseconds = end - start
    
    samplerate1 = no_samples / (tarray1[-1] - tarray1[0]) #actual samples per second channel 1
    samplerate2 = no_samples / (tarray2[-1] - tarray2[0]) #actual samples per second channel 2

    #print("Time Elapsed Total= ", totalseconds)
    #print("No. Samples per Channel = ", no_samples)
    print("Actual Samplerate1 = " + str(samplerate1))
    print("Actual Samplerate2 = " + str(samplerate2))
    
    for i in range(len(tarray1)):
        tarray1[i]-=start

    for j in range(len(tarray2)):
        tarray2[j]-=start
            
    return tarray1, tarray2, varray1, varray2, samplerate1, samplerate2




srlist = [] #samplerate list

#for p in range(10):
    #t,v,sr = readvsr(1,100000,21000)
    #srlist.append(sr)

#srarray = np.array(srlist)
#print(np.mean(srarray))

sr1list = []
sr2list = []

for q in range(10):
    t1,t2,v1,v2,sr1,sr2 = readvbothsr(100000,13000)
    sr1list.append(sr1)
    sr2list.append(sr2)
    
sr1array = np.array(sr1list)
sr2array = np.array(sr2list)
print(np.mean(sr1array))
print(np.mean(sr2array))