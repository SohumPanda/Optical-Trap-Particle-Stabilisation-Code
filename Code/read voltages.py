from ADCDACPi import ADCDACPi
import time as ti
import numpy as np
import matplotlib.pyplot as plt
from threading import Thread
#import pandas as pd

# NEED TO RETAKE ACTUAL SAMPLERATE SPEEDS VS NUMBER OF MATH LOOPS USING CONTINUOUS_READ AND REFIT GRAPHS

# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)

#z = 1.02943288
#z = 1
z = 1.1255542576995787 #scaling factor for 1.3 W used for particle aa
#z = 1
#z = 1.1442367821323516
#z = 1.0793766413340333 # scaling factor for 1.0

# this is the number we need to multiply channel 2 by to have both channels read the same value
# when no light is getting in to the PSD
# Therefore when particle is in middle of PSD, both channels should read same val

def readv(channel, no_samples):
    # function to read and save as many datapoints as you like into an array
    # from channel 1 or 2
    # no adjustable sample rate, just goes as fast as it can 
    
    counter = 1
    
    varray = np.zeros(no_samples)
    tarray = np.zeros(no_samples)

    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to voltages array
        varray[counter - 1] = adcdac.read_adc_voltage(channel, 0)
        tarray[counter - 1] = ti.time()        
        counter = counter + 1
        #t.sleep()

    start = tarray[0]
    #print("Start: " + str(start))
    end = tarray[-1]
    #print("End: " + str(end))
    
    totalseconds = end - start
    samplerate = no_samples / totalseconds #actual samples per second

    #print("Time Elapsed = ", totalseconds)
    #print("No. Samples per Channel = ", no_samples)
    print("Actual Samplerate = " + str(samplerate))
    
    for i in range(len(tarray)):
        tarray[i]-=start
    
    tarray = tarray.astype('float32')
    varray = varray.astype('float32')
    
    return tarray, varray, start, end



def readvsr(channel, no_samples, input_samplerate):
    # function to read and save as many datapoints as you like into an array
    # from channel 1 or 2
    # this function is with an adjustable sample rate
    
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
        
    tarray = tarray.astype('float32')
    varray = varray.astype('float32')
        
    return tarray, varray, start, end#, samplerate



def readvboth(no_samples):
    # function to read and save as many datapoints as you like into 2 arrays
    # 1 for channel 1, and 1 for channel 2. Both channels take same number of readings 

    counter = 1
    
    varray1 = np.zeros(no_samples)
    varray2 = np.zeros(no_samples)

    tarray1 = np.zeros(no_samples)
    tarray2 = np.zeros(no_samples)
    
    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to volatages array
        varray1[counter - 1] = adcdac.read_adc_voltage(1, 0)
        tarray1[counter - 1] = ti.time()
        varray2[counter - 1] = adcdac.read_adc_voltage(2, 0)
        tarray2[counter - 1] = ti.time()
        counter = counter + 1
        #t.sleep()

    start1 = tarray1[0]
    #print("Start: " + str(start))
    end1 = tarray1[-1]
    #print("End: " + str(end))
    start2 = tarray2[0]
    #print("Start: " + str(start))
    end2 = tarray2[-1]
    #print("End: " + str(end))
    
    
    samplerate1 = no_samples / (tarray1[-1] - tarray1[0]) #actual samples per second channel 1
    samplerate2 = no_samples / (tarray2[-1] - tarray2[0]) #actual samples per second channel 2


    print("Actual Samplerate1 = " + str(samplerate1))
    print("Actual Samplerate2 = " + str(samplerate2))
    
    for i in range(len(tarray1)):
        tarray1[i]-=start1

    for j in range(len(tarray2)):
        tarray2[j]-=start2
        
    tarray1 = tarray1.astype('float32')
    tarray2 = tarray2.astype('float32')
    varray1 = varray1.astype('float32')
    varray2 = varray2.astype('float32') 
     
    return tarray1, tarray2, varray1, z*varray2, start1, start2, end1, end2
           
           
            
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

    ln = int(-0.1357*input_samplerate + 1995)  # where ln is loop number
    #print(ln/2)

    while counter <= no_samples:
        # read the voltage from channel 1 and apppend to volatages array
        varray1[counter - 1] = adcdac.read_adc_voltage(1, 0)
        tarray1[counter - 1] = ti.time()
        varray2[counter - 1] = adcdac.read_adc_voltage(2, 0)
        tarray2[counter - 1] = ti.time()
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
    
    
    samplerate1 = no_samples / (end1 - start1) #actual samples per second channel 1
    samplerate2 = no_samples / (end2 - start2) #actual samples per second channel 2


    print("Actual Samplerate1 = " + str(samplerate1))
    print("Actual Samplerate2 = " + str(samplerate2))
    
    for i in range(len(tarray1)):
        tarray1[i]-=start1

    for j in range(len(tarray2)):
        tarray2[j]-=start2
        
    tarray1 = tarray1.astype('float32')
    tarray2 = tarray2.astype('float32')
    varray1 = varray1.astype('float32')
    varray2 = varray2.astype('float32')
    
    print(np.mean(varray1))
    print(np.std(varray1))
    print(np.mean(z*varray2))
    print(np.std(z*varray2))
            
    return tarray1, tarray2, varray1, z*varray2, start1, start2, end1, end2



