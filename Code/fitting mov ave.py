import numpy as np
import matplotlib.pyplot as plt
from ADCDACPi import ADCDACPi
import time as ti

# create an instance of the ADCDAC Pi with a DAC gain set to 1 for 0 - 2.048 V, 2 for 0 - 3.3 V
adcdac = ADCDACPi(2)

# set the reference voltage.  this should be set to the exact voltage
# measured on the raspberry pi 3.3V rail.
adcdac.set_adc_refvoltage(3.3)



def moving_av(channel,ave_length,no_samples):
    averages = np.zeros(no_samples)
    times = np.zeros(no_samples)
    readings = np.zeros(ave_length)
    counter = 1
    x = np.arange(1,11,1) #this creates and array from 1 to 10 to acts as the x values for the fit
    
    while counter <= no_samples:
    
        channel = 1
        next_reading = adcdac.read_adc_voltage(channel, 0)
        readings = np.append(readings, next_reading)
        readings = np.delete(readings, 0)
        
        #fit the 10 most recent readings (where 10 = ave_length, can change this to be ny length we want)
        
        fit,cov = np.polyfit(x,readings,1, cov=True)
        fitplot = np.poly1d(fit)
        gradient = fit[0]
        
        if gradient <= 0:
            adcdac.set_dac_voltage(1, 0)
                
        else:
            adcdac.set_dac_voltage(1,1)
        
        
        avg = np.mean(readings)
        averages[counter - 1] = avg
        times[counter - 1] = ti.time()
        counter = counter + 1
                    
    start = times[0]
    end = times[-1]
        
    for i in range(len(times)):
        times[i]-=start

    return averages, times
    

av,ti = moving_av(1,10,10000)

plt.plot(ti[10:], av[10:], 'rx')
plt.show()
print((ti[-1] - ti[0])/10000)
