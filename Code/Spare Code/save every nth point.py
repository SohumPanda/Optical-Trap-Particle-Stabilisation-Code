from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt


# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)



# NEED TO CHECK ON FAST SD CARD IF ln FUNCTION FOR MATHS TO GET CORRECT SAMPLE RATE
# STILL GIVES CORRECT ACTUAL SAMPLE RATE WITH ADDED IF/ELSE  

def readvsr_n(channel, no_samples, input_samplerate, nth_point):
    # function to read and save as many datapoints as you like into an array
    # from channel 1 or 2
    # this function is with an adjustable sample rate
    
    # modified to save every nth value      
    
    counter = 1
    
    varray = []
    tarray = []
    #narray = []  #this is here just to check if every nth number is actually saved. IT WORKS
    
    ln = int(-0.04711*input_samplerate + 1307)  # where ln is loop number
        
    while counter <= no_samples:      
        v = adcdac.read_adc_voltage(channel, 0)
        t = ti.time()
        
        if counter%nth_point is 0:   # this saves every nth point
            varray.append(v)
            tarray.append(t)
            #narray.append(counter)
            counter = counter + 1
            for o in range(ln):
                1+1
        
        else:
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
        
    return tarray, varray, start, end#, narray#, samplerate



def readvbothsr_n(no_samples,input_samplerate,nth_point):
    # function to read and save as many datapoints as you like into 2 arrays
    # 1 for channel 1, and 1 for channel 2. Both channels take same number of readings
    # this function can only sample each channel at half the speed of a single channel
    # so at 2.5MHz with no math loop delay, each channel samples at 14.6 kHz 

    counter = 1
    
    varray1 = []
    varray2 = []
    tarray1 = []
    tarray2 = []
    #narray = []

    ln = int(-0.1357*input_samplerate + 1995)  # where ln is loop number
    #print(ln/2)

    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to volatages array
        v1 = adcdac.read_adc_voltage(1, 0)
        t1 = ti.time()
        v2 = adcdac.read_adc_voltage(2, 0)
        t2 = ti.time()
        
        if counter%nth_point is 0:   # this saves every nth point
            varray1.append(v1)
            tarray1.append(t1)
            varray2.append(v2)
            tarray2.append(t2)
            #narray.append(counter)
            counter = counter + 1
            for o in range(ln):
                1+1
        
        else:
            counter = counter + 1
            for o in range(ln):
                1+1
        

    start1 = tarray1[0]
    #print("Start: " + str(start))
    end1 = tarray1[-1]
    #print("End: " + str(end))
    start2 = tarray2[0]
    #print("Start: " + str(start))
    end2 = tarray2[-1]
    #print("End: " + str(end))
    
    totalseconds = end2 - start1
    
    samplerate1 = no_samples / (end1 - start1) #actual samples per second channel 1
    samplerate2 = no_samples / (end2 - start2) #actual samples per second channel 2

    #print("Time Elapsed Total= ", totalseconds)
    #print("No. Samples per Channel = ", no_samples)
    print("Actual Samplerate1 = " + str(samplerate1))
    print("Actual Samplerate2 = " + str(samplerate2))
    
    for i in range(len(tarray1)):
        tarray1[i]-=start1

    for j in range(len(tarray2)):
        tarray2[j]-=start2
            
    return tarray1, tarray2, varray1, varray2, start1, start2, end1, end2#, narray



def continuous_read(channel, no_samples, input_samplerate, nth_point, no_runs):  
   
   #func to loop readvsr for n number of runs
   #this func is for continuous reading from 1 channel     
   #no_runs is how many times we run readv().
    start = ti.time()
    savetimes = []
    starttimes = []
    endtimes = []
    counter = 1
    while counter<= no_runs:
        t,v,start,end = readvsr_n(channel, no_samples, input_samplerate, nth__point)
        #t,v,start,end = readv(channel, no_samples)
        data = np.column_stack((t,v))
        a = ti.time()
        #np.savetxt('batch'+str(counter), data, delimiter=',')
        np.save('batch'+str(counter), data)
        b = ti.time()
        c = b-a
        savetimes.append(c)
        starttimes.append(start)
        endtimes.append(end)
        counter+=1

    for i in range(len(starttimes)):
        starttimes[i]-=start

    for j in range(len(endtimes)):
        endtimes[j]-=start
        
    del starttimes[0] 
    del endtimes[-1]
    
    gapsarray = np.array(starttimes) - np.array(endtimes)
    gaps = gapsarray.tolist()
    
    #savetimes is a list of the times to save each batch
    #gaps is a list of the times between the last saved point in a batch and the first saved point in the next batch     
    return savetimes, gaps   



def continuous_readboth(no_samples, input_samplerate, nth_point, no_runs):
    
    counter = 1
    start = ti.time()
    savetimes = []
    starttimes1 = []
    endtimes1 = []
    starttimes2 = []
    endtimes2 = []
    while counter <= no_runs:
        t1,t2,v1,v2,s1,s2,e1,e2 = readvbothsr_n(no_samples, input_samplerate, nth_point)
        #t1,t2,v1,v2,s1,s2,e1,e2 = readvboth(no_samples) #this read func reads at the max possible sample rate
        data = np.column_stack((t1,t2,v1,v2))
        a = ti.time()
        #np.savetxt('batch'+str(counter), data, delimiter=',')
        np.save('batch'+str(counter), data)
        b = ti.time()
        c = b-a
        savetimes.append(c)
        starttimes1.append(s1)
        endtimes1.append(e1)
        starttimes2.append(s2)
        endtimes2.append(e2)
        counter+=1
    
    for i in range(len(starttimes1)):
        starttimes1[i]-=start
        starttimes2[i]-=start

    for j in range(len(endtimes1)):
        endtimes1[j]-=start
        endtimes2[j]-=start
        
    del starttimes1[0] 
    del endtimes1[-1]
    del starttimes2[0] 
    del endtimes2[-1]
    
    gapsarray1 = np.array(starttimes1) - np.array(endtimes1)
    gaps1 = gapsarray1.tolist()
    gapsarray2 = np.array(starttimes2) - np.array(endtimes2)
    gaps2 = gapsarray2.tolist()
    
    #savetimes is a list of the times to save each batch
    #gaps1 is a list of the times between the last saved point in a batch and the first saved point in the next batch for channel 1
    #gaps2 is a list of the times between the last saved point in a batch and the first saved point in the next batch for channel 2
    return savetimes, gaps1, gaps2