def continuous_read(channel, no_samples, input_samplerate, no_runs):  
   
   #func to loop readvsr for n number of runs
   #this func is for continuous reading from 1 channel     
   #no_runs is how many times we run readv().
    start = ti.time()
    savetimes = []
    starttimes = []
    endtimes = []
    counter = 1
    while counter<= no_runs:
        t,v,start,end = readvsr(channel, no_samples, input_samplerate)
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
    gaps.append(0)
    
    #savetimes is a list of the times to save each batch
    #gaps is a list of the times between the last saved point in a batch and the first saved point in the next batch     
    st_and_gaps = np.column_stack((savetimes,gaps))
    np.savetxt('savetimes_and_gaps', st_and_gaps, delimiter=',')
    
    return savetimes, gaps   



def continuous_readboth(no_samples, input_samplerate, no_runs):
    
    counter = 1
    start = ti.time()
    savetimes = []
    starttimes1 = []
    endtimes1 = []
    starttimes2 = []
    endtimes2 = []
    print('start')
    while counter<= no_runs:
        t1,t2,v1,v2,s1,s2,e1,e2 = readvbothsr(no_samples, input_samplerate) #s1,e1,s2,e2 are the start and end times for the readings in channels 1 and 2 
        #t1,t2,v1,v2,s1,s2,e1,e2 = readvboth(no_samples) #this read func reads at the max possible sample rate
        data = np.column_stack((t1,t2,v1,v2))
        a = ti.time()
        #np.savetxt('batch'+str(counter), data, delimiter=',')
        np.save('batch'+str(counter), data)
        #np.savetxt('/media/pi/06A879EAA879D89F/batch'+str(counter), data, delimiter=',') #saving to external SSD
        #np.save('/media/pi/06A879EAA879D89F/batch'+str(counter), data) #saving to external SSD
        #df = pd.DataFrame(data)
        #df.to_pickle(str(counter)+'batch.pkl')
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
    gaps1.append(0)
    gapsarray2 = np.array(starttimes2) - np.array(endtimes2)
    gaps2 = gapsarray2.tolist()
    gaps2.append(0)
    
    #savetimes is a list of the times to save each batch
    #gaps1 is a list of the times between the last saved point in a batch and the first saved point in the next batch for channel 1
    #gaps2 is a list of the times between the last saved point in a batch and the first saved point in the next batch for channel 2
    st_and_gaps = np.column_stack((savetimes,gaps1,gaps2))
    np.savetxt('savetimes_and_gaps', st_and_gaps, delimiter=',')
    print('end')
    
    return savetimes, gaps1, gaps2
             
class squarewave():
    
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):        
        while self._running:
            adcdac.set_dac_voltage(1, 2)  # set the voltage on channel 1 to 1.5V
            ti.sleep(7)  # wait 0.5 seconds
            adcdac.set_dac_voltage(1, 0)  # set the voltage on channel 1 to 0V
            ti.sleep(7)  # wait 0.5 seconds
            #freq = 1/(2*sleeptime)
            
class loop():
    
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
    
    def run(self):
        st,g1,g2 = continuous_readboth(100000,11500,1)

