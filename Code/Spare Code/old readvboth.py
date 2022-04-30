from ADCDACPi import ADCDACPi
import time as t
import numpy as np
import matplotlib.pyplot as plt


# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)



########## OLD VERSION OF readvboth ##########
# this version can take different sample numbers for each
# channel, turns out we don't ever actually need to do this
# so this version is long and complicted
        
def readvboth(no_samples1, no_samples2):
    # function to read and save as many datapoints (no_samples) as you like into 
    # an array. Difference is that this function simultaneously reads in to 2 arrays 
    # to capture the voltages from both channels instead of just channel one

    counter1 = 1
    counter2 = 1
    
    readvboth.no_samples1 = no_samples1
    readvboth.no_samples2 = no_samples2

    varray1 = np.zeros(no_samples1)
    varray2 = np.zeros(no_samples2)
    readvboth.varray1 = varray1
    readvboth.varray2 = varray2
    
    tarray1 = np.zeros(no_samples1)
    tarray2 = np.zeros(no_samples2)
    readvboth.tarray1 = tarray1
    readvboth.tarray2 = tarray2
    
    start = t.time()
    print("Start: " + str(start))
            
    while counter1 <= no_samples1 or counter2 <= no_samples2:

        if no_samples1 >= no_samples2 and counter2 <= no_samples2:
        
            varray1[counter1 - 1] = adcdac.read_adc_voltage(1, 0)
            varray2[counter2 - 1] = adcdac.read_adc_voltage(2, 0)
            tarray1[counter1 - 1] = t.time()
            tarray2[counter2 - 1] = t.time()
            counter1 = counter1 + 1
            counter2 = counter2 + 1 
           
        elif no_samples1 >= no_samples2 and counter1 <= no_samples1:
            
            varray1[counter1 - 1] = adcdac.read_adc_voltage(1, 0)
            tarray1[counter1 - 1] = t.time()
            counter1 = counter1 + 1

        elif no_samples2 >= no_samples1 and counter1 <= no_samples1:
            
            varray1[counter1 - 1] = adcdac.read_adc_voltage(1, 0)
            varray2[counter2 - 1] = adcdac.read_adc_voltage(2, 0)
            tarray1[counter1 - 1] = t.time()
            tarray2[counter2 - 1] = t.time()
            counter1 = counter1 + 1
            counter2 = counter2 + 1 
               
        elif no_samples2 >= no_samples1 and counter2 <= no_samples2:
            
            varray2[counter2 - 1] = adcdac.read_adc_voltage(2, 0)
            tarray2[counter2 - 1] = t.time()
            counter2 = counter2 + 1
               

    end = t.time()
    print("End: " + str(end))
    
    readvboth.totalseconds = end - start
    
    
    samplerate1 = no_samples1 / (tarray1[-1] - tarray1[0]) #samples per second
    samplerate2 = no_samples2 / (tarray2[-1] - tarray2[0]) #samples per second

    print("Time Elapsed Total= ", readvboth.totalseconds)    
    print("Samplerate1 = " + str(samplerate1))
    print("Samplerate2 = " + str(samplerate2))
    
    for i in range(len(tarray1)):
            tarray1[i]-=start
            
    for j in range(len(tarray2)):
            tarray2[j]-=start