class demosin():
    #this produces a 100Hz sine wave
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
         
        adcdac = ADCDACPi(1)

        sinewave_array = \
            [2048, 2073, 2098, 2123, 2148, 2174, 2199, 2224,
             2249, 2274, 2299, 2324, 2349, 2373, 2398, 2423,
             2448, 2472, 2497, 2521, 2546, 2570, 2594, 2618,
             2643, 2667, 2690, 2714, 2738, 2762, 2785, 2808,
             2832, 2855, 2878, 2901, 2924, 2946, 2969, 2991,
             3013, 3036, 3057, 3079, 3101, 3122, 3144, 3165,
             3186, 3207, 3227, 3248, 3268, 3288, 3308, 3328,
             3347, 3367, 3386, 3405, 3423, 3442, 3460, 3478,
             3496, 3514, 3531, 3548, 3565, 3582, 3599, 3615,
             3631, 3647, 3663, 3678, 3693, 3708, 3722, 3737,
             3751, 3765, 3778, 3792, 3805, 3817, 3830, 3842,
             3854, 3866, 3877, 3888, 3899, 3910, 3920, 3930,
             3940, 3950, 3959, 3968, 3976, 3985, 3993, 4000,
             4008, 4015, 4022, 4028, 4035, 4041, 4046, 4052,
             4057, 4061, 4066, 4070, 4074, 4077, 4081, 4084,
             4086, 4088, 4090, 4092, 4094, 4095, 4095, 4095,
             4095, 4095, 4095, 4095, 4094, 4092, 4090, 4088,
             4086, 4084, 4081, 4077, 4074, 4070, 4066, 4061,
             4057, 4052, 4046, 4041, 4035, 4028, 4022, 4015,
             4008, 4000, 3993, 3985, 3976, 3968, 3959, 3950,
             3940, 3930, 3920, 3910, 3899, 3888, 3877, 3866,
             3854, 3842, 3830, 3817, 3805, 3792, 3778, 3765,
             3751, 3737, 3722, 3708, 3693, 3678, 3663, 3647,
             3631, 3615, 3599, 3582, 3565, 3548, 3531, 3514,
             3496, 3478, 3460, 3442, 3423, 3405, 3386, 3367,
             3347, 3328, 3308, 3288, 3268, 3248, 3227, 3207,
             3186, 3165, 3144, 3122, 3101, 3079, 3057, 3036,
             3013, 2991, 2969, 2946, 2924, 2901, 2878, 2855,
             2832, 2808, 2785, 2762, 2738, 2714, 2690, 2667,
             2643, 2618, 2594, 2570, 2546, 2521, 2497, 2472,
             2448, 2423, 2398, 2373, 2349, 2324, 2299, 2274,
             2249, 2224, 2199, 2174, 2148, 2123, 2098, 2073,
             2048, 2023, 1998, 1973, 1948, 1922, 1897, 1872,
             1847, 1822, 1797, 1772, 1747, 1723, 1698, 1673,
             1648, 1624, 1599, 1575, 1550, 1526, 1502, 1478,
             1453, 1429, 1406, 1382, 1358, 1334, 1311, 1288,
             1264, 1241, 1218, 1195, 1172, 1150, 1127, 1105,
             1083, 1060, 1039, 1017, 995, 974, 952, 931,
             910, 889, 869, 848, 828, 808, 788, 768,
             749, 729, 710, 691, 673, 654, 636, 618,
             600, 582, 565, 548, 531, 514, 497, 481,
             465, 449, 433, 418, 403, 388, 374, 359,
             345, 331, 318, 304, 291, 279, 266, 254,
             242, 230, 219, 208, 197, 186, 176, 166,
             156, 146, 137, 128, 120, 111, 103, 96,
             88, 81, 74, 68, 61, 55, 50, 44,
             39, 35, 30, 26, 22, 19, 15, 12,
             10, 8, 6, 4, 2, 1, 1, 0,
             0, 0, 1, 1, 2, 4, 6, 8,
             10, 12, 15, 19, 22, 26, 30, 35,
             39, 44, 50, 55, 61, 68, 74, 81,
             88, 96, 103, 111, 120, 128, 137, 146,
             156, 166, 176, 186, 197, 208, 219, 230,
             242, 254, 266, 279, 291, 304, 318, 331,
             345, 359, 374, 388, 403, 418, 433, 449,
             465, 481, 497, 514, 531, 548, 565, 582,
             600, 618, 636, 654, 673, 691, 710, 729,
             749, 768, 788, 808, 828, 848, 869, 889,
             910, 931, 952, 974, 995, 1017, 1039, 1060,
             1083, 1105, 1127, 1150, 1172, 1195, 1218, 1241,
             1264, 1288, 1311, 1334, 1358, 1382, 1406, 1429,
             1453, 1478, 1502, 1526, 1550, 1575, 1599, 1624,
             1648, 1673, 1698, 1723, 1747, 1772, 1797, 1822,
             1847, 1872, 1897, 1922, 1948, 1973, 1998, 2023]

        while True:
            for val in sinewave_array:
                adcdac.set_dac_raw(1, val)
                #ti.sleep(0.001)


def sine(time,amplitude,frequency,phase,offset):
    wave = amplitude*(np.sin(time*2*np.pi*frequency + phase)) + offset
    return wave

class sin():

    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
        
        N = 400
        f = 1
        t = np.linspace(0,1/f,N)
        wave = sine(t,1,f,0,1) 
        
        while True:
            for val in wave:
                adcdac.set_dac_voltage(1,val)

tvsw = squarewave()
tvswthread = Thread(target=tvsw.run)
tvswthread.start()

#sin_x = sin()
#sin_xthread = Thread(target=sin_x.run)
#sin_xthread.start()

batch = loop()
batchthread = Thread(target=batch.run)
batchthread.start()


#st,g1,g2 = continuous_readboth(100000,10500,10)


#t1,t2,v1,v2,s1,s2,e1,e2 = readvbothsr(1000, 10000)
#continuous_readboth(100000,10000)
#st,g = continuous_read(1,1000,25000,4)
#st,g1,g2 = continuous_readboth(1000,25000,4) #st = savetimes list, g1 and g2 = gaps1 and gaps2 lists
#st,g1,g2 = continuous_readboth(100000,10100,10)
#t,v,s,e = readv(1,100000)

#PRE BUS speed messing around 
#for readv1 and readv2 individually, sample rate at 19.5 kHz for 100,000 samples
#for readvboth, as reading two channels at once,
#takes double the time and sample rate on each channel is 9.8 kHz

#POST BUS messing around
#need a copy of ADCDACPi.py in the same folder as this file
#adjusted ADC bus speed up from 20 mil to 50 mil
#seems like going higher doesn't make a difference
#improves 1 channel sample rate to 39 kHz for 100,000 samples
#for reading both channels simultaneously, each with 100,000 samples
#each channel sample rate is 19.9 kHz



 



